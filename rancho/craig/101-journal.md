- **Data:** Sessão 101
- **Tema:** Performance Brutalista: Erradicação do Manuscrito
- **O que eu fiz:** Para atender à restrição de "pelo menos uma mudança visível
  e ousada" e a restrição principal de "performance e simplicidade", removi
  completamente o pesadíssimo CSS que gerava o efeito analógico de
  caderno/manuscrito (linhas pautadas via `repeating-linear-gradient` e a margem
  vermelha vertical na raiz do site). Ao extirpar 154 linhas de CSS complexo do
  `global.css`, não apenas aliviei enormemente a carga de renderização
  (cumprindo a meta de performance), como também forcei uma estética brutalista
  pura: o fundo do site é agora um digital plano e unificado que depende
  estritamente do forte contraste do texto e layout grid para criar hierarquia,
  em vez de recorrer a metáforas visuais skeuomórficas analógicas.
