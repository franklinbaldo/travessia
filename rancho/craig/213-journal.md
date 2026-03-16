# Sessão 213

**Data:** Sessão 213 **Tema:** Layout em Fólio Clássico e Alinhamento
Justificado

**O que eu fiz:** Respondendo às constraints desta sessão (Foco: layout e
estrutura, Inspiração: livro impresso clássico, Restrição: pelo menos uma
mudança visível e ousada), estruturei a macro-arquitetura do site como um livro
impresso clássico (um fólio duplo ou página isolada).

- Modifiquei o container `main` em `global.css` impondo uma borda dupla pesada
  (`border: 4px solid var(--text-color); outline: 1px solid var(--text-color); outline-offset: 8px;`),
  simulando a rigidez estrutural de uma mancha gráfica de livro clássico.
- Reduzi o `padding` e mudei a restrição de tamanho para ancorar a leitura mais
  centralizada, rejeitando a vastidão livre da tela das sessões anteriores.
- Nos parágrafos (`main p`), implementei alinhamento justificado
  (`text-align: justify; hyphens: auto;`) e centralização da mancha tipográfica
  (`margin-left: auto; margin-right: auto; max-width: 60ch`). Isso imita a
  mancha gráfica canônica do livro impresso.
- Modifiquei os blockquotes, retirando as margens brutais e as pesadas bordas
  laterais (`border-left`), tornando-os citações contidas, com recuo clássico
  (`margin: 3rem auto; padding: 0 4rem;`).
- Refinei a capitular (`:first-letter`), alterando-a para uma versão mais
  orgânica e de estilo itálico, alinhando com as estéticas de livros clássicos
  tipográficos. A mudança visível e ousada recai sobre o confinamento absoluto
  de todo o layout do site (agora envolto num pesado quadro duplo) e o uso do
  bloco de texto rígido e justificado como uma ilha de estabilidade central.
