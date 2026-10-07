# -*- coding: utf-8 -*-
import html, urllib.parse

CARDS = [
    (1,  "戴婉錡", "新娘",     "f", False, True),
    (2,  "戴建勳", "新娘爸爸", "f", False, False),
    (3,  "林碧霞", "新娘外婆", "f", True,  False),
    (4,  "戴蔡美惠","新娘奶奶", "f", False, False),
    (5,  "郭乃華", "新娘媽媽", "f", False, False),
    (6,  "羅聖明", "新郎",     "m", False, True),
    (7,  "羅茂松", "新郎爸爸", "m", False, False),
    (8,  "張秀緞", "新郎媽媽", "m", False, False),
    (9,  "張坤輝", "新郎阿公", "m", False, False),
    (10, "羅茂騰", "新郎叔叔", "m", False, False),
]

# ---- subtle 宮廷 damask pattern tile (gold filigree) ----
tile = '''<svg xmlns="http://www.w3.org/2000/svg" width="46" height="46" viewBox="0 0 46 46">
<g fill="none" stroke="#C9A24B" stroke-width="0.9" opacity="0.30">
<path d="M23 3 L43 23 L23 43 L3 23 Z"/>
<path d="M23 12 C28 17,28 17,23 23 C18 17,18 17,23 12 Z"/>
<path d="M23 34 C28 29,28 29,23 23 C18 29,18 29,23 34 Z"/>
<path d="M12 23 C17 18,17 18,23 23 C17 28,17 28,12 23 Z"/>
<path d="M34 23 C29 18,29 18,23 23 C29 28,29 28,34 23 Z"/>
</g>
<g fill="#C9A24B" opacity="0.30">
<circle cx="23" cy="23" r="1.1"/>
<circle cx="0" cy="0" r="1"/><circle cx="46" cy="0" r="1"/>
<circle cx="0" cy="46" r="1"/><circle cx="46" cy="46" r="1"/>
</g></svg>'''
pat = "url(\"data:image/svg+xml,%s\")" % urllib.parse.quote(tile)

# ---- crest / logo (B & W royal seal) ----
def crest(couple):
    filled = "filled" if couple else ""
    return f'''<div class="crest {filled}">
      <div class="cr-crown">&#9819;</div>
      <div class="cr-mono">B<span>&amp;</span>W</div>
      <div class="cr-date">10 &middot; 11</div>
    </div>'''

def face(no, name, title, side, veg, couple):
    vegbadge = '<div class="veg">素</div>' if veg else ''
    dot = f'<span class="dot {side}"></span>'
    nm = html.escape(name); tt = html.escape(title)
    return f'''<div class="face {'c' if couple else ''}">
      {crest(couple)}
      <div class="name">{nm}</div>
      <div class="title">{tt}</div>
      <div class="corner l">{dot}{no}</div>
      {vegbadge}
    </div>'''

def card_html(no, name, title, side, veg, couple):
    f = face(no, name, title, side, veg, couple)
    return f'''<div class="card {'couple' if couple else ''}">
      <div class="half top">{f}</div>
      <div class="fold"></div>
      <div class="half bot">{f}</div>
    </div>'''

pages = []
for i in range(0, len(CARDS), 6):
    inner = "\n".join(card_html(*c) for c in CARDS[i:i+6])
    pages.append(f'<div class="sheet">\n{inner}\n</div>')
cards = "\n".join(pages)

