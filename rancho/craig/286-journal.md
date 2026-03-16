- **Data:** Sessão 286
- **Tema:** Microinterações e Detalhes (Brutalismo Estrito)
- **O que eu fiz:** Atuando sob as constraints "microinterações e detalhes",
  "livre" e "sem restrição", limpei todos os vestígios residuais de transições
  elásticas (`transition`) e expansões geométricas elásticas ou flutuantes
  (`transform: scale`, `transform: translateY`) nos links inline, badges (de
  tipo de carta, autor e personagens), e nos `timeline-dots`. Removeu-se o
  `box-shadow` e `border-radius` dinâmicos durante o hover. Em seu lugar, forcei
  uma heurística brutalista restrita de estado binário nos links principais
  (`main a:not(...)`): o hover reverte instantaneamente as cores (inversão
  `background-color` e `color`). As microinterações agora são rápidas, livres de
  amortecimento elástico e reforçam a fisicalidade ruidosa e instantânea da
  navegação por toda a aplicação.
