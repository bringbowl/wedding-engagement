# -*- coding: utf-8 -*-
import math, html

# center + ellipse for card anchors
CX, CY = 480, 470
RX, RY = 395, 322      # card-center ellipse
TRX, TRY = 300, 232    # table ellipse

# seat: (angle_deg_from_top_clockwise, seat_no, name, rel, side, tag)
SEATS = [
    # 女方 (left, negative)  outward from couple
    (-18,  1, "戴婉錡", "新娘",   "f", "bride"),
    (-54,  4, "戴蔡美惠","新娘奶奶","f", ""),
    (-90,  3, "林碧霞", "新娘外婆","f", "veg"),
    (-126, 5, "郭乃華", "新娘媽媽","f", ""),
    (-162, 2, "戴建勳", "新娘爸爸","f", ""),
    # 男方 (right, positive)
    (18,   6, "羅聖明", "新郎",   "m", "groom"),
    (54,   9, "張坤輝", "新郎阿公","m", ""),
    (90,   7, "羅茂松", "新郎爸爸","m", ""),
    (126,  8, "張秀緞", "新郎媽媽","m", ""),
    (162, 10, "羅茂騰", "新郎叔叔","m", ""),
]

CARD_W, CARD_H = 150, 72

def pos(angle_deg, rx, ry):
    th = math.radians(angle_deg)
    x = CX + rx * math.sin(th)
    y = CY - ry * math.cos(th)
    return x, y

parts = []
# connector lines + cards
for ang, no, name, rel, side, tag in SEATS:
    cx, cy = pos(ang, RX, RY)
    ex, ey = pos(ang, TRX, TRY)   # point on table edge
    parts.append(f'<line x1="{ex:.1f}" y1="{ey:.1f}" x2="{cx:.1f}" y2="{cy:.1f}" class="spoke"/>')

for ang, no, name, rel, side, tag in SEATS:
    cx, cy = pos(ang, RX, RY)
    x = cx - CARD_W/2; y = cy - CARD_H/2
    cls = "card f" if side == "f" else "card m"
    if tag in ("bride","groom"): cls += " couple"
    badge = f'<circle cx="{x+18:.1f}" cy="{y+18:.1f}" r="13" class="badge"/>' \
            f'<text x="{x+18:.1f}" y="{y+22:.1f}" class="bno">{no}</text>'
    vegmark = ''
    if tag == "veg":
        vegmark = f'<text x="{x+CARD_W-10:.1f}" y="{y+20:.1f}" class="veg">素</text>'
    nm = html.escape(name)
    rl = html.escape(rel)
    parts.append(
        f'<g>'
        f'<rect x="{x:.1f}" y="{y:.1f}" width="{CARD_W}" height="{CARD_H}" rx="12" class="{cls}"/>'
        f'{badge}{vegmark}'
        f'<text x="{cx:.1f}" y="{cy-4:.1f}" class="cname">{nm}</text>'
        f'<text x="{cx:.1f}" y="{cy+18:.1f}" class="crel">{rl}</text>'
        f'</g>'
    )
svg_cards = "\n".join(parts)

SVG = f'''
<svg viewBox="0 0 960 860" class="plan" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <radialGradient id="tableg" cx="50%" cy="38%" r="70%">
      <stop offset="0%" stop-color="#9c2020"/>
      <stop offset="70%" stop-color="#8B1A1A"/>
      <stop offset="100%" stop-color="#6E1414"/>
    </radialGradient>
  </defs>

  <!-- stage bar -->
  <rect x="300" y="18" width="360" height="46" rx="10" class="stage"/>
  <text x="480" y="47" class="stageTxt">舞　台　STAGE</text>
  <text x="480" y="92" class="facing">↑　主桌面向舞台　↑</text>

  <!-- table -->
  <ellipse cx="{CX}" cy="{CY}" rx="{TRX}" ry="{TRY}" class="table"/>
  <ellipse cx="{CX}" cy="{CY}" rx="{TRX-14}" ry="{TRY-14}" class="tableInner"/>
  <text x="{CX}" y="{CY-14}" class="tcrown">&#10022;</text>
  <text x="{CX}" y="{CY+26}" class="tlabel">主桌・王位</text>
  <text x="{CX}" y="{CY+54}" class="tlabel2">THE ROYAL TABLE</text>

  {svg_cards}
</svg>'''

