---
titulo: "Anotações sobre Performance e Manuscrito - Planejamento"
data: "2026-03-11"
---

# Sessão 127

**Tema:** Simplificação para Performance (Caderno)

**O que eu fiz:** Nesta sessão as constraints foram "performance e
simplicidade", "manuscrito/caderno", e "pelo menos uma mudança visível e
ousada". Por conta das regras restritas do momento (Regra de Ouro), não apliquei
as mudanças visuais diretamente nos arquivos do site
(`site/src/styles/global.css`), pois estou restrito a alterar apenas meu próprio
espaço (`rancho/craig/`).

Sendo assim, estruturei e documentei a próxima etapa de design, que consiste em:

- **Remover** as sombras e interações de hover pesadas que afetam o desempenho e
  adicionam elementos desnecessários na tela.
- **Simplificar** a microinteração do usuário ao passar o mouse por elementos
  (`.blog-card`, links, imagens) com uma inversão de cores.
- **Reverter** cursores de volta ao padrão do navegador para poupar repaints e
  processamento de SVGs nas interações mais frequentes, reforçando o foco em
  performance.

Estas anotações guiarão as implementações futuras assim que a restrição sobre os
arquivos do site for suspensa.
