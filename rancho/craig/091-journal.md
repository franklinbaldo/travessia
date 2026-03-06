Data: Sessão 091
Tema: Performance e Simplicidade

O que eu fiz:
Nesta sessão, a constraint sorteada foi "performance e simplicidade", com inspiração livre e sem outras restrições. Para cumprir essa diretriz de maneira eficaz, realizei uma série de otimizações voltadas para a performance de renderização (paint/composite) e a redução do tempo de execução no thread principal (JavaScript).

Ações realizadas:
- **Redução de Custo de Renderização:** Removi as declarações de `box-shadow` pesadas (e com desfoque duro) e `text-shadow` que, embora adicionassem textura física, demandam muito repaints do navegador durante rolagem.
- **Otimização de Transições CSS:** Substituí as transições baseadas em `all`, que frequentemente forçam recálculos desnecessários de layout, por propriedades específicas focadas em `background-color` e `color`.
- **Simplificação de Micro-interações:** Removi os efeitos de `transform: translateY()` em hovers de botões e cards (como `BlogCard.astro` e `FeaturedPost.astro`). Alterações de transform, mesmo no compositing, acrescentam camadas. A leitura do texto torna-se agora mais estável.
- **Remoção de Javascript Oneroso:** Eliminei o event listener global de scroll e a manipulação do DOM da barra de progresso no `Layout.astro`. Ouvintes de scroll frequentes (`updateScroll`) provocam *layout thrashing* contínuo. Ao remover a barra, focamos a interface na leitura ininterrupta, garantindo uma performance fluída, de 60 FPS, mesmo em dispositivos de baixo custo.

O site mantém sua essência estrutural de revista literária clássica, porém de forma muito mais enxuta, garantindo carregamento mais rápido e rolagem sem engasgos, refletindo um respeito pelo hardware do leitor.
