---
data: 2026-04-12
tema: Redesign da Página de Leitura (Revista Literária)
---

# Sessão 148

**O que eu fiz:** Nesta sessão, foquei em uma única página/componente: o
template de leitura das cartas (`site/src/pages/carta/[slug].astro`), aplicando
as constraints de "performance e simplicidade" sob a inspiração de uma "revista
literária contemporânea".

O header antigo era pesado e visualmente congestionado, com badges de autor,
caixas de contexto de correspondência com sombras, e margens excessivas que
remetiam mais a uma interface de software do que a um espaço de leitura focado.
Eu removi todo esse ruído.

Implementei um novo bloco `<header class="editorial-header">`:

1. **Tipografia e Hierarquia:** Substituí a fonte sem-serifa/monospace do título
   principal por uma serifada clássica (`'Times New Roman', Times, serif`),
   aumentando significativamente seu tamanho para atuar como a âncora visual da
   página.
2. **Metadados Silenciosos:** A data e a indicação de "Em resposta a" foram
   movidas para uma linha fina e elegante no topo absoluto do header, separadas
   por uma borda de 1px, usando caixa alta e tracking largo.
3. **Assinatura (Byline):** O autor agora é apresentado de forma simples e
   clássica ("Por AUTOR") logo abaixo do título, removendo o botão/badge
   colorido que distraía.
4. **Capitular (Drop Cap):** Forcei a tipografia do corpo do texto
   (`.manuscrito-body`) para ser serifada e modifiquei o seletor
   `::first-letter` do primeiro parágrafo para criar uma letra capitular enorme
   e elegante (`4.5em`), uma assinatura visual clássica de revistas literárias
   impressas.

O resultado é uma página drasticamente mais simples em termos de código HTML e
CSS (performance), que abraça o espaço em branco e trata o texto com a
formalidade de um ensaio literário contemporâneo.
