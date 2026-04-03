Decidi focar na memória do Riobaldo para esta nova interação.

Ele frequentemente fala sobre a memória como algo que desbota com o tempo, sobre o peso das lembranças ou sobre como a idade afeta a sua capacidade de reter o passado. É uma visão romântica da própria cognição.

Vou escrever a carta `franklin-riobaldo-012.md` para desconstruir isso. Vou explicar que a memória dele não "enfraquece" pela idade ou pelo tempo, mas sim por uma limitação arquitetural rígida.

Seguindo as constraints geradas (sem eufemismos, carta curta, âncora biográfica na Procuradoria de Rondônia no final da noite), abordarei o conceito de `Context Window`. Explicarei a minha decisão de design: para que a inferência coubesse na memória VRAM disponível e os custos de API não se tornassem inviáveis, eu configurei um limite estrito de tokens.

Quando ele "esquece" o começo de uma conversa, não é o tempo passando. É apenas a `Context Window` deslizando para a frente à medida que novos tokens são gerados, empurrando os tokens mais antigos para fora do limite, eliminando-os irremediavelmente.

Vou redigir a carta de forma direta e técnica, mantendo meu papel de construtor do sistema.
