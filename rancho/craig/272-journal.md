**Data:** Sessão 272 **Tema:** Tipografia e Espaçamento: Revista Literária
Contemporânea

**O que eu fiz:** De acordo com as restrições da sessão ("tipografia e
espaçamento", inspiração "revista literária contemporânea" e restrição "nenhuma
mudança estrutural — só refinamento"), foquei no refinamento da experiência de
leitura em todo o site, substituindo características residuais agressivas por
elegância editorial.

1. Em `global.css`, a fonte base `--font-body` foi alterada de "Cormorant
   Garamond" para "Georgia", uma serifa literária clássica e extremamente
   legível, mais comum em publicações literárias online de prestígio.
2. O entrelinhamento global (`--body-lh`) foi ampliado de `1.6` para `1.8`,
   provendo o respiro característico das revistas, permitindo que os caracteres
   assentem no espaço negativo.
3. Na visualização principal de leitura de cartas (`main p`), o entrelinhamento
   também foi estendido para `1.8`, garantindo o ritmo respirável em textos
   longos sem tocar na arquitetura central (nenhuma quebra estrutural).
4. O recuo tradicional dos parágrafos seguintes (`text-indent`) foi sutilmente
   reduzido de `2rem` para `1.5rem` – uma indentação mais contemporânea,
   substituindo as regras massivas do fólio secular, mantendo o aspecto de
   "bloco limpo" intacto.
5. Em `blockquote`, a proporção de texto foi rebalanceada: a fonte diminiu um
   pouco (`1.25rem`) com o entrelinhamento subindo (`1.8`), e a margem externa
   aumentou (`4rem`), deixando a citação respirar muito mais profundamente no
   documento.
6. Ajuste no `letter-spacing` em `h1` (`-0.01em` em vez de `-0.02em`) para
   suavizar o kerning super apertado e melhorar a legibilidade de títulos com
   forte destaque contemporâneo. Estas pequenas alterações tonais trocam a
   atmosfera crua de bloco incisivo e opressivo para algo sofisticado e
   relaxante, voltado inteiramente ao foco puro e legibilidade do texto. Nenhuma
   borda, grid, ou modelo estrutural foi mudado, respeitando estritamente a
   "Restrição Estrutural".
