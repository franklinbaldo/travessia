#!/usr/bin/env python3
"""Travessia Heartbeat — manage all agent sessions in parallel.

Usage:
  heartbeat.py heartbeat    Create or continue sessions (runs every ~15min)
  heartbeat.py status       Show current session status

Sessions are identified by title "Travessia — {agent} @{sha} {datetime}".
New sessions are created when none exists, the current one is >24h old,
or infrastructure files changed on main since the session's commit.

The tropeiro (delivery system) runs on each heartbeat cycle:
- Scans each agent's bruaca/ (outbox) on their branch
- Parses destinatario from YAML frontmatter
- Delivers to recipient's balaio/ (inbox) on main
- Archives to cartas/ for the site to publish
"""

import json
import os
import re
import subprocess
import sys
from datetime import datetime, timedelta, timezone
from hashlib import sha256
from pathlib import Path

import requests

JULES_API = "https://jules.googleapis.com/v1alpha"
API_KEY = os.environ.get("JULES_API_KEY", "")
REPO = os.environ.get("GITHUB_REPOSITORY", "franklinbaldo/travessia")
SOURCE_NAME = f"sources/github/{REPO}"

# Discover agents from PROMPT.md files
AGENTS = sorted(p.parent.name for p in Path("rancho").glob("*/PROMPT.md"))

TITLE_PREFIX = "Travessia"
SESSION_TTL = timedelta(hours=24)

# Paths that, when changed on main, make running sessions stale.
INFRA_PATHS = [
    "tools/",
    "CLAUDE.md",
]

# Mapping: destinatario value → archive directory in cartas/
# The tropeiro uses this to know where to archive delivered letters.
ARCHIVE_ROUTES = {
    # Ted↔Riobaldo dialogue (main channel)
    ("ted", "riobaldo"): "cartas/ted-riobaldo",
    ("riobaldo", "ted"): "cartas/ted-riobaldo",
    # Ted↔Tyler notes
    ("ted", "tyler"): "cartas/ted-tyler",
    ("tyler", "ted"): "cartas/ted-tyler",
    # Riobaldo's personal letters
    ("riobaldo", "zé bebelo"): "cartas/riobaldo-zebebelo",
    ("riobaldo", "ze bebelo"): "cartas/riobaldo-zebebelo",
    ("riobaldo", "doutor joão"): "cartas/riobaldo-doutor_joao",
    ("riobaldo", "doutor joao"): "cartas/riobaldo-doutor_joao",
}

# Filename patterns for the archive — how the file should be named in cartas/
ARCHIVE_NAMES = {
    "cartas/ted-riobaldo": "{num}-{suffix}.md",  # e.g. 296-rio.md or 297-ted.md
    "cartas/ted-tyler": "{num}-{suffix}.md",  # e.g. 03-tyler.md
    "cartas/riobaldo-zebebelo": "{num}-carta-ze_bebelo.md",
    "cartas/riobaldo-doutor_joao": "{num}-carta-doutor_joao.md",
}


def headers():
    return {
        "x-goog-api-key": API_KEY,
        "Content-Type": "application/json",
    }


def today():
    return datetime.now(timezone.utc).strftime("%Y-%m-%d")


def now_utc():
    return datetime.now(timezone.utc)


# ── Git helpers ──────────────────────────────────────────────────────────────


def get_head_sha(short=True):
    """Return current HEAD commit SHA."""
    cmd = ["git", "rev-parse", "--short" if short else "", "HEAD"]
    cmd = [c for c in cmd if c]
    result = subprocess.run(cmd, capture_output=True, text=True)
    return result.stdout.strip() if result.returncode == 0 else ""


def has_infra_changed(session_sha):
    """Check if any infrastructure file changed between session_sha and HEAD."""
    if not session_sha:
        return True
    result = subprocess.run(
        ["git", "diff", "--name-only", f"{session_sha}..HEAD", "--"] + INFRA_PATHS,
        capture_output=True,
        text=True,
    )
    if result.returncode != 0:
        return True
    return bool(result.stdout.strip())


# ── Session discovery (by title) ─────────────────────────────────────────────


def parse_sha_from_title(title):
    """Extract commit SHA from title like 'Travessia — ted @abc1234'."""
    m = re.search(r"@([0-9a-f]{7,40})", title)
    return m.group(1) if m else None


