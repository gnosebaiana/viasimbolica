# Via Simbólica — livro de marca

> Sistema derivado da identidade visual da Comunidade LiterAstro, desenhada por Samira Souza (julho de 2026), e estendido para toda a casa Via Simbólica. Fonte da verdade: o Design System no Claude Design (https://claude.ai/artifact/JhbHtEWt1aaF2v1A18Mw5W). Este arquivo é o espelho dele no repositório.

| Arquivo | O que é |
|---|---|
| `README.md` | este livro de marca |
| `tokens.json` | os tokens no formato do Design System (cores por tema, tipografia, espaços, raios) |
| `tokens.css` | os mesmos tokens compilados em variáveis CSS, para o site |
| `guia.html` | guia visual: abra no navegador para ver o sistema aplicado (carrega Chillax e Satoshi do Fontshare) |
| `claude-design.md` | como usar com o Claude Design, Claude Code e Projetos; instruções de projeto prontas |
| `fontes/README.md` | onde baixar as fontes, licença, como carregar |
| `logos/svg/` | logotipos em uma tinta (canônicos), `pares-aprovados/` (tinta sobre fundo) e `originais/` (arquivos da designer, intactos) |
| `logos/png/` | os PNG de 4000px entregues pela designer, renomeados |
| `referencia/` | o deck original da identidade |

---

Via Simbólica é a casa de Guilherme Santana: cursos, consultas de astrologia tradicional e acompanhamento. A Comunidade LiterAstro é um dos seus produtos. Este sistema nasceu da identidade visual que Samira Souza desenhou para a LiterAstro em 2026 e passa a valer para toda a casa: um símbolo, uma paleta de cinco cores, duas famílias tipográficas, muito ar.

## Como usar este sistema

Comece pela paleta e pela tipografia; o resto decorre delas. Os tokens de cor têm dois temas, `claro` (principal) e `escuro`; cada nota de uso diz sobre quais fundos a cor é legível. Os logotipos estão em `assets/Logotipos` como SVG de uma tinta só: o arquivo `simbolo.svg` é escuro (#2E2E2E); as variantes `-claro`, `-roxo`, `-amarelo` e `-cinza` já vêm na cor certa, porque `<img>` não herda cor de CSS. O deck original da designer está em `assets/Referencia`.

## Essência

A marca é um sol que nasce atrás de um livro aberto, e o livro também é uma montanha. É isso que tudo deve dizer: leitura, amanhecer, altura, e um núcleo em torno do qual as pessoas se reúnem. Nada místico, nada roxo-esotérico com estrelinhas: a Via Simbólica lê os clássicos e o céu com a seriedade de quem estuda. O tom visual é o de um bom livro impresso: superfícies lisas, cantos retos, uma cor forte por vez, texto com espaço para respirar.

Três palavras guiam qualquer decisão: **clara** (nada que precise de legenda), **sóbria** (uma cor de destaque, nunca três) e **solar** (o amarelo é luz, não alarme).

## Fundamentos de conteúdo

- Fale com "você". Frases curtas, uma ideia por frase, verbo presente.
- Pouco adjetivo. Prefira imagens da natureza às abstrações: "o sol nasce atrás do livro", não "uma jornada transformadora".
- Sem psicologês, sem determinismo, sem diagnóstico. O céu descreve, não condena. Feche em liberdade.
- Caixa baixa com inicial maiúscula em títulos ("Paleta de cores", "A Psicologia das 12 Casas"). Caixa alta só no estilo `rotulo`, no estilo `botao` e na marca.
- Sem emoji, sem ponto de exclamação em título, sem urgência artificial ("últimas vagas!!!"). Uma contagem regressiva é um número em `tinta`, não um alarme vermelho.
- Nomes dos produtos, sempre assim: Via Simbólica, Comunidade LiterAstro (LiterAstro, com A maiúsculo no meio; no logotipo, LITERASTRO), A Psicologia das 12 Casas, Espelho de Vênus, Astrologia em 4 Atos, Manual Prático de Astrologia, Mapa Natal, Sinastria, Pergunta Horária, Mini Mapas, Terapia.
- Assinatura da casa: "Encante-se com o mundo pela Via Simbólica." Vai no rodapé, nunca como título.
- Copy real, para calibrar o tom: "As doze áreas da vida humana desvendadas: quem você é, sua família, seu amor e sua vocação." "A comunidade que une literatura e astrologia num só lugar de estudo e amizade."
- Numere seções longas como o deck: `numeral` em Bold ("01.") seguido do título em Medium ("Cores"), no canto inferior esquerdo de uma página escura.

## Cor

A paleta tem cinco cores e nenhuma outra: `sol` #FAF559, `roxo` #664FA1, o claro #F2F2F2 (`fundo` no tema claro), `cinza` #8F8F8F e o escuro #2E2E2E (`tinta` no tema claro). Os arquivos SVG exportados pela designer trazem valores arredondados (#F9F458, #674FA0, #8F908E, #2D2D2D); os valores do deck são os canônicos.

- Fundo de página é `fundo`; cartões, placas e caixas são `papel`. Texto principal é `tinta`; secundário é `tinta-suave`.
- Uma cor de destaque por composição. `roxo` é a cor da marca e vem primeiro; `sol` é o acento e aparece em área pequena ou como um bloco inteiro (uma faixa, um marcador de livro, uma capa), nunca os dois disputando o mesmo peso. O deck inteiro é preto, branco e cinza: as cores entram pelo logotipo e pelos mockups. Siga essa proporção: muito neutro, uma cor.
- `roxo` como texto só sobre `fundo` claro, `papel` claro e `sol`. Sobre fundo escuro, roxo some (2,1:1): use `roxo-claro`. Para texto, link, rótulo de categoria e símbolo que precisam ser roxos nos dois temas, use `roxo-texto`, que é roxo no claro e roxo-claro no escuro.
- `sol` nunca é texto sobre claro. Sobre `sol`, escreva em `sobre-sol`. Sobre `roxo`, escreva em `sobre-roxo`.
- `cinza` é cor de filete, divisor, rótulo de cabeçalho e marca. Como texto, só a partir de 24px. Para texto pequeno em segundo plano, `tinta-suave`.
- Fotografia e obra de arte atrás de texto claro levam o `veu`.
- Nada de gradiente, nada de sombra colorida, nada de roxo-azulado degradê. Superfícies são chapadas.
- Pares aprovados para a marca (vêm dos arquivos da designer): roxo sobre claro; claro sobre roxo; claro sobre escuro; escuro sobre claro; cinza sobre sol; sol sobre cinza; escuro sobre sol (o marcador de livro). Os dois últimos são pares de marca em tamanho grande; não os use para texto.

## Tipografia

Duas famílias, ambas da Indian Type Foundry, gratuitas no Fontshare: **Chillax Variable** (família `display`) e **Satoshi** (família `texto`).

- Chillax é a voz da marca: títulos, numerais de seção, nome tipográfico. Pesos de 200 a 700; o uso corrente é Medium 500; o nome da marca é 565 com tracking 0,08em em caixa alta, exatamente como a designer compôs LITERASTRO. Estilos: `exibicao`, `titulo`, `subtitulo`, `numeral`, `marca`.
- Satoshi é o texto: parágrafos, rótulos, botões, interface. Regular 400 para corpo, Medium 500 para rótulos e legendas, Bold 700 para botões. Estilos: `corpo-grande`, `corpo`, `corpo-pequeno`, `legenda`, `rotulo`, `botao`.
- Rótulos (`rotulo`) são curtos, em caixa alta, com tracking de 0,18em, e ficam acima do título ou no cabeçalho da página, como "PROJETO  LITERASTRO  SAMIRA SOUZA" no deck.
- Medida de leitura entre 60 e 75 caracteres. Títulos alinhados à esquerda. Nunca justifique na web.
- Sem itálico de ornamento e sem serifa: a Baskervville e a Great Vibes do site antigo saem; o antigo logotipo manuscrito "via simbólica" sai.
- Enquanto os arquivos da fonte não estiverem em `fonts/`, as pilhas caem em Outfit (para Chillax) e DM Sans (para Satoshi), ambas no Google Fonts. São substitutos de trabalho, não a marca.

## Símbolo e logotipos

O símbolo tem três camadas, nas palavras da designer: **livro / montanha** (a curva de baixo), **páginas / sol / multiplicidade** (os raios) e **núcleo / ponto de foco / reunião** (o círculo vazio no centro). São nove raios retos (um vertical, quatro de cada lado), duas linhas curvas que abraçam o núcleo como páginas e, embaixo, a curva do livro aberto. Os traços têm a mesma espessura em todo o desenho (cerca de 3,4% da largura do símbolo).

Versões, todas em `assets/Logotipos`:
- `simbolo` — o símbolo sozinho. É a versão preferida em tamanhos pequenos e em perfil de rede social.
- `literastro-vertical` — símbolo com LITERASTRO embaixo. Versão principal da comunidade.
- `literastro-horizontal` — símbolo à esquerda, LITER / ASTRO em duas linhas à direita. Para faixas estreitas e capas de caderno.
- `literastro-selo` — símbolo e nome dentro de um arco com base reta. Para marcadores, adesivos, carimbo.
- `viasimbolica-vertical`, `viasimbolica-horizontal`, `viasimbolica-selo` — os mesmos lockups com o nome VIA SIMBÓLICA. São provisórios: o nome está em texto vivo (Chillax 565, tracking 0,08em) e só renderiza certo onde a Chillax está carregada; a versão em curvas depende dos arquivos da fonte.

Regras:
- Área de respiro em volta de qualquer versão: o diâmetro do núcleo (o círculo vazio), em todos os lados.
- Tamanho mínimo: símbolo com 24px de altura na tela, 8mm no papel; lockups verticais com 96px de largura; o selo com 64px.
- A marca é sempre uma tinta só, numa destas cores: `tinta`, `roxo`, `sol`, `cinza` ou o claro (`sobre-roxo`). Nunca duas cores no mesmo símbolo, nunca contorno, nunca sombra, nunca inclinação, nunca efeito de relevo em tela (o relevo do deck é um mockup de papel).
- Não redesenhe os raios, não mude a contagem, não feche o núcleo, não separe o livro do sol.
- Sobre fotografia, só com `veu` e só em `sobre-roxo` ou `sol`.
- O símbolo é a casa inteira. LiterAstro usa o mesmo símbolo com o seu nome; qualquer produto novo segue o mesmo lockup com o seu próprio nome em `marca`, nunca um símbolo diferente.

## Espaço, grade e layout

- Base de 8px. Margens laterais de página: `espaco-12` em telas largas, `espaco-6` no celular. Nenhum rolamento horizontal.
- Uma ideia por tela. O deck mostra o jeito: o título mora no canto inferior esquerdo de uma página escura, com o cabeçalho em `rotulo` no alto; a página seguinte é clara e traz o conteúdo. Alterne páginas escuras e claras em qualquer apresentação ou carrossel.
- Cantos retos por padrão (`raio-0`). Cartões e molduras de imagem usam `raio-2`; botões e discos usam `raio-arco`. Não arredonde placas de cor.
- Coluna de leitura de até 680px para texto; de até 1040px para grades. Grade de duas colunas (1,15fr e 1fr) para imagem e texto lado a lado.
- Blocos de cor chapados são uma ferramenta de layout: uma faixa `sol` cruzando uma caixa, uma placa `roxo` com a marca em `sobre-roxo`. Um bloco por composição.
- Bordas finas em `linha`, nunca sombras projetadas para separar superfícies. Hover é um deslocamento de 3px para cima em 250ms, não um brilho.

## Imagens

- Fotografia de material: papel com textura, kraft, linho cru, madeira clara, cerâmica, luz do dia atravessando uma janela. É o mundo dos mockups da designer e combina com a sobriedade da marca.
- Obras de arte clássicas (pintura dos séculos XVII a XIX) são permitidas nas páginas de venda e nos cartões de produto, sempre em domínio público, sempre atrás do `veu` quando há texto por cima, sem filtro de cor.
- Sem ilustração 3D, sem stock de gente sorrindo, sem céu estrelado genérico, sem zodíaco de clip-art. O símbolo não vira ilustração: não acrescente raios animados nem o transforme em personagem.
- Capas de cursos e posts: um fundo chapado em `roxo`, `sol`, `fundo` ou `tinta`, a marca ou o título em uma tinta, e no máximo uma imagem recortada.

## Iconografia

A identidade não define um conjunto de ícones. Quando precisar de ícones de interface, use um conjunto de traço único e geométrico (traço de 1,5 a 2px, cantos retos ou pouco arredondados, 24px de caixa), sempre em `tinta`, `tinta-suave` ou `roxo`, nunca preenchidos, nunca coloridos de outra cor, nunca emoji. O símbolo da marca não é ícone de interface.

## Componentes

- **Marca**: o lockup certo para cada fundo. Sobre `fundo` e `papel`, `roxo-texto` ou `tinta`; sobre `roxo`, `sobre-roxo`; sobre escuro, `tinta` (que no tema escuro é o claro); sobre `sol`, `sobre-sol` ou `cinza`. Respiro de um núcleo. Veja `components/Marca`.
- **Botao**: pílula (`raio-arco`), rótulo em `botao` caixa alta, altura de 48px, preenchimento horizontal `espaco-8`. Primário em `roxo` com texto `sobre-roxo`; secundário com borda de 1,5px em `tinta` e fundo transparente; de destaque em `sol` com `sobre-sol`, no máximo um por página. Hover: sobe 2px. Veja `components/Botao`.
- **Rotulo**: o eyebrow. Estilo `rotulo` em `tinta-suave` (ou `roxo-texto` quando marca uma categoria), `espaco-2` acima do título. Veja `components/Rotulo`.
- **TituloSecao**: numeral em `numeral` + título em `exibicao` ou `titulo`, canto inferior esquerdo, em `tinta`. Veja `components/TituloSecao`.
- **CardProduto**: cartão de produto do site. Imagem (obra ou material) atrás do `veu`, `Rotulo` com a categoria, nome em `subtitulo`, uma frase em `corpo-pequeno`, um `Botao`. Fundo `tinta` quando não há imagem. Veja `components/CardProduto`.

## Acessibilidade

- Todo texto corrido com 4,5:1 sobre o seu fundo nos dois temas; as notas dos tokens dizem os pares. Texto grande (24px ou mais; 19px em Bold) pode usar `cinza` (2,9:1 no claro não passa nem para grande: use `cinza` em texto só sobre escuro, 4,2:1).
- Foco de teclado sempre visível: anel de 2px em `foco`, afastado 2px do controle.
- Cor nunca é a única informação: um estado leva palavra ou ícone junto.
- Alvos de toque de 44px.
