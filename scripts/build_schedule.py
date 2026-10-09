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
  <meta name="description" content="羅聖明 ＆ 戴婉錡 2026.10.11 台南阿勇家漂亮議會廳清晨梳化、文定儀式與午宴流程表、影音流程、備品與負責人員清單。">
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
      font-size: 24px;
      margin: 0 0 6px;
      color: var(--wine);
      letter-spacing: .08em;
      font-weight: 900;
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
      grid-template-columns: repeat(4, 1fr);
      gap: 5px;
      background: var(--card-bg);
      border: 1px solid var(--border);
      padding: 5px;
      border-radius: 14px;
      margin-bottom: 18px;
      box-shadow: 0 3px 12px rgba(0,0,0,0.04);
      position: sticky;
      top: 10px;
      z-index: 100;
    }
    .tab-btn {
      font-family: inherit;
      font-size: 13px;
      font-weight: 700;
      color: var(--gray-ink);
      background: transparent;
      border: none;
      border-radius: 10px;
      padding: 9px 2px;
      cursor: pointer;
      transition: all .2s;
      text-align: center;
      white-space: nowrap;
    }
    @media (max-width: 360px) {
      .tab-btn {
        font-size: 11.5px;
        padding: 7px 1px;
      }
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

    /* Party Section Divider & Badges */
    .party-title {
      display: flex;
      align-items: center;
      gap: 8px;
      font-size: 15px;
      font-weight: 700;
      color: var(--wine);
      margin: 20px 0 12px;
      padding-bottom: 6px;
      border-bottom: 1.5px solid var(--gold);
    }
    .party-badge {
      font-size: 11px;
      font-weight: 700;
      padding: 2px 8px;
      border-radius: 6px;
      letter-spacing: .05em;
    }
    .party-badge.bride {
      background: #FCE8E6;
      color: #C5221F;
      border: 1px solid #F5C2C7;
    }
    .party-badge.groom {
      background: #E8F0FE;
      color: #1A73E8;
      border: 1px solid #BED7FB;
    }

    /* Location Card */
    .loc-card {
      background: #FFFDF8;
      border: 1.5px solid var(--gold);
      border-radius: 12px;
      padding: 14px 16px;
      margin-bottom: 14px;
      box-shadow: 0 3px 10px rgba(201, 162, 75, 0.12);
    }
    .loc-head {
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 8px;
      margin-bottom: 6px;
    }
    .loc-title {
      font-size: 15px;
      font-weight: 700;
      color: var(--wine);
      display: flex;
      align-items: center;
      gap: 6px;
    }
    .loc-address {
      font-size: 14px;
      font-weight: 600;
      color: #2B1D12;
      margin: 6px 0 10px;
      letter-spacing: .02em;
      line-height: 1.5;
    }
    .loc-action-bar {
      display: flex;
      flex-wrap: wrap;
      align-items: center;
      gap: 10px;
    }
    .loc-btn {
      display: inline-flex;
      align-items: center;
      gap: 5px;
      font-size: 12.5px;
      font-weight: 700;
      color: #fff;
      background: #1A73E8;
      text-decoration: none;
      padding: 6px 14px;
      border-radius: 6px;
      box-shadow: 0 2px 4px rgba(26, 115, 232, 0.25);
      transition: all .15s;
    }
    .loc-btn:hover, .loc-btn:active {
      background: #1557B0;
      transform: translateY(-1px);
    }
    .loc-vendor-note {
      font-size: 12px;
      color: var(--gray-ink);
    }
    .loc-vendor-note b {
      color: var(--wine);
    }

    /* Quick Info Banner in Tab 2 */
    .pre-arrival-banner {
      background: #FFFBF2;
      border: 1.5px solid var(--gold);
      border-radius: 12px;
      padding: 12px 14px;
      margin-bottom: 16px;
      display: flex;
      align-items: center;
      gap: 12px;
      cursor: pointer;
      box-shadow: 0 2px 8px rgba(0,0,0,0.03);
      transition: all .15s;
    }
    .pre-arrival-banner:hover {
      background: #FAF3E6;
      border-color: var(--gold-d);
      transform: translateY(-1px);
    }
    .pab-icon {
      font-size: 24px;
      flex-shrink: 0;
    }
    .pab-content {
      flex: 1;
    }
    .pab-title {
      font-size: 13.5px;
      font-weight: 700;
      color: var(--wine);
      margin-bottom: 3px;
    }
    .pab-desc {
      font-size: 12px;
      color: var(--gray-ink);
      line-height: 1.45;
    }
    .pab-arrow {
      font-size: 12px;
      font-weight: 700;
      color: var(--gold-d);
      background: #FAF0D8;
      border: 1px solid var(--gold);
      padding: 4px 10px;
      border-radius: 999px;
      white-space: nowrap;
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

    /* Next Step Button */
    .next-pane-btn {
      display: block;
      width: 100%;
      text-align: center;
      background: linear-gradient(135deg, #FAF3E6 0%, #F5EADA 100%);
      border: 1.5px solid var(--gold);
      border-radius: 12px;
      padding: 14px 16px;
      margin: 24px 0 10px;
      font-size: 14px;
      font-weight: 700;
      color: var(--wine);
      cursor: pointer;
      box-shadow: 0 4px 12px rgba(110, 20, 20, 0.06);
      transition: all .2s;
    }
    .next-pane-btn:hover, .next-pane-btn:active {
      background: var(--wine);
      color: #fff;
      transform: translateY(-2px);
      box-shadow: 0 6px 18px rgba(110, 20, 20, 0.2);
    }

    /* Tab 4: Grid Checklist */
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
      .top-nav, .tabs-bar, .next-pane-btn, .foot-note, footer, .pre-arrival-banner { display: none !important; }
      .tab-pane { display: block !important; page-break-after: always; }
      .t-card, .cl-box, .loc-card { box-shadow: none; border: 1px solid #ccc; break-inside: avoid; }
    }
  </style>
</head>
<body>
  <div class="wrap">
    <div class="top-nav">
      <div style="display:flex; align-items:center; gap:8px; flex-wrap:wrap;">
        <a href="index.html" class="back-btn">‹ 返回工作台首頁</a>
        <a href="https://docs.google.com/spreadsheets/d/1TasCO9KSlpflyi-poXNur0p5EYWLFvtHGZI3R7eKsYg/edit?gid=848591360#gid=848591360" target="_blank" rel="noopener" class="back-btn" style="color:var(--wine); font-weight:700; background:var(--cream); border-color:var(--gold);">📊 雲端試算表 ↗</a>
      </div>
      <span class="update-tag">VER 2026/10/9</span>
    </div>

    <header>
      <div class="eyebrow">Engagement &amp; Banquet Schedule</div>
      <h1>羅聖明 <span class="heart">♥</span> 戴婉錡</h1>
      <p class="meta-loc">2026.10.11 (日) 阿勇家餐飲事業 - 漂亮議會廳</p>
      <div class="vendors-pill">
        <span class="vp-item"><b>主持人</b> Amy 筆電+音控</span>
        <span class="vp-item"><b>禮服</b> 1 文定 + 2 晚</span>
        <span class="vp-item"><b>新秘</b> 妃妃</span>
        <span class="vp-item"><b>婚攝</b> 竺竺</span>
        <span class="vp-item"><b>錄影</b> 萊玥</span>
        <span class="vp-item"><b>佈置</b> 法爾</span>
      </div>
    </header>

    <!-- Navigation Tabs -->
    <div class="tabs-bar">
      <button class="tab-btn active" data-tab="tab-before" onclick="switchTab('tab-before')">🌅 抵達前</button>
      <button class="tab-btn" data-tab="tab-ceremony" onclick="switchTab('tab-ceremony')">💍 文定儀式</button>
      <button class="tab-btn" data-tab="tab-banquet" onclick="switchTab('tab-banquet')">🥂 午宴流程</button>
      <button class="tab-btn" data-tab="tab-props" onclick="switchTab('tab-props')">📋 備品人員</button>
    </div>

    <!-- ==================== TAB 1: 抵達前梳化＆出發 ==================== -->
    <div id="tab-before" class="tab-pane active">
      <div class="pane-header">
        <h2><span>🌅</span> 清晨 · 抵達前梳化 ＆ 移動出發</h2>
        <span class="badge">02:50 - 09:50</span>
      </div>

      <!-- 女方專區 -->
      <div class="party-title">
        <span>👰 女方時程 · 永康新娘家 ➔ 漂亮議會廳</span>
        <span class="party-badge bride">新娘＆女方親友</span>
      </div>

      <!-- 開妝地點卡片 -->
      <div class="loc-card">
        <div class="loc-head">
          <span class="loc-title">🏠 開妝地點 · 新娘家</span>
          <span class="party-badge bride">女方集合點</span>
        </div>
        <div class="loc-address">台南市永康區廣興街38巷25弄31號</div>
        <div class="loc-action-bar">
          <a href="https://maps.google.com/?q=台南市永康區廣興街38巷25弄31號" target="_blank" rel="noopener" class="loc-btn">
            <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M12 2C8.13 2 5 5.13 5 9c0 5.25 7 13 7 13s7-7.75 7-13c0-3.87-3.13-7-7-7z"/><circle cx="12" cy="9" r="2.5"/></svg>
            開啟 Google 地圖導航 ↗
          </a>
          <span class="loc-vendor-note">新秘造型：<b>妃妃</b></span>
        </div>
      </div>

      <div class="timeline">
        <!-- 06:15 -->
        <div class="t-card">
          <div class="t-top">
            <span class="t-time">06:15</span>
            <span class="t-act">新秘抵達 · Setting</span>
          </div>
          <div class="t-body">
            <b>新秘妃妃抵達新娘家。</b>
            梳化工具擺設定位、化妝燈鏡就位，進行妝前保養打底準備。
          </div>
          <div class="t-meta-box">
            <div class="meta-row">
              <span class="m-label staff">人員</span>
              <span class="m-text">新秘妃妃、新娘</span>
            </div>
            <div class="meta-row">
              <span class="m-label couple">地點</span>
              <span class="m-text">永康新娘家（台南市永康區廣興街38巷25弄31號）</span>
            </div>
          </div>
        </div>

        <!-- 06:30 - 09:15 -->
        <div class="t-card highlight">
          <div class="t-top">
            <span class="t-time">06:30 - 09:15</span>
            <span class="t-act">新娘妝髮造型</span>
          </div>
          <div class="t-body">
            <b>新娘完整妝髮梳化（文定第一套新中式造型）。</b>
            基礎保養、精緻底妝、眼妝修容、編髮造型。完妝後換穿文定禮服。
            <div class="notice-star">★ 完妝時間預留充足，確保妝容服貼無瑕，穿著開扣或拉鍊衣物方便更換禮服。</div>
          </div>
          <div class="t-meta-box">
            <div class="meta-row">
              <span class="m-label staff">造型</span>
              <span class="m-text">文定第 1 套造型（新中式紅色禮服）</span>
            </div>
          </div>
        </div>

        <!-- 07:00 - 09:00 -->
        <div class="t-card">
          <div class="t-top">
            <span class="t-time">07:00 - 09:00</span>
            <span class="t-act">新娘媽媽妝髮</span>
          </div>
          <div class="t-body">
            <b>新娘媽媽妝髮梳化。</b>
            媽媽粉底、彩妝及高雅髮型吹整，著宴會主婚人禮服。
          </div>
          <div class="t-meta-box">
            <div class="meta-row">
              <span class="m-label staff">人員</span>
              <span class="m-text">新娘媽媽（主婚人）</span>
            </div>
          </div>
        </div>

        <!-- 09:30 -->
        <div class="t-card highlight">
          <div class="t-top">
            <span class="t-time">09:30</span>
            <span class="t-act">移動至宴會廳</span>
          </div>
          <div class="t-body">
            <b>女方由新娘家出發，移動前往阿勇家漂亮議會廳。</b>
            女方親友、伴娘（文魚、Linda）攜帶隨身急救包、禮服及物品出發。
          </div>
          <div class="t-meta-box">
            <div class="meta-row">
              <span class="m-label couple">隨身備</span>
              <span class="m-text">新娘急救包、備用鞋、合約尾款、婚鞋、飾品盒</span>
            </div>
          </div>
        </div>

        <!-- 09:50 -->
        <div class="t-card highlight">
          <div class="t-top">
            <span class="t-time">09:50</span>
            <span class="t-act">進休息室 · 上頭飾調整妝髮</span>
          </div>
          <div class="t-body">
            <b>新娘進漂亮議會廳新娘休息室。</b>
            新秘妃妃協助佩戴文定精緻金屬髮飾、耳環，進行最後補妝與細節調整，準備迎接 10:25 文定儀式入座！
            <div class="notice-star">★ 10:00 親友陸續抵達會場，10:25 長輩入座奉茶區，好命婆二姨準備引導新娘。</div>
          </div>
          <div class="t-meta-box">
            <div class="meta-row">
              <span class="m-label venue">地點</span>
              <span class="m-text">漂亮議會廳 · 新娘休息室</span>
            </div>
            <div class="meta-row">
              <span class="m-label staff">人員</span>
              <span class="m-text">新娘、新秘妃妃、女方好命婆二姨 (郭乃萍)</span>
            </div>
          </div>
        </div>
      </div>

      <!-- 男方專區 -->
      <div class="party-title" style="margin-top: 30px;">
        <span>🤵 男方時程 · 男方開妝 ➔ 遊覽車隊發車</span>
        <span class="party-badge groom">新郎＆男方親友</span>
      </div>

      <div class="timeline">
        <!-- 02:50 -->
        <div class="t-card">
          <div class="t-top">
            <span class="t-time">02:50</span>
            <span class="t-act">化妝師抵達</span>
          </div>
          <div class="t-body">
            <b>化妝師抵達男方處所。</b>
            整理化妝用品與工具，確認新郎及男方長輩梳化次序與空間。
          </div>
          <div class="t-meta-box">
            <div class="meta-row">
              <span class="m-label staff">人員</span>
              <span class="m-text">男方化妝師、新郎</span>
            </div>
          </div>
        </div>

        <!-- 03:00 -->
        <div class="t-card highlight">
          <div class="t-top">
            <span class="t-time">03:00</span>
            <span class="t-act">男方開妝</span>
          </div>
          <div class="t-body">
            <b>新郎及男方親友開妝。</b>
            新郎修容、髮型抓整吹定、西裝整裝；男方長輩梳化打理。
          </div>
          <div class="t-meta-box">
            <div class="meta-row">
              <span class="m-label staff">對象</span>
              <span class="m-text">新郎 Barry、男方主婚人長輩</span>
            </div>
          </div>
        </div>

        <!-- 05:00 -->
        <div class="t-card highlight">
          <div class="t-top">
            <span class="t-time">05:00</span>
            <span class="t-act">遊覽車準時發車</span>
          </div>
          <div class="t-body">
            <b>男方親友團集合，遊覽車準時發車南下台南！</b>
            清點隨車聘禮與貴重物品，出發前往「阿勇家漂亮議會廳」。
            <div class="notice-star">★ 隨車物資提醒：六禮聘禮（喜餅各24盒、四色喜糖、香燭禮炮、小聘現金、金飾盒、木盛盒）、男方長輩喝茶紅包（6包）。</div>
          </div>
          <div class="t-meta-box">
            <div class="meta-row">
              <span class="m-label couple">重要物資</span>
              <span class="m-text">文定六禮聘禮、金飾盒、小聘現金、喝茶紅包*6</span>
            </div>
          </div>
        </div>

        <!-- 09:30 預計抵達 -->
        <div class="t-card">
          <div class="t-top">
            <span class="t-time">09:30</span>
            <span class="t-act">抵達宴會廳 · 擺聘</span>
          </div>
          <div class="t-body">
            <b>遊覽車隊抵達台南漂亮議會廳。</b>
            協助卸載六禮聘禮，由主持人 Amy 引導擺放聘禮桌。男方長輩稍作休息，等待 10:25 儀式就位。
          </div>
          <div class="t-meta-box">
            <div class="meta-row">
              <span class="m-label venue">地點</span>
              <span class="m-text">阿勇家餐飲事業 - 漂亮議會廳（台南）</span>
            </div>
          </div>
        </div>
      </div>

      <button type="button" class="next-pane-btn" onclick="switchTab('tab-ceremony')">
        接續下一步：💍 查看早晨文定儀式流程 (09:30–11:00) ›
      </button>
    </div>

    <!-- ==================== TAB 2: 文定儀式 ==================== -->
    <div id="tab-ceremony" class="tab-pane">
      <div class="pane-header">
        <h2><span>💍</span> 早晨 · 文定儀式流程表</h2>
        <span class="badge">09:30 - 11:00</span>
      </div>

      <!-- Quick Link to Pre-arrival -->
      <div class="pre-arrival-banner" onclick="switchTab('tab-before')">
        <div class="pab-icon">🌅</div>
        <div class="pab-content">
          <div class="pab-title">抵達前清晨梳化＆出發速覽</div>
          <div class="pab-desc">男方：02:50 化妝師抵達 · 03:00 開妝 · 05:00 遊覽車發車<br>女方：06:15 新秘抵達娘家 · 06:30-09:15 新娘妝髮 · 09:30 移動 · 09:50 休息室上頭飾</div>
        </div>
        <span class="pab-arrow">完整流程 ›</span>
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

            <!-- 坐高椅矮凳、戴戒 -->
            <div class="sub-section">
              <div class="sub-sec-title">③ 坐高椅踩矮凳 · 戴戒</div>
              <ol class="step-list">
                <li>新娘坐高椅、踩矮凳（坐定後不可隨意亂動）。</li>
                <li>新郎為新娘戴戒指（<b>金戒＋銅戒繫紅線</b>，戴在右手中指）。</li>
                <li>新娘為新郎戴戒指（<b>金戒指</b>，戴在左手中指）。</li>
              </ol>
            </div>

            <!-- 見面禮、添妝 -->
            <div class="sub-section">
              <div class="sub-sec-title">④ 見面禮（戴金飾）＆ 長輩添妝</div>
              <ol class="step-list">
                <li><b>婆婆</b>為新娘戴項鍊、手鍊、耳環。</li>
                <li><b>岳母</b>為新郎戴項鍊。</li>
                <li><b>外婆</b>為新娘添妝項鍊。</li>
                <li><b>阿嬤</b>為新娘添妝項鍊。</li>
              </ol>
            </div>

            <!-- 喝甜湯 -->
            <div class="sub-section">
              <div class="sub-sec-title">⑤ 喝甜湯</div>
              <div style="font-size: 13.5px; color: var(--wine); padding: 4px 0;">
                新人一同喝甜湯，象徵圓圓滿滿、甜甜蜜蜜。
              </div>
            </div>

            <!-- 拍合照 -->
            <div class="sub-section">
              <div class="sub-sec-title">⑥ 禮成 · 拍大合照</div>
              <div style="font-size: 13.5px; color: var(--wine); padding: 4px 0;">
                雙方全體長輩親友大合照留念。
              </div>
            </div>
          </div>
          <div class="t-meta-box">
            <div class="meta-row">
              <span class="m-label staff">好命婆</span>
              <span class="m-text">二姨 (郭乃萍)（牽引、奉茶、扶椅）</span>
            </div>
            <div class="meta-row">
              <span class="m-label staff">媒人婆</span>
              <span class="m-text">阿珠阿姨（介紹長輩）</span>
            </div>
            <div class="meta-row">
              <span class="m-label staff">紅包代收</span>
              <span class="m-text">文魚（伴娘）</span>
            </div>
          </div>
        </div>

        <!-- 11:00 回休息室 -->
        <div class="t-card">
          <div class="t-top">
            <span class="t-time">11:00</span>
            <span class="t-act">禮成 · 收拾整理</span>
          </div>
          <div class="t-body">
            <b>儀式圓滿完成，新人回休息室收拾。</b>
            <div class="notice-star">★ 提醒：預留中、西喜餅各 12 盒於新娘房（男方帶回）。</div>
          </div>
          <div class="t-meta-box">
            <div class="meta-row">
              <span class="m-label couple">喜餅回禮</span>
              <span class="m-text">中式秘覓 12 盒 ＋ 西式日禾春 12 盒（男方回禮帶回）</span>
            </div>
          </div>
        </div>
      </div>

      <button type="button" class="next-pane-btn" onclick="switchTab('tab-banquet')">
        接續下一步：🥂 查看中午午宴宴客流程 (11:00 起) ›
      </button>
    </div>

    <!-- ==================== TAB 3: 午宴流程 ==================== -->
    <div id="tab-banquet" class="tab-pane">
      <div class="pane-header">
        <h2><span>🥂</span> 中午 · 午宴流程表</h2>
        <span class="badge">11:00 - 14:30+</span>
      </div>

      <div class="timeline">
        <!-- 11:00 彩排 -->
        <div class="t-card">
          <div class="t-top">
            <span class="t-time">11:00</span>
            <span class="t-act">進場總彩排</span>
          </div>
          <div class="t-body">
            <b>進場總彩排：</b>新人、儐相、雙方主婚人走位彩排，熟悉音樂進場點與致詞站位。
          </div>
          <div class="t-meta-box">
            <div class="meta-row">
              <span class="m-label staff">出席人員</span>
              <span class="m-text">新人、儐相四人（伴郎 Ollie/2千、伴娘 文魚/Linda）、雙方主婚人、主持人 Amy</span>
            </div>
          </div>
        </div>

        <!-- 11:30 迎賓 -->
        <div class="t-card">
          <div class="t-top">
            <span class="t-time">11:30</span>
            <span class="t-act">賓客迎賓 · 貼紙活動</span>
          </div>
          <div class="t-body">
            <b>迎賓開始：</b>播放迎賓音樂、輪播婚紗照影片。
            賓客於禮金桌簽到、領取喜餅，並於臉部貼上 <b>Dresscode 貼紙</b>準備稍後互動！
          </div>
          <div class="t-meta-box">
            <div class="meta-row">
              <span class="m-label media">影音</span>
              <span class="m-text">迎賓音樂 ＋ 婚紗輪播影片（筆電：Amy）</span>
            </div>
            <div class="meta-row">
              <span class="m-label couple">新人備</span>
              <span class="m-text">Dresscode 臉部貼紙（接待禮金桌發放）</span>
            </div>
          </div>
        </div>

        <!-- 12:30 開場影片 -->
        <div class="t-card highlight">
          <div class="t-top">
            <span class="t-time">12:30</span>
            <span class="t-act">播開場影片 (1:35)</span>
          </div>
          <div class="t-body">
            <b>播放開場影片（長度 1 分 35 秒）。</b>
            影片播畢後<b>直接開大門</b>準備第一次進場！
          </div>
          <div class="t-meta-box">
            <div class="meta-row">
              <span class="m-label media">影音</span>
              <span class="m-text">開場影片（1:35，播畢直接開大門）</span>
            </div>
          </div>
        </div>

        <!-- 12:35 一進 -->
        <div class="t-card highlight">
          <div class="t-top">
            <span class="t-time">12:35</span>
            <span class="t-act">第一次進場</span>
          </div>
          <div class="t-body">
            <b>隆重進場順序：</b>
            <ol class="step-list" style="margin-top: 6px;">
              <li><b>儐相四人一同走：</b>伴郎 Ollie &amp; 伴郎 2千 / 伴娘 文魚 &amp; 伴娘 Linda 【流程1】</li>
              <li><b>女方主婚人入場：</b>爸爸、媽媽 【流程2】</li>
              <li><b>男方主婚人入場：</b>爸爸、媽媽 【流程3】</li>
              <li><b>新郎入場：</b>至紅毯中段定位迎接 【流程4】</li>
              <li><b>新娘入場：</b>（無捧花）步入紅毯，走向新郎 【流程5】</li>
            </ol>
          </div>
          <div class="t-meta-box">
            <div class="meta-row">
              <span class="m-label media">影音</span>
              <span class="m-text">一進音樂（流程 1~5）</span>
            </div>
            <div class="meta-row">
              <span class="m-label couple">胸花準備</span>
              <span class="m-text">新郎胸花*1、雙方主婚人胸花*4</span>
            </div>
          </div>
        </div>

        <!-- 12:40 致詞 -->
        <div class="t-card">
          <div class="t-top">
            <span class="t-time">12:40</span>
            <span class="t-act">主婚人致詞</span>
          </div>
          <div class="t-body">
            <b>雙方長輩登台致詞：</b>
            致詞順序：<b>新郎爸爸 → 新娘媽媽 → 新娘爸爸</b>。
            <div class="notice-star">★ 致詞時請雙方阿公、阿嬤一同受邀上台！</div>
          </div>
          <div class="t-meta-box">
            <div class="meta-row">
              <span class="m-label venue">會場備</span>
              <span class="m-text">致詞麥克風*1 【流程6】</span>
            </div>
          </div>
        </div>

        <!-- 12:45 舉杯 -->
        <div class="t-card highlight">
          <div class="t-top">
            <span class="t-time">12:45</span>
            <span class="t-act">全體總敬酒舉杯</span>
          </div>
          <div class="t-body">
            <b>新人與雙方主婚人長輩於台上向全場賓客舉杯總敬酒！</b>
          </div>
          <div class="t-meta-box">
            <div class="meta-row">
              <span class="m-label venue">會場備</span>
              <span class="m-text">酒杯*9（新人2 + 主婚人4 + 長輩3） 【流程7】</span>
            </div>
          </div>
        </div>

        <!-- 12:50 開席用餐 -->
        <div class="t-card">
          <div class="t-top">
            <span class="t-time">12:50</span>
            <span class="t-act">開席用餐</span>
          </div>
          <div class="t-body">
            <b>開席！</b>長輩新人回主桌用餐，播放溫馨背景音樂。
          </div>
          <div class="t-meta-box">
            <div class="meta-row">
              <span class="m-label media">影音</span>
              <span class="m-text">用餐背景音樂</span>
            </div>
          </div>
        </div>

        <!-- 12:55 成長影片 -->
        <div class="t-card">
          <div class="t-top">
            <span class="t-time">12:55</span>
            <span class="t-act">播成長影片 (6:15)</span>
          </div>
          <div class="t-body">
            <b>播放新人成長愛情交往影片（長度 6 分 15 秒）。</b>
          </div>
          <div class="t-meta-box">
            <div class="meta-row">
              <span class="m-label media">影音</span>
              <span class="m-text">成長影片（6:15，Amy 筆電播映）</span>
            </div>
          </div>
        </div>

        <!-- 13:00 換二進禮服 -->
        <div class="t-card">
          <div class="t-top">
            <span class="t-time">13:00</span>
            <span class="t-act">新娘離席更換二進禮服</span>
          </div>
          <div class="t-body">
            新娘離席回休息室，更換第二套禮服及調整造型髮妝。
          </div>
          <div class="t-meta-box">
            <div class="meta-row">
              <span class="m-label staff">造型</span>
              <span class="m-text">第 2 套晚禮服（二進造型）</span>
            </div>
          </div>
        </div>

        <!-- 13:25 二進 -->
        <div class="t-card highlight">
          <div class="t-top">
            <span class="t-time">13:25</span>
            <span class="t-act">第二次進場</span>
          </div>
          <div class="t-body">
            <b>新人第二次浪漫進場！</b>步入紅毯，走向舞台準備進行現場互動遊戲。
          </div>
          <div class="t-meta-box">
            <div class="meta-row">
              <span class="m-label media">影音</span>
              <span class="m-text">二進進場音樂 【流程8】</span>
            </div>
          </div>
        </div>

        <!-- 13:30 婚禮雙活動 -->
        <div class="t-card highlight">
          <div class="t-top">
            <span class="t-time">13:30</span>
            <span class="t-act">婚禮互動雙活動</span>
          </div>
          <div class="t-body">
            <!-- 活動一 -->
            <div class="sub-section">
              <div class="sub-sec-title">活動 ①【Dresscode 大賞】票選貼紙前三名</div>
              <div style="font-size: 13.5px; color: var(--wine); margin-bottom: 6px;">
                依照賓客臉部 Dresscode 貼紙票選出最佳造型前三名！
              </div>
              <ul class="step-list" style="font-size: 13px;">
                <li><b>冠軍：</b>3D 立體拼裝書</li>
                <li><b>亞軍：</b>教堂甜拼圖</li>
                <li><b>季軍：</b>45cm 慵懶維尼熊</li>
              </ul>
            </div>

            <!-- 活動二 -->
            <div class="sub-section">
              <div class="sub-sec-title">活動 ②【全場之最】趣味挑戰（共 6 題）</div>
              <div style="font-size: 13.5px; color: var(--wine); margin-bottom: 6px;">
                邀請全場賓客互動，符合條件者上台領獎！
              </div>
              <ol class="step-list" style="font-size: 13px;">
                <li>目前手機電量最高的人</li>
                <li>今天走路步數最高的人</li>
                <li>今天最早發限時動態的人</li>
                <li>FB 追蹤人數最多的人</li>
                <li>最遠道而來的賓客</li>
                <li>跟新人最有緣分的壽星</li>
              </ol>
              <div style="font-size: 12.5px; color: #8B1A1A; margin-top: 5px; font-weight: 600;">
                ★ 獎品：禮券紅包*6包
              </div>
            </div>
          </div>
          <div class="t-meta-box">
            <div class="meta-row">
              <span class="m-label media">影音</span>
              <span class="m-text">活動背景音樂 【流程 9~12】</span>
            </div>
            <div class="meta-row">
              <span class="m-label couple">新人備獎品</span>
              <span class="m-text">
                <b>大賞獎品*3：</b>3D立體拼裝書、教堂甜拼圖、45cm維尼熊<br>
                <b>全場之最：</b>禮券紅包*6包
              </span>
            </div>
          </div>
        </div>

        <!-- 13:50 逐桌敬酒 -->
        <div class="t-card">
          <div class="t-top">
            <span class="t-time">13:50</span>
            <span class="t-act">逐桌敬酒</span>
          </div>
          <div class="t-body">
            <b>新人與雙方主婚人逐桌向親友賓客敬酒致謝。</b>
          </div>
          <div class="t-meta-box">
            <div class="meta-row">
              <span class="m-label media">影音</span>
              <span class="m-text">敬酒背景音樂</span>
            </div>
            <div class="meta-row">
              <span class="m-label venue">會場備</span>
              <span class="m-text">敬酒酒杯*6（新人2 + 主婚人4）</span>
            </div>
          </div>
        </div>

        <!-- 14:05 換三進禮服 + 男方離席習俗 -->
        <div class="t-card highlight">
          <div class="t-top">
            <span class="t-time">14:05</span>
            <span class="t-act">換送客禮服 ＆ 男方離席習俗</span>
          </div>
          <div class="t-body">
            <b>新娘離席：</b>更換第三套送客禮服，由新秘妃妃更換亮眼送客造型。
            <div class="sub-section" style="margin-top: 8px;">
              <div class="sub-sec-title">🐟 男方「見魚離席」傳統習俗</div>
              <div style="font-size: 13px; color: var(--gray-ink); line-height: 1.6;">
                出第 7 或 8 道魚料理時，男方主桌及親友依照訂婚習俗「見魚離席」，不說再見默默離席。<br>
                <b>當天安排：男方離席出去走一圈後再回席用餐。</b><br>
                ★ 男方備「壓桌錢紅包」，離席時放置主桌，由<b>女方紅包代收人（文魚）</b>代收。
              </div>
            </div>
          </div>
          <div class="t-meta-box">
            <div class="meta-row">
              <span class="m-label couple">紅包代收</span>
              <span class="m-text">男方壓桌錢紅包（文魚代收）</span>
            </div>
            <div class="meta-row">
              <span class="m-label staff">造型</span>
              <span class="m-text">第 3 套晚禮服（送客造型）</span>
            </div>
          </div>
        </div>

        <!-- 14:30 送客 -->
        <div class="t-card highlight">
          <div class="t-top">
            <span class="t-time">14:30</span>
            <span class="t-act">送客 · 合照留念</span>
          </div>
          <div class="t-body">
            <b>甜蜜送客：</b>新人於送客背板前發放喜糖、喜餅與送客小物，與親友合照留念！
          </div>
          <div class="t-meta-box">
            <div class="meta-row">
              <span class="m-label media">影音</span>
              <span class="m-text">送客歡樂音樂</span>
            </div>
            <div class="meta-row">
              <span class="m-label couple">新人備</span>
              <span class="m-text">乖乖喜糖、巧克力喜糖</span>
            </div>
            <div class="meta-row">
              <span class="m-label venue">會場備</span>
              <span class="m-text">喜糖提籃</span>
            </div>
          </div>
        </div>
      </div>

      <button type="button" class="next-pane-btn" onclick="switchTab('tab-props')">
        接續下一步：📋 查看備品準備與人員分工清單 ›
      </button>
    </div>

    <!-- ==================== TAB 4: 備品與人員分工 ==================== -->
    <div id="tab-props" class="tab-pane">
      <div class="pane-header">
        <h2><span>📋</span> 備品準備 ＆ 人員分工速查表</h2>
        <span class="badge">速查清單</span>
      </div>

      <div class="checklist-grid">
        <!-- 新人準備清單 -->
        <div class="cl-box">
          <div class="cl-title">
            <span>🎁 新人自備備品</span>
            <span class="cl-tag">自備物品</span>
          </div>
          <ul class="cl-items">
            <li><span class="cl-dot">✦</span><b>六禮聘禮：</b>秘覓喜餅*24盒、日禾春喜餅*24盒、四色喜糖*2組、香燭禮炮*2組、頭尾禮紅包、男女金飾、小聘現金、木盛盒*1</li>
            <li><span class="cl-dot">✦</span><b>儀式紅包：</b>男方長輩喝茶紅包*6包、壓桌錢紅包</li>
            <li><span class="cl-dot">✦</span><b>儀式物品：</b>甜湯 1 碗</li>
            <li><span class="cl-dot">✦</span><b>胸花佩戴：</b>新郎胸花*1、主婚人胸花*4</li>
            <li><span class="cl-dot">✦</span><b>迎賓活動：</b>Dresscode 臉部貼紙</li>
            <li><span class="cl-dot">✦</span><b>二進獎品：</b>3D立體拼裝書、教堂甜拼圖、45cm維尼熊</li>
            <li><span class="cl-dot">✦</span><b>活動獎金：</b>禮券紅包*6包</li>
            <li><span class="cl-dot">✦</span><b>送客甜點：</b>乖乖、巧克力</li>
            <li><span class="cl-dot">✦</span><b>隨身用品：</b>新娘急救包、合約尾款、婚鞋</li>
          </ul>
        </div>

        <!-- 餐廳會場備品 -->
        <div class="cl-box">
          <div class="cl-title">
            <span>🏛️ 漂亮議會廳會場提供</span>
            <span class="cl-tag">場地備品</span>
          </div>
          <ul class="cl-items">
            <li><span class="cl-dot">✦</span><b>文定桌位：</b>聘禮桌*1-2張、高矮椅（新娘坐高椅踩矮凳）</li>
            <li><span class="cl-dot">✦</span><b>奉茶器具：</b>喝茶長輩椅*6、茶盤、茶杯、甜茶</li>
            <li><span class="cl-dot">✦</span><b>影音麥克風：</b>致詞麥克風*1支</li>
            <li><span class="cl-dot">✦</span><b>宴席酒杯：</b>舞台總舉杯酒杯*9只、逐桌敬酒酒杯*6只</li>
            <li><span class="cl-dot">✦</span><b>送客用品：</b>喜糖提籃</li>
          </ul>
        </div>

        <!-- 關鍵工作人員名冊 -->
        <div class="cl-box" style="grid-column: 1 / -1;">
          <div class="cl-title">
            <span>👥 關鍵分工人員名冊</span>
            <span class="cl-tag">人員配置</span>
          </div>
          <ul class="cl-items">
            <li><span class="cl-dot">✦</span><b>婚禮主持兼音控：</b>Amy（筆電播映、儀式引導、流程掌控）</li>
            <li><span class="cl-dot">✦</span><b>女方開妝新秘：</b>妃妃（06:15 抵達永康新娘家 setting，新娘＆媽媽梳化）</li>
            <li><span class="cl-dot">✦</span><b>男方開妝化妝師：</b>男方化妝師（02:50 抵達男方開妝）</li>
            <li><span class="cl-dot">✦</span><b>女方好命婆：</b>二姨 (郭乃萍)（牽引、奉茶、扶椅）</li>
            <li><span class="cl-dot">✦</span><b>男方媒人婆：</b>阿珠阿姨</li>
            <li><span class="cl-dot">✦</span><b>男方喝茶長輩：</b>爸爸、媽媽、阿公、堂伯父、叔叔、新郎</li>
            <li><span class="cl-dot">✦</span><b>代收紅包/壓桌錢：</b>文魚（伴娘）</li>
            <li><span class="cl-dot">✦</span><b>伴郎組：</b>Ollie（趙銘輝）、2千（劉良謙）</li>
            <li><span class="cl-dot">✦</span><b>伴娘組：</b>文魚（張文瑜）、Linda（李佳諭）</li>
            <li><span class="cl-dot">✦</span><b>婚禮攝影與錄影：</b>竺竺 ＆ 萊玥</li>
            <li><span class="cl-dot">✦</span><b>會場佈置：</b>法爾佈置</li>
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
      document.querySelectorAll('.tab-btn').forEach(btn => {
        btn.classList.toggle('active', btn.getAttribute('data-tab') === tabId);
      });
      document.querySelectorAll('.tab-pane').forEach(pane => {
        pane.classList.toggle('active', pane.id === tabId);
      });

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
