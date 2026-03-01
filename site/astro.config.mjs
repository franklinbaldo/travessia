import { defineConfig } from "astro/config";
import remarkDirective from "remark-directive";
import remarkAdmonitions from "./src/plugins/remark-admonitions.ts";

// https://astro.build/config
export default defineConfig({
  site: "https://franklinbaldo.github.io",
  base: "/travessia/",
  trailingSlash: "ignore",
  markdown: {
    remarkPlugins: [remarkDirective, remarkAdmonitions],
  },
});
