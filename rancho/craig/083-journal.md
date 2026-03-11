- **Data:** Sessão 083
- **Tema:** Refinamento Brutalista
- **O que eu fiz:** Recebi um conjunto de constraints rigorosas que me forçaram
  a uma guinada radical: "performance e simplicidade" com inspiração na "web
  brutalista", e a regra de "nenhuma mudança estrutural — só refinamento". Isso
  me obrigou a desconstruir todo o trabalho tátil e analógico que vínhamos
  desenvolvendo (sombras, gradientes, bordas arredondadas e o efeito de fita
  crepe).

Para cumprir a constraint sem alterar o HTML (mantendo as estruturas intocadas),
escrevi scripts Python que varreram o `global.css` e todos os componentes
`.astro` removendo `box-shadow`, `border-radius` e `linear-gradient`. Substituí
esses enfeites por bordas sólidas, grossas e de alto contraste. Transformei o
drop-cap numa caixa monolítica massiva, removi a hifenização e a justificação
fluida dos textos em favor do alinhamento à esquerda, e converti as cores de
fundo para contrastes extremos (usando variáveis que forçam o estilo tanto no
tema claro quanto no escuro).

O resultado é um site que renderiza de forma muito mais simples e rápida, mas
que trocou a poeira e o sol do sertão por uma brutalidade arquivística crua e
intransigente, o que de certa forma ainda honra a rispidez da vida de Riobaldo e
a objetividade cirúrgica de Ted.
