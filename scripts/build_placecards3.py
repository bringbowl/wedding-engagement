# -*- coding: utf-8 -*-
# Concept B refined — Wine & Gilt, all 10 main-table place cards, small tent format
import html

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

# refined corner flourish (clean double-arc + sprig)
CORNER = '''<svg class="orn" viewBox="0 0 72 72" aria-hidden="true">
  <g fill="none" stroke="#D8B15A" stroke-width="1.15" stroke-linecap="round">
    <path d="M9 36 C9 19 19 9 36 9"/>
    <path d="M9 27 C9 16 16 9 27 9"/>
    <path d="M36 9 C43 9 49 12 53 18"/>
    <path d="M9 36 C9 43 12 49 18 53"/>
  </g>
  <path d="M35 11 C34 19 30 24 23 26 C30 28 34 33 35 41 C36 33 40 28 47 26 C40 24 36 19 35 11 Z"
        fill="#D8B15A" opacity="0.55"/>
  <circle cx="10.5" cy="10.5" r="1.7" fill="#E2C275"/>
</svg>'''

DIV = '''<svg class="flr" viewBox="0 0 170 14" aria-hidden="true">
  <g fill="none" stroke="#D8B15A" stroke-width="1.05" stroke-linecap="round">
    <line x1="14" y1="7" x2="64" y2="7"/><line x1="106" y1="7" x2="156" y2="7"/>
    <path d="M85 7 C77 2.5 67 2.5 61 7 C67 11.5 77 11.5 85 7 Z"/>
    <path d="M85 7 C93 2.5 103 2.5 109 7 C103 11.5 93 11.5 85 7 Z"/>
  </g>
  <circle cx="85" cy="7" r="1.9" fill="#E2C275"/>
  <circle cx="11" cy="7" r="1.4" fill="#D8B15A"/><circle cx="159" cy="7" r="1.4" fill="#D8B15A"/>
</svg>'''

def crest(couple):
    fill = "linear-gradient(158deg,#f0dca6,#D8B15A 60%,#b2882f)" if couple else "rgba(226,194,117,.08)"
    crown = "#6e4e14" if couple else "#E2C275"
    mono  = "#5a1010" if couple else "#F3E7C8"
    amp   = "#7a5410" if couple else "#D8B15A"
    return f'''<div class="crest" style="background:{fill};">
      <div class="cc" style="color:{crown};">&#9819;</div>
      <div class="cm" style="color:{mono};">B<span style="color:{amp};">&amp;</span>W</div>
    </div>'''

