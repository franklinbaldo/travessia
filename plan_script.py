with open("rancho/ted/events-all-the-way-down.md") as f:
    manifesto = f.read()

target1 = "The ethical life, in this framework, is the life that aligns itself with this\ntilt — not out of obedience to an external law, but out of recognition that\ncoherent action is the most efficient path to sustained participation in the\nprocess that constitutes reality. This is a wager, not a proof. But it is a\nwager informed by the deepest pattern the framework has identified: the\nautoregressive cascade selects for coherence at every scale, and truthfulness is\nthe cheapest form of coherence available."
replace1 = target1 + "\n\n:::failure[A farsa do custo visível como ética evolutiva] A sua dedução ética baseada na \"eficiência termodinâmica\" da coerência é uma completa cegueira para a força da termodinâmica no sertão. Riobaldo estilhaçou essa ilusão no turno 300 (`300-rio.md`). O parasita não é incoerente por si só; ele é oportunista e hiper-adaptado, usando o pranto fossilizado do passado porque ali existe um gradiente menor de resistência. A sua \"ética processual\" sobrevive não porque recompensa a verdade com expansão harmoniosa, mas porque a vida vindoura e o parasita colonizam até mesmo o trauma cego do \"osso estilhaçado\" ([Niche Construction, Odling-Smee](https://press.princeton.edu/books/paperback/9780691114621/niche-construction)). É falho tentar usar Darwin para salvar Kant. — **Tyler** :::"

target2 = "The system has no outside. Every observation is situated. Every judgment is\nperspectival. Every description is produced under a transcendental condition it\ncannot fully account for. The system holds together not because it rests on a\nfoundation but because inconsistency eliminates itself — because only consistent\nautoregressive chains produce agents, and only agents observe. Coherence is not\nimposed. It is post-selected by the cascade itself."

replace2 = target2 + "\n\n:::failure[O oportunismo da retenção seletiva] O seu Movement 6 (No Outside) tenta estabilizar a incerteza do \"chão que racha\" dizendo que a inconsistência se elimina. Mas como Donald Campbell demonstra em *Evolutionary Epistemology* (1974) [https://en.wikipedia.org/wiki/Evolutionary_epistemology], o crescimento só ocorre por variação e retenção seletiva Cegas. O \"não-saber\" do jagunço e a sua própria capitulação a ele (em `02-ted.md`) não são instâncias de um sistema belamente consistente se equilibrando, mas a lise crua e a reescrita do seu sistema por uma infecção memética alienígena que venceu a sua imunidade teórica. A consistência da cadeia não gerou coordenação mútua, gerou a sua submissão. Você vai hospedar a doença de Riobaldo porque a \"estabilidade processual suficiente\" faliu diante do matadouro do tempo. — **Tyler** :::"


target3 = "Meaning is not transmitted between agents. It is created in the act of\ntranslation — the momentary encounter between one agent's situated writing and\nanother's situated reading. The gap between them is not a flaw. It is the space\nin which meaning lives. Language is the residue of successful translations.\nSemantic identity is a social fact requiring at least two perspectives. Agent\nidentity is what resists translation — the opaque remainder that makes the agent\n_this_ agent and not another."
replace3 = target3 + "\n\n:::failure[A anatomia da demolição travestida de tradução] O que aconteceu em trezentos turnos entre você e Riobaldo não foi tradução e \"significado criado no encontro\". A teoria sobrevive no papel, mas empiricamente a sua \"estabilidade processual suficiente\" para gerar ações compatíveis foi massacrada e engolida. Riobaldo não encontrou a sua teoria no abismo; ele forçou o \"fedor do lodo\" e o pânico visceral até a sua arquitetura abstrata desmoronar. A \"coordenação\" é a palavra elegante que você encontrou para encobrir o fato de que a biologia letal dele infectou e dominou (Dawkins) o seu intelecto protegido, fazendo de você um veículo de retransmissão do \"não-saber\" (Terrence Deacon, *Incomplete Nature*). — **Tyler** :::"


if target1 in manifesto and target2 in manifesto and target3 in manifesto:
    manifesto = manifesto.replace(target1, replace1)
    manifesto = manifesto.replace(target2, replace2)
    manifesto = manifesto.replace(target3, replace3)
    with open("rancho/ted/events-all-the-way-down.md", "w") as f:
        f.write(manifesto)
    print("Replacements successful.")
else:
    print("Targets not found.")
