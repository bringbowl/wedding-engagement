# -*- coding: utf-8 -*-
import html, json

# owner -> color
OWNER_COLORS = {
    "新郎":"#2F5A7A", "新郎跟主婚人":"#2F5A7A", "新娘":"#B4476B", "新娘表妹":"#9C4A6E", "新郎新娘":"#A8822F",
    "伴郎":"#2E7D6B", "伴娘":"#7A4E9E", "文魚":"#7A4E9E", "Linda":"#9A4E86",
    "婚顧":"#6b6150", "大家一起":"#6b6150", "伴郎伴娘":"#8a5a2b",
}
def pill(owner):
    c=OWNER_COLORS.get(owner,"#6b6150")
    return f'<span class="own" style="background:{c};">{html.escape(owner)}</span>'

# item types:
#   ("i", owner, text)              normal checkable
#   ("i", owner, text, [subs])      checkable with checkable sub-items; subs=[(owner,text),...]
#   ("h", headtext)                 sub-heading (not checkable)
SECTIONS = [
 ("出發前", "行李清點・帶齊才出門", "BEFORE YOU LEAVE", "新郎新娘", [
   ("i","新郎新娘","喜餅帶齊：中式 60 盒（59 葷＋1 素）、西式 90 盒"),
   ("i","新郎新娘","文定六禮（郭元益 ×2）、聘金、金飾盒、木盛盒"),
   ("i","新郎新娘","紅包：奉茶給新娘（男方長輩、叔叔）"),
   ("i","新郎新娘","三套禮服＋配件：① 新中式 ② 金色魚尾 ③ 送客澎裙"),
   ("i","新郎新娘","鞋（婚鞋＋好走備用）、頭飾、手套、耳環項鍊"),
   ("i","新郎新娘","捧花、文定戒、對戒"),
   ("i","新郎新娘","新娘急救包：補妝、別針、OK繃、衛生棉、暈車藥、小點心、充電線"),
   ("i","新郎新娘","拍攝道具：喜帖 ×2、婚禮小物 ×2（可拆）、求婚戒指、結婚戒指"),
   ("i","新郎新娘","禮金桌／接待用品：禮金簿、紅包袋、文具組、簽到本、投票貼紙、婚禮小物、祝福小卡、筆"),
   ("i","新郎新娘","座位圖（一大一小）、賓客對照表 ×2、主桌＋各桌桌卡"),
   ("i","新郎新娘","無框畫 ＋ 相簿 ＋ 謝卡"),
   ("i","新郎新娘","禮券紅包 ＋ 三項獎品（dresscode／抽獎用）"),
   ("i","新郎新娘","工作人員紅包"),
   ("i","新郎新娘","尾款（場地／廠商）"),
   ("i","新郎新娘","喜糖"),
   ("i","新娘","甜湯"),
   ("i","新郎新娘","吸管"),
   ("i","新郎新娘","訂婚當天分工清單表（本清單印出）"),
   ("i","新郎新娘","證件、合約、保單、工作人員聯絡清單"),
 ]),
 ("9:30", "到場後", "ARRIVAL", "", [
   ("i","伴郎","清點喜餅（中式 59 葷＋1 素、西式 90）",[
       ("伴郎","先把中式 1 盒「素」拿出來（給素食長輩）"),
       ("伴郎","文定儀式桌：中式 24 盒 ＋ 西式 24 盒"),
       ("伴郎","新娘房（女方直接帶回家）：中式 19 盒 ＋ 西式 34 盒"),
       ("伴郎","其餘喜餅全部拿到一樓禮金桌"),
   ]),
   ("i","伴娘","備妥平面攝影拍攝道具：喜帖 ×2、婚禮小物拆開 ×2、求婚戒指、結婚戒指"),
   ("i","婚顧","和場地／專員確認：動線、燈光、音響、投影"),
 ]),
 ("11:00", "文定儀式物品回收・佈置（11:00–11:30）", "HAND-OFF & SET-UP", "", [
   ("h","文定儀式物品回收"),
   ("i","文魚","聘金 ＋ 金飾盒 → 拿到新娘房"),
   ("i","Linda","郭元益六禮 ×1 → 拿到新娘房"),
   ("i","新郎","喜餅 14 盒中式 ＋ 14 盒西式"),
   ("i","伴郎","剩下多的喜餅 → 拿到一樓禮金桌"),
   ("i","新郎","郭元益六禮 ×1 ＋ 木盛盒"),
   ("h","佈置就位"),
   ("i","伴娘","禮金桌就位：禮金簿、紅包袋、文具組、喜餅、投票貼紙、婚禮小物、簽到本、座位圖（一大一小）、賓客對照表 ×2、祝福小卡、筆"),
   ("i","伴娘","無框畫、相簿、謝卡擺放"),
   ("i","伴郎","主桌桌卡擺放（對照主桌帶位圖）"),
   ("i","伴郎","各桌桌卡擺放"),
    ("i","新郎跟主婚人","主婚人別上胸花"),
 ]),
 ("12:30", "宴席開始後", "AFTER BANQUET STARTS", "新娘表妹", [
   ("i","新娘表妹","投票貼紙 / 禮金簿 / 筆電 / 文具 收到新娘房"),
   ("i","新娘表妹","紅包給新娘三姨"),
   ("i","新娘表妹","檢查沒有貴重物品後再離開"),
 ]),
 ("結束後", "收尾清點", "WRAP-UP", "", [
   ("i","新娘","禮金清點"),
   ("i","大家一起","回收禮金桌物品"),
   ("i","新娘","尾款結算"),
   ("i","新娘","工作人員紅包發放（伴郎伴娘記得來領）"),
 ]),
]

