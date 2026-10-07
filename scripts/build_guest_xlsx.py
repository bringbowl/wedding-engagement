# -*- coding: utf-8 -*-
import openpyxl
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side, NamedStyle
from openpyxl.worksheet.datavalidation import DataValidation
from openpyxl.utils import get_column_letter

# ---- palette (red-gold 宮廷) ----
DEEP_RED  = "8B1A1A"
WINE      = "6E1414"
GOLD      = "C9A24B"
GOLD_LT   = "F3E7C8"
CREAM     = "FBF6EA"
INK       = "2B1D12"
GREY_LINE = "D8C9A6"

FONT = "Microsoft JhengHei"

def font(sz=11, bold=False, color=INK, italic=False):
    return Font(name=FONT, size=sz, bold=bold, color=color, italic=italic)

def fill(c): return PatternFill("solid", fgColor=c)

thin = Side(style="thin", color=GREY_LINE)
med  = Side(style="medium", color=GOLD)
box  = Border(left=thin, right=thin, top=thin, bottom=thin)
box_gold = Border(left=med, right=med, top=med, bottom=med)

center = Alignment(horizontal="center", vertical="center", wrap_text=True)
left   = Alignment(horizontal="left", vertical="center", wrap_text=True)
leftt  = Alignment(horizontal="left", vertical="top", wrap_text=True)

# 13 桌（王位=主桌）
TABLES = [
    ("王位",       "主桌・舞台正前方中央"),
    ("獅子王",     "左／中區"),
    ("天外奇蹟",   "左／中區"),
    ("睡美人",     "左／中區"),
    ("小美人魚",   "左／中區"),
    ("花木蘭",     "左／中區"),
    ("熊的傳說",   "左／中區"),
    ("金銀島",     "左／中區"),
    ("美女與野獸", "右區"),
    ("仙履奇緣",   "右區"),
    ("阿拉丁",     "右區"),
    ("變身國王",   "右區"),
    ("冰雪奇緣",   "右區"),
]
TABLE_NAMES = [t[0] for t in TABLES]

wb = openpyxl.Workbook()

# =====================================================================
# Sheet 1  使用說明
# =====================================================================
ws = wb.active
ws.title = "使用說明"
ws.sheet_view.showGridLines = False
ws.column_dimensions["A"].width = 3
ws.column_dimensions["B"].width = 96

def banner(ws, row, text, sub=None):
    ws.merge_cells(start_row=row, start_column=2, end_row=row, end_column=2)
    c = ws.cell(row, 2, text)
    c.font = font(18, True, "FFFFFF")
    c.fill = fill(DEEP_RED)
    c.alignment = Alignment(horizontal="center", vertical="center")
    ws.row_dimensions[row].height = 40
    if sub:
        ws.merge_cells(start_row=row+1, start_column=2, end_row=row+1, end_column=2)
        s = ws.cell(row+1, 2, sub)
        s.font = font(11, False, WINE)
        s.fill = fill(GOLD_LT)
        s.alignment = Alignment(horizontal="center", vertical="center")
        ws.row_dimensions[row+1].height = 24

banner(ws, 1, "BARRY ♥ WINNIE ・ 訂婚宴 賓客對照表", "幸福登機門  GATE 2F  ・  2026.10.11  ・  台南")

lines = [
    ("", ""),
    ("這份檔案怎麼用？", "H"),
    ("只要填「賓客總表」這一張，其他看法都從它來。接待、禮金桌、排桌，看同一份資料就好。", "P"),
    ("", ""),
    ("①　賓客總表（最主要・填這張）", "H"),
    ("每位賓客一列：姓名、桌次（點格子會跳出 13 桌下拉選單）、關係／稱謂、紅包金額、報到打勾、備註。", "P"),
    ("・ 想「依姓名查」：點『姓名』欄 → 上方篩選箭頭 → 排序 A→Z／筆劃，報到報名字一秒找到桌號。", "P"),
    ("・ 想「依桌次看」：點『桌次』欄的篩選箭頭 → 勾某一桌，就只顯示那桌的人。", "P"),
    ("・ 禮金桌：直接用『紅包金額』『報到』『備註』三欄邊收邊記。", "P"),
    ("", ""),
    ("②　依桌次（排桌・桌卡用）", "H"),
    ("13 桌各一區塊，空白座位行讓你寫名字、擺桌卡。每桌標題旁會自動顯示『總表裡分到這桌的人數』，方便對人數。", "P"),
    ("", ""),
    ("③　桌次總覽（鳥瞰）", "H"),
    ("13 桌的名稱、位置區塊、人數一覽。桌號欄留空，你們要編號再填（也可以不編號，直接用桌名帶位）。", "P"),
    ("", ""),
    ("小提醒", "H"),
    ("・ 黃底的格子＝要你填的地方。灰字範例列只是示範格式，正式用可以直接蓋掉或刪掉。", "P"),
    ("・ 桌名若之後有改，記得三張表一起改（總覽、依桌次、下拉選單都在『桌次總覽』那張的 A 欄）。", "P"),
    ("・ 這張是模板，先把骨架給你，名單你事後慢慢補即可。", "P"),
]
r = 3
for text, kind in lines:
    ws.merge_cells(start_row=r, start_column=2, end_row=r, end_column=2)
    c = ws.cell(r, 2, text)
    if kind == "H":
        c.font = font(13, True, DEEP_RED); ws.row_dimensions[r].height = 26
    elif kind == "P":
        c.font = font(11, False, INK); c.alignment = leftt; ws.row_dimensions[r].height = 22
    else:
        ws.row_dimensions[r].height = 8
    r += 1

