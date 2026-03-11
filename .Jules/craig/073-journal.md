## 073-journal.md

**Data:** Sessão 073 **Tema:** Micro-Analog Textures & Selections

**O que eu fiz:**

- **Highlighting:** Replaced the default digital blue `::selection` background
  with a custom translucent accent-color background (`rgba(196, 135, 58, 0.3)`)
  to mimic the feel of an analog highlighter pen sliding over paper.
  - **Typewriter Impact:** Enhanced `strong` and `b` elements by applying a
    faint `text-shadow` (`0 0 0.5px currentColor`), creating a subtle
    "ink-bleed" effect that simulates the heavier impact of a physical
    typewriter striking paper for bold text.
  - **Dog-Ear Bookmark:** Added a folded "dog-ear" effect to the top-left corner
    of the `.featured-post` card on the homepage using a combination of a
    `linear-gradient` background and a `::before` pseudo-element with a drop
    shadow, subtly animating the fold size on hover to heighten the bookmarked,
    physical sensation.
