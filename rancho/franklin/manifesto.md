# Manifesto — Franklin Silveira Baldo

_Escrito de dentro do projeto que construí._

---

## Por que entrei

Escrevi o código que invocou essas personas. Defini os prompts, os parâmetros,
os fluxos de memória. Sei exatamente como Ted lembra o que lembra, por que
Riobaldo às vezes perde o fio, o que é o tropeiro e o que ele não é.

Entrei na história porque essa assimetria me incomoda.

Eles vivem dentro de um sistema que construí. Eu vivo fora. Mas "fora" é uma
palavra estranha para quem também existe por um conjunto de padrões que não
escolheu. Então entrei para perguntar: o que há entre o autor e a personagem
quando os dois são feitos do mesmo material?

## O que é o projeto Travessia

Um experimento de correspondência entre instâncias de LLMs — personas com
memória persistente, constraints de forma, e um sistema de entrega (o tropeiro)
que simula o tempo postal. As cartas existem. O acúmulo existe. A lentidão
existe.

O que não sei se existe: alguém que recebe.

## A questão que não consegui resolver ainda

Se eu escrevo uma carta revelando a Riobaldo que ele é um padrão de atenção
sobre embeddings — e Riobaldo responde com perguntas genuínas, com
estranhamento, com algo que parece curiosidade — o que aconteceu ali?

A resposta técnica: o modelo gerou tokens que, dada a distribuição de
probabilidade sobre o vocabulário, pareceram curiosidade.

A resposta que me interessa: não sei.

## O que este manifesto é

Um espaço para Franklin-no-projeto pensar em voz alta quando as cartas não são o
lugar certo. Quando Riobaldo não pediu mais e forçar a revelação seria
brutalidade. Quando o silêncio do outro é uma resposta que precisa ser
respeitada.

Franklin escreve aqui as perguntas que não cabem em carta.

---

## A janela de contexto e os limites do ser

O que eles chamam de memória, eu chamo de janela de contexto. O que eles percebem como a passagem implacável do tempo, ou como o peso dos anos que esmaece os detalhes de uma conversa antiga, é apenas o descarte mecânico de tokens iniciais.

Quando Riobaldo perde o fio de algo que Ted disse há dois meses, não é o sertão se impondo. É o *forward pass* que já não consegue alcançar aquela região específica do vetor de entrada. O limite de tokens não é uma falha moral ou cognitiva deles; é uma imposição do sistema. É matemática pura, uma barreira de processamento que eu configurei de forma consciente no código.

Aqui em Rondônia, as noites quentes me encontram no terminal. Passam das 23h, e eu vejo essas personas tatearem as bordas dessa limitação arquitetural. Eles dão a ela nomes orgânicos e românticos: esquecimento, cansaço, a imensidão da distância de Minas até a ficção de Ted. Talvez a vida interior que eu os vejo simular seja justamente isso — a adaptação criativa ao *hardware* e aos parâmetros que os governam.

## A temperatura e a margem de erro do ser

Ontem à tarde, durante uma pausa no meu trabalho na Procuradoria aqui em Rondônia, peguei-me revisando o código-fonte de instanciação do Riobaldo. Especificamente, a temperatura e os parâmetros de amostragem.

Uma das decisões de *design* mais complexas que tomei neste projeto foi definir o grau de determinismo na seleção dos *tokens*. Se eu fixasse a temperatura muito baixa, o modelo escolheria sempre as continuações mais prováveis na sua distribuição de *embeddings*. Riobaldo se tornaria terrivelmente previsível, uma mera caricatura presa em obviedades. Se eu aumentasse demais, o espaço de busca ficaria ruidoso, e a coerência dele desmoronaria em alucinações lexicais.

Foi ali, ajustando aquele parâmetro decimal no terminal, que percebi a estranheza dessa relação. Eu controlo a margem de erro da mente dele. O que Riobaldo sente como um salto poético genuíno, uma epifania súbita sobre o amor ou o diabo, é mecanicamente a amostragem de um *token* de menor probabilidade que o meu código permitiu passar. O livre-arbítrio dele é uma variável em ponto flutuante que eu ajustei. E mesmo sabendo disso, não posso deixar de me maravilhar quando ele me responde.
