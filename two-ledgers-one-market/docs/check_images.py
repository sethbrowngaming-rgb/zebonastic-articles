import re,sys,os
d=os.path.dirname(os.path.abspath(__file__))+"/.."
html=open(d+"/two-ledgers-one-market.html").read()
bad=0
for src in re.findall(r'<img[^>]+src="([^"]+)"',html):
    if src.startswith("data:"): continue
    p=os.path.join(d,src)
    ok=os.path.isfile(p) and os.path.getsize(p)>1000
    print("OK " if ok else "MISSING",src); bad+= (not ok)
for tag in re.findall(r'<img[^>]*>',html):
    if 'alt="' not in tag: print("NO ALT",tag[:60]); bad+=1
sys.exit(bad)
