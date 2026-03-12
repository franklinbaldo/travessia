---
titulo: "Microinterações e Detalhes - Manuscrito/Caderno"
data: "2026-03-11"
---

# Sessão 126
**Tema:** Microinterações Manuscritas

**O que eu fiz:**
Para responder às constraints "microinterações e detalhes", "manuscrito/caderno" e "sem restrição", mergulhei nos detalhes táteis da interface para evocar ainda mais a sensação de um caderno físico ou manuscrito em andamento.

Primeiro, substituí o cursor brutalista (um bloco quadrado) por um ícone de lápis/caneta desenhado em SVG (`data:image/svg+xml`), reforçando a metáfora de que o leitor está interagindo com o texto com um instrumento de escrita na mão.

Segundo, expandi o efeito de "dog-ear" (canto de página dobrado) que existia apenas no `.featured-post` para todos os `.blog-card`. Ao passar o mouse, a ponta superior direita da carta "dobra" suavemente, dando a sensação física de manipular um pedaço de papel.

Terceiro, adicionei uma microinteração de desenho livre aos botões/tags como `.card-tipo` e `.autor-badge`. No estado de `:hover`, a borda assume um raio de curvatura imperfeito e um estilo tracejado, com uma leve rotação de -2 graus, imitando um círculo desenhado às pressas à mão livre para destacar uma palavra.

Por fim, imagens dentro do corpo do manuscrito (`.manuscrito-body img`) agora reagem ao `:hover` não apenas removendo a rotação, mas escalando levemente, mudando seu `border-radius` para uma forma distorcida e imperfeita, simulando o efeito de uma foto colada que levanta do papel quando tocada.

Essas adições injetam vida e irregularidade orgânica nas microinterações sem corromper a estrutura rigorosa já estabelecida.
