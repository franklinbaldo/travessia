- **Data:** Sessão 221
- **Tema:** Caderno Brutalista (Cor, Contraste e Linhas)
- **O que eu fiz:** A constraint desta sessão ditou foco em "cor e contraste"
  com a inspiração de "manuscrito/caderno". Para me afastar ainda mais da "falsa
  codex" e do classicismo literário confortável que tomou o design, eu
  transformei a classe `.manuscrito-body` em um objeto tangível de grande
  contraste e hostilidade tipográfica.

Ao invés de uma página delicada e orgânica, implementei um sistema de linhas de
caderno construídas rigidamente via `linear-gradient` e com `background-size`
estrito. As linhas são absolutas: pretas (`var(--text-color)`) no tema claro, ou
cinzas (`var(--secondary-color)`) no tema escuro.

A margem ("caderno") não é uma sutileza, mas sim um bloco agressivo desenhado
com bordas espessas de 4px, projetando uma sombra dura e brutalista
(`box-shadow: 12px 12px 0px var(--accent-color);`) que salta da tela. A linha de
sangria esquerda do caderno também foi acentuada com um traço vibrante em cor
vermelha (`var(--accent-color)`), com opacidade total (diferente da antiga
sutileza).

Essas intervenções forçam a área da leitura a agir não apenas como um pergaminho
fluido, mas como uma máquina de anotações restritiva, onde as palavras do
usuário e as linhas guias lutam pela mesma prioridade de contraste. Cor aqui não
sinaliza estética decorativa, mas estrutura inflexível.
