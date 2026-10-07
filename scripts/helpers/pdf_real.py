from playwright.sync_api import sync_playwright
import urllib.parse, os
html_path = os.path.abspath("outputs/html/主桌桌卡_皇家版.html")
url="file://"+urllib.parse.quote(html_path)
with sync_playwright() as p:
    b=p.chromium.launch(); pg=b.new_page()
    pg.goto(url); pg.wait_for_timeout(2000)
    pg.emulate_media(media="print")
    pg.pdf(path="outputs/pdf/主桌桌卡_皇家版.pdf", format="A4", print_background=True, margin={"top":"0","bottom":"0","left":"0","right":"0"})
    b.close()
print("ok")
