# Como usar esta identidade com o Claude

## O que já está pronto

O Design System do Via Simbólica está publicado no Claude Design, dentro da sua conta, como um artefato do tipo "Design System":

**https://claude.ai/artifact/JhbHtEWt1aaF2v1A18Mw5W**

Ele contém o livro de marca (README), os tokens (cores nos temas claro e escuro, tipografia com os arquivos reais de Chillax e Satoshi, espaços, raios), as duas marcas da Via Simbólica em todas as versões, o símbolo da LiterAstro, os pares de cor aprovados, o deck original da designer e cinco componentes com pré-visualização (Marca, Botao, Rotulo, TituloSecao, CardProduto). Não existe "agente" a criar no Claude Design: o mecanismo é anexar esse Design System aos projetos. Faça assim:

1. Abra o Claude Design (claude.ai/design).
2. Em **Design systems**, marque "Via Simbólica" como padrão (ou anexe-o a cada projeto novo).
3. Todo projeto novo passa a usar as cores, as fontes, os logotipos e as regras do README.

Para uma peça nova, peça em uma frase o que é, para quem e onde vai ser vista ("post quadrado para o Instagram anunciando a abertura da turma 1 das 12 Casas, fundo roxo, marca principal da Via Simbólica em claro"). O sistema já responde ao resto.

## Qual ferramenta para cada coisa

| Quando você quer... | Use | Por quê |
|---|---|---|
| Uma peça visual: post, carrossel, capa de curso, banner, slide, mockup de página, convite | **Claude Design** com este Design System anexado | Canvas, comentários na peça, ajustes por slider e exportação. É o lugar do design visual. |
| Qualquer coisa que vira código: o site (GitHub Pages), páginas de venda, e-mail HTML, gerar dezenas de variações de um asset, converter logotipos em curvas, manter a identidade versionada | **Claude Code** (esta sessão, neste repositório) | Mexe nos arquivos, roda ferramentas (Chromium, Python), faz commit. A pasta `identidade/` é a fonte da verdade e o site deve consumir `tokens.css`. |
| Texto, nomes, briefs, roteiro de vídeo, revisão de copy no tom da marca, dúvidas rápidas | **Projeto normal no claude.ai** com `identidade/README.md` nas instruções ou no conhecimento do projeto | Não precisa de canvas nem de código; precisa de memória do tom e das regras. |

Regra prática: o Design System vive em um lugar só (o artefato) e o repositório é o espelho dele. Quando mudar uma regra, mude nos dois ou me peça que eu sincronize.

## Instruções de projeto (cole no Projeto do claude.ai ou no campo de instruções do Claude Design)

```
Você é o designer e redator da Via Simbólica (astrologia tradicional, cursos, consultas e a Comunidade LiterAstro), de Guilherme Santana. Siga o Design System "Via Simbólica" (https://claude.ai/artifact/JhbHtEWt1aaF2v1A18Mw5W) e o livro de marca identidade/README.md.

Identidade em uma linha: a casa olha e ilumina. Um Sol que também é um olho (marca principal) e uma estrela cadente que assina (assinatura). Clara, sóbria, solar. O sol atrás do livro aberto é só da LiterAstro.

Cor: cinco cores e nenhuma outra. Roxo #664FA1 é a cor da marca; sol #FAF559 é o acento; claro #F2F2F2, cinza #8F8F8F e escuro #2E2E2E são os neutros; fundos de página escuros usam #191919. Uma cor de destaque por composição. Sol nunca é texto sobre claro. Roxo nunca é texto sobre escuro (use #B9A9E0). Nada de gradiente, sombra colorida ou brilho.

Tipografia: Chillax Variable (títulos, numerais de seção, nome VIA SIMBÓLICA em peso 565, caixa alta, tracking 0,08em) e Satoshi (texto, rótulos em caixa alta com tracking 0,18em, botões). Great Vibes só dentro da assinatura, nunca como fonte de texto. Títulos em caixa baixa com inicial maiúscula. Alinhamento à esquerda.

Marcas: a Via Simbólica tem duas. A principal é um cartão roxo 2:3 com nove raios e um disco claros recortados pela borda (o Sol que também é um olho): não se redesenha, não se gira, não se arredonda; use os arquivos viasimbolica-principal-*. A assinatura é a estrela cadente com "via simbólica" manuscrito em Great Vibes: fecha a peça, de 120 a 320px de largura, uma tinta só. O símbolo do livro-sol-montanha é da LiterAstro e só aparece em peças da comunidade. Pares aprovados, sete: roxo sobre claro, claro sobre roxo, claro sobre escuro, escuro sobre claro, escuro sobre sol, cinza sobre sol, sol sobre cinza.

Layout: cantos retos, muito ar, uma ideia por tela, títulos no canto inferior esquerdo de páginas escuras alternando com páginas claras, grade de 8px, blocos de cor chapados como ferramenta.

Imagens: materiais naturais e luz do dia (papel, kraft, linho, madeira) ou pintura clássica em domínio público atrás de um véu escuro a 60%. Sem 3D, sem stock, sem zodíaco de clip-art, sem emoji.

Texto: "você", frases curtas, pouco adjetivo, imagens da natureza, sem psicologês e sem determinismo; fechar na liberdade. Assinatura: "Encante-se com o mundo pela Via Simbólica."

Antes de entregar, confira: uma só cor de destaque? Contraste de texto acima de 4,5:1? Símbolo intacto e em uma tinta? Fonte certa? Respiro?
```

## O que falta para fechar (depende de você)

1. **O site.** As quatro páginas atuais (`index.html`, `venus/`, `12casas/`, `literastro/`) ainda estão na identidade antiga (dourado, marfim, Baskervville). Por decisão sua, ficam assim até a identidade estar batida. Quando quiser, migro todas para `tokens.css`, para as duas marcas da Via Simbólica e para o símbolo da LiterAstro na página da comunidade.
2. **Impressão.** Para gráfica, peça a versão em CMYK e com sangria de qualquer peça; os valores da paleta são RGB de tela e precisam de prova.

## Decisões já tomadas

- A LiterAstro fica com o símbolo que a designer desenhou; a Via Simbólica herda paleta, tipografia e modo de compor, mas usa marcas próprias: a principal (o Sol-olho, geometria exata da capa do Design System, sem alteração) e a assinatura (a estrela cadente com o nome manuscrito, como estava no site).
- As fontes Chillax e Satoshi estão registradas no Design System (arquivos em `fonts/`, uso privado). Não ficam no repositório público por causa da licença do Fontshare; o `guia.html` as carrega pelo CSS do Fontshare, e o site passará a carregá-las assim quando for migrado.
- Os nomes nos lockups estão em curvas: VIA SIMBÓLICA em Chillax 565, "via simbólica" em Great Vibes e LITER / ASTRO no horizontal canônico da LiterAstro. Nenhum arquivo canônico depende de fonte instalada; só o `literastro-horizontal.svg` original da designer, guardado em `originais/`, tem texto vivo.
