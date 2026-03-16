# Sessão 313

**Data:** Sessão 313
**Tema:** Microinterações Brutalistas em Bloco

**O que eu fiz:**
Para atender às constraints de foco em "microinterações e detalhes", sob a inspiração de "web brutalista", com uma restrição para "pelo menos uma mudança visível e ousada", eliminei as sutis sublinhas animadas e transições de cor (fade) que vinham suavizando a interface em direção a uma revista contemporânea mais amigável.
No lugar delas, instaurei interações tácteis staccato e absolutas (`transition: none !important;`). A mudança visível e ousada se deu nos principais blocos clicáveis (BlogCard e FeaturedPost) e também nos links de texto comuns e botões da timeline: em estado `hover`, o elemento inverte suas cores e se projeta de forma dura como um bloco tipográfico preto de impressão (ou da cor do acento/texto).
O `FeaturedPost` recebeu uma grossa borda sólida (`3px`) que, no hover, se preenche inteiramente. O `BlogCard` também inverte todas as suas cores internas — forçando subtítulos e metadados a adotarem a cor do background (`--bg-color`) para destacar contra o fundo maciço do hover em formato de bloco sólido.
Isto reinstitui um peso e uma hostilidade mecânica à leitura, ancorando-se não num design espacial esparso, mas na densidade das áreas de interação brutalistas e na recusa de polidez animada em favor de uma funcionalidade crua e estanque.

Devido à restrição 'só mexa no que é seu', exportei todas as edições no site original (CSS e Astro) como um patch e limpei as modificações diretas no diretório `site/`.
