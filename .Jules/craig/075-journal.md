## 075-journal.md

**Data:** Sessão 075
**Tema:** Punched Holes & Creased Paper Tactility

**O que eu fiz:**
- **Paper Crease:** Added a vertical "fold" or crease down the left edge of `.blog-card` elements on the homepage feed using a `linear-gradient` background. This subtle shadow simulates a physical piece of paper that has been folded and unfolded.
  - **Punched Holes:** Transformed the `.footer-nav-link` (Previous/Next) buttons into tactile binder cards. Added a `::before` pseudo-element styled as a punched circle (using `border-radius: 50%` and an inset shadow) to physically ground the "index card" metaphor into the paper environment.
  - **Dog-Ear Fix:** Restored the `linear-gradient` to `.featured-post` elements to prevent background overwrites on hover, ensuring the "dog-ear" folded corner effect remains robust.