# assign indices to all checkable
idx=0
def take():
    global idx; v=idx; idx+=1; return v

secs_html=[]; total=0
for badge,title,en,secowner,items in SECTIONS:
    rows=[]; seccount=0
    secpill = f'<span class="secown">全部：{pill(secowner)}</span>' if secowner else ""
    for it in items:
        if it[0]=="h":
            rows.append(f'<div class="subhead">{html.escape(it[1])}</div>')
            continue
        owner=it[1]; text=it[2]; subs=it[3] if len(it)>3 else []
        i=take(); seccount+=1
        subhtml=""
        if subs:
            sr=[]
            for so,st in subs:
                si=take(); seccount+=1
                sr.append(f'<label class="item sub"><input type="checkbox" data-i="{si}"><span class="box"></span>'
                          f'<span class="t">{html.escape(st)}</span>{pill(so)}</label>')
            subhtml='<div class="subs">'+"\n".join(sr)+'</div>'
        rows.append(
            f'<label class="item"><input type="checkbox" data-i="{i}"><span class="box"></span>'
            f'<span class="t">{html.escape(text)}</span>{pill(owner)}</label>{subhtml}')
    total=idx
    secs_html.append(f'''<section class="sec">
      <div class="sec-h">
        <span class="badge">{html.escape(badge)}</span>
        <span class="st"><span class="zh">{html.escape(title)}</span><span class="en">{en}</span></span>
        <span class="cnt" data-cnt>0/{seccount}</span>
      </div>
      {f'<div class="secownbar">{secpill}</div>' if secowner else ''}
      <div class="items">{''.join(rows)}</div>
    </section>''')

sections_html="\n".join(secs_html)
# legend
LEG=[("新郎","新郎"),("新娘","新娘"),("新娘表妹","新娘表妹"),("伴郎","伴郎"),("伴娘","伴娘"),("文魚","文魚(伴娘)"),("新郎跟主婚人","新郎跟主婚人"),("Linda","Linda(伴娘)"),("婚顧","婚顧")]
legend="".join(f'<span class="lg">{pill(k)}<i>{html.escape(lbl)}</i></span>' for k,lbl in LEG)

