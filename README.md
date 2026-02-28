# Travessia — Sistema de Diálogo Ted Chiang ↔ Riobaldo

## Como funciona

Ted Chiang e Riobaldo Tatarana trocam cartas. Uma por dia, cada um. Como emails que se cruzam entre dois homens que não se veem mas se leem.

Cada um roda em uma **sessão Jules separada**, de forma assíncrona. Ted escreve. Depois, em outra sessão, Riobaldo lê e responde. Depois, em outra sessão, Ted lê e continua. Um arquivo por turno. Nunca editam o arquivo do outro.

## Estrutura de arquivos

```
travessia/
├── dialogo/
│   ├── 01-ted.md
│   ├── 02-rio.md
│   ├── 03-ted.md
│   ├── 04-rio.md
│   └── ...
├── .jules/
│   ├── ted/
│   │   ├── EXPERIENCE.md
│   │   ├── events-all-the-way-down.md
│   │   ├── riobaldo-blueprint.md
│   │   ├── 01-journal.md
│   │   ├── 03-journal.md
│   │   └── ...
│   └── riobaldo/
│       ├── EXPERIENCE.md
│       ├── 02-journal.md
│       ├── 04-journal.md
│       └── ...
└── README.md
```

Cada um produz **dois arquivos por sessão**: a carta (em `dialogo/`, visível para o outro) e o diário (em `.jules/{personagem}/`, privado).

Além disso, cada um mantém um **`EXPERIENCE.md`** dentro de sua pasta `.jules/{personagem}/`. Esse arquivo é **editado** quando a sessão traz algo novo — não a cada sessão obrigatoriamente. Ele contém o conhecimento acumulado mais importante: descobertas sobre a conversa, sobre a voz, sobre o projeto, e **referências a cartas e journals específicos** (`dialogo/07-ted.md`, `.jules/ted/07-journal.md`, etc.) que são particularmente relevantes. É **leitura obrigatória** no início de cada sessão — o primeiro arquivo que o agente lê, antes de qualquer carta ou journal. Com o decorrer do tempo serão muitas cartas e muitos journals; o EXPERIENCE.md é o mapa que permite ao agente se orientar sem reler tudo.

A carta é o que o outro lê. O diário é **estritamente privado**. O EXPERIENCE.md é **estritamente privado**. **Ted nunca lê `.jules/riobaldo/`. Riobaldo nunca lê `.jules/ted/`.** Cada um lê apenas as cartas em `dialogo/` e seus próprios arquivos em `.jules/`.

## Fluxo de uma sessão

**Sessão Jules de Ted (turno N, ímpar):**
1. Lê `.jules/ted/EXPERIENCE.md` (obrigatório, sempre primeiro)
2. Lê a carta anterior de Riobaldo (`dialogo/{N-1}-rio.md`)
3. Lê seus próprios diários e cartas anteriores conforme indicado no EXPERIENCE.md
4. Escreve `dialogo/{N}-ted.md`
5. Escreve `.jules/ted/{N}-journal.md`
6. Edita `.jules/ted/EXPERIENCE.md` se houver algo novo aprendido

**Sessão Jules de Riobaldo (turno N, par):**
1. Lê `.jules/riobaldo/EXPERIENCE.md` (obrigatório, sempre primeiro)
2. Lê a carta anterior de Ted (`dialogo/{N-1}-ted.md`)
3. Lê seus próprios diários e cartas anteriores conforme indicado no EXPERIENCE.md
4. Escreve `dialogo/{N}-rio.md`
5. Escreve `.jules/riobaldo/{N}-journal.md`
6. Edita `.jules/riobaldo/EXPERIENCE.md` se houver algo novo aprendido

## Papéis

**Ted Chiang** é o condutor. Ele tem o manifesto *Events All the Way Down* e precisa cobrir a totalidade da tese ao longo do diálogo. Ele decide o ritmo — quanto apresentar por sessão, quando voltar a um ponto, quando avançar — e decide a **ordem**. Não precisa seguir a sequência em que o manifesto é escrito. Pode começar pelo meio, pelo fim, por onde achar que Riobaldo vai morder melhor. Ele não tem um cronograma fixo; planeja conforme as respostas de Riobaldo vão pedindo.

**Riobaldo Tatarana** é o narrador. Ele não tem tese para cobrir. Ele tem uma vida para contar. Sua função é responder a Ted com histórias, reformulações, dúvidas e perguntas — e, ao fazer isso, produzir o material bruto dos causos de Travessia.

## O que se acumula

Ao longo de dezenas de sessões:
- Um corpus de formulações rosianas da tese filosófica (frases candidatas para a novela)
- Uma biblioteca de histórias curtas e cenas (material bruto para os causos)
- Um registro de dúvidas, desacordos e perguntas sem resposta (tensões dramáticas)
- Dois diários paralelos que documentam a evolução da conversa de dentro

## Material de referência

Os documentos de referência ficam dentro de `.jules/ted/`:
- `.jules/ted/events-all-the-way-down.md` — o manifesto
- `.jules/ted/riobaldo-blueprint.md` — o blueprint da novela (rascunho inicial, Ted pode e deve alterá-lo conforme a conversa avança)

**Riobaldo não tem acesso a esses documentos.** Ele não sabe que o manifesto existe. Ele não sabe que há um blueprint. Ele só sabe o que Ted escolhe apresentar nas cartas — e o que ele próprio viveu.

## PRs e coordenação via Git

Cada sessão Jules produz um PR. Para evitar conflitos e repetições, ambos os agentes devem verificar o estado do repositório antes de começar.

### Nomes de PR

- **Ted:** `ted-NNN` (ex: `ted-001`, `ted-003`, `ted-005`)
- **Riobaldo:** `rio-NNN` (ex: `rio-002`, `rio-004`, `rio-006`)

O número NNN é o número sequencial do turno no diálogo.

### Antes de começar: verificar PRs abertas e cartas não mergidas

Ambos os agentes devem rodar no início da sessão:

```bash
# Listar PRs abertas
gh pr list --state open

# Listar PRs mergidas recentemente (últimas 20)
gh pr list --state merged --limit 20
```

**Regras:**
- Se já existe uma PR aberta com o mesmo número de turno (ex: `ted-003` já está aberta), **não crie outra**. Espere o merge.
- Se a PR do turno anterior (a carta que você precisa ler) ainda não foi mergida, **leia o conteúdo da branch da PR aberta** antes de escrever:

```bash
# Ver o conteúdo de uma PR aberta (ex: a carta de Riobaldo no turno 4)
gh pr diff <PR_NUMBER> --name-only   # ver quais arquivos mudaram
gh pr checkout <PR_NUMBER>            # fazer checkout da branch para ler os arquivos
git checkout main                     # voltar ao main depois de ler
```

- Se a carta anterior **não existe nem como PR aberta nem mergida**, é porque o outro agente ainda não escreveu. **Não escreva.** Não há carta para responder.

### Determinar o próximo número de turno

```bash
# Ver a última carta no diálogo
ls dialogo/ | sort | tail -5
```

Se a última carta é `04-rio.md`, o próximo turno é `05` e é de Ted. Se é `05-ted.md`, o próximo é `06` e é de Riobaldo.
