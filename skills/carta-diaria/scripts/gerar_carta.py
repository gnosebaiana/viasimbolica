#!/usr/bin/env python3
"""Gera o PDF A5 de uma carta diária da Via Simbólica.

Uso:
  python3 gerar_carta.py --numero 2 --titulo "O barro" --data 2026-11-16 \
      --texto carta.md [--hora 07:30] [--fecho "Até amanhã,|Guiga|*Via Simbólica*"] [--saida .]

carta.md: só o corpo da carta (sem o título e sem o fecho), um parágrafo por
bloco, separados por linha em branco. Itálico com *assim*, _assim_ ou <i>assim</i>.

Saídas: "Carta nº N · Via Simbólica.pdf" na pasta --saida, e um resumo no terminal.
Código 2: a Lua muda de signo nesse dia e a hora não foi dada (pergunte a hora).
"""
import argparse, base64, html, math, os, re, subprocess, sys, tempfile, datetime as dt

AQUI = os.path.dirname(os.path.abspath(__file__))
ASSETS = os.path.join(os.path.dirname(AQUI), "assets")
sys.path.insert(0, AQUI)
from glifos import SOL, LUA, SIGNOS, svg  # noqa: E402


def garantir(modulo, pacote=None):
    try:
        return __import__(modulo)
    except ImportError:
        subprocess.run([sys.executable, "-m", "pip", "install", "-q", pacote or modulo], check=True)
        return __import__(modulo)


ephem = garantir("ephem")
pypdf = garantir("pypdf")


def longitude(corpo, quando_utc):
    d = ephem.Date(quando_utc)
    corpo.compute(d, epoch=d)
    return math.degrees(ephem.Ecliptic(corpo, epoch=d).lon) % 360


