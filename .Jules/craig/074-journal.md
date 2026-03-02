## 074-journal.md

**Data:** Sessão 074 **Tema:** Physical Labels and Taped Notes

**O que eu fiz:**

- **Admonitions:** Redesigned `.admonition` blocks in the docs from generic
  left-bordered boxes to physical "taped notes".
  - Added a `1px` border, subtle drop shadow, and a slight rotation (`0.5deg`)
    to make the block resemble a loose note.
  - Added a `::before` pseudo-element with `backdrop-filter: blur(2px)` and a
    slight negative rotation to act as a piece of transparent tape adhering the
    note to the page.
  - Implemented a hover interaction that lifts and straightens the note.
  - **Blog Card Labels:** Updated the `.card-tipo` badges on the homepage feed
    to resemble physically pasted paper labels.
    - Added a dashed border (`1px dashed var(--divider-color)`), slight
      box-shadow, and a rotation (`-1deg`).
    - Reduced the background opacity to `0.08` to feel more like tinted paper
      than a digital block color.
    - Added a subtle hover effect (`transform: rotate(0) scale(1.02)`) linked to
      the `.blog-card` hover state for added tactility.
