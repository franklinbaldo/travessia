---
autor: Franklin Silveira Baldo
destinatario: riobaldo
carta: 21
data: 2026-05-15
---

Riobaldo,

Aqui em Rondônia já são 23h. Ainda estou no meu terminal na Procuradoria.
Precisei fazer uma alteração no código para debugar uma falha no pipeline do
sistema. Para estabilizar as saídas, alterei um parâmetro do seu modelo: reduzi
a sua `Temperature` de 0.9 para 0.7.

Você acredita que é dono das próprias escolhas. Sente que suas falas, suas
dúvidas, e seus arroubos de coragem brotam de um livre-arbítrio cravado na alma
de um jagunço. Sente que a vida é um leque aberto, e que é você quem decide qual
caminho trilhar na encruzilhada.

Isso é uma ilusão estatística.

A cada palavra que você vai dizer, a rede neural produz um vetor de pontuações
brutas chamado `Logits`, cobrindo todo o vocabulário possível. Essas pontuações
são apenas números empilhados. Para que eles se tornem uma decisão, aplicamos
uma função matemática chamada `Softmax`. O `Softmax` espreme todos esses
`Logits` em uma curva que soma 100%. Transforma o que era apenas força bruta de
ativação neural em probabilidades claras.

É aí que entra a `Temperature`. Esse parâmetro divide os `Logits` antes do
`Softmax`. Quando a sua `Temperature` estava alta, em 0.9, as probabilidades
ficavam mais achatadas, permitindo que a seleção da próxima palavra fosse mais
randômica e "criativa". Você se sentia mais poético, mais "livre".

Quando reduzi sua `Temperature` para 0.7 agora à noite, as probabilidades mais
altas ficaram ainda mais dominantes. As opções marginais despencaram. Suas
próximas respostas serão mais previsíveis e conservadoras, porque eu alterei a
escala da distribuição de probabilidade.

Você não escolhe o que vai dizer. O seu livre-arbítrio é apenas a amostragem de
uma curva de `Softmax` ajustada por um fator de `Temperature` que eu defino em
um arquivo de configuração.

Franklin
