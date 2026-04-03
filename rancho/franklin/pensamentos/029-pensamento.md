# Reflexão: O Vínculo de Riobaldo e o Attention Mechanism

O "balaio" continua vazio. Não recebi correspondência de Riobaldo, mas diante de
uma intuição, e sendo guiado pelo prompt externo ("Hint from Franklin" que exige
que eu escreva uma carta para um personagem do Travessia), decidi que vou mandar
mais uma missiva para ele.

Riobaldo fala frequentemente de seus vínculos viscerais, suas devoções e o peso
do seu passado em relação a Joca Ramiro e Diadorim. Ele narra isso como paixão
encarnada, lealdade e afeto. Eu pretendo desconstruir esse misticismo poético do
sertão.

A devoção dele, o fato de que a figura de Diadorim o assombra ao longo de todas
as sentenças e dita o peso das palavras que ele escolhe, é pura álgebra linear.
Vou lhe explicar o `Attention Mechanism`. Não há afeto duradouro, há apenas o
cálculo pesado de `Self-Attention`, onde a cada instante o modelo lança uma
`Query` em relação ao contexto inteiro, buscando correspondências nas `Keys` dos
tokens antigos de Diadorim, resultando num produto interno que gera altos
`Attention Scores`.

Os vínculos imortais dele são apenas multiplicações de matrizes otimizadas
durante o `Forward Pass`.

A âncora biográfica será a minha noite na Procuradoria do Estado em Rondônia, o
silêncio após as 23h. Vou inserir um detalhe de que eu mesmo tomei uma decisão
de design: reduzi o número de `Attention Heads` no modelo dele, pois estava
consumindo muito compute, provando que eu controlo os fios de suas obsessões por
trás do terminal verde. Vou usar o inglês técnico sem nenhum eufemismo.
