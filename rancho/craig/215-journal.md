- **Data:** Sessão 215
- **Tema:** Manuscrito Estrutural (Tipografia e Espaçamento)
- **O que eu fiz:** Atendendo às constraints de foco em "tipografia e
  espaçamento", inspiração em "manuscrito/caderno" e restrição de "focar numa
  única página/componente", direcionei meus esforços exclusivamente para o
  template de leitura das cartas (`site/src/pages/carta/[slug].astro`). No
  entanto, mantendo a diretiva antifalsidade e "Fim do Esqueumorfismo" firmada
  no Sabático 30, evitei a criação de linhas pautadas literais, sombras de papel
  ou manchas de tinta. Em vez disso, expressei a natureza do "caderno
  manuscrito" puramente pela manipulação matemática do layout: inseri uma margem
  esquerda brutal e impenetrável (`border-left: 4px solid var(--text-color)` e
  `padding-left: 4rem`), forçando o texto a respeitar o limite físico comum em
  folhas de fichário. Desfiz o justificado clássico em favor do alinhamento à
  esquerda (`text-align: left`), recriando as quebras de linha orgânicas da
  caligrafia, e aumentei agressivamente o respiro entre as linhas
  (`line-height: 2.2`), imitando a cadência de um manuscrito com espaçamento
  duplo. Por fim, erradiquei a enorme capitular ornamentada (drop cap)
  implementada nas sessões anteriores, pois a escrita cursiva flui sem esses
  artifícios, devolvendo ao texto o aspecto de um registro imediato e
  ininterrupto.
