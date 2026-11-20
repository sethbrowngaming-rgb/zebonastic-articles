import numpy as np, soundfile as sf, subprocess, json
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
def frame_border(d,col=INK): d.rectangle([40,40,W-40,H-40],outline=col,width=8)

def s1(d):
    frame_border(d); d.text((90,120),"GAME RESEARCH WRITER / 20 NOV 2026",font=F(MONO,28),fill=TERRA)
    txt(d,"TWO LEDGERS,",F(MONO,92),560,INK); txt(d,"ONE MARKET",F(MONO,92),680,INK)
    d.rectangle([90,840,990,850],fill=INK)
    txt(d,"Nvidia and AMD just reported. What can the numbers actually tell us about gaming hardware?",F(SERIF,50),900,INK)
def s2(d):
    frame_border(d); d.text((90,120),"AMD / GAMING / Q3 2026",font=F(MONO,30),fill=TERRA)
    d.text((90,330),"-40%",font=F(MONO,260),fill=INK)
    txt(d,"Y/Y, to $773M",F(SERIF,64),640,INK)
    d.rectangle([90,800,990,806],fill=INK)
    d.text((90,860),"Q2 2026:  $779M",font=F(MONO,56),fill=GREY); d.text((90,950),"Q3 2026:  $773M",font=F(MONO,56),fill=INK)
    txt(d,"The drop appears to predate the quarter. The release gives no split between console chips and graphics.",F(SERIF,46),1140,INK)
    d.text((90,1700),"SOURCE: AMD IR, 3 NOV 2026",font=F(MONO,26),fill=GREY)
def s3(d):
    frame_border(d); d.text((90,120),"NVIDIA / EDGE COMPUTING / Q3 FY27",font=F(MONO,30),fill=TERRA)
    d.text((90,330),"+42%",font=F(MONO,260),fill=INK)
    txt(d,"Y/Y, to $8.2B",F(SERIF,64),640,INK)
    d.rectangle([90,800,990,806],fill=INK)
    d.rectangle([90,880,990,1040],outline=TERRA,width=8); d.text((120,925),"NO GAMING LINE",font=F(MONO,60),fill=TERRA)
    txt(d,"Edge also holds workstations, laptops, robotics, cars and telecom. Its growth is not evidence about gaming.",F(SERIF,46),1140,INK)
    d.text((90,1700),"SOURCE: NVIDIA IR, 17 NOV 2026",font=F(MONO,26),fill=GREY)
def s4(d):
    txt(d,"Shrinking at one, booming at the other?",F(SERIF,92),500,CREAM,sp=1.2)
    txt(d,"Different definitions. Different quarters. Not comparable.",F(SERIF,54),1050,LIGHT)
    d.text((90,1400),"NOT SUPPORTED BY THE EVIDENCE",font=F(MONO,36),fill=TERRA)
def s5(d):
    frame_border(d)
    rows=[("WE KNOW","AMD's numbers. Nvidia's change.",INK),("WE THINK","AMD's drop started earlier.",INK),("WE DON'T KNOW","Why. Or Nvidia's gaming revenue.",TERRA)]
    y=300
    for lab,t,c in rows:
        d.text((90,y),lab,font=F(MONO,40),fill=GREY); txt(d,t,F(SERIF,66),y+70,c); y+=420
def s6(d):
    frame_border(d)
    txt(d,"FULL ARTICLE, CLAIM LEDGER AND SOURCES",F(MONO,60),620,INK)
    d.rectangle([90,900,990,906],fill=INK)
    txt(d,"Link in the description",F(SERIF,62),960,TERRA)
S=[(CREAM,s1,"Two chip makers. Two earnings reports. One confusing picture."),
   (CREAM,s2,"AMD says gaming revenue fell forty percent, to seven hundred seventy three million dollars. But last quarter it was seven seventy nine. Most of the drop was already there."),
   (CREAM,s3,"Nvidia says its Edge Computing segment grew forty two percent. But Nvidia no longer reports gaming on its own. That segment also holds workstations, robotics and cars."),
   (DARK,s4,"So is gaming shrinking at one company and booming at the other? The evidence does not say that."),
   (CREAM,s5,"What we know: AMD's numbers. What we think: AMD's drop started earlier. What we don't know: why, or what Nvidia's gaming revenue is."),
   (CREAM,s6,"Full article, claim ledger and sources. Link in the description.")]
k=Kokoro("/home/claude/work/models/kokoro.onnx","/home/claude/work/models/voices.bin")
SR=24000; GAP=0.45
audio=[];durs=[]
for i,(bg,fn,t) in enumerate(S):
    a,sr=k.create(t,voice="am_onyx",speed=1.0,lang="en-us"); assert sr==SR
    a=np.concatenate([np.zeros(int(0.25*SR)),a,np.zeros(int(GAP*SR))]); audio.append(a); durs.append(len(a)/SR)
    scene(bg,fn).save(f"{OUT}s{i}.png")
total=sum(durs); print("durs",[round(x,1) for x in durs],"total",round(total,1))
assert total<59, total
nar=np.concatenate(audio)
# original synthesized music: slow minor pad + soft pulse
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
subprocess.run(["ffmpeg","-y","-loglevel","error","-f","concat","-safe","0","-i",OUT+"list.txt","-i",OUT+"mix.wav","-vf","fps=30,format=yuv420p","-c:v","libx264","-preset","veryfast","-crf","20","-c:a","aac","-b:a","160k","-shortest",OUT+"two-ledgers-short.mp4"],check=True)
print("ok")
