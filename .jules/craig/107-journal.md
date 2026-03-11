- **Data:** Sessão 107
- **Tema:** Microinterações Brutalistas
- **O que eu fiz:**
  Foquei em "microinterações e detalhes" sob a inspiração de "web brutalista".

  1. Alterei o cursor global de um SVG circular suave para um retângulo puro (quadrado) sem contornos suaves.
  2. Removi transições suaves dos elementos interativos principais (`.blog-card`, `.featured-post`, `.vereda`, `.timeline-dot`).
  3. Adicionei estados de `hover` mais austeros: translação de -4px nos eixos x e y, acompanhada de `box-shadow` pesado (`12px 12px` para cartões, `10px 10px` para posts em destaque e `6px 6px` para botões) que simulam um efeito de clique cru e físico, com cores invertidas imediatamente, sem delays.
  4. Implementei estilos de `focus-visible` universais bem marcados com cores contrastantes e `outline-offset` para garantir acessibilidade brutal e mecânica na navegação pelo teclado.
  5. Refinei a pseudo-classe `:active` para um pressionamento que elimina ou inverte a profundidade crua do `box-shadow`.
