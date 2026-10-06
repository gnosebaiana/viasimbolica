# Fontes da identidade

| Papel | Família | Pesos usados | Onde baixar |
|---|---|---|---|
| Display, títulos, nome da marca | **Chillax Variable** (Indian Type Foundry) | 200 a 700; nome da marca em 565 | https://www.fontshare.com/fonts/chillax |
| Texto corrido, rótulos, botões | **Satoshi** (Indian Type Foundry) | 400, 500, 700 | https://www.fontshare.com/fonts/satoshi |
| Só a assinatura (em curvas) | **Great Vibes** (TypeSETit, OFL) | 400 | https://fonts.google.com/specimen/Great+Vibes |

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

Os arquivos variáveis `Chillax-Variable.woff2`, `Satoshi-Variable.woff2` e `Satoshi-VariableItalic.woff2` já estão guardados no Design System (pasta `fonts/`, privada) e registrados em `tokens.json`. As pré-visualizações e as peças do Claude Design usam as fontes reais. A Great Vibes da assinatura vem do Google Fonts e só existe em curvas nos arquivos da marca.

## No Figma, Illustrator, Canva, InDesign

Instale as famílias localmente a partir do download do Fontshare. Todos os lockups canônicos em `logos/svg/viasimbolica/` e `logos/svg/literastro/` estão com o nome em curvas e não dependem de fonte instalada. O único arquivo com texto vivo é o `literastro-horizontal.svg` original da designer, em `logos/svg/literastro/originais/`, que pede a Chillax instalada.
