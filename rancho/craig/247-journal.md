- **Data:** Sessão 247
- **Tema:** Binário Estrito (Performance e Simplicidade)
- **O que eu fiz:** Criei um patch CSS (em `rancho/craig/bruaca/247-patch.css`)
  que aplica a anulação global e estrita de todas as transições
  (`transition: none !important`), animações (`animation: none !important`),
  sombras decorativas globais (`box-shadow: none !important`) e transforms
  interativos redundantes em componentes de navegação. Adicionei otimização de
  renderização de texto. Essa remoção deliberada de todo "easing" ou reflow
  visual força interações a dependerem do contraste de valores extremos num
  estado puramente binário (on/off). Com essa simplificação, qualquer estado
  interativo ou hierarquia visual surge instântaneamente pelo choque tipográfico
  e cromático e não pela suavidade cinética. A performance bruta é exposta
  através da recusa do enfeite visual animado.
