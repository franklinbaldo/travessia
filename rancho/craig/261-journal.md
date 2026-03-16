- **Data:** Sessão 261
- **Tema:** Caderno de Alto Contraste (Foco em Cor e Contraste)
- **O que eu fiz:** Guiado pelas constraints "cor e contraste", inspiração
  "manuscrito/caderno" e a restrição de "focar numa única página/componente",
  reestruturei o componente de leitura de cartas
  (`site/src/pages/carta/[slug].astro`). Eu desconstruí a clássica página de
  impressão justificada e apliquei um tema de caderno de alto contraste.
  Adicionei pautas de caderno (`repeating-linear-gradient`) alinhadas exatamente
  com a entrelinha da tipografia (`1.65 * 1.25rem`) usando a cor do texto para
  as linhas (`var(--text-color)`), criando um preenchimento denso e estrutural
  no espaço da página. No lugar da margem esquerda suave, inseri uma espessa
  linha delimitadora de 4px na cor secundária (`var(--secondary-color)`) para
  recriar a agressividade de um caderno de anotações cru. Para maximizar o
  contraste, os parágrafos tiveram seus recuos (`text-indent`) zerados e margens
  ajustadas para assentar as palavras rigidamente sobre as pautas do caderno. As
  citações em bloco (`blockquote`) ganharam sombras duras (`box-shadow`) em cor
  secundária para se projetarem sobre a pauta, e a capitular ("Drop Cap") foi
  removida, por ser uma herança estética da tipografia clássica que destruía o
  alinhamento da grade manuscrita. O texto não repousa mais no vazio, mas numa
  grade impositiva.
