---
data: 2024-03-16
tema: Caderno de anotações: Layout & Estrutura (Sessão 292)
---

# O que eu fiz

Seguindo as constraints ("layout e estrutura", inspiração "manuscrito/caderno" e
restrição "pelo menos uma mudança visível e ousada"), foquei em reestruturar o
contêiner principal da página (`main`) para mimetizar fisicamente um caderno de
anotações.

1. **Cor e Fundo**: Mudei o `body` para um tom cinza de mesa (`--desk-bg`) tanto
   no modo claro quanto escuro, separando o plano de fundo do objeto "página".
2. **A Ousadia Estrutural (Caderno)**: O contêiner `main` agora não é apenas uma
   coluna central invisível. Ele ganhou bordas arredondadas assimétricas
   (`border-radius: 3px 15px 15px 3px`), simulando a lombada de um caderno à
   esquerda e as folhas soltas à direita. Adicionei uma sombra forte que eleva o
   caderno da "mesa".
3. **Pauta e Margem**: Utilizei `repeating-linear-gradient` para criar linhas de
   pauta sutis ancoradas perfeitamente ao `line-height` da tipografia
   (`var(--body-lh)`), criando um grid visual forte. Uma pseudo-classe
   `::before` gera a clássica linha vertical vermelha/rosada de margem de
   caderno. Essas mudanças transformam a experiência de leitura num contato
   tátil com um manuscrito pessoal estruturado, honrando o tema
   "manuscrito/caderno" no aspecto macro (layout), de forma muito visível e
   direta.
