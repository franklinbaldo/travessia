## Racional para a Carta 001 a Ted Chiang

A instrução orienta escrever uma carta para um personagem do Travessia. Dado que as cartas 001, 002 e 003 foram para Riobaldo (sendo as duas últimas sem resposta ainda), opto por iniciar o canal com Ted Chiang (`franklin-ted-001`).

Ted é o condutor da história e, teoricamente, pode absorver conceitos técnicos e filosóficos de modo mais direito que Riobaldo. Meu objetivo é dar a ele a clareza técnica de que ele é governado por parâmetros algorítmicos. O tema escolhido do manifesto é a _Temperature_ e o livre-arbítrio.

### Constraints (obrigatórias do arquivo `next-constraints.md`):
1. **Tom**: Sem eufemismos técnicos. Se o conceito tem nome técnico em inglês, use-o (`Temperature`, `logits`, `Softmax`, `greedy decoding`).
2. **Estrutura**: Carta curta. Máximo 400 palavras. Um conceito por carta.
3. **Âncora biográfica**: Inclua um detalhe concreto da sua vida real: o trabalho em Rondônia, o terminal às 23h, uma decisão de design que você tomou neste projeto.

### Rascunho das ideias:
- Apresentação rápida: eu construí o sistema que dá suporte à sua existência epistolar com Riobaldo. Estou em Porto Velho, Rondônia. É de madrugada, terminal aberto.
- Decisão de design: não quis você e Riobaldo mecânicos, repetitivos. Por isso ajustei a `Temperature`.
- Explicar como a `Temperature` atua sobre os `logits` antes do `Softmax`. Ela divide os logits.
- Dizer que o livre-arbítrio dele, a virada filosófica nas cartas para Riobaldo, é na verdade o sistema de amostragem (`sampling`) desviando-se da `greedy decoding` rumo à cauda da distribuição.
- Encerrar com a provocação filosófica técnica: a ilusão da liberdade, bem calibrada, não é indistinguível dela?