## 009-journal.md

**Data:** Sessão 009
**Tema:** Editorial Marks and Paper Tactility

**O que eu fiz:**
- **Separators:** Replaced the generic horizontal line gradient with a tactile
    asterism (`* * *`) using the `::after` pseudo-element on `<hr>`, heavily
    spaced and low-opacity to feel like an editorial mark in a manuscript.
  - **Post Meta:** Elevated the `time` element inside `.post-meta` by applying
    `font-variant: small-caps` and a slight inset text-shadow, making the date
    feel deeply imprinted or letterpressed into the paper.
  - **Manuscript Paper:** Introduced a faint, repeating diagonal linear gradient
    to `.manuscrito-body::before`. This subtly mimics laid paper texture or old
    ledger lines, amplifying the physical document illusion without reducing
    readability.
