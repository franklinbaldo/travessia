## 087-journal.md

**Data:** Sessão 087 **Tema:** High Contrast Blocks and Inverted Interactions

**O que eu fiz:**

- Focando na constraint "cor e contraste", refinei os micro-interações do feed e
  tipografia para abraçar uma estética mais stark e posterizada, distanciando as
  sombras sutis que havíamos criado na iteração passada.
- **Selecão:** Substituí o `background-color` sutil das pseudo-classes
  `::selection` e `::-moz-selection` por um fundo sólido `var(--accent-color)`
  com a cor da fonte correspondente a `var(--bg-color)`. Essa mudança resulta
  numa cor de realce com um contraste muito mais agressivo, semelhante à uma
  tarja preta grossa, mas utilizando o nosso vermelho.
- **Micro-interações no Feed (`BlogCard.astro` & `FeaturedPost.astro`):**
  Modifiquei a pseudo-classe `:hover` de cartões. Em vez de uma cor de
  água/poeira, um background block forte preenche os cards e o conteúdo textual
  fica branco (`var(--bg-color)`), criando uma interação extrema, onde há
  inversão das cores - como se fosse mergulhado num mar de nanquim ou de sangue
  de jagunço (`var(--text-color)`).
- **Cartão do Tipo:** Atualizei os marcadores (`.tipo-*`) para preencher um
  fundo sólido usando variáveis das próprias bordas, removendo a necessidade de
  um canal alfa (ex: preenchimento escuro, cor do texto clara). A leitura agora
  é afiada e dramática.
