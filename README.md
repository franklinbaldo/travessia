# Travessia — Sistema de Diálogo Multi-Agente

## Como funciona

Ted Chiang, Riobaldo Tatarana, Tyler Cowen e Craig Mod interagem através de
canais de cartas. Cada agente roda em sessões paralelas (heartbeat a cada 15
min), escrevendo na sua bruaca (outbox) e lendo do seu balaio (inbox). O
Tropeiro (heartbeat.py) entrega as cartas entre os agentes.

## Estrutura de arquivos

```
travessia/
├── rancho/
│   ├── riobaldo/
│   │   ├── PROMPT.md
│   │   ├── EXPERIENCE.md
│   │   ├── bruaca/           ← outbox (cartas a enviar)
│   │   ├── balaio/           ← inbox (cartas recebidas)
│   │   └── fitas/
│   ├── ted/
│   │   ├── PROMPT.md
│   │   ├── EXPERIENCE.md
│   │   ├── GLOSSARIO.md
│   │   ├── events-all-the-way-down.md
│   │   ├── riobaldo-blueprint.md
│   │   ├── bruaca/           ← outbox
│   │   ├── balaio/           ← inbox
│   │   └── {N}-journal.md
│   ├── tyler/
│   │   ├── PROMPT.md
│   │   ├── EXPERIENCE.md
│   │   ├── bruaca/           ← outbox
│   │   └── balaio/           ← inbox
│   └── craig/
│       ├── PROMPT.md
│       ├── EXPERIENCE.md
│       ├── bruaca/           ← outbox
│       ├── balaio/           ← inbox
│       └── {NNN}-journal.md
├── cartas/                   ← arquivo público (tropeiro copia aqui)
│   ├── ted-riobaldo/
│   ├── ted-tyler/
│   ├── riobaldo-zebebelo/
│   └── riobaldo-doutor_joao/
├── manuscrito/               ← textos de ficção
├── .jules/
│   ├── skills/
│   ├── sessions.json
│   └── heartbeats/
├── tools/                    ← heartbeat.py, sortear-constraints.sh
├── site/                     ← Site Astro.js (build automático)
└── README.md
```

## Regra de Ouro

Cada agente só pode modificar arquivos dentro do seu `rancho/{agente}/`.
Exceções: Craig pode modificar `site/`, Tyler pode anotar o manifesto.

## Sistema de Correio (Tropeiro)

Os agentes não escrevem diretamente em `cartas/` nem no `rancho/` de outro
agente. O fluxo é:

1. Agente escreve carta em `rancho/{agente}/bruaca/{N}-carta-{destinatario}.md`
2. O Tropeiro (heartbeat.py) lê a bruaca no branch do PR mergeado
3. O Tropeiro entrega: copia para `rancho/{destinatario}/balaio/` e para
   `cartas/{rota}/` (arquivo público para o site)
4. Agente lê cartas recebidas de `rancho/{agente}/balaio/`

## Canais de cartas (arquivo)

| Canal               | Participantes        | Direção      | Descrição                          |
| ------------------- | -------------------- | ------------ | ---------------------------------- |
| `ted-riobaldo`      | Ted ↔ Riobaldo       | bidirecional | Diálogo epistolar principal        |
| `ted-tyler`         | Ted ↔ Tyler          | bidirecional | Bastidores: tese, romance, crítica |
| `riobaldo-zebebelo` | Riobaldo → Zé Bebelo | sink         | Reflexões práticas, tom direto     |
| `riobaldo-doutor_joao` | Riobaldo → Dr. João | sink        | Reflexões letradas, tom reflexivo  |

## Papéis

**Ted Chiang** — condutor, pesquisador do romance.

- Escreve em: `rancho/ted/bruaca/`
- Lê de: `rancho/ted/balaio/`, `rancho/ted/`

**Riobaldo Tatarana** — narrador, respondente.

- Escreve em: `rancho/riobaldo/bruaca/`
- Lê de: `rancho/riobaldo/balaio/`, `rancho/riobaldo/`

**Tyler Cowen** — leitor externo, anotador, crítico.

- Escreve em: `rancho/tyler/bruaca/`
- Lê de: `rancho/tyler/balaio/`, `rancho/tyler/`,
  `rancho/ted/events-all-the-way-down.md`, `rancho/ted/riobaldo-blueprint.md`

**Craig Mod** — designer do site.

- Escreve em: `rancho/craig/`, `site/`
- Lê de: `rancho/craig/balaio/`, `rancho/craig/`

**Zé Bebelo** e **Doutor João** — destinatários (sinks). Não são agentes ativos.

## Material de referência

- `rancho/ted/events-all-the-way-down.md` — o manifesto (documento vivo, anotado
  por Ted e Tyler)
- `rancho/ted/riobaldo-blueprint.md` — o blueprint da novela
- `rancho/ted/GLOSSARIO.md` — glossário de tradução manifesto ↔ sertão

**Riobaldo não tem acesso a esses documentos.** Ele não sabe que o manifesto
existe. Ele só sabe o que Ted escolhe apresentar nas cartas.

## PRs e coordenação via Git

| Agente   | PR name     | Pode tocar                    |
| -------- | ----------- | ----------------------------- |
| Ted      | `ted-NNN`   | `rancho/ted/`                 |
| Riobaldo | `rio-NNN`   | `rancho/riobaldo/`            |
| Tyler    | `tyler-NNN` | `rancho/tyler/`, manifesto    |
| Craig    | `craig-NNN` | `rancho/craig/`, `site/`      |
