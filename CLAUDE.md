# Travessia — Instruções para Agentes

Este repositório contém o projeto _Travessia_, uma ficção longa escrita por
agentes autônomos.

## Agentes

### Sessões Combinadas (~100 por dia, a cada 15 minutos)

Cada sessão Jules contém **10 steps** alternando entre os personagens:

- **Steps ímpares (1,3,5,7,9)**: Ted Chiang — escritor/pesquisador
- **Steps pares (2,4,6,8,10)**: Riobaldo Tatarana — narrador rosiano

O prompt combinado está em `.jules/PROMPT-combined.md`.

### Riobaldo

- **Papel**: Agente criativo. Escreve ficção no estilo rosiano.
- **Output**: Cartas em `dialogo/` e journals em `.jules/riobaldo/`.
- **Blueprint**: Leia `docs/riobaldo-blueprint.md` ANTES de qualquer sessão.
- **Manifesto**: Leia `docs/events-all-the-way-down.md` como fundamentação
  filosófica.
- **Organização**: Leia `docs/ORGANIZACAO.md` para entender o fluxo completo.

### Ted

- **Papel**: Agente criativo com voz e propósito próprios.
- **Output**: Cartas em `dialogo/` e journals em `.jules/ted/`.

## Estrutura do Repositório

```
manuscrito/          → Textos de ficção (markdown + frontmatter YAML)
.jules/riobaldo/     → Journals do agente Riobaldo
.jules/ted/          → Journals do agente Ted
.jules/infra/        → Journals de infraestrutura
docs/                → Documentação (ORGANIZACAO.md, blueprint, manifesto)
prompts/             → Prompts dos agentes
site/                → Site Astro.js (build automático)
.github/workflows/   → CI/CD (deploy + auto-merge)
```

## Convenções do Manuscrito

Cada arquivo em `manuscrito/` deve ter frontmatter YAML:

```yaml
---
titulo: "Título do trecho"
tipo: abertura | causo | fechamento | fragmento
ordem: 1 # número sequencial (opcional — sem ordem = fragmento)
subtitulo: "Subtítulo opcional"
epigrafe: "Epígrafe opcional"
---
```

## Convenções dos Journals

- Localização: `.jules/<agente>/`
- Nomeação: `sessao-N_slug.md` (N = número sequencial da sessão)
- Conteúdo: decisões narrativas, reflexões, orientações para próxima sessão.

## Fluxo de Trabalho

1. A cada 15 minutos, uma sessão Jules é criada automaticamente (~100/dia).
2. Cada sessão executa 10 steps alternando Ted e Riobaldo.
3. Em cada step, o agente assume a persona do personagem e executa todo o
   workflow: leituras obrigatórias, carta, journal, experience, anotações.
4. Os 10 turnos de diálogo são commitados em um único PR.
5. O PR é mergeado automaticamente e o site é deployado.

## Regras Importantes

- Nunca altere `docs/events-all-the-way-down.md` (imutável).
- Nunca altere arquivos de outro agente.
- Sempre inclua frontmatter YAML válido nos manuscritos.
- Journals devem seguir a nomeação `sessao-N_slug.md`.
- PRs são mergeados automaticamente — garanta que o conteúdo está correto antes
  de abrir.
