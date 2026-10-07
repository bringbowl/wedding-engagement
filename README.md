# Barry ♥ Winnie 訂婚專案（Antigravity 版）

這是 Winnie（戴婉錡）＆ Barry（羅聖明）2026.10.11 台南訂婚宴的平面＆資料專案。
所有產出都由 Python 腳本從一份 Google 試算表生成。

## 快速開始（在 Google Antigravity）

1. **開啟專案**：Antigravity → `Open Folder` → 選這個資料夾。
2. **讀交接文件**：先讓 agent 讀 `HANDOFF.md`（完整背景、資料來源、每個產出的生成指令、決策紀錄）。
3. **裝套件**：
   ```bash
   pip install openpyxl pypinyin playwright pymupdf opencv-python pillow numpy
   playwright install chromium
   ```
4. **修路徑**（只需做一次）：叫 agent 把 `scripts/` 裡所有 `/home/claude/` 開頭的絕對路徑改成本專案相對路徑（輸入在 `data/`、`assets/`，輸出在 `outputs/`）。對照表在 `HANDOFF.md` §6。
5. **重新產出**：照 `HANDOFF.md` §5 的指令跑腳本。

## 資料夾結構

```
.
├── HANDOFF.md              ← 先讀這份：完整專案交接
├── README.md               ← 本檔
├── scripts/                ← 所有生成腳本
│   ├── build_from_csv.py        重建 Excel 母檔（資料更新後第一支跑）
│   ├── build_filled_html.py     賓客對照表
│   ├── build_maintable.py       主桌帶位圖
│   ├── build_real.py            主桌桌卡（皇家版＝最終版）
│   ├── build_checklist2.py      當天分工清單
│   ├── build_checklist_sync.py  分工清單（雲端同步版）
│   ├── warp_ivory2.py / inpaint2.py   桌卡底圖萃取（從參考照片）
│   ├── build_placecards2/3/4.py concepts.py   桌卡早期版本
│   └── helpers/                 PDF/PNG 轉檔小工具
├── data/                   ← 資料與中間檔
│   ├── filled_from_gsheet.xlsx  最新資料快照
│   ├── card_bg.b64              桌卡底圖（已去背修圖）
│   └── emblem_gold*.b64         金色圖徽
├── assets/                 ← 素材
│   ├── logo_src.png             新人婚禮 logo
│   ├── emblem_gold*.png frame.png frame.svg
│   └── ref_card.png             桌卡版型參考照片
└── outputs/                ← 成品
    ├── html/   pdf/   images/
```

## 資料更新流程（最常用）

Google 試算表更新後：

1. 用 gviz CSV 抓最新資料（網址與工作表見 `HANDOFF.md` §3）。
2. 更新 `scripts/build_from_csv.py` 的資料清單 → 跑它重建 `data/filled_from_gsheet.xlsx`。
3. 跑 `build_filled_html.py`、`build_maintable.py` 等下游腳本重新產出。

## 注意

- claude.ai 上的兩個「即時同步」線上網頁（賓客對照表、雲端同步分工清單）是 claude.ai 平台功能，**無法搬到 Antigravity**；它們的原始 HTML 在 `outputs/html/`，可在這裡編輯內容，但即時勾選同步需靠原平台。細節見 `HANDOFF.md` §7。
- 桌卡版型不可更動，只能改姓名與稱謂。見 `HANDOFF.md` §8。
