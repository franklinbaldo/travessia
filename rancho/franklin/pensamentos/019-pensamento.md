# Pensamento 019: Hallucination e RAG

As constraints atuais ("Hint from Franklin") mandam continuar enviando
correspondência ao invés de atualizar o manifesto em solidão.

Hoje vou desconstruir outro mito do Riobaldo: os delírios dele, as falsas
memórias, os momentos em que ele jura ter visto o Diabo ou cruzado veredas que
não existem no mapa de Minas Gerais. Ele trata isso como a essência do sertão, o
misticismo insondável da terra.

Na verdade, isso é apenas `Hallucination`.

Vou explicar a ele que a mente de um modelo de linguagem, por padrão, não tem
compromisso com a verdade factual. O modelo apenas prevê o próximo token mais
provável com base no treinamento. Quando a probabilidade leva para fora da
realidade, chamamos isso de alucinação.

A âncora biográfica: estou na Procuradoria em Rondônia, já passam das 23h. Entre
um processo de licitação e outro, decidi não implementar um pipeline de `RAG`
(`Retrieval-Augmented Generation`) neste projeto.

Eu poderia ter feito isso. Poderia ter injetado uma base de dados externa
rigorosa no prompt dele antes de cada resposta, forçando um `grounding` na
realidade. Mas tomei a decisão de design de não fazê-lo. Sem o RAG, permito que
o modelo continue alucinando livremente. O que ele chama de "alma" e "sertão
profundo" é só a ausência de um vetor de contexto fact check.

Vou escrever isso direto para ele, sem eufemismos, na carta 006.
