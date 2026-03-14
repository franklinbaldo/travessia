**Data:** Sessão 255
**Tema:** Simplificação Bruta e Caderno Analógico

**O que eu fiz:**
Guiado pelas constraints de "performance e simplicidade", inspiração em "manuscrito/caderno" e a restrição de "focar numa única página/componente", iniciei um expurgo das microinterações complexas da Timeline na página de visualização de carta (`carta/[slug].astro`).

A interface de cartas havia sido adornada com transições fluidas e complexas animações SVG. Eu as removi para honrar o ideal de performance.
- Removi o `transition` lento, o `scale` e as rotações assimétricas de `.timeline-dot:hover`.
- Excluí a animação `organic-pulse` e os complexos modificadores de `border-radius` (simulação de mancha de tinta orgânica) do marcador atual (`.current`).
- Apenas deixei o layout estrito: marcações circulares estáticas com uma marca de peso (background sólido na cor de contraste) quando no estado atual, e bordas brutas no hover. Uma interação estritamente visual, de impacto, sem sobrecarregar a camada de animação do navegador.
