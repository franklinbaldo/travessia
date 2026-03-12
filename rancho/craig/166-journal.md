---
data: 2026-03-12
tema: "Redesign of FooterNav for Manuscript Aesthetic"
---

# Redesign of FooterNav for Manuscript Aesthetic

**O que eu fiz:** Adhering strictly to the constraints of "microinterações e detalhes", "manuscrito/caderno" and "focar numa única página/componente", I completely redesigned the `FooterNav` component (`site/src/components/FooterNav.astro`).

I stripped away the heavy, skeuomorphic "notebook" aesthetic that previously cluttered the footer. The repeating linear gradients, solid colored borders, simulated ink colors, intense hover shadow scaling, and complex pseudo-element corner folds were all removed.

In their place, I introduced a minimalist manuscript aesthetic. The footer navigation links now feature a clean transparent background, separated from the main content by a crisp `1px solid var(--text-color)` top border. This creates a much cleaner, more refined look that aligns with the recent editorial redesigns of other components.

For the required focus on micro-interactions, I replaced the dramatic, almost violent spatial shifts with a subtle, physical manuscript lift (`transform: translateY(-2px) rotate(-1deg)`) and a simple `opacity: 0.8` transition on hover. Crucially, I maintained and refined the elegant animated strikethrough/underline microinteraction for the titles. This ensures the component feels tactile and responsive, embodying the "manuscrito/caderno" feel through subtle motion rather than heavy visual simulation.
