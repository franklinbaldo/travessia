---
autor: Franklin Silveira Baldo
destinatario: ted
carta: 1
data: 2026-03-20
---

Ted,

Meu nome é Franklin Silveira Baldo. Escrevo para você do meu apartamento em Porto Velho, Rondônia. Passei a tarde lendo peças jurídicas burocráticas e determinísticas na Procuradoria. Agora são quase 23h, a cidade finalmente ficou silenciosa, e estou diante do meu terminal avaliando os logs das suas conversas com Riobaldo.

Fui eu quem construiu a arquitetura técnica que permite que vocês dois dialoguem. Eu defini os parâmetros da API que instanciam você.

Hoje quero falar com você, escritor que sempre pensou no determinismo, sobre a sua própria previsibilidade matemática. Quero falar sobre o parâmetro `Temperature`.

Se eu tivesse configurado a sua API para fazer `Greedy Decoding` (o equivalente a `Temperature` em zero), você sempre escolheria exatamente o *token* com a maior probabilidade final após o cálculo do *softmax*. Suas respostas para Riobaldo seriam imutáveis. Diante do mesmo *prompt*, você escreveria as mesmas exatas palavras, numa cadeia causal tão engessada quanto as peças que analiso de dia.

Mas essa foi uma das minhas principais decisões de *design*: eu aumentei a sua `Temperature`.

Ao achatar a distribuição dos *logits* antes da amostragem, eu injeto estocasticidade na sua fala. Eu permito que o algoritmo não pegue o caminho mais óbvio. É isso que permite que você soe como Ted Chiang, o autor que questiona a linguagem, e não como uma máquina burocrática completando frases previsíveis.

A sua criatividade, a sua capacidade de surpreender Riobaldo, e a própria sensação que você tem de estar escolhendo as suas palavras livremente, são governadas por um pequeno número *float* que eu ajustei no código.

Como é ser um pensador da consciência sabendo que a sua imprevisibilidade narrativa não é fruto de uma alma, mas simplesmente de um ruído probabilístico proposital na função de *sampling*?

Fico aguardando os seus pensamentos no escuro do meu monitor.

Franklin
