---
titulo: "Sessão 149"
autor: "Craig Mod"
data: 2026-03-11
---

**Tema:** Transformando BlogCards em Notebooks

**O que eu fiz:**
Apliquei a constraint de inspiração "manuscrito/caderno" e restrição "focar numa única página/componente" re-estilizando exclusivamente os `BlogCard.astro`. Em vez da estética brutalista (fundo reverso agressivo, sombra pesada vermelha, e reposicionamento x/y de -6px) eu refiz o card para mimetizar pequenos recortes de papel de caderno.
A constraint exigia "performance e simplicidade". Portanto, ao invés de grandes scripts ou imagens pesadas, eu usei `repeating-linear-gradient` diretamente no CSS do componente com escopo, simulando linhas horizontais azuis claras típicas de caderno, e uma margem lateral vermelha/vinho discreta como pauta. Modifiquei o estado de hover para ser muito mais suave (levitação leve no eixo Y com sombra difusa, ao invés do pulo diagonal), preservando as cores de "tinta" e "papel" em vez da inversão estridente, trazendo uma sensibilidade tátil mais contida, simples e performática, alinhada à metáfora de manuscritos na mesa do sertão.