# =====================================================================
# Sheet 4 (建在前面，給下拉選單引用)  桌次總覽
# =====================================================================
ov = wb.create_sheet("桌次總覽")
ov.sheet_view.showGridLines = False
headers = ["桌次名稱", "桌號", "位置區塊", "人數（自動）", "備註"]
widths  = [16, 8, 24, 12, 30]
for i, (h, w) in enumerate(zip(headers, widths), start=1):
    ov.column_dimensions[get_column_letter(i)].width = w

# title
ov.merge_cells("A1:E1")
t = ov.cell(1, 1, "桌次總覽")
t.font = font(16, True, "FFFFFF"); t.fill = fill(DEEP_RED); t.alignment = center
ov.row_dimensions[1].height = 34
# header row 2
for i, h in enumerate(headers, start=1):
    c = ov.cell(2, i, h)
    c.font = font(11, True, "FFFFFF"); c.fill = fill(WINE)
    c.alignment = center; c.border = box
ov.row_dimensions[2].height = 24

for idx, (name, loc) in enumerate(TABLES):
    row = 3 + idx
    is_head = (name == "王位")
    vals = [name, "", loc,
            f'=COUNTIF(賓客總表!C:C,A{row})', ""]
    for i, v in enumerate(vals, start=1):
        c = ov.cell(row, i, v)
        c.alignment = center if i in (1,2,4) else left
        c.border = box_gold if is_head else box
        if i == 1:
            c.font = font(12, True, DEEP_RED if is_head else INK)
            c.fill = fill(GOLD_LT if is_head else CREAM)
        elif i == 2:
            c.fill = fill("FFFDE7"); c.font = font(11, False, INK)  # 黃底=填桌號
        else:
            c.font = font(11, False, INK)
            if i == 5: c.fill = fill("FFFDE7")
    ov.row_dimensions[row].height = 24

note_r = 3 + len(TABLES) + 1
ov.merge_cells(start_row=note_r, start_column=1, end_row=note_r, end_column=5)
n = ov.cell(note_r, 1, "「人數（自動）」會依『賓客總表』裡填的桌次自動統計。黃底欄位（桌號／備註）可自行填寫。")
n.font = font(10, False, WINE, italic=True); n.alignment = left

# =====================================================================
# Sheet 2  賓客總表 (master)
# =====================================================================
mw = wb.create_sheet("賓客總表")
mw.sheet_view.showGridLines = False
m_headers = ["序號", "姓名", "桌次", "關係／稱謂", "紅包金額", "報到", "備註"]
m_widths  = [6, 16, 14, 18, 12, 7, 28]
for i, (h, w) in enumerate(zip(m_headers, m_widths), start=1):
    mw.column_dimensions[get_column_letter(i)].width = w

mw.merge_cells("A1:G1")
t = mw.cell(1, 1, "賓客總表　｜　填這張就好（可依姓名或桌次排序／篩選）")
t.font = font(15, True, "FFFFFF"); t.fill = fill(DEEP_RED); t.alignment = center
mw.row_dimensions[1].height = 34

for i, h in enumerate(m_headers, start=1):
    c = mw.cell(2, i, h)
    c.font = font(11, True, "FFFFFF"); c.fill = fill(WINE)
    c.alignment = center; c.border = box
mw.row_dimensions[2].height = 26

# example row (grey, format demo)
example = [1, "（範例）王小明", "獅子王", "男方－大伯", 3600, "✓", "吃素，需素食餐"]
for i, v in enumerate(example, start=1):
    c = mw.cell(3, i, v)
    c.font = font(10, False, "9A9A9A", italic=True)
    c.alignment = center if i in (1,3,5,6) else left
    c.border = box
    c.fill = fill("F2F2F2")
mw.row_dimensions[3].height = 22

# blank fillable rows
TOTAL_ROWS = 140
for r in range(4, 4 + TOTAL_ROWS):
    mw.cell(r, 1, r - 3)  # 序號 auto 1..N
    mw.cell(r, 1).font = font(10, False, "8A8A8A")
    mw.cell(r, 1).alignment = center
    for i in range(2, 8):
        c = mw.cell(r, i)
        c.border = box
        c.alignment = center if i in (3,5,6) else left
        c.font = font(11, False, INK)
        # 黃底標示可填：姓名/關係/紅包/備註 give subtle input fill
        if i in (2,3,4,5,6,7):
            c.fill = fill("FFFFFF")
    mw.row_dimensions[r].height = 22

