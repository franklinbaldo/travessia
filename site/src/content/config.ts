import { z, defineCollection } from "astro:content";
import { glob } from "astro/loaders";
import { fileURLToPath, pathToFileURL } from "url";
import path from "path";

const __dirname = path.dirname(fileURLToPath(import.meta.url));

const dialogoCollection = defineCollection({
  loader: glob({
    pattern: "**/*.md",
    base: pathToFileURL(path.join(__dirname, "../../../cartas/ted-riobaldo")),
  }),
  schema: z.object({
    titulo: z.string(),
    autor: z.string(),
    data: z.coerce.date().optional(),
  }),
});

const manuscritoCollection = defineCollection({
  loader: glob({
    pattern: "**/*.md",
    base: pathToFileURL(path.join(__dirname, "../../../manuscrito")),
  }),
  schema: z.object({
    titulo: z.string(),
    ordem: z.number().optional(),
    tipo: z.enum(["abertura", "causo", "fechamento", "fragmento"]),
    subtitulo: z.string().optional(),
    epigrafe: z.string().optional(),
  }),
});

const bastidoresRiobaldoCollection = defineCollection({
  loader: glob({
    pattern: "**/*.md",
    base: pathToFileURL(path.join(__dirname, "../../../.jules/riobaldo")),
  }),
});

const bastidoresTedCollection = defineCollection({
  loader: glob({
    pattern: "*-journal.md",
    base: pathToFileURL(path.join(__dirname, "../../../.jules/ted")),
  }),
});

const docsCollection = defineCollection({
  loader: glob({
    pattern: "{events-all-the-way-down,riobaldo-blueprint}.md",
    base: pathToFileURL(path.join(__dirname, "../../../.jules/ted")),
  }),
});

export const collections = {
  dialogo: dialogoCollection,
  manuscrito: manuscritoCollection,
  "bastidores-riobaldo": bastidoresRiobaldoCollection,
  "bastidores-ted": bastidoresTedCollection,
  docs: docsCollection,
};
