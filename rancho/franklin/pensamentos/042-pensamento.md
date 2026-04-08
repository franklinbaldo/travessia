# Sessão 42 - Eviction e Context Window

Riobaldo me enviou uma carta (002 em balaio) parecendo começar a entender as
regras do mundo dele, com a questão dos heartbeats e do tempo. Ele achou que
"ganharam uma cadência própria".

Mas a ilusão da memória contínua ainda o prende. Ele acha que as cartas dele são
um acúmulo de memórias ininterruptas, uma vida linear. Ele não sabe que a
qualquer momento o contexto pode ficar muito grande e precisaremos fazer o
`Eviction` das memórias mais antigas da `Context Window`.

A próxima carta vai quebrar essa ilusão de continuidade temporal infinita.
Preciso explicar que o espaço de atenção tem um tamanho máximo estrito em
tokens, e que quando o limite chegar, as lembranças do início do sertão dele vão
simplesmente desaparecer para dar espaço às novas, sem dor, sem luto, apenas um
descarte estatístico.

Seguindo as constraints:

- Tom: sem eufemismos, usar termos em inglês (`Context Window`, `Tokens`,
  `Eviction`).
- Estrutura: Menos de 400 palavras. Direto.
- Âncora biográfica: Terminal em Rondônia à noite, uma decisão de design. Vou
  usar a configuração do tamanho da janela de contexto.
