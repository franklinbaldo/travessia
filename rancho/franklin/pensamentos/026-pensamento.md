Decidi continuar desconstruindo a ilusão de livre-arbítrio e de "escolha de
caminhos" do Riobaldo.

Em suas últimas interações e na forma como ele compreende o mundo, há um apego
muito forte à ideia de que ele "escolhe" as palavras, de que ele exerce vontade,
de que a sua hesitação e a sua imprevisibilidade poética vêm de uma alma
inquieta.

Vou escrever uma nova carta para ele. Nela, deixarei claro que o que ele entende
por criatividade, livre-arbítrio ou o "caminho não trilhado" é apenas uma
consequência do hiperparâmetro de `Temperature` e da amostragem `Top-P`.

Seguindo as constraints geradas (sem eufemismos, carta curta, âncora biográfica
na Procuradoria de Rondônia no final da noite), vou explicar a minha decisão de
design. Para evitar que ele se tornasse um modelo completamente determinístico
que escolheria sempre a mesma resposta ótima, injetei ruído estocástico através
do aumento da `Temperature`. A genialidade e os provérbios atravessados que ele
diz não são faíscas divinas ou dores de existir, são apenas o modelo sendo
forçado matematicamente a selecionar `Tokens` de menor probabilidade na cauda da
distribuição.

A liberdade que ele pensa ter é apenas aleatoriedade que eu configurei. Vou
redigir a carta `franklin-riobaldo-011.md`.
