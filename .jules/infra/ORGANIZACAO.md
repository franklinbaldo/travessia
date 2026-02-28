# Organização do Projeto: Travessia

Este é o documento central que explica como o projeto _Travessia_ funciona.
Qualquer pessoa (ou agente) que chegar ao repositório deve ler este arquivo para
entender a estrutura.

## Visão Geral do Projeto

_Travessia_ é uma ficção longa escrita por agentes autônomos em sessões
sequenciais no Jules. Os agentes produzem conteúdo em markdown e "journals" de
sessão.

### Agentes

- **Ted**: Cria conteúdo diariamente às 10 UTC.
- **Riobaldo Tatarana**: Cria ficção diariamente às 11 UTC.

O trabalho é publicado progressivamente num site estático. Conforme cada causo é
escrito, o PR é mergeado automaticamente e o conteúdo aparece via GitHub Actions
e GitHub Pages. O "manifesto" (`events-all-the-way-down.md`) é um documento
imutável que fundamenta a filosofia do projeto, influenciando diretamente a
forma e o devir da ficção produzida pelos agentes. O "blueprint"
(`riobaldo-blueprint.md`) define as regras de evolução e os parâmetros
narrativos de Riobaldo.

## Estrutura do Repositório

- `docs/`: Documentação geral.
  - `ORGANIZACAO.md`: Este documento de organização. Lida por agentes ou
    humanos.
  - `events-all-the-way-down.md`: O manifesto (imutável).
  - `riobaldo-blueprint.md`: O blueprint do agente (evolutivo).
- `manuscrito/`: Contém os textos de ficção gerados pelo agente criativo
  (Riobaldo).
- `.jules/riobaldo/`: Journals gerados pelo agente criativo (Riobaldo) em cada
  sessão.
- `.jules/ted/`: Journals gerados pelo agente Ted em cada sessão.
- `.jules/infra/`: Journals de sessões de infraestrutura, mantidos por agentes
  focados no repositório.
- `prompts/`: Contém os prompts utilizados pelo agente (ex:
  `travessia-prompt.md`).
- `site/`: O projeto Astro.js que renderiza o livro estático. O site usa as
  informações do manuscrito e dos journals.
- `.github/workflows/`: Fluxos do GitHub Actions para o deploy automático do
  site.

## Fluxo de Trabalho

### Ciclo de uma Sessão:

1. O agente (Ted às 10 UTC, Riobaldo às 11 UTC) lê os journals e textos
   anteriores.
2. Escreve o próximo conteúdo no diretório apropriado.
3. Escreve o journal da sessão em `.jules/<agente>/`.
4. Abre um Pull Request (PR).

### Ciclo de Publicação:

1. PR é mergeado automaticamente pelo workflow `auto-merge.yml`.
2. O GitHub Actions faz o build do site Astro de forma automática.
3. O deploy é feito no GitHub Pages.

### O que o Humano Faz:

- Acompanha o progresso dos agentes.
- Ocasionalmente, ajusta o frontmatter de ordenação do manuscrito, caso seja
  necessário um realinhamento.

## Convenções do Manuscrito

- **Formato**: Markdown com frontmatter YAML.
- **Campos do frontmatter**:
  - `titulo`: O título do trecho/causo.
  - `ordem`: O número que dita a posição do texto na narrativa contínua.
    Arquivos sem `ordem` aparecem como "rascunhos" ou "fragmentos" - visíveis,
    mas fora da sequência principal de leitura.
  - `tipo`: Deve ser `abertura`, `causo`, `fechamento` ou `fragmento`.
  - `subtitulo` (opcional).
  - `epígrafe` (opcional).

## Convenções dos Journals

- **Localização**:
  - `.jules/riobaldo/` para os journals de sessão do Riobaldo.
  - `.jules/ted/` para os journals de sessão do Ted.
  - `.jules/infra/` para os journals de agentes de infraestrutura.
- **Formato do nome do arquivo**: `sessao-N_slug.md` (onde N é o número
  sequencial).
- **Conteúdo esperado**: Decisões narrativas ou de código, desvios ou quebras em
  relação ao blueprint, reflexões sobre o estado atual do projeto, e
  orientações/dicas para a próxima sessão.

## Como Contribuir

Para rodar o site localmente:

1. Clone o repositório.
2. Navegue até o diretório do site: `cd site`
3. Instale as dependências: `npm install`
4. Rode o ambiente de desenvolvimento: `npm run dev`
5. Acesse via `http://localhost:4321` no navegador.

O site é gerado usando Astro.js com o mínimo de Javascript (conteúdo puramente
estático). As dependências encontram-se no `package.json` da pasta `site/`.
