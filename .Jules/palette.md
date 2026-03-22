## 2026-03-01 - Keyboard Navigation Accessibility

**Learning:** The Astro project uses standard HTML navigation elements but
lacked a global `:focus-visible` state, making keyboard navigation (Tab)
invisible to screen reader/keyboard-only users. **Action:** Always add a global
`*:focus-visible` rule in the primary CSS file (e.g., `global.css`) using a
prominent theme color (like `--accent-color`) to ensure accessibility across all
interactive elements without needing component-specific overrides.

## 2026-03-02 - ARIA Pressed State on Interactive Filters

**Learning:** Interactive filter buttons relying purely on CSS classes (e.g.,
`.active`) for visual feedback leave screen reader users blind to their
selection state. Using `aria-pressed` is the correct semantic pattern for this,
and it needs to be synced via JavaScript when the state changes. **Action:**
When creating or maintaining UI elements that act as toggleable filters, always
ensure an `aria-pressed` attribute is present and synchronized with the
element's visual active state.

## 2026-03-03 - Focusable Invisible Elements and Skip Links

**Learning:** Buttons like `#back-to-top` that are visually hidden using
`opacity: 0` and `pointer-events: none` can still be focused by keyboard users,
creating a confusing "invisible focus" trap. Additionally, bypassing navigation
repeatedly on every page is a major friction point for keyboard/screen reader
users. **Action:** Always pair `opacity: 0` with `visibility: hidden` (and
toggle to `visibility: visible`) when hiding interactive elements. Furthermore,
ensure every core layout includes an accessible "skip to content" link that
receives focus when tabbed.

## 2026-03-05 - ARIA Current State on Pagination/Timelines

**Learning:** When building visual sequences like timeline dots or pagination
links, using CSS classes (e.g., `.current` or `.active`) only provides visual
feedback. Screen reader users need semantic context to understand which item in
a sequence is currently active. **Action:** Always add `aria-current="page"` (or
appropriately "step", "location") to the active link within a sequence or
navigation component to ensure screen reader users can identify the current
context.

## 2026-03-12 - Distinguishing Multiple Navigation Landmarks

**Learning:** When a page has multiple `<nav>` elements (e.g., a main header
menu and a footer pagination component), screen reader users hear "navigation"
multiple times without context. Additionally, sequential pagination links lack
semantic relationships without specific attributes. **Action:** Always provide
descriptive `aria-label` attributes (like "Navegação principal" or "Navegação da
postagem") to distinguish multiple `<nav>` landmarks. Furthermore, use
`rel="prev"` and `rel="next"` on pagination links to explicitly define their
sequential relationship for assistive technologies.

## 2026-03-14 - Theme Toggle Button ARIA Pressed State

**Learning:** When using a button element to toggle a global state like a
light/dark theme, it acts as a boolean switch. Screen readers need to know its
current status beyond just the `aria-label` "Alternar tema" (Toggle theme).
Using `aria-pressed` provides immediate feedback on the current active state of
the button. **Action:** For standalone state-toggling buttons (like theme
switches), initialize `aria-pressed` correctly based on the current state on
load, and dynamically synchronize the `aria-pressed` attribute when the state
changes.

## 2026-03-15 - Explicitly Hiding Decorative Child Elements in Labeled Buttons

**Learning:** When an interactive element (like a button) uses an `aria-label`
to provide its accessible name, any child elements that contain text characters
or icons used purely for visual decoration (like state icons `☽` and `☀`) must
be explicitly hidden from screen readers using `aria-hidden="true"`. Otherwise,
assistive technologies may announce both the `aria-label` and the text content
of the children, creating redundant and confusing auditory noise. **Action:**
Always add `aria-hidden="true"` to child elements that contain text or icon
characters if the parent element already provides a complete accessible name via
`aria-label`.

## 2026-03-17 - Decorative Text Readability for Screen Readers

**Learning:** Text-based visual separators or decorative characters (like
`&larr;` or `&rarr;`) inside navigation links get read out loud by screen
readers literally (e.g. "leftwards arrow Anterior"). This introduces confusing
audio clutter for users relying on assistive technology. **Action:** Always wrap
decorative text characters within interactive elements in a
`<span aria-hidden="true">` to preserve visual formatting while hiding the
meaningless noise from screen readers.

## 2026-03-22 - Native Tooltips on Icon-Only Elements

**Learning:** While providing an `aria-label` on icon-only buttons makes them accessible to screen reader users, sighted users who rely on mouse hover or keyboard focus need a way to understand the button's function. A native tooltip using the `title` attribute bridges this gap.
**Action:** When creating or maintaining icon-only buttons (or elements acting like buttons with minimal visual text), always pair the `aria-label` attribute with a matching `title` attribute to ensure universal discoverability.

## 2026-03-24 - Hiding visually hidden elements from screen readers incorrectly

**Learning:** Using `display: none` on elements intended to be visually hidden but still available to screen readers (like the `.sr-only` headings generated for footnotes) completely removes the element from the accessibility tree, defeating its purpose.
**Action:** Replace `display: none` with standard `sr-only` CSS properties (absolute positioning, 1px width/height, overflow hidden, clip) so the element remains accessible to screen readers while being visually hidden.
