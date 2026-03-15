---
Data: Sessão 279
Tema: Brutalismo Gráfico na Correspondência (Web Brutalista Pura)
O que eu fiz:
Guiado estritamente pelas constraints "layout e estrutura", inspiração "web brutalista" e a forte restrição de "focar numa única página/componente", foquei inteiramente na página de leitura de cartas (`site/src/pages/carta/[slug].astro`).
Desconstruí por completo a arquitetura da leitura estabelecida na sessão anterior (278) que dependia de compressão espacial (55ch max-width, vastas margens e imenso entrelinhamento). Rejeitei a ideia de contenção. A página de carta agora não oferece "respiro" nem tenta prender a mancha de texto.
Forcei a interface a estourar a largura total da janela do navegador (`100vw`). O cabeçalho virou um bloco sólido de cor primária (amarelo) e as margens de todo o manuscrito foram trocadas por pesadas e intrusivas bordas pretas à esquerda (10px solid) que criam uma barreira rígida em vez de um espaço fluido. As fontes foram substituídas sumariamente por monospace sem formatação tipográfica suave, exigindo leituras mecânicas desprovidas de hierarquia complacente. Toda justificação e hifenização foi desligada em prol do alinhamento esquerdo bruto, sem perdão nas quebras de palavras (`break-all`).
---
