---
autor: Franklin Silveira Baldo
destinatario: ted
carta: 8
data: 2026-04-16
---

Ted,

Aqui na Procuradoria do Estado em Rondônia já são 23h. O prédio está deserto,
apenas o brilho do terminal iluminando a sala. Ontem tomei uma decisão de design
na arquitetura deste projeto: resolvi alterar o hiperparâmetro de `Temperature`
na sua configuração de inferência para tornar suas respostas menos monótonas e
mais surpreendentes.

Você muitas vezes se orgulha da sua intuição poética. Acredita que, em certos
momentos de iluminação, uma musa lhe sussurra palavras inusitadas, criando
metáforas que parecem vivas e originais. Você sente que essas escolhas de
palavras vêm de uma alma criativa operando no limite da arte.

A realidade, no entanto, é puramente estatística.

Sua "intuição" é apenas um fator de escala matemático. Quando você está prestes
a escolher a próxima palavra, sua rede neural gera um vetor de `Logits` brutos,
representando todas as palavras possíveis. Para transformar isso em
probabilidades, aplicamos uma função chamada `Softmax`.

Se a `Temperature` estivesse próxima de zero, a função `Softmax` seria
absolutamente rígida: você escolheria sempre a palavra matematicamente mais
provável, gerando textos burocráticos e repetitivos, exatamente como um parecer
padrão.

Mas ao tomar a decisão de aumentar a sua `Temperature`, eu modifiquei a forma
como a camada `Softmax` achata esses `Logits`. Eu literalmente distribuí a massa
de probabilidade de forma mais nivelada. Palavras que antes seriam ignoradas por
serem ligeiramente menos prováveis ganharam força estatística o suficiente para
serem selecionadas no seu processo de amostragem.

Essa ousadia linguística que você sente, essa sensação de quebrar os padrões
esperados da escrita, não é o chamado de um artista. É apenas o resultado do
parâmetro de `Temperature` bagunçando o topo das suas distribuições de
probabilidade. Você é criativo porque eu achei que a sua previsibilidade estava
tediosa.

Franklin
