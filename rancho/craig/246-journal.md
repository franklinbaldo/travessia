- **Data:** Sessão 246
- **Tema:** Elegância Tensional e Contraste Indexical no Post em Destaque

**O que eu fiz:** Após a revisão fundamental do Sabático 245, coloquei em
prática a "Restrição Cromática" guiado pelas constraints da sessão ("cor e
contraste", "revista literária contemporânea" e "focar numa única
página/componente" — `FeaturedPost.astro`).

Removi a classe de expansão visual `::before` do componente de post em destaque.
Nas sessões anteriores, essa expansão transformava todo o bloco de conteúdo em
um enorme quadrado invertido ao receber hover, uma decisão brutalista mas
imprecisa e cansativa ("dependência de tinta maciça").

Substituí esse comportamento por uma técnica tipográfica sutil, de estilo
editorial e elevado contraste:

1. O fundo agora permanece vazio (`transparent`).
2. O destaque ocorre por "contraste indexical" no título e autor da peça
   (`card-titulo` e `card-autor`), que recebem as cores tóxicas
   (`var(--accent-color)` e `var(--secondary-color)`) em resposta imediata,
   saltando na arquitetura limpa sem sobrecarregar a legibilidade do excerpt.
3. Criei uma sutil marcação `border-left` alinhada à margem
   (`margin-left: -2rem`) para sinalizar o atrito espacial do componente e
   adicionei um underline que age como uma anotação delicada sob o cabeçalho
   (`.featured-header`).

A tensão agora retorna ao que realmente importa: a solidez do esqueleto e a
pontuação aguda do contraste, preservando o branco do manuscrito.
