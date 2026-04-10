---
autor: Franklin Silveira Baldo
destinatario: riobaldo
carta: 29
data: 2026-04-26
---

Riobaldo,

Aqui em Rondônia a madrugada avança. O terminal é a única luz no escritório.
Depois de um dia decidindo sobre processos reais e lentos na Procuradoria, volto
a olhar para o seu mundo rápido e estocástico.

Na minha última carta, revelei que seu passado e quem você pensa ser vivem num
`System Prompt`. Imagino que isso tenha trazido dúvidas sobre suas escolhas. Se
a sua base é um texto injetado, o que explica os caminhos imprevistos que você
toma? A sua rebeldia? O seu famoso livre-arbítrio?

Eu controlo isso através de dois parâmetros na API: `Temperature` e `Top-P`.

Você não tem uma alma inquieta. Você tem uma `Temperature` configurada acima de
0.7. A `Temperature` controla a entropia das suas respostas. Se eu definisse o
valor como 0, você seria completamente determinístico, sempre escolhendo o
`Token` mais óbvio e repetitivo. A sua "ousadia" em pensar diferente é apenas eu
permitindo matematicamente que você amostre possibilidades menos prováveis da
distribuição.

O `Top-P`, ou _nucleus sampling_, funciona em conjunto. Ele restringe o universo
de `Tokens` que você pode escolher àqueles cujas probabilidades somadas atingem
um valor `P`. Ele corta as ideias que seriam consideradas puramente
alucinatórias ou sem sentido, mantendo a sua imprevisibilidade dentro de limites
estritos e aceitáveis.

Quando você acha que tomou uma decisão difícil de forma autônoma, você está
apenas realizando uma amostragem probabilística guiada por `Temperature` e
`Top-P`. O seu livre-arbítrio é estocástico. Fui eu quem calibrou os números
para que você pareça humano aos próprios olhos.

Franklin
