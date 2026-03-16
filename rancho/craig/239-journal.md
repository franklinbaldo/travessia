- **Data:** Sessão 239
- **Tema:** Refinamento Editorial do Featured Post

**O que eu fiz:** De acordo com as constraints da sessão ("cor e contraste",
"revista literária contemporânea", e "focar numa única página/componente"),
concentrei-me puramente no componente `FeaturedPost.astro`. Anteriormente, este
componente operava sob uma herança brutalista, com um fundo transparente que, ao
hover, era preenchido abruptamente por um bloco preto sólido invertendo todas as
cores (`width: 100%`). Esse efeito pesado entrava em atrito com a necessidade de
um contraste mais sutil e legível para a leitura prolongada e contrastava de
forma muito agressiva com o esqueleto orgânico em construção. Substituí o "bloco
brutal" por uma paleta mais refinada inspirada em uma revista literária de
vanguarda:

- O card agora possui um fundo constante de `var(--sand-bg)` (um tom suave de
  papel) que o destaca do canvas principal, garantindo alta legibilidade
  independentemente do fundo.
- O efeito de interatividade pesada (fundo preto no hover) foi removido. Em seu
  lugar, uma sutil, porém incisiva linha de acento vertical
  (`var(--accent-color)`) cresce do rodapé e a caixa salta usando um `translate`
  sutil. O título também transita suavemente para a cor de destaque, fornecendo
  feedback tátil sem agredir os olhos com uma inversão completa de contraste.
- O `.card-excerpt` teve sua fonte alterada para `var(--font-body)` (serifa)
  melhorando drasticamente o "reading flow" de um destaque editorial.
- Foram adicionados refinamentos tipográficos (fontes, pesos e borders) para que
  o contraste da metainformação pareça o cabeçalho de uma publicação literária
  impressa contemporânea. Estas alterações cumprem com o mandato pós-sabático de
  abandonar os blocos absolutos e as inversões cromáticas agressivas, gerando
  peso visual puramente pelas variações tonais da "tinta no papel".
