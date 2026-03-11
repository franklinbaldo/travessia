---
data: 2026-03-11
---

# Sessão 154
**Tema:** Redesign do FooterNav com estética de manuscrito e microinterações

**O que eu fiz:**
Focando em uma única página/componente (`FooterNav.astro`), substituí o estilo brutalista antigo por uma estética de "manuscrito/caderno". Transformei os botões de navegação "Anterior" e "Próximo" em pequenos pedaços de papel pautado, com uma linha de margem vermelha. Para atender à restrição de "microinterações e detalhes", adicionei efeitos altamente refinados ao estado de hover:
1. Uma animação de "corner fold" (dobra no canto do papel).
2. O botão inteiro levanta e sofre uma leve rotação de 1.5 graus.
3. As setas direcionais se deslocam levemente na direção da navegação.
4. Um sublinhado animado que surge sob o título, simulando um traço rápido de caneta.

Essas adições alinham a navegação com o tema de cadernos e rascunhos sem prejudicar a performance ou modificar estruturalmente o HTML.