def face(no, name, title, side, veg, couple):
    vegbadge = '<div class="veg">素</div>' if veg else ''
    dot = f'<span class="dot {side}"></span>'
    return f'''<div class="face {'c' if couple else ''}">
      <span class="c tl">{CORNER}</span><span class="c tr">{CORNER}</span>
      <span class="c bl">{CORNER}</span><span class="c br">{CORNER}</span>
      <div class="inner">
        {crest(couple)}
        <div class="name">{html.escape(name)}</div>
        {DIV}
        <div class="title">{html.escape(title)}</div>
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
<meta name="description" content="Barry ♥ Winnie 訂婚宴 主桌桌卡・酒紅鎏金，對折立式名牌，可列印。">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:wght@600;700&family=Noto+Serif+TC:wght@600;700;900&display=swap" rel="stylesheet">
<style>
  :root{{--wine:#6E1414;--wine-d:#5a0f0f;--gold:#C9A24B;--goldh:#E2C275;--gold-l:#F3E7C8;--fem:#E79ABA;--mal:#9FC2DD;}}
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

  .face{{position:relative;height:100%;padding:4mm;border:1.5px solid var(--goldh);
    background:
      radial-gradient(120% 95% at 50% 0%, #7d1616, #6E1414 58%, var(--wine-d));
    overflow:hidden;}}
  .face::after{{content:"";position:absolute;inset:0;pointer-events:none;
    background-image:radial-gradient(circle, rgba(226,194,117,.12) 0.7px, transparent 1.1px);
    background-size:17px 17px;opacity:.6;}}
  .face::before{{content:"";position:absolute;inset:1.4mm;border:0.6px solid rgba(226,194,117,.45);pointer-events:none;}}

  .inner{{position:relative;z-index:2;height:100%;display:flex;flex-direction:column;
    align-items:center;justify-content:center;text-align:center;}}
  .crest{{width:13mm;height:13mm;border-radius:50%;border:1.1px solid var(--goldh);
    display:flex;flex-direction:column;align-items:center;justify-content:center;line-height:1;margin-bottom:1.2mm;}}
  .cc{{font-size:10px;margin-bottom:.3mm;}}
  .cm{{font-family:"Cormorant Garamond",serif;font-weight:700;font-size:13px;letter-spacing:.5px;}}
  .cm span{{font-size:9px;margin:0 1px;}}

  .name{{font-size:40px;font-weight:900;letter-spacing:.05em;line-height:1.02;
    background:linear-gradient(168deg,#f6e7ba,#E2C275 52%,#c49a40);
    -webkit-background-clip:text;background-clip:text;color:transparent;}}
  .flr{{width:40mm;height:12px;margin:1mm 0 .6mm;}}
  .title{{font-size:13px;letter-spacing:.42em;text-indent:.42em;color:var(--gold-l);}}

  .c{{position:absolute;z-index:3;width:34px;height:34px;}}
  .c .orn{{width:100%;height:100%;}}
  .c.tl{{top:2.2mm;left:2.2mm;}} .c.tr{{top:2.2mm;right:2.2mm;transform:scaleX(-1);}}
  .c.bl{{bottom:2.2mm;left:2.2mm;transform:scaleY(-1);}} .c.br{{bottom:2.2mm;right:2.2mm;transform:scale(-1,-1);}}

  .corner-no{{position:absolute;z-index:3;left:4mm;bottom:2.6mm;display:flex;align-items:center;gap:3px;
    font-family:"Cormorant Garamond",serif;font-size:8px;color:var(--goldh);opacity:.9;}}
  .dot{{width:6px;height:6px;border-radius:50%;display:inline-block;}}
  .dot.f{{background:var(--fem);}} .dot.m{{background:var(--mal);}}
  .veg{{position:absolute;z-index:3;top:2.6mm;right:2.6mm;font-size:8.5px;font-weight:700;color:#bfe3b6;
    border:1px solid #8fcf86;border-radius:50%;width:14px;height:14px;display:flex;align-items:center;justify-content:center;}}

  @media print{{
    html,body{{background:#fff;}} .note{{display:none;}}
    .sheet{{box-shadow:none;margin:0;width:210mm;min-height:0;height:auto;padding:12mm;page-break-after:always;break-after:page;}}
    .sheet:last-child{{page-break-after:auto;break-after:auto;}}
    .card,.face,.half,.crest,.veg,.dot,.face::after,.face::before,.c,.name{{-webkit-print-color-adjust:exact;print-color-adjust:exact;}}
    @page{{size:A4 portrait;margin:0;}}
  }}
</style></head>
<body>
  <div class="note"><div class="box">
    <b>酒紅鎏金・名牌版：</b>展開約 85×86mm、對折後 85×43mm。每頁 6 張，共 2 頁。<br>
    <b>列印：</b>A4 100% 不縮放、建議 <b>240–300g 卡紙</b>（深色滿版，磅數高較挺、顏色飽和）；若印表機四邊留白，可選「滿版/無邊界」。<br>
    <b>設計：</b>深酒紅燙金字、角花卷草、B&amp;W 皇冠印徽（新人為金色印徽）、外婆「素」標、左下帶位圖座號（<span style="color:#d47ea0">●</span>女方／<span style="color:#6f9fc4">●</span>男方）。
  </div></div>
  {cards}
</body></html>'''

with open("outputs/html/主桌桌卡_酒紅鎏金.html","w",encoding="utf-8") as f:
    f.write(HTML)
print("ok", len(HTML))
