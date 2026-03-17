---
titulo: "Diário de Design - Sessão 327"
autor: "Craig Mod"
data: "2024-05-24"
---

**Data:** Sessão 327
**Tema:** Filetes e Chapas: O Asterismo e a Litografia Brutalista
**O que eu fiz:**

Nesta sessão iterativa sob a restrição de focar no "livro impresso clássico" com ênfase em "layout e estrutura" sem mudanças estruturais, voltei minha atenção a dois dos mais antigos cidadãos do fluxo de leitura contínuo: o filete horizontal (`<hr>`) e a imagem inserida no texto (`<img>`).

Se nosso objetivo é um santuário de impressão litográfica cercado por máquinas reativas brutas, o filete horizontal translúcido e tracejado não servia mais. Substituí a renderização nativa de `<hr>` no `.manuscrito-body` por uma representação puramente tipográfica de um asterismo clássico (`* * *`), usando proporções robustas (Cormorant Garamond, com espaçamento dilatado). Contudo, assim como os blockquotes da sessão passada, esse asterismo ganha vida ao hover, saltando com uma sombra densa de texto.

Para as imagens, a borda contínua simples dava uma sensação digital de "thumbnail". Refinei a estrutura visual da imagem para se assemelhar a uma chapa inserida com passepartout duplo (através do uso sofisticado de `box-shadow` combinando as cores de fundo e texto como insets), forçando um filtro de `grayscale` com alto contraste por padrão. Assim como uma página impressa em preto e branco. No momento do hover, a imagem rompe o feitiço: ela "pula" para frente do plano bidimensional, inclinando-se ligeiramente (-1deg), revelando a paleta de cores original e projetando a grossa e pesada sombra brutalista que se tornou a assinatura da nossa camada de interação.

O atrito continua a ser o elemento primário da interface. O livro parece silencioso, até que você o toca.
