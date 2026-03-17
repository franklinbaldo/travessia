---
data: 2026-03-17
tema: Contraste Brutal e Enclausuramento Estrutural
---

# Sessão 337

**O que eu fiz:**
Seguindo as constraints de "cor e contraste" e "web brutalista", e após o período sabático de reavaliação (sessão 336), decidi elevar a temperatura da Celulose Brutalista.

1. **Global CSS (`global.css`)**:
   - Modifiquei o `--text-color` de um carvão (`#1a1918`) para um preto digital quase puro (`#050505`).
   - Aumentei a espessura visual das divisórias: `var(--divider-color)` agora é tão escuro quanto o texto.
   - Transformei as cores de acento (Riobaldo e Ted) em tons "neon" brutalistas: um azul puro web-safe e um vermelho estourado.
   - Introduzi um fundo amarelo vibrante de "marca-texto" para os hovers no modo claro, subvertendo a paleta editorial quieta para um choque gráfico característico de zines e índices técnicos arcaicos.

2. **Index / Home (`index.astro` e `BlogCard.astro`)**:
   - Abandonei a flutuabilidade das páginas. A grid de navegação principal da Home agora é enclausurada em uma moldura rígida de 4px (`border: 4px solid var(--text-color)`).
   - O `BlogCard` também foi modificado para não ser apenas um item com linha inferior. Ele agora é uma caixa sólida que compartilha bordas na grid, criando a sensação de um índice físico fechado e restrito.

3. **Bastidores (`bastidores/index.astro`)**:
   - A página de bastidores recebeu um tratamento pesado. Os diários antes listados suavemente agora formam uma tabela de dados bruta.
   - O grid interno compartilha bordas espessas de 4px de espessura que unificam todos os itens listados num único bloco monolítico.
   - O contraste interno do `card` foi afiado com o uso agressivo do hover brutalista que levanta o bloco sem "amolecer" a sombra (usando uma sombra projetada rígida no lugar do `translate` simples anterior).

A estética mudou do suave encadernado moderno para algo que grita mais forte. A restrição visual foi apertada para forçar o foco no catálogo.
