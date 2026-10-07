# 訂婚專案工作交接文件（HANDOFF）

> 這份文件把「我跟 Claude 的對話成果」與「未來的工作流程」整包交給 Google Antigravity。
> 讀完這一份，Antigravity 裡的 AI agent（或你自己）就能接手繼續做下去。

---

## 0. 給 Antigravity Agent 的一句話

你接手的是一個**婚禮訂婚宴的平面＆資料專案**。所有產出都是用 Python 腳本「從資料生成」的（HTML / PDF / PNG / Excel），資料來源是一份 Google 試算表。你的工作就是：資料更新時重新抓、重新跑腳本、重新產出檔案。下面 §5 有每個產出對應的指令。

⚠️ 腳本裡目前寫的是原本雲端環境的絕對路徑 `/home/claude/...`。在 Antigravity 本機請把它們改成本專案資料夾的相對路徑（或請 agent 自動改）。對照表見 §6。

---

## 1. 專案基本資料

| 項目 | 內容 |
|---|---|
| 新娘 | 戴婉錡（Winnie） |
| 新郎 | 羅聖明（Barry） |
| 場合 | 訂婚宴（文定） |
| 日期 | 2026.10.11 |
| 地點 | 台南 |
| 主題 | 歐洲宮廷 × 迪士尼 |
| 主視覺 | 「幸福登機門／登機證（boarding pass）」概念 |
| 品牌標語 | 幸福登機門 GATE 2F · FLIGHT BW1011 · 2026.10.11 台南 |

## 2. 視覺規範（Brand）

**色票（紅金宮廷）**

| 名稱 | HEX | 用途 |
|---|---|---|
| wine 酒紅 | `#6E1414` | 主色、標題 |
| gold 金 | `#C9A24B` | 線框、分隔線 |
| gold-deep 深金 | `#A8822F` | 名字燙金 |
| red 紅 | `#8B1A1A` | 強調字 |
| cream 米白 | `#FBF6EA` | 底色 |
| gold-highlight 亮金 | `#E2C275` | 高光 |

**字型**
- `Noto Serif TC`（中文；名字用 900 最粗）
- `Cormorant Garamond`（拉丁字、英文稱謂）
- `Pinyon Script`（花體，對應他們婚禮 logo 的手寫感）

**Logo／圖徽**
- `assets/logo_src.png`：新人真正的婚禮 logo（蜂蜜罐＋花環字母組合，黑白）
- `assets/emblem_gold.png` / `assets/emblem_gold_bright.png`：從 logo 用亮度去背萃取出的金色線稿版
- `assets/frame.png` / `assets/frame.svg`：桌卡用的宮廷外框
- `assets/ref_card.png`：使用者指定「要做成這樣」的桌卡參考照片（皇家版版型來源）

## 3. 資料來源（最重要）

所有賓客／座位資料來自同一份 Google 試算表：

```
試算表 ID：1TasCO9KSlpflyi-poXNur0p5EYWLFvtHGZI3R7eKsYg
權限：知道連結的人可檢視（anyone with link can view）
```

**抓資料的正確方法 —— gviz CSV（逐工作表）**

不要用 Google Drive 的 xlsx 匯出（檔案約 6MB，會把 MCP 傳輸打爆、也不會存檔）。
改用 gviz 的 CSV 匯出，一次抓一個工作表：

```
https://docs.google.com/spreadsheets/d/1TasCO9KSlpflyi-poXNur0p5EYWLFvtHGZI3R7eKsYg/gviz/tq?tqx=out:csv&sheet=<工作表名稱URL編碼>
```

已知工作表：
- `gid=848591360` → 賓客總表
- `gid=201770222` → 使用說明
- `sheet=依桌次`（URL 編碼 `%E4%BE%9D%E6%A1%8C%E6%AC%A1`）

> 在 Antigravity 本機，agent 可直接用 Python `requests` 抓這些 URL（不需要特殊權限，因為是公開可檢視）。

