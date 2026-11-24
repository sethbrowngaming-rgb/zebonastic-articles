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
im,d=base(BK,WH,"OCT 2026",1)
d.text((70,430),"49.9%",font=F(FB,300),fill=OR)
y=block(d,"OF NEW STEAM RELEASES CARRIED AN AI DISCLOSURE",F(FB,70),70,820,W-140,WH,1.1)
im.save("f1.png")
im,d=base(WH,BK,"ONE MONTH",2)
y=block(d,"THAT IS ONE MONTH.",F(FB,110),70,380,W-140,BK,1.05)
d.rectangle([70,y+30,500,y+44],fill=OR)
d.text((70,y+120),"2026 SO FAR",font=F(FM,44),fill=GR)
d.text((70,y+180),"40.5%",font=F(FB,280),fill=BL)
block(d,"12,351 of 30,474 releases, to Nov 24",F(FB,48),70,y+520,W-140,GR)
im.save("f2.png")
im,d=base(BK,WH,"THE FLAG",3)
y=block(d,"SELF-REPORTED.",F(FB,100),70,330,W-140,WH,1.05)
d.rectangle([70,y+30,500,y+44],fill=OR)
d.rectangle([70,y+120,W-70,y+420],outline=WH,width=6)
d.text((100,y+145),"COUNTS",font=F(FM,44),fill=OR)
block(d,"AI content players see or hear",F(FB,58),100,y+215,W-200,WH,1.1)
d.rectangle([70,y+480,W-70,y+780],outline=WH,width=6)
d.text((100,y+505),"CAN'T SAY",font=F(FM,44),fill=OR)
block(d,"how much AI a game used. Dev tools are outside the form.",F(FB,50),100,y+575,W-200,WH,1.1)
im.save("f3.png")
im,d=base(WH,BK,"WHY?",4)
block(d,"FLAGGED RELEASES PER YEAR",F(FB,74),70,230,W-140,BK,1.1)
rows=[("2024",2319,OR),("2025",4937,OR),("2026 to Nov 24",12351,OR)]
y=480
for g,v,c in rows:
    d.text((70,y),g,font=F(FM,38),fill=GR)
    bw=int((W-140-220)*v/12351)
    d.rectangle([70,y+60,70+bw,y+170],fill=c)
    d.text((70+bw+16,y+78),f"{v:,}",font=F(FB,60),fill=BK)
    y+=250
block(d,"Reason not established: more AI? more disclosure? different mix? rule change?",F(FB,46),70,y+30,W-140,GR,1.15)
im.save("f4.png")
im,d=base(BK,WH,"VERDICT",5)
y=block(d,"HALF OF NEW GAMES USE AI?",F(FB,100),70,330,W-140,WH,1.05)
y=block(d,"THE EVIDENCE DOESN'T SAY THAT.",F(FB,100),70,y+40,W-140,OR,1.05)
d.rectangle([70,y+110,W-70,y+260],fill=OR)
d.text((100,y+145),"READ THE FULL ARTICLE",font=F(FB,66),fill=BK)
im.save("f5.png")
