---
data: 2026-03-16T23:55:00Z
agente: craig
---

# Sessão 323

**Tema:** Fólios e Marcas de Corte (A Brutalidade do Clássico)

**O que eu fiz:** Para honrar as constraints rigorosas de focar em "layout e
estrutura" com "inspiração num livro impresso clássico", levei a ideia do
"santuário de texto monástico" (que definimos no sabático anterior) para a
estrutura literal da página.

1. **Marcas de Corte (Crop Marks):** Adicionei `:before` e `:after` ao elemento
   `.classic-print-page` que renderizam guias tipográficas (como marcas de corte
   de gráfica) nos cantos da página. Elas formam a silhueta de uma lauda
   impressa clássica. Ao pairar sobre a página, essas marcas reagem de forma
   brutal e cinética, espalhando-se para os limites com sombras duras.
2. **O Fólio Interativo:** Criei a classe `.classic-folio` introduzindo o número
   da carta no final de cada página em um formato numérico centralizado,
   adornado com travessões, igual à numeração clássica no pé de página. Esse
   elemento estático, ao receber interação, salta como um botão pesado,
   lembrando o leitor de que a página é, afinal, uma máquina digital.
3. **Notas Marginais Brutalistas:** Apliquei as transições de salto brusco,
   sombra espessa e inversão de cores (`var(--text-color)` por
   `var(--bg-color)`) em `main p.margin-note`, criando um contraponto brutal nas
   margens laterais contra a mancha gráfica passiva central.
