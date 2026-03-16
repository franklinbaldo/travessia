---
Data: 2026-03-16
Tema: O Caderno Brutal (Tipografia e Espaçamento)
O que eu fiz:
Atendendo às constraints sorteadas (Foco: tipografia e espaçamento, Inspiração: manuscrito/caderno, Restrição: pelo menos uma mudança visível e ousada), transformei radicalmente a superfície de leitura do Travessia.

Substituí o "livro impresso" limpo e macio das sessões anteriores por um caderno pautado de anotações brutas.
1. Usei `repeating-linear-gradient` para traçar linhas de escrita (`var(--notebook-line)`) com 32px de altura no `main`.
2. Tracei uma linha vertical ousada e vermelha (`var(--notebook-margin)`) cortando o lado esquerdo usando `main::before`.
3. Ajustei o padding e a margem global para alinhar as novas marcações estruturais do "caderno" com o conteúdo da página.
4. Troquei a tipografia primária `Cormorant Garamond` (com sua elegância de revista literária) por uma família de fontes `monospace` (focada em `Courier`), impondo a urgência e o peso de um relatório datilografado ou notas de campo de Riobaldo e Ted.
A alteração afeta tanto o tema claro (linhas cinza com margem vermelha) quanto o tema escuro (linhas chumbo com margem carmim profundo), que corrigi especificamente para não desaparecerem e manter a estética.

A ousadia da mudança reside no choque contra a limpeza literária recente, forçando um utilitarismo tátil à experiência de ler as cartas.
---
