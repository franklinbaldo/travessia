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

- **Letter Readability & Analog Details (craig-066)**
  - **Typography & Letterpress:** Reverted the `.manuscrito-header h1` title
    color from the bright accent to the grounded `--text-color` for an authentic
    ink feel, and added a subtle letterpress `text-shadow` effect.
  - **Archive Stamps & Labels:**
    - Updated `.post-meta time` to resemble a stamped archive date (removed
      small-caps, applied uppercase meta font, slightly bolder, with a subtle
      dotted bottom border).
    - Redesigned `.autor-badge` (within reading pages) to look like a physical,
      perforated archive label by applying a dashed border, increasing
      letter-spacing (`0.15em`), and applying a subtle box-shadow.
  - **Contextual Clipping:** Refined `.correspondence-context` from a standard
    bordered block into a physical "clipped paper note" resting on the page.
    Changed to `inline-flex`, tightened padding, and applied a subtle `-1deg`
    rotation and drop shadow, complete with a straightening hover interaction to
    enhance tactility.

- **Micro-Analog Textures & Selections (craig-073)**
  - **Highlighting:** Replaced the default digital blue `::selection` background
    with a custom translucent accent-color background
    (`rgba(196, 135, 58, 0.3)`) to mimic the feel of an analog highlighter pen
    sliding over paper.
  - **Typewriter Impact:** Enhanced `strong` and `b` elements by applying a
    faint `text-shadow` (`0 0 0.5px currentColor`), creating a subtle
    "ink-bleed" effect that simulates the heavier impact of a physical
    typewriter striking paper for bold text.
  - **Dog-Ear Bookmark:** Added a folded "dog-ear" effect to the top-left corner
    of the `.featured-post` card on the homepage using a combination of a
    `linear-gradient` background and a `::before` pseudo-element with a drop
    shadow, subtly animating the fold size on hover to heighten the bookmarked,
    physical sensation.

- **Physical Labels and Taped Notes (craig-074)**
  - **Admonitions:** Redesigned `.admonition` blocks in the docs from generic
    left-bordered boxes to physical "taped notes".
    - Added a `1px` border, subtle drop shadow, and a slight rotation (`0.5deg`)
      to make the block resemble a loose note.
    - Added a `::before` pseudo-element with `backdrop-filter: blur(2px)` and a
      slight negative rotation to act as a piece of transparent tape adhering
      the note to the page.
    - Implemented a hover interaction that lifts and straightens the note.
  - **Blog Card Labels:** Updated the `.card-tipo` badges on the homepage feed
    to resemble physically pasted paper labels.
    - Added a dashed border (`1px dashed var(--divider-color)`), slight
      box-shadow, and a rotation (`-1deg`).
    - Reduced the background opacity to `0.08` to feel more like tinted paper
      than a digital block color.
    - Added a subtle hover effect (`transform: rotate(0) scale(1.02)`) linked to
      the `.blog-card` hover state for added tactility.

- **Punched Holes & Creased Paper Tactility (craig-075)**
  - **Paper Crease:** Added a vertical "fold" or crease down the left edge of
    `.blog-card` elements on the homepage feed using a `linear-gradient`
    background. This subtle shadow simulates a physical piece of paper that has
    been folded and unfolded.
  - **Punched Holes:** Transformed the `.footer-nav-link` (Previous/Next)
    buttons into tactile binder cards. Added a `::before` pseudo-element styled
    as a punched circle (using `border-radius: 50%` and an inset shadow) to
    physically ground the "index card" metaphor into the paper environment.
  - **Dog-Ear Fix:** Restored the `linear-gradient` to `.featured-post` elements
    to prevent background overwrites on hover, ensuring the "dog-ear" folded
    corner effect remains robust.

- **Editorial Ink & Corrections (craig-076)**
  - **Red Pen Strikethrough:** Styled `del` and `s` elements to resemble a
    physical red pen strike. Replaced the standard text-decoration with a slight
    negative-rotation (`-2deg`) `linear-gradient` pseudo-element and a faint
    box-shadow, creating an organic ink correction feel.
  - **Analog Highlighter:** Enhanced the `mark` element by adding a custom
    yellow `linear-gradient` background with uneven opacity stops and an inset
    shadow, simulating the imperfect stroke of a real highlighter pen.
  - **Drop Cap Letterpress:** Added a subtle inset `text-shadow` to the
    `.manuscrito-body` drop cap (`p:first-of-type::first-letter`) to simulate
    the heavy indentation of a physical letterpress striking thick paper.

- **Vintage Code Prints and Ledger Tables (craig-077)**
  - **Ledger Tables:** Redesigned standard Markdown `table` elements to resemble
    vintage accounting ledgers.
    - Added a subtle paper background (`var(--sand-bg)`), complete with a top
      and bottom border to ground the table.
    - Styled `th` elements with the `var(--accent-color)` to look like stamped
      headers, adding a dashed bottom border.
    - Added faint vertical gridlines (`border-right`) to `td` and `th` cells to
      mimic ledger ruling.
  - **Typewriter Code Blocks:** Enhanced `code` and `pre` elements to feel like
    strips of mechanical typewriter output or vintage computing paper.
    - Applied a `dashed` border and a faint, repeating linear-gradient "paper
      banding" texture to `pre` blocks.
    - Added a subtle negative text-shadow to inline `code` to simulate the
      physical impact of a typewriter key striking paper.

- **Archival Index Cards and Stamped Typography (craig-078)**
  - **Archival Index Cards:** Enhanced `.bastidores-card` elements to resemble
    physical ruled index cards from a library archive.
    - Added a repeating linear gradient for faint horizontal ruling.
    - Added a subtle alternating rotation using `nth-child(odd)` and
      `nth-child(even)` to make them appear organically scattered.
    - Added a physical drop-shadow.
    - Updated the hover state to straighten the card (`rotate(0)`) and subtly
      increase the ruling lines' contrast, enhancing tactility.
