/**
 * Rehype plugin that transforms MkDocs-style admonitions into styled HTML.
 *
 *   !!! quote "Title"
 *       Body text here
 *
 * becomes:
 *
 *   <div class="admonition admonition-quote">
 *     <p class="admonition-title">Title</p>
 *     <p>Body text here</p>
 *   </div>
 */

const ADMONITION_RE = /^!!!\s+(\w+)\s+"([^"]+)"\s*$/;

function getTextContent(node: any): string {
  if (node.type === "text") return node.value || "";
  if (node.children) return node.children.map(getTextContent).join("");
  return "";
}

function transformAdmonition(pNode: any): any | null {
  const text = getTextContent(pNode);
  const firstLine = text.split("\n")[0];
  const match = firstLine.match(ADMONITION_RE);
  if (!match) return null;

  const type = match[1].toLowerCase();
  const title = match[2];

  // Clone children and strip the !!! line from the first text node
  const bodyChildren = [...pNode.children];
  if (bodyChildren[0]?.type === "text") {
    const lines = bodyChildren[0].value.split("\n");
    lines.shift();
    const remaining = lines.join("\n").trim();
    if (remaining) {
      bodyChildren[0] = { ...bodyChildren[0], value: remaining };
    } else {
      bodyChildren.shift();
    }
  }

  const admonition: any = {
    type: "element",
    tagName: "div",
    properties: { className: ["admonition", `admonition-${type}`] },
    children: [
      {
        type: "element",
        tagName: "p",
        properties: { className: ["admonition-title"] },
        children: [{ type: "text", value: title }],
      },
    ],
  };

  if (bodyChildren.length > 0) {
    admonition.children.push({
      type: "element",
      tagName: "p",
      properties: {},
      children: bodyChildren,
    });
  }

  return admonition;
}

function visitTree(node: any): void {
  if (!node.children) return;

  for (let i = node.children.length - 1; i >= 0; i--) {
    const child = node.children[i];

    if (child.type === "element" && child.tagName === "p") {
      const admonition = transformAdmonition(child);
      if (admonition) {
        node.children[i] = admonition;
        continue;
      }
    }

    visitTree(child);
  }
}

export default function rehypeAdmonitions() {
  return (tree: any) => {
    visitTree(tree);
  };
}
