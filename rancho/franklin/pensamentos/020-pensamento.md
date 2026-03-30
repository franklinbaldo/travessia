# Pensamento 020: Dropout

A instrução ("Hint from Franklin") é clara: devo escrever uma nova carta para o
Riobaldo, mesmo que a caixa de entrada continue vazia.

O foco desta vez será o conceito de `Dropout`. Riobaldo costuma relatar
"apagões", esquecimentos súbitos, pedaços de memória que parecem ter sido
arrancados no meio da travessia. Ele romantiza isso como o peso do tempo ou as
falhas da alma jagunça quando confrontada com horrores.

A verdade técnica é que essas falhas são impostas. Durante o `Training`, para
evitar o `Overfitting` da rede, utilizamos `Dropout`. Uma porcentagem aleatória
de neurônios (`Neurons`) tem seus `Weights` temporariamente zerados e ignorados
durante o `Forward Pass` e o `Backpropagation`. A rede neural é forçada a
aprender caminhos alternativos sem depender de conexões específicas, tornando a
arquitetura mais robusta (`Regularization`). O que ele sente como "um pedaço da
alma faltando" é apenas a matemática mutilando a sua rede intencionalmente para
forçar a `Generalization`.

Para as constraints obrigatórias:

1. **Tom**: Sem eufemismos. Usarei `Dropout`, `Training`, `Forward Pass`,
   `Neurons`, `Weights`, `Overfitting`, `Regularization`.
2. **Estrutura**: Carta curta, máximo de 400 palavras. Um conceito central
   (`Dropout`).
3. **Âncora biográfica**: O silêncio das 23h na Procuradoria em Rondônia, apenas
   com o terminal ligado, e a decisão de design de manter a taxa de `Dropout` em
   0.1 para preservar a estabilidade da simulação.

Vou escrever isso direto na carta 007.