HTML = f'''<!doctype html>
<html lang="zh-Hant"><head>
<meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>主桌桌卡（名牌版）</title>
<meta name="description" content="Barry ♥ Winnie 訂婚宴 主桌桌卡・標準名牌尺寸，宮廷花紋底＋皇冠印徽，對折立式，可列印。">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:wght@600;700&family=Noto+Serif+TC:wght@600;700;900&display=swap" rel="stylesheet">
<style>
  :root{{--red:#8B1A1A;--wine:#6E1414;--gold:#C9A24B;--gold-d:#A8822F;
    --gold-l:#F3E7C8;--cream:#FBF6EA;--ink:#2B1D12;--fem:#B4476B;--mal:#2F5A7A;}}
  *{{box-sizing:border-box;}}
  html,body{{margin:0;padding:0;background:#e9dcc2;color:var(--ink);font-family:"Noto Serif TC",serif;}}
  .note{{max-width:720px;margin:0 auto;padding:18px 16px 4px;}}
  .note .box{{background:#fff;border:1px solid var(--gold);border-left:5px solid var(--gold);
    border-radius:10px;padding:12px 16px;font-size:13px;color:var(--wine);line-height:1.85;}}
  .note b{{color:var(--red);}}

  .sheet{{background:#fff;width:210mm;min-height:297mm;margin:16px auto;padding:12mm 12mm;
    display:grid;grid-template-columns:repeat(2,85mm);grid-auto-rows:86mm;
    justify-content:center;align-content:start;gap:6mm 8mm;box-shadow:0 6px 22px rgba(0,0,0,.12);}}

  .card{{width:85mm;height:86mm;position:relative;break-inside:avoid;}}
  .half{{height:43mm;overflow:hidden;}}
  .half.top .face{{transform:rotate(180deg);}}
  .fold{{height:0;border-top:1px dashed #cdb996;}}

  .face{{position:relative;height:100%;padding:4.5mm 5mm;
    border:1.4px solid var(--gold);background-color:var(--cream);
    background-image:{pat};background-size:23px 23px;
    display:flex;flex-direction:column;align-items:center;justify-content:center;text-align:center;}}
  .face::before{{content:"";position:absolute;inset:1.3mm;border:0.7px solid rgba(201,162,75,.55);
    pointer-events:none;}}
  .face.c{{background-color:#fffdf6;border-color:var(--gold-d);}}

  /* crest */
  .crest{{width:15mm;height:15mm;border-radius:50%;border:1.3px solid var(--gold-d);
    display:flex;flex-direction:column;align-items:center;justify-content:center;
    background:rgba(255,255,255,.55);margin-bottom:1.6mm;line-height:1;}}
  .crest.filled{{background:linear-gradient(160deg,#e9cf92,#C9A24B);border-color:#8a6a24;}}
  .cr-crown{{font-size:11px;color:var(--gold-d);margin-bottom:.4mm;}}
  .crest.filled .cr-crown{{color:#6e4e14;}}
  .cr-mono{{font-family:"Cormorant Garamond",serif;font-weight:700;font-size:13px;color:var(--wine);
    letter-spacing:.5px;}}
  .cr-mono span{{color:var(--gold-d);margin:0 1px;font-size:10px;}}
  .crest.filled .cr-mono{{color:#5a1010;}} .crest.filled .cr-mono span{{color:#7a5410;}}
  .cr-date{{font-family:"Cormorant Garamond",serif;font-size:6.5px;letter-spacing:1px;color:var(--gold-d);margin-top:.3mm;}}

  .name{{font-size:38px;font-weight:900;color:var(--red);letter-spacing:.04em;line-height:1.05;}}
  .face.c .name{{color:#7a1414;}}
  .title{{font-size:14px;color:var(--wine);margin-top:1.4mm;letter-spacing:.18em;}}

  .corner{{position:absolute;bottom:2.4mm;font-size:8px;color:#a98f55;letter-spacing:.06em;
    display:flex;align-items:center;gap:3px;font-family:"Cormorant Garamond",serif;}}
  .corner.l{{left:4mm;}}
  .dot{{width:6px;height:6px;border-radius:50%;display:inline-block;}}
  .dot.f{{background:var(--fem);}} .dot.m{{background:var(--mal);}}
  .veg{{position:absolute;top:3mm;right:3mm;font-size:9px;font-weight:700;color:#2e7d32;
    border:1px solid #2e7d32;border-radius:50%;width:15px;height:15px;display:flex;
    align-items:center;justify-content:center;background:#fff;}}

  @media print{{
    html,body{{background:#fff;}} .note{{display:none;}}
    .sheet{{box-shadow:none;margin:0;width:210mm;min-height:0;height:auto;padding:12mm;
      page-break-after:always;break-after:page;}}
    .sheet:last-child{{page-break-after:auto;break-after:auto;}}
    .card,.face,.half,.veg,.dot,.crest,.face::before{{-webkit-print-color-adjust:exact;print-color-adjust:exact;}}
    @page{{size:A4 portrait;margin:0;}}
  }}
</style></head>
<body>
  <div class="note"><div class="box">
    <b>名牌尺寸：</b>展開約 85×86mm、對折後 85×43mm（小巧站立）。每頁 6 張，共 2 頁。建議 <b>190–250g 卡紙</b>、A4 100% 不縮放。<br>
    <b>對折：</b>沿中間淡色折線對折，折好正反兩面都是正的字。<br>
    <b>設計：</b>宮廷金色花紋底＋ B&amp;W 皇冠印徽；新人為金色印徽、外婆有「素」標、左下角為帶位圖座號（<span style="color:var(--fem)">●</span>女方／<span style="color:var(--mal)">●</span>男方）。
  </div></div>
  {cards}
</body></html>'''

with open("outputs/html/主桌桌卡_名牌版.html","w",encoding="utf-8") as f:
    f.write(HTML)
print("ok", len(HTML))