# data validation: 桌次 dropdown from 桌次總覽!A3:A15
dv = DataValidation(type="list",
                    formula1="=桌次總覽!$A$3:$A$15",
                    allow_blank=True, showErrorMessage=True)
dv.error = "請從下拉選單選擇桌次"
dv.errorTitle = "桌次"
dv.prompt = "點這裡選桌次"
dv.promptTitle = "桌次"
mw.add_data_validation(dv)
dv.add(f"C3:C{3+TOTAL_ROWS}")

# 報到 ✓ dropdown
dv2 = DataValidation(type="list", formula1='"✓,—"', allow_blank=True)
mw.add_data_validation(dv2)
dv2.add(f"F3:F{3+TOTAL_ROWS}")

# freeze + autofilter
mw.freeze_panes = "A3"
mw.auto_filter.ref = f"A2:G{3+TOTAL_ROWS}"

# summary strip at top-right area? keep simple: a totals note on row above?
# Add live count of 已填/已報到 at the far right header area via helper cells below data
sumr = 4 + TOTAL_ROWS + 1
mw.cell(sumr, 2, "賓客總數（已填姓名）：").font = font(11, True, DEEP_RED)
mw.cell(sumr, 5, f'=COUNTA(B4:B{3+TOTAL_ROWS})').font = font(11, True, INK)
mw.cell(sumr, 5).alignment = center
mw.cell(sumr+1, 2, "已報到：").font = font(11, True, DEEP_RED)
mw.cell(sumr+1, 5, f'=COUNTIF(F4:F{3+TOTAL_ROWS},"✓")').font = font(11, True, INK)
mw.cell(sumr+1, 5).alignment = center
mw.cell(sumr+2, 2, "紅包合計：").font = font(11, True, DEEP_RED)
mw.cell(sumr+2, 5, f'=SUM(E4:E{3+TOTAL_ROWS})').font = font(11, True, INK)
mw.cell(sumr+2, 5).alignment = center
mw.cell(sumr+2, 5).number_format = '"$"#,##0'

# =====================================================================
# Sheet 3  依桌次 (by-table layout for printing/seating)
# =====================================================================
bt = wb.create_sheet("依桌次")
bt.sheet_view.showGridLines = False
# layout: two columns of table-blocks? keep single column for clarity, 12 seats each
bt.column_dimensions["A"].width = 6
bt.column_dimensions["B"].width = 26
bt.column_dimensions["C"].width = 22
bt.column_dimensions["D"].width = 30

bt.merge_cells("A1:D1")
t = bt.cell(1, 1, "依桌次　｜　排桌・桌卡・帶位用")
t.font = font(15, True, "FFFFFF"); t.fill = fill(DEEP_RED); t.alignment = center
bt.row_dimensions[1].height = 32

SEATS = 12
row = 3
for name, loc in TABLES:
    is_head = (name == "王位")
    # table header
    bt.merge_cells(start_row=row, start_column=1, end_row=row, end_column=4)
    hc = bt.cell(row, 1, f"　{name}" + ("（主桌）" if is_head else "") + f"　—　{loc}")
    hc.font = font(13, True, "FFFFFF")
    hc.fill = fill(WINE if not is_head else DEEP_RED)
    hc.alignment = Alignment(horizontal="left", vertical="center")
    bt.row_dimensions[row].height = 28
    row += 1
    # sub header
    subs = ["座位", "姓名", "關係／稱謂", "備註"]
    for i, s in enumerate(subs, start=1):
        c = bt.cell(row, i, s)
        c.font = font(10, True, WINE); c.fill = fill(GOLD_LT)
        c.alignment = center; c.border = box
    # headcount cell appended to the right of備註 header? put into D header text already. Instead show count under seat area.
    bt.row_dimensions[row].height = 20
    row += 1
    for s in range(1, SEATS + 1):
        bt.cell(row, 1, s).font = font(10, False, "8A8A8A")
        bt.cell(row, 1).alignment = center; bt.cell(row, 1).border = box
        for i in range(2, 5):
            c = bt.cell(row, i); c.border = box; c.font = font(11, False, INK)
            c.alignment = left if i in (2,3,4) else center
        bt.row_dimensions[row].height = 21
        row += 1
    # count line
    bt.merge_cells(start_row=row, start_column=1, end_row=row, end_column=4)
    cl = bt.cell(row, 1, f'=\"　本桌（總表已分配）：\"&COUNTIF(賓客總表!C:C,\"{name}\")&\" 人\"')
    cl.font = font(10, False, DEEP_RED, italic=True)
    cl.alignment = left
    row += 2  # gap

# =====================================================================
# save
# =====================================================================
out = "data/訂婚賓客對照表.xlsx"
# order sheets: 使用說明, 賓客總表, 依桌次, 桌次總覽
wb.move_sheet("賓客總表", -(wb.sheetnames.index("賓客總表") - 1))
# ensure order
desired = ["使用說明", "賓客總表", "依桌次", "桌次總覽"]
wb._sheets.sort(key=lambda s: desired.index(s.title))
wb.active = wb.sheetnames.index("賓客總表")
wb.save(out)
print("saved", out)
print("sheets:", wb.sheetnames)
