from playwright.sync_api import sync_playwright
import urllib.parse, os
html_path = os.path.abspath("outputs/html/主桌帶位圖.html")
url="file://"+urllib.parse.quote(html_path)
with sync_playwright() as p:
    b=p.chromium.launch()
    pg=b.new_page(viewport={"width":1040,"height":1000}, device_scale_factor=2)
    pg.goto(url); pg.wait_for_timeout(1500)
    # screenshot just the content wrap for tight margins
    el=pg.query_selector(".wrap")
    el.screenshot(path="outputs/images/主桌帶位圖.png")
    b.close()
print("done")
