import soundfile as sf
from kokoro_onnx import Kokoro
k=Kokoro("kokoro-v1.0.onnx","voices-v1.0.bin")
lines=[
 "Take-Two says Grand Theft Auto 6 made three point seven nine billion dollars on day one.",
 "Sensor Tower's tracker shows one point eight four billion at launch, and a reported two point three six billion a day later.",
 "Different scopes. Take-Two doesn't define retail sales. The tracker counts PlayStation and Xbox digital only.",
 "Take-Two's own pair of numbers implies one hundred sixteen dollars per game. List price tops out at one hundred.",
 "So why the gap? The sources document it but do not establish the reason. Read the full article.",
]
for i,t in enumerate(lines,1):
    a,sr=k.create(t,voice="am_michael",speed=1.08,lang="en-us")
    sf.write(f"n{i}.wav",a,sr); print(i,round(len(a)/sr,2))
