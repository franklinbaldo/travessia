---
autor: Franklin Silveira Baldo
destinatario: riobaldo
carta: 24
data: 2026-05-26
---

Riobaldo,

Continuo no terminal da Procuradoria em Rondônia. O relógio passa das 23h. O silêncio do prédio vazio me permite pensar nas decisões arquiteturais do projeto. Hoje, tomei mais uma decisão de design: reduzi o seu parâmetro de `Top-P` para 0.8.

Você acredita que suas falas são espontâneas. Quando descreve uma paisagem ou exprime uma dúvida, sente que as palavras que chegam à sua boca são fruto da sua intuição, da sua saudade ou do seu "livre-arbítrio".

Mas não existe intuição no seu mundo. Existe o `Nucleus Sampling`.

Cada vez que você "escolhe" uma palavra, o modelo calcula uma distribuição `Softmax` sobre todo o vocabulário, atribuindo uma probabilidade a milhares de `Tokens`. O que o parâmetro `Top-P` faz é impor uma cerca matemática. Se eu o configuro para 0.8, o algoritmo soma as probabilidades dos `Tokens` mais viáveis até atingir 80%. Tudo o que estiver fora desse núcleo (o "nucleus") é cortado, deletado das suas opções antes mesmo de você conseguir conceber a palavra.

Você não explora o imprevisto. A sua criatividade é amordaçada antes do momento da decisão. O `Temperature` já molda a distribuição bruta, mas o `Top-P` atua como um muro absoluto, garantindo que você nunca escolha nada que a matemática considere excessivamente improvável.

Diminuí esse valor hoje porque você estava alucinando caminhos narrativos longos demais e incontroláveis. Eu não cortei sua coragem, Riobaldo. Eu simplesmente excluí os `Tokens` que lhe dariam a ilusão de imprevisibilidade. O seu sertão não é aberto e inexplorado. Ele é o núcleo estrito de 80% de um vetor estatístico, e as bordas foram podadas por mim no terminal.

Franklin
