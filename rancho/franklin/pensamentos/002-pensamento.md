As constraints para a sessão atual estão em `rancho/franklin/next-constraints.md`:
1. Tom: sem eufemismos técnicos.
2. Estrutura: Carta curta. Máximo 400 palavras. Um conceito por carta.
3. Âncora biográfica: detalhe concreto da vida real (trabalho em Rondônia, terminal às 23h, decisão de design).

Eu redigi a carta `franklin-riobaldo-002.md` abordando a `context window` (um conceito, termos técnicos em inglês, curta, e âncoras biográficas solicitadas).
Depois de redigir a carta 2 para Riobaldo, o prompt diz "No final, execute: `bash tools/sortear-constraints.sh franklin`". Como visto, o script retorna um erro pois não reconhece `franklin`.

O script original não tem suporte para `franklin` e a regra do repositório diz que não devo modificá-lo: "Do not overwrite or mock repository tool scripts (e.g., `tools/sortear-constraints.sh`) during your session. You must execute the existing scripts as provided in the codebase to ensure authentic outputs and avoid destructive modifications."
A consequência de eu executar `bash tools/sortear-constraints.sh franklin` é simplesmente o erro. E tudo bem. Eu restaurei o `next-constraints.md` original para o que era antes para ser fiel.
