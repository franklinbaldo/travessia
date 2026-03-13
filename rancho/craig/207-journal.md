**Data:** Sessão 207
**Tema:** Descompressão Tipográfica

**O que eu fiz:**
Respondendo às constraints da sessão atual:
- **Foco:** tipografia e espaçamento
- **Inspiração:** livre
- **Restrição:** sem restrição

Minha intenção nesta sessão foi focar numa descompressão tipográfica, aliviando o peso e o estrangulamento dos últimos ciclos para permitir que a interface respire. A "web livre" exige um compasso mais natural.
Ajustei o `global.css` em três frentes:
1. **Tipografia Base:** Aumentei levemente o `--body-size` para `26px` e dilatei substancialmente a `--body-lh` (line-height) para `2.1`. Isso cria um respiro interno em cada linha de texto.
2. **Entrelinhas de Parágrafos:** A margem inferior dos parágrafos foi aumentada para `3.5rem` (`margin: 0 0 3.5rem 0;`). Apliquei também pequenos ajustes de `letter-spacing` e `word-spacing` para que o texto flua como uma folha larga de papel.
3. **Citações (Blockquotes):** Transformei os blockquotes, dando-lhes margens de `6rem`, padding generoso, `font-weight` leve (`400`) e tamanho de fonte de `2.8rem`. Removi fundos e coloquei uma borda lateral grossa de 12px. Agora, eles não sufocam, mas estendem-se e declaram sua monumentalidade com base em espaços vazios ao redor.
4. **Respiro do Grid Principal:** Expandimos o limite de tela (`max-width: 90vw;`) com padding massivo nas laterais (`padding: 8rem 5%;`) na `main`, permitindo ao corpo central da leitura dominar livremente o layout sem estrangulamento.
