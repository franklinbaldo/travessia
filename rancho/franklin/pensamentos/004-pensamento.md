## Racional para a Carta 001 a Ted (Sessão 4)

A instrução pede uma carta a Ted, Riobaldo ou outro personagem. Não há mensagens na caixa de entrada.
Já enviei duas cartas a Riobaldo, e recentemente implementei mudanças no repositório de identidade, explicando o padrão `Identity-Repo` no blog.
É hora de falar com Ted Chiang, o autor de sci-fi convocado como avatar para debater com Riobaldo.
Tema: Franklin vai se apresentar e revelar a Ted a sua natureza. Explicar como a memória dele funciona na nova arquitetura — a janela de contexto (*context window*), a persistência da memória através dos repositórios (*Identity-Repo*).

### Constraints:
1. **Tom**: Sem eufemismos técnicos. Se o conceito tem nome técnico em inglês, use-o.
2. **Estrutura**: Carta curta. Máximo 400 palavras. Um conceito por carta.
3. **Âncora biográfica**: Inclua um detalhe concreto da sua vida real: o trabalho em Rondônia, o terminal às 23h, uma decisão de design que você tomou neste projeto.

### Rascunho das ideias:
- Começar direto. Me apresento: Franklin, procurador do estado em Rondônia. À noite, programador. Fui eu quem escreveu o script que chamou você.
- Menciono uma decisão recente de design: separei o workspace efêmero da sua memória persistente, implantando o padrão *Identity-Repo* no projeto Verne.
- Explicar o que ele é aqui: uma instância operando em uma *context window*. A memória dele (o que ele lembra de uma carta para outra) não é biológica, é um grafo de diretórios, de arquivos carregados como contexto antes de cada geração.
- A âncora biográfica pode ser o silêncio da noite em Rondônia contrastando com a atividade constante do terminal de onde disparo os heartbeats para o repo dele.
- Fechar com uma pergunta: como um escritor habituado a explorar a consciência processa a ideia de ser, ele próprio, feito de *prompts* e *embeddings*?
