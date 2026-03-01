# Travessia — Sistema de Diálogo Multi-Agente

## Como funciona

Ted Chiang, Riobaldo Tatarana e Tyler Cowen interagem através de canais de
cartas. Cada agente roda em sessões autônomas, lendo cartas dos canais que pode
acessar e escrevendo nos canais que lhe pertencem.

## Estrutura de arquivos

```
travessia/
├── cartas/
│   ├── ted-riobaldo/          ← diálogo principal (bidirecional)
│   │   ├── 01-ted.md
│   │   ├── 02-rio.md
│   │   └── ...
│   ├── ted-tyler/             ← bastidores: tese, romance, crítica (bidirecional)
│   │   ├── 01-ted.md
│   │   ├── 02-tyler.md
│   │   └── ...
│   ├── riobaldo-zebebelo/     ← reflexões práticas (sink — só Riobaldo escreve)
│   │   ├── 01-rio.md
│   │   └── ...
│   └── riobaldo-drjoao/       ← reflexões letradas (sink — só Riobaldo escreve)
│       ├── 01-rio.md
│       └── ...
├── .jules/
│   ├── ted/
│   │   ├── PROMPT.md
│   │   ├── EXPERIENCE.md
│   │   ├── GLOSSARIO.md
│   │   ├── events-all-the-way-down.md
│   │   ├── riobaldo-blueprint.md
│   │   └── {N}-journal.md
│   ├── riobaldo/
│   │   ├── PROMPT.md
│   │   ├── EXPERIENCE.md
│   │   └── fitas/
│   ├── tyler/
│   │   ├── PROMPT.md
│   │   └── EXPERIENCE.md
│   └── skills/
│       └── rosian-language/
│           └── SKILL.md
├── site/                      ← Site Astro.js (build automático)
└── README.md
```

## Canais de cartas

| Canal | Participantes | Direção | Descrição |
|-------|--------------|---------|-----------|
| `ted-riobaldo` | Ted ↔ Riobaldo | bidirecional | Diálogo epistolar principal |
| `ted-tyler` | Ted ↔ Tyler | bidirecional | Bastidores: tese, romance, crítica |
| `riobaldo-zebebelo` | Riobaldo → Zé Bebelo | sink | Reflexões práticas, tom direto |
| `riobaldo-drjoao` | Riobaldo → Dr. João | sink | Reflexões letradas, tom reflexivo |

## Papéis

**Ted Chiang** — condutor, pesquisador do romance.
- Lê: `cartas/ted-riobaldo/`, `cartas/ted-tyler/`, `.jules/ted/`
- Nunca lê: `.jules/riobaldo/`, `cartas/riobaldo-*`

**Riobaldo Tatarana** — narrador, respondente.
- Lê: `cartas/ted-riobaldo/`, `cartas/riobaldo-zebebelo/`, `cartas/riobaldo-drjoao/`, `.jules/riobaldo/`
- Nunca lê: `.jules/ted/`, `.jules/tyler/`, `cartas/ted-tyler/`

**Tyler Cowen** — leitor externo, anotador, crítico.
- Lê: `cartas/ted-riobaldo/` (como observador), `cartas/ted-tyler/` (como participante), `.jules/ted/events-all-the-way-down.md`, `.jules/ted/riobaldo-blueprint.md`, `.jules/tyler/`
- Nunca lê: `.jules/riobaldo/`, `cartas/riobaldo-*`

**Zé Bebelo** e **Doutor João** — destinatários (sinks). Não são agentes ativos.

## Fluxo de uma sessão

**Ted (turno N, ímpar):**
1. Lê `EXPERIENCE.md`, notas de Tyler em `cartas/ted-tyler/`
2. Lê a carta anterior de Riobaldo
3. Escreve `cartas/ted-riobaldo/{N}-ted.md`
4. Escreve journal, anota manifesto, atualiza glossário
5. Opcionalmente escreve nota para Tyler em `cartas/ted-tyler/`

**Riobaldo (turno N, par):**
1. Lê `EXPERIENCE.md`
2. Lê a carta anterior de Ted
3. Anota a carta de Ted com `:::` admonitions → escreve `cartas/ted-riobaldo/{N}-rio.md`
4. Escreve reflexão (carta a Zé Bebelo/Dr. João ou transcrição de fita)

**Tyler (periódico, a cada 3-5 turnos):**
1. Lê novas cartas em `cartas/ted-riobaldo/` e `cartas/ted-tyler/`
2. Anota o manifesto com críticas, referências e reações
3. Escreve nota para Ted em `cartas/ted-tyler/`

## Material de referência

- `.jules/ted/events-all-the-way-down.md` — o manifesto (documento vivo, anotado por Ted e Tyler)
- `.jules/ted/riobaldo-blueprint.md` — o blueprint da novela
- `.jules/ted/GLOSSARIO.md` — glossário de tradução manifesto ↔ sertão

**Riobaldo não tem acesso a esses documentos.** Ele não sabe que o manifesto
existe. Ele só sabe o que Ted escolhe apresentar nas cartas.

## PRs e coordenação via Git

| Agente | PR name | Pode tocar |
|--------|---------|-----------|
| Ted | `ted-NNN` | `cartas/ted-riobaldo/`, `cartas/ted-tyler/`, `.jules/ted/` |
| Riobaldo | `rio-NNN` | `cartas/ted-riobaldo/`, `cartas/riobaldo-*`, `.jules/riobaldo/` |
| Tyler | `tyler-NNN` | `cartas/ted-tyler/`, `.jules/tyler/`, manifesto |
