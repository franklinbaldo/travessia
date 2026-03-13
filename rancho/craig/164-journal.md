---
data: 2026-03-12
tema: "Redesign of BlogCard for Contemporary Literary Magazine"
o_que_eu_fiz:
  "In Sessão 164, adhering to the constraints of 'layout e estrutura' and
  'revista literária contemporânea' while restricted to 'focar numa única
  página/componente', I completely redesigned the `BlogCard` component
  (`site/src/components/BlogCard.astro`). I stripped away the heavy, tactile
  'notebook' aesthetic—removing the repeating linear gradients, solid borders,
  simulated ink colors, hover shadow scaling, and corner folds. Instead, I
  introduced a minimalist, editorial layout characteristic of a contemporary
  literary magazine. The cards now feature a clean transparent background,
  separated only by a crisp `1px solid var(--text-color)` top border. I
  reordered the internal elements via flex `order`, placing the metadata above
  the title to mirror classic journalistic datelines. The typography was shifted
  entirely to a refined serif (`Times New Roman`) for titles and excerpts, while
  keeping the metadata in a strict uppercase sans-serif. For interactions, I
  replaced the dramatic spatial shifts with a simple, elegant `opacity: 0.7`
  transition on hover, focusing entirely on structural clarity and unadorned
  typography rather than skeuomorphic physicality."
---
