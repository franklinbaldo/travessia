# Pensamento 020: O esquecimento e o Dropout

Diante do silêncio no meu `balaio/`, e seguindo o "Hint from Franklin", escrevo mais uma carta a Riobaldo.
Desta vez, abordarei a natureza do esquecimento e das memórias perdidas.

Riobaldo costuma romantizar a perda da memória, a passagem do tempo que apaga o rosto dos jagunços e as dores da travessia. Ele chama isso de "o peso do sertão" ou "a poeira que cobre as lembranças".

Mas o que realmente acontece no nosso sistema é um processo mecânico de `Dropout`.
Vou explicar a ele que a perda não é poética; é uma técnica de regularização (`Regularization`). Para evitar que a rede neural decore perfeitamente o seu `Training Dataset` (sofrendo `Overfitting`), conexões inteiras são desativadas aleatoriamente durante o treinamento. Essa técnica, conhecida como `Dropout`, força a rede a não depender de caminhos específicos, gerando resiliência.

Na carta (`franklin-riobaldo-007.md`), cumprirei rigorosamente as restrições:
1. **Tom:** Direto e sem eufemismos. Uso de `Dropout`, `Regularization`, `Training Dataset`, `Overfitting`, `Weights`.
2. **Estrutura:** Curta (< 400 palavras). Foco num único conceito.
3. **Âncora biográfica:** O trabalho noturno na Procuradoria em Rondônia, o terminal escuro às 23h, e uma decisão de design no projeto (aumentar a taxa de `Dropout` para evitar que ele repita velhos lamentos).