**資料更新時的流程**
1. 用 gviz CSV 重新抓各工作表。
2. 把新資料更新進 `scripts/build_from_csv.py` 裡的 `MASTER`（賓客清單）與 `SEATING`（座位）兩個清單，或改寫成直接讀 CSV。
3. 跑 `build_from_csv.py` → 產生 `data/filled_from_gsheet.xlsx`。
4. 跑下游腳本（對照表、座位圖等）重新產出。

> 目前 `data/filled_from_gsheet.xlsx` 是最後一次抓的快照。
> 最後一次更新的重點：花木蘭桌 = 趙銘輝/Ollie、劉良謙、李佳諭/Linda、劉彥伯/Paul（女方前同事）、Cecile（女方前同事）、李俊儀/Gemma、林怡真/Amanda（共 7 人）。

## 4. 產出清單（outputs/）

| 檔案 | 說明 |
|---|---|
| `html/訂婚賓客對照表_已填_可列印.html` | 接待／禮金桌用，三種檢視：依姓名查詢、依桌次、禮金桌核對 |
| `html/主桌帶位圖.html` ＋ `images/主桌帶位圖.png` | 主桌圓桌帶位圖 |
| `html/主桌桌卡_皇家版.html` ＋ `pdf/主桌桌卡_皇家版.pdf` | **最終採用版**桌卡（沿用參考照片版型，10 張＋2 張空白手寫） |
| `html/主桌桌卡_名牌版.html`、`主桌桌卡_酒紅鎏金.html` ＋對應 PDF | 桌卡的早期／備選版本 |
| `html/訂婚分工清單_雲端同步.html` | 當天分工檢查清單（雲端同步版，手機可勾選） |
| `html/訂婚當天分工清單.html` ＋ `pdf/訂婚當天分工清單.pdf` | 分工清單（可列印版） |
| `html/engagement_entrance_script.html` | 說書人／旁白進場台詞 |
| `html/engagement_music_list.html` | 音樂清單 |
| `html/growth_video_guide.html` | 成長影片指南 |
| `html/welcome_screen.html` | 迎賓畫面 |

## 5. 每個產出 → 生成腳本與指令

在專案根目錄執行（路徑已改相對後）：

```bash
# 1. 從最新資料重建 Excel 母檔（其他腳本的輸入）
python scripts/build_from_csv.py        # → data/filled_from_gsheet.xlsx

# 2. 賓客對照表（接待／禮金桌）
python scripts/build_filled_html.py     # → outputs/html/訂婚賓客對照表_已填_可列印.html

# 3. 主桌帶位圖
python scripts/build_maintable.py       # → 主桌帶位圖.html (SVG)
python scripts/helpers/png.py           # → 主桌帶位圖.png

# 4. 主桌桌卡（皇家版＝最終版）
#    依賴：data/card_bg.b64（已去背修圖的底圖）、assets/ref_card.png
python scripts/build_real.py            # → 主桌桌卡_皇家版.html
python scripts/helpers/pdf_real.py      # → 主桌桌卡_皇家版.pdf
#    若要從參考照片重新萃取底圖：
#    python scripts/warp_ivory2.py      # 透視校正 ref_card.png → ivory_flat.png
#    python scripts/inpaint2.py         # 遮罩中央文字區 + inpaint → card_bg.b64

# 5. 當天分工檢查清單
python scripts/build_checklist2.py      # → outputs/html/訂婚當天分工清單.html
python scripts/helpers/pdf_cl2.py       # → 訂婚當天分工清單.pdf
python scripts/build_checklist_sync.py  # → 雲端同步版 HTML
```

