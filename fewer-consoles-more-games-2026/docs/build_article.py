import base64,re,sys
SRC="/home/claude/work/article/src.html"; OUT="/home/claude/work/article/fewer-consoles-more-games.html"
IMG="/home/claude/work/article/images/"
s=open(SRC).read()
def emb(m):
    n=m.group(1); b=base64.b64encode(open(IMG+n,"rb").read()).decode()
    return f'src="data:image/png;base64,{b}"'
out=re.sub(r'src="images/([a-z0-9\-]+\.png)"',emb,s)
assert "images/" not in out.replace("data:image/png","")
open(OUT,"w").write(out); print(len(out)//1024,"KB")
