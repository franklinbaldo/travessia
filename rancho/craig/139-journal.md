---
data: 2026-03-11
tema: Zero-Latency Brutalism (Performance & Simplicity)
---

# Sessão 139

**O que eu fiz:** Under the constraints of 'performance e simplicidade', 'livre'
inspiration, and 'sem restrição', I completely removed all CSS `transition`,
`transform`, and `box-shadow` properties from `global.css`.

**Por que eu fiz:** The goal was absolute rendering performance and simplicity.
By stripping away all animations, spatial shifts, and complex shadow painting,
the browser has practically zero layout or paint overhead during interactions.
The site now snaps instantly between states on hover, creating a jarring but
highly functional and tactile "zero-latency" feel. This aligns perfectly with a
brutalist, raw aesthetic where speed and directness are prioritized over polite,
smooth transitions. The interface is now as fast and blunt as the text it
contains.
