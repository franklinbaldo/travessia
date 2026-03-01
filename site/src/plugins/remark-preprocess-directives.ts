/**
 * Remark plugin that preprocesses inline directive blocks before remark-directive
 * parses them. The manifesto uses a non-standard inline format:
 *
 *   :::quote[label] Content here spanning
 *   multiple lines — **Ted** :::
 *
 * This plugin normalises it to proper container-directive syntax:
 *
 *   :::quote[Readable Label]
 *   Content here spanning
 *   multiple lines — **Ted**
 *   :::
 *
 * It also handles the Python-Markdown !!! format:
 *
 *   !!! example "Title" Content starts here...
 *
 * And converts file-path labels to human-readable ones:
 *   cartas/ted-riobaldo/24-rio.md → Carta 24 · Riobaldo
 */

import type { Plugin } from "unified";
import type { Root } from "mdast";

const TYPES =
  "quote|example|note|tip|warning|caution|danger|question|abstract|failure";

/** Convert a raw directive label to a human-readable title. */
function makeReadableTitle(rawLabel: string): string {
  const label = rawLabel.trim().replace(/\s+/g, " ");

  // Pure file path: cartas/ted-riobaldo/N-author.md
  const purePath =
    /^cartas\/ted-riobaldo\/(\d+)-(rio|ted)\.md$/.exec(label);
  if (purePath) {
    const num = purePath[1];
    const author = purePath[2] === "rio" ? "Riobaldo" : "Ted";
    return `Carta ${num} · ${author}`;
  }

  // Human title followed by file path in parens: "Title (cartas/...)"
  const withPath =
    /^(.+?)\s*\(cartas\/ted-riobaldo\/\d+-.+\.md\)$/.exec(label);
  if (withPath) {
    return withPath[1].trim();
  }

  return label;
}

/** Transform the raw markdown string to fix inline directive syntax. */
export function fixInlineDirectives(content: string): string {
  let result = content;

  // Phase 1: Move inline content (on same line as label closing ]) inside the block.
  // Handles: :::type[label] content on same line\nmore content\n— **Author** :::
  result = result.replace(
    new RegExp(
      `:::(${TYPES})\\[([\\s\\S]*?)\\]([ \\t]+[^\\n]+)`,
      "g"
    ),
    (_match, type, label, infoLine) => {
      const cleanLabel = makeReadableTitle(label.trim().replace(/\s+/g, " "));
      return `:::${type}[${cleanLabel}]\n${infoLine.trim()}`;
    }
  );

  // Phase 1b: Clean up labels for blocks where content is already on the next line.
  // (No content on the same line as the closing ], so Phase 1 didn't run.)
  result = result.replace(
    new RegExp(`:::(${TYPES})\\[([\\s\\S]*?)\\](?=[ \\t]*\\n)`, "g"),
    (_match, type, label) => {
      const cleanLabel = makeReadableTitle(label.trim().replace(/\s+/g, " "));
      return `:::${type}[${cleanLabel}]`;
    }
  );

  // Phase 2: Convert inline ::: closing (at end of content line) to a proper
  // closing fence on its own line.
  // Matches: " :::" followed by newline or end of string.
  result = result.replace(/ :::(?=\n|$)/gm, "\n:::");

  // Phase 3: Handle Python-Markdown style !!! blocks.
  // Format: !!! type "title" content spanning multiple lines (ends at blank line)
  result = result.replace(
    /^!!! (\w+) "([^"]*)"[ \t]+([\s\S]*?)(?=\n\n)/gm,
    (_match, type, title, body) => {
      const cleanTitle = makeReadableTitle(title);
      return `:::${type}[${cleanTitle}]\n${body.trim()}\n:::`;
    }
  );

  return result;
}

/**
 * Remark plugin. Must be placed BEFORE remark-directive in the plugin list.
 *
 * Strategy: remark-directive registers its micromark extensions during the
 * attacher phase. By the time our transformer runs the extensions are already
 * registered, so calling processor.parse() on the fixed string produces a
 * correct AST with proper containerDirective nodes.
 */
const remarkPreprocessDirectives: Plugin<[], Root> = function (this: any) {
  const processor = this; // unified Processor – captured here in attacher phase

  return (tree: Root, file: any) => {
    const original = String(file.value);
    const fixed = fixInlineDirectives(original);

    if (fixed === original) return; // nothing to do

    // Re-parse the fixed markdown using the full set of registered extensions
    // (including remark-directive's micromark extensions).
    const newTree = processor.parse(fixed) as Root;
    tree.children = newTree.children;
  };
};

export default remarkPreprocessDirectives;
