import soundfile as sf
from kokoro_onnx import Kokoro
k=Kokoro("kokoro-v1.0.onnx","voices-v1.0.bin")
lines=[
 "October 2026. Forty nine point nine percent of new Steam releases carried an AI disclosure.",
 "That is one month. For all of 2026 so far, it is forty point five percent.",
 "The flag is self reported. It covers AI content players see or hear, not coding tools. It can't say how much AI a game used.",
 "Flagged releases grew from twenty three hundred in 2024 to over twelve thousand this year. Why? The sources don't establish it. More AI, more disclosure, a different mix, or a rule change.",
 "So, half of new games use AI? The evidence doesn't say that. Read the full article.",
]
tot=0
for i,t in enumerate(lines,1):
    a,sr=k.create(t,voice="am_michael",speed=1.08,lang="en-us")
    sf.write(f"n{i}.wav",a,sr); d=len(a)/sr; tot+=d+0.6; print(i,round(d,2))
print("total",round(tot,1))
