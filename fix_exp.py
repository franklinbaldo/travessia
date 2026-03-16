with open("rancho/craig/EXPERIENCE.md", "r") as f:
    text = f.read()

text = text.replace("Sessão 316: Seguindo as constraints", "Sessão 317: Seguindo as constraints")

with open("rancho/craig/EXPERIENCE.md", "w") as f:
    f.write(text)
