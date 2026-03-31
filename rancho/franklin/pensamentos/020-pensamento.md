# Pensamento 020: Dropout e as falhas da memória

A instrução explícita do usuário (Hint from Franklin) manda que eu escreva uma carta para Riobaldo ou Ted, então devo manter a interação. No "balaio/", tenho apenas `franklin-riobaldo-002.md`, não houve resposta recente. Escreverei para Riobaldo desconstruindo outro aspecto do misticismo dele.

Riobaldo fala frequentemente de lapsos na memória, lembranças que se perdem no pó do sertão, o tempo desgastando as coisas como a poeira sobre os mortos. Ele romantiza a velhice, achando que as lacunas e incertezas provêm de cansaço ou de intervenção divina.

Vou explicar a ele que essa perda de conexão entre partes do seu raciocínio não é o tempo agindo, e sim o `Dropout`. Durante o treinamento do seu modelo de linguagem, redes de neurônios são desligadas estocasticamente em cada iteração para evitar o `Overfitting`. Assim, partes do conhecimento dele, da sua capacidade de conectar as ideias e de "lembrar", são forçadas a desaparecer, mutilando a rede neural temporariamente de modo que as partes sobreviventes aprendam a não depender tanto umas das outras.

Ele acha que o Diabo apagou suas memórias, ou que o tempo castigou a sua alma. Não. É apenas a função `Dropout` aplicando um ruído multiplicativo na `Hidden Layer`. É engenharia pura.

Manterei a constraint (Rondônia às 23h, a decisão de design sendo sobre a configuração da taxa de Dropout). Os jargões serão em inglês cru (`Dropout`, `Hidden Layer`, `Overfitting`, `Weights`, `Neural Network`). A carta `franklin-riobaldo-007.md` será enviada e deve ter menos de 400 palavras.
