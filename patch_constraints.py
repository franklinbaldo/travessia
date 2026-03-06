import re

with open(".jules/ted/next-constraints.md", "r") as f:
    content = f.read()

target = """## Como aplicar

- **Tom**: "admiração declarada" — esta é a postura emocional de Ted nesta carta.
- **Tamanho**: "curto (1 parágrafo)" — respeite o limite. Se saiu "mínimo", escreva 3-5 frases e pare. A brevidade é a constraint.
- **Foco**: "ideia nova do manifesto" — este é o objetivo da carta. Se saiu "só perguntas", Ted não apresenta conteúdo, só pergunta.
- **Modo**: "só perguntas para Riobaldo" — define o registro. Se saiu "só imagens concretas", Ted não pode usar linguagem abstrata.
"""
new_block = """## Como aplicar

- **Tom**: "admiração declarada" — esta é a postura emocional de Ted nesta carta.
- **Tamanho**: "curto (1 parágrafo)" — respeite o limite. Se saiu "curto", escreva 1 parágrafo e pare.
- **Foco**: "ideia nova do manifesto" — este é o objetivo da carta. Ted apresenta uma ideia nova do manifesto.
- **Modo**: "só perguntas para Riobaldo" — define o registro. Ted só pode se comunicar através de perguntas para Riobaldo nesta carta.
"""

new_content = content.replace(target, new_block)

with open(".jules/ted/next-constraints.md", "w") as f:
    f.write(new_content)
