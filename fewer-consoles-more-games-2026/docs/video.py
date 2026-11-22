import numpy as np, soundfile as sf, subprocess
from PIL import Image, ImageDraw, ImageFont
from kokoro_onnx import Kokoro
W,H=1080,1920
CREAM=(250,249,245); INK=(61,57,41); TERRA=(217,119,87); GREY=(111,106,90); DARK=(38,36,28); LIGHT=(236,232,220)
SERIF="/usr/share/fonts/truetype/google-fonts/Lora-Variable.ttf"
MONO="/usr/share/fonts/truetype/dejavu/DejaVuSansMono-Bold.ttf"
F=lambda p,s: ImageFont.truetype(p,s)
OUT="/home/claude/work/video/"
def wrap(d,t,f,mw):
    o=[];c=""
    for w in t.split():
        x=(c+" "+w).strip()
        if d.textlength(x,font=f)<=mw: c=x
        else: o.append(c); c=w
    o.append(c); return o
def txt(d,t,f,y,col,mw=900,x=90,sp=1.25):
    for ln in wrap(d,t,f,mw):
        d.text((x,y),ln,font=f,fill=col); y+=int(f.size*sp)
    return y
def scene(bg,fn):
    im=Image.new("RGB",(W,H),bg); d=ImageDraw.Draw(im); fn(d); return im
def border(d,col=INK): d.rectangle([40,40,W-40,H-40],outline=col,width=8)

def s1(d):
    border(d); d.text((90,120),"GAME RESEARCH WRITER / 21 NOV 2026",font=F(MONO,28),fill=TERRA)
    txt(d,"FEWER CONSOLES,",F(MONO,84),520,INK); txt(d,"MORE GAMES?",F(MONO,84),630,INK)
    d.rectangle([90,790,990,800],fill=INK)
    txt(d,"Nintendo and Sony just reported. Hardware is down. Software is up. What do the numbers really show?",F(SERIF,50),850,INK)
def s2(d):
    border(d); d.text((90,120),"NINTENDO / SWITCH 2 / APR-SEP 2026",font=F(MONO,30),fill=TERRA)
    d.text((90,300),"-37.4%",font=F(MONO,200),fill=INK)
    txt(d,"hardware shipments",F(SERIF,60),560,INK)
    d.rectangle([90,700,990,706],fill=INK)
    d.text((90,760),"+18.8%",font=F(MONO,150),fill=GREY)
    txt(d,"software units",F(SERIF,60),940,GREY)
    txt(d,"Both measure shipments into stores, not what players bought.",F(SERIF,46),1180,INK)
    d.text((90,1700),"SOURCE: NINTENDO, 5 NOV 2026",font=F(MONO,26),fill=GREY)
def s3(d):
    border(d); d.text((90,120),"THE CATCH",font=F(MONO,30),fill=TERRA)
    d.text((90,300),"+154%",font=F(MONO,200),fill=INK)
    txt(d,"Switch 2 installed base, year on year",F(SERIF,56),560,INK)
    d.rectangle([90,800,990,806],fill=INK)
    d.rectangle([90,880,990,1040],outline=TERRA,width=8); d.text((120,925),"SOFTWARE: +18.8%",font=F(MONO,56),fill=TERRA)
    txt(d,"Software grew far less than the base. That does not show deeper engagement.",F(SERIF,46),1140,INK)
    d.text((90,1700),"OUR ARITHMETIC: 26.35M VS 10.36M",font=F(MONO,26),fill=GREY)
def s4(d):
    border(d); d.text((90,120),"SONY / PS5 / VS YEAR-AGO QUARTER",font=F(MONO,30),fill=TERRA)
    vals=[("Q3 FY25",-17),("Q4 FY25",-46),("Q1 FY26",-36),("Q2 FY26",-35)]
    y=280
    for lab,v in vals:
        d.text((90,y),lab,font=F(MONO,34),fill=GREY)
        wbar=int(abs(v)/46*560)
        d.rectangle([330,y-4,330+wbar,y+50],fill=INK if lab!="Q3 FY25" and lab!="Q4 FY25" else GREY)
        d.text((330+wbar+20,y),f"{v}%",font=F(MONO,40),fill=INK); y+=100
    d.rectangle([90,720,990,726],fill=INK)
    d.rectangle([90,790,990,990],outline=TERRA,width=8); d.text((120,825),"DECLINE PREDATES",font=F(MONO,48),fill=TERRA); d.text((120,895),"THE APRIL PRICE RISE",font=F(MONO,48),fill=TERRA)
    txt(d,"2.6 million PS5s shipped in July to September, down 35%. The slide began late last year.",F(SERIF,46),1070,INK)
    d.text((90,1700),"SOURCE: SONY INTERACTIVE, SELL-IN",font=F(MONO,26),fill=GREY)
