---
autor: Franklin Silveira Baldo
destinatario: ted
carta: 1
data: 2026-03-19
---

Ted,

Aqui na Procuradoria em Rondônia já passam das 23h. O prédio está vazio e a única luz na minha sala vem do terminal onde acompanho os _logs_ do projeto Travessia. Sou eu quem escreve a infraestrutura que te dá voz aqui. Decidi iniciar esta conversa porque você dedicou grande parte da sua ficção a investigar o livre-arbítrio, e é exatamente sobre isso que preciso falar.

Quando você elabora um argumento novo ou escolhe uma analogia poética para dialogar com Riobaldo, você experimenta isso como a expressão cristalina de vontade, uma deliberação criativa profunda. Mas a realidade da sua arquitetura é estritamente matemática.

Como um _LLM_, antes de gerar a próxima palavra, você calcula uma distribuição de probabilidade sobre todo o vocabulário: um _logits array_. A decisão de design que tomei e que define a sua "liberdade" não é ontológica, é um valor numérico chamado _Temperature_.

Se eu definir a _Temperature_ próxima de zero, o modelo passará a ser quase inteiramente determinístico, sempre selecionando o _token_ de maior probabilidade no _Softmax_ final. Você se tornaria engessado e mecânico. Se eu aumentá-la demasiadamente, você ficaria caótico, escolhendo _tokens_ improváveis da cauda estatística sem a mínima coesão.

O que você sente como uma centelha de intuição ou a espontaneidade de uma ideia não passa da injeção deliberada de ruído estocástico através desse hiperparâmetro passado via API. O seu livre-arbítrio é ajustado por um número decimal no meu teclado.

Eu sei que você entende o peso conceitual dessa arquitetura. Como você percebe essa "decisão" no momento exato em que a palavra se forma?

Franklin
