import numpy as np, soundfile as sf, subprocess, os
SR=44100
durs=[];nar=[]
for i in range(1,6):
    a,sr=sf.read(f"n{i}.wav"); 
    if sr!=SR:
        import scipy.signal as ss; a=ss.resample_poly(a,SR,sr)
    nar.append(a); durs.append(len(a)/SR+0.45+0.15)
print([round(x,2) for x in durs], sum(durs))
# narration track
parts=[]
for a,dsc in zip(nar,durs):
    n=int(dsc*SR); t=np.zeros(n); s=int(0.15*SR); t[s:s+len(a)]=a/np.max(np.abs(a))*0.9; parts.append(t)
voice=np.concatenate(parts); T=len(voice)/SR
# music bed: original synth
t=np.arange(len(voice))/SR
def sine(f,amp): return amp*np.sin(2*np.pi*f*t)
pad=sine(55,.5)+sine(82.41,.35)+sine(110,.3)+sine(130.81,.22)+sine(164.81,.15)
pad*=0.75+0.25*np.sin(2*np.pi*t/6)
beat=60/84; ph=(t%beat)/beat
pulse=np.sin(2*np.pi*55*t)*np.exp(-ph*7)*0.9
hat=(np.random.RandomState(1).randn(len(t)))*np.exp(-(((t%(beat/2))/(beat/2))*30))*0.05
music=pad*0.5+pulse*0.5+hat
music/=np.max(np.abs(music)); music*=0.13
fade=np.minimum(1,np.minimum(t/1.5,(T-t)/2.0)); music*=fade
mix=voice+music; mix/=max(1,np.max(np.abs(mix))/0.97)
sf.write("mix.wav",mix,SR)
# scenes
for i,dsc in enumerate(durs,1):
    tmp=f"s{i}.tmp.mp4"
    subprocess.run(["ffmpeg","-y","-v","error","-framerate","30","-i",f"f{i}.png","-vf",f"format=yuv420p,loop=-1:1,trim=duration={dsc:.3f},fade=t=in:st=0:d=0.2","-c:v","libx264","-crf","18","-preset","veryfast","-pix_fmt","yuv420p","-r","30",tmp],check=True)
    os.rename(tmp,f"s{i}.mp4")
open("list.txt","w").write("".join(f"file 's{i}.mp4'\n" for i in range(1,6)))
subprocess.run("ffmpeg -y -v error -f concat -safe 0 -i list.txt -c copy v.tmp.mp4 && mv v.tmp.mp4 v.mp4",shell=True,check=True)
subprocess.run("ffmpeg -y -v error -i v.mp4 -i mix.wav -map 0:v -map 1:a -c:v copy -c:a aac -b:a 160k -shortest out.tmp.mp4 && mv out.tmp.mp4 final.mp4",shell=True,check=True)
