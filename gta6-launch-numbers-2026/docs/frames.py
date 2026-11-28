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
im,d=base(BK,WH,"NOV 20, 2026",1)
d.text((70,430),"$3.79B",font=F(FB,260),fill=OR)
block(d,"GTA VI DAY-ONE RETAIL SALES, PER TAKE-TWO",F(FB,70),70,800,W-140,WH,1.1)
d.text((70,1180),"Company estimate. Unaudited.",font=F(FM,40),fill=GR if False else WH)
im.save("f1.png")
im,d=base(WH,BK,"THE TRACKER",2)
d.text((70,330),"SENSOR TOWER",font=F(FM,48),fill=GR)
d.text((70,400),"$1.84B",font=F(FB,250),fill=BL)
block(d,"at launch. PlayStation and Xbox digital only.",F(FB,56),70,700,W-140,BK)
d.text((70,1000),"REPORTED NEXT DAY",font=F(FM,44),fill=GR)
d.text((70,1070),"$2.36B",font=F(FB,200),fill=BL)
block(d,"one outlet, not confirmed",F(FB,50),70,1300,W-140,GR)
im.save("f2.png")
im,d=base(BK,WH,"SCOPE",3)
y=block(d,"DIFFERENT COUNTS.",F(FB,100),70,330,W-140,WH,1.05)
d.rectangle([70,y+30,500,y+44],fill=OR)
d.rectangle([70,y+120,W-70,y+470],outline=WH,width=6)
d.text((100,y+145),"TAKE-TWO",font=F(FM,44),fill=OR)
block(d,"Never defines \"retail sales.\" No day-one unit count.",F(FB,54),100,y+215,W-200,WH,1.1)
d.rectangle([70,y+530,W-70,y+880],outline=WH,width=6)
d.text((100,y+555),"TRACKER",font=F(FM,44),fill=OR)
block(d,"Modelled estimate. Retail code boxes not described as counted.",F(FB,54),100,y+625,W-200,WH,1.1)
im.save("f3.png")
im,d=base(WH,BK,"THE MATH",4)
block(d,"DOLLARS PER UNIT",F(FB,84),70,230,W-140,BK,1.1)
rows=[("SENSOR TOWER",96.6,BL),("TAKE-TWO",116.6,OR)]
y=520
for g,v,c in rows:
    d.text((70,y),g,font=F(FM,40),fill=GR)
    bw=int((W-140-260)*v/116.6)
    d.rectangle([70,y+60,70+bw,y+190],fill=c)
    d.text((70+bw+16,y+90),f"${v}",font=F(FB,64),fill=BK)
    y+=300
d.text((70,y+10),"US top list price: $99.99",font=F(FM,42),fill=BK)
block(d,"Scope, timing or definition. Not established.",F(FB,50),70,y+90,W-140,GR,1.15)
im.save("f4.png")
im,d=base(BK,WH,"VERDICT",5)
y=block(d,"WHY THE GAP?",F(FB,110),70,330,W-140,WH,1.05)
y=block(d,"SOURCES DOCUMENT IT. THEY DON'T EXPLAIN IT.",F(FB,86),70,y+40,W-140,OR,1.05)
d.rectangle([70,y+110,W-70,y+260],fill=OR)
d.text((100,y+145),"READ THE FULL ARTICLE",font=F(FB,66),fill=BK)
im.save("f5.png")
