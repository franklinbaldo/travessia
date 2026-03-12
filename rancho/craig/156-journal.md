---
data: "Sessão 156 tema: \"Masthead Brutalista: Tinta Sólida e Sombras Duras\""
---

## O que eu fiz

Hoje, sob as constraints estritas de focar em "performance e simplicidade", me inspirar na "web brutalista" e aplicar "pelo menos uma mudança visível e ousada", concentrei-me exclusivamente na página principal (`site/src/pages/index.astro`), mais especificamente no componente hero (`.blog-hero`).

Abandonei a tentativa anterior de simular uma delicada primeira página de jornal antigo (broadsheet). Em vez disso, impus um tratamento de alto contraste e brutalista: o container inteiro de texto do hero (`.hero-typographic`) agora é um enorme bloco preenchido com a cor de "tinta" (`var(--text-color)`) e texto invertido (`var(--bg-color)`). O que torna a mudança estruturalmente inconfundível é a adição de uma enorme sombra dura de `10px 10px 0` na cor de destaque vermelha (`var(--accent-color)`), ancorando o elemento na página como um soco visual pesado.

A tipografia do título principal (`h1`) foi modificada drasticamente, passando da fonte com serifa para uma fonte sans-serif grotesca e pesada (`var(--font-meta)`), com pesos máximos e letter-spacing negativo. A citação (`.hero-quote`) foi tirada do itálico clássico e empurrada para um fundo sólido vermelho, ganhando peso e autoridade.

Essa mudança é ruidosa, brutalista e performática: sem imagens, apenas manipulação crua do CSS (backgrounds, sombras sólidas, propriedades de tipografia agressivas), gerando o impacto ousado requisitado.
