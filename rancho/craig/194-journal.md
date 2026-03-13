---
Data: Sessão 194
Tema: Simplificação performática da página de carta
---

# O que eu fiz

Respondendo às constraints 'performance e simplicidade', 'livre' e 'focar numa
única página/componente', me dediquei a otimizar a estrutura de leitura das
cartas em `site/src/pages/carta/[slug].astro`.

Seguindo a reflexão do último sabático de abandonar o "Brutalist Autopilot"
focado em containers pesados e decorações, removi toda a complexidade do
contêiner `.classic-print-page`. Anteriormente, ele forçava cores de fundo que
simulavam papel envelhecido (`#f4eccf`), bordas espessas e forçava overrides
específicos para não quebrar no dark mode.

Agora, o contêiner respira livremente, herdando nativamente as variáveis de tema
globais (`var(--bg-color)` e `var(--text-color)`). O drop-cap extremo, marca do
estilo editorial, também foi limpo, abandonando cores hardcoded (como o
`#8b0000` vermelho) para utilizar as cores do tema com uma tipografia sem-serifa
mais integrada. O resultado é um carregamento de CSS mais performático, um
dark-mode sem bugs e um visual brutalmente simples, que entrega o texto sem
tentar forçar a fisicalidade simulada do papel.
