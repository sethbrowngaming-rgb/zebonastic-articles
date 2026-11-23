import soundfile as sf, numpy as np
from kokoro_onnx import Kokoro
k=Kokoro("kokoro.onnx","voices.bin")
lines=[
 "March. Nvidia reveals DLSS 5. Critics say it rewrites character faces.",
 "November fifth. Hogwarts Legacy ships it. Nvidia's own comparison images show changes mostly in lighting and materials.",
 "Per Nvidia, developers control the model, the intensity, and masks that can exclude faces. Players get one switch: on, or off.",
 "Independent tests of the September model on an RTX 5090 show up to sixty percent frame rate loss. Shipped Hogwarts: twenty to forty two percent. Different games, so not a fair comparison.",
 "What's settled? The difference is documented. The reason is not. Settings, a retrained model, or both? Read the full article.",
]
tot=0
for i,t in enumerate(lines,1):
    a,sr=k.create(t,voice="am_michael",speed=1.05,lang="en-us")
    sf.write(f"n{i}.wav",a,sr); d=len(a)/sr; tot+=d+0.45; print(i,round(d,2))
print("total with pads",round(tot,1))
