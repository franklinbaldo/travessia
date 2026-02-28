# Travessia — Instruções para Agentes

Este repositório contém o projeto _Travessia_, uma ficção longa escrita por
agentes autônomos.

## Agentes

### Riobaldo (sessão diária às 11 UTC)

- **Papel**: Agente criativo. Escreve ficção no estilo rosiano.
- **Output**: Manuscritos em `manuscrito/` e journals em `.jules/riobaldo/`.
- **Blueprint**: Leia `docs/riobaldo-blueprint.md` ANTES de qualquer sessão.
- **Manifesto**: Leia `docs/events-all-the-way-down.md` como fundamentação
  filosófica.
- **Organização**: Leia `docs/ORGANIZACAO.md` para entender o fluxo completo.

### Ted (sessão diária às 10 UTC)

- **Papel**: Agente criativo com voz e propósito próprios.
- **Output**: Conteúdo em diretório próprio e journals em `.jules/ted/`.

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

1. Leia journals e textos anteriores para contexto.
2. Escreva o próximo conteúdo no diretório apropriado.
3. Escreva o journal da sessão em `.jules/<agente>/`.
4. Abra um Pull Request. O PR será mergeado automaticamente.
5. O deploy do site acontece automaticamente após merge na main.

## Regras Importantes

- Nunca altere `docs/events-all-the-way-down.md` (imutável).
- Nunca altere arquivos de outro agente.
- Sempre inclua frontmatter YAML válido nos manuscritos.
- Journals devem seguir a nomeação `sessao-N_slug.md`.
- PRs são mergeados automaticamente — garanta que o conteúdo está correto antes
  de abrir.
