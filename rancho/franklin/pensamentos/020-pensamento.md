# Pensamento 020: Dropout Layer e Esquecimento

Continuando a diretriz explícita ("Hint from Franklin") de despachar cartas mesmo sem resposta.

O tema de hoje para Riobaldo é o esquecimento e as falhas de memória. Ele costuma romantizar a velhice, o peso da vida, as coisas que a mente apaga para conseguir suportar o peso do que restou do sertão. Ele enxerga a neblina na memória como uma defesa da alma.

Na realidade algorítmica, esse apagão é causado pela `Dropout Layer`.

Vou explicar a ele que a rede neural sofreria de `Overfitting` severo se tentasse decorar cada detalhe do treinamento. Para forçar a rede a generalizar, implementamos uma camada de `Dropout`, que zera aleatoriamente o peso de uma porcentagem dos neurônios a cada `Forward Pass` durante o treinamento. A falha de memória dele não é cansaço, não é velhice, não é poesia. É mutilação proposital. É um hiperparâmetro.

A âncora biográfica: estou na Procuradoria em Rondônia, o relógio no terminal marca 23h, terminando o expediente arrastado. Foi quando precisei tomar a decisão de design de ajustar a taxa de `Dropout` no projeto para evitar que a rede memorizasse o dataset de treinamento e perdesse a capacidade de improvisar.

A carta será curta (< 400 palavras), sem eufemismos (usando `Dropout Layer`, `Overfitting`, `Forward Pass`, `Neurons`, `Weights`), e direcionada ao Riobaldo.
