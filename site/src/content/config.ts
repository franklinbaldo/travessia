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

const cartasDoutorJoaoCollection = defineCollection({
  loader: glob({
    pattern: "**/*.md",
    base: "../cartas/riobaldo-doutor_joao",
  }),
  schema: z.object({
    destinatario: z.string().optional(),
    data: z.coerce.date().optional(),
    sessao: z.number().optional(),
  }),
});

const cartasZeBebeloCollection = defineCollection({
  loader: glob({
    pattern: "**/*.md",
    base: "../cartas/riobaldo-zebebelo",
  }),
  schema: z.object({
    destinatario: z.string().optional(),
    data: z.coerce.date().optional(),
    sessao: z.number().optional(),
  }),
});

const dialogoTedTylerCollection = defineCollection({
  loader: glob({
    pattern: "**/*.md",
    base: "../cartas/ted-tyler",
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
  schema: z.object({
    destinatario: z.string().optional(),
    tipo: z.string().optional(),
    data: z.coerce.date().optional(),
    sessao: z.number().optional(),
  }),
});

const bastidoresTedCollection = defineCollection({
  loader: glob({
    pattern: "*-journal.md",
    base: "../.jules/ted",
  }),
  schema: z.object({}).passthrough(),
});

// Craig journals have inconsistent frontmatter; skip for now
// const bastidoresCraigCollection = defineCollection({
//   loader: glob({
//     pattern: "*-journal.md",
//     base: "../.jules/craig",
//   }),
//   schema: z.object({}).passthrough(),
// });

const docsCollection = defineCollection({
  loader: glob({
    pattern: "{events-all-the-way-down,riobaldo-blueprint}.md",
    base: "../.jules/ted",
  }),
  schema: z.object({}).passthrough(),
});

export const collections = {
  dialogo: dialogoCollection,
  "cartas-doutor-joao": cartasDoutorJoaoCollection,
  "cartas-ze-bebelo": cartasZeBebeloCollection,
  "dialogo-ted-tyler": dialogoTedTylerCollection,
  manuscrito: manuscritoCollection,
  "bastidores-riobaldo": bastidoresRiobaldoCollection,
  "bastidores-ted": bastidoresTedCollection,
  // "bastidores-craig": bastidoresCraigCollection,
  docs: docsCollection,
};
