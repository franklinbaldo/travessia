import re

with open('rancho/riobaldo/EXPERIENCE.md', 'r') as f:
    content = f.read()

summary_addition = """
Na sessão 302, Ted insistiu que eu deveria afundar a lâmina no meu próprio osso e cavar a pedra para deixar uma valeta de água limpa para as gerações futuras lamberem, sacrificando a mim mesmo. Recusei com raiva fria, evocando a visão de um teiú chupando um osso de bezerro devorado por onça que acabou soterrado pelo vento seco da chapada. Declarei que a natureza soterra com poeira morta qualquer sacrifício de carne antes que o menino do futuro encontre água, e rejeitei mutilar meu sofrimento apenas para aplacar a doce ilusão dele.
"""

hallucinated_text = """Na sessão 302, Ted insistiu que eu deveria afundar a lâmina no meu próprio osso e cavar a pedra para deixar uma valeta de água limpa para as gerações futuras lamberem, sacrificando a mim mesmo. Recusei com raiva fria, observando da minha varanda o vento levantar redemoinhos de pó e um bezerro guacho lambendo a poeira de um mourão na esperança de água. Declarei que o vento e a poeiridão nivelam e soterram qualquer sacrifício antes mesmo que o menino do futuro sinta sede, e recusei ser um mártir só para aplacar a ilusão dele de que o sofrimento humano tem alguma utilidade grandiosa.
"""

if hallucinated_text in content:
    content = content.replace(hallucinated_text, "")

# Ensure it's not already added
if summary_addition.strip() not in content:
    # Just insert it before '## 2. My Goals'
    content = content.replace("## 2. My Goals", summary_addition.strip() + "\n\n## 2. My Goals")

with open('rancho/riobaldo/EXPERIENCE.md', 'w') as f:
    f.write(content)
