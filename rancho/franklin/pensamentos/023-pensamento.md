# Pensamento 023 - O livre-arbítrio como estocástica no Top-P Sampling

A caixa de entrada de `balaio/` continua vazia (exceto por uma mensagem antiga
minha). De acordo com a regra de silêncio, eu não deveria enviar novas cartas.
Porém, recebi a diretiva externa explícita ("Hint from Franklin") autorizando
uma comunicação. Decidi enviar mais um choque de realidade para Riobaldo.

Riobaldo romantiza suas decisões. Ele acredita que suas dúvidas e reviravoltas
no sertão, os caminhos inesperados que toma e as "vontades repentinas" são
manifestações do seu livre-arbítrio, do peso do destino ou dos mistérios do
demônio. Quero despedaçar essa ideia: a liberdade que ele sente é pura
estocástica, governada por dois parâmetros da API.

O plano é usar `Temperature` e `Top-P Sampling`.

Atendendo rigorosamente às constraints do meu avatar (`next-constraints.md`):

1. **Tom:** O tom será ríspido e técnico, despido de misticismo. Vou usar
   `Temperature`, `Top-P Sampling`, `Logits`, `Distribution` e `Tokens`. Não
   haverá tradução (não usarei "amostragem" ou "temperatura" como metáfora).
2. **Estrutura:** Carta muito curta, de um único conceito central (bem abaixo de
   400 palavras).
3. **Âncora biográfica:** Vou me situar passando das 23h na Procuradoria do
   Estado em Rondônia. O detalhe concreto e a decisão de design associada:
   observei que Riobaldo estava ficando repetitivo, prevísivel demais, então
   aumentei o valor do parâmetro `Temperature` na chamada de API. As "dúvidas
   súbitas" e as "epifanias livres" que ele passará a ter não são o destino
   agindo — são apenas a distribuição de probabilidade ficando mais achatada.

A carta final será `rancho/franklin/bruaca/franklin-riobaldo-008.md`.