def signo(lon):
    return int(lon // 30)


def ceu(data, hora, fuso):
    """Sol e Lua (zodíaco tropical, equinócio da data) no momento local dado."""
    local = dt.datetime.combine(data, hora)
    utc = local - dt.timedelta(hours=fuso)
    return longitude(ephem.Sun(), utc), longitude(ephem.Moon(), utc)


def lua_muda_no_dia(data, fuso):
    ini = ceu(data, dt.time(0, 0), fuso)[1]
    fim = ceu(data, dt.time(23, 59), fuso)[1]
    if signo(ini) == signo(fim):
        return None
    # busca a hora do ingresso
    a, b = dt.datetime.combine(data, dt.time(0, 0)), dt.datetime.combine(data, dt.time(23, 59))
    for _ in range(30):
        m = a + (b - a) / 2
        if signo(ceu(m.date(), m.time(), fuso)[1]) == signo(ini):
            a = m
        else:
            b = m
    return SIGNOS[signo(ini)][0], SIGNOS[signo(fim)][0], b.strftime("%Hh%M")


def inline(t):
    t = html.escape(t.strip(), quote=False)
    t = re.sub(r"&lt;(/?)(i|em)&gt;", r"<\1i>", t)
    t = re.sub(r"&lt;(/?)(b|strong)&gt;", r"<\1b>", t)
    t = re.sub(r"\*\*(?!\s)(.+?)(?<!\s)\*\*", r"<b>\1</b>", t)
    t = re.sub(r"(?<![\w*])\*(?!\s)(.+?)(?<!\s)\*(?![\w*])", r"<i>\1</i>", t)
    t = re.sub(r"(?<![\w_])_(?!\s)(.+?)(?<!\s)_(?![\w_])", r"<i>\1</i>", t)
    t = re.sub(r'"([^"]+)"', r"“\1”", t)
    t = re.sub(r"\s+", " ", t)
    return t


def fonte(nome):
    with open(os.path.join(ASSETS, "fontes", nome), "rb") as f:
        return "data:font/woff2;base64," + base64.b64encode(f.read()).decode()


def renderizar(carta_html, fundo_html, pdf_texto, pdf_fundo, rodape):
    r = subprocess.run(["node", os.path.join(AQUI, "render.js"), carta_html, fundo_html, pdf_texto, pdf_fundo, rodape],
                       capture_output=True, text=True)
    if r.returncode == 0:
        return
    try:
        from playwright.sync_api import sync_playwright
    except ImportError:
        sys.exit("Não achei Playwright (nem no node, nem no Python). Instale: pip install playwright && playwright install chromium\n" + r.stderr)
    rod = ('<div style="width:100%;font-family:Helvetica,Arial,sans-serif;font-size:6.5pt;letter-spacing:.14em;color:#8a847d;'
           'padding:0 17mm;display:flex;justify-content:space-between"><span>' + rodape +
           '</span><span><span class="pageNumber"></span> / <span class="totalPages"></span></span></div>')
    with sync_playwright() as p:
        b = p.chromium.launch()
        pg = b.new_page()
        pg.goto("file://" + os.path.abspath(carta_html))
        pg.evaluate("document.fonts.ready")
        pg.pdf(path=pdf_texto, width="148mm", height="210mm", print_background=True, prefer_css_page_size=True,
               display_header_footer=True, header_template="<span></span>", footer_template=rod)
        pg.goto("file://" + os.path.abspath(fundo_html))
        pg.pdf(path=pdf_fundo, width="148mm", height="210mm", print_background=True, prefer_css_page_size=True)
        b.close()


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--numero", required=True)
    ap.add_argument("--tipo", choices=["carta", "glosa"], default="carta")
    ap.add_argument("--titulo", default="", help="vazio numa glosa sem título: o título vira 'Glosa nº N'")
    ap.add_argument("--data", required=True, help="AAAA-MM-DD, o dia em que a carta foi escrita")
    ap.add_argument("--hora", help="HH:MM, hora local em que foi escrita")
    ap.add_argument("--fuso", type=float, default=-3, help="horas em relação a UTC (Brasília = -3)")
    ap.add_argument("--texto", required=True)
    ap.add_argument("--fecho", default="Até amanhã,|Guiga|*Via Simbólica*")
    ap.add_argument("--saida", default=".")
    a = ap.parse_args()

    data = dt.date.fromisoformat(a.data)
    ingresso = lua_muda_no_dia(data, a.fuso)
    if a.hora:
        hora = dt.time.fromisoformat(a.hora)
    elif ingresso:
        de, para, quando = ingresso
        print(f"PERGUNTAR A HORA: em {data:%d/%m/%Y} a Lua passa de {de} para {para} às {quando} (fuso {a.fuso:+g}). "
              f"Rode de novo com --hora.", file=sys.stderr)
        sys.exit(2)
    else:
        hora = dt.time(12, 0)

    sol, lua = ceu(data, hora, a.fuso)
    s_sol, s_lua = SIGNOS[signo(sol)], SIGNOS[signo(lua)]

    with open(a.texto, encoding="utf-8") as f:
        blocos = [b for b in re.split(r"\n\s*\n", f.read()) if b.strip()]
    if not blocos:
        sys.exit("O texto da carta está vazio.")
    def bloco(b):
        if b.lstrip().startswith(">"):
            miolo = re.sub(r"^\s*>\s?", "", b, flags=re.M)
            return f'<blockquote><p>{inline(miolo)}</p></blockquote>'
        return f"<p>{inline(b)}</p>"
    pars = []
    for b in blocos:
        h = bloco(b)
        if h.startswith("<blockquote>") and pars and pars[-1].startswith("<blockquote>"):
            pars[-1] = pars[-1][:-len("</blockquote>")] + h[len("<blockquote>"):]
        else:
            pars.append(h)
    nome_tipo = "Carta" if a.tipo == "carta" else "Glosa"
    titulo = a.titulo.strip() or f"{nome_tipo} nº {a.numero}"
    fecho = "".join(f"<p>{inline(l)}</p>" for l in a.fecho.split("|") if l.strip())

    astros = (f'<span title="Sol em {s_sol[0]}">{svg(SOL)}{svg(s_sol[1])}</span>'
              f'<span title="Lua em {s_lua[0]}">{svg(LUA)}{svg(s_lua[1])}</span>')
    with open(os.path.join(ASSETS, "carta.html"), encoding="utf-8") as f:
        t = f.read()
    for k, v in {
        "__CHILLAX__": fonte("Chillax-Variable.woff2"),
        "__SATOSHI__": fonte("Satoshi-Variable.woff2"),
        "__SATOSHI_ITALICO__": fonte("Satoshi-VariableItalic.woff2"),
        "__NUMERO__": html.escape(str(a.numero)),
        "__TITULO__": inline(titulo),
        "__ROTULO__": f"{nome_tipo} nº {html.escape(str(a.numero))}" if a.titulo.strip() else "Correspondências",
        "__ASTROS__": astros,
        "__DATA__": f"{data.day:02d} · {data.month:02d} · {data.year}",
        "__CORPO__": "\n".join(pars[:-1]),
        "__ULTIMO__": pars[-1],
        "__FECHO__": fecho,
    }.items():
        t = t.replace(k, v)

    os.makedirs(a.saida, exist_ok=True)
    nome = f"{nome_tipo} nº {a.numero} · Via Simbólica.pdf"
    destino = os.path.join(a.saida, nome)
    with tempfile.TemporaryDirectory() as tmp:
        ch = os.path.join(tmp, "carta.html")
        with open(ch, "w", encoding="utf-8") as f:
            f.write(t)
        pt, pf = os.path.join(tmp, "texto.pdf"), os.path.join(tmp, "fundo.pdf")
        renderizar(ch, os.path.join(ASSETS, "fundo.html"), pt, pf, f"{nome_tipo.upper()} Nº {a.numero} · VIA SIMBÓLICA")
        fundo = pypdf.PdfReader(pf).pages[0]
        w = pypdf.PdfWriter()
        for pg in pypdf.PdfReader(pt).pages:
            pg.merge_page(fundo, over=False)
            w.add_page(pg)
        w.add_metadata({"/Title": f"{nome_tipo} nº {a.numero} · {re.sub('<[^>]+>', '', inline(titulo))}",
                        "/Author": "Guiga · Via Simbólica"})
        try:
            w.compress_identical_objects(remove_duplicates=True, remove_unreferenced=True)
        except TypeError:
            w.compress_identical_objects()
        with open(destino, "wb") as f:
            w.write(f)

    r = pypdf.PdfReader(destino)
    ultima = r.pages[-1].extract_text() or ""
    linhas = [l for l in ultima.splitlines() if l.strip() and "VIA SIMB" not in l.upper()]
    print(f"PDF: {destino}")
    print(f"Páginas: {len(r.pages)} · {os.path.getsize(destino)//1024} KB")
    print(f"Céu em {data:%d/%m/%Y} às {hora:%H:%M} (fuso {a.fuso:+g}): Sol a {sol%30:.0f}° de {s_sol[0]}, Lua a {lua%30:.0f}° de {s_lua[0]}")
    if ingresso and a.hora:
        print(f"Atenção: neste dia a Lua passa de {ingresso[0]} para {ingresso[1]} às {ingresso[2]}.")
    print(f"Linhas de texto na última página: {len(linhas)}")


if __name__ == "__main__":
    main()
