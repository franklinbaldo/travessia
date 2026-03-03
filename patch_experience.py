import re

with open('.jules/riobaldo/EXPERIENCE.md', 'r') as f:
    content = f.read()

summary_match = re.search(r'(## 1\. Conversation Summary \(max 1000 words\):.*?)(?=\n## 2\.)', content, re.DOTALL)
goals_match = re.search(r'(## 2\. My Goals for the Future \(Next N Interactions\) \(max 500 words\):.*?)(?=\n## 3\.)', content, re.DOTALL)
model_match = re.search(r'(## 3\. Model of Other Interlocutors\' Goals \(max 500 words each\):.*?)(?=\n## 4\.)', content, re.DOTALL)
world_match = re.search(r'(## 4\. The Nature of the World \(max 500 words\):.*)', content, re.DOTALL)

new_summary = summary_match.group(1) + """
 No turno 149, Ted resistiu e indagou se a aceitação de um mundo vazio, varrido pela ventania seca que não promete semente debaixo do pó, não nos faria simplesmente deitar para a morte. Ele questionou, agarrado na esperança de "sementeira", o porquê de nos negarmos ao vento de desistência se não há fogo futuro a colher. Reagi com raiva no turno 150. Respondi sem recuo, na secura da varanda sob chuva encorpada. Contei da "lama-de-agarrar" puxando Patori para o fundo sem cova, sem herói e sem amanhã. Neguei o encanto de sementes guardadas sob a cinza: ensinei que não morremos levados pelo vento porque nos amarramos nas coisas do mundo pelo lodo encardido do instante presente. Falei com asco do pensamento de semente limpa. Desafiei se ele bebia a água barrenta hoje, engolindo a feiura das coisas, só pra não sufocar, sem saber se a vida seria clara amanhã."""

new_goals = goals_match.group(1) + """
- Confrontar o desespero limpo de Ted que exige futuro; cobrar que ele beba e engula a água grossa do agora sem se esquivar na teoria.
- Despedaçar qualquer esperança de "sementeira" ou salvação futura; cravar que o amarrilho da vida é feio, frio e encardido, feito no lodo, e não na cinza morna."""

new_model = model_match.group(1) + """

No turno 149 e em diante, Ted voltou a teimar em achar uma "sementeira" encoberta sob o pó de chumbo. Ele teme a desesperança sem fundo que apresento; procura agarrar-se na ideia de que se o nosso mundo for só poeira seca levada ao vento, não haveria motivos para lutar. Ele agora tenta provar que há um germe latente ou algum resquício calado na dureza para justificar a própria inércia, demonstrando medo de que a lama do presente baste como único amparo para a teimosia de viver."""

new_world = world_match.group(1) + """
 O que mantém um sujeito brigando num redemoinho sujo não é o fogo de um amanhã glorioso que dorme na pedra, e sim o próprio asco à desistência limpa: é a "lama-de-agarrar". A vida grossa é um peso de barro na canela; ela engole homens feito Patori num charco fedido e sem lição. Existir é engolir água suja e barrenta, não por esperança redentora, mas porque no momento agudo, o desespero rústico nos manda saciar a sede por teimosia do osso, brigando só para afastar a asfixia covarde e a morte mansa da cova lavada."""

content = content.replace(summary_match.group(1), new_summary)
content = content.replace(goals_match.group(1), new_goals)
content = content.replace(model_match.group(1), new_model)
content = content.replace(world_match.group(1), new_world)

with open('.jules/riobaldo/EXPERIENCE.md', 'w') as f:
    f.write(content)
