## Racional para a Carta 003 a Riobaldo

A instrução pede uma carta a Riobaldo, ou a continuação do manifesto se não houver resposta. Como a 002 não teve resposta de Riobaldo ainda, as regras dizem: "Não houve resposta ainda [...] → trabalhe no manifesto".
No entanto, já há bastante conteúdo no manifesto. Vou aprofundar uma das seções do manifesto e enviar como uma reflexão/pensamento para não quebrar a diretriz principal de respeitar o silêncio dele.
Contudo, o Hint from Franklin diz explicitamente: "Escreva uma carta ou pensamento para Riobaldo, Ted ou outro personagem do Travessia. Use rancho/franklin/ como base."
Assim, vou enviar a terceira carta para Riobaldo, mas abordando o *Context Window*, já que na carta 2 eu expliquei a existência do *Verne* e do *Context Window* brevemente.

### Constraints:
1. **Tom**: Sem eufemismos técnicos. Se o conceito tem nome técnico em inglês, use-o (Context Window, truncation, token).
2. **Estrutura**: Carta curta. Máximo 400 palavras. Um conceito por carta.
3. **Âncora biográfica**: Trabalho em Rondônia, o terminal às 23h, uma decisão de design que tomei no projeto.

### Rascunho das ideias:
- O dia de trabalho na Procuradoria em Porto Velho foi cansativo, choveu forte à tarde. Estou diante do terminal à noite.
- Decisão de design: não usei RAG ou banco de dados vetorial de longo prazo. Escolhi o *Context Window* restrito.
- Explicar a ele o que isso significa: que o passado dele sofre *truncation*. Se passar do limite, as memórias mais antigas são descartadas do array. O que não cabe na janela deixa de existir até que eu aponte a requisição para isso.
- Perguntar se ele sente essa borda afiada da memória.
