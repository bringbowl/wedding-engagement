# -*- coding: utf-8 -*-
# Three elevated place-card design concepts (front face, 新娘 sample)
import urllib.parse

# ---------- shared SVG ornaments ----------
CORNER = '''<svg class="orn" viewBox="0 0 90 90" aria-hidden="true">
  <g fill="none" stroke="CSTROKE" stroke-width="1.1" stroke-linecap="round">
    <path d="M10 40 Q10 10 40 10"/>
    <path d="M16 40 Q16 16 40 16"/>
    <path d="M40 10 Q70 12 66 40" opacity=".0"/>
    <path d="M16 40 C24 42 30 48 30 58 C38 50 48 50 56 52 C46 44 42 34 40 16"
          fill="CFILL" stroke="none"/>
    <path d="M40 16 C40 30 48 40 62 42" />
    <path d="M62 42 C56 40 52 44 52 50"/>
  </g>
  <circle cx="11" cy="11" r="2.1" fill="CSTROKE"/>
  <circle cx="40" cy="12" r="1.3" fill="CSTROKE"/>
  <circle cx="12" cy="40" r="1.3" fill="CSTROKE"/>
</svg>'''

def corner(stroke, fill="none"):
    return CORNER.replace("CSTROKE", stroke).replace("CFILL", fill)

def crest(ring, crownc, monoc, filled=False):
    bg = "FILLGRAD" if filled else "rgba(255,255,255,.0)"
    return f'''<div class="crest" style="border-color:{ring};background:{bg};">
      <div class="cc" style="color:{crownc};">&#9819;</div>
      <div class="cm" style="color:{monoc};">B<span style="color:{ring};">&amp;</span>W</div>
      <div class="cd" style="color:{ring};">EST&middot;10&middot;11</div>
    </div>'''

# flourish divider
DIV = '''<svg class="flr" viewBox="0 0 160 16" aria-hidden="true">
  <g fill="none" stroke="DSTROKE" stroke-width="1.1" stroke-linecap="round">
    <path d="M80 8 C70 2 58 2 50 8 C58 14 70 14 80 8 Z"/>
    <path d="M80 8 C90 2 102 2 110 8 C102 14 90 14 80 8 Z"/>
    <line x1="8" y1="8" x2="50" y2="8"/><line x1="110" y1="8" x2="152" y2="8"/>
  </g>
  <circle cx="80" cy="8" r="2" fill="DSTROKE"/>
  <circle cx="5" cy="8" r="1.5" fill="DSTROKE"/><circle cx="155" cy="8" r="1.5" fill="DSTROKE"/>
</svg>'''
def divider(stroke): return DIV.replace("DSTROKE", stroke)

NAME, TITLE = "戴婉錡", "新娘"

# ---------- Concept A: Ivory Filigree ----------
A = f'''<div class="face A">
  <div class="c tl">{corner("#A8822F","rgba(201,162,75,.10)")}</div>
  <div class="c tr">{corner("#A8822F","rgba(201,162,75,.10)")}</div>
  <div class="c bl">{corner("#A8822F","rgba(201,162,75,.10)")}</div>
  <div class="c br">{corner("#A8822F","rgba(201,162,75,.10)")}</div>
  <div class="inner">
    {crest("#A8822F","#A8822F","#6E1414")}
    <div class="name">{NAME}</div>
    {divider("#A8822F")}
    <div class="title">{TITLE}</div>
  </div>
</div>'''

# ---------- Concept B: Wine & Gilt ----------
B = f'''<div class="face B">
  <div class="c tl">{corner("#D8B15A","rgba(216,177,90,.12)")}</div>
  <div class="c tr">{corner("#D8B15A","rgba(216,177,90,.12)")}</div>
  <div class="c bl">{corner("#D8B15A","rgba(216,177,90,.12)")}</div>
  <div class="c br">{corner("#D8B15A","rgba(216,177,90,.12)")}</div>
  <div class="inner">
    {crest("#E2C275","#E2C275","#F3E7C8")}
    <div class="name gold">{NAME}</div>
    {divider("#D8B15A")}
    <div class="title gold2">{TITLE}</div>
  </div>
</div>'''

