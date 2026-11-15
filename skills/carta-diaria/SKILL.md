---
name: carta-diaria
description: Gera o PDF da carta diária da Via Simbólica (as "Correspondências" que o Guiga manda por e-mail) no desenho fixado, com papel, estrela cadente e o Sol e a Lua do dia calculados. Use sempre que o Guiga pedir o PDF de uma carta, falar em "carta nº", "gera a carta de hoje", "a carta tá pronta no Notion", Casa 6, correspondências, ou quiser a versão em PDF que vai anexada ao e-mail, mesmo que ele não diga "PDF" nem "skill". Também serve para refazer uma carta já gerada (outra data, título corrigido, texto revisto).
---

# Carta diária

A carta é o texto que o Guiga escreve todo dia e envia por e-mail aos leitores, sempre com uma versão em PDF anexada. O PDF é a carta como foi desenhada: papel, as letras da marca, o céu do dia em que foi escrita. O desenho já foi aprovado; o seu trabalho é aplicar, não redesenhar.

## Fluxo

1. **Achar a carta.** Ela fica no Notion, na página "Casa 6: rotina e organização", com o título "Carta nº N - Título". Busque por "Carta nº N" e abra a página principal; ignore subpáginas como "versão anterior". Se o Guiga colar o texto na conversa, use o texto colado.

2. **Separar as partes.**
   - Número e título: vêm do nome da página ("Carta nº 1 - Por que falar em cartas" → número 1, título "Por que falar em cartas").
   - Corpo: os parágrafos, palavra por palavra. Não revise, não corte, não "melhore": a carta é dele. Só os itálicos do Notion viram `*assim*`.
   - Fecho: o que vem depois do último parágrafo ("Até amanhã," / "Guiga" / *Via Simbólica*). Passe em `--fecho`, linhas separadas por `|`. Se for igual ao padrão, não precisa passar.
   Salve o corpo num arquivo `.md`, um parágrafo por bloco, com linha em branco entre eles.

3. **Data e hora.** O céu do topo é o do dia em que a carta foi **escrita**. Se o Guiga disser "é de hoje", use a data de hoje. Se não souber a data, pergunte. A hora só importa quando a Lua muda de signo naquele dia: o script avisa (código de saída 2, mensagem "PERGUNTAR A HORA") e aí você pergunta ao Guiga a hora em que escreveu. Fuso padrão: Brasília (−3).

4. **Gerar.**
   ```bash
   python3 <skill>/scripts/gerar_carta.py --numero 1 --titulo "Por que falar em cartas" \
     --data 2026-11-15 --hora 15:00 --texto carta.md --saida <pasta>
   ```
   O script calcula Sol e Lua com efeméride (`ephem`, zodíaco tropical), escolhe os ícones, monta a página e gera `Carta nº N · Via Simbólica.pdf`. Ele instala `ephem` e `pypdf` se faltarem. Para desenhar o PDF precisa de Playwright com Chromium (pelo `node` ou pelo Python); se não houver, `pip install playwright && playwright install chromium`.

5. **Conferir.** Leia o resumo que o script imprime (páginas, tamanho, céu). Olhe a primeira e a última página renderizadas uma vez (`pdftoppm -r 60 -png`). O que conferir: o topo (título, estrela, ícones, data), e que a última página traz o fim do texto junto com o fecho, nunca o fecho sozinho (o modelo já prende o último parágrafo ao fecho).

6. **Entregar.** Mande o PDF ao Guiga e diga em uma linha o céu usado ("Sol em Escorpião, Lua em Aquário, 15/11/2026"). Se a data ou a hora foram suposição sua, diga.

## O desenho fixado

Estas decisões foram tomadas com o Guiga. Não mude nenhuma sem ele pedir.

- **Formato:** A5 retrato (148 × 210 mm), papel branco quente (#f6f3ee) com textura leve até a borda.
- **Letras:** Chillax só no título; Satoshi no resto (corpo 9,6 pt, entrelinha 1,56). As fontes vão embutidas no PDF.
- **Topo, à esquerda:** "CARTA Nº N" em versalete pequeno e o título em Chillax.
- **Topo, à direita:** a estrela cadente da logo, em roxo (#664fa1), **sem fundo**; embaixo, o ícone do Sol ao lado do signo dele e o da Lua ao lado do signo dela; embaixo, a data em algarismos: `15 · 11 · 2026`.
- **Texto:** justificado, **todo parágrafo com recuo** (6 mm), sem espaço entre parágrafos.
- **Fecho:** "Até amanhã," / "Guiga" / *Via Simbólica*, na mesma letra do corpo, em linhas seguidas; uma estrela cadente pequena em roxo embaixo. Sempre na mesma página do último parágrafo.
- **Rodapé:** "CARTA Nº N · VIA SIMBÓLICA" e o número da página.
- **Tamanho:** abaixo de 1 MB, para anexar ao e-mail.

O que o Guiga recusou e não deve voltar: selo roxo com borda picotada, "Escorpião · água fixa" ou qualquer descrição do signo por extenso, a logo do olho/sol, assinatura cursiva ou "à mão", data em algarismos romanos, a última página só com o fecho, as iluminuras das Très Riches Heures.

## Por que o céu sai do script

A posição do Sol e da Lua nunca é estimada de cabeça: um signo errado no topo da carta é um erro público, e a Lua troca de signo a cada dois dias e meio. Por isso o cálculo fica no script, e por isso ele para quando a Lua muda de signo no dia e a hora não foi dada.

## Arquivos

- `scripts/gerar_carta.py`: gera o PDF (cálculo do céu, montagem, junção com o papel, resumo).
- `scripts/glifos.py`: os ícones em traço do Sol, da Lua e dos 12 signos.
- `scripts/render.js`: desenha o PDF pelo Chromium (o Python usa o Playwright dele se o `node` não tiver).
- `assets/carta.html`: o modelo da página. `assets/fundo.html`: o papel. `assets/fontes/`: Chillax e Satoshi.