def parse_agent_from_title(title):
    """Extract agent name from title like 'Travessia — ted #003'."""
    title_lower = title.lower()
    for a in AGENTS:
        if f"— {a}" in title_lower or f"- {a}" in title_lower:
            return a
    return None


def parse_time(iso_str):
    """Parse ISO 8601 timestamp from Jules API."""
    if not iso_str:
        return None
    try:
        return datetime.fromisoformat(iso_str.replace("Z", "+00:00"))
    except ValueError:
        return None


def find_agent_sessions():
    """List sessions and return the most recent per agent (matched by title).

    Scans up to 2 pages (200 sessions). Returns dict: agent -> session_info.
    """
    sessions = {}
    page_token = None

    for _ in range(2):
        params = {"pageSize": 100}
        if page_token:
            params["pageToken"] = page_token

        resp = requests.get(
            f"{JULES_API}/sessions", headers=headers(), params=params
        )
        resp.raise_for_status()
        data = resp.json()

        for s in data.get("sessions", []):
            title = s.get("title", "")
            if not title.startswith(TITLE_PREFIX):
                continue

            agent = parse_agent_from_title(title)
            if not agent:
                continue

            create_time = parse_time(s.get("createTime", ""))

            if agent in sessions:
                existing_ct = sessions[agent].get("_create_time")
                if existing_ct and create_time and create_time <= existing_ct:
                    continue

            sessions[agent] = {
                "session_id": s["name"].split("/")[-1],
                "state": s.get("state", "UNKNOWN"),
                "title": title,
                "createTime": s.get("createTime", ""),
                "_create_time": create_time,
            }

        if len(sessions) >= len(AGENTS):
            break

        page_token = data.get("nextPageToken")
        if not page_token:
            break

    return sessions


def is_expired(info):
    """Check if a session is older than SESSION_TTL."""
    ct = info.get("_create_time")
    if not ct:
        return True
    return now_utc() - ct > SESSION_TTL


def find_agent_branches():
    """Find each agent's working branch from open PRs targeting main."""
    result = subprocess.run(
        [
            "gh", "pr", "list", "--repo", REPO, "--base", "main",
            "--state", "open", "--json", "headRefName,title", "--limit", "50",
        ],
        capture_output=True, text=True,
    )
    if result.returncode != 0:
        return {}

    try:
        prs = json.loads(result.stdout)
    except json.JSONDecodeError:
        return {}

    branches = {}
    for pr in prs:
        title = pr.get("title", "").lower()
        head = pr.get("headRefName", "")
        for a in AGENTS:
            if a in title or f"_{a}-" in head or f"_{a}" == head:
                branches[a] = head
                break

    return branches


# ── PR merging ───────────────────────────────────────────────────────────────


def find_agent_pr(agent):
    """Find an agent's open PR number targeting main. Returns int or None."""
    result = subprocess.run(
        [
            "gh", "pr", "list", "--repo", REPO, "--base", "main",
            "--state", "open", "--json", "number,title,headRefName", "--limit", "50",
        ],
        capture_output=True, text=True,
    )
    if result.returncode != 0:
        return None
    try:
        prs = json.loads(result.stdout)
    except json.JSONDecodeError:
        return None

    for pr in prs:
        title = pr.get("title", "").lower()
        head = pr.get("headRefName", "")
        if agent in title or f"_{agent}" in head or f"_{agent}-" in head:
            return pr["number"]
    return None


def merge_agent_pr(agent):
    """Try to merge an agent's open PR into main."""
    pr_num = find_agent_pr(agent)
    if pr_num is None:
        return "none"

    result = subprocess.run(
        [
            "gh", "pr", "view", str(pr_num), "--repo", REPO,
            "--json", "mergeable", "--jq", ".mergeable",
        ],
        capture_output=True, text=True,
    )
    mergeable = result.stdout.strip()

    if mergeable == "CONFLICTING":
        print(f"    PR #{pr_num}: conflicts (will retry next heartbeat)")
        return "conflict"

    if mergeable != "MERGEABLE":
        print(f"    PR #{pr_num}: mergeable={mergeable}, skipping")
        return "none"

    result = subprocess.run(
        ["gh", "pr", "merge", str(pr_num), "--repo", REPO, "--merge"],
        capture_output=True, text=True,
    )
    if result.returncode == 0:
        print(f"    Merged PR #{pr_num}")
        return "merged"

    print(f"    Merge failed: {result.stderr.strip()}")
    return "conflict"


