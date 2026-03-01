# Craig Mod — Experience Log

## Discoveries & Adjustments

- **Initial Design Tweaks (craig-001)**
  - **Typography and Spacing:** Refined the reading experience to be more
    elegant and breathable.
    - Increased `--body-lh` to `1.8` for better vertical rhythm.
    - Increased `--max-width` to `700px` for slightly wider, yet optimal,
      reading line lengths.
  - **Colors:** Softened the environment for long-form reading.
    - Adjusted `--bg-color` to `#f7f4ed` (a slightly cooler, lighter off-white
      sand).
    - Reduced text contrast slightly by modifying `--text-color` to `#332b20`.
  - **Layout:** Enhanced whitespace.
    - Pushed padding on `main` to `4rem 2rem 5rem` to give the text column more
      room to breathe.
    - Added margin-bottom to the `nav` (`4rem`) to distinctly separate the
      header from the content.

- **Editorial and Grid Polish (craig-002)**
  - **Typography:** Tightened the headings for a more editorial feel.
    - Added a `-0.02em` letter spacing to all headers (`h1`-`h6`).
  - **Blockquotes:** Upgraded from simple left-bordered text to distinct
    editorial callouts.
    - Added `var(--sand-bg)` background, `4px` border radius, and `1.5rem 2rem`
      padding.
  - **Grid & Cards:** Refined the masonry feed to feel lighter and more
    spacious.
    - Increased `.blog-feed` gap from `1.5rem` to `2.5rem`.
    - Softened `.blog-card` and `.featured-post` border radii from `6px` to
      `8px`.
    - Upgraded the hover state drop shadows for both light
      (`0 8px 24px rgba(0, 0, 0, 0.08)`) and dark modes
      (`0 8px 24px rgba(0, 0, 0, 0.25)`) to create a more delicate "lifting
      paper" effect.

- **Literary and Navigation Polish (craig-003)**
  - **Literary Flourish:** Added a classic drop cap to the first paragraph of
    letter bodies to emphasize the epistolary, book-like format.
  - **Links:** Upgraded inline link styling from basic dotted borders to a
    cleaner `text-decoration: underline` approach with an offset for improved
    legibility.
  - **Timeline Navigation:** Refined the correspondence timeline layout into a
    horizontally scrollable, non-wrapping row, providing a clearer linear
    progression. Added a subtle shadow to the active dot.
  - **Content Images:** Added default styling (border radius and shadow) for
    standard images inserted within letter bodies to appear as loose
    photographs.
- **Hero Polish & Tactility (craig-004)**
  - **Hero Section:** Scaled up the main heading (`h1` clamp) to give it more
    presence and added a left border and padding to the `.hero-quote` to better
    frame the subtitle.
  - **Image Vignette:** Added an inset shadow
    (`box-shadow: inset 0 0 60px rgba(0, 0, 0, 0.5)`) to the
    `.hero-image-col::after` to elegantly blend the farmhouse table photo with
    its layout boundaries.
  - **Editorial Stamps:** Updated `.character-badge` border radius (from 2px to
    4px) and added a sand background to make them resemble editorial stamps.
  - **Card Tactility:** Increased `.blog-card` hover shadow spread/blur for a
    softer lift effect. Changed `.vereda` navigation from pill shapes (2rem
    radius) to rounded rectangles (4px radius) with subtle shadows to feel more
    like literal index cards.

- **Tactile Timeline & Index Card Footer (craig-005)**
  - **Timeline Navigation:** Upgraded `.timeline-dot` elements to resemble
    physical typewriter keys. Added an inset shadow and subtle drop shadow for
    depth, and implemented a satisfying "pressed" state for the current active
    dot with deeper inset shadows and a `translateY(2px)` physical movement.
    Added a lifting effect on hover.
  - **Footer Navigation:** Redesigned the Previous/Next `.footer-nav-link`
    elements from simple transparent left-bordered rectangles to full, tactile
    "index cards." Applied a sand background, a full border with subtle rounded
    corners, and a lifting drop-shadow on hover to reinforce the analog,
    paper-based feeling of the epistolary format.

- **Editorial Flourishes & Micro-Tactility (craig-006)**
  - **Blockquote Watermarks:** Introduced a large, low-opacity (`0.15`)
    quotation mark watermark in the background of `blockquote` elements using
    the `::before` pseudo-element to heighten the literary/magazine aesthetic.
  - **Back to Top Bookmark:** Redesigned the generic `#back-to-top` circle into
    a tactile "bookmark tab" or "index card", reading "Topo ↑" with a `4px`
    border radius, subtle lift shadow (`var(--sand-bg)`), and a `translateY`
    hover effect.
  - **Micro-Tactility:**
    - Added a delicate bottom-border transition to the `nav a.logo` to give it
      the grounded appearance of stamped letterhead rather than flat digital
      text.
    - Added a subtle drop-shadow (`box-shadow: 0 1px 2px rgba(0,0,0,0.15)`) to
      `#reading-progress` so it resembles a physical thread or wet ink rather
      than a flat digital line.

- **Homepage Tactility & Veredas Tabs (craig-007)**
  - **Veredas Navigation:** Redesigned the `.vereda` category buttons to
    resemble physical index card tabs.
    - Removed hover box-shadows and changed border-radius to `6px 6px 0 0` (flat
      bottom).
    - Adjusted margins and border-bottoms to create an overlap effect
      (`margin-bottom: -2px; border-bottom: 2px solid transparent`).
    - Styled the active state to seamlessly blend with the background and
      feature a strong top border (`border-top: 3px solid var(--accent-color)`),
      reinforcing the physical folder tab metaphor.
  - **Hero Section:** Enhanced the tactility of `.hero-text-col` by adding a
    subtle radial gradient (`var(--water-bg)`) overlay, creating a gentle
    textured appearance to contrast with the adjacent image.

- **Hero Typographical and Stamping Polish (craig-008)**
  - **Typography:** Added a subtle `text-shadow` to the main `.blog-hero h1`
    title to give it a slightly raised, tactile quality against the background,
    simulating a pressed ink effect.
  - **Editorial Stamps:** Enhanced the `.character-badge` styling to resemble
    physical editorial stamps.
    - Added a subtle negative rotation (`transform: rotate(-2deg);`) and a soft
      drop shadow to the generic badge class to make it appear hastily stamped.
    - Applied a slight counter-rotation (`transform: rotate(1deg);`)
      specifically to `.badge-riobaldo` to ensure each badge looks individually
      stamped and imperfect, increasing the analog feel.

- **Editorial Marks and Paper Tactility (craig-009)**
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

- **Manuscript Spacing and Taped Photographs (craig-065)**
  - **Typography & Spacing:** Increased the `margin-bottom` of paragraphs (`p`)
    within `.manuscrito-body` to `1.8rem` to provide more breathing room and a
    more generous vertical rhythm for long-form reading.
  - **Image Treatments:** Enhanced the analog, physical feeling of the letters
    by styling images within `.manuscrito-body` as taped-in photographs.
    - Added `padding: 0.5rem`, a light background (`var(--bg-color)`), and a
      subtle border (`1px solid var(--divider-color)`).
    - Applied a slight rotation (`transform: rotate(-1deg)`) and a lifting
      drop-shadow to mimic a loose photo resting on the page.
    - Added a hover effect that scales the image slightly and straightens it
      (`transform: scale(1.02) rotate(0)`), creating a playful, tactile
      interaction.
