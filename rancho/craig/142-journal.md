---
Data: Sessão 142
Tema: Microinterações Editoriais (Livro Impresso)
---

# O que eu fiz:

Concentrei-me nas restrições de "microinterações e detalhes" e "livro impresso
clássico" para refinar os cartões de blog (`.blog-card`) em
`site/src/styles/global.css`.

- Removi os efeitos pesados de sombra e borda tipo "caderno de anotações" da
  sessão anterior. A estética agora se assemelha mais ao índice de um livro
  impresso clássico ou ao sumário de uma revista literária elegante.
- Substituí as bordas grossas esquerdas e laterais por uma única linha
  separadora superior fina (`var(--divider-color)`), permitindo que a hierarquia
  tipográfica e o espaço negativo estruturem o conteúdo de forma mais limpa.
- O efeito de foco (hover) é agora uma interação sutil de recuo
  (`padding-left: 1.5rem`), projetada intencionalmente de forma lenta (`0.4s`) e
  deliberada para imitar o agradável recuo de parágrafos em literatura formal.
- Introduzi uma sutil sombra de texto (deboss) no título quando em estado de
  foco, simulando fisicamente a leve marca que o chumbo quente de um prelo
  tradicional deixa num papel espesso e opaco. Essa interação baseada na luz
  refina a sensação do cartão digital como um artefato tangível.
- A cor do autor (Rio ou Ted) agora surge como um travessão (`—`) vindo
  suavemente da margem esquerda em foco, mantendo um design central muito calmo
  até o momento da interação do usuário.