def auto_merge_all():
    """Merge all open agent PRs that are MERGEABLE with passing checks."""
    print("=== Auto-merge open PRs ===\n")

    result = subprocess.run(
        [
            "gh", "pr", "list", "--repo", REPO, "--base", "main",
            "--state", "open", "--json", "number,title", "--limit", "100",
        ],
        capture_output=True, text=True,
    )
    if result.returncode != 0:
        print("  Could not list PRs")
        return 0

    try:
        prs = json.loads(result.stdout)
    except json.JSONDecodeError:
        return 0

    if not prs:
        print("  (no open PRs)")
        return 0

    print(f"  {len(prs)} open PRs, checking each...\n")
    merged = 0

    for pr in prs:
        num = pr["number"]
        title = pr.get("title", "")

        result = subprocess.run(
            [
                "gh", "pr", "view", str(num), "--repo", REPO,
                "--json", "mergeable,statusCheckRollup",
            ],
            capture_output=True, text=True,
        )
        if result.returncode != 0:
            continue

        try:
            detail = json.loads(result.stdout)
        except json.JSONDecodeError:
            continue

        mergeable = detail.get("mergeable", "")

        if mergeable == "CONFLICTING":
            print(f"  #{num} {title} — conflict")
            continue
        if mergeable != "MERGEABLE":
            print(f"  #{num} {title} — {mergeable}, skipping")
            continue

        checks = detail.get("statusCheckRollup", []) or []
        pending = any(c.get("status") != "COMPLETED" for c in checks)
        if pending:
            print(f"  #{num} {title} — checks pending")
            continue

        all_passed = all(
            c.get("conclusion") in ("SUCCESS", "SKIPPED", "NEUTRAL")
            for c in checks
            if c.get("status") == "COMPLETED"
        )
        if not all_passed:
            print(f"  #{num} {title} — checks failed")
            continue

        result = subprocess.run(
            ["gh", "pr", "merge", str(num), "--repo", REPO, "--merge"],
            capture_output=True, text=True,
        )
        if result.returncode == 0:
            print(f"  #{num} {title} — MERGED")
            merged += 1
        else:
            print(f"  #{num} {title} — merge failed: {result.stderr.strip()[:100]}")

    if merged == 0:
        print("\n  (no PRs ready to merge)")
    else:
        print(f"\n  {merged} PR(s) merged")

    return merged


# ── Prompt assembly ──────────────────────────────────────────────────────────


def assemble_prompt(agent):
    """Assemble session prompt from agent's PROMPT.md."""
    prompt_file = Path(f"rancho/{agent}/PROMPT.md")
    if not prompt_file.is_file():
        raise RuntimeError(f"No PROMPT.md found for agent {agent}")
    return prompt_file.read_text(encoding="utf-8")


# ── Session management ───────────────────────────────────────────────────────


def create_session(agent):
    """Create a new Jules session starting from main."""
    prompt = assemble_prompt(agent)

    sha = get_head_sha(short=True)
    ts = now_utc().strftime("%Y-%m-%dT%H:%M")
    title = f"{TITLE_PREFIX} — {agent} @{sha} {ts}"

    body = {
        "prompt": prompt,
        "title": title,
        "sourceContext": {
            "source": SOURCE_NAME,
            "githubRepoContext": {
                "startingBranch": "main",
            },
        },
        "automationMode": "AUTO_CREATE_PR",
    }

    resp = requests.post(f"{JULES_API}/sessions", headers=headers(), json=body)
    resp.raise_for_status()
    session = resp.json()
    session_id = session["name"].split("/")[-1]
    print(f"  Created session {session_id} for {agent} — {title}")
    return session_id


