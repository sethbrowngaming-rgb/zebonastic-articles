import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib import font_manager as fm
import glob
for f in glob.glob("/usr/share/fonts/truetype/google-fonts/ofl/dmsans/*.ttf"): fm.fontManager.addfont(f)
plt.rcParams["font.family"]="DM Sans"
SURF="#fcfcfb"; INK="#0b0b0b"; SEC="#52514e"; BLUE="#2a78d6"; ORG="#eb6834"
OUT="/home/claude/dlss5-hogwarts-legacy-2026/images/"

def loss(a,b): return round((a-b)/a*100,1)
rows=[
 ("NBA 2K27, Sept. build\nDigital Foundry via Notebookcheck\n4K Ultra", loss(128.4,62.7), "128.4 → 62.7 fps", ORG),
 ("NBA 2K27, Sept. build\nTechSpot, early-access copy\n4K", loss(192,76), "192 → 76 fps", ORG),
 ("Hogwarts Legacy, shipped Nov. 5\nDSOGaming, Hogsmeade (CPU-limited)\n4K, DLSS Quality", loss(123,98), "123 → 98 fps", BLUE),
 ("Hogwarts Legacy, shipped Nov. 5\nDSOGaming, opening area\n4K, DLSS Quality", loss(173,100), "173 → 100 fps", BLUE),
]
print(rows)
fig,ax=plt.subplots(figsize=(8,5),dpi=200,facecolor=SURF); ax.set_facecolor(SURF)
y=list(range(len(rows)))[::-1]
for yi,(lab,v,fps,c) in zip(y,rows):
    ax.barh(yi,v,height=0.5,color=c)
    ax.text(v+1.2,yi,f"−{v:.1f}%\n{fps}",va="center",fontsize=9.5,color=INK,linespacing=1.3)
ax.set_yticks(y); ax.set_yticklabels([r[0] for r in rows],fontsize=8.5,color=SEC)
ax.set_xlim(0,100); ax.set_xlabel("Measured frame-rate loss with DLSS 5 on, RTX 5090 (%)",fontsize=9,color=SEC)
for s in ("top","right","left"): ax.spines[s].set_visible(False)
ax.spines["bottom"].set_color("#cfcfca"); ax.tick_params(axis="y",length=0); ax.tick_params(axis="x",colors=SEC,labelsize=8)
ax.xaxis.grid(True,color="#e6e6e2",lw=0.8); ax.set_axisbelow(True)
from matplotlib.patches import Patch
fig.legend(handles=[Patch(color=ORG,label="September model, NBA 2K27"),Patch(color=BLUE,label="October model, shipped Hogwarts Legacy")],loc="lower center",ncol=2,fontsize=8.5,frameon=False,bbox_to_anchor=(0.62,0.0))
fig.suptitle("DLSS 5 frame-rate cost on an RTX 5090: four independent measurements",x=0.02,ha="left",fontsize=12.5,fontweight="bold",color=INK)
fig.text(0.02,0.90,"Different games, scenes and settings: bars are NOT a like-for-like comparison. Sources in article.",fontsize=8.5,color=SEC)
fig.subplots_adjust(left=0.40,right=0.97,top=0.84,bottom=0.17)
fig.savefig(OUT+"fig1-measured-cost-rtx5090.png",facecolor=SURF); plt.close(fig)

gpus=["RTX 5090","RTX 5080","RTX 5070 Ti","RTX 5070","RTX 5060 Ti 16GB","RTX 5060","RTX 5050"]
ms=[7.9,13.7,17.0,22.1,31.1,37.8,53.1]
fig,ax=plt.subplots(figsize=(8,4.6),dpi=200,facecolor=SURF); ax.set_facecolor(SURF)
y=list(range(len(gpus)))[::-1]
ax.barh(y,ms,height=0.55,color=ORG)
for yi,v in zip(y,ms): ax.text(v+0.8,yi,f"{v} ms",va="center",fontsize=10,color=INK,bbox=dict(facecolor=SURF,edgecolor="none",pad=1.5),zorder=5)
ax.axvline(16.7,color=SEC,lw=1,ls=(0,(4,3))); ax.text(17.3,len(gpus)-0.45,"16.7 ms = one frame at 60 fps",fontsize=8,color=SEC,va="center")
ax.set_yticks(y); ax.set_yticklabels(gpus,fontsize=9.5,color=INK); ax.set_xlim(0,64)
ax.set_xlabel("Estimated DLSS 5 cost per frame at 4K output (ms)",fontsize=9,color=SEC)
for s in ("top","right","left"): ax.spines[s].set_visible(False)
ax.spines["bottom"].set_color("#cfcfca"); ax.tick_params(axis="y",length=0); ax.tick_params(axis="x",colors=SEC,labelsize=8)
ax.xaxis.grid(True,color="#e6e6e2",lw=0.8); ax.set_axisbelow(True)
fig.suptitle("Estimated per-frame cost of the September DLSS 5 model, by GPU",x=0.02,ha="left",fontsize=12.5,fontweight="bold",color=INK)
fig.text(0.02,0.90,"TechSpot, NBA 2K27 early-access copy. Derived from frame-time differences, not direct measurement.",fontsize=8.5,color=SEC)
fig.subplots_adjust(left=0.22,right=0.97,top=0.83,bottom=0.14)
fig.savefig(OUT+"fig2-render-time-by-gpu.png",facecolor=SURF); plt.close(fig)
