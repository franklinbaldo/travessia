---
data: 2026-03-13
tema: "Índice Brutalista e Reestruturação de Lista"
---

# Sessão 191

## Tema: Índice Brutalista e Reestruturação de Lista

### O que eu fiz:

Seguindo as constraints obrigatórias de "performance e simplicidade", "web
brutalista", e "pelo menos uma mudança visível e ousada", tomei a decisão de
abandonar o complexo layout em múltiplas colunas do "broadsheet" jornalístico
(`.blog-feed`) que governava a página inicial (`site/src/pages/index.astro`).

Em vez disso, impus um modelo austero de lista de diretório, onde cada
`BlogCard` não é mais um "cartão" isolado (com margens, bordas pesadas de 4px e
enormes box-shadows interactivos), mas sim uma linha densa e ininterrupta,
separada apenas por pesadas bordas inferiores de 2px
(`border-bottom: 2px solid var(--text-color)`). O conteúdo do card foi
reorganizado utilizando um Grid layout simples para alinhar rigidamente as
meta-informações numa coluna esquerda e o título/excerpto numa coluna direita em
telas maiores.

A interação no hover foi radicalmente simplificada e tornada mais crua: agora a
"linha" inteira inverte a cor instantaneamente sem qualquer tipo de deslocamento
espacial (`transform: translate`) ou surgimento de sombras, focando puramente no
contraste e eliminando o peso de renderização.

No hero container (`.hero-typographic`), eliminei a "caixa" colorida ao fundo e
as linhas tracejadas, bem como sua sombra em bloco, integrando sua tipografia
gigantesca diretamente no fluxo contínuo do índice de diretório. A citação ("O
diabo não há...") agora ostenta uma forte barra lateral esquerda de 6px em vez
de um background blocky.

Essa mudança ousada maximiza a performance ao reduzir massivamente a
complexidade do DOM e do CSS, retornando a estética à agressividade funcional da
"web brutalista".
