import numpy as np, json, subprocess
from PIL import Image, ImageDraw, ImageFont
W,H,FPS=1080,1920,30
CREAM=(250,249,245); INK=(61,57,41); TERRA=(217,119,87); GREY=(138,133,117); DARK=(38,36,28)
SERIF="/usr/share/fonts/truetype/google-fonts/Lora-Variable.ttf"; MONO="/home/claude/work/fonts/JetBrainsMono-Regular.ttf"
def F(p,s): return ImageFont.truetype(p,s)
IM="/home/claude/work/article/images/"
times=json.load(open("/home/claude/work/video/times.json"))

def wrap(d,text,font,maxw):
    out=[];cur=""
    for w in text.split():
        t=(cur+" "+w).strip()
        if d.textlength(t,font=font)<=maxw: cur=t
        else: out.append(cur); cur=w
    out.append(cur); return out

def layer(draw_fn,bg):
    im=Image.new("RGBA",(W,H),(0,0,0,0)); draw_fn(ImageDraw.Draw(im),im); return im

def text_layer(text,font,y,color,maxw=920,spacing=1.3,center=True):
    def fn(d,im):
        lines=wrap(d,text,font,maxw); lh=int(font.size*spacing); yy=y
        for ln in lines:
            w=d.textlength(ln,font=font); d.text(((W-w)/2 if center else 80,yy),ln,font=font,fill=color); yy+=lh
    return layer(fn,None)

