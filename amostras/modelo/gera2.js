const {chromium}=require('playwright');(async()=>{const b=await chromium.launch();const p=await b.newPage();
await p.goto('file://'+process.argv[2]);await p.evaluate(()=>document.fonts.ready);
await p.pdf({path:'conteudo.pdf',width:'148mm',height:'210mm',printBackground:true,preferCSSPageSize:true,displayHeaderFooter:true,headerTemplate:'<span></span>',
footerTemplate:'<div style="width:100%;font-family:Helvetica,Arial,sans-serif;font-size:6.5pt;letter-spacing:.14em;color:#8a847d;padding:0 17mm;display:flex;justify-content:space-between"><span>CARTA Nº 1 · VIA SIMBÓLICA</span><span><span class="pageNumber"></span> / <span class="totalPages"></span></span></div>'});
await p.goto('file://'+process.argv[3]);await p.pdf({path:'fundo.pdf',width:'148mm',height:'210mm',printBackground:true,preferCSSPageSize:true});await b.close()})()
