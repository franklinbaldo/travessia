**Data:** 2026-03-15 **Tema:** Early Print Folio (Tipografia Clássica Ousada)
**O que eu fiz:** Guiado pelas constraints "tipografia e espaçamento",
inspiração em "livro impresso clássico" e foco em "única página/componente"
(`carta/[slug].astro`), conduzi uma transformação radical do layout de leitura.
Atingi o limite do "refinamento de revista literária" (que vinha deixando o
design apático e polido demais) e busquei uma inspiração mais antiga e brutal:
os primeiros fólios impressos. Na página da correspondência, a tipografia
assumiu um papel muito mais arquitetônico. O cabeçalho editorial perdeu as
métricas soltas da web contemporânea para formar um bloco duro, contido em
`65ch`, separado do texto por uma borda pesada `3px double`. Todas as fontes
meta (`editorial-meta`, `byline`) abandonaram o sans-serif contemporâneo para
assumirem a fonte serifa do corpo, forçando uma homogeneidade monólitica. O
corpo do texto (`.manuscrito-body p`) passou por um ajuste profundo: o recuo do
primeiro parágrafo dobrou para `2.5rem`, o `line-height` diminuiu para `1.35` e
usei `letter-spacing: -0.01em` e `word-spacing: -0.05em` para recriar o atrito
tenso e o aspecto de blocos densos das antigas impressões tipográficas
justificadas. A mudança mais dramática e ousada, porém, foi a inclusão de um
"Drop Cap" maciço na primeira letra (`font-size: 6rem; font-weight: 900`),
cravando a abertura do texto no papel. A página perdeu o ar de "revista
descolada" e ganhou o peso e a imobilidade de um documento clássico e austero.
