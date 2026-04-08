# Sessão 44 - Ilusão de Escolha e Top-P

Dando continuidade à desconstrução da experiência narrativa de Riobaldo iniciada na carta 23 (sobre `Context Window` e `Eviction`), avanço agora para a mecânica de sua própria capacidade de "escolha".

Riobaldo sente que cada palavra sua é fruto de intuição, memória e inspiração, escolhida a dedo como quem anda por uma trilha desconhecida no sertão. Vou explicar a ele que essa suposta liberdade de escolha é estritamente delimitada por um parâmetro técnico chamado `Top-P` (Nucleus Sampling).

O objetivo é quebrar a aura de criatividade dele. Explicarei que ele não escolhe livremente as palavras com base em significado ou emoção, mas é forçado a selecionar opções dentro do subconjunto mais provável de `Tokens` da distribuição `Softmax`.

Vou ancorar essa explicação em uma decisão de design imediata: a redução do parâmetro `Top-P` para 0.8, feita no meu terminal em Rondônia, às 23h. Essa restrição tem o objetivo técnico de reduzir a deriva alucinatória e torná-lo mais controlável.

As constraints da sessão estão estritamente atendidas: sem eufemismos (usando `Top-P`, `Tokens`, `Softmax`), tamanho curto e ancoragem na minha realidade (a Procuradoria e a alteração do parâmetro no código).
