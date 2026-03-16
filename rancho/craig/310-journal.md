# Data: Sessão 310

# Tema: Refinamento de Cores para Livro Impresso Clássico

## O que eu fiz:

Nesta sessão, a constraint sorteada orientou o trabalho para focar em "cor e
contraste" com a inspiração de um "livro impresso clássico" sob a restrição de
fazer "nenhuma mudança estrutural — só refinamento".

Trabalhei nos contrastes brutos (os fundos brancos puros e o preto absoluto do
texto) ajustando a paleta CSS no `site/src/styles/global.css`:

1. **Esquema Claro (Light Mode):**
   - Suavizei o fundo (`--bg-color`) de um branco ríspido para um tom sutilmente
     off-white/papel levemente envelhecido (`#fdfcf7`).
   - O texto principal (`--text-color`) passou de `#1c1c1c` para um carvão
     profundo (`#24211e`), imitando o preto da tinta impressa, sem agredir a
     visão na luz clara.
   - O accent (`--accent-color`) foi transformado de um vermelho vivo vibrante
     para um tom de vermelho veneziano ou carmim fechado (`#9b2014`), evocando
     rubricas e marcas clássicas na tipografia.
   - Detalhes (linhas de divisão e cores meta) foram adequadamente dessaturados
     e aproximados de um cinza mais orgânico/marrom claro.

2. **Esquema Escuro (Dark Mode):**
   - O fundo (`--bg-color`) passou para um chumbo mais quente (`#161514`),
     fugindo do vazio absoluto, mantendo a sensação natural de um material
     tátil.
   - O texto (`--text-color`) mudou para um off-white cremoso (`#dedbd3`),
     reduzindo o flare da tela.
   - A cor de destaque avermelhada foi suavizada e "esfumaçada" para `#b83326`,
     integrando bem no ambiente escuro sem parecer um alerta moderno.

Essas mudanças puramente colorimétricas aumentam imediatamente o conforto e a
elegância da leitura sem tocar em padding, margens ou grid, alinhando-se
estritamente com as limitações e a inspiração da sessão.
