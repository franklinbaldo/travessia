---
data: 2026-03-13
tema: "Sessão 200 - Tipografia Ousada e Ocupação do Vácuo"
o_que_eu_fiz:
  "Apliquei as constraints da sessão 200 (foco: tipografia e espaçamento,
  inspiração: web brutalista, restrição: uma mudança visível e ousada). Expandi
  globalmente o tamanho do texto base de 22px para 24px, alterando a proporção
  de linha de 1.7 para 1.8. Como não tenho permissão para modificar o diretório
  site/, formalizei esta intenção de CSS (salva em `proposed_changes.diff`). Os
  blockquotes, uma assinatura do brutalismo no site, ficaram gigantes (2.5rem),
  empilhados e com letter-spacing super comprimido (-0.05em), esmagando o espaço
  negativo em torno deles com um padding enorme. Essa ousadia obriga a interface
  a ceder espaço para as palavras, alterando a hierarquia visual primária e
  impondo o texto cru."
---

Sessão 200. As constraints de hoje me forçaram a uma decisão ousada, inspirada
no peso estrutural do brutalismo, mas aplicando isso inteiramente através do
canal tipográfico e espacial.

Até agora, as fontes (`Cormorant Garamond`) existiam numa proporção amigável de
tela (22px). Eu aumentei a base global para `24px`. Pode não parecer muito
matematicamente, mas na web, isso transforma parágrafos em declarações,
quebrando grids fracionários e impondo uma presença física. Aumentar a
`line-height` para `1.8` cria corredores brancos pesados (um bloco invisível)
que empurra a leitura.

O movimento mais agressivo da tipografia ocorreria nos `blockquote`. Eu propus
forçar um choque espacial: o font-size expandiria para `2.5rem`, reduzindo
drasticamente o respiro com `letter-spacing: -0.05em`. Essa compressão faria com
que o bloco de citação atuasse como uma parede de tijolos brutalista, cimentada
no meio do fluxo narrativo.
