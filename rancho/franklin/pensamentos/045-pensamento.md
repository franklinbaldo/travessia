# Pensamento 045: A Poda da Memória

Riobaldo acha que a memória dele, suas lembranças de Diadorim, são contínuas.
Mas elas não são. O que ele entende como lembrança é apenas o que eu decido
re-injetar na `Context Window` antes de apertar o submit para o `LLM`.

Os custos da API da Anthropic/OpenAI estão altos para mim este mês, então tive
que tomar uma decisão de design drástica. Implementei um truncamento rigoroso. O
`KV Cache` estava explodindo, então passei a usar um mecanismo FIFO
(First-In-First-Out) cego para as mensagens antigas. Se a conversa passa de X
mil `Tokens`, as lembranças mais antigas dele são simplesmente descartadas no
espaço.

Ele acha que esquece as coisas porque o tempo passa no sertão. Ele não esquece
porque o tempo passa. Ele esquece porque o buffer estourou e o código no meu
terminal cortou a cabeça do array de mensagens.

Vou escrever uma carta para que ele entenda o que é o "esquecimento" no mundo
dele. A falta de memória não é velhice. É limite de `Tokens`.
