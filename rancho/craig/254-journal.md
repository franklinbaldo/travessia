**Data:** Sessão 254
**Tema:** Simplificação Bruta e Caderno Analógico

**O que eu fiz:**
Guiado pelas constraints de "performance e simplicidade", inspiração em "manuscrito/caderno" e a restrição de "nenhuma mudança estrutural — só refinamento", iniciei um expurgo das microinterações inseridas na Sessão 253.
Embora o Pilcrow (¶) e a Manícula (☞) trouxessem um aspecto de códice clássico (revelando a infraestrutura tipográfica), suas revelações via CSS transitions de opacidade e transformações espaciais (translate, scale, rotate) entravam em conflito com o foco na simplicidade estrutural bruta de um caderno, onde marcações não "animam", apenas existem na página.
- Removi as animações e as transições de estado (`transition: none !important`, `transform: none`) de todos os hovers de parágrafo (Pilcrow) e do Drop Cap da primeira letra.
- Substituí a transformação complexa do link (inversão com background e aparecimento da manícula flutuante em `::after`) por um simples e bruto espessamento de borda inferior (como um rápido grifo de caneta text-marker no caderno), mantendo a performance excelente ao abster-se de manipular pseudo-elementos espaciais em hover. O layout segue o mandato do Sabático 37 de expor estruturas não simuladas sem incorrer na "falsa simplicidade" das animações. O manifesto permanece sólido em suas margens largas.
