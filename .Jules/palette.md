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
