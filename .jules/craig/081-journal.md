- **Data:** Sessão 081
- **Tema:** Adicionando textura e materialidade: Listas desenhadas à mão e fitas
  adesivas
- **O que eu fiz:** Dando continuidade à minha missão de tornar a experiência de
  leitura ainda mais tátil, implementei duas mudanças significativas hoje.
  Primeiro, refatorei as listas (`ul`), substituindo os marcadores padrões por
  um SVG personalizado que simula um círculo desenhado à mão. Isso ajuda as
  listas a parecerem menos com elementos web e mais com inventories batidos à
  máquina ou checklists anotados à margem da página. Segundo, introduzi um
  efeito visual de "fita adesiva" (masking tape) usando pseudo-elementos
  (`::after`) com gradientes lineares e sombras sutis (`box-shadow` e inset)
  para simular translucidez e textura. Apliquei essa fita no topo das citações
  em bloco (`blockquote`) e nos cartões do blog (`.blog-card`), reforçando a
  metáfora de um dossiê acumulado ou recortes presos apressadamente numa parede
  de fazenda.
