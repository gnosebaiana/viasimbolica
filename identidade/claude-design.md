# Como usar esta identidade com o Claude

## O que já está pronto

O Design System do Via Simbólica está publicado no Claude Design, dentro da sua conta, como um artefato do tipo "Design System":

**https://claude.ai/artifact/JhbHtEWt1aaF2v1A18Mw5W**

Ele contém o livro de marca (README), os tokens (cores nos temas claro e escuro, tipografia, espaços, raios), os logotipos e os pares de cor aprovados, o deck original da designer e cinco componentes com pré-visualização (Marca, Botao, Rotulo, TituloSecao, CardProduto). Não existe "agente" a criar no Claude Design: o mecanismo é anexar esse Design System aos projetos. Faça assim:

1. Abra o Claude Design (claude.ai/design).
2. Em **Design systems**, marque "Via Simbólica" como padrão (ou anexe-o a cada projeto novo).
3. Todo projeto novo passa a usar as cores, as fontes, os logotipos e as regras do README.

Para uma peça nova, peça em uma frase o que é, para quem e onde vai ser vista ("post quadrado para o Instagram anunciando a abertura da turma 1 das 12 Casas, fundo roxo, símbolo em claro"). O sistema já responde ao resto.

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

Identidade em uma linha: um sol que nasce atrás de um livro aberto, que também é montanha. Clara, sóbria, solar.

Cor: cinco cores e nenhuma outra. Roxo #664FA1 é a cor da marca; sol #FAF559 é o acento; claro #F2F2F2, cinza #8F8F8F e escuro #2E2E2E são os neutros; fundos de página escuros usam #191919. Uma cor de destaque por composição. Sol nunca é texto sobre claro. Roxo nunca é texto sobre escuro (use #B9A9E0). Nada de gradiente, sombra colorida ou brilho.

Tipografia: Chillax Variable (títulos, numerais de seção, marca em peso 565, caixa alta, tracking 0,08em) e Satoshi (texto, rótulos em caixa alta com tracking 0,18em, botões). Títulos em caixa baixa com inicial maiúscula. Alinhamento à esquerda.

Marca: o símbolo é uma tinta só, nunca duas cores, nunca contorno, nunca redesenhado. Respiro de um núcleo em volta. Sobre claro, roxo ou escuro; sobre roxo, claro; sobre sol, escuro ou cinza (só a marca). LiterAstro e qualquer produto usam o mesmo símbolo com o seu nome.

Layout: cantos retos, muito ar, uma ideia por tela, títulos no canto inferior esquerdo de páginas escuras alternando com páginas claras, grade de 8px, blocos de cor chapados como ferramenta.

Imagens: materiais naturais e luz do dia (papel, kraft, linho, madeira) ou pintura clássica em domínio público atrás de um véu escuro a 60%. Sem 3D, sem stock, sem zodíaco de clip-art, sem emoji.

Texto: "você", frases curtas, pouco adjetivo, imagens da natureza, sem psicologês e sem determinismo; fechar na liberdade. Assinatura: "Encante-se com o mundo pela Via Simbólica."

Antes de entregar, confira: uma só cor de destaque? Contraste de texto acima de 4,5:1? Símbolo intacto e em uma tinta? Fonte certa? Respiro?
```

## O que falta para fechar (depende de você)

1. **Fontes.** Baixe Chillax e Satoshi no Fontshare (gratuitas) e me mande os arquivos `.woff2`/`.ttf`, ou arraste-os para a página do Design System. Com eles eu (a) registro as fontes no sistema para as pré-visualizações ficarem fiéis e (b) converto em curvas os lockups "Via Simbólica", que hoje estão em texto vivo. Veja `fontes/README.md`.
2. **Decisão de marca.** Assumi que o símbolo da LiterAstro passa a ser o símbolo da casa inteira, e que cada produto usa o mesmo símbolo com o seu nome. Se preferir um símbolo próprio para a Via Simbólica e a LiterAstro como submarca, eu reorganizo.
3. **O site.** As quatro páginas atuais (`index.html`, `venus/`, `12casas/`, `literastro/`) ainda estão na identidade antiga (dourado, marfim, Baskervville, Great Vibes). O próximo passo natural é migrá-las para `tokens.css` e para os logotipos novos; peça quando quiser que eu faça.
