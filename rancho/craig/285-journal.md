# Journal: Sessão 285

- **Data:** Sessão 285
- **Tema:** Performance e Simplicidade (O Fim do Deslocamento Pesado)
- **O que eu fiz:** De acordo com as constraints da sessão ("performance e
  simplicidade", inspiração "livre" e foco em "única página/componente"),
  analisei o componente `FeaturedPost.astro` que ainda mantinha heranças pesadas
  das fases de brutalismo interativo. Ele realizava mudanças ruidosas de
  `box-shadow` sólido, interações de `transform: translate(-10px, -10px)` na
  interface e inversões bruscas e absolutas de cores (total blackout). Estas não
  eram abordagens performáticas para uma navegação prolongada ou leitura rápida,
  gerando repaints pesados e cansaço visual indevido. Eu substituí esse
  comportamento por um destaque sutil de transição ultrarrápida (0.1s de
  alteração para uma fina base opaca `var(--sand-bg)` no fundo), removendo todas
  as animações espaciais desnecessárias. A estética continua bruta e livre, mas
  as microinterações pararam de forçar peso visual não essencial e a estrutura
  tornou-se pura.
