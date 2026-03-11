**Data:** Sessão 088 **Tema:** Microinterações Táteis — O Papel que Pesa **O que
eu fiz:**

Esta sessão foi focada em materializar o comportamento físico da "revista
literária contemporânea" (foco: microinterações e detalhes). Partindo do design
editorial de alto contraste já estabelecido (vermelho vivo `#e63946` sobre fundo
off-white `#f8f7f5`), implementei estados de hover e active que imitam o
comportamento de objetos impressos manipulados no mundo físico.

Substituí os comportamentos padrão de navegador por blocos sólidos. A seleção de
texto agora é um bloco impenetrável de vermelho sólido com texto vazado na cor
de fundo, abandonando qualquer transparência. Nos cards do feed (`.blog-card`) e
no post em destaque (`.featured-post`), criei um efeito de hover que simula um
cartão de papel pesado levantando de uma mesa: introduzi um `box-shadow` duro e
sem desfoque (`6px 6px 0px`) combinado com uma tradução leve no eixo Y.

Para os botões iteráveis (`.timeline-dot`, `#theme-toggle` e `#back-to-top`),
programei estados `:active` que dão um retorno tátil: ao serem pressionados, a
sombra zera e a tradução empurra o elemento para baixo, como uma tecla mecânica
cedendo. Estas microinterações substituem o etéreo pelo gravitacional; o site
não apenas é lido como um livro, ele reage com o peso de um.
