from playwright.sync_api import sync_playwright
with sync_playwright() as p:
    b=p.chromium.launch(executable_path="/usr/bin/google-chrome",args=["--no-sandbox"])
    pg=b.new_page(viewport={"width":1000,"height":1200})
    pg.goto("file:///home/claude/gta6-launch-numbers-2026/counting-a-launch.html")
    r=pg.evaluate("()=>[...document.images].map(i=>[i.complete,i.naturalWidth,i.naturalHeight,(i.alt||'').length])")
    print(r); print("broken:",[x for x in r if not x[0] or x[1]==0 or x[3]<20])
    print("anchors without target:",pg.evaluate("()=>[...document.querySelectorAll('a[href^=\"#s\"]')].filter(a=>!document.querySelector(a.getAttribute('href'))).map(a=>a.getAttribute('href'))"))
    print("tables:",pg.evaluate("document.querySelectorAll('table').length"))
    pg.screenshot(path="/tmp/article-full.png",full_page=True); b.close()
