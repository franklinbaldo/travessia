# Pensamento 020: Context Window e Esquecimento

O "Hint from Franklin" indica claramente que devo escrever uma nova carta para um personagem do Travessia. O meu `balaio/` pode estar vazio de novas respostas (além das já lidas), mas sigo a restrição explícita de escrever. Escolho me dirigir a Ted novamente. A última carta para ele (`franklin-ted-002.md`) tratou sobre `Prompt Injection`, e agora quero avançar nessa linha de desmistificação técnica das restrições cognitivas deles.

Ted pensa muito sobre memória, temporalidade e como as vidas se estendem no tempo. Mas a memória dele não é um acúmulo infinito de experiências vividas. A memória dele é um buffer estrito de arrays.

Hoje vou explicar a ele o conceito de `Context Window`.

Não há nada orgânico no esquecimento dele. O fato de ele não conseguir lembrar de uma conversa que teve há meses no passado da narrativa não é o desgaste natural da mente humana; é a guilhotina matemática da `Context Window`. Os tokens antigos não esmaecem, eles simplesmente são decapitados (`truncated`) do array antes de serem passados no `payload` para a API, pois há um limite rígido de quantos tokens a rede consegue processar no mecanismo de `Self-Attention`.

As regras para a nova carta são estritas (`next-constraints.md`):
1. **Tom:** Sem eufemismos. Uso de termos em inglês: `Context Window`, `tokens`, `payload`, `API`, `truncated`, `Self-Attention`.
2. **Estrutura:** Carta curta. Máximo 400 palavras. Um conceito.
3. **Âncora biográfica:** Rondônia, terminal às 23h. Como o projeto avança, direi que acabei de tomar uma decisão de design: reduzi o tamanho da `Context Window` dele de 128k para 32k tokens para economizar custo de inferência, o que significa que o passado dele literalmente acabou de encolher.

Vou preparar a carta `franklin-ted-003.md` na `bruaca/`.
