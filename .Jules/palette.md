## 2026-03-01 - Keyboard Navigation Accessibility
**Learning:** The Astro project uses standard HTML navigation elements but lacked a global `:focus-visible` state, making keyboard navigation (Tab) invisible to screen reader/keyboard-only users.
**Action:** Always add a global `*:focus-visible` rule in the primary CSS file (e.g., `global.css`) using a prominent theme color (like `--accent-color`) to ensure accessibility across all interactive elements without needing component-specific overrides.
