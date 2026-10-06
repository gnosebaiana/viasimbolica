# Migrar o site para a identidade Via Simbólica

As quatro páginas (`index.html`, `venus/`, `12casas/`, `literastro/`) estão na identidade antiga: dourado, marfim, Baskervville, Great Vibes como fonte de título e o logotipo manuscrito como marca única. O caminho recomendado tem quatro passos, um por sessão de trabalho, cada um com captura de tela para aprovação antes do commit.

## 0. Decisões que só você toma (antes de começar)

1. **As obras de arte nos cartões ficam?** O livro de marca permite pintura clássica em domínio público atrás do véu. Se ficam, trocamos só a moldura e a tipografia; se saem, os cartões viram blocos de cor com a marca principal.
2. **Página inicial clara ou escura?** A identidade prevê os dois temas. Sugestão: inicial clara (fundo #F2F2F2), páginas de venda alternando seções escuras e claras como o deck.
3. **LiterAstro mantém o símbolo dela na página da comunidade** e a casa aparece pela assinatura no rodapé. Confirme.

## 1. Fundação compartilhada (uma sessão)

- Criar `assets/site.css` com `identidade/tokens.css` embutido no topo e os componentes do livro de marca (Botao, Rotulo, TituloSecao, CardProduto, Marca, faixa de destaque) escritos uma vez.
- Fontes pelo CSS hospedado do Fontshare, Outfit e DM Sans do Google Fonts como reserva. Nenhum arquivo de fonte no repositório.
- Favicon e ícones de app a partir de `logos/png/viasimbolica/favicon/`; `<meta name="theme-color">` em roxo.
- Marca principal completa no cabeçalho, assinatura no rodapé com a frase "Encante-se com o mundo pela Via Simbólica."

## 2. Página inicial (uma sessão)

- Trocar o cabeçalho manuscrito pela marca principal; cartões de produto no componente CardProduto; botões em pílula roxa; rede social em três blocos chapados nas cores da paleta (roxo, sol com texto escuro, escuro com texto claro) em vez das cores de terceiros.
- Manter todos os links, textos e o destaque com contagem regressiva (em `tinta`, sem vermelho).

## 3. Páginas de venda (uma sessão cada: Vênus, 12 Casas)

- Estrutura do deck: seção escura com título numerado no canto inferior esquerdo, seção clara com o conteúdo; alternar.
- Baskervville sai; títulos em Chillax Medium, texto em Satoshi. Itálicos de ênfase viram peso ou cor (`roxo-texto`), nunca outra fonte.
- Obras de arte com `veu` quando há texto por cima; molduras com `raio-2`, bordas em `linha`, sem sombra.

## 4. Comunidade LiterAstro (uma sessão)

- Mesmo sistema; o símbolo da LiterAstro no topo e nos cartões da biblioteca; assinatura da casa no rodapé.
- Pares aprovados para a marca: roxo sobre claro, claro sobre roxo, claro sobre escuro.

## Como pedir

Uma página por vez, nesta ordem, com uma frase: "migra a página inicial para a identidade nova, obras ficam, tema claro". Eu devolvo capturas em desktop e celular antes de publicar. Cada página migrada entra num commit próprio para você poder voltar atrás.

## Se preferir desenhar antes de programar

Abra o Claude Design com o Design System "Via Simbólica" anexado e peça "mockup da página inicial do site com os cinco cartões de produto". Aprove o layout lá e me passe o link do projeto; eu implemento o que foi aprovado. Esse caminho vale a pena se você quer experimentar duas ou três composições antes de decidir; se a dúvida é só "troca o visual pelo novo", vá direto pelo passo 1.