def img_layer(path,y,width=1000):
    src=Image.open(path).convert("RGBA"); r=width/src.width; src=src.resize((width,int(src.height*r)),Image.LANCZOS)
    im=Image.new("RGBA",(W,H),(0,0,0,0)); im.paste(src,((W-width)//2,y)); return im, src.height

# scene definitions: bg, list of (layer, reveal_time_s)
scenes=[]
def S(bg,items): scenes.append((bg,items))
# 1 title
S(CREAM,[(text_layer("The Memory Squeeze",F(SERIF,104),640,INK,maxw=900,spacing=1.15),0.3),
         (text_layer("What AI-driven DRAM demand is doing to PC and console gaming",F(SERIF,46),1010,INK,maxw=860),1.6),
         (text_layer("19 NOV 2026  /  EVIDENCE-GRADED",F(MONO,30),1420,GREY),2.6)])
# 2 revenue
im,h=img_layer("/home/claude/work/video/vc-revenue.png",700,width=900)
S(CREAM,[(text_layer("DRAM revenue, Q3 2026",F(SERIF,70),300,INK,maxw=900),0.2),
         (text_layer("about $200B, up 369% year over year",F(SERIF,46),460,TERRA,maxw=900),1.2),
         (im,2.4),(text_layer("Counterpoint Research, 5 Nov 2026",F(MONO,28),700+h+50,GREY),5.0)])
# 3 retail
im,h=img_layer("/home/claude/work/video/vc-retail.png",700,width=900)
S(CREAM,[(text_layer("What shoppers see",F(SERIF,70),300,INK,maxw=900),0.2),
         (text_layer("Retail DDR5 kits, a year apart",F(SERIF,46),460,TERRA,maxw=900),1.2),
         (im,2.8),(text_layer("Secondhand tracker data: direction solid, dollars approximate",F(MONO,26),700+h+50,GREY,maxw=900),6.0)])
# 4 forecast
im,h=img_layer("/home/claude/work/video/vc-forecast.png",700,width=900)
S(CREAM,[(text_layer("Slower is not lower",F(SERIF,70),300,INK,maxw=900),0.2),
         (text_layer("TrendForce contract-price forecasts",F(SERIF,46),460,TERRA,maxw=900),1.2),
         (im,2.6),(text_layer("Forecast ranges, not outcomes",F(MONO,28),700+h+50,GREY),5.5)])
# 5 consoles
def con(d,im):
    rows=[("NINTENDO",["Switch 2 raised $450 to $500","No further increase planned","Says it can secure enough memory"]),("SONY",["PS5: 97.9M shipped, 2.6M last quarter","Memory secured through Apr 2027","PS6 'proceeding as scheduled'"])]
    y=720
    for name,ls in rows:
        d.rectangle([80,y,1000,y+4],fill=INK); d.text((90,y+30),name,font=F(MONO,38),fill=TERRA)
        yy=y+100
        for l in ls: d.text((90,yy),l,font=F(SERIF,46),fill=INK); yy+=70
        y+=420
im=layer(con,None); h=0
S(CREAM,[(text_layer("Nintendo and Sony",F(SERIF,70),300,INK,maxw=900),0.2),
         (text_layer("Earnings day, 5 November",F(SERIF,46),460,TERRA,maxw=900),1.2),
         (im,2.4),(text_layer("Company statements, via press coverage",F(MONO,28),1620,GREY),6.5)])
# 6 dark punctuation
S(DARK,[(text_layer("Why did Switch 2 sales fall 37%?",F(SERIF,84),560,CREAM,maxw=900),0.3),
        (text_layer("No source we found establishes the reason.",F(SERIF,52),1010,(236,232,220),maxw=860),2.6),
        (text_layer("Tariffs. Lifecycle. A thin release slate. Candidates, not findings.",F(MONO,30),1330,TERRA,maxw=860),5.5)])
# 7 know/think/dont
def kt(d,im):
    rows=[("WE KNOW","Memory prices are sharply up.",INK),("WE THINK","AI demand is a major driver.",INK),("WE DON'T KNOW","How long it lasts.",TERRA)]
    y=470
    for lab,tx,c in rows:
        d.text((90,y),lab,font=F(MONO,34),fill=GREY); d.text((90,y+60),tx,font=F(SERIF,64),fill=c); y+=330
S(CREAM,[(layer(kt,None),0.2)])
# 8 outro
S(CREAM,[(text_layer("Full article, claim ledger, and every source",F(SERIF,70),640,INK,maxw=860),0.3),
         (text_layer("Link in the description",F(SERIF,52),1080,TERRA,maxw=860),1.8),
         (text_layer("Narration: AI voice (Kokoro am_onyx). Music: original, synthesized.",F(MONO,24),1650,GREY,maxw=900),2.6)])
# staggered reveal for scene 7
scenes[6]=(CREAM,[(layer(lambda d,im:(d.text((90,470),"WE KNOW",font=F(MONO,34),fill=GREY),d.text((90,530),"Memory prices are sharply up.",font=F(SERIF,64),fill=INK)),None),0.2),
                  (layer(lambda d,im:(d.text((90,800),"WE THINK",font=F(MONO,34),fill=GREY),d.text((90,860),"AI demand is a major driver.",font=F(SERIF,64),fill=INK)),None),3.8),
                  (layer(lambda d,im:(d.text((90,1130),"WE DON'T KNOW",font=F(MONO,34),fill=GREY),d.text((90,1190),"How long it lasts.",font=F(SERIF,64),fill=TERRA)),None),6.2)])

total=sum(d for _,d in times)+0.0
nfr=int(round(total*FPS))
cmd=["ffmpeg","-y","-loglevel","error","-f","rawvideo","-pix_fmt","rgb24","-s",f"{W}x{H}","-r",str(FPS),"-i","-",
     "-an","-c:v","libx264","-preset","veryfast","-crf","19","-pix_fmt","yuv420p","/home/claude/work/video/silent.mp4"]
p=subprocess.Popen(cmd,stdin=subprocess.PIPE)
def alpha(im,a):
    if a>=1: return im
    arr=np.array(im); arr[...,3]=(arr[...,3]*a).astype(np.uint8); return Image.fromarray(arr,"RGBA")
for f in range(nfr):
    t=f/FPS; si=0
    for i,(s,d) in enumerate(times):
        if s<=t<s+d: si=i
    s0,dur=times[si]; lt=t-s0; bg,items=scenes[si]
    canvas=Image.new("RGBA",(W,H),bg+(255,))
    for lay,rt in items:
        a=max(0,min(1,(lt-rt)/0.45))
        if a<=0: continue
        off=int((1-a)*24)
        canvas.alpha_composite(alpha(lay,a),(0,off))
    # scene fade-out in the last 0.2s
    out=canvas.convert("RGB")
    p.stdin.write(out.tobytes())
p.stdin.close(); p.wait(); print("frames",nfr)
