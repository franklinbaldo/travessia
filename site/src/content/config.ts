import { z, defineCollection } from 'astro:content';
import { glob } from 'astro/loaders';
import { fileURLToPath } from 'url';
import path from 'path';

const __dirname = path.dirname(fileURLToPath(import.meta.url));

const manuscritoCollection = defineCollection({
  loader: glob({ pattern: '**/*.md', base: path.join(__dirname, '../../../manuscrito') }),
  schema: z.object({
    titulo: z.string(),
    ordem: z.number().optional(),
    tipo: z.enum(['abertura', 'causo', 'fechamento', 'fragmento']),
    subtitulo: z.string().optional(),
    epigrafe: z.string().optional(),
  }),
});

const bastidoresRiobaldoCollection = defineCollection({
  loader: glob({ pattern: '**/*.md', base: path.join(__dirname, '../../../.jules/riobaldo') }),
});

const bastidoresTedCollection = defineCollection({
  loader: glob({ pattern: '*-journal.md', base: path.join(__dirname, '../../../.jules/ted') }),
});

const docsCollection = defineCollection({
  loader: glob({ pattern: '{events-all-the-way-down,riobaldo-blueprint}.md', base: path.join(__dirname, '../../../.jules/ted') }),
});

export const collections = {
  'manuscrito': manuscritoCollection,
  'bastidores-riobaldo': bastidoresRiobaldoCollection,
  'bastidores-ted': bastidoresTedCollection,
  'docs': docsCollection,
};
