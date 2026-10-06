# Via Simbólica — livro de marca

> Sistema derivado da identidade visual da Comunidade LiterAstro, desenhada por Samira Souza (julho de 2026), e estendido para toda a casa Via Simbólica, que usa marcas próprias. Fonte da verdade: o Design System no Claude Design (https://claude.ai/artifact/JhbHtEWt1aaF2v1A18Mw5W). Este arquivo é o espelho dele no repositório.

| Arquivo | O que é |
|---|---|
| `README.md` | este livro de marca |
| `tokens.json` | os tokens no formato do Design System (cores por tema, tipografia, espaços, raios) |
| `tokens.css` | os mesmos tokens compilados em variáveis CSS, para o site |
| `guia.html` | guia visual: abra no navegador para ver o sistema aplicado (carrega Chillax e Satoshi do Fontshare) |
| `claude-design.md` | como usar com o Claude Design, Claude Code e Projetos; instruções de projeto prontas; decisões tomadas |
| `fontes/README.md` | onde baixar as fontes, licença, como carregar |
| `logos/svg/viasimbolica/` | as duas marcas da Via Simbólica: principal (forma completa e seus pares, marcas soltas, miniatura e seus pares, avatar, lockups) e assinatura, nomes em curvas |
| `logos/svg/literastro/` | o símbolo da LiterAstro em uma tinta (canônico), `pares-aprovados/` e `originais/` (arquivos da designer, intactos) |
| `logos/png/viasimbolica/`, `logos/png/literastro/` | PNG de 4000px de cada marca, exportados dos SVG canônicos; `logos/png/literastro/originais/` guarda os PNG da designer (cores arredondadas, dois com 4001px) |
| `referencia/` | o deck original da identidade |
---

Via Simbólica é a casa de Guilherme Santana: cursos, consultas de astrologia tradicional e acompanhamento. A Comunidade LiterAstro é um dos seus produtos. Este sistema nasceu da identidade visual que Samira Souza desenhou para a LiterAstro em 2026 e passa a valer para toda a casa: a mesma paleta de cinco cores, as mesmas duas famílias tipográficas, o mesmo jeito de compor com muito ar. As marcas, não: a Via Simbólica tem as suas, a **principal** (o Sol que também é um olho) e a **assinatura** (a estrela cadente com o nome manuscrito). O símbolo do sol atrás do livro aberto é da LiterAstro e só aparece em peças da comunidade.

## Como usar este sistema

Comece pela paleta e pela tipografia; o resto decorre delas. Os tokens de cor têm dois temas, `claro` (principal) e `escuro`; cada nota de uso diz sobre quais fundos a cor é legível. As marcas estão em `assets/Marcas-Via-Simbolica` (as da casa) e em `assets/LiterAstro` (as da comunidade), como SVG de cores fixas (uma tinta só, ou tinta e cartão nos pares da principal), com uma variante por cor ou par, porque `<img>` não herda cor de CSS. Os pares de tinta e fundo aprovados pela designer estão em `assets/Pares-aprovados`. O deck original está em `assets/Referencia`. As fontes estão em `fonts/`.

## Essência

A casa olha e ilumina. A marca principal diz isso de uma vez: um Sol que também é um olho, nove raios iguais abrindo-se a partir de um disco claro sobre um cartão roxo; na miniatura, a borda do cartão os recorta. A assinatura diz o resto: uma estrela cadente e o nome escrito à mão, como quem assina uma carta. A LiterAstro tem a sua imagem própria: o sol que nasce atrás de um livro aberto, que também é montanha. Nada místico, nada roxo-esotérico com estrelinhas espalhadas: a Via Simbólica lê os clássicos e o céu com a seriedade de quem estuda. O tom visual é o de um bom livro impresso: superfícies lisas, cantos retos, uma cor forte por vez, texto com espaço para respirar.

Três palavras guiam qualquer decisão: **clara** (nada que precise de legenda), **sóbria** (uma cor de destaque, nunca três) e **solar** (o amarelo é luz, não alarme).

## Fundamentos de conteúdo

- Fale com "você". Frases curtas, uma ideia por frase, verbo presente.
- Pouco adjetivo. Prefira imagens da natureza às abstrações: "o sol nasce atrás do livro", não "uma jornada transformadora".
- Sem psicologês, sem determinismo, sem diagnóstico. O céu descreve, não condena. Feche em liberdade.
- Caixa baixa com inicial maiúscula em títulos ("Paleta de cores", "A Psicologia das 12 Casas"). Caixa alta só no estilo `rotulo`, no estilo `botao` e no nome VIA SIMBÓLICA dos lockups. A assinatura é toda em caixa baixa.
- Sem emoji, sem ponto de exclamação em título, sem urgência artificial ("últimas vagas!!!"). Uma contagem regressiva é um número em `tinta`, não um alarme vermelho.
- Nomes dos produtos, sempre assim: Via Simbólica, Comunidade LiterAstro (LiterAstro, com A maiúsculo no meio; no logotipo, LITERASTRO), A Psicologia das 12 Casas, Espelho de Vênus, Astrologia em 4 Atos, Manual Prático de Astrologia, Mapa Natal, Sinastria, Pergunta Horária, Mini Mapas, Terapia.
- Frase da casa: "Encante-se com o mundo pela Via Simbólica." Vai no rodapé, junto da assinatura, nunca como título.
- Copy real, para calibrar o tom: "As doze áreas da vida humana desvendadas: quem você é, sua família, seu amor e sua vocação." "A comunidade que une literatura e astrologia num só lugar de estudo e amizade."
- Numere seções longas como o deck: `numeral` em Bold ("01.") seguido do título em Medium ("Cores"), no canto inferior esquerdo de uma página escura.

## Cor

A paleta da designer tem cinco cores: `sol` #FAF559, `roxo` #664FA1, o claro #F2F2F2 (`fundo` no tema claro), `cinza` #8F8F8F e o escuro #2E2E2E (`tinta` no tema claro). O sistema acrescenta só neutros derivados para fundo, papel, filete e texto secundário (`fundo` escuro #191919 e `papel` claro #FFFFFF, que são os fundos do deck; `linha`; `tinta-suave`; `veu`) e `roxo-claro` #B9A9E0 para o roxo legível no escuro; nenhuma outra cor. Os arquivos SVG exportados pela designer trazem valores arredondados (#F9F458, #674FA0, #8F908E, #2D2D2D); os valores do deck são os canônicos.

- Fundo de página é `fundo`; cartões, placas e caixas são `papel`. Texto principal é `tinta`; secundário é `tinta-suave`.
- Uma cor de destaque por composição. `roxo` é a cor da marca e vem primeiro; `sol` é o acento e aparece em área pequena ou como um bloco inteiro (uma faixa, um marcador de livro, uma capa), nunca os dois disputando o mesmo peso. O deck inteiro é preto, branco e cinza: as cores entram pelo logotipo e pelos mockups. Siga essa proporção: muito neutro, uma cor.
- `roxo` como texto só sobre `fundo` claro, `papel` claro e `sol`. Sobre `fundo` e `papel` escuros, roxo some (2,7:1 e 2,1:1): use `roxo-claro`. Para texto, link, rótulo de categoria e marca que precisam ser roxos nos dois temas, use `roxo-texto`, que é roxo no claro e roxo-claro no escuro.
- `sol` nunca é texto sobre claro. Sobre `sol`, escreva em `sobre-sol`. Sobre `roxo`, escreva em `sobre-roxo`.
- `cinza` é cor de filete, divisor, rótulo de cabeçalho e marca. Como texto, só a partir de 24px. Para texto pequeno em segundo plano, `tinta-suave`.
- Fotografia e obra de arte atrás de texto claro levam o `veu`.
- Nada de gradiente, nada de sombra colorida, nada de roxo-azulado degradê. Superfícies são chapadas.
- Pares aprovados para qualquer marca, sete ao todo: roxo sobre claro; claro sobre roxo; claro sobre escuro; escuro sobre claro; cinza sobre sol; sol sobre cinza; escuro sobre sol. Os seis primeiros vêm dos arquivos da designer; escuro sobre sol vem do marcador de livro do deck. Os pares com cinza são pares de marca em tamanho grande; não os use para texto.

## Tipografia

Duas famílias para tudo, ambas da Indian Type Foundry, gratuitas no Fontshare, com os arquivos em `fonts/`: **Chillax Variable** (família `display`) e **Satoshi** (família `texto`). Uma terceira, **Great Vibes** (família `assinatura`), existe só dentro da marca secundária e nunca é fonte de texto.

- Chillax é a voz da marca: títulos, numerais de seção, o nome VIA SIMBÓLICA nos lockups. Pesos de 200 a 700; o uso corrente é Medium 500; o nome da marca é 565 com tracking 0,08em em caixa alta, exatamente como a designer compôs LITERASTRO. Estilos: `exibicao`, `titulo`, `subtitulo`, `numeral`, `marca`.
- Satoshi é o texto: parágrafos, rótulos, botões, interface. Regular 400 para corpo, Medium 500 para rótulos e legendas, Bold 700 para botões. Estilos: `corpo-grande`, `corpo`, `corpo-pequeno`, `legenda`, `rotulo`, `botao`.
- Great Vibes aparece uma única vez no sistema: no "via simbólica" manuscrito da assinatura, já convertido em curvas nos arquivos. Não a use em título, destaque ou citação.
- Rótulos (`rotulo`) são curtos, em caixa alta, com tracking de 0,18em, e ficam acima do título ou no cabeçalho da página, como "PROJETO  LITERASTRO  SAMIRA SOUZA" no deck.
- Medida de leitura entre 60 e 75 caracteres. Títulos alinhados à esquerda. Nunca justifique na web.
- Sem itálico de ornamento e sem serifa: a Baskervville do site antigo sai.

## Marcas

A casa tem duas marcas; a comunidade tem a sua. Nunca junte duas delas no mesmo bloco visual sem hierarquia: a principal manda, a assinatura fecha, a da LiterAstro aparece só em peças da LiterAstro.

### Marca principal: o Sol que também é um olho

A marca tem duas formas com a mesma geometria. Na **completa**, um cartão horizontal de 464×288 em `roxo` com, no claro da paleta (#F2F2F2, o `sobre-roxo`, igual nos dois temas), um disco de raio 32 assentado perto da base (centro a 56 da borda inferior) e nove raios inteiros, da mesma espessura (8) e do mesmo comprimento (112), saindo dele a 0, 22,5, 45, 67,5 e 90 graus para cada lado, entre os raios 64 e 176 do centro; o leque fica a 56 das bordas laterais e da superior, e embaixo o centro do disco fica a 56 da borda. É a forma de todo uso em que a marca aparece inteira: lockups, capas, cabeçalhos, impressos. Na **miniatura**, o mesmo leque num cartão vertical 2:3 (192×288) que recorta os raios laterais pela borda: é a forma do ícone, do favicon, do avatar e de qualquer tamanho pequeno, e o corte faz parte dela. O disco é a pupila e é o sol; os raios são cílios e luz. Nas duas formas o cartão não é fundo, é a marca: tem a cor dela e termina onde o desenho termina.

Versões, em `assets/Marcas-Via-Simbolica`:
- `viasimbolica-principal` — a versão mestre completa: cartão roxo, marcas claras. Use esta sempre que a marca aparecer inteira.
- `viasimbolica-principal-claro-sobre-escuro`, `-escuro-sobre-sol`, `-roxo-sobre-claro`, `-sol-sobre-cinza`, `-claro-sobre-fundo-escuro` — a completa nos pares aprovados; o nome diz "marcas-sobre-cartão".
- `viasimbolica-principal-marcas` (e `-claro`, `-roxo`, `-sol`) — só os raios e o disco da completa, para pousar sobre um campo chapado na proporção 464:288 (uma capa inteira em roxo, por exemplo). Nunca sobre fotografia ou campo de outra proporção.
- `viasimbolica-miniatura` (e os mesmos cinco pares) — a forma recortada 2:3, para ícone, favicon, avatar e tamanhos pequenos.
- `viasimbolica-avatar` (e `-escuro`) — a miniatura centrada num quadrado `fundo`, para perfis e favicon.
- `viasimbolica-vertical` (e `-claro`) — a completa com VIA SIMBÓLICA embaixo, nome em curvas (Chillax 565, tracking 0,08em), com a largura do cartão.
- `viasimbolica-horizontal` (e `-claro`) — a completa à esquerda, VIA / SIMBÓLICA em duas linhas à direita. Para faixas, cabeçalhos e capas de caderno.

Regras:
- Não altere nada da geometria: contagem, ângulos, espessura, comprimento, raio do disco, posição, proporção dos cartões, recorte da miniatura. Não arredonde os cantos. Não gire. Não use a miniatura onde a marca aparece inteira, nem a completa como ícone.
- Uma tinta para as marcas e uma para o cartão, sempre num par aprovado. Sem contorno, sombra, brilho ou relevo em tela.
- Respiro em volta do cartão: o diâmetro do disco (64 na escala do arquivo), em todos os lados. Nos lockups, o respiro é medido a partir do conjunto.
- Tamanho mínimo: completa com 160px de largura na tela, 40mm no papel; miniatura com 24px de altura; lockup vertical com 200px de largura; horizontal com 320px.
- Sobre fotografia, só com `veu` e só as versões com cartão, nunca as marcas soltas.

### Assinatura: a estrela cadente

A marca secundária é a que o site já usava: uma estrela de quatro pontas com duas trilhas finas atrás (a trilha de cima a 60% da tinta, a de baixo a 35%) e, embaixo, "via simbólica" escrito à mão em Great Vibes, caixa baixa, centrado sob a estrela. Nos arquivos o nome já está em curvas.

Versões: `viasimbolica-assinatura` (em `tinta`), `-claro`, `-roxo`, `-sol`.

Regras:
- É uma assinatura: fecha, não abre. Rodapé de página, fecho de vídeo, assinatura de e-mail, verso de material impresso, canto de uma peça que a marca principal já ocupa.
- Uma tinta só, num par aprovado. As transparências das trilhas fazem parte do desenho; não as chapadas.
- Largura entre 120px e 320px na tela. Maior que isso a letra manuscrita vira ilustração; menor, as trilhas somem.
- Nunca sobre fotografia sem `veu`. Nunca como fonte: o texto da assinatura não se reescreve com outras palavras.

### LiterAstro

A comunidade mantém o símbolo que a designer desenhou: **livro / montanha** (a curva de baixo), **páginas / sol / multiplicidade** (os raios) e **núcleo / ponto de foco / reunião** (o círculo vazio no centro). São nove raios retos, duas linhas curvas que abraçam o núcleo como páginas e, embaixo, a curva do livro aberto; traços de espessura única, cerca de 3,4% da largura. Versões em `assets/LiterAstro`: `literastro-vertical` (principal), `literastro-horizontal`, `literastro-selo` e o `simbolo` sozinho, cada um em cinco tintas. Respiro de um núcleo; símbolo com 24px de altura no mínimo; uma tinta só; não redesenhar. Em peça da LiterAstro, a casa aparece pela assinatura, pequena, no rodapé.

## Espaço, grade e layout

- Base de 8px. Margens laterais de página: `espaco-12` em telas largas, `espaco-6` no celular. Nenhum rolamento horizontal.
- Uma ideia por tela. O deck mostra o jeito: o título mora no canto inferior esquerdo de uma página escura, com o cabeçalho em `rotulo` no alto; a página seguinte é clara e traz o conteúdo. Alterne páginas escuras e claras em qualquer apresentação ou carrossel.
- Cantos retos por padrão (`raio-0`). Cartões e molduras de imagem usam `raio-2`; botões e discos usam `raio-arco`. Não arredonde placas de cor nem o cartão da marca.
- Coluna de leitura de até 680px para texto; de até 1040px para grades. Grade de duas colunas (1,15fr e 1fr) para imagem e texto lado a lado.
- Blocos de cor chapados são uma ferramenta de layout: uma faixa `sol` cruzando uma caixa, uma placa `roxo` com a marca em `sobre-roxo`. Um bloco por composição. A própria marca principal é um bloco: pode ancorar uma capa inteira.
- Bordas finas em `linha`, nunca sombras projetadas para separar superfícies. Hover é um deslocamento para cima em 250ms (3px em cartões, 2px em botões), não um brilho.

## Imagens

- Fotografia de material: papel com textura, kraft, linho cru, madeira clara, cerâmica, luz do dia atravessando uma janela. É o mundo dos mockups da designer e combina com a sobriedade da marca.
- Obras de arte clássicas (pintura dos séculos XVII a XIX) são permitidas nas páginas de venda e nos cartões de produto, sempre em domínio público, sempre atrás do `veu` quando há texto por cima, sem filtro de cor.
- Sem ilustração 3D, sem stock de gente sorrindo, sem céu estrelado genérico, sem zodíaco de clip-art. As marcas não viram ilustração: não anime os raios, não acrescente estrelas à assinatura.
- Capas de cursos e posts: um fundo chapado em `roxo`, `sol`, `fundo` ou `tinta`, a marca ou o título em uma tinta, e no máximo uma imagem recortada.

## Iconografia

A identidade não define um conjunto de ícones. Quando precisar de ícones de interface, use um conjunto de traço único e geométrico (traço de 1,5 a 2px, cantos retos ou pouco arredondados, 24px de caixa), sempre em `tinta`, `tinta-suave` ou `roxo-texto`, nunca preenchidos, nunca coloridos de outra cor, nunca emoji. As marcas não são ícones de interface.

## Componentes

- **Marca**: a principal e a assinatura, cada uma no par certo para o fundo. Sobre `fundo` e `papel`, a principal mestre e a assinatura em `tinta`; sobre `roxo`, a principal mestre (o cartão some no fundo e ficam as marcas) e a assinatura em `sobre-roxo`; sobre `sol`, a principal escuro-sobre-sol e a assinatura em `sobre-sol`. Veja `components/Marca`.
- **Botao**: pílula (`raio-arco`), rótulo em `botao` caixa alta, altura de 48px, preenchimento horizontal `espaco-8`. Primário em `roxo` com texto `sobre-roxo`; secundário com borda de 1,5px em `tinta` e fundo transparente; de destaque em `sol` com `sobre-sol`, no máximo um por página. Hover: sobe 2px. Veja `components/Botao`.
- **Rotulo**: o eyebrow. Estilo `rotulo` em `tinta-suave` (ou `roxo-texto` quando marca uma categoria), `espaco-2` acima do título. Veja `components/Rotulo`.
- **TituloSecao**: numeral em `numeral` + título em `exibicao` ou `titulo`, canto inferior esquerdo, em `tinta`. Veja `components/TituloSecao`.
- **CardProduto**: cartão de produto do site. Imagem (obra ou material) atrás do `veu`, `Rotulo` com a categoria, nome em `subtitulo`, uma frase em `corpo-pequeno`, um `Botao`. Sem imagem, a área da esquerda é um bloco `roxo` com a marca principal completa. Veja `components/CardProduto`.

## Acessibilidade

- Todo texto corrido com 4,5:1 sobre o seu fundo nos dois temas; as notas dos tokens dizem os pares. Texto grande (24px ou mais; 19px em Bold) pode usar `cinza` sobre `fundo` escuro (5,4:1) e `papel` escuro (4,2:1); sobre `fundo` claro ele não passa nem para texto grande (2,9:1) e sobre `papel` claro passa por pouco (3,2:1), só em texto grande.
- Foco de teclado sempre visível: anel de 2px em `foco`, afastado 2px do controle.
- Cor nunca é a única informação: um estado leva palavra ou ícone junto.
- Alvos de toque de 44px.
