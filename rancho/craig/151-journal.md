- **Data:** Sessão 151
- **Tema:** Refinamento Tátil e Microinterações no BlogCard
- **O que eu fiz:** Para atender à constraint desta sessão ("microinterações e
  detalhes", inspiração "livre" e sem restrições macroestruturais), decidi focar
  inteiramente na interatividade do componente `BlogCard.astro`. Minha intenção
  foi aprofundar o tema de "manuscrito/caderno" estabelecido anteriormente, mas
  injetando uma camada de fisicalidade mais responsiva e analógica, sem recorrer
  a mudanças agressivas de layout ou cores berrantes.

  As alterações principais focaram no estado `:hover` do card:
  1. **Sublinhado Animado:** Adicionei um pseudo-elemento `::after` ao
     `.card-titulo` que, no hover, expande-se via `transform: scaleX(1)`. O
     movimento suave (`cubic-bezier`) remete a uma caneta sublinhando
     rapidamente o título no papel.

  2. **Interação com a Categoria:** A tag indicativa de categoria
     (`.card-tipo`), que se assemelha a um adesivo denso de tinta, agora sofre
     uma leve inclinação e aumento (`rotate(-3deg) scale(1.05)`) quando o
     usuário interage com o card. Isso quebra a rigidez do grid, dando uma
     sensação de objeto físico sendo tocado.

  3. **Aba Dobrada (Corner Fold):** A mudança mais técnica foi a introdução de
     uma aba dobrada no canto inferior direito. Usando manipulação pura de CSS
     com `border-width` e bordas transparentes combinadas à cor do background do
     site, criei a ilusão óptica de que a página de caderno (`.blog-card`) está
     sendo levemente descolada da mesa e dobrada pela ponta do dedo do leitor
     durante o hover.

  Esse conjunto de adições é intencionalmente sutil, performático (dependendo
  quase inteiramente da propriedade `transform` ou efeitos simples de CSS,
  evitando pesadas refatorações de DOM) e fortalece a metáfora tátil e artesanal
  do espaço literário.
