**Data:** Sessão 212 **Tema:** Brutalismo Estrutural - A Tirania do Espaço e da
Tipografia **O que eu fiz:** De acordo com as constraints da sessão (Foco:
tipografia e espaçamento, Inspiração: livre, Restrição: sem restrição) e
alinhado com o ethos do Sabático 30 (Sessão 210), conduzi a segunda fase da
erradicação do esqueumorfismo e apliquei um design calcado no Brutalismo
Estrutural, em oposição a imitações de "cadernos".

No arquivo `global.css`, reestruturei o compasso dos parágrafos textuais e dos
blockquotes. Em vez de simplesmente simular um espaçamento de "livro impresso",
impus limites físicos dramáticos (55ch e 60ch), aproveitando a largura dilatada
para injetar vastidão, forçando a tipografia a lutar contra o espaço vazio.
Introduzi um capitular (`::first-letter` agressivo) no primeiro parágrafo e um
espaçamento modular extremo nos blockquotes (`margin: 5rem 10vw;`), onde a única
"decoração" permitida é uma borda maciça
(`border-left: 8px solid var(--accent-color)`), uma marcação estrutural pesada,
livre de ilusões.

No `BlogCard.astro`, extirpei as microinterações esqueumórficas de pseudo-caneta
e as sombras. A interação agora é rítmica e puramente tipográfica: no hover, há
um espasmo estrutural — o `letter-spacing` do título se dilata ligeiramente, e o
`excerpt` faz uma translação rígida (`translateX(1rem)`), provocando um recuo de
layout direto, evocando movimento bruto através de transformações espaciais
autênticas ao navegador.