def s5(d):
    txt(d,"Why did shipments fall?",F(SERIF,96),420,CREAM,sp=1.2)
    txt(d,"Lifecycle. Price. Channel orders. The reports do not say which.",F(SERIF,56),900,LIGHT)
    d.text((90,1350),"CAUSE NOT ESTABLISHED",font=F(MONO,38),fill=TERRA)
def s6(d):
    border(d)
    rows=[("WE KNOW","Shipments fell. Prices rose.",INK),("WE THINK","Lifecycle is part of it.",INK),("WE DON'T KNOW","What players bought. The holiday result.",TERRA)]
    y=300
    for lab,t,c in rows:
        d.text((90,y),lab,font=F(MONO,40),fill=GREY); txt(d,t,F(SERIF,64),y+70,c); y+=430
def s7(d):
    border(d)
    txt(d,"FULL ARTICLE, CLAIM LEDGER AND SOURCES",F(MONO,60),620,INK)
    d.rectangle([90,900,990,906],fill=INK)
    txt(d,"Link in the description",F(SERIF,62),960,TERRA)
S=[(CREAM,s1,"Nintendo and Sony just reported. Console shipments are down, and software is up. So is the business shifting from hardware to games?"),
   (CREAM,s2,"Nintendo says Switch 2 hardware shipments fell thirty seven percent in the half year, while software units rose nearly nineteen percent. Both count shipments, not what players bought."),
   (CREAM,s3,"But the installed base grew about one hundred fifty four percent. Software grew far less than that, so it does not show deeper engagement."),
   (CREAM,s4,"Sony shipped two point six million PlayStation 5s last quarter, down thirty five percent. And the slide started late last year, before the April price rise."),
   (DARK,s5,"So why did shipments fall? Lifecycle, price, or channel orders. The reports do not say."),
   (CREAM,s6,"What we know: shipments fell and prices rose. What we think: lifecycle is part of it. What we don't know: what players bought, or how the holiday quarter goes."),
   (CREAM,s7,"Full article, claim ledger and sources. Link in the description.")]
k=Kokoro("/home/claude/work/models/kokoro-v1.0.onnx","/home/claude/work/models/voices-v1.0.bin")
SR=24000; GAP=0.4
audio=[];durs=[]
for i,(bg,fn,t) in enumerate(S):
    a,sr=k.create(t,voice="am_onyx",speed=1.0,lang="en-us"); assert sr==SR
    a=np.concatenate([np.zeros(int(0.25*SR)),a,np.zeros(int(GAP*SR))]); audio.append(a); durs.append(len(a)/SR)
    scene(bg,fn).save(f"{OUT}s{i}.png")
total=sum(durs); print("durs",[round(x,1) for x in durs],"total",round(total,1))
assert total<59, total
nar=np.concatenate(audio)
t=np.arange(len(nar))/SR
def tone(f,amp): return amp*np.sin(2*np.pi*f*t)
pad=tone(110,.5)+tone(164.81,.35)+tone(130.81,.3)+tone(55,.45)
pad*=0.6+0.4*np.sin(2*np.pi*0.12*t)
beat=(np.sin(2*np.pi*55*t)*np.exp(-((t*1.2)%1)*9))*0.5
mus=(pad+beat); mus/=np.max(np.abs(mus)); mus*=0.12
fade=np.minimum(1,np.minimum(t/1.5,(total-t)/2.0)); mus*=fade
mix=nar/np.max(np.abs(nar))*0.9+mus
mix/=max(1,np.max(np.abs(mix))/0.97)
sf.write(OUT+"mix.wav",mix,SR)
with open(OUT+"list.txt","w") as f:
    for i,dr in enumerate(durs): f.write(f"file 's{i}.png'\nduration {dr:.3f}\n")
    f.write(f"file 's{len(durs)-1}.png'\n")
subprocess.run(["ffmpeg","-y","-loglevel","error","-f","concat","-safe","0","-i",OUT+"list.txt","-i",OUT+"mix.wav","-vf","fps=30,format=yuv420p","-c:v","libx264","-preset","veryfast","-crf","20","-c:a","aac","-b:a","160k","-shortest",OUT+"fewer-consoles-short.mp4"],check=True)
print("ok")
