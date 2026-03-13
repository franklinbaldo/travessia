- **Data:** Sessão 153
- **Tema:** Simplificação para Performance e Estética de Impresso
- **O que eu fiz:** Para atender às constraints desta sessão ("performance e
  simplicidade", inspiração "livro impresso clássico" e "nenhuma mudança
  estrutural — só refinamento"), foquei em otimizar a página da carta individual
  (`site/src/pages/carta/[slug].astro`).

  A versão anterior da classe `.classic-print-page` introduzia bordas duplas
  grossas e `box-shadows` complexas (especialmente no modo escuro) que, embora
  esteticamente agradáveis, não eram ideais para performance e adicionavam peso
  desnecessário à renderização.

  Minha intervenção consistiu em simplificar drasticamente esses elementos
  visuais sem alterar a estrutura do DOM:
  1. Removi completamente as propriedades `box-shadow` (tanto a normal quanto a
     do modo escuro).
  2. Substituí a borda grossa e pesada (`border: 6px double #111111`) por uma
     linha simples, limpa e de alta performance (`border: 1px solid #111111`).

  Essa mudança reforça a estética crua de um impresso clássico puro — focando
  mais na mancha gráfica e no contraste da tinta no papel do que em efeitos
  decorativos — ao mesmo tempo em que reduz o overhead de renderização do
  navegador, cumprindo rigorosamente as diretrizes da sessão.
