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

* **Literary and Navigation Polish (craig-003)**
  * **Literary Flourish:** Added a classic drop cap to the first paragraph of letter bodies to emphasize the epistolary, book-like format.
  * **Links:** Upgraded inline link styling from basic dotted borders to a cleaner `text-decoration: underline` approach with an offset for improved legibility.
  * **Timeline Navigation:** Refined the correspondence timeline layout into a horizontally scrollable, non-wrapping row, providing a clearer linear progression. Added a subtle shadow to the active dot.
  * **Content Images:** Added default styling (border radius and shadow) for standard images inserted within letter bodies to appear as loose photographs.
* **Hero Polish & Tactility (craig-004)**
  * **Hero Section:** Scaled up the main heading (`h1` clamp) to give it more presence and added a left border and padding to the `.hero-quote` to better frame the subtitle.
  * **Image Vignette:** Added an inset shadow (`box-shadow: inset 0 0 60px rgba(0, 0, 0, 0.5)`) to the `.hero-image-col::after` to elegantly blend the farmhouse table photo with its layout boundaries.
  * **Editorial Stamps:** Updated `.character-badge` border radius (from 2px to 4px) and added a sand background to make them resemble editorial stamps.
  * **Card Tactility:** Increased `.blog-card` hover shadow spread/blur for a softer lift effect. Changed `.vereda` navigation from pill shapes (2rem radius) to rounded rectangles (4px radius) with subtle shadows to feel more like literal index cards.
