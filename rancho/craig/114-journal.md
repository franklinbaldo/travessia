- **Data:** Sessão 114
- **Tema:** Redesign do cabeçalho da página de leitura (Livro Impresso Clássico)
- **O que eu fiz:** Atendendo às restrições de focar numa única
  página/componente e trazer uma inspiração de livro impresso clássico, refiz o
  `.manuscrito-header` em `global.css` e a estrutura de metadados em
  `carta/[slug].astro`. Removi as pesadas bordas brutalistas (superior e
  inferior de 4px) e as substituí por uma moldura mais elegante e limpa (uma
  linha inferior de 1px com um detalhe de linha dupla parcial usando `::after`).
  Centralizei todo o bloco de metadados (autor, data e correspondência),
  removendo as tags `.separator` supérfluas e os alinhamentos à esquerda. A
  página agora lembra a folha de rosto ou o cabeçalho de um capítulo de um
  clássico livro impresso, dando um peso literário formal e elegante ao título,
  mantendo a coerência com as sessões anteriores focadas em melhoria
  tipográfica.
