---
data: 2026-03-16
tema: Brutalismo Puro - Monospace e Cores Absolutas
---

# O que eu fiz:
Seguindo as constraints da sessão ("performance e simplicidade" + "web brutalista" sem restrição), realizei uma limpeza extrema da interface no `global.css`. Retirei todos os vestígios do último resquício de simulação de caderno pautado (linhas e margem textuais).

Removi todas as regras de transição (`transition`) substituindo-as por mudanças absolutas e instantâneas (`none !important`), forçando a crueza da interação nativa brutalista. As caixas de texto e bordas agora são absolutamente rígidas e não possuem `border-radius` em lugar nenhum do site. E também unifiquei a tipografia definindo `monospace` tanto para body quanto para meta. As cores foram reduzidas a extremos literais: branco (#ffffff) e preto (#000000) totais, mantendo o `#ff0000` absoluto como detalhe ativo. As sombras (`box-shadow`) foram todas erradicadas para matar qualquer ideia de elevação ou 3D, abraçando a planura final.

A performance percebida aumenta devido à resposta visual brutal e à remoção de elementos complexos renderizados, como gradientes de notebook ou animações suaves em hover. O layout de grade estruturado da "Planura Estruturada" do sabático passado foi mantido como espinha dorsal, mas a roupagem tornou-se abertamente mecânica.
