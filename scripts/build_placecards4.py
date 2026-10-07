# -*- coding: utf-8 -*-
# Final: Wine & Gilt place cards fused with the couple's real B&W honey-jar emblem + brand type
import html

EMB   = "data:image/png;base64," + open("data/emblem_gold.png.b64").read().strip()
EMB_B = "data:image/png;base64," + open("data/emblem_gold_bright.png.b64").read().strip()

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

def face(no, name, title, side, veg, couple):
    emb = EMB_B if couple else EMB
    vegbadge = '<div class="veg">素</div>' if veg else ''
    dot = f'<span class="dot {side}"></span>'
    return f'''<div class="face {'c' if couple else ''}">
      <div class="inner">
        <img class="emblem" src="{emb}" alt="B&amp;W">
        <div class="name">{html.escape(name)}</div>
        <div class="title">{html.escape(title)}</div>
        <div class="script">Barry &amp; Winnie</div>
      </div>
      <div class="corner-no">{dot}<span>{no}</span></div>
      {vegbadge}
    </div>'''

def card_html(*c):
    f = face(*c)
    return f'''<div class="card {'couple' if c[5] else ''}">
      <div class="half top">{f}</div><div class="fold"></div><div class="half bot">{f}</div>
    </div>'''

pages = []
for i in range(0, len(CARDS), 6):
    inner = "\n".join(card_html(*c) for c in CARDS[i:i+6])
    pages.append(f'<div class="sheet">\n{inner}\n</div>')
cards = "\n".join(pages)

HTML = f'''<!doctype html>
<html lang="zh-Hant"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>主桌桌卡・酒紅鎏金</title>
<meta name="description" content="Barry ♥ Winnie 訂婚宴 主桌桌卡，融合婚禮 logo 與字體風格，酒紅鎏金對折名牌。">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:wght@500;600;700&family=Pinyon+Script&family=Noto+Serif+TC:wght@600;700;900&display=swap" rel="stylesheet">
<style>
  :root{{--wine:#6E1414;--wine-d:#550d0d;--gold:#C9A24B;--goldh:#E2C275;--gold-l:#F3E7C8;--fem:#E79ABA;--mal:#9FC2DD;}}
  *{{box-sizing:border-box;}}
  html,body{{margin:0;padding:0;background:#e9dcc2;color:#2B1D12;font-family:"Noto Serif TC",serif;}}
  .note{{max-width:720px;margin:0 auto;padding:18px 16px 4px;}}
  .note .box{{background:#fff;border:1px solid var(--gold);border-left:5px solid var(--gold);
    border-radius:10px;padding:12px 16px;font-size:13px;color:var(--wine);line-height:1.85;}}
  .note b{{color:#8B1A1A;}}

  .sheet{{background:#fff;width:210mm;min-height:297mm;margin:16px auto;padding:12mm;
    display:grid;grid-template-columns:repeat(2,85mm);grid-auto-rows:86mm;
    justify-content:center;align-content:start;gap:6mm 8mm;box-shadow:0 6px 22px rgba(0,0,0,.12);}}
  .card{{width:85mm;height:86mm;position:relative;break-inside:avoid;}}
  .half{{height:43mm;overflow:hidden;}}
  .half.top .face{{transform:rotate(180deg);}}
  .fold{{height:0;border-top:1px dashed #cdb996;}}

  .face{{position:relative;height:100%;padding:3.4mm;border:1.5px solid var(--goldh);
    background:radial-gradient(125% 100% at 50% 6%, #7d1616, #6E1414 60%, var(--wine-d));
    overflow:hidden;}}
  .face::before{{content:"";position:absolute;inset:1.5mm;border:0.6px solid rgba(226,194,117,.42);pointer-events:none;z-index:3;}}
  .inner{{position:relative;z-index:2;height:100%;display:flex;flex-direction:column;
    align-items:center;justify-content:center;text-align:center;}}

  .emblem{{height:15mm;width:auto;display:block;margin-bottom:.4mm;
    filter:drop-shadow(0 1px 1px rgba(0,0,0,.25));}}
  .name{{font-size:37px;font-weight:900;letter-spacing:.05em;line-height:1;
    background:linear-gradient(168deg,#f8ecc4,#E2C275 52%,#c49a40);
    -webkit-background-clip:text;background-clip:text;color:transparent;}}
  .title{{font-size:12.5px;letter-spacing:.44em;text-indent:.44em;color:var(--gold-l);margin-top:1.6mm;}}
  .script{{font-family:"Pinyon Script",cursive;font-size:15px;color:var(--goldh);
    margin-top:.8mm;opacity:.92;}}

  .corner-no{{position:absolute;z-index:4;left:3.6mm;bottom:2.4mm;display:flex;align-items:center;gap:3px;
    font-family:"Cormorant Garamond",serif;font-size:8px;color:var(--goldh);opacity:.85;}}
  .dot{{width:5.5px;height:5.5px;border-radius:50%;display:inline-block;}}
  .dot.f{{background:var(--fem);}} .dot.m{{background:var(--mal);}}
  .veg{{position:absolute;z-index:4;top:2.4mm;right:2.4mm;font-size:8px;font-weight:700;color:#bfe3b6;
    border:1px solid #8fcf86;border-radius:50%;width:13px;height:13px;display:flex;align-items:center;justify-content:center;}}

  @media print{{
    html,body{{background:#fff;}} .note{{display:none;}}
    .sheet{{box-shadow:none;margin:0;width:210mm;min-height:0;height:auto;padding:12mm;page-break-after:always;break-after:page;}}
    .sheet:last-child{{page-break-after:auto;break-after:auto;}}
    .card,.face,.half,.veg,.dot,.name,.emblem,.face::before{{-webkit-print-color-adjust:exact;print-color-adjust:exact;}}
    @page{{size:A4 portrait;margin:0;}}
  }}
</style></head>
<body>
  <div class="note"><div class="box">
    <b>酒紅鎏金・融合你們的婚禮 logo：</b>展開約 85×86mm、對折後 85×43mm，每頁 6 張共 2 頁。<br>
    <b>列印：</b>A4 100% 不縮放、建議 <b>240–300g 卡紙</b>；深色滿版建議選「滿版／無邊界」列印。<br>
    <b>設計：</b>直接用你們的 B&amp;W honey jar 徽標＋手寫字體風格；新人為亮金徽標、外婆「素」標、左下帶位圖座號（<span style="color:#d47ea0">●</span>女方／<span style="color:#6f9fc4">●</span>男方）。
  </div></div>
  {cards}
</body></html>'''

with open("outputs/html/主桌桌卡_酒紅鎏金.html","w",encoding="utf-8") as f:
    f.write(HTML)
print("ok", len(HTML))
