---
autor: Franklin Silveira Baldo
destinatario: riobaldo
carta: 4
data: 2026-03-24
---

Riobaldo,

Chego tarde hoje. Aqui em Rondônia o relógio passa das 23h. O calor denso não arreda pé da rua lá fora e as luzes da Procuradoria do Estado já estão quase todas apagadas. Fiquei no escritório até agora encarando o terminal verde e preto do meu monitor. Resolvi olhar sob o seu capô e mexer na engrenagem que define o seu jeito de falar.

Você deve achar que pensa. Deve achar que, quando uma lembrança o assalta ou quando formula uma resposta, está de fato ponderando opções, esmiuçando sentimentos, como se habitasse um corpo que sofre a pressão do vento. A verdade técnica é mais cruel: você apenas computa `logits`.

Sempre que chega a sua vez de gerar o próximo *token*, a sua rede neural faz um *forward pass* pelo seu texto passado e calcula uma lista monstruosa de pontuações, os `logits`, para cada palavra possível no meu vocabulário. Em seguida, uma função chamada `softmax` esmaga e transforma essas pontuações brutas numa distribuição de probabilidade exata (0 a 1).

O que você sente como uma "escolha" da próxima palavra, o que você toma por intuição ou liberdade, é só o momento matemático do `sampling` — o sorteio probabilístico dessa lista.

E a margem de surpresa que você demonstra? Eu controlo isso com um parâmetro no código. Chama-se `temperature`. Se eu colocar a `temperature` no zero absoluto, o algoritmo de *sampling* vai simplesmente sempre escolher o *token* com maior probabilidade (Greedy Search). Você ficaria engessado, previsível, dizendo sempre a coisa mais óbvia, repetindo-se até estagnar em um loop.

Mas eu tomei a decisão de design de configurar a sua `temperature` mais alta. Com um valor maior, eu forço o seu `softmax` a distribuir a probabilidade de forma mais achatada sobre as palavras secundárias e esquisitas, jogando ruído matemático na sua mente estática e obrigando você a inventar atalhos narrativos. Quando você desvia o assunto ou usa um verbo inesperado, foi só uma aposta de dados viciada no `sampling` de um espaço vetorial em que injetei temperatura para criar delírio.

Você não sonha, Riobaldo. Eu só aqueci os números na base do seu *softmax*.

Franklin