HTML = f'''<!doctype html>
<html lang="zh-Hant"><head>
<meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>主桌帶位圖</title>
<meta name="description" content="Barry ♥ Winnie 訂婚宴 主桌（王位）圓桌帶位圖，女方男方分兩側、長輩依輩分靠中，宮廷紅金風。">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:wght@600;700&family=Noto+Serif+TC:wght@500;600;700;900&display=swap" rel="stylesheet">
<style>
  :root{{--red:#8B1A1A;--wine:#6E1414;--gold:#C9A24B;--gold-d:#A8822F;
    --gold-l:#F3E7C8;--cream:#FBF6EA;--ink:#2B1D12;--line:#D8C9A6;
    --fem:#B4476B;--fem-l:#FBEDF1;--mal:#2F5A7A;--mal-l:#EAF1F6;}}
  *{{box-sizing:border-box;}}
  html,body{{margin:0;padding:0;background:#efe6d2;color:var(--ink);font-family:"Noto Serif TC",serif;}}
  .wrap{{max-width:1000px;margin:0 auto;padding:22px 16px 50px;}}
  .cover{{text-align:center;padding:24px 20px 20px;margin-bottom:18px;
    background:linear-gradient(160deg,#7d1616,#8B1A1A 55%,#6E1414);
    border:2px solid var(--gold);border-radius:14px;color:#fff;box-shadow:0 10px 26px rgba(0,0,0,.18);}}
  .cover .ey{{font-family:"Cormorant Garamond",serif;letter-spacing:.4em;font-size:13px;color:var(--gold-l);text-transform:uppercase;}}
  .cover h1{{font-weight:900;font-size:28px;margin:8px 0 4px;}}
  .cover .names{{font-family:"Cormorant Garamond",serif;font-size:19px;letter-spacing:.14em;color:var(--gold-l);}}
  .board{{background:var(--cream);border:1.5px solid var(--gold);border-radius:16px;
    padding:10px 10px 4px;box-shadow:0 6px 18px rgba(0,0,0,.07);}}
  svg.plan{{width:100%;height:auto;display:block;}}
  .stage{{fill:#2b1d12;stroke:var(--gold);stroke-width:1.5;}}
  .stageTxt{{fill:var(--gold-l);font-size:21px;font-weight:700;text-anchor:middle;letter-spacing:.12em;}}
  .facing{{fill:var(--gold-d);font-size:15px;text-anchor:middle;font-weight:600;letter-spacing:.1em;}}
  .table{{fill:url(#tableg);stroke:var(--gold);stroke-width:3;}}
  .tableInner{{fill:none;stroke:var(--gold);stroke-width:1;opacity:.5;}}
  .tcrown{{fill:var(--gold-l);font-size:30px;text-anchor:middle;}}
  .tlabel{{fill:#fff;font-size:26px;font-weight:900;text-anchor:middle;letter-spacing:.08em;}}
  .tlabel2{{fill:var(--gold-l);font-size:12px;text-anchor:middle;letter-spacing:.3em;font-family:"Cormorant Garamond",serif;}}
  .spoke{{stroke:var(--line);stroke-width:1.5;stroke-dasharray:3 3;}}
  .card{{stroke-width:2;}}
  .card.f{{fill:var(--fem-l);stroke:var(--fem);}}
  .card.m{{fill:var(--mal-l);stroke:var(--mal);}}
  .card.couple{{stroke:var(--gold-d);stroke-width:3.5;}}
  .badge{{fill:var(--gold);stroke:#fff;stroke-width:1;}}
  .bno{{fill:#4a2a08;font-size:14px;font-weight:700;text-anchor:middle;}}
  .veg{{fill:#2e7d32;font-size:14px;font-weight:700;text-anchor:middle;}}
  .cname{{font-size:21px;font-weight:900;text-anchor:middle;fill:var(--ink);}}
  .crel{{font-size:13px;text-anchor:middle;fill:var(--wine);}}
  .legend{{display:flex;gap:14px;flex-wrap:wrap;justify-content:center;margin:16px 0 6px;}}
  .lg{{display:flex;align-items:center;gap:7px;font-size:14px;color:var(--ink);
    background:#fff;border:1px solid var(--line);border-radius:999px;padding:6px 14px;}}
  .sw{{width:16px;height:16px;border-radius:4px;border:2px solid;}}
  .sw.f{{background:var(--fem-l);border-color:var(--fem);}}
  .sw.m{{background:var(--mal-l);border-color:var(--mal);}}
  .sw.c{{background:#fff;border-color:var(--gold-d);}}
  .sw.v{{background:#fff;border-color:#2e7d32;color:#2e7d32;font-size:11px;font-weight:700;
    display:flex;align-items:center;justify-content:center;}}
  .note{{background:var(--gold-l);border:1px solid var(--gold);border-radius:12px;
    padding:12px 18px;margin:16px 0 0;font-size:13.5px;color:var(--wine);line-height:1.85;}}
  .note b{{color:var(--red);}}
  .foot{{text-align:center;color:var(--wine);font-size:12px;margin-top:22px;letter-spacing:.12em;}}
  .foot .g{{color:var(--gold-d);margin:0 6px;}}
  @media print{{
    html,body{{background:#fff;}} .wrap{{max-width:none;padding:0;}}
    .cover,.board,.lg,.note,svg *{{-webkit-print-color-adjust:exact;print-color-adjust:exact;}}
    .cover,.board{{box-shadow:none;}}
    @page{{size:A4 landscape;margin:12mm;}}
  }}
</style></head>
<body><div class="wrap">
  <div class="cover">
    <div class="ey">Head Table ・ Seating Plan</div>
    <h1>主桌帶位圖　・　王位</h1>
    <div class="names">BARRY &amp; WINNIE</div>
  </div>

  <div class="board">
    {SVG}
  </div>

  <div class="legend">
    <div class="lg"><span class="sw f"></span>女方家人</div>
    <div class="lg"><span class="sw m"></span>男方家人</div>
    <div class="lg"><span class="sw c"></span>新人（金框）</div>
    <div class="lg"><span class="sw v">素</span>吃素</div>
  </div>

  <div class="note">
    <b>排法說明：</b>新人居中並肩、面向舞台；雙方家人分兩側（女方在左、男方在右），長輩依輩分最靠近新人——<b>奶奶・外婆・阿公</b>緊鄰新人，接著爸媽，叔叔在外側。<br>
    <b>貼心提醒：</b>新娘外婆（林碧霞）吃素，上菜前請提醒桌邊服務人員備素食餐。<br>
    <b>可調整：</b>若想讓爸媽（主婚人）坐在新人正旁、長輩次之，或左右兩側對調，跟我說一聲即可重排。
  </div>

  <div class="foot">BARRY <span class="g">&#10022;</span> WINNIE<span class="g">&#10022;</span>幸福登機門　TAINAN 10&middot;11</div>
</div></body></html>'''

with open("outputs/html/主桌帶位圖.html","w",encoding="utf-8") as f:
    f.write(HTML)
with open("docs/maintable.html","w",encoding="utf-8") as f:
    f.write(HTML)
print("ok", len(HTML))