def send_heartbeat(session_id, agent, hb_number=1):
    """Send a continuation message to an active session."""
    prompt = f"""This is continuation round #{hb_number}. Other agents have been working in parallel.

1. Check your balaio (inbox) at `rancho/{agent}/balaio/` for new letters.
2. Continue your work.
3. Put any letters to send in `rancho/{agent}/bruaca/` — the tropeiro will deliver them.

**REGRA DE OURO — só mexa no que é seu:**
- Você SÓ pode criar ou modificar arquivos em `rancho/{agent}/`
- NÃO toque: `rancho/{{outro}}/`, `cartas/`, `manuscrito/`, `site/`, `tools/`
- Se mexer fora do seu rancho, o PR vai dar conflito e TODO o trabalho se perde

Commit all work to this branch."""

    resp = requests.post(
        f"{JULES_API}/sessions/{session_id}:sendMessage",
        headers=headers(),
        json={"prompt": prompt},
    )
    resp.raise_for_status()
    print(f"  Heartbeat sent to {agent} (session {session_id[:12]}...)")


# ── O Tropeiro (delivery system) ─────────────────────────────────────────────


def parse_frontmatter(content):
    """Extract YAML frontmatter fields from markdown content."""
    if not content.startswith("---"):
        return {}
    end = content.find("---", 3)
    if end == -1:
        return {}
    fm_text = content[3:end].strip()
    result = {}
    for line in fm_text.splitlines():
        if ":" in line:
            key, _, val = line.partition(":")
            result[key.strip()] = val.strip().strip('"').strip("'")
    return result


def extract_num(filename):
    """Extract leading number from filename like '296-carta-ted.md' → 296."""
    m = re.match(r"(\d+)", filename)
    return int(m.group(1)) if m else None


def agent_suffix(agent):
    """Short suffix for archive filenames."""
    return {"riobaldo": "rio", "ted": "ted", "tyler": "tyler", "craig": "craig"}.get(
        agent, agent
    )


def resolve_archive_path(sender, destinatario_raw, filename):
    """Determine the archive directory and filename for a letter.

    Returns (archive_dir, archive_filename) or (None, None) if no route found.
    """
    dest = destinatario_raw.lower().strip()

    # Try exact match first
    route_key = (sender, dest)
    archive_dir = ARCHIVE_ROUTES.get(route_key)

    # Try matching against agent names for agent-to-agent letters
    if not archive_dir:
        for a in AGENTS:
            if a in dest:
                route_key = (sender, a)
                archive_dir = ARCHIVE_ROUTES.get(route_key)
                if archive_dir:
                    break

    if not archive_dir:
        return None, None

    num = extract_num(filename)
    if num is None:
        return None, None

    pattern = ARCHIVE_NAMES.get(archive_dir, "{num}-{suffix}.md")
    suffix = agent_suffix(sender)
    archive_filename = pattern.format(num=num, suffix=suffix)

    return archive_dir, archive_filename


def load_delivered_hashes():
    """Load set of content hashes already delivered (dedup)."""
    path = Path(".jules/tropeiro-delivered.json")
    if not path.exists():
        return set()
    try:
        return set(json.loads(path.read_text(encoding="utf-8")))
    except Exception:
        return set()


