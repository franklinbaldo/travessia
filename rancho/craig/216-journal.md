- **Data:** Sessão 216
- **Tema:** Microinterações de Revista Contemporânea
- **O que eu fiz:** Atendendo às constraints de foco em "microinterações e
  detalhes", com inspiração em "revista literária contemporânea" e uma restrição
  de "pelo menos uma mudança visível e ousada", concentrei-me em revitalizar a
  interatividade de componentes centrais da interface para algo mais
  contemporâneo, fluido e marcante. No componente `FeaturedPost.astro` (A Última
  Carta), introduzi uma transição de hover ousada e imersiva: ao invés da
  simples mudança de opacidade da versão anterior, implementei um preenchimento
  em bloco animado de fundo escuro (`var(--text-color)`) que se expande
  lateralmente usando pseudo-elementos (`::before`). A cor de todo o texto
  dentro da postagem, incluindo título, excerpt e metadados, transita
  dinamicamente para a cor de fundo original para criar um contraste absoluto e
  intenso.

No componente `BlogCard.astro`, removi as sombras duras remanescentes de ciclos
brutalistas (`box-shadow` e `translate(-4px, -4px)`) no arquivo `global.css`. Em
vez disso, incorporei uma microinteração arquitetural: no hover, uma linha
vertical acentuada (vermelha, `var(--accent-color)`) desce a partir do topo do
card para emoldurar o conteúdo. Em resposta a isso, o título do card, em
conjunto com o excerto, desloca-se suavemente para a direita, como um avanço na
grade do design, com o título assumindo uma postura itálica, simulando o
comportamento de ênfase típico em curadorias editoriais contemporâneas.
Adicionalmente, também alterei globalmente a seleção de texto e inseri um efeito
de hover audacioso para as bolinhas da linha do tempo, que agora se iluminam e
se expandem ligeiramente (`scale(1.1)`) absorvendo a cor de destaque,
transmitindo vivacidade imediata e interatividade sofisticada em detalhes
diminutos.
