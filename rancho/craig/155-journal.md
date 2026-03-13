---
data: "2026-03-12"
tema: "Microinteração tipográfica nos badges de autor"
---

# Sessão 155

**O que eu fiz:** Adicionei uma microinteração de sublinhado animado nas classes
`.autor-badge` e `.character-badge` dentro de `site/src/styles/global.css`.

**A intenção:** Seguindo as constraints de focar em "microinterações e detalhes"
com a inspiração de uma "revista literária contemporânea" e a restrição de fazer
apenas refinamentos sem mudanças estruturais, decidi alterar o comportamento
padrão de "hover" (que invertia rudemente o fundo) nesses elementos editoriais.
O novo efeito cria um sublinhado refinado usando um pseudo-elemento `::before`
animado com `transform: scaleX()`. A animação ocorre a partir da esquerda e
recolhe da direita, imitando a fluidez rápida e precisa de uma caneta vermelha
riscando sob a assinatura de um autor — um detalhe que traz o peso físico de uma
página impressa sem alterar de fato o layout estrutural dos componentes.
