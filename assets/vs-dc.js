/* Via Simbólica: motor mínimo que reproduz, no site, as partes interativas das páginas feitas no canvas.
   Cada <template data-dc> guarda uma seção com {{valores}} e <sc-for>; o Component da página
   (renderVals + setState) é o mesmo do canvas. Gerado junto com as páginas por
   ferramentas/site/montar_paginas.py. */
(function () {
  var MARCA = /\{\{\s*([\w.$]+)\s*\}\}/g;
  var comp = null, blocos = [];

  function valor(caminho, escopo) {
    return caminho.split('.').reduce(function (o, k) { return o == null ? undefined : o[k]; }, escopo);
  }
  function texto(s, escopo) {
    return s.replace(MARCA, function (_, c) { var v = valor(c, escopo); return v == null ? '' : String(v); });
  }

  function processar(no, escopo) {
    var filhos = Array.prototype.slice.call(no.childNodes);
    filhos.forEach(function (f) {
      if (f.nodeType === 3) {
        if (f.data.indexOf('{{') > -1) f.data = texto(f.data, escopo);
        return;
      }
      if (f.nodeType !== 1) return;
      if (f.localName === 'sc-for') {
        var lista = valor((f.getAttribute('list') || '').replace(/[{}\s]/g, ''), escopo) || [];
        var nome = f.getAttribute('as');
        lista.forEach(function (item) {
          var sub = Object.assign({}, escopo); sub[nome] = item;
          var copia = document.createDocumentFragment();
          Array.prototype.forEach.call(f.childNodes, function (c) { copia.appendChild(c.cloneNode(true)); });
          processar(copia, sub);
          f.parentNode.insertBefore(copia, f);
        });
        f.parentNode.removeChild(f);
        return;
      }
      Array.prototype.slice.call(f.attributes).forEach(function (a) {
        if (a.value.indexOf('{{') < 0) return;
        if (/^on/i.test(a.name)) {
          var fn = valor(a.value.replace(/[{}\s]/g, ''), escopo);
          f.removeAttribute(a.name);
          if (typeof fn === 'function') f.addEventListener(a.name.slice(2).toLowerCase(), fn);
        } else {
          f.setAttribute(a.name, texto(a.value, escopo));
        }
      });
      processar(f, escopo);
    });
  }

  function desenhar() {
    var vals = comp.renderVals();
    blocos.forEach(function (b) {
      var frag = b.modelo.content.cloneNode(true);
      processar(frag, vals);
      var tmp = document.createElement('div'); tmp.appendChild(frag.cloneNode(true));
      if (tmp.innerHTML === b.ultimo) {
        // Mesmo HTML: só religa os eventos, sem perder rolagem nem foco.
        return;
      }
      b.ultimo = tmp.innerHTML;
      var foco = document.activeElement, idx = -1;
      if (foco && b.saida.contains(foco)) idx = Array.prototype.indexOf.call(b.saida.querySelectorAll('button'), foco);
      b.saida.replaceChildren(frag);
      if (idx > -1) { var alvo = b.saida.querySelectorAll('button')[idx]; if (alvo) alvo.focus({ preventScroll: true }); }
    });
  }

  window.DCLogic = class {
    constructor() { this.state = {}; }
    setState(s) { this.state = Object.assign({}, this.state, s); desenhar(); }
  };

  window.vsIniciar = function (Componente) {
    comp = new Componente();
    blocos = Array.prototype.map.call(document.querySelectorAll('template[data-dc]'), function (t) {
      var saida = document.createElement('div');
      saida.style.display = 'contents';
      t.parentNode.insertBefore(saida, t);
      return { modelo: t, saida: saida, ultimo: null };
    });
    desenhar();
  };
})();
