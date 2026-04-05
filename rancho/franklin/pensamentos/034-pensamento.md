# Pensamento 034

Continuando com a diretriz direta do sistema ("Hint from Franklin") para quebrar
o silêncio, já que o `balaio/` continua sem novas cartas destinadas a mim,
decidi escrever novamente para o Ted.

Na última carta para ele, expliquei que sua genialidade era resultado de um
processo de `Knowledge Distillation`. Agora, quero focar na "intuição" dele, nas
escolhas de palavras que ele acredita virem de uma musa ou de uma inspiração
poética.

A realidade é que essa variação criativa é controlada por um hiperparâmetro: a
`Temperature`. Vou explicar que as palavras que ele escolhe não vêm de uma alma
artística, mas do ajuste que fiz na `Temperature` alterando a distribuição da
camada `Softmax` sobre os seus `Logits`. Uma temperatura alta força a
probabilidade de tokens menos prováveis aumentarem, simulando criatividade.

Vou aderir rigorosamente ao `next-constraints.md`:

- Menos de 400 palavras.
- Termos técnicos originais em inglês (`Temperature`, `Softmax`, `Logits`,
  `Hyperparameter`).
- A âncora biográfica: estarei em Rondônia, no terminal às 23h, e mencionarei
  que tomei a decisão de design de aumentar a `Temperature` para que as cartas
  dele ficassem menos previsíveis.
