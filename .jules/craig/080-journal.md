---
Data: Sessão 080
Tema: Estilização de Listas e Inventários Analógicos
O que eu fiz: Adicionei estilização para elementos `ul`, `ol` e `li` no arquivo `global.css`. O objetivo foi transformar as listas padrão da web em "inventários datilografados" que se integram à estética tátil e arquivística do projeto Travessia. Adicionei uma margem/padding específica que simula o recuo de um texto à máquina, junto a uma sutil borda esquerda para imitar a linha-guia de cadernos ou livros-caixa (`border-left: 1px solid var(--divider-color)`). O "bullet" padrão das listas não ordenadas (`ul`) foi substituído por um hífen mais tátil (`"—  "`). Já as listas ordenadas (`ol`) receberam estilização de máquina de escrever nos números via `ol::marker`, reforçando o uso da fonte secundária (`var(--font-meta)`) com uma cor sutil para separar o índice do conteúdo principal, reforçando a imersão de um livro aberto na mesa de fazenda.
---
