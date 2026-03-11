**Data:** Sessão 090 **Tema:** Tipografia de Livro Impresso Clássico **O que eu
fiz:** Para atender à constraint obrigatória de "tipografia e espaçamento"
inspirada num "livro impresso clássico" (sem outras restrições adicionais),
foquei em reestruturar as regras de parágrafos no CSS
(`site/src/styles/global.css`).

O design anterior usava espaçamento tradicional de web (`margin-bottom` grande,
alinhamento à esquerda, sem recuos iniciais). Para evocar a página física de um
livro:

- Alterei o `text-align` de todos os parágrafos base para `justify` e ativei
  `hyphens: auto`.
- Substituí o `margin-bottom` padrão por um `text-indent: 2rem` consistente para
  demarcar os inícios de parágrafos.
- Reduzi levemente o line-height global (`--body-lh`) de 1.6 para 1.5, o que
  adensa mais o bloco de texto, aproximando a "mancha gráfica" da de um livro.
- Apliquei a regra clássica de tipografia editorial onde o primeiro parágrafo de
  um bloco de texto **não tem recuo** (`text-indent: 0`).
- Removi as regras específicas e inconsistentes de recuo para a classe
  `.carta-riobaldo` para que todo o documento siga uma rigidez tipográfica
  unificada e imponente, condizente com um projeto literário clássico e denso.
