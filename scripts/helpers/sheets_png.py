from playwright.sync_api import sync_playwright
import urllib.parse, os
html_path = os.path.abspath("outputs/html/主桌桌卡_皇家版.html")
url="file://"+urllib.parse.quote(html_path)
with sync_playwright() as p:
    b=p.chromium.launch()
    pg=b.new_page(device_scale_factor=3)
    pg.goto(url); pg.wait_for_timeout(1500)
    sheets=pg.query_selector_all(".sheet")
    print("sheets found:", len(sheets))
    for i,s in enumerate(sheets):
        s.screenshot(path=f"outputs/images/sheet_{i+1}.png")
        box=s.bounding_box(); print(i+1, "box", round(box['width']),"x",round(box['height']))
    b.close()
