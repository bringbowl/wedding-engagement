from playwright.sync_api import sync_playwright
import urllib.parse, os
svg=open("assets/frame.svg").read()
html=f"<!doctype html><html><head><meta charset=utf-8><style>*{{margin:0}}body{{background:#777}}</style></head><body>{svg}</body></html>"
wrap_path = os.path.abspath("outputs/html/frame_wrap.html")
open(wrap_path,"w").write(html)
with sync_playwright() as p:
    b=p.chromium.launch(); pg=b.new_page(device_scale_factor=2)
    pg.goto("file://"+urllib.parse.quote(wrap_path)); pg.wait_for_timeout(900)
    el=pg.query_selector("svg")
    el.screenshot(path="assets/frame.png")
    b.close()
print("rendered")
