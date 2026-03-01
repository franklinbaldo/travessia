import { defineConfig } from "astro/config";
import rehypeAdmonitions from "./src/plugins/rehype-admonitions.ts";

// https://astro.build/config
export default defineConfig({
  site: "https://franklinbaldo.github.io",
  base: "/travessia/",
  trailingSlash: "ignore",
  markdown: {
    rehypePlugins: [rehypeAdmonitions],
  },
});