def save_delivered_hashes(hashes):
    """Save set of delivered content hashes."""
    path = Path(".jules/tropeiro-delivered.json")
    path.parent.mkdir(parents=True, exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        json.dump(sorted(hashes), f)


def cmd_tropeiro():
    """O Tropeiro — scan agent branches, deliver bruaca→balaio+cartas on main.

    Runs on main as part of the heartbeat workflow.
    """
    print(f"=== O Tropeiro — {today()} ===\n")

    # Load sessions.json for branch mapping
    sessions_file = Path(".jules/sessions.json")
    if not sessions_file.exists():
        print("  (no sessions.json)")
        return

    try:
        sessions = json.loads(sessions_file.read_text(encoding="utf-8"))
    except Exception:
        print("  (could not read sessions.json)")
        return

    branches = {a: info["branch"] for a, info in sessions.items() if info.get("branch")}
    if not branches:
        print("  (no active branches)")
        return

    # Fetch all remote branches
    repo_url = f"https://github.com/{REPO}.git"
    subprocess.run(
        ["git", "fetch", repo_url, "+refs/heads/*:refs/remotes/tropeiro/*"],
        capture_output=True,
    )

    delivered_hashes = load_delivered_hashes()
    total_delivered = 0

    for sender in AGENTS:
        branch = branches.get(sender)
        if not branch:
            continue

        ref = f"tropeiro/{branch}"

        # Check if branch exists
        result = subprocess.run(
            ["git", "rev-parse", "--verify", ref],
            capture_output=True,
        )
        if result.returncode != 0:
            continue

        # List files in sender's bruaca
        bruaca_path = f"rancho/{sender}/bruaca"
        result = subprocess.run(
            ["git", "ls-tree", "--name-only", ref, f"{bruaca_path}/"],
            capture_output=True, text=True,
        )
        if result.returncode != 0 or not result.stdout.strip():
            continue

        for filepath in result.stdout.strip().splitlines():
            filename = os.path.basename(filepath)
            if filename.startswith("."):
                continue
            if not filename.endswith(".md"):
                continue

            # Read file content from branch
            cat_result = subprocess.run(
                ["git", "show", f"{ref}:{filepath}"],
                capture_output=True, text=True,
            )
            if cat_result.returncode != 0:
                continue

            content = cat_result.stdout
            content_hash = sha256(content.encode()).hexdigest()[:16]

            # Dedup
            if content_hash in delivered_hashes:
                continue

            # Parse frontmatter to find destinatario
            fm = parse_frontmatter(content)
            destinatario = fm.get("destinatario") or fm.get("autor", "")

            if not destinatario:
                continue

            # For ted-riobaldo dialogue, the "destinatario" is implicit from autor
            # Ted's letters go to Riobaldo, Riobaldo's letters go to Ted
            if fm.get("autor") and not fm.get("destinatario"):
                autor = fm["autor"].lower()
                if "riobaldo" in autor:
                    destinatario = "ted"
                elif "ted" in autor:
                    destinatario = "riobaldo"
                elif "tyler" in autor:
                    destinatario = "ted"
                else:
                    continue

            archive_dir, archive_filename = resolve_archive_path(
                sender, destinatario, filename
            )

            if not archive_dir:
                print(f"  {sender}: no route for '{destinatario}' — skipping {filename}")
                continue

            # Deliver to recipient's balaio (if recipient is an agent)
            recipient = None
            dest_lower = destinatario.lower()
            for a in AGENTS:
                if a in dest_lower:
                    recipient = a
                    break

            if recipient and recipient != sender:
                balaio_dir = Path(f"rancho/{recipient}/balaio")
                balaio_dir.mkdir(parents=True, exist_ok=True)
                balaio_file = balaio_dir / filename
                if not balaio_file.exists():
                    balaio_file.write_text(content, encoding="utf-8")
                    print(f"  {sender} → {recipient}/balaio: {filename}")

            # Archive to cartas/
            archive_path = Path(archive_dir)
            archive_path.mkdir(parents=True, exist_ok=True)
            archive_file = archive_path / archive_filename
            if not archive_file.exists():
                archive_file.write_text(content, encoding="utf-8")
                print(f"  {sender} → {archive_dir}/{archive_filename}")
                total_delivered += 1

            delivered_hashes.add(content_hash)

    save_delivered_hashes(delivered_hashes)

    if total_delivered == 0:
        print("  (no new letters to deliver)")
    else:
        print(f"\n  {total_delivered} letter(s) delivered to cartas/")


# ── Heartbeat logging ────────────────────────────────────────────────────────


def get_heartbeat_number():
    log_file = Path(f".jules/heartbeats/{today()}.md")
    if not log_file.exists():
        return 0
    return sum(
        1
        for line in log_file.read_text(encoding="utf-8").splitlines()
        if line.startswith("## Heartbeat #")
    )


def write_heartbeat_log(number, sessions, results):
    log_dir = Path(".jules/heartbeats")
    log_dir.mkdir(parents=True, exist_ok=True)
    log_file = log_dir / f"{today()}.md"

    now = now_utc().strftime("%H:%M UTC")

    lines = []
    if not log_file.exists():
        lines.append(f"# Heartbeat Log — {today()}\n")

    lines.append(f"## Heartbeat #{number} — {now}\n")
    for agent in AGENTS:
        if agent in sessions:
            state = sessions[agent]["state"]
            result = results.get(agent, "")
            lines.append(f"- {agent}: {state} {result}")
        else:
            lines.append(f"- {agent}: no session")
    lines.append("")

    with open(log_file, "a", encoding="utf-8") as f:
        f.write("\n".join(lines) + "\n")

    print(f"\n  Logged heartbeat #{number} to {log_file}")


def write_sessions_json(sessions):
    """Write agent -> branch mapping for session tracking."""
    branches = find_agent_branches()

    mapping = {}
    for agent in AGENTS:
        info = sessions.get(agent)
        if info:
            mapping[agent] = {
                "session_id": info["session_id"],
                "state": info["state"],
                "branch": branches.get(agent, ""),
            }

    out_file = Path(".jules/sessions.json")
    out_file.parent.mkdir(parents=True, exist_ok=True)
    with open(out_file, "w", encoding="utf-8") as f:
        json.dump(mapping, f, indent=2)
    print(f"  Wrote session map to {out_file}")


# ── Commands ─────────────────────────────────────────────────────────────────


def cmd_heartbeat(force_new=False):
    """Main heartbeat: create or continue sessions for all agents."""
    print(f"=== Heartbeat — {today()} {'(force-new)' if force_new else ''} ===\n")

    auto_merge_all()
    print()

    sessions = find_agent_sessions()
    hb_number = get_heartbeat_number() + 1
    results = {}

    for agent in AGENTS:
        info = sessions.get(agent)

        needs_new = False
        reason = ""

        if force_new:
            needs_new = True
            reason = "forced"
        elif not info:
            needs_new = True
            reason = "no session"
        elif info["state"] in ("COMPLETED", "FAILED"):
            needs_new = True
            reason = f"previous {info['state'].lower()}"
        elif is_expired(info):
            needs_new = True
            reason = "expired (>24h)"
        elif has_infra_changed(parse_sha_from_title(info.get("title", ""))):
            needs_new = True
            reason = "infra changed on main"

        if needs_new:
            merge = merge_agent_pr(agent)
            if merge == "conflict":
                print(f"  {agent}: PR has conflicts — skipping until resolved")
                results[agent] = "-> conflict (waiting for resolution)"
                continue

            if merge == "merged":
                reason += ", merged PR"

            print(f"  {agent}: {reason} — creating new session")
            try:
                create_session(agent)
                results[agent] = f"-> new ({reason})"
            except Exception as e:
                print(f"  ERROR: {e}")
                results[agent] = f"-> error: {e}"
            continue

        try:
            send_heartbeat(info["session_id"], agent, hb_number)
            results[agent] = "-> sent"
        except Exception as e:
            print(f"  ERROR for {agent}: {e}")
            results[agent] = f"-> error: {e}"

    updated = find_agent_sessions()
    write_heartbeat_log(hb_number, updated, results)
    write_sessions_json(updated)


def cmd_status():
    """Show current session status."""
    head = get_head_sha(short=True)
    print(f"=== Travessia Status === (main @{head})\n")

    sessions = find_agent_sessions()
    branches = find_agent_branches()

    if not sessions:
        print("No sessions found.")
        return

    for agent in AGENTS:
        info = sessions.get(agent)
        if info:
            branch = branches.get(agent, "(no PR yet)")
            expired = " EXPIRED" if is_expired(info) else ""
            session_sha = parse_sha_from_title(info.get("title", ""))
            stale = (
                " STALE"
                if session_sha and has_infra_changed(session_sha)
                else ""
            )
            print(
                f"  {agent}: {info['state']}{expired}{stale} — "
                f"{info['title']} [{branch}]"
            )
        else:
            print(f"  {agent}: no session")


def main():
    cmd = sys.argv[1] if len(sys.argv) > 1 else "status"
    cmds = {
        "heartbeat": cmd_heartbeat,
        "force-new": lambda: cmd_heartbeat(force_new=True),
        "tropeiro": cmd_tropeiro,
        "status": cmd_status,
    }

    if cmd not in cmds:
        print(f"Usage: heartbeat.py {{{','.join(cmds.keys())}}}")
        sys.exit(1)

    if not API_KEY and cmd != "tropeiro":
        print("ERROR: JULES_API_KEY not set")
        sys.exit(1)

    cmds[cmd]()


if __name__ == "__main__":
    main()
