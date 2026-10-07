# -*- coding: utf-8 -*-
import html
BG = "data:image/png;base64," + open("data/card_bg.b64").read().strip()

# no, name, zh-role, en-role, veg
CARDS = [
    (1,  "戴婉錡", "新娘",     "BRIDE",          False),
    (2,  "戴建勳", "新娘爸爸", "BRIDE'S FATHER", False),
    (3,  "林碧霞", "新娘外婆", "GRANDMOTHER",    True),
    (4,  "戴蔡美惠","新娘奶奶", "GRANDMOTHER",    False),
    (5,  "郭乃華", "新娘媽媽", "BRIDE'S MOTHER", False),
    (6,  "羅聖明", "新郎",     "GROOM",          False),
    (7,  "羅茂松", "新郎爸爸", "GROOM'S FATHER", False),
    (8,  "張秀緞", "新郎媽媽", "GROOM'S MOTHER", False),
    (9,  "張坤輝", "新郎阿公", "GRANDFATHER",    False),
    (10, "羅茂騰", "新郎叔叔", "UNCLE",          False),
    (11, "", "", "", False),   # 空白備用卡（現場手寫）
    (12, "", "", "", False),   # 空白備用卡（現場手寫）
]

def face(no,name,zh,en,veg):
    veg_el='<div class="veg">&#127807; 素食 VEG</div>' if veg else ''
    if not name and not zh:   # blank card for handwriting
        return '<div class="face"><div class="txt"></div></div>'
    nlen=len(name)
    ncls="name"+(" n4" if nlen>=4 else "")
    rcls="role"+(" long" if len(en)>8 else "")
    return f'''<div class="face">
      <div class="txt">
        <div class="{rcls}"><span class="zh">{html.escape(zh)}</span><span class="sl">/</span><span class="en">{html.escape(en)}</span></div>
        <div class="{ncls}">{html.escape(name)}</div>
      </div>
      {veg_el}
    </div>'''

def card(*c):
    f=face(*c)
    return f'<div class="card"><div class="half top">{f}</div><div class="fold"></div><div class="half bot">{f}</div></div>'

pages=[]
for i in range(0,len(CARDS),4):
    inner="\n".join(card(*c) for c in CARDS[i:i+4])
    pages.append(f'<div class="sheet">\n{inner}\n</div>')
cards="\n".join(pages)

HTML=f'''<!doctype html><html lang="zh-Hant"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>主桌桌卡</title>
<meta name="description" content="Barry ♥ Winnie 主桌桌卡，皇冠郵戳皇家版，中英雙語，可列印對折。">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:wght@600;700&family=Noto+Serif+TC:wght@600;700;900&display=swap" rel="stylesheet">
<style>
  *{{box-sizing:border-box;}}
  html,body{{margin:0;padding:0;background:#e9dcc2;color:#2B1D12;font-family:"Noto Serif TC",serif;}}
  .note{{max-width:740px;margin:0 auto;padding:18px 16px 4px;}}
  .note .box{{background:#fff;border:1px solid #C9A24B;border-left:5px solid #C9A24B;border-radius:10px;
    padding:12px 16px;font-size:13px;color:#6E1414;line-height:1.85;}}
  .note b{{color:#8B1A1A;}}
  .sheet{{background:#fff;width:210mm;min-height:297mm;margin:16px auto;padding:9mm 8mm;
    display:grid;grid-template-columns:repeat(2,88mm);grid-auto-rows:134mm;
    justify-content:center;align-content:start;gap:5mm 7mm;box-shadow:0 6px 22px rgba(0,0,0,.12);}}
  .card{{width:88mm;height:134mm;position:relative;break-inside:avoid;}}
  .half{{height:67mm;overflow:hidden;}}
  .half.top .face{{transform:rotate(180deg);}}
  .fold{{height:0;border-top:1px dashed #cdb996;}}

  .face{{position:relative;height:100%;background-image:url("{BG}");background-size:100% 100%;background-repeat:no-repeat;}}
  .txt{{position:absolute;left:8%;right:8%;top:49%;transform:translateY(-50%);text-align:center;}}
  .role{{white-space:nowrap;line-height:1;margin-bottom:3.2mm;}}
  .role .zh{{font-family:"Noto Serif TC",serif;font-weight:700;font-size:25px;color:#6e1414;letter-spacing:.02em;}}
  .role .sl{{font-size:21px;color:#9c7a2e;margin:0 5px;font-weight:400;}}
  .role .en{{font-family:"Cormorant Garamond",serif;font-weight:700;font-size:24px;color:#6e1414;letter-spacing:.06em;}}
  .role.long .zh{{font-size:22px;}} .role.long .en{{font-size:19px;}} .role.long .sl{{font-size:18px;margin:0 4px;}}
  .name{{font-family:"Noto Serif TC",serif;font-weight:900;font-size:50px;color:#a8823a;letter-spacing:.05em;line-height:1;
    text-shadow:0 1px 0 rgba(120,88,30,.25);white-space:nowrap;}}
  .name.n4{{font-size:43px;}}
  .veg{{position:absolute;left:50%;bottom:11%;transform:translateX(-50%);font-size:10px;font-weight:700;
    letter-spacing:.1em;color:#2e7d32;border:1px solid #7cbf72;border-radius:999px;padding:1px 9px;background:rgba(255,255,255,.6);}}

  @media print{{
    html,body{{background:#fff;}} .note{{display:none;}}
    .sheet{{box-shadow:none;margin:0;width:210mm;min-height:0;height:auto;padding:9mm 8mm;page-break-after:always;break-after:page;}}
    .sheet:last-child{{page-break-after:auto;break-after:auto;}}
    .card,.face,.half,.name,.role,.veg{{-webkit-print-color-adjust:exact;print-color-adjust:exact;}}
    @page{{size:A4 portrait;margin:0;}}
  }}
</style></head><body>
  <div class="note"><div class="box">
    <b>皇冠郵戳・皇家版（原圖版型）主桌 10 張：</b>展開約 88×134mm、對折後 88×67mm，每頁 4 張共 3 頁。<br>
    <b>列印：</b>A4 100% 不縮放、建議 240–300g 卡紙，沿中間折線對折。<br>
    <b>說明：</b>完整沿用你參考圖的版型（皇冠・燙金角框・卷草・AIR MAIL／TAINAN 郵戳），只替換中英稱謂與名字；外婆附素食標。
  </div></div>
  {cards}
</body></html>'''
open("outputs/html/主桌桌卡_皇家版.html","w",encoding="utf-8").write(HTML)
open("docs/placecards.html","w",encoding="utf-8").write(HTML)
print("ok",len(HTML))
