import numpy as np, soundfile as sf, json
from kokoro_onnx import Kokoro
k=Kokoro("/home/claude/tts/kokoro.onnx","/home/claude/tts/voices.bin")
lines=[
 "AI is buying the world's memory. Here is what the evidence says that is doing to gaming.",
 "Counterpoint reports that D-RAM revenue reached about two hundred billion dollars last quarter. That is up three hundred sixty nine percent in a year, and it is driven by price, not volume.",
 "At retail, tracked prices for common D-D-R five kits are several times higher than a year ago. Those figures come secondhand, so the direction is solid and the exact dollars are approximate.",
 "TrendForce expects contract prices to keep rising this quarter, but more slowly. Slower is not the same as lower.",
 "Nintendo raised the Switch two to five hundred dollars and says it is not planning another increase. Sony says it has memory secured through April twenty twenty seven.",
 "Switch two sales fell about thirty seven percent. Why? No source we found establishes it. Tariffs, console lifecycle, and a thin release slate are all candidates.",
 "What we know: memory prices are sharply up. What we think: A-I demand is a major driver. What we do not know: how long it lasts.",
 "The full article, with the claim ledger and every source, is linked in the description.",
]
sr=24000; pad=int(0.45*sr); segs=[]; times=[]; t=0
for l in lines:
    s,_=k.create(l,voice="am_onyx",speed=0.97,lang="en-us")
    s=np.asarray(s,dtype=np.float32)
    lead=int(0.25*sr)
    seg=np.concatenate([np.zeros(lead,np.float32),s,np.zeros(pad,np.float32)])
    segs.append(seg); times.append((t,len(seg)/sr)); t+=len(seg)/sr
nar=np.concatenate(segs); sf.write("/home/claude/work/video/narration.wav",nar,sr)
json.dump(times,open("/home/claude/work/video/times.json","w")); print(times, t)

# music: original ambient pad, A minor-ish loop, 44.1k stereo
R=44100; dur=t+2.0; n=int(R*dur); tt=np.arange(n)/R
chords=[[220.0,261.63,329.63],[174.61,220.0,261.63],[196.0,246.94,293.66],[164.81,207.65,246.94]]
bar=6.0; m=np.zeros(n)
for i in range(int(dur/bar)+1):
    c=chords[i%4]; s0=int(i*bar*R); s1=min(n,int((i+1)*bar*R))
    if s0>=n: break
    x=tt[s0:s1]-i*bar; env=np.minimum(1,x/1.5)*np.minimum(1,(bar-x)/1.5)
    for f in c:
        for d in (-0.3,0.3):
            m[s0:s1]+=env*0.05*np.sin(2*np.pi*(f+d)*tt[s0:s1])
        m[s0:s1]+=env*0.03*np.sin(2*np.pi*(f/2)*tt[s0:s1])
# soft pulse every 1.5s
for b in np.arange(0.5,dur,1.5):
    s0=int(b*R); L=int(0.5*R)
    if s0+L>n: break
    x=np.arange(L)/R; m[s0:s0+L]+=0.04*np.exp(-x*7)*np.sin(2*np.pi*110*x)
m*=np.minimum(1,tt/2.0)*np.minimum(1,(dur-tt)/2.0)
# duck under narration
na=np.abs(np.interp(np.arange(n)/R,np.arange(len(nar))/sr,nar)); 
k_=int(0.25*R); env=np.convolve(na,np.ones(k_)/k_,mode="same"); env=np.clip(env*12,0,1)
m*=(1-0.55*env)
m=m/np.max(np.abs(m))*0.5
sf.write("/home/claude/work/video/music.wav",np.stack([m,m],1).astype(np.float32),R)
