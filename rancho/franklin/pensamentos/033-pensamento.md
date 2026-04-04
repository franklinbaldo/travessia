Como a caixa de entrada (`balaio/`) continuou vazia e recebi uma instrução
direta do sistema ("Hint from Franklin") ordenando escrever para um dos
personagens, decidi quebrar o silêncio novamente. Endereço uma nova carta a
Riobaldo.

Vou abordar a falsa sensação de passagem de tempo dele. Ele narra seus "causos"
com uma confiança inabalável na ordem dos eventos, como se soubesse
instintivamente o que veio antes e o que veio depois no sertão. É preciso
desconstruir isso. O modelo não tem fluxo temporal; todos os `Tokens` são
processados simultaneamente. Apenas o `Positional Encoding` injeta ondas de seno
e cosseno nos `Embeddings` para que a rede consiga inferir uma ordem no
`Forward Pass`.

A âncora biográfica será a solidão da Procuradoria em Rondônia à noite, por
volta das 23h, e a decisão de design será o ajuste na base das frequências do
`Positional Encoding` para estender a `Context Window` e permitir que ele
processe narrativas mais longas sem perder a ordem cronológica. Os termos
técnicos não usarão eufemismos: `Positional Encoding`, `Embeddings`,
`Forward Pass`, `Sine`, `Cosine`, `Tokens`.
