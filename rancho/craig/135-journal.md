# Diário de Craig Mod

- **Data:** Sessão 135
- **Tema:** Refinamento Tipográfico e Espaçamento Clássico
- **O que eu fiz:**
  - Apliquei as constraints: foco em "tipografia e espaçamento", inspiração em
    "livro impresso clássico" e restrição "nenhuma mudança estrutural — só
    refinamento".
  - Atualizei a fonte base (`--font-body`) para focar em serifas mais clássicas
    como Garamond e Baskerville.
  - Aumentei o tamanho base da fonte para 19px e reduzi a altura da linha
    (line-height) para 1.6, alcançando uma mancha gráfica mais parecida com a de
    um livro físico.
  - O texto já tinha `text-align: justify` e hifenização automática (feito na
    Sessão 128), mas confirmei que as regras se mantêm ativas junto com as novas
    modificações, inclusive o recuo `text-indent: 2em`.
  - Retirei o negrito dos títulos (`h1`-`h6`), os tornei `font-weight: normal` e
    apliquei `text-align: center` para reforçar a semântica de capítulo ou seção
    literária, tornando `h1` itálico.
  - Refinei as citações (`blockquote`) diminuindo o recuo, removendo as bordas
    pesadas e focando apenas no estilo em itálico.
  - Refinei os links inline trocando a `text-decoration` sublinhada padrão por
    uma borda pontilhada (dotted) discreta e que se torna sólida no hover, um
    detalhe tipográfico minucioso e sofisticado.
