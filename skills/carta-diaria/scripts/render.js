// Uso: node render.js <carta.html> <fundo.html> <conteudo.pdf> <fundo.pdf> <rodape>
// Gera o PDF do texto (sem fundo) e uma página de papel; o Python junta os dois.
const path = require('path');
let chromium;
try { ({ chromium } = require('playwright')); }
catch (e) { console.error('playwright não encontrado para o node'); process.exit(3); }
(async () => {
  const [carta, fundo, saidaTexto, saidaFundo, rodape] = process.argv.slice(2);
  const b = await chromium.launch();
  const p = await b.newPage();
  await p.goto('file://' + path.resolve(carta));
  await p.evaluate(() => document.fonts.ready);
  await p.pdf({
    path: saidaTexto, width: '148mm', height: '210mm', printBackground: true, preferCSSPageSize: true,
    displayHeaderFooter: true, headerTemplate: '<span></span>',
    footerTemplate: '<div style="width:100%;font-family:Helvetica,Arial,sans-serif;font-size:6.5pt;letter-spacing:.14em;color:#8a847d;padding:0 17mm;display:flex;justify-content:space-between"><span>' + rodape + '</span><span><span class="pageNumber"></span> / <span class="totalPages"></span></span></div>'
  });
  await p.goto('file://' + path.resolve(fundo));
  await p.pdf({ path: saidaFundo, width: '148mm', height: '210mm', printBackground: true, preferCSSPageSize: true });
  await b.close();
})().catch(e => { console.error(e); process.exit(1); });
