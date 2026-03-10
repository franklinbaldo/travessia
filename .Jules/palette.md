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

**Learning:** When building visual sequences like timeline dots or pagination links, using CSS classes (e.g., `.current` or `.active`) only provides visual feedback. Screen reader users need semantic context to understand which item in a sequence is currently active.
**Action:** Always add `aria-current="page"` (or appropriately "step", "location") to the active link within a sequence or navigation component to ensure screen reader users can identify the current context.

## 2024-03-08 - Distinguishing Multiple Navigation Landmarks

**Learning:** When a page contains multiple `<nav>` elements (e.g., main menu, category filters, and footer pagination), screen readers announce them all generically as "navigation landmark". This makes it difficult for non-visual users to understand the purpose of each menu and quickly jump to the right one.
**Action:** Always add a descriptive `aria-label` (like "Principal", "Categorias", or "Navegação da postagem") to every `<nav>` element on a page to provide clear semantic boundaries and context. Additionally, use `rel="prev"` and `rel="next"` on sequential navigation links.

## 2026-03-10 - Dynamic ARIA Labels for Theme Toggles

**Learning:** Static labels like "Alternar tema" (Toggle theme) lack actionable clarity. For screen reader users and mouse users wanting tooltip context, it's ambiguous what the next state will be. The theme toggle should explicitly indicate the *action* it performs based on current state.
**Action:** When implementing theme toggles or similar binary state buttons, dynamically update the `aria-label` and `title` via JavaScript to reflect the *action* that will occur when clicked (e.g., "Mudar para tema claro" or "Mudar para tema escuro").
