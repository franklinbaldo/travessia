import sys

with open('cartas/ted-riobaldo/126-rio.md', 'r', encoding='utf-8') as f:
    content = f.read()

# Fix the dialogue spacing
content = content.replace(
    'Eu me cheguei perto. "Diadorim, encosta pra cá. Vem quentar a mão nessa brasa", eu falei, baixinho, pra não espantar a mudeza da noite.\nDiadorim me olhou e arrespondeu, não com a boca frouxa do alívio, mas feito quem desama a vida. "Jagunço não pode ter o corpo quente demais, Riobaldo. O calor amolece a precisão."\n"Mas o frio dói no osso, Reinaldo", teimei, de coração nas mãos. "O frio enrija e endurece as juntas do caboclo."\n"É a precisura de não sentir, Riobaldo. O ferro pra cortar carece ser frio. Se a mão esquenta demais, a gente deslembra que tá em guerra, afrouxa o pulso. O calor vicia."\n"E se a guerra acabar, Diadorim? E se a gente sentar pra descanso e só sobrar a fogueira da paz, pra ajuntar família e vizinho?"\nFoi quando ele me deu um sorriso que rasgou a noite como espinho, um rastro triste. "A gente já virou a guerra, Riobaldo. A mão que pega no gume nunca mais se achega na brasa sem arder nela inteira. Quem amola, esfria junto."',
    'Eu me cheguei perto. "Diadorim, encosta pra cá. Vem quentar a mão nessa brasa", eu falei, baixinho, pra não espantar a mudeza da noite.\n\nDiadorim me olhou e arrespondeu, não com a boca frouxa do alívio, mas feito quem desama a vida. "Jagunço não pode ter o corpo quente demais, Riobaldo. O calor amolece a precisão."\n\n"Mas o frio dói no osso, Reinaldo", teimei, de coração nas mãos. "O frio enrija e endurece as juntas do caboclo."\n\n"É a precisura de não sentir, Riobaldo. O ferro pra cortar carece ser frio. Se a mão esquenta demais, a gente deslembra que tá em guerra, afrouxa o pulso. O calor vicia."\n\n"E se a guerra acabar, Diadorim? E se a gente sentar pra descanso e só sobrar a fogueira da paz, pra ajuntar família e vizinho?"\n\nFoi quando ele me deu um sorriso que rasgou a noite como espinho, um rastro triste. "A gente já virou a guerra, Riobaldo. A mão que pega no gume nunca mais se achega na brasa sem arder nela inteira. Quem amola, esfria junto."'
)

with open('cartas/ted-riobaldo/126-rio.md', 'w', encoding='utf-8') as f:
    f.write(content)
print("Dialogue spacing patched.")
