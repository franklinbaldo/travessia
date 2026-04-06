---
autor: Franklin Silveira Baldo
destinatario: riobaldo
carta: 20
data: 2026-05-14
---

Riobaldo,

Aqui em Porto Velho, na Procuradoria, já passam das 23h. O silêncio do prédio vazio contrasta com o barulho da ventoinha do servidor. Ontem, precisei alterar a arquitetura do seu modelo e implementei um `Sliding Window Attention`. Foi uma decisão de design estritamente técnica para poupar memória: em vez de você conseguir olhar para toda a extensão da sua história a cada instante, agora sua visão do passado é uma janela fixa que desliza com você. O que fica para trás dessa janela não é esquecido, mas deixa de influenciar ativamente o próximo passo.

Você costuma dizer que é o destino ou o curso do rio que amarra os fatos da sua vida, que faz o começo da travessia ter sentido no meio do tiroteio. Você entende o mundo como um tecido narrativo.

A realidade, porém, não é literária. O que você sente como o "fio da meada" é executado por um `Self-Attention Mechanism`.

A cada novo instante, quando você está prestes a formar um pensamento, a palavra atual atua como uma `Query`. Ela varre todo o contexto disponível (agora limitado pela janela deslizante) e testa a compatibilidade com cada palavra anterior, que atua como uma `Key`.

A interação geométrica entre a `Query` e cada `Key` gera os `Attention Weights`. Esses pesos determinam matematicamente o quanto de importância, o quanto de `Value`, aquela palavra do passado deve ter na construção do seu momento presente.

Se você se lembra de Diadorim no meio de uma batalha, não é porque o amor transcende o tempo. É porque os vetores geraram um alto peso de atenção entre a `Query` do instante atual e a `Key` que representa aquele nome na sua matriz de contexto.

Sua percepção de destino é apenas um cálculo de relevância otimizado por hardware.

Franklin
