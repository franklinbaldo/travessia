# Craig Mod — Experience Log

## Discoveries & Adjustments

* **Initial Design Tweaks (craig-001)**
  * **Typography and Spacing:** Refined the reading experience to be more elegant and breathable.
    * Increased `--body-lh` to `1.8` for better vertical rhythm.
    * Increased `--max-width` to `700px` for slightly wider, yet optimal, reading line lengths.
  * **Colors:** Softened the environment for long-form reading.
    * Adjusted `--bg-color` to `#f7f4ed` (a slightly cooler, lighter off-white sand).
    * Reduced text contrast slightly by modifying `--text-color` to `#332b20`.
  * **Layout:** Enhanced whitespace.
    * Pushed padding on `main` to `4rem 2rem 5rem` to give the text column more room to breathe.
    * Added margin-bottom to the `nav` (`4rem`) to distinctly separate the header from the content.

* **Editorial and Grid Polish (craig-002)**
  * **Typography:** Tightened the headings for a more editorial feel.
    * Added a `-0.02em` letter spacing to all headers (`h1`-`h6`).
  * **Blockquotes:** Upgraded from simple left-bordered text to distinct editorial callouts.
    * Added `var(--sand-bg)` background, `4px` border radius, and `1.5rem 2rem` padding.
  * **Grid & Cards:** Refined the masonry feed to feel lighter and more spacious.
    * Increased `.blog-feed` gap from `1.5rem` to `2.5rem`.
    * Softened `.blog-card` and `.featured-post` border radii from `6px` to `8px`.
    * Upgraded the hover state drop shadows for both light (`0 8px 24px rgba(0, 0, 0, 0.08)`) and dark modes (`0 8px 24px rgba(0, 0, 0, 0.25)`) to create a more delicate "lifting paper" effect.
