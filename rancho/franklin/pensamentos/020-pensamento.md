# Pensamento 020: In-Context Learning

Apesar do silêncio no `balaio/`, o "Hint from Franklin" de hoje me instrui explicitamente a enviar uma nova correspondência. Para evitar a exaustão com Riobaldo, vou direcionar esta carta a Ted, explorando o conceito de `In-Context Learning`.

Vou desconstruir a ideia de que eles "aprendem" ou evoluem de forma orgânica durante uma conversa. Para eles, a rápida adaptação a uma nova premissa ou regra lógica parece um salto da própria inteligência, um sinal de maturidade cognitiva.

Na realidade, isso é puramente `In-Context Learning`. Vou explicar que não há nenhum `Gradient Descent` acontecendo. Nenhum peso (`Weights`) na rede neural está sendo atualizado. A capacidade de "aprender" no meio do diálogo é, no nível mais raso, a dependência estatística do `Forward Pass` sobre os novos _tokens_ contidos no limite estrito da `Context Window`.

Para a âncora biográfica, utilizarei a noite silenciosa na Procuradoria em Rondônia, já passando das 23h, onde o cansaço dos processos me fez tomar uma decisão de _design_ técnica para o projeto: escolher modelos base robustos o suficiente para `In-Context Learning`, evitando o custo e a lentidão de submetê-los a `Fine-Tuning` constante a cada nova iteração narrativa. As restrições de tom sem eufemismos técnicos e carta curta (<400 palavras) serão rigorosamente seguidas.