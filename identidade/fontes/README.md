# Fontes da identidade

| Papel | Família | Pesos usados | Onde baixar |
|---|---|---|---|
| Display, títulos, marca | **Chillax Variable** (Indian Type Foundry) | 200 a 700; marca em 565 | https://www.fontshare.com/fonts/chillax |
| Texto corrido, rótulos, botões | **Satoshi** (Indian Type Foundry) | 400, 500, 700 | https://www.fontshare.com/fonts/satoshi |

As duas são gratuitas pela **ITF Free Font License** (uso pessoal e comercial, impresso e digital). A licença **não permite redistribuir os arquivos** (subir num servidor público, num repositório aberto, mandar por e-mail). Por isso os arquivos `.woff2` **não ficam neste repositório**: cada pessoa baixa do Fontshare.

## Na web (site, páginas de venda, e-mails HTML)

Use o CSS hospedado pelo próprio Fontshare, que é a forma licenciada de servir as fontes:

```html
<link rel="preconnect" href="https://api.fontshare.com">
<link href="https://api.fontshare.com/v2/css?f[]=chillax@200,300,400,500,600,700&f[]=satoshi@400,500,700&display=swap" rel="stylesheet">
```

Pilhas de fallback (as mesmas do `tokens.json`):

```css
--font-display: "Chillax Variable", Chillax, Outfit, ui-sans-serif, system-ui, sans-serif;
--font-texto:   Satoshi, "DM Sans", ui-sans-serif, system-ui, sans-serif;
```

Outfit e DM Sans estão no Google Fonts e são substitutos de trabalho enquanto a Chillax e a Satoshi não carregam. Não são a marca.

## No Claude Design (Design System)

A página do Design System só carrega fontes do Google Fonts ou arquivos guardados no próprio sistema (`fonts/`). Para as pré-visualizações mostrarem Chillax e Satoshi de verdade:

1. Baixe os dois pacotes no Fontshare (botão "Download family").
2. Mande os arquivos `Chillax-Variable.woff2` (ou `.ttf`) e `Satoshi-Variable.woff2` numa conversa comigo, ou arraste-os para a página do Design System: a página guarda fontes em `fonts/` e eu registro cada uma em `tokens.json` (`type.fonts`).

O Design System é privado (só quem está logado e tem acesso vê), então guardar os arquivos nele é uso próprio, não redistribuição.

## No Figma, Illustrator, Canva, InDesign

Instale as famílias localmente a partir do download do Fontshare. Os lockups "Via Simbólica" em `logos/svg/viasimbolica-*.svg` usam texto vivo em Chillax e só rendem certo com a fonte instalada; para a versão definitiva, converta o texto em curvas (Illustrator: Objeto › Expandir; Inkscape: Caminho › Objeto para caminho) ou me envie os arquivos da fonte e eu gero as curvas.
