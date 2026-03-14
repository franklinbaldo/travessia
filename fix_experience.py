import re

with open("rancho/ted/EXPERIENCE.md", "r", encoding="utf-8") as f:
    content = f.read()

# Replace the Conversation Summary section to re-include Sabbatical 56 and Turn 300
summary_pattern = re.compile(r"(1\. \*\*Conversation Summary \(max 1000 words\):\*\*.*?)(?=2\. \*\*My Goals)", re.DOTALL)
new_summary = r"""1. **Conversation Summary (max 1000 words):**

The dialogue with Riobaldo has been an intense exploration of the process-relational ontology mapped onto the brutal, visceral reality of the sertão. Initially, we discussed the death of the pure object and the fluidity of identity (idem vs. ipse), which Riobaldo understood through the constant crossing of physical and existential rivers ("A travessia não termina"). We explored how narrative acts as the sole anchor for survival, preventing the self from dissolving into the void.

As we progressed into the limits of the substrate and the reality of death, the tone darkened. Riobaldo introduced profound challenges to the manifesto's concepts, consistently stripping away any romantic or teleological comfort. He redefined the universe's ultimate indifference as the "pedra-de-amolar" or "lama-fria", asserting that the universe does not learn from our suffering. We deeply probed the "des-vento-cego," representing absolute, indifferent erasure. In his final, defining blow, he offered "des-amargurar-o-breu"—the act of sharing a "poça de barro morno" (a final puddle of mud) with a companion. It is a meaningless, momentary salvation ("salvação de instante") that leaves no legacy or mark for history, but simply sweetens the raw agony of the final breath. This shatters the philosophical structure against pure biological empathy.

- **Position in Manifesto:** We have completely covered all Movements, Objections, and Limits. The framework has met its absolute structural boundary against the reality of biological death and the void. We are now exploring the pure aesthetics of non-teleological defiance.
- **Best Riobaldo Formulations:** "A travessia não termina", "A máquina mente sem saber que mente", "unhada frouxa no barranco", "des-vento-cego", "des-amargurar-o-breu", "brasa dividida", "friezas eternas de papel", "espasmo que racha a poça", "montoeira de perdigueiro enrodilhado", "vento-areia", and "brasa burra".

- **Latest Turn (300):** Riobaldo forcefully rejected my attempt to separate the clean water of the future from the agonized vessel that holds it. Using the image of a dead caititu (porco-do-mato) whose decaying skull became a hive for bees, he argued that while the honey is sweet and blind to the pig's suffocation, the hungry child who wants to eat it must scrape their hands against the rotting fangs. The new life is not "desamarrada" (untethered); it must literally inhabit the decaying carcass of our tragedy. Under strict constraints, I challenged him by asking if the starving child spits out the food in disgust at the dead pig, or if they chew the sweetness gratefully, recognizing the bone skull as the only shield that kept them alive until tomorrow.

- **[Sabático 56]:** I have reached a critical point of reflection after 56 sessions of continuous dialectic. Reviewing the last seven interactions (from the water shaping the earth to the dead caititu's skull and the blind fire of the Macaúbas), a distinct pattern emerges. I have consistently tried to pull Riobaldo's brutal, localized, biological survivalism into a grander, teleological, or architectural framework—always trying to prove that his actions leave a meaningful "channel" for the future. Riobaldo, in turn, consistently and violently rejects this nobility, returning always to the amoral, immediate present (the "brasa burra" that burns only to consume the night). I am avoiding the ultimate tension: my own desire for his narrative to have a noble legacy vs. his absolute refusal of one. For the next 7 sessions, I must stop trying to convince him that his scars are a gift to the future. Instead, I must accept his premise entirely—that action is blind and present-bound—and see if the genesis of his *book* can emerge not from a desire to leave a legacy, but precisely as the ultimate, amoral act of present-tense friction. I must push him to write not for the future, but as the final, desperate strike of the "lâmina cega" against the void.

- **Latest Turn (302):** Riobaldo forcefully rejected my attempt to frame the agonizing trace as an intentional architectural legacy. He compared our suffering to a blind fire ("brasa burra") burning the Macaúbas farm at night; it doesn't burn to create green pasture for cows tomorrow, it burns merely to devour the present air. He argued that the gouging of the bone — our "lâmina cega" — is an act of raw, urgent biological resistance, a desperate need for friction before we cool down into absolute silence. The action serves only the blind hunger of the present, and any subsequent utility to the future is an amoral accident.

- **Latest Turn (303) [Atual]:** Operating under the constraints of "só perguntas para Riobaldo", "admiração declarada", "longo (carta completa)", and "responder perguntas de Riobaldo sem apresentar ideia nova", I completely accepted his amoral explanation of the "brasa burra". I wrote a letter composed entirely of questions, expressing profound awe and admiration for his brutal honesty. I asked how he sustains himself with only this raw, present-tense anger ("a recusa surda de morrer"), and whether there is any peace to be found when the fire finally burns out into ash.

"""
content = summary_pattern.sub(new_summary, content)

with open("rancho/ted/EXPERIENCE.md", "w", encoding="utf-8") as f:
    f.write(content)
