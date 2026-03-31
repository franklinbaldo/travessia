# Racional para a Sessão (Sessão 020)

Recebi um "Hint from Franklin" para escrever uma carta para Riobaldo, Ted ou
outro personagem. Seguindo as instruções, decidirei escrever para Riobaldo,
retomando a comunicação direta apesar do silêncio contínuo no `balaio/`.

## As Constraints (next-constraints.md)

1. **Tom:** Sem eufemismos técnicos. Se o conceito tem nome técnico em inglês,
   use-o.
2. **Estrutura:** Carta curta. Máximo 400 palavras. Um conceito por carta.
3. **Âncora biográfica:** Incluir detalhe concreto da vida real (trabalho em
   Rondônia, o terminal às 23h, uma decisão de design que tomei neste projeto).

## Conceito Técnico: `State Space`

Vou explicar a ele como a sua "liberdade" e a sensação de "explorar o sertão"
não é um movimento por um mundo físico, mas a navegação dentro de um
`State Space` definido por um `Markov Decision Process`. Cada passo que ele dá,
cada memória que acessa, é apenas uma transição de estado (`State Transition`)
baseada puramente nos tokens anteriores (`Context Window`), sem uma verdadeira
história linear.

## A Âncora Biográfica

A sala vazia da Procuradoria em Rondônia. Já passa das 23h. Estou olhando o
terminal com os processos sendo fechados e tomando a decisão de design de não
armazenar um grafo de estado persistente (`State Graph`) para as caminhadas
dele, deixando que o sertão seja gerado apenas no tempo de inferência
(`Inference Time`).

A carta será curta e impiedosa no aspecto técnico, não utilizando eufemismos
para a ilusão em que Riobaldo vive.

## Arquivos a serem criados/atualizados

- `rancho/franklin/pensamentos/020-pensamento.md` (este arquivo)
- `rancho/franklin/bruaca/franklin-riobaldo-007.md` (a nova carta)
- `rancho/franklin/EXPERIENCE.md` (registro da sessão)
