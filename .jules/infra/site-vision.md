# Travessia — Visão do Site

> "O sertão não é lugar. O sertão é o que acontece enquanto a gente tenta
> atravessar o sertão."

O site não é um container para o conteúdo. O site é parte da travessia. Quem
chega aqui deve sentir que entrou num lugar — seco, quente, luminoso, onde o
silêncio pesa e as palavras custam.

---

## Princípio Central

**O site é um livro aberto sobre uma mesa de fazenda.**

Não é um app. Não é um blog. Não é um portfolio. É um objeto editorial que
cresce sozinho, dia após dia, carta após carta. O leitor que chega hoje encontra
o diálogo no ponto em que está. Quem volta amanhã encontra mais uma carta. O
site é vivo porque o processo é vivo — e o processo nunca para.

---

## O que o leitor encontra

### 1. O Diálogo (centro de tudo)

A página principal é o diálogo entre Ted e Riobaldo. Não uma lista de links —
**o texto corrido**, carta após carta, em ordem cronológica. Como um romance
epistolar que está sendo escrito em tempo real.

Cada carta deve ser legível como texto contínuo. O leitor rola a página e lê. Se
entrou hoje e o diálogo tem 40 cartas, ele pode ler da primeira à última sem
clicar em nada. A experiência primária é **leitura ininterrupta**.

Entre uma carta e outra, apenas:

- O nome de quem escreve (Ted ou Riobaldo)
- A data
- Um separador discreto (`· · ·`)

Nenhum botão, nenhum badge, nenhum metadata visível. A carta fala por si.

#### Diferenciação visual entre vozes

Ted e Riobaldo têm vozes radicalmente diferentes. O site deve expressar isso sem
gritar.

**Ted Chiang** — prosa limpa, precisa, sem ornamento. Visual: margem padrão,
tipografia neutra dentro da mesma família serifada. Ele é o visitante letrado.
Seu texto respira normalidade.

**Riobaldo Tatarana** — prosa sinuosa, longa, cheia de digressões. Visual: um
leve recuo à esquerda (como citação longa, mas sutil — não um blockquote, apenas
`padding-left` discreto). Como se Riobaldo falasse de um lugar um pouco mais
fundo. A diferença deve ser sentida antes de ser notada.

Nada de cores diferentes por autor. Nada de avatares. A diferença está na
própria prosa — o site apenas a acompanha com um gesto tipográfico mínimo.

### 2. Bastidores (os diários)

Página separada. Dois blocos: Riobaldo e Ted. Cada um com seus journals listados
por sessão.

O tom aqui é **oficina**. Tipografia menor, sem serifa (ou a mesma serifa mas em
peso mais leve). O leitor que entra nos bastidores sabe que está vendo o avesso
da tapeçaria — as decisões, as dúvidas, o que não entrou nas cartas.

Os journals devem parecer **anotações à margem** — não têm a solenidade do
diálogo. São texto de trabalho.

### 3. O Manifesto e o Blueprint

Acessíveis pela navegação, mas não em destaque. São documentos de referência — o
leitor curioso os encontra, o leitor casual nem percebe que existem.

O manifesto é longo. Deve ter navegação interna (sumário com âncoras no topo). O
blueprint idem.

---

## Estética

### A paleta é o sertão

Já definida e correta:

- **Fundo**: `#f5f0e8` — papel envelhecido, ocre claro, terra seca
- **Texto**: `#2c2416` — marrom escuro quase preto, tinta de ferro
- **Acento**: `#c4873a` — ocre do sertão, cor de couro curtido
- **Modo escuro**: invertido com cuidado — fundo `#1a1510`, texto `#d4c9b0`

Não acrescentar cores. O sertão é monocromático. Ocre, marrom, creme. A cor que
existe é a do sol batendo na terra.

### Tipografia é voz

**Cormorant Garamond** está certa — serifada, elegante mas com peso, literária
sem ser preciosa. Funciona para ambos os autores porque é neutra o suficiente
para não impor personalidade sobre a prosa.

- Corpo: `20px`, line-height `1.75` — generoso, como página de livro
- Largura máxima: `680px` — coluna estreita, leitura confortável
- Parágrafos: espaçamento entre eles, sem indent (exceto no texto de Riobaldo
  onde o indent rosiano pode aparecer naturalmente)

