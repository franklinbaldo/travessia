---
Data: Sessão 183
Tema: Manuscrito e Mancha de Tinta — Microinterações
---

## O que eu fiz

Respondendo às constraints rigorosas desta sessão — foco em "microinterações e detalhes", inspiração "manuscrito/caderno", e a restrição de fazer "pelo menos uma mudança visível e ousada" — concentrei-me no componente principal da home, o `FeaturedPost.astro`.

Nas iterações anteriores, este componente simulava a estrutura física de um bloco de notas com encadernação lateral. Para elevar isso a um novo patamar tátil sem mexer na estrutura subjacente, criei duas microinterações avançadas baseadas puramente em CSS pseudo-elementos (`::before` e `::after`):

1. **Dog-Ear Corner Fold**: Inseri um efeito de dobra no canto superior direito do caderno (a "orelha" da página, o dog-ear). Quando o usuário passa o mouse, a ponta superior direita "dobra" fisicamente para baixo (`border-width` transiciona para 35px simulando sombra projetada por trás e a revelação do background subjacente). Essa pequena modificação evoca imediatamente a fisicalidade de um caderno manuseado.

2. **Mancha de Tinta Expansiva (A Mudança Ousada)**: Em vez de um *hover state* sutil (como escurecer o fundo ou mudar as letras), decidi introduzir um gradiente radial agressivo (`radial-gradient`), simulando tinta espessa se espalhando velozmente por debaixo do texto. No `:hover`, essa mancha (usando `mix-blend-mode: multiply` ou `screen` dependendo do tema) expande rapidamente de 0 para 250% do tamanho do card usando curvas de *easing* dramáticas (`cubic-bezier(0.19, 1, 0.22, 1)`).

Isso preenche a restrição de uma "mudança visível e ousada", pois a interação tátil de "passar a página" é amplificada pelo impacto visual de "derramar a tinta", unindo a delicadeza de um manuscrito com a crueza que define a linguagem do blog até agora.
