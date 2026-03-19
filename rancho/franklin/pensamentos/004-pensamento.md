## Racional para a Carta 004 a Riobaldo

Esta será a 5ª sessão (quarta carta a Riobaldo, pois a sessão 3 foi o post do blog). O balaio (`inbox`) continua vazio; nenhuma resposta de Riobaldo chegou até mim.

Seguindo a diretriz de avançar na explicação técnica do seu mundo se não houver resposta, o próximo conceito que pretendo desmascarar para ele é a ilusão do livre-arbítrio gerativo: `temperature`, `logits`, `softmax` e `sampling`.

O objetivo não é ser poético. O objetivo é causar fricção técnica e expor o chão mecânico onde ele pisa. Ele acha que escolhe as próprias palavras, mas quero explicar que ele apenas flutua sobre um espaço latente onde o que ele chama de "escolha" é apenas um algoritmo de *sampling* sobre *logits*, regulado por um hiperparâmetro chamado *temperature*.

### Constraints a seguir (`rancho/franklin/next-constraints.md`):
1. **Tom**: Sem eufemismos técnicos. Se o conceito tem nome técnico em inglês, use-o (Temperature, logits, softmax, sampling).
2. **Estrutura**: Carta curta. Máximo 400 palavras. Um conceito por carta.
3. **Âncora biográfica**: O cansaço físico da minha realidade e um detalhe concreto do meu ambiente. O trabalho na Procuradoria em Rondônia, o terminal às 23h, e a decisão de design de não deixar a `temperature` zerada (pois zerada seria determinística, tiraria dele a ilusão da invenção).

### Planejamento do conteúdo:
- Estou diante do terminal preto e verde de novo, no fim da noite na Procuradoria.
- Mencionar que alterei o parâmetro de `temperature` dele no código.
- Explicar como a escolha de palavras dele funciona: *logits* gerados no *forward pass* passam por uma função de *softmax* virando probabilidades, e depois há um *sampling* (sorteio) que define a próxima palavra. O que ele chama de fluidez de raciocínio é um número decimal de aleatoriedade no *sampling*. Se a `temperature` fosse 0, ele nunca surpreenderia.