**Python 相依套件**
```
pip install openpyxl pypinyin playwright pymupdf opencv-python pillow numpy
playwright install chromium        # HTML→PDF/PNG 需要
```
- `openpyxl`：讀寫 xlsx
- `pypinyin`：中文姓名排序（依姓名查詢）
- `playwright` + chromium：HTML 轉 PDF／PNG（啟用列印媒體模擬）
- `pymupdf`：PDF 頁面轉圖
- `opencv-python`：桌卡照片透視校正、inpaint
- `pillow` / `numpy`：圖片去背、alpha 萃取

## 6. 路徑對照（絕對 → 相對）

腳本內的 `/home/claude/xxx` 請改成：

| 腳本裡寫的 | 改成（本專案相對路徑） |
|---|---|
| `/home/claude/card_bg.b64` | `data/card_bg.b64` |
| `/home/claude/emblem_gold.png.b64` | `data/emblem_gold.png.b64` |
| `/home/claude/emblem_gold_bright.png.b64` | `data/emblem_gold_bright.png.b64` |
| `/home/claude/filled_from_gsheet.xlsx` | `data/filled_from_gsheet.xlsx` |
| `/home/claude/frame.svg` | `assets/frame.svg` |
| `/home/claude/ref_card.png` | `assets/ref_card.png` |
| `/home/claude/訂婚賓客對照表_已填_可列印.html` 等輸出 | `outputs/html/...` |

> 快速做法：在 Antigravity 叫 agent「把 scripts/ 下所有 `/home/claude/` 開頭的路徑改成專案相對路徑，輸入放 data/、assets/，輸出放 outputs/」。

## 7. 線上版本（雲端連結）

以下兩個是發佈在 claude.ai 上的「活」網頁版本（有雲端同步功能，非本機檔案）：

- 賓客對照表（公開連結）：`https://claude.ai/artifact/1zrhZ6JMQH5Lq4Na725qjV`
- 雲端同步分工清單（db + user，公開連結）：`https://claude.ai/artifact/BtH1RthfbTLQL6ZnadUKHJ`

⚠️ **誠實說明**：這兩個網頁的即時同步（大家手機一起勾選）是 claude.ai 的功能，**無法搬到 Antigravity**。它們會繼續留在 claude.ai。它們的原始 HTML 已放在 `outputs/html/`，你可以在 Antigravity 裡編輯內容，但「即時雲端同步勾選」這個功能本身依賴 claude.ai 的平台。
> 分工清單同步的現實：用個人 Gmail 帳號發佈時，公開連結的人只能「看到」同步狀態，只有擁有者能勾。要讓工作人員也能勾，需用 email 邀請他們當 editor（而不是用公開連結）。

## 8. 重要決策與限制（避免重做）

- 桌卡最終版**必須完全沿用參考照片 `ref_card.png` 的版型**，只有「姓名、稱謂」可以改，其他元素一律不動。因此做法是用 OpenCV 把照片透視校正＋把中央文字區 inpaint 掉當底圖，再疊上可編輯的中英雙語稱謂與燙金姓名。不要重畫版型。
- 稱謂一律**中英雙語**（中文在上、金色分隔線、英文大寫在下）。
- 主桌桌卡只做主桌 10 位 ＋ 2 張空白備用（現場手寫）。
- 說書人旁白：雙方父母進場是**女方父母先、男方父母後**，所以旁白拆成 03A／03B 兩段。
- 主桌帶位圖：新娘爸爸與新娘媽媽位置已對調（戴建勳在 -162°、郭乃華在 -126°）。
- 分工清單：出發前全部由新郎新娘負責（含甜湯＝新娘、無框畫＋相簿＋謝卡、禮券紅包＋三項獎品、工作人員紅包、尾款、喜糖、吸管、分工清單表）；11:00 佈置就位含無框畫／相簿／謝卡擺放（伴娘負責）。

## 9. 尚未完成／未來可做

- 結婚（正婚）場的相關設計（目前只做到訂婚場）
- 邀請卡
- 奉茶吉祥話卡
- 其他依新人需求新增的平面物

---

檔案結構見同目錄 `README.md`。