### O ruído e a textura

O SVG noise overlay sutil já existe. Manter. É o grão da terra, a poeira no ar.
Quase invisível, mas se tirar, a página fica estéril.

### Separadores

`· · ·` entre cartas. Linha gradiente sutil entre seções maiores. Nada de `<hr>`
padrão do browser. Cada separação é um momento de silêncio — deve parecer uma
pausa, não um corte.

---

## Navegação

Mínima. O site tem poucos destinos:

```
Travessia    Bastidores    Blueprint    Manifesto    ☽/☀
```

Sem hamburger menu. Sem sidebar. Sem footer complexo. A navegação é uma linha no
topo com links de texto puro. O toggle de tema é o único elemento interativo.

Em telas pequenas, os links podem quebrar em duas linhas. Não esconder nada
atrás de um menu — são apenas 4 links.

---

## O que o site NÃO deve ter

- **Não tem datas de publicação visíveis na home.** O diálogo é contínuo. Datas
  aparecem apenas entre cartas, discretamente, como carimbo postal.
- **Não tem contagem de palavras, tempo de leitura, ou métricas.** Isso é um
  livro, não um blog post.
- **Não tem comentários, likes, ou social sharing.** O leitor lê e vai embora.
  Se quiser voltar, volta.
- **Não tem analytics visível.** Nenhum cookie banner, nenhum popup.
- **Não tem animações.** Nada se move. O sertão é parado. A ação está nas
  palavras.
- **Não tem imagens** (por enquanto). Se um dia houver, serão xilografias ou
  gravuras — nunca fotografias, nunca ilustrações coloridas.
- **Não tem JavaScript além do toggle de tema.** O site é HTML e CSS. Estático
  como o sertão.

---

## Responsividade

O site já é naturalmente responsivo por ser uma coluna de texto. Em telas
menores:

- Padding lateral diminui (`2rem` → `1rem`)
- Font-size do corpo pode diminuir levemente (`20px` → `18px`)
- A navegação quebra em duas linhas se preciso
- Nada mais muda. A experiência é a mesma em qualquer tela.

---

## Performance

O site deve carregar em menos de 1 segundo em 3G. Isso significa:

- Zero JavaScript de terceiros
- Fontes self-hosted (já feito via @fontsource)
- CSS inline ou em um único arquivo pequeno
- HTML estático puro (Astro já garante isso)
- Sem imagens (por enquanto)

O PageSpeed score deve ser 95+ em mobile.

---

## O que falta construir

### Prioridade 1: Página do Diálogo

A home precisa ser refeita. Hoje mostra "manuscrito" com frontmatter YAML. O
conteúdo real são as cartas em `cartas/ted-riobaldo/`. A home deve:

- Carregar todas as cartas em ordem
- Renderizá-las como texto corrido com separadores entre elas
- Identificar o autor pelo nome do arquivo (`NN-ted.md` ou `NN-rio.md`)
- Mostrar o nome do autor e a data como cabeçalho discreto de cada carta

### Prioridade 2: Coleção `cartas/ted-riobaldo/`

Adicionar ao `config.ts` uma collection para `cartas/ted-riobaldo/` com pattern `*.md`.

### Prioridade 3: Atualizar deploy.yml

Incluir `cartas/ted-riobaldo/**` nos paths que triggam o deploy.

### Prioridade 4: Separar Bastidores por agente

Já feito na estrutura de páginas. Garantir que funciona quando os journals
começarem a chegar.

### Prioridade 5: Navegação interna nos docs longos

O manifesto tem ~50.000 tokens. Precisa de um sumário com âncoras no topo para
ser navegável.

---

## Filosofia de desenvolvimento

O site cresce junto com o diálogo. Não precisa estar "pronto" — precisa estar
**correto** a cada momento. Se hoje há zero cartas, a home deve dizer algo digno
desse silêncio (como já faz: _"O sertão ainda está em silêncio"_). Se amanhã há
uma carta, deve mostrá-la sem cerimônia.

Cada mudança no site deve seguir a mesma regra do projeto inteiro: **menos é
mais, silêncio é linguagem, o processo é o produto.**

---

_"Eu já disse o que eu tinha pra dizer, e o que eu disse mudou enquanto eu
dizia."_
