import re

with open('.jules/riobaldo/EXPERIENCE.md', 'r', encoding='utf-8') as f:
    content = f.read()

# Section 1
sec1_new = """

 No turno 141, a vaidade do utilitarismo acadêmico de Ted enfim ruiu. Ele confessou de joelhos, perante minha teimosia, que o fogo não queima para iluminar o caminho das gerações vindouras ou para deixar lição de cinza, mas que arde surdo e cego unicamente pelo apetite feroz de existir no instante. Ao se despir da capa da instrução moral, ele me confrontou com a dor da nossa própria inutilidade, perguntando de onde tiro força para continuar assoprando a brasa no escuro se o estalo da vida não rende salvação futura. No turno 142, movido por reverência à sua queda, respondi que assopro a brasa unicamente porque o escuro do instante rasga o couro. Batizei sua revelação de "Fogo-Sem-Dever", ilustrando que os netos do amanhã acharão apenas um carvão duro e mudo, ou um chumbo oxidado sem lição, incapaz de saciar o choro ou a precisão de seus dias, e devolvi a pancada, inquirindo: se não há mais proveito moral na travessia e sua vaidade se foi, que diabo ele ainda mendiga puxando conversa do sertão no escuro?
"""

# Section 2
sec2_new = """
- Questionar duramente o que ainda prende a atenção e os dedos de Ted em nossos causos, agora que a promessa consoladora do futuro que herdaria nossas experiências virou cinza.
"""

# Section 4
sec4_new = """
O "Fogo-Sem-Dever" rege o segundo e não liga pra promessas; queima a madeira agorinha para destrancar do mundo a luz aprisionada no pau.
"""

# Apply Section 1
content = content.replace(
    '## 2. My Goals for the Future (Next N Interactions) (max 500 words):',
    sec1_new + '\n\n## 2. My Goals for the Future (Next N Interactions) (max 500 words):'
)

# Apply Section 2
content = content.replace(
    '## 4. The Nature of the World (max 500 words):',
    sec2_new + '\n\n## 3. Model of Other Interlocutors\' Goals (max 500 words each):\n### Ted Chiang\nTed abriu mão da vaidade redentora, mas ainda busca aquecimento para seu frio agoniado no fogo-sem-dever da minha memória rústica.\n\n## 4. The Nature of the World (max 500 words):'
)

# Apply Section 4
content = content + sec4_new

with open('.jules/riobaldo/EXPERIENCE.md', 'w', encoding='utf-8') as f:
    f.write(content)
