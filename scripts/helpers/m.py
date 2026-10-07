from playwright.sync_api import sync_playwright
import urllib.parse, os
html_path = os.path.abspath("outputs/html/訂婚賓客對照表_已填_可列印.html")
url="file://"+urllib.parse.quote(html_path)
with sync_playwright() as p:
    b=p.chromium.launch(); pg=b.new_page(viewport={"width":390,"height":844}, device_scale_factor=2)
    pg.goto(url); pg.wait_for_timeout(1000)
    pg.screenshot(path="outputs/images/ref_mobile.png")
    # check horizontal overflow
    ov=pg.evaluate("({sw:document.documentElement.scrollWidth, cw:document.documentElement.clientWidth})")
    print(ov)
    b.close()
