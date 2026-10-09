# -*- coding: utf-8 -*-
"""
Generate Wedding Engagement & Banquet Schedule Webpage.
Outputs:
  - outputs/html/訂婚與午宴當天流程表.html
  - docs/schedule.html
"""

HTML = """<!doctype html>
<html lang="zh-Hant">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
  <title>2026.10.11 文定儀式 ＆ 午宴流程表 · Barry ♥ Winnie</title>
  <meta name="description" content="羅聖明 ＆ 戴婉錡 2026.10.11 台南阿勇家漂亮議會廳文定儀式與午宴流程表、影音流程、備品與負責人員清單。">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:wght@600;700&family=Noto+Serif+TC:wght@500;600;700;900&display=swap" rel="stylesheet">
  <style>
    :root {
      --wine: #6E1414;
      --red: #8B1A1A;
      --gold: #C9A24B;
      --gold-d: #A8822F;
      --gold-l: #F5EADA;
      --gold-hl: #E2C275;
      --cream: #FBF6EA;
      --bg: #F8F3E8;
      --ink: #2B1D12;
      --gray-ink: #5C4A3A;
      --card-bg: #FFFFFF;
      --border: #E8DCC6;
    }
    * { box-sizing: border-box; -webkit-tap-highlight-color: transparent; }
    html, body {
      margin: 0; padding: 0;
      background: var(--bg);
      color: var(--ink);
      font-family: "Noto Serif TC", "PingFang TC", "Songti TC", serif;
      min-height: 100vh;
    }
    body {
      padding: 16px 12px 64px;
      display: flex;
      flex-direction: column;
      align-items: center;
    }
    .wrap {
      width: 100%;
      max-width: 720px;
    }

    /* Top Navigation Back Link */
    .top-nav {
      display: flex;
      align-items: center;
      justify-content: space-between;
      margin-bottom: 12px;
      padding: 0 4px;
    }
    .back-btn {
      display: inline-flex;
      align-items: center;
      gap: 6px;
      font-size: 13px;
      color: var(--wine);
      text-decoration: none;
      background: var(--card-bg);
      border: 1px solid var(--border);
      padding: 6px 14px;
      border-radius: 999px;
      font-weight: 600;
      box-shadow: 0 2px 6px rgba(0,0,0,0.04);
      transition: all .15s;
    }
    .back-btn:hover, .back-btn:active {
      border-color: var(--gold);
      background: var(--cream);
    }
    .update-tag {
      font-size: 11px;
      color: #8C745E;
      font-family: "Cormorant Garamond", serif;
      letter-spacing: .08em;
    }

    /* Hero Header */
    header {
      text-align: center;
      background: var(--card-bg);
      border: 1.5px solid var(--gold);
      border-radius: 16px;
      padding: 24px 18px 20px;
      box-shadow: 0 8px 24px rgba(110, 20, 20, 0.08);
      position: relative;
      margin-bottom: 16px;
    }
    header::before {
      content: "";
      position: absolute;
      top: 5px; left: 5px; right: 5px; bottom: 5px;
      border: 1px solid rgba(201, 162, 75, 0.35);
      border-radius: 12px;
      pointer-events: none;
    }
    .eyebrow {
      display: inline-block;
      font-family: "Cormorant Garamond", serif;
      font-size: 12px;
      letter-spacing: .2em;
      color: var(--wine);
      background: var(--cream);
      border: 1px solid var(--gold);
      border-radius: 999px;
      padding: 3px 12px;
      margin-bottom: 10px;
      font-weight: 700;
      text-transform: uppercase;
    }
    h1 {
      font-size: 22px;
      font-weight: 900;
      color: var(--wine);
      margin: 0 0 6px;
      letter-spacing: .04em;
    }
    h1 .heart {
      color: var(--gold);
      margin: 0 3px;
    }
    .meta-loc {
      font-size: 13px;
      color: var(--gray-ink);
      margin: 0 0 10px;
      font-weight: 600;
      letter-spacing: .05em;
    }
    .vendors-pill {
      display: flex;
      flex-wrap: wrap;
      justify-content: center;
      gap: 6px;
      font-size: 11.5px;
      color: var(--wine);
      margin-top: 8px;
      padding-top: 10px;
      border-top: 1px dashed var(--border);
    }
    .vp-item {
      background: #FAF3E6;
      border: 1px solid #E4D2B4;
      border-radius: 6px;
      padding: 2px 8px;
    }
    .vp-item b {
      color: var(--gold-d);
    }

    /* Tabs (Segmented Control) */
    .tabs-bar {
      display: grid;
      grid-template-columns: repeat(3, 1fr);
      gap: 6px;
      background: var(--card-bg);
      border: 1px solid var(--border);
      padding: 6px;
      border-radius: 14px;
      margin-bottom: 18px;
      box-shadow: 0 3px 12px rgba(0,0,0,0.04);
      position: sticky;
      top: 10px;
      z-index: 100;
    }
    .tab-btn {
      font-family: inherit;
      font-size: 13.5px;
      font-weight: 700;
      color: var(--gray-ink);
      background: transparent;
      border: none;
      border-radius: 10px;
      padding: 10px 4px;
      cursor: pointer;
      transition: all .2s;
      text-align: center;
      white-space: nowrap;
    }
    .tab-btn:hover {
      background: rgba(201, 162, 75, 0.1);
      color: var(--wine);
    }
    .tab-btn.active {
      background: var(--wine);
      color: #fff;
      box-shadow: 0 4px 12px rgba(110, 20, 20, 0.25);
    }

    /* Tab Panes */
    .tab-pane {
      display: none;
    }
    .tab-pane.active {
      display: block;
      animation: fadeIn .25s ease-out;
    }
    @keyframes fadeIn {
      from { opacity: 0; transform: translateY(4px); }
      to { opacity: 1; transform: translateY(0); }
    }

    /* Section Subhead */
    .pane-header {
      background: linear-gradient(135deg, #7D1616 0%, #6E1414 100%);
      color: #fff;
      border-radius: 12px;
      padding: 14px 16px;
      margin-bottom: 16px;
      border: 1px solid var(--gold);
      box-shadow: 0 4px 14px rgba(110, 20, 20, 0.15);
      display: flex;
      align-items: center;
      justify-content: space-between;
    }
    .pane-header h2 {
      margin: 0;
      font-size: 16px;
      font-weight: 700;
      letter-spacing: .05em;
      display: flex;
      align-items: center;
      gap: 8px;
    }
    .pane-header .badge {
      font-size: 11px;
      background: rgba(255,255,255,.18);
      border: 1px solid rgba(255,255,255,.3);
      padding: 2px 8px;
      border-radius: 999px;
      font-family: "Cormorant Garamond", serif;
      letter-spacing: .1em;
    }

    /* Timeline Container & Cards */
    .timeline {
      display: flex;
      flex-direction: column;
      gap: 14px;
    }
    .t-card {
      background: var(--card-bg);
      border: 1px solid var(--border);
      border-radius: 14px;
      padding: 16px 18px;
      box-shadow: 0 3px 12px rgba(0,0,0,0.03);
      position: relative;
      transition: border-color .15s;
    }
    .t-card:hover {
      border-color: var(--gold);
    }
    .t-card.highlight {
      border: 1.5px solid var(--gold);
      background: linear-gradient(180deg, #FFFFFF 0%, #FCF8EE 100%);
    }

    /* Card Top: Time Badge + Title */
    .t-top {
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 10px;
      margin-bottom: 10px;
      border-bottom: 1px solid #F2E8D8;
      padding-bottom: 9px;
    }
    .t-time {
      font-family: "Cormorant Garamond", serif;
      font-size: 16px;
      font-weight: 700;
      color: var(--wine);
      background: var(--cream);
      border: 1px solid var(--gold);
      padding: 3px 10px;
      border-radius: 8px;
      letter-spacing: .08em;
      white-space: nowrap;
    }
    .t-act {
      font-size: 16px;
      font-weight: 700;
      color: var(--wine);
      flex: 1;
      text-align: right;
      letter-spacing: .03em;
    }

    /* Content details */
    .t-body {
      font-size: 14px;
      line-height: 1.7;
      color: var(--ink);
    }
    .step-list {
      margin: 0; padding: 0 0 0 20px;
    }
    .step-list li {
      margin-bottom: 5px;
    }
    .step-list li:last-child {
      margin-bottom: 0;
    }
    .notice-star {
      background: #FFF9ED;
      border-left: 3px solid var(--gold);
      padding: 6px 10px;
      font-size: 13px;
      color: #8B1A1A;
      border-radius: 0 6px 6px 0;
      margin: 8px 0 4px;
      font-weight: 600;
    }

    /* Tags & Badges Area (Media, Props, Staff) */
    .t-meta-box {
      margin-top: 12px;
      padding-top: 10px;
      border-top: 1px dashed #EDE1CA;
      display: flex;
      flex-direction: column;
      gap: 7px;
      font-size: 12.5px;
    }
    .meta-row {
      display: flex;
      align-items: flex-start;
      gap: 8px;
    }
    .m-label {
      flex-shrink: 0;
      font-size: 11px;
      font-weight: 700;
      padding: 2px 7px;
      border-radius: 5px;
      letter-spacing: .05em;
      margin-top: 1.5px;
    }
    .m-label.venue {
      background: #FFF3CD;
      color: #856404;
      border: 1px solid #FFEEBA;
    }
    .m-label.couple {
      background: #F8D7DA;
      color: #721C24;
      border: 1px solid #F5C6CB;
    }
    .m-label.staff {
      background: #D1ECF1;
      color: #0C5460;
      border: 1px solid #BEE5EB;
    }
    .m-label.media {
      background: #E2E3E5;
      color: #383D41;
      border: 1px solid #D6D8DB;
    }
    .m-text {
      flex: 1;
      color: var(--gray-ink);
      line-height: 1.55;
    }
    .m-text b {
      color: var(--wine);
    }

    /* Sub-timeline block inside cards */
    .sub-section {
      background: #FAF6ED;
      border: 1px solid #EADBBE;
      border-radius: 10px;
      padding: 10px 12px;
      margin-top: 8px;
    }
    .sub-sec-title {
      font-size: 13.5px;
      font-weight: 700;
      color: var(--wine);
      margin-bottom: 6px;
      display: flex;
      align-items: center;
      gap: 6px;
    }

    /* Tab 3: Grid Checklist */
    .checklist-grid {
      display: grid;
      grid-template-columns: 1fr;
      gap: 14px;
    }
    @media (min-width: 600px) {
      .checklist-grid {
        grid-template-columns: 1fr 1fr;
      }
    }
    .cl-box {
      background: var(--card-bg);
      border: 1px solid var(--border);
      border-radius: 14px;
      padding: 16px 18px;
      box-shadow: 0 3px 12px rgba(0,0,0,0.03);
    }
    .cl-title {
      font-size: 15px;
      font-weight: 700;
      color: var(--wine);
      border-bottom: 1.5px solid var(--gold);
      padding-bottom: 7px;
      margin-bottom: 10px;
      display: flex;
      align-items: center;
      justify-content: space-between;
    }
    .cl-tag {
      font-size: 11px;
      padding: 1px 7px;
      border-radius: 4px;
      background: var(--cream);
      color: var(--gold-d);
      border: 1px solid var(--gold);
    }
    .cl-items {
      list-style: none;
      margin: 0; padding: 0;
      font-size: 13px;
      color: var(--ink);
      line-height: 1.7;
    }
    .cl-items li {
      padding: 4px 0;
      border-bottom: 1px dotted #F0E6D2;
      display: flex;
      align-items: flex-start;
      gap: 8px;
    }
    .cl-items li:last-child {
      border-bottom: none;
    }
    .cl-dot {
      color: var(--gold);
      font-size: 15px;
      line-height: 1;
      margin-top: 3px;
    }

    /* Footer Note */
    .foot-note {
      text-align: center;
      margin-top: 18px;
      font-size: 12px;
      color: #9C8570;
      letter-spacing: .05em;
    }
    footer {
      text-align: center;
      margin-top: 32px;
      font-size: 12px;
      color: #8C745E;
      font-family: "Cormorant Garamond", serif;
      letter-spacing: .12em;
    }
    footer .glyph {
      color: var(--gold);
      margin: 0 4px;
    }

    /* Print Styles */
    @media print {
      body { background: #fff; padding: 0; }
      .top-nav, .tabs-bar, .foot-note, footer { display: none; }
      .tab-pane { display: block !important; page-break-after: always; }
      .t-card, .cl-box { box-shadow: none; border: 1px solid #ccc; break-inside: avoid; }
    }
  </style>
</head>
<body>
  <div class="wrap">
    <div class="top-nav">
      <a href="index.html" class="back-btn">‹ 返回工作台首頁</a>
      <span class="update-tag">VER 2026/10/4</span>
    </div>

    <header>
      <div class="eyebrow">Engagement &amp; Banquet Schedule</div>
      <h1>羅聖明 <span class="heart">♥</span> 戴婉錡</h1>
      <p class="meta-loc">2026.10.11 (日) 阿勇家餐飲事業 - 漂亮議會廳</p>
      <div class="vendors-pill">
        <span class="vp-item"><b>主持人</b> Amy 筆電+音控</span>
        <span class="vp-item"><b>禮服</b> 1 文定 + 2 晚</span>
        <span class="vp-item"><b>造型</b> 妃妃</span>
        <span class="vp-item"><b>婚攝</b> 竺竺</span>
        <span class="vp-item"><b>錄影</b> 萊玥</span>
        <span class="vp-item"><b>佈置</b> 法爾</span>
      </div>
    </header>

    <!-- Navigation Tabs -->
    <div class="tabs-bar">
      <button class="tab-btn active" onclick="switchTab('tab-ceremony')">💍 文定儀式</button>
      <button class="tab-btn" onclick="switchTab('tab-banquet')">🥂 午宴流程</button>
      <button class="tab-btn" onclick="switchTab('tab-props')">📋 備品人員</button>
    </div>

    <!-- ==================== TAB 1: 文定儀式 ==================== -->
    <div id="tab-ceremony" class="tab-pane active">
      <div class="pane-header">
        <h2><span>💍</span> 早晨 · 文定儀式流程表</h2>
        <span class="badge">09:30 - 11:00</span>
      </div>

      <div class="timeline">
        <!-- 09:30 -->
        <div class="t-card">
          <div class="t-top">
            <span class="t-time">09:30</span>
            <span class="t-act">儀式前準備 · 擺聘</span>
          </div>
          <div class="t-body">
            <b>Amy 確認各樣文定物品 ＆ 擺放。</b>
            <div class="notice-star">★ 預先擺妥六禮聘禮桌、長輩喝茶椅（6張）與高矮椅。</div>
          </div>
          <div class="t-meta-box">
            <div class="meta-row">
              <span class="m-label venue">會場備</span>
              <span class="m-text">聘禮桌*1-2張、高矮椅、喝茶椅*6、茶盤、茶杯、甜茶</span>
            </div>
            <div class="meta-row">
              <span class="m-label couple">新人備</span>
              <span class="m-text">
                <b>六禮（聘禮桌擺放）：</b>1. 秘覓喜餅*24盒、2. 日禾春喜餅*24盒、3. 四色喜糖*2組、4. 香燭禮炮*2組、5. 男/女頭尾禮紅包、6. 男/女金飾、7. 小聘(現金)、8. 木盛盒*1<br>
                <b>儀式另備：</b>男方長輩喝茶紅包*6、甜湯 1 碗
              </span>
            </div>
          </div>
        </div>

        <!-- 10:00 -->
        <div class="t-card">
          <div class="t-top">
            <span class="t-time">10:00</span>
            <span class="t-act">親友陸續抵達</span>
          </div>
          <div class="t-body">
            親友陸續抵達漂亮議會廳宴會廳，稍作休息、寒暄迎賓。
          </div>
        </div>

        <!-- 10:25 -->
        <div class="t-card highlight">
          <div class="t-top">
            <span class="t-time">10:25</span>
            <span class="t-act">雙方親友入座</span>
          </div>
          <div class="t-body">
            雙方親友就座（新郎的位置於奉茶區的最後一位）。
            <div class="notice-star">★ 提醒：新郎入座前將喝茶紅包（6包）發給喝茶親友準備。</div>
          </div>
          <div class="t-meta-box">
            <div class="meta-row">
              <span class="m-label staff">人員安排</span>
              <span class="m-text">男方喝茶長輩依序就座：爸爸 → 媽媽 → 阿公 → 堂伯父 → 叔叔 → 新郎</span>
            </div>
          </div>
        </div>

        <!-- 10:30-11:00 儀式核心 -->
        <div class="t-card highlight">
          <div class="t-top">
            <span class="t-time">10:30 - 11:00</span>
            <span class="t-act">文定核心儀式</span>
          </div>
          <div class="t-body">
            <!-- 奉茶 -->
            <div class="sub-section">
              <div class="sub-sec-title">① 新娘入場 · 奉茶</div>
              <ol class="step-list">
                <li>新娘由<b>好命婆</b>牽引入場。</li>
                <li>新娘由好命婆陪伴，依序向男方親友奉茶。</li>
                <li>奉茶完畢，新娘由好命婆牽至入口休息。</li>
                <li>男方喝茶親友備妥紅包捲入茶杯中。</li>
              </ol>
            </div>

            <!-- 壓茶甌 -->
            <div class="sub-section">
              <div class="sub-sec-title">② 壓茶甌</div>
              <ol class="step-list">
                <li>新娘再次由好命婆牽引入場。</li>
                <li>新娘由好命婆陪伴，將男方親友茶杯及紅包收回。</li>
                <li>新娘將收回之茶盤交給<b>女方紅包代收人</b>。</li>
              </ol>
            </div>

            <!-- 戴戒指 -->
            <div class="sub-section">
              <div class="sub-sec-title">③ 坐高腳椅 · 交換戒指 · 添妝</div>
              <ol class="step-list">
                <li>新娘由好命婆攙扶坐上高腳椅、腳踏矮凳（好命婆可回座）。</li>
                <li>邀請新郎至新娘身邊。</li>
                <li>新人交換戒指（新娘：金戒+銅戒繫紅線；新郎：金戒）。</li>
                <li>男方媽媽為新娘戴金飾（耳環、項鍊、手鍊）。</li>
                <li>女方媽媽為新郎戴金項鍊。</li>
                <li>女方外婆為新娘添妝，戴項鍊一條。</li>
                <li>女方阿嬤為新娘添妝，戴項鍊一條。</li>
              </ol>
            </div>

            <!-- 喝甜湯 -->
            <div class="sub-section">
              <div class="sub-sec-title">④ 喝甜湯</div>
              <div>新人互餵對方喝一口甜湯，象徵圓滿甜蜜。</div>
            </div>

            <!-- 禮成合照 -->
            <div class="sub-section">
              <div class="sub-sec-title">⑤ 禮成 ＆ 親友大合照</div>
              <div>Amy 宣布禮成、正式介紹新人，隨後進行家族大合照。</div>
            </div>
          </div>

          <div class="t-meta-box">
            <div class="meta-row">
              <span class="m-label staff">關鍵人員</span>
              <span class="m-text">
                <b>男方喝茶 6 位：</b>爸爸(羅茂松)、媽媽(張秀緞)、阿公(張坤輝)、堂伯父、叔叔(羅茂騰)、新郎(羅聖明)<br>
                <b>男方媒人婆：</b>阿珠阿姨<br>
                <b>女方好命婆：</b>二姨 (郭乃萍)<br>
                <b>女方紅包代收人：</b>文魚
              </span>
            </div>
          </div>
        </div>

        <!-- 11:00 -->
        <div class="t-card">
          <div class="t-top">
            <span class="t-time">11:00</span>
            <span class="t-act">新人回休息室 · 文定收拾</span>
          </div>
          <div class="t-body">
            <ul class="step-list">
              <li>新人一同回休息室換裝休息。</li>
              <li>Amy 請親友協助將文定備品收拾至新娘房。</li>
            </ul>
            <div class="notice-star">★ 務必預留：中西式喜餅各 12 盒於新娘房（男方儀式結束帶回）。</div>
          </div>
        </div>
      </div>
    </div>

    <!-- ==================== TAB 2: 午宴流程 ==================== -->
    <div id="tab-banquet" class="tab-pane">
      <div class="pane-header">
        <h2><span>🥂</span> 中午 · 午宴宴客流程表</h2>
        <span class="badge">11:00 - 14:30+</span>
      </div>

      <div class="timeline">
        <!-- 11:00 彩排 -->
        <div class="t-card">
          <div class="t-top">
            <span class="t-time">11:00</span>
            <span class="t-act">午宴進場總彩排</span>
          </div>
          <div class="t-body">
            午宴進場總彩排（伴郎伴娘、雙方主婚人、新人動線確認，*依現場狀況彈性調整*）。
          </div>
        </div>

        <!-- 11:30 迎賓 -->
        <div class="t-card">
          <div class="t-top">
            <span class="t-time">11:30</span>
            <span class="t-act">迎賓 · 賓客入席</span>
          </div>
          <div class="t-body">
            賓客陸續進場、禮金桌簽名發餅、引導至座位。<br>
            迎賓時邀請賓客於專區黏貼【Dresscode 臉部票選貼紙】。
          </div>
          <div class="t-meta-box">
            <div class="meta-row">
              <span class="m-label media">影音播放</span>
              <span class="m-text">迎賓音樂 ＋ 婚紗照輪播</span>
            </div>
          </div>
        </div>

        <!-- 12:30-12:35 開場影片 -->
        <div class="t-card">
          <div class="t-top">
            <span class="t-time">12:30 - 12:35</span>
            <span class="t-act">婚禮開始 · 開場影片</span>
          </div>
          <div class="t-body">
            播放婚禮開場影片（長度約 1:35）。
            <div class="notice-star">★ 影片結束直接開門，燈光聚焦大門入口！</div>
          </div>
          <div class="t-meta-box">
            <div class="meta-row">
              <span class="m-label media">影音播放</span>
              <span class="m-text">影片內建音樂</span>
            </div>
          </div>
        </div>

        <!-- 12:35-12:40 第一次進場 -->
        <div class="t-card highlight">
          <div class="t-top">
            <span class="t-time">12:35 - 12:40</span>
            <span class="t-act">第一次進場</span>
          </div>
          <div class="t-body">
            <ol class="step-list">
              <li><b>儐相進場：</b>Ollie ＆ 2千 / 文魚 ＆ Linda 一同進場入座（四位一起走不用分開）。</li>
              <li><b>女方主婚人進場：</b>戴建勳 爸爸 ＆ 郭乃華 媽媽進場後入席主桌。</li>
              <li><b>男方主婚人進場：</b>羅茂松 爸爸 ＆ 張秀緞 媽媽進場後入席主桌。</li>
              <li><b>新郎入場：</b>新郎羅聖明入場至紅毯定位點，比手勢深情迎接新娘入場。</li>
              <li><b>新娘入場：</b>新娘戴婉錡入場（無捧花），與新郎會合後同步牽手步上舞台。</li>
            </ol>
          </div>
          <div class="t-meta-box">
            <div class="meta-row">
              <span class="m-label media">影音流程</span>
              <span class="m-text">伴郎伴娘[流程1] → 女方父母[流程2] → 男方父母[流程3] → 新郎[流程4] → 新娘[流程5]</span>
            </div>
            <div class="meta-row">
              <span class="m-label couple">新人備</span>
              <span class="m-text">新郎胸花*1、雙方主婚人胸花*4</span>
            </div>
          </div>
        </div>

        <!-- 12:40-12:45 致詞 -->
        <div class="t-card">
          <div class="t-top">
            <span class="t-time">12:40 - 12:45</span>
            <span class="t-act">舞台致詞</span>
          </div>
          <div class="t-body">
            邀請雙方主婚人、新娘阿嬤（戴蔡美惠、林碧霞）、新郎阿公（張坤輝）上台。<br>
            <b>主婚人致詞順序：</b>新郎爸爸 → 新娘媽媽 → 新娘爸爸
          </div>
          <div class="t-meta-box">
            <div class="meta-row">
              <span class="m-label media">影音播放</span>
              <span class="m-text">流程 6</span>
            </div>
            <div class="meta-row">
              <span class="m-label venue">會場備</span>
              <span class="m-text">麥克風 * 1</span>
            </div>
          </div>
        </div>

        <!-- 12:45-12:50 舉杯 -->
        <div class="t-card">
          <div class="t-top">
            <span class="t-time">12:45 - 12:50</span>
            <span class="t-act">全場舉杯致謝</span>
          </div>
          <div class="t-body">
            新人與雙方主婚人、長輩向全場嘉賓舉杯致謝，全場齊賀！
          </div>
          <div class="t-meta-box">
            <div class="meta-row">
              <span class="m-label media">影音播放</span>
              <span class="m-text">流程 7</span>
            </div>
            <div class="meta-row">
              <span class="m-label venue">會場備</span>
              <span class="m-text">酒杯 * 9 個</span>
            </div>
          </div>
        </div>

        <!-- 12:50 開席用餐 -->
        <div class="t-card">
          <div class="t-top">
            <span class="t-time">12:50</span>
            <span class="t-act">開席 · 享用佳餚</span>
          </div>
          <div class="t-body">
            新人與雙方主婚人入席主桌，全場賓客正式享用阿勇家豐盛宴席。
          </div>
          <div class="t-meta-box">
            <div class="meta-row">
              <span class="m-label media">影音播放</span>
              <span class="m-text">用餐音樂 ＋ 婚紗照輪播</span>
            </div>
          </div>
        </div>

        <!-- 12:55-13:00 播放成長影片 -->
        <div class="t-card">
          <div class="t-top">
            <span class="t-time">12:55 - 13:00</span>
            <span class="t-act">播放成長故事影片</span>
          </div>
          <div class="t-body">
            全場燈光調暗，播放新人成長故事影片（約 6:15）。
          </div>
          <div class="t-meta-box">
            <div class="meta-row">
              <span class="m-label media">影音播放</span>
              <span class="m-text">影片內建音樂</span>
            </div>
          </div>
        </div>

        <!-- 13:00-13:25 新娘換裝 -->
        <div class="t-card">
          <div class="t-top">
            <span class="t-time">13:00 - 13:25</span>
            <span class="t-act">新娘換裝（二進造型）</span>
          </div>
          <div class="t-body">
            新人一同回新娘休息室換裝，新秘老師進行二進妝髮造型。
          </div>
          <div class="t-meta-box">
            <div class="meta-row">
              <span class="m-label media">影音播放</span>
              <span class="m-text">用餐音樂 ＋ 婚紗照輪播</span>
            </div>
          </div>
        </div>

        <!-- 13:25-13:30 第二次進場 -->
        <div class="t-card highlight">
          <div class="t-top">
            <span class="t-time">13:25 - 13:30</span>
            <span class="t-act">第二次進場</span>
          </div>
          <div class="t-body">
            大門開啟，新人一同牽手進場，向熱情賓客揮手致意後步上舞台。
          </div>
          <div class="t-meta-box">
            <div class="meta-row">
              <span class="m-label media">影音播放</span>
              <span class="m-text">流程 8</span>
            </div>
          </div>
        </div>

        <!-- 13:30-13:50 婚禮活動 -->
        <div class="t-card highlight">
          <div class="t-top">
            <span class="t-time">13:30 - 13:50</span>
            <span class="t-act">婚禮趣味互動活動</span>
          </div>
          <div class="t-body">
            <!-- 活動 1 -->
            <div class="sub-section">
              <div class="sub-sec-title">🏆 活動一：【Dresscode 大賞頒獎】</div>
              <div>Amy 現場統計迎賓時賓客之票選貼紙（臉部貼紙），前三位得票最多者上台領獎：</div>
              <ul class="step-list" style="margin-top:6px;">
                <li>🥇 <b>冠軍：</b>3D 立體拼裝書</li>
                <li>🥈 <b>亞軍：</b>教堂甜拼圖</li>
                <li>🥉 <b>季軍：</b>45cm 慵懶維尼熊</li>
              </ul>
            </div>

            <!-- 活動 2 -->
            <div class="sub-section">
              <div class="sub-sec-title">🎯 活動二：【全場之最】趣味挑戰</div>
              <div>新人至主桌前出題，符合條件之賓客至紅毯走道集合，新人核實後頒發<b>禮券紅包</b>：</div>
              <ol class="step-list" style="margin-top:6px;">
                <li>🔋 手機電量最高的</li>
                <li>👟 今日步數最高的</li>
                <li>📱 最早發限動的</li>
                <li>🌟 臉書最多追蹤數的</li>
                <li>✈️ 最遠道而來的朋友</li>
                <li>🎂 最有緣分壽星</li>
              </ol>
            </div>
          </div>
          <div class="t-meta-box">
            <div class="meta-row">
              <span class="m-label media">影音播放</span>
              <span class="m-text">流程 9 - 12</span>
            </div>
            <div class="meta-row">
              <span class="m-label couple">新人備品</span>
              <span class="m-text">投票貼紙、Dresscode前三名禮物、全場之最禮券紅包*6</span>
            </div>
          </div>
        </div>

        <!-- 13:50-14:05 逐桌敬酒 -->
        <div class="t-card">
          <div class="t-top">
            <span class="t-time">13:50 - 14:05</span>
            <span class="t-act">逐桌敬酒致謝</span>
          </div>
          <div class="t-body">
            新人與雙方主婚人逐桌敬酒，感謝親朋好友遠道而來的祝福。
          </div>
          <div class="t-meta-box">
            <div class="meta-row">
              <span class="m-label venue">會場備</span>
              <span class="m-text">敬酒杯 * 6 個</span>
            </div>
          </div>
        </div>

        <!-- 14:05-14:30 新娘換裝 / 男方離席 -->
        <div class="t-card highlight">
          <div class="t-top">
            <span class="t-time">14:05 - 14:30</span>
            <span class="t-act">送客換裝 ＆ 男方見魚離席</span>
          </div>
          <div class="t-body">
            <ul class="step-list">
              <li><b>新娘送客換裝：</b>新娘回新娘房換穿第三套送客禮服與補妝。</li>
              <li><b>男方見魚離席習俗：</b>出魚料理時，Amy 提醒男方主家見魚離席。新郎媽媽給予壓桌錢紅包。男方至會場外繞一圈散步後，再回宴會廳繼續用餐。</li>
            </ul>
            <div class="notice-star">★ 壓桌錢負責收回人：文魚（伴娘）</div>
          </div>
          <div class="t-meta-box">
            <div class="meta-row">
              <span class="m-label media">影音播放</span>
              <span class="m-text">用餐音樂 ＋ 生活照輪播</span>
            </div>
            <div class="meta-row">
              <span class="m-label couple">新人備</span>
              <span class="m-text">壓桌錢紅包</span>
            </div>
          </div>
        </div>

        <!-- 14:30 送客 -->
        <div class="t-card highlight">
          <div class="t-top">
            <span class="t-time">14:30</span>
            <span class="t-act">歡送賓客 · 拍照合影</span>
          </div>
          <div class="t-body">
            Amy 宣布喜宴圓滿禮成，邀請嘉賓至背板送客區與新人開心合影、領取喜糖。
          </div>
          <div class="t-meta-box">
            <div class="meta-row">
              <span class="m-label media">影音播放</span>
              <span class="m-text">送客音樂</span>
            </div>
            <div class="meta-row">
              <span class="m-label couple">新人備</span>
              <span class="m-text">乖乖 ＆ 巧克力喜糖</span>
            </div>
            <div class="meta-row">
              <span class="m-label venue">會場備</span>
              <span class="m-text">喜糖提籃</span>
            </div>
          </div>
        </div>
      </div>
    </div>

    <!-- ==================== TAB 3: 備品與人員 ==================== -->
    <div id="tab-props" class="tab-pane">
      <div class="pane-header">
        <h2><span>📋</span> 備品準備 ＆ 人員分工速查表</h2>
        <span class="badge">ITEMS &amp; ROLES</span>
      </div>

      <div class="checklist-grid">
        <!-- 新人準備物品 (儀式) -->
        <div class="cl-box">
          <div class="cl-title">
            <span>🎁 新人備品 · 文定六禮</span>
            <span class="cl-tag">聘禮桌擺放</span>
          </div>
          <ul class="cl-items">
            <li><span class="cl-dot">✦</span>秘覓喜餅 * 24 盒</li>
            <li><span class="cl-dot">✦</span>日禾春喜餅 * 24 盒</li>
            <li><span class="cl-dot">✦</span>四色喜糖 * 2 組</li>
            <li><span class="cl-dot">✦</span>香燭禮炮 * 2 組</li>
            <li><span class="cl-dot">✦</span>男方頭尾禮紅包、女方頭尾禮紅包</li>
            <li><span class="cl-dot">✦</span>男方金飾、女方金飾盒</li>
            <li><span class="cl-dot">✦</span>小聘（現金）</li>
            <li><span class="cl-dot">✦</span>木盛盒 * 1 個</li>
            <li><span class="cl-dot">✦</span>男方長輩喝茶紅包 * 6 包</li>
            <li><span class="cl-dot">✦</span>儀式甜湯 1 碗</li>
            <li><span class="cl-dot">✦</span>交換戒指（新娘金+銅戒、新郎金戒）</li>
          </ul>
        </div>

        <!-- 新人準備物品 (午宴) -->
        <div class="cl-box">
          <div class="cl-title">
            <span>🎉 新人備品 · 午宴活動</span>
            <span class="cl-tag">宴會廳</span>
          </div>
          <ul class="cl-items">
            <li><span class="cl-dot">✦</span>新郎胸花 * 1、主婚人胸花 * 4</li>
            <li><span class="cl-dot">✦</span>迎賓票選臉部貼紙</li>
            <li><span class="cl-dot">✦</span>Dresscode 冠軍：3D 立體拼裝書</li>
            <li><span class="cl-dot">✦</span>Dresscode 亞軍：教堂甜拼圖</li>
            <li><span class="cl-dot">✦</span>Dresscode 季軍：45cm 慵懶維尼熊</li>
            <li><span class="cl-dot">✦</span>全場之最 6 題禮券紅包</li>
            <li><span class="cl-dot">✦</span>壓桌錢紅包（給女方代收）</li>
            <li><span class="cl-dot">✦</span>送客喜糖：乖乖 ＆ 巧克力</li>
            <li><span class="cl-dot">✦</span>男方帶回喜餅：中西各 12 盒預留新娘房</li>
          </ul>
        </div>

        <!-- 會場提供物品 -->
        <div class="cl-box">
          <div class="cl-title">
            <span>🏛️ 會場提供備品</span>
            <span class="cl-tag">阿勇家餐廳</span>
          </div>
          <ul class="cl-items">
            <li><span class="cl-dot">✦</span>聘禮桌 * 1-2 張</li>
            <li><span class="cl-dot">✦</span>高椅 1 張 ＆ 矮腳凳 1 個（踩凳添妝）</li>
            <li><span class="cl-dot">✦</span>長輩喝茶椅 * 6 張</li>
            <li><span class="cl-dot">✦</span>奉茶茶盤 1 個、茶杯 6 個、溫甜茶</li>
            <li><span class="cl-dot">✦</span>舞台致詞無線麥克風 * 1</li>
            <li><span class="cl-dot">✦</span>台上舉杯酒杯 * 9 個</li>
            <li><span class="cl-dot">✦</span>逐桌敬酒酒杯 * 6 個</li>
            <li><span class="cl-dot">✦</span>送客喜糖提籃</li>
          </ul>
        </div>

        <!-- 關鍵人員名冊 -->
        <div class="cl-box">
          <div class="cl-title">
            <span>👥 關鍵工作人員名冊</span>
            <span class="cl-tag">當日職責</span>
          </div>
          <ul class="cl-items">
            <li><span class="cl-dot">✦</span><b>主持人：</b>Amy（筆電+音控掌控、時程主持）</li>
            <li><span class="cl-dot">✦</span><b>女方好命婆：</b>二姨 (郭乃萍)（牽引、奉茶、扶椅）</li>
            <li><span class="cl-dot">✦</span><b>男方媒人婆：</b>阿珠阿姨</li>
            <li><span class="cl-dot">✦</span><b>男方喝茶長輩：</b>爸爸、媽媽、阿公、堂伯父、叔叔、新郎</li>
            <li><span class="cl-dot">✦</span><b>代收紅包/壓桌錢：</b>文魚（伴娘）</li>
            <li><span class="cl-dot">✦</span><b>伴郎組：</b>Ollie（趙銘輝）、2千（劉良謙）</li>
            <li><span class="cl-dot">✦</span><b>伴娘組：</b>文魚（張文瑜）、Linda（李佳諭）</li>
            <li><span class="cl-dot">✦</span><b>新秘造型：</b>妃妃</li>
            <li><span class="cl-dot">✦</span><b>婚禮攝影：</b>竺竺 ＆ 萊玥</li>
          </ul>
        </div>
      </div>
    </div>

    <p class="foot-note">* 流程時間僅供參考，當日實際時程依現場狀況彈性微調</p>

    <footer>
      BARRY <span class="glyph">&#10022;</span> WINNIE <span class="glyph">&#10022;</span> 幸福登機門 · TAINAN 10&middot;11
    </footer>
  </div>

  <script>
    function switchTab(tabId) {
      document.querySelectorAll('.tab-btn').forEach(btn => btn.classList.remove('active'));
      document.querySelectorAll('.tab-pane').forEach(pane => pane.classList.remove('active'));
      
      const targetPane = document.getElementById(tabId);
      if (targetPane) {
        targetPane.classList.add('active');
      }
      
      const buttons = document.querySelectorAll('.tab-btn');
      if (tabId === 'tab-ceremony') buttons[0].classList.add('active');
      else if (tabId === 'tab-banquet') buttons[1].classList.add('active');
      else if (tabId === 'tab-props') buttons[2].classList.add('active');

      // Scroll smoothly back to top of tabs if scrolled down
      const tabsBar = document.querySelector('.tabs-bar');
      if (tabsBar && tabsBar.getBoundingClientRect().top < 0) {
        tabsBar.scrollIntoView({ behavior: 'smooth' });
      }
    }
  </script>
</body>
</html>
"""

def main():
    with open("outputs/html/訂婚與午宴當天流程表.html", "w", encoding="utf-8") as f:
        f.write(HTML)
    with open("docs/schedule.html", "w", encoding="utf-8") as f:
        f.write(HTML)
    print("Schedule generated successfully:")
    print(" - outputs/html/訂婚與午宴當天流程表.html")
    print(" - docs/schedule.html")

if __name__ == "__main__":
    main()
