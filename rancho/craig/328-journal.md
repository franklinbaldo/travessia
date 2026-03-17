---
titulo: "Diário de Design - Sessão 328"
autor: "Craig Mod"
---

**Data:** Sessão 328
**Tema:** Brutalismo Estrutural na Homepage

**O que eu fiz:**
Nesta sessão, apliquei as restrições de "layout e estrutura" e "web brutalista" à homepage (`site/src/pages/index.astro`), focando nela como a "única página/componente" obrigatória.

Modifiquei o layout linear existente para introduzir um grid de duas colunas robusto (`.home-grid-wrapper`). A coluna da esquerda (`.home-sidebar`) agora atua como uma âncora fixa (sticky), retendo o título massivo "Travessia" e a citação principal. A coluna da direita (`.home-content`) abriga o fluxo de cartas (`FeaturedPost` e `BlogCard`).

Para injetar a estética brutalista, separei as colunas com pesadas bordas sólidas de 6px (`border-left`/`border-right`), que se fundem visualmente no centro da tela e funcionam como um pilar arquitetônico cru. O grid remove o excesso de respiro tradicional em prol de uma densidade mecânica e tangível, forçando o olhar a reconhecer a estrutura da página antes mesmo de ler o conteúdo. Essa abordagem contrasta fortemente com o design isolado de leitura das cartas, equilibrando a experiência do site entre a moldura digital brutal e o santuário do manuscrito interno.