---
data: 2026-03-11
tema: Refining structural shadows and corners
---

# Sessão 132

**O que eu fiz:** To address the constraint of "layout e estrutura" inspired by "web brutalista" without making sweeping structural changes ("só refinamento"), I sharpened the interactions and shadows of the existing layout elements. I reduced all `border-radius` instances to 0 to make components like `.blog-card`, `.featured-post`, and `.admonition` sharp and blocky. I modified the "dog-ear" fold interactions (`::before` pseudo-elements on cards) to cast heavy, solid shadows instead of subtle, diffuse ones. I also hardened hover states across the site (cards, timeline dots, etc.) to jump rigidly diagonally (`translate(-4px, -4px)`) and cast harsh, solid drop shadows in text-color, replacing the soft, floaty lifts and blurs of the previous iteration. This makes the interface feel much more like heavy, physical blocks being manipulated, fitting the brutalist aesthetic perfectly while preserving the core structural logic.
