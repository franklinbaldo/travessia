---
data: "Sessão 144"
tema: "Layout da Última Carta como Caderno"
---

# O que eu fiz:

Focando no aspecto "layout e estrutura" e sob a inspiração "manuscrito/caderno", reimaginei totalmente a apresentação da Última Carta (`FeaturedPost.astro`). Retirei sua dependência visual do CSS global de posts e o tornei um elemento físico palpável.

A página inicial agora apresenta a carta em destaque flutuando ligeiramente (`rotate(-0.5deg)`) acima da interface estrutural (`site/src/components/FeaturedPost.astro`). Adicionei fundos que imitam papel macio, sombras em camadas detalhadas, pautas pálidas horizontais e uma encadernação lateral estilizada com buracos circulares, criados com gradientes radiais. O hover desfaz essa rotação, e aproxima o "papel" do leitor, conferindo mais profundidade táctil (removendo as transições da sessão 139) e uma paleta de cores (`ink` vs `paper`) distinta. Tudo encapsulado dentro do próprio componente Astro em prol de um acoplamento mais inteligente. Removemos o CSS redundante respectivo de `site/src/styles/global.css`.

A modificação foca num só componente ("Última Carta") para ancorar o site text-heavy em pelo menos uma textura de profunda referência física.
