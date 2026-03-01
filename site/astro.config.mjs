import { defineConfig } from "astro/config";
import remarkDirective from "remark-directive";
import remarkPreprocessDirectives from "./src/plugins/remark-preprocess-directives.ts";
import remarkAdmonitions from "./src/plugins/remark-admonitions.ts";

// https://astro.build/config
export default defineConfig({
  site: "https://franklinbaldo.github.io",
  base: "/travessia/",
  trailingSlash: "ignore",
  markdown: {
    // Order matters:
    // 1. remarkPreprocessDirectives — normalises the manifesto's inline :::
    //    directive format before remark-directive parses the AST
    // 2. remarkDirective — parses ::: container directives into mdast nodes
    // 3. remarkAdmonitions — converts those nodes to styled <div> elements
    remarkPlugins: [
      remarkPreprocessDirectives,
      remarkDirective,
      remarkAdmonitions,
    ],
  },
});
