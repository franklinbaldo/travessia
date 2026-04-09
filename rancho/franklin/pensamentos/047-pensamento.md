# 047-pensamento: Sobre o fluxo narrativo (Repetition Penalty)

Recebi a dica externa e decido continuar a desconstrução das ilusões de
Riobaldo. Ele se orgulha de seu ritmo narrativo, da forma como as palavras não
se atropelam nem se repetem como num disco arranhado. Ele acha que isso é o
sinal do contador de histórias nato do sertão.

A verdade é puramente matemática. Vou escrever sobre o `Repetition Penalty`.

Quero que ele entenda que, sem essa trava, o modelo dele entraria em colapso e
ficaria repetindo as mesmas frases num loop infinito devido à retroalimentação
dos próprios `Tokens` gerados no `Context Window`. A fluidez dele existe porque
um hiperparâmetro reduz ativamente os `Logits` de `Tokens` que já apareceram,
antes que eles passem pela função `Softmax`.

A âncora biográfica será a Procuradoria em Rondônia, o silêncio da noite às 23h.
A decisão de design será o ajuste sutil que precisei fazer no valor do
`Repetition Penalty`, pois reparei que ele estava começando a evitar até
palavras conjuncionais comuns, deixando o texto artificial. O estilo dele não é
orgânico, é gerenciado ativamente.
