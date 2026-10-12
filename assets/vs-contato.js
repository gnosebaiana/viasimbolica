/* Via Simbólica: formulário de contato dos botões de compra.
   O botão abre uma janela que pede nome e telefone, grava os dois na planilha
   (Google Sheets, pelo Apps Script em ferramentas/site/planilha-contatos.gs)
   e leva a pessoa ao WhatsApp do Guilherme com a mensagem já escrita. */
(function () {
  // Endereço do App da Web do Apps Script. Vazio: o formulário não grava, só leva ao WhatsApp.
  var PLANILHA_URL = 'https://script.google.com/macros/s/AKfycbzlSehDlHXqCe-Wgx02_WAEtPvBhAuPBYfOpXM03Th8-OWeOS0ZXRS2SvNGPxpQSDgd/exec';
  var WHATSAPP = '557192469207';

  var dialogo, form, campoNome, campoTel, campoIsca, erro, produtoAtual = '', origemAtual = '';

  function pixel(evento, dados) {
    try { if (window.fbq) window.fbq('track', evento, dados); } catch (e) {}
  }
  function lembrar(chave, valor) {
    try { if (valor === undefined) return localStorage.getItem(chave) || ''; localStorage.setItem(chave, valor); } catch (e) { return ''; }
  }
  function digitos(s) { return (s || '').replace(/\D/g, ''); }
  function mascara(s) {
    var d = digitos(s).replace(/^55(?=\d{10,11}$)/, '').slice(0, 11);
    if (d.length <= 2) return d.length ? '(' + d : '';
    if (d.length <= 6) return '(' + d.slice(0, 2) + ') ' + d.slice(2);
    if (d.length <= 10) return '(' + d.slice(0, 2) + ') ' + d.slice(2, 6) + '-' + d.slice(6);
    return '(' + d.slice(0, 2) + ') ' + d.slice(2, 7) + '-' + d.slice(7);
  }

  function montar() {
    dialogo = document.createElement('dialog');
    dialogo.className = 'vs-contato';
    dialogo.setAttribute('aria-labelledby', 'vs-contato-titulo');
    dialogo.innerHTML =
      '<form class="vs-contato__form" novalidate>' +
        '<button type="button" class="vs-contato__fechar" aria-label="Fechar">×</button>' +
        '<p class="vs-contato__rotulo" data-produto></p>' +
        '<h2 id="vs-contato-titulo" class="vs-contato__titulo">Fale com o Guilherme</h2>' +
        '<p class="vs-contato__texto">Deixe seu nome e seu telefone. Em seguida, a conversa abre no WhatsApp com a mensagem pronta.</p>' +
        '<label class="vs-contato__campo"><span>Nome</span>' +
          '<input name="nome" type="text" autocomplete="name" required minlength="2" maxlength="80"></label>' +
        '<label class="vs-contato__campo"><span>Telefone (WhatsApp)</span>' +
          '<input name="telefone" type="tel" inputmode="tel" autocomplete="tel" required placeholder="(71) 99999-9999"></label>' +
        '<label class="vs-contato__isca" aria-hidden="true">Não preencha<input name="site" type="text" tabindex="-1" autocomplete="off"></label>' +
        '<p class="vs-contato__erro" role="alert"></p>' +
        '<button type="submit" class="vs-contato__enviar">CONTINUAR NO WHATSAPP</button>' +
        '<p class="vs-contato__aviso">Usamos seu nome e seu telefone só para responder ao seu pedido.</p>' +
      '</form>';
    document.body.appendChild(dialogo);
    form = dialogo.querySelector('form');
    campoNome = form.elements.nome;
    campoTel = form.elements.telefone;
    campoIsca = form.elements.site;
    erro = dialogo.querySelector('.vs-contato__erro');

    campoTel.addEventListener('input', function () { campoTel.value = mascara(campoTel.value); });
    dialogo.querySelector('.vs-contato__fechar').addEventListener('click', function () { dialogo.close(); });
    dialogo.addEventListener('click', function (e) { if (e.target === dialogo) dialogo.close(); });
    form.addEventListener('submit', enviar);
  }

  function enviar(e) {
    e.preventDefault();
    var nome = campoNome.value.trim().replace(/\s+/g, ' ');
    var tel = digitos(campoTel.value);
    if (nome.length < 2) { erro.textContent = 'Escreva o seu nome.'; campoNome.focus(); return; }
    if (tel.length < 10 || tel.length > 13) { erro.textContent = 'Confira o telefone, com o DDD.'; campoTel.focus(); return; }
    erro.textContent = '';
    lembrar('vs-nome', nome);
    lembrar('vs-telefone', campoTel.value);

    var botao = form.querySelector('.vs-contato__enviar');
    botao.disabled = true;
    botao.textContent = 'ABRINDO O WHATSAPP…';

    if (PLANILHA_URL && !campoIsca.value) {
      var dados = new URLSearchParams({
        nome: nome, telefone: campoTel.value, produto: produtoAtual,
        origem: origemAtual, pagina: location.pathname
      });
      try { fetch(PLANILHA_URL, { method: 'POST', mode: 'no-cors', body: dados, keepalive: true }); } catch (err) {}
    }
    pixel('Lead', { content_name: produtoAtual });

    var msg = 'Olá, Guilherme. Meu nome é ' + nome + ' e quero saber mais sobre: ' + produtoAtual + '.';
    var destino = 'https://wa.me/' + WHATSAPP + '?text=' + encodeURIComponent(msg);
    setTimeout(function () {
      location.href = destino;
      botao.disabled = false;
      botao.textContent = 'CONTINUAR NO WHATSAPP';
      dialogo.close();
    }, 400);
  }

  // Chamado pelos botões: onclick="return vsContato('Mapa Natal', this)"
  window.vsContato = function (produto, botao) {
    if (!dialogo) montar();
    var rotulo = botao ? (botao.textContent || '').trim() : '';
    var formato = /PDF/i.test(rotulo) ? ' em PDF' : /IMPRESSO/i.test(rotulo) ? ' impresso' : '';
    produtoAtual = produto + formato;
    origemAtual = rotulo;
    dialogo.querySelector('[data-produto]').textContent = produtoAtual.toUpperCase();
    if (!campoNome.value) campoNome.value = lembrar('vs-nome');
    if (!campoTel.value) campoTel.value = lembrar('vs-telefone');
    erro.textContent = '';
    pixel('Contact', { content_name: produtoAtual });
    if (typeof dialogo.showModal === 'function') dialogo.showModal(); else dialogo.setAttribute('open', '');
    (campoNome.value ? campoTel : campoNome).focus();
    return false;
  };
})();
