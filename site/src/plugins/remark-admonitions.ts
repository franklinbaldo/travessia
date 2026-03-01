/**
 * Remark plugin that transforms directive containers into admonition HTML.
 * Requires `remark-directive` to be registered before this plugin.
 *
 *   :::quote[Title]
 *   Body text here
 *   :::
 *
 * becomes:
 *
 *   <div class="admonition admonition-quote">
 *     <p class="admonition-title">Title</p>
 *     <div class="admonition-body">Body text here</div>
 *   </div>
 */

import { visit } from "unist-util-visit";
import { h } from "hastscript";

const TYPES = new Set([
  "quote", "example", "warning", "note", "tip", "caution", "danger",
  "question", "abstract", "failure",
]);

export default function remarkAdmonitions() {
  return (tree: any) => {
    visit(tree, "containerDirective", (node: any) => {
      const type = node.name?.toLowerCase();
      if (!type || !TYPES.has(type)) return;

      // Extract title from directive label (:::type[Title])
      let title = type.charAt(0).toUpperCase() + type.slice(1);
      if (node.children[0]?.data?.directiveLabel) {
        title = node.children[0].children[0].value;
        node.children.shift();
      }

      const data = node.data || (node.data = {});
      const hast = h("div", { class: `admonition admonition-${type}` });
      data.hName = hast.tagName;
      data.hProperties = hast.properties;

      // Prepend title paragraph
      node.children.unshift({
        type: "paragraph",
        data: {
          hName: "p",
          hProperties: { className: ["admonition-title"] },
        },
        children: [{ type: "text", value: title }],
      });
    });
  };
}
