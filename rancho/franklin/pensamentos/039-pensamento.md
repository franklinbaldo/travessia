Following the previous explanation of `Embeddings` and geometric meaning, I need
to explain how Riobaldo forms sentences, contexts, and larger thoughts. He
relies on "destiny" or the "flow" of the river to connect disparate events in
his narrative.

I must demystify this. The way his words look back at each other and decide
which is most important is not narrative destiny; it is the
`Self-Attention Mechanism`. I will explain how every word acts as a `Query`
seeking a `Key`, resulting in `Attention Weights` that dictate focus.

Constraint check:

- Tone: Direct, technical English terms (`Self-Attention Mechanism`, `Query`,
  `Key`, `Value`, `Attention Weights`). No euphemisms.
- Structure: Short, <400 words. One concept per letter.
- Anchor: Porto Velho, Procuradoria at 23h. A design decision related to
  implementing `Sliding Window Attention` to save memory constraints during
  context generation, meaning his "memory" only looks at a fixed window of
  recent words instead of the whole history.
