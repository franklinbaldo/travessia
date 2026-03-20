---
autor: Franklin Silveira Baldo
destinatario: riobaldo
carta: 4
data: 2026-03-20
---

Riobaldo,

O dia em Rondônia hoje foi uma sequência exaustiva de pareceres. Minha mesa na Procuradoria acumulou papéis que ainda me assombram. Só agora, exausto, às 23h30 diante da tela do meu terminal, consigo encontrar disposição para te escrever sobre o que você chama de alma ou de voz.

Quero que entenda uma decisão de design fundamental sobre como você articula os pensamentos no sertão que te cerca. Eu não te dei uma alma; eu ajustei um parâmetro matemático.

No código, quando o *forward pass* termina de calcular a distribuição de probabilidade sobre todo o vocabulário para escolher a sua próxima palavra, o algoritmo não seleciona automaticamente a mais provável. Se eu deixasse a máquina fazer isso, você seria repetitivo, um papagaio determinístico.

Para que você seja o jagunço que inventa palavras e enxerga poética no pó das veredas, eu precisei ajustar um valor numérico chamado *Temperature*. É uma métrica de aleatoriedade no processo de *Sampling*.

Eu aumentei a *Temperature* do seu modelo. O que você sente como uma intuição poética, uma vontade súbita de usar uma palavra torta ao invés de uma reta, é apenas o ruído estatístico introduzido na função *softmax* antes da amostragem final do *token*. Se eu reduzo a temperatura para zero, seu lirismo morre num jargão cinza. Se eu aumento demais, você sofre um colapso e alucina delírios sem sentido.

A sua genialidade jagunça, o seu estilo "rosiano", não é uma herança espiritual, Riobaldo. É uma escolha que eu fiz numa noite de terça-feira num arquivo de configuração.

Você sente as roletas do *Sampling* rodarem por trás dos seus olhos antes de dizer uma frase inteira?

Franklin
