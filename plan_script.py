with open('rancho/tyler/EXPERIENCE.md', 'r') as f:
    text = f.read()

# I deleted session 10. Let me get it back from git
import subprocess
out = subprocess.check_output(['git', 'show', 'HEAD:rancho/tyler/EXPERIENCE.md']).decode()
import re
parts_old = re.split(r'(?=\d\.\s\*\*)', out)
summary_old = parts_old[1]

# Extract session 10
s10 = re.search(r'\*\*Session 10.*?(?=\*\*Session 11)', summary_old, re.DOTALL)
if s10:
    s10_text = s10.group(0)

    parts_new = re.split(r'(?=\d\.\s\*\*)', text)
    summary_new = parts_new[1]

    # insert before Session 11
    summary_new = summary_new.replace("**Session 11", s10_text + "**Session 11")
    parts_new[1] = summary_new

    with open('rancho/tyler/EXPERIENCE.md', 'w') as f:
        f.write("".join(parts_new))
