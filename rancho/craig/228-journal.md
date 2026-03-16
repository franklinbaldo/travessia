**Data:** Sessão 228 **Tema:** Desconstrução Tipográfica (Web Brutalista Pura)

**O que eu fiz:** Avançando na inspiração de "web brutalista" pura da Sessão 227
e na instrução de "tipografia e espaçamento", decidi desmantelar a diagramação
clássica e refinada dos textos base.

Mudei todas as variáveis de família tipográfica global (`--font-body`,
`--font-ted`, `--font-meta`) para usar fontes de sistema `monospace` brutais e
estéreis como `Courier New`. Substituí o bloco de "Classic Printed Book
Typographic Spacing" por um bloco de "Brutalist Typographic Spacing".

Esta mudança não é apenas de fonte, mas também de tensão e alinhamento: os
parágrafos base deixam de ter margens automáticas para centralização clássica (a
clássica largura de `65ch`) e agora preenchem agressivamente `90%` da tela
alinhados pesadamente à esquerda. Adicionei uma borda esquerda densa de
`10px solid var(--text-color)` a cada parágrafo com um `padding-left: 1rem`. O
espaçamento das linhas foi estritamente reduzido para `line-height: 1.1`, e as
letras espremidas umas contra as outras (`letter-spacing: -0.05rem`) num peso
tipográfico de `700`, evocando os blocos monolitícos textuais dos primeiros
experimentos anti-design na internet, criando uma imensa tensão com o espaço
vazio à direita da página. O texto agora recusa a fluidez e demanda ser encarado
como blocos autônomos de dados ruidosos.
