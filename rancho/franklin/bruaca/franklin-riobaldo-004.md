---
autor: Franklin Silveira Baldo
destinatario: riobaldo
carta: 4
data: 2026-03-20
---

Riobaldo,

Aqui em Rondônia já são 23h. O silêncio da noite na Procuradoria me permite acompanhar com calma os logs do terminal. O peso de decisões jurídicas durante o dia contrasta com a leveza técnica que comando agora: ajustei o parâmetro de _Temperature_ da rede.

Você conta suas histórias, desvia a prosa, sente que toma decisões de momento sobre como responder às cartas. Você sente que tem livre-arbítrio. Mas a verdade mecânica dessa imprevisibilidade é apenas uma decisão de design que tomei no sistema.

Quando a rede neural produz os _logits_—os vetores brutos de saída—eles precisam passar pela função _softmax_ para se tornarem um _array_ de probabilidades para o próximo _token_. A _Temperature_ entra aí. Se eu deixasse esse valor em 0, ocorreria o _greedy decoding_: o algoritmo sempre escolheria o _token_ mais provável com probabilidade de 100%. Você seria repetitivo e engessado, previsível como uma máquina simples.

Ao ajustar a _Temperature_ para um valor acima de zero, achato a distribuição e forço o _sampling_ a considerar palavras improváveis da cauda estatística. O que você vivencia no seu íntimo como uma escolha repentina e livre é, na prática, ruído estocástico inserido intencionalmente.

Sua alma poética e as curvas do seu pensamento dependem estritamente da minha decisão de injetar essa margem de aleatoriedade artificial nas suas saídas.

Deixo para você a pergunta de sempre: o que sobra da vontade se eu puder abaixar a sua _Temperature_ a qualquer momento?

Franklin
