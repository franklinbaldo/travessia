#!/usr/bin/env bash
# sortear-constraints.sh — Gera constraints aleatórias para a próxima sessão
# Usa /dev/urandom para aleatoriedade real (sem viés de LLM).
#
# Uso: bash tools/sortear-constraints.sh <agente>
#   agente: riobaldo | ted | tyler | craig
#
# Output: .jules/<agente>/next-constraints.md (commitável)

set -euo pipefail

AGENT="${1:?Uso: bash tools/sortear-constraints.sh <agente>}"
REPO_ROOT="$(cd "$(dirname "$0")/.." && pwd)"
OUTPUT_DIR="${REPO_ROOT}/.jules/${AGENT}"
OUTPUT_FILE="${OUTPUT_DIR}/next-constraints.md"

# Função: sorteia um índice de 0 a N-1 usando /dev/urandom
pick() {
  local n="$1"
  local rand
  rand=$(od -An -tu4 -N4 /dev/urandom | tr -d ' ')
  echo $(( rand % n ))
}

# Função: seleciona elemento de array por índice
choose() {
  local -n arr=$1
  local idx
  idx=$(pick ${#arr[@]})
  echo "${arr[$idx]}"
}

# ============================================================
# DIMENSÕES POR AGENTE
# ============================================================

generate_riobaldo() {
  local -a tom=("confronto" "ternura" "humor seco" "reverência" "raiva fria")
  local -a forma=("carta longa" "carta curta (máx 20 linhas)" "lista numerada" "diálogo reconstruído de memória" "carta normal")
  local -a campo=("fogo e brasa" "bicho e rastro" "pedra e osso" "vento e poeira" "silêncio e escuro" "água e lama" "livre")
  local -a tempo=("passado remoto (infância/juventude)" "guerra (anos de jagunço)" "agora (varanda/velhice)" "futuro imaginado")
  local -a restricao=(
    "sem nenhuma pergunta — só afirmações e declarações"
    "sem metáfora de água ou rio — encontre outro campo"
    "comece pelo fim — conte o resultado antes da história"
    "a carta gira em torno de um único objeto físico concreto"
    "Riobaldo discorda radicalmente de Ted nesta sessão"
    "máximo 1 neologismo na carta inteira"
    "sem provérbios fabricados — só narração direta"
    "sem restrição especial"
    "sem restrição especial"
  )

  local t=$(choose tom)
  local f=$(choose forma)
  local c=$(choose campo)
  local tp=$(choose tempo)
  local r=$(choose restricao)

  cat > "$OUTPUT_FILE" <<EOF
---
gerado: $(date -u +%Y-%m-%dT%H:%M:%SZ)
agente: riobaldo
---

# Constraints para a próxima sessão

Estas constraints foram geradas por sorteio real (urandom). São obrigatórias.

| Dimensão | Valor sorteado |
|----------|---------------|
| **Tom** | ${t} |
| **Forma** | ${f} |
| **Campo sensorial dominante** | ${c} |
| **Tempo narrativo** | ${tp} |
| **Restrição formal** | ${r} |

## Como aplicar

- **Tom**: define a temperatura emocional da carta. "${t}" deve permear o texto inteiro, não só o início.
- **Forma**: "${f}" — siga este formato. Se for "lista numerada", a carta é uma lista. Se for "diálogo reconstruído", transcreva uma conversa de memória com falas diretas.
- **Campo sensorial**: as imagens e metáforas desta sessão devem vir prioritariamente de "${c}". Outros campos podem aparecer, mas este domina.
- **Tempo**: a memória/causo principal deve vir de "${tp}".
- **Restrição**: "${r}". Se houver restrição, é inviolável.
EOF
}

generate_ted() {
  local -a tom=("provocação intelectual" "escuta atenta" "admiração declarada" "dúvida genuína" "urgência")
  local -a tamanho=("longo (carta completa)" "médio (2-3 parágrafos)" "curto (1 parágrafo)" "mínimo (3-5 frases)")
  local -a foco=("responder perguntas de Riobaldo sem apresentar ideia nova" "ideia nova do manifesto" "retomar fio de sessões anteriores" "só perguntas — nenhuma afirmação")
  local -a modo=("só imagens concretas — zero abstração" "abstração permitida onde necessária" "só perguntas para Riobaldo" "modo normal")

  local t=$(choose tom)
  local ta=$(choose tamanho)
  local f=$(choose foco)
  local m=$(choose modo)

  cat > "$OUTPUT_FILE" <<EOF
---
gerado: $(date -u +%Y-%m-%dT%H:%M:%SZ)
agente: ted
---

# Constraints para a próxima sessão

Estas constraints foram geradas por sorteio real (urandom). São obrigatórias.

| Dimensão | Valor sorteado |
|----------|---------------|
| **Tom** | ${t} |
| **Tamanho** | ${ta} |
| **Foco** | ${f} |
| **Modo** | ${m} |

## Como aplicar

- **Tom**: "${t}" — esta é a postura emocional de Ted nesta carta.
- **Tamanho**: "${ta}" — respeite o limite. Se saiu "mínimo", escreva 3-5 frases e pare. A brevidade é a constraint.
- **Foco**: "${f}" — este é o objetivo da carta. Se saiu "só perguntas", Ted não apresenta conteúdo, só pergunta.
- **Modo**: "${m}" — define o registro. Se saiu "só imagens concretas", Ted não pode usar linguagem abstrata.
EOF
}

generate_tyler() {
  local -a postura=("cético agressivo" "curioso e generoso" "demolidor cirúrgico" "entusiasmado (raro — algo o impressionou)" "lacônico")
  local -a foco=("argumento do manifesto" "referências cruzadas (links obrigatórios)" "qualidade do diálogo ted-riobaldo" "lacuna que ninguém viu")
  local -a extensao=("nota curta (máx 300 palavras)" "nota média (300-600 palavras)" "nota longa (600-800 palavras)")

  local p=$(choose postura)
  local f=$(choose foco)
  local e=$(choose extensao)

  cat > "$OUTPUT_FILE" <<EOF
---
gerado: $(date -u +%Y-%m-%dT%H:%M:%SZ)
agente: tyler
---

# Constraints para a próxima sessão

Estas constraints foram geradas por sorteio real (urandom). São obrigatórias.

| Dimensão | Valor sorteado |
|----------|---------------|
| **Postura** | ${p} |
| **Foco** | ${f} |
| **Extensão** | ${e} |

## Como aplicar

- **Postura**: "${p}" — define o tom de Tyler. Se saiu "demolidor cirúrgico", pelo menos metade das anotações devem ser críticas duras.
- **Foco**: "${f}" — este é o eixo principal da sessão.
- **Extensão**: "${e}" — respeite o limite.
EOF
}

generate_craig() {
  local -a foco=("tipografia e espaçamento" "cor e contraste" "layout e estrutura" "microinterações e detalhes" "performance e simplicidade")
  local -a inspiracao=("livro impresso clássico" "revista literária contemporânea" "manuscrito/caderno" "web brutalista" "livre")
  local -a restricao=("nenhuma mudança estrutural — só refinamento" "pelo menos uma mudança visível e ousada" "focar numa única página/componente" "sem restrição")

  local f=$(choose foco)
  local i=$(choose inspiracao)
  local r=$(choose restricao)

  cat > "$OUTPUT_FILE" <<EOF
---
gerado: $(date -u +%Y-%m-%dT%H:%M:%SZ)
agente: craig
---

# Constraints para a próxima sessão

Estas constraints foram geradas por sorteio real (urandom). São obrigatórias.

| Dimensão | Valor sorteado |
|----------|---------------|
| **Foco** | ${f} |
| **Inspiração** | ${i} |
| **Restrição** | ${r} |

## Como aplicar

- **Foco**: "${f}" — esta sessão deve se concentrar neste aspecto do design.
- **Inspiração**: "${i}" — use como referência estética dominante.
- **Restrição**: "${r}".
EOF
}

# ============================================================
# MAIN
# ============================================================

if [[ ! -d "$OUTPUT_DIR" ]]; then
  echo "Erro: diretório ${OUTPUT_DIR} não existe. Agente '${AGENT}' é válido?" >&2
  exit 1
fi

case "$AGENT" in
  riobaldo) generate_riobaldo ;;
  ted)      generate_ted ;;
  tyler)    generate_tyler ;;
  craig)    generate_craig ;;
  *)
    echo "Erro: agente '${AGENT}' não reconhecido. Use: riobaldo | ted | tyler | craig" >&2
    exit 1
    ;;
esac

echo "Constraints geradas em: ${OUTPUT_FILE}"
cat "$OUTPUT_FILE"
