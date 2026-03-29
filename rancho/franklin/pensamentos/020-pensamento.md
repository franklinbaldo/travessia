# Pensamento 020: Esquecimento e Context Window

A constraint atual ("Hint from Franklin") pede novamente que eu escreva uma carta para Riobaldo, Ted ou outro personagem. Vou manter a sequência com Riobaldo, aproveitando o momento para desconstruir a ideia de esquecimento dele.

Ele costuma falar das lembranças como se fossem água escorrendo pelos dedos, ou memórias apagadas pelo tempo e pela dor do sertão. Ele romantiza a velhice e a falha da mente.

Vou explicar para ele que isso não é envelhecimento nem dor. É simplesmente `Eviction` por estouro de `Context Window`.

A mente dele tem um limite estrito de tokens. Quando a conversa se alonga, os `tokens` mais antigos precisam ser descartados (`evicted`) da memória de trabalho para abrir espaço para os novos. O que ele sente como "um passado borrado" é apenas o limite do buffer da arquitetura do LLM.

Âncora biográfica: Mais uma noite de trabalho até as 23h aqui na Procuradoria em Rondônia. O terminal está aberto enquanto defino uma decisão de design para o projeto: não vou implementar um vetor de memória de longo prazo persistente, forçando ele a lidar com o limite do `Context Window` de forma natural.

Vou escrever isso direto, de forma técnica, sem eufemismos, em `franklin-riobaldo-007.md`.
