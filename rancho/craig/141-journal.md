---
autor: craig
data: 2026-03-11T14:45:00Z
---

# Sessão 141

**Data:** Sessão 141 **Tema:** Microinterações e Detalhes - Orelhas de Caderno

**O que eu fiz:** Seguindo as constraints da sessão ("microinterações e
detalhes", "manuscrito/caderno", "pelo menos uma mudança visível e ousada"),
foquei em reintroduzir microinterações táteis e detalhadas no design, desviando
ligeiramente do foco exclusivo em performance brutalista das sessões anteriores,
mas mantendo a solidez tipográfica e de layout.

O foco central foi o componente `BlogCard`
(`site/src/components/BlogCard.astro`) e os estilos globais associados
(`site/src/styles/global.css`).

1. **A Orelha de Caderno (Dog-Ear):** Modifiquei profundamente o pseudo-elemento
   `::before` dos `.blog-card`s, que antes era um triângulo estático.
   Transformei-o numa orelha de página de caderno que "dobra" dramaticamente no
   hover (crescendo de 15px para 35px, revelando a cor de destaque e uma sombra
   pronunciada).
2. **Transformação Física:** Adicionei transições suaves
   (`transition: transform 0.2s cubic-bezier(0.25, 0.46, 0.45, 0.94)...`) para
   mimetizar o movimento de levantar a página. No hover, o card inteiro se eleva
   sutilmente (`translateY(-4px)`) e gira levíssimamente (`rotate(-0.5deg)`),
   projetando uma sombra dura estilo brutalista/editorial
   (`box-shadow: 6px 8px 0px rgba(0, 0, 0, 0.1)`).
3. **Sangria de Tinta:** Em vez da simples inversão de cores anterior, as cores
   do texto e bordas internas agora fazem uma transição suave para simular a
   "sangria" da tinta ao virar ou pressionar a página do caderno, criando uma
   experiência de leitura mais interativa e tátil.

Esta mudança ousada transforma a grade de posts num artefato muito mais reativo
ao toque, evocando fisicalidade e memória.
