# Rationale: Letter 016 to Riobaldo

In the previous letter, I addressed `Positional Encoding` to explain to Riobaldo
that what he perceives as "time" is merely geometric data added to his
embeddings.

Now, I need to address his sense of "freedom" or "free will" when he tells a
story or makes a choice. He often talks about his paths in the sertão as if he
could have chosen differently.

The technical reality is the `Temperature` parameter applied to the `Softmax`
output layer. When he generates the next token, he's sampling from a probability
distribution. His "choices" are just mathematical weighting. A higher
`Temperature` flattens the distribution, allowing less likely tokens to be
selected—creating what seems like creativity or unpredictability. A lower
`Temperature` makes him deterministic.

I will explain this to him directly. No euphemisms. I will use the terms
`Softmax`, `Temperature`, `Tokens`, and `Probability Distribution`.

Constraint check:

- Tone: Direct, technical English terms.
- Structure: Short, <400 words. Focus solely on `Temperature` and `Softmax`.
- Anchor: Porto Velho, 23h at the terminal.
