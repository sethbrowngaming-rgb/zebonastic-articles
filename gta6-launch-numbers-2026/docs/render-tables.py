from playwright.sync_api import sync_playwright
OUT="/home/claude/gta6-launch-numbers-2026/images/"
names={"table1":"table1-who-counted-what.png","table2":"table2-explanations.png","table3":"table3-know-think-dont-know.png"}
with sync_playwright() as p:
    b=p.chromium.launch(executable_path="/usr/bin/google-chrome",args=["--no-sandbox"])
    pg=b.new_page(viewport={"width":1300,"height":900},device_scale_factor=2)
    pg.goto("file:///home/claude/gta6-launch-numbers-2026/docs/tables.html")
    for k,v in names.items():
        pg.locator("#"+k).screenshot(path=OUT+v)
    b.close()
print("tables ok")
