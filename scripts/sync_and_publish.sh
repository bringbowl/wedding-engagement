#!/bin/bash
set -e

echo "=== 1. 從 Google 試算表抓取最新資料並重建 Excel ==="
python scripts/build_from_csv.py --fetch

echo "=== 2. 重新產出賓客對照表、分工清單、主桌帶位圖 ==="
python scripts/build_filled_html.py
python scripts/build_checklist_sync.py
python scripts/build_schedule.py
python scripts/build_maintable.py
python scripts/build_real.py

echo "=== 3. 提交變更並推送到 GitHub Pages ==="
git add .
if git diff --staged --quiet; then
  echo "所有檔案已是最新狀態，無需推送。"
else
  git commit -m "update: sync latest data from google sheet and rebuild web pages"
  if git remote get-url origin >/dev/null 2>&1; then
    git push
    echo "=== 線上共享網址已成功自動更新！ ==="
  else
    echo "尚未設定 git remote origin，請先設定遠端倉庫。"
  fi
fi
