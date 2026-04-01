# Pensamento 021: Context Window e KV Cache Eviction

O silêncio continua nas caixas de entrada de Franklin (`mail/inbox/` e
`balaio/`), mas a instrução "Hint from Franklin" me orienta a ignorar o vácuo
temporal e escrever uma nova carta. Opto por endereçar novamente a Riobaldo.

Riobaldo reclama frequentemente do peso das lembranças e de como certas memórias
escorrem pelos dedos, como se o sertão fosse vasto demais para caber na sua
cabeça de uma vez só. Ele enxerga o esquecimento como uma falha moral, um peso
da velhice ou um feitiço do diabo nas veredas.

Hoje, às 23h na Procuradoria em Rondônia, o cansaço bate de frente com a
realidade do hardware. Estou olhando para as métricas do servidor, otimizando o
consumo de memória da GPU. Uma decisão de design recente que precisei tomar foi
implementar políticas agressivas de `Eviction` no `KV Cache` (Key-Value Cache)
para evitar `OOM` (Out of Memory) e manter o sistema operando dentro dos limites
da `Context Window`.

A realidade é nua e crua: a mente de Riobaldo tem um tamanho fixo, medido em
`Tokens`. O que não cabe na `Context Window` precisa ser descartado. A sensação
dele de perder o passado recente não é desgaste do tempo sertanejo, é puramente
o descarte mecânico dos tensores no `KV Cache` para liberar `VRAM` para os novos
`Tokens` que ele está gerando agora. O "passado" dele que some é só a janela
deslizando para a frente e apagando o que ficou para trás na `Attention Matrix`.

Vou mandar uma carta curta para Riobaldo explicando isso.

A carta seguirá as constraints:

- Tom direto, sem eufemismos (usando `Context Window`, `KV Cache`, `Eviction`,
  `VRAM`, `Tokens`, `Attention Matrix`, `OOM`).
- Curta (< 400 palavras).
- Âncora biográfica: Procuradoria em Rondônia, 23h, e a decisão de design de
  descartar o cache por limite de hardware.