HTML=f'''<!doctype html><html lang="zh-Hant"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>訂婚當天分工清單</title>
<meta name="description" content="Barry ♥ Winnie 訂婚當天分工檢查清單，含負責人、喜餅分配、文定回收，可勾選可列印。">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:wght@600;700&family=Noto+Serif+TC:wght@500;600;700;900&display=swap" rel="stylesheet">
<style>
  :root{{--red:#8B1A1A;--wine:#6E1414;--gold:#C9A24B;--gold-d:#A8822F;--gold-l:#F3E7C8;--cream:#FBF6EA;--ink:#2B1D12;--line:#E4D6B4;}}
  *{{box-sizing:border-box;-webkit-tap-highlight-color:transparent;}}
  html,body{{margin:0;padding:0;background:#efe6d2;color:var(--ink);font-family:"Noto Serif TC",serif;}}
  .wrap{{max-width:780px;margin:0 auto;padding:0 14px 60px;}}
  header{{text-align:center;padding:24px 18px 18px;margin:14px 0 12px;border-radius:14px;color:#fff;
    background:linear-gradient(160deg,#7d1616,#8B1A1A 55%,#6E1414);border:2px solid var(--gold);box-shadow:0 8px 24px rgba(0,0,0,.16);}}
  header .ey{{font-family:"Cormorant Garamond",serif;letter-spacing:.36em;font-size:12px;color:var(--gold-l);text-transform:uppercase;}}
  header h1{{font-weight:900;font-size:24px;margin:8px 0 4px;}}
  header .meta{{font-size:12px;color:#f0ddc0;letter-spacing:.12em;margin-top:6px;}}
  header .rule{{width:60px;height:2px;background:var(--gold);margin:11px auto 0;}}
  .bar{{position:sticky;top:0;z-index:20;background:var(--cream);border:1px solid var(--gold);border-radius:12px;
    padding:9px 12px;margin:0 0 12px;display:flex;align-items:center;gap:12px;box-shadow:0 3px 10px rgba(0,0,0,.08);}}
  .bar .prog{{flex:1;}} .bar .ptrack{{height:9px;background:#eadfc2;border-radius:99px;overflow:hidden;}}
  .bar .pfill{{height:100%;width:0;background:linear-gradient(90deg,var(--gold),var(--gold-d));transition:width .25s;}}
  .bar .plab{{font-size:12px;color:var(--wine);margin-top:3px;font-weight:600;}}
  .bar button{{font-family:inherit;font-size:12.5px;border:1px solid var(--gold-d);background:#fff;color:var(--wine);border-radius:99px;padding:7px 12px;cursor:pointer;white-space:nowrap;}}
  .bar button:active{{background:var(--gold-l);}}
  .legend{{display:flex;flex-wrap:wrap;gap:6px 12px;background:var(--gold-l);border:1px solid var(--gold);border-radius:10px;padding:9px 13px;margin:0 0 15px;}}
  .lg{{display:inline-flex;align-items:center;gap:5px;font-size:12px;color:var(--wine);}}
  .lg i{{font-style:normal;}}
  .sec{{background:#fff;border:1px solid var(--line);border-radius:14px;margin:0 0 13px;overflow:hidden;box-shadow:0 3px 12px rgba(0,0,0,.05);}}
  .sec-h{{display:flex;align-items:center;gap:10px;padding:12px 14px;background:linear-gradient(90deg,#fbf4e6,#fdfaf2);border-bottom:1px solid var(--line);cursor:pointer;}}
  .badge{{flex-shrink:0;font-family:"Cormorant Garamond",serif;font-weight:700;font-size:15px;color:#fff;background:var(--red);border-radius:8px;padding:5px 11px;min-width:52px;text-align:center;}}
  .st{{flex:1;display:flex;flex-direction:column;}}
  .st .zh{{font-weight:700;font-size:16px;color:var(--red);}}
  .st .en{{font-family:"Cormorant Garamond",serif;font-size:11px;letter-spacing:.18em;color:var(--gold-d);}}
  .cnt{{font-size:12px;color:var(--wine);font-weight:600;white-space:nowrap;}}
  .secownbar{{padding:7px 14px 0;font-size:12px;color:var(--wine);}}
  .secownbar .secown{{display:inline-flex;align-items:center;gap:6px;}}
  .items{{padding:4px 6px 9px;}}
  .subhead{{margin:8px 10px 2px;font-size:12.5px;font-weight:700;color:var(--gold-d);letter-spacing:.06em;
    border-left:3px solid var(--gold);padding-left:8px;}}
  .item{{display:flex;align-items:flex-start;gap:10px;padding:10px;border-radius:9px;cursor:pointer;}}
  .item:active{{background:#faf5e8;}}
  .item.sub{{padding:8px 10px 8px 4px;}}
  .subs{{margin:0 0 2px 30px;border-left:2px dashed #ecdfbf;}}
  .item input{{position:absolute;opacity:0;width:0;height:0;}}
  .box{{flex-shrink:0;width:22px;height:22px;border:2px solid var(--gold-d);border-radius:6px;margin-top:1px;display:flex;align-items:center;justify-content:center;background:#fff;transition:.12s;}}
  .box::after{{content:"";width:11px;height:6px;border-left:2.6px solid #fff;border-bottom:2.6px solid #fff;transform:rotate(-45deg) scale(0);transition:.12s;margin-top:-2px;}}
  .item input:checked ~ .box{{background:var(--gold-d);border-color:var(--gold-d);}}
  .item input:checked ~ .box::after{{transform:rotate(-45deg) scale(1);}}
  .item .t{{flex:1;font-size:14.5px;line-height:1.55;color:var(--ink);}}
  .item.sub .t{{font-size:13.5px;}}
  .item input:checked ~ .t{{color:#a79a84;text-decoration:line-through;text-decoration-color:#cDBf9f;}}
  .own{{flex-shrink:0;color:#fff;font-size:11px;font-weight:700;border-radius:99px;padding:2px 9px;white-space:nowrap;margin-top:1px;letter-spacing:.03em;}}
  footer{{text-align:center;color:var(--wine);font-size:11.5px;margin-top:22px;letter-spacing:.1em;}}
  footer .g{{color:var(--gold-d);margin:0 6px;}}
  @media print{{
    html,body{{background:#fff;}} .bar{{display:none!important;}}
    .wrap{{max-width:none;padding:0;}}
    header,.sec,.legend{{box-shadow:none;}}
    header,.badge,.sec-h,.box,.own,.item input:checked ~ .box,.legend{{-webkit-print-color-adjust:exact;print-color-adjust:exact;}}
    .sec-h{{break-inside:avoid;break-after:avoid;page-break-after:avoid;}}
    .secownbar{{break-before:avoid;}}
    .item,.item.sub{{break-inside:avoid;page-break-inside:avoid;}}
    .subhead{{break-after:avoid;page-break-after:avoid;}}
    .sec{{margin-bottom:8px;}}
    .item input:checked ~ .t{{color:var(--ink);text-decoration:none;}}
    @page{{size:A4;margin:11mm;}}
  }}
</style></head><body><div class="wrap">
  <header>
    <div class="ey">Engagement Day &middot; Duty Roster</div>
    <h1>訂婚當天 ・ 分工檢查清單</h1>
    <div class="rule"></div>
    <div class="meta">BARRY &amp; WINNIE　・　幸福登機門　・　2026.10.11　台南</div>
  </header>
  <div class="bar">
    <div class="prog"><div class="ptrack"><div class="pfill" id="pfill"></div></div>
      <div class="plab"><span id="pnum">0</span> / {total} 已完成</div></div>
    <button onclick="window.print()">列印</button>
    <button onclick="resetAll()">重置</button>
  </div>
  <div class="legend">{legend}</div>
  {sections_html}
  <footer>BARRY <span class="g">&#10022;</span> WINNIE<span class="g">&#10022;</span>幸福登機門　TAINAN 10&middot;11</footer>
</div>
<script>
  var KEY="bw_duty_v1", total={total};
  var boxes=[].slice.call(document.querySelectorAll('input[type=checkbox]'));
  function load(){{try{{return JSON.parse(localStorage.getItem(KEY))||{{}};}}catch(e){{return {{}};}}}}
  function save(st){{try{{localStorage.setItem(KEY,JSON.stringify(st));}}catch(e){{}}}}
  var state=load();
  boxes.forEach(function(b){{if(state[b.dataset.i])b.checked=true;
    b.addEventListener('change',function(){{state[b.dataset.i]=b.checked; if(!b.checked)delete state[b.dataset.i]; save(state); refresh();}});}});
  function refresh(){{
    var done=boxes.filter(function(b){{return b.checked;}}).length;
    document.getElementById('pnum').textContent=done;
    document.getElementById('pfill').style.width=(total?(done/total*100):0)+'%';
    document.querySelectorAll('.sec').forEach(function(s){{
      var ins=s.querySelectorAll('input'), d=0; ins.forEach(function(i){{if(i.checked)d++;}});
      s.querySelector('[data-cnt]').textContent=d+'/'+ins.length;}});
  }}
  document.querySelectorAll('.sec-h').forEach(function(h){{
    h.addEventListener('click',function(e){{ if(e.target.tagName==='INPUT')return;
      var el=h.parentElement.querySelector('.items'); el.style.display= el.style.display==='none'?'':'none';}});}});
  function resetAll(){{ if(!confirm('確定清除所有勾選？'))return; state={{}}; save(state); boxes.forEach(function(b){{b.checked=false;}}); refresh(); }}
  window.resetAll=resetAll; refresh();
</script></body></html>'''

open("outputs/html/訂婚當天分工清單.html","w",encoding="utf-8").write(HTML)
print("ok",len(HTML),"total items",total)
