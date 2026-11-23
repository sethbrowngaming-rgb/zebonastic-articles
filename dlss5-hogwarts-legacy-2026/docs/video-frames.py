from PIL import Image, ImageDraw, ImageFont
W,H=1080,1920
BK=(11,11,11); WH=(252,252,251); OR=(235,104,52); BL=(42,120,214); GR=(82,81,78)
FB="/usr/share/fonts/truetype/google-fonts/Poppins-Bold.ttf"
FM="/usr/share/fonts/truetype/dejavu/DejaVuSansMono-Bold.ttf"
def F(p,s): return ImageFont.truetype(p,s)
def wrap(d,t,f,w):
    out=[];cur=""
    for wd in t.split():
        n=(cur+" "+wd).strip()
        if d.textlength(n,font=f)<=w: cur=n
        else: out.append(cur);cur=wd
    out.append(cur);return out
def block(d,t,f,x,y,w,fill,gap=1.15):
    for ln in wrap(d,t,f,w):
        d.text((x,y),ln,font=f,fill=fill); y+=int(f.size*gap)
    return y
def base(bg,fg,label,n):
    im=Image.new("RGB",(W,H),bg);d=ImageDraw.Draw(im)
    d.rectangle([30,30,W-31,H-31],outline=fg,width=10)
    d.rectangle([70,90,70+len(label)*26+40,160],fill=OR); d.text((90,106),label,font=F(FM,34),fill=BK)
    d.text((W-170,H-130),f"{n}/5",font=F(FM,40),fill=fg)
    d.text((70,H-130),"ZEBONASTIC",font=F(FM,40),fill=fg)
    return im,d
# 1
im,d=base(BK,WH,"MARCH 2026",1)
y=block(d,"DLSS 5 REVEAL",F(FB,150),70,520,W-140,WH,1.05)
d.rectangle([70,y+30,500,y+44],fill=OR)
block(d,"Critics: it rewrites character faces.",F(FB,64),70,y+110,W-140,WH)
im.save("f1.png")
# 2
im,d=base(WH,BK,"NOV 5",2)
y=block(d,"HOGWARTS LEGACY SHIPS IT",F(FB,130),70,420,W-140,BK,1.05)
d.rectangle([70,y+30,500,y+44],fill=OR)
y=block(d,"Nvidia's own comparison images:",F(FB,56),70,y+110,W-140,GR)
block(d,"changes mostly in lighting and materials.",F(FB,66),70,y+10,W-140,BK)
im.save("f2.png")
# 3
im,d=base(BK,WH,"PER NVIDIA",3)
y=block(d,"WHO DECIDES?",F(FB,150),70,360,W-140,WH,1.05)
d.rectangle([70,y+30,500,y+44],fill=OR)
d.rectangle([70,y+120,W-70,y+420],outline=WH,width=6)
d.text((100,y+145),"DEVELOPERS",font=F(FM,44),fill=OR)
block(d,"model, intensity, masks (faces too)",F(FB,60),100,y+215,W-200,WH,1.1)
d.rectangle([70,y+480,W-70,y+680],outline=WH,width=6)
d.text((100,y+505),"PLAYERS",font=F(FM,44),fill=OR)
d.text((100,y+575),"on / off",font=F(FB,72),fill=WH)
im.save("f3.png")
# 4
im,d=base(WH,BK,"RTX 5090 · 4K",4)
block(d,"FRAME-RATE LOSS WITH DLSS 5",F(FB,76),70,230,W-140,BK,1.1)
rows=[("NBA 2K27","SEPT MODEL",60,OR),("NBA 2K27","SEPT MODEL",51,OR),("HOGWARTS","SHIPPED NOV 5",42,BL),("HOGWARTS","SHIPPED NOV 5",20,BL)]
y=500
for g,s,v,c in rows:
    d.text((70,y),f"{g} · {s}",font=F(FM,34),fill=GR)
    bw=int((W-140-170)*v/65)
    d.rectangle([70,y+52,70+bw,y+142],fill=c)
    d.text((70+bw+16,y+60),f"−{v}%",font=F(FB,64),fill=BK)
    y+=240
block(d,"Different games and scenes: not like-for-like.",F(FB,44),70,y+10,W-140,GR,1.15)
im.save("f4.png")
# 5
im,d=base(BK,WH,"SETTLED?",5)
y=block(d,"DIFFERENCE: DOCUMENTED.",F(FB,100),70,330,W-140,WH,1.05)
y=block(d,"REASON: NOT.",F(FB,100),70,y+30,W-140,OR,1.05)
y=block(d,"Settings? Retrained model? Both?",F(FB,62),70,y+70,W-140,WH,1.15)
d.rectangle([70,y+60,W-70,y+210],fill=OR)
d.text((100,y+95),"READ THE FULL ARTICLE",font=F(FB,66),fill=BK)
im.save("f5.png")
