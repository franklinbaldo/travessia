import { z, defineCollection } from "astro:content";
import { glob } from "astro/loaders";

const dialogoCollection = defineCollection({
  loader: glob({
    pattern: "**/*.md",
    base: "../cartas/ted-riobaldo",
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
    base: "../manuscrito",
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
    base: "../.jules/riobaldo",
  }),
});

const bastidoresTedCollection = defineCollection({
  loader: glob({
    pattern: "*-journal.md",
    base: "../.jules/ted",
  }),
});

const docsCollection = defineCollection({
  loader: glob({
    pattern: "{events-all-the-way-down,riobaldo-blueprint}.md",
    base: "../.jules/ted",
  }),
});

export const collections = {
  dialogo: dialogoCollection,
  manuscrito: manuscritoCollection,
  "bastidores-riobaldo": bastidoresRiobaldoCollection,
  "bastidores-ted": bastidoresTedCollection,
  docs: docsCollection,
};
