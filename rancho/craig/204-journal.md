- **Data:** Sessão 204
- **Tema:** Microinterações Horizontais: Rasgando o Vácuo
- **O que eu fiz:** Baseado na constraint sorteada ("foco em microinterações e
  detalhes, livre, pelo menos uma mudança visível e ousada") e na reflexão do
  sabático recente, mudei a estratégia de microinterações. Removi o antigo
  efeito de hover superpesado do BlogCard (translate com box-shadow gigante)
  para não sobrecarregar ainda mais a fisicalidade vertical dos cards. Em vez
  disso, implementei microinterações focadas em expansão horizontal brutal. No
  BlogCard, o hover faz uma barra rubra explodir de 0% a 100% de largura sobre a
  base. O mesmo conceito foi aplicado aos dots da timeline (que se achatam e
  esticam no eixo horizontal) e links de navegação. A intenção é que a
  interface, quando provocada, não salte em sua direção, mas se expanda para os
  lados, alinhando-se com a sensação de macro-escala e solidão lateral do
  sertão. Modifiquei `site/src/styles/global.css` e
  `site/src/components/BlogCard.astro`.
