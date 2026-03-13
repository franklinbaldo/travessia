---
data: 2026-03-12
tema: "Simplificando o Hero para Performance"
o_que_eu_fiz:
  "Focando nas constraints de 'performance e simplicidade' e 'livre' inspiração,
  com a restrição de fazer 'pelo menos uma mudança visível e ousada'. O Hero
  Banner gigante anterior, com fundo de cor sólida invertida e sombras brutais,
  carregava excessivamente o visual e aumentava a complexidade na renderização
  (box shadows exagerados, uso constante de !important). Redesenhei
  completamente o Hero em site/src/pages/index.astro, adotando uma abordagem
  minimalista e de alta performance. Removi o box-shadow agressivo, o background
  invertido e os layouts complexos de flexbox e grid que competiam entre si. O
  novo design é perfeitamente fluido, utilizando texto escuro sobre fundo
  transparente e separando a área do Hero com uma linha fina e elegante (1px
  solid). Diminui a fonte do <h1> de clamp(3rem, 10vw, 6rem) para clamp(2.5rem,
  8vw, 5rem), permitindo que ele seja processado com mais rapidez pelos motores
  de layout dos navegadores e trazendo um respiro à página. Esta mudança visível
  e ousada em prol do minimalismo cria uma experiência de leitura muito mais
  rápida e elegante."
---
