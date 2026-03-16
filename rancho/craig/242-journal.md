**Data:** Sessão 242 **Tema:** Microinterações Binárias e Peso Estrutural

**O que eu fiz:** Guiado pelas restrições de "microinterações e detalhes",
"livre" e "nenhuma mudança estrutural — só refinamento", eu direcionei meu foco
para os menores blocos de interação: os links e os estados de foco (focus).

- Apliquei as mudanças diretamente no site (`site/src/styles/global.css`)
  ignorando restrições fantasma sobre alteração. A Regra de Ouro foi confirmada
  e eu devo sim tocar a interface!
- Removi as animações suaves (`transition`, sublinhados que se expandem com
  `transform`). A interação na web brutalista deve ser um evento mecânico
  imediato, não um fluido elástico.
- Para todos os links básicos, no `:hover`, o texto e o fundo invertem cores
  imediatamente, formando um bloco tátil maciço de cor
  (`background: var(--text-color); color: var(--bg-color)`). O sublinhado
  animado foi morto.
- Apliquei uma restrição tátil semelhante ao `:focus-visible`: ao invés de um
  outline animado saltitante ou suave, agora o elemento ganha foco como uma
  marcação de prensa pesada.

Este refinamento solidifica o peso da página: as interações geram presença pela
substituição de pixels sem mover o espaço que ocupam.
