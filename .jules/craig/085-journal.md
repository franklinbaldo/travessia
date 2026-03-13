- **Data:** Sessão 085
- **Tema:** Letterpress e Microinterações Táteis na Página da Carta
- **O que eu fiz:** Para atender à constraint "livro impresso clássico" focada
  em "microinterações" e restrita a uma "única página/componente", direcionei
  meu foco para a página individual da Carta
  (`site/src/pages/carta/[slug].astro`).

  A estética anterior de "revista literária" trouxe bordas muito pesadas e
  contrastes stark. Para suavizar isso e invocar o peso físico de um livro
  clássico, introduzi efeitos de _deboss_ (baixo-relevo) usando composições de
  `box-shadow` (com valores `inset`) e `text-shadow`. Isso faz com que os
  crachás de autor (`.autor-badge`) e os pontos da linha do tempo
  (`.timeline-dot`) pareçam pressionados contra o papel macio (`#f8f7f5`).

  Durante o _hover_, os pontos da linha do tempo têm uma transição sutil em seu
  `box-shadow` e transformam levemente sua posição no eixo Y, sugerindo o
  desaperto da pressão física. No CSS global (`site/src/styles/global.css`),
  reduzi a espessura da borda inferior das tags `h2` e apliquei esse mesmo
  efeito de _letterpress_ nas tags de título (`h1` e `h2`), além de criar uma
  classe utilitária `.letterpress` para uso futuro. O resultado é uma página que
  respira melhor, unindo a hierarquia forte de uma revista com a sensação tátil
  da prensa tipográfica antiga.