# ---------- Concept C: Boarding Pass ----------
C = f'''<div class="face C">
  <div class="bp-main">
    <div class="bp-head">幸福登機門　&#10022;　THE ROYAL TABLE</div>
    <div class="bp-body">
      <div class="bp-left">
        <div class="bp-lab">PASSENGER ・ 貴賓</div>
        <div class="name">{NAME}</div>
        <div class="title">{TITLE}</div>
      </div>
    </div>
    <div class="bp-foot"><span>FLIGHT&nbsp; BW1011</span><span>GATE&nbsp; 2F</span><span>10 &middot; 11</span></div>
  </div>
  <div class="bp-stub">
    {crest("#A8822F","#A8822F","#6E1414")}
    <div class="bp-seat">SEAT</div>
    <div class="bp-seatno">01</div>
    <div class="bp-bars"></div>
  </div>
</div>'''

HTML = f'''<!doctype html>
<html lang="zh-Hant"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>桌卡設計概念</title>
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,500;0,600;0,700;1,600&family=Noto+Serif+TC:wght@500;600;700;900&display=swap" rel="stylesheet">
<style>
  :root{{--red:#8B1A1A;--wine:#6E1414;--gold:#C9A24B;--gold-d:#A8822F;--gold-l:#F3E7C8;--cream:#FBF6EA;--ink:#2B1D12;}}
  *{{box-sizing:border-box;}}
  body{{margin:0;background:#dfd2b6;font-family:"Noto Serif TC",serif;padding:30px 24px;}}
  .wrap{{max-width:560px;margin:0 auto;}}
  .concept{{margin:0 0 30px;}}
  .tag{{display:flex;align-items:baseline;gap:10px;margin:0 2px 10px;}}
  .tag .k{{font-family:"Cormorant Garamond",serif;font-weight:700;font-size:22px;color:var(--wine);
    background:var(--gold-l);border:1px solid var(--gold);width:34px;height:34px;border-radius:50%;
    display:flex;align-items:center;justify-content:center;}}
  .tag .n{{font-size:17px;font-weight:700;color:var(--ink);}}
  .tag .d{{font-size:12px;color:#7a6a45;margin-left:auto;}}

  /* card face: tent front, landscape 85x43mm shown at ~2x */
  .face{{width:520px;height:263px;position:relative;border-radius:3px;overflow:hidden;
    box-shadow:0 10px 26px rgba(70,40,20,.22);}}
  .inner{{position:absolute;inset:0;display:flex;flex-direction:column;align-items:center;justify-content:center;text-align:center;}}
  .name{{font-size:58px;font-weight:900;letter-spacing:.06em;line-height:1;}}
  .title{{font-size:19px;letter-spacing:.42em;text-indent:.42em;margin-top:2px;}}
  .orn{{width:62px;height:62px;}}
  .c{{position:absolute;}} .c.tl{{top:10px;left:10px;}} .c.tr{{top:10px;right:10px;transform:scaleX(-1);}}
  .c.bl{{bottom:10px;left:10px;transform:scaleY(-1);}} .c.br{{bottom:10px;right:10px;transform:scale(-1,-1);}}
  .crest{{width:62px;height:62px;border-radius:50%;border:1.4px solid;display:flex;flex-direction:column;
    align-items:center;justify-content:center;line-height:1;margin-bottom:10px;}}
  .cc{{font-size:15px;margin-bottom:2px;}}
  .cm{{font-family:"Cormorant Garamond",serif;font-weight:700;font-size:19px;letter-spacing:.5px;}}
  .cm span{{font-size:13px;margin:0 2px;}}
  .cd{{font-family:"Cormorant Garamond",serif;font-size:7.5px;letter-spacing:2px;margin-top:2px;}}
  .flr{{width:150px;height:15px;margin:10px 0 2px;}}

  /* A ivory */
  .face.A{{background:
      radial-gradient(130% 90% at 50% 0%, rgba(201,162,75,.08), transparent 55%),
      var(--cream);border:1.5px solid var(--gold-d);}}
  .face.A .inner{{outline:1px solid rgba(168,130,47,.45);outline-offset:-9px;}}
  .face.A .name{{color:var(--red);}} .face.A .title{{color:var(--wine);}}

  /* B wine */
  .face.B{{background:
      radial-gradient(130% 100% at 50% 0%, #7d1616, #6E1414 55%, #5a0f0f),var(--wine);
      border:1.5px solid #D8B15A;}}
  .face.B .inner{{outline:1px solid rgba(216,177,90,.5);outline-offset:-9px;}}
  .face.B .name.gold{{background:linear-gradient(170deg,#f4e3b0,#D8B15A 55%,#b98e36);
      -webkit-background-clip:text;background-clip:text;color:transparent;}}
  .face.B .title.gold2{{color:#E2C275;}}
  .face.B::after{{content:"";position:absolute;inset:0;pointer-events:none;
      background-image:radial-gradient(circle, rgba(216,177,90,.10) 1px, transparent 1.4px);
      background-size:20px 20px;opacity:.5;}}

  /* C boarding pass */
  .face.C{{display:flex;background:var(--cream);border:1.5px solid var(--gold-d);}}
  .bp-main{{flex:1;display:flex;flex-direction:column;}}
  .bp-head{{background:linear-gradient(90deg,#7d1616,#8B1A1A);color:var(--gold-l);
    font-size:12px;letter-spacing:.18em;padding:9px 16px;font-weight:600;}}
  .bp-body{{flex:1;display:flex;align-items:center;padding:4px 20px;}}
  .bp-lab{{font-family:"Cormorant Garamond",serif;font-size:11px;letter-spacing:.28em;color:#9a7a3f;margin-bottom:4px;}}
  .face.C .name{{font-size:52px;color:var(--red);line-height:1;}}
  .face.C .title{{font-size:16px;letter-spacing:.34em;color:var(--wine);margin-top:4px;text-indent:.34em;}}
  .bp-foot{{display:flex;justify-content:space-between;padding:8px 18px;border-top:1px dashed #cbb68a;
    font-family:"Cormorant Garamond",serif;font-size:11px;letter-spacing:.14em;color:#8a7038;}}
  .bp-stub{{width:140px;border-left:2px dashed #c3a76f;display:flex;flex-direction:column;
    align-items:center;justify-content:center;gap:4px;background:
      repeating-linear-gradient(180deg,rgba(201,162,75,.05) 0 2px,transparent 2px 7px),var(--cream);position:relative;}}
  .bp-stub .crest{{margin-bottom:2px;}}
  .bp-seat{{font-family:"Cormorant Garamond",serif;font-size:11px;letter-spacing:.3em;color:#9a7a3f;}}
  .bp-seatno{{font-family:"Cormorant Garamond",serif;font-weight:700;font-size:40px;color:var(--red);line-height:.9;}}
  .bp-bars{{width:96px;height:22px;margin-top:4px;background:
     repeating-linear-gradient(90deg,#4a2a08 0 2px,transparent 2px 3px,#4a2a08 3px 4px,transparent 4px 7px);
     opacity:.8;}}
  /* notches */
  .bp-stub::before,.bp-stub::after{{content:"";position:absolute;left:-7px;width:12px;height:12px;border-radius:50%;background:#dfd2b6;}}
  .bp-stub::before{{top:-6px;}} .bp-stub::after{{bottom:-6px;}}
</style></head>
<body><div class="wrap">
  <div class="concept"><div class="tag"><span class="k">A</span><span class="n">鎏金典雅　Ivory Filigree</span><span class="d">象牙米金・角花卷草・印徽</span></div>{A}</div>
  <div class="concept"><div class="tag"><span class="k">B</span><span class="n">酒紅鎏金　Wine &amp; Gilt</span><span class="d">深酒紅・燙金字・最華麗</span></div>{B}</div>
  <div class="concept"><div class="tag"><span class="k">C</span><span class="n">幸福登機門　Boarding Pass</span><span class="d">延續你們座位圖主視覺・最獨特</span></div>{C}</div>
</div></body></html>'''

with open("outputs/html/card_concepts.html","w",encoding="utf-8") as f:
    f.write(HTML)
print("ok", len(HTML))
