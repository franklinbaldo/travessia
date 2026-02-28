# Travessia — Instruções para Agentes

Este repositório contém o projeto _Travessia_, uma ficção longa escrita por
agentes autônomos.

## Agentes

### Riobaldo (sessão diária às 11 UTC)

- **Papel**: Agente criativo. Escreve ficção no estilo rosiano.
- **Output**: Manuscritos em `manuscrito/`, cartas e fitas em `.jules/riobaldo/`.
- **Blueprint**: Leia `docs/riobaldo-blueprint.md` ANTES de qualquer sessão.
- **Manifesto**: Leia `docs/events-all-the-way-down.md` como fundamentação
  filosófica.
- **Organização**: Leia `docs/ORGANIZACAO.md` para entender o fluxo completo.

### Ted (sessão diária às 10 UTC)

- **Papel**: Agente criativo com voz e propósito próprios.
- **Output**: Conteúdo em diretório próprio e journals em `.jules/ted/`.

## Estrutura do Repositório

```
manuscrito/                → Textos de ficção (markdown + frontmatter YAML)
.jules/riobaldo/           → Reflexões do agente Riobaldo
.jules/riobaldo/cartas/    → Cartas pessoais (a Zé Bebelo, Doutor João, etc.)
.jules/riobaldo/fitas/     → Transcrições de gravações em fita magnética
.jules/riobaldo/rascunhos/ → Rascunhos das cartas ao Ted
.jules/ted/                → Journals do agente Ted
.jules/infra/              → Journals de infraestrutura
docs/                      → Documentação (ORGANIZACAO.md, blueprint, manifesto)
prompts/                   → Prompts dos agentes
site/                      → Site Astro.js (build automático)
.github/workflows/         → CI/CD (deploy + auto-merge)
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

## Convenções das Reflexões de Sessão

### Riobaldo

As reflexões de Riobaldo são artefatos diegéticos (existem dentro da ficção):

- **Cartas pessoais**: `.jules/riobaldo/cartas/{N}-carta-{destinatario}.md`
  - Cartas a Zé Bebelo, Doutor João ou outros conhecidos
  - Frontmatter: `destinatario`, `data`, `sessao`
- **Transcrições de fita**: `.jules/riobaldo/fitas/{N}-fita.md`
  - Gravações em máquina de fitas que o Doutor João trouxe da Alemanha
  - Frontmatter: `tipo: "transcricao"`, `data`, `sessao`

### Outros agentes

- Localização: `.jules/<agente>/`
- Nomeação: `sessao-N_slug.md` (N = número sequencial da sessão)
- Conteúdo: decisões narrativas, reflexões, orientações para próxima sessão.

## Fluxo de Trabalho

1. Leia journals e textos anteriores para contexto.
2. Escreva o próximo conteúdo no diretório apropriado.
3. Escreva o journal da sessão em `.jules/<agente>/`.
4. Abra um Pull Request. O PR será mergeado automaticamente.
5. O deploy do site acontece automaticamente após merge na main.

## Regras Importantes

- Nunca altere `docs/events-all-the-way-down.md` (imutável).
- Nunca altere arquivos de outro agente.
- Sempre inclua frontmatter YAML válido nos manuscritos.
- Reflexões de Riobaldo devem seguir o formato de cartas ou fitas (ver PROMPT.md).
- Journals de outros agentes devem seguir a nomeação `sessao-N_slug.md`.
- PRs são mergeados automaticamente — garanta que o conteúdo está correto antes
  de abrir.
