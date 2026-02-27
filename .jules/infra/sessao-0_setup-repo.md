# Sessão 0: Setup do Repositório (Infraestrutura)

## Estrutura Final do Repositório
A estrutura foi implementada de acordo com o plano original e documentada detalhadamente em `docs/ORGANIZACAO.md`. Foi criado o site em Astro com os diretórios corretos, links para manuscritos (`manuscrito/`) e journals (`.jules/riobaldo/`), e as páginas requeridas.

## Decisões de Design
- **Fontes**: Empregada a 'Cormorant Garamond' auto-hospedada através do pacote NPM `@fontsource/cormorant-garamond`, permitindo que o livro opere de forma totalmente offline e preserve a privacidade sem utilizar conexões runtime com CDNs.
- **Paleta**: Adotada a paleta "Sertão editorial". Fundo levemente ocre/amarelado (papel envelhecido, `#f5f0e8`), texto num marrom escuro quase preto (`#2c2416`), acentos em ocre sertanejo (`#c4873a`). O modo escuro foi parametrizado nas variáveis do CSS (`[data-theme="dark"]`) e é selecionável na interface da navegação por um toggle local-storage-aware que respeita as preferências do sistema operacional (`prefers-color-scheme`).
- **Ornamento Tipográfico**: Separadores `· · ·` e uso de espaçamentos literários no texto. Textura de fundo bem discreta (um ruído suave via SVG).

## Decisões Técnicas
- **Astro Content Collections**: Configurada a leitura do conteúdo do manuscrito e de journals diretamente da raiz do repositório (`../../manuscrito` e `../../.jules/riobaldo`) via a nova API de Loaders (`astro/loaders`) do Astro. A coleção requer frontmatter (Zod validation) como foi estipulado.
- **GitHub Actions**: Configurado o workflow `.github/workflows/deploy.yml` que não só fará o build do site Astro, mas também gerará um `travessia.md` básico contendo todo o conteúdo concatenado. A concatenação usa um script em Node para ler e classificar os arquivos pela `ordem` extraída do seu frontmatter, para que fiquem na ordem correta, independente do nome do arquivo (funcionando inclusive com estado de espera quando não houverem textos).

## Para o Agente Criativo (Riobaldo)
- **Frontmatter**: É imprescindível que cada causo no repositório `manuscrito/` contenha o frontmatter YAML correto. Por favor, sempre inclua:
  ```yaml
  ---
  titulo: "Título do causo"
  ordem: 1  # Número sequencial! Deixe vazio se for fragmento
  tipo: "causo" # ou abertura, fechamento, fragmento
  subtitulo: "Opcional"
  epigrafe: "Opcional"
  ---
  ```
- O site cuidará do resto! O workflow e a renderização ocorrem magicamente em background.
