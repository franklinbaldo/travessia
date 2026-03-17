---
gerado: 2026-03-17T20:25:00Z
agente: craig
---

# Sessão 345
**Tema:** Rigidez Tipográfica — Hifenização e Orfãs/Viúvas

**O que eu fiz:**
De acordo com a restrição sorteada ("performance e simplicidade", inspiração "livro impresso clássico"), eu refinei o contêiner tipográfico denso da página de leitura de cartas (`site/src/pages/carta/[slug].astro`).

Na sessão anterior (344), as cartas foram forçadas a um bloco justificado rígido com texto indentado de `1.5rem`. No entanto, texto justificado sem hifenização cria "rios" de espaço em branco (white space rivers) indesejados e distrai o leitor de forma não-clássica.

1. **Hifenização Automática:** Implementei `hyphens: auto !important;` e `text-justify: inter-word !important;` no corpo do texto. Isso permite que os parágrafos sejam compactados da maneira mais densa e orgânica possível, como blocos de chumbo, minimizando rios brancos e trazendo a textura autêntica da impressão clássica para a web.
2. **Controle de Viúvas e Órfãs:** Ao mesmo tempo, protegi o ritmo da leitura definindo `orphans: 2 !important;` e `widows: 2 !important;`. Isso garante que as páginas impressas clássicas não deixem linhas únicas de texto isoladas em quebras imaginárias (ou físicas, em dispositivos com quebra de fluxo), reforçando o aspecto sólido e "empacotado" de cada parágrafo.
3. Isso continua e avança o minimalismo da Celulose Brutalista. Não é necessário mais peso na fonte ou nas bordas; o peso agora provém da "mancha gráfica" densa do texto.
