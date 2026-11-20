import matplotlib; matplotlib.use("Agg")
import matplotlib.pyplot as plt, textwrap
from matplotlib import font_manager as fm
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch
OUT="/home/claude/work/article/images"
CREAM="#FAF9F5"; INK="#3D3929"; TERRA="#D97757"; GREY="#8A8575"; LIGHT="#E8E4D8"
SERIF="/usr/share/fonts/truetype/google-fonts/Lora-Variable.ttf"; MONO="/home/claude/work/fonts/JetBrainsMono-Regular.ttf"
for f in (SERIF,MONO): fm.fontManager.addfont(f)
serif=fm.FontProperties(fname=SERIF); mono=fm.FontProperties(fname=MONO)
plt.rcParams["font.family"]=serif.get_name()

# Causal chain
fig=plt.figure(figsize=(11,6.4),dpi=150,facecolor=CREAM)
fig.text(0.05,0.94,"From data-center demand to a gamer's price tag",fontsize=20,va="top",color=INK)
fig.text(0.05,0.875,"Each link is graded by the evidence that exists for it. Illustration of the argument, not data.",fontsize=10.5,va="top",color=GREY,fontproperties=mono)
ax=fig.add_axes([0,0,1,1]); ax.set_xlim(0,11); ax.set_ylim(0,6.4); ax.axis("off")
nodes=["AI server and data-center demand","DRAM makers shift advanced capacity to servers","Conventional DRAM contract prices rise","Retail RAM kits and device costs rise","Console and PC pricing, specs, and build choices change"]
conf=["Strong inference\n(TrendForce, Counterpoint)","Confirmed (forecast)\n(TrendForce)","Strong inference\n(retail trackers, secondhand)","Strong inference\n(company statements; tariffs\nand lifecycle also cited)"]
ys=[4.9,3.9,2.9,1.9,0.9]
for y,t in zip(ys,nodes):
    ax.add_patch(FancyBboxPatch((0.5,y-0.32),5.6,0.64,boxstyle="square,pad=0",fc=LIGHT if y!=ys[-1] else INK,ec=INK,lw=1.5))
    ax.text(0.65,y,"\n".join(textwrap.wrap(t,50)),va="center",fontsize=12.5,color=(INK if y!=ys[-1] else CREAM))
for i,c in enumerate(conf):
    y=(ys[i]+ys[i+1])/2
    ax.add_patch(FancyArrowPatch((3.3,ys[i]-0.34),(3.3,ys[i+1]+0.34),arrowstyle="-|>",mutation_scale=16,color=INK,lw=1.6))
    ax.text(6.5,y,c,va="center",fontsize=10,color=(TERRA if c.startswith("Strong") else INK),fontproperties=mono)
ax.text(0.5,0.18,"Not established by any source reviewed: that memory prices alone explain falling Switch 2 sales.",fontsize=10,color=GREY,fontproperties=mono)
fig.savefig(f"{OUT}/diagram-causal-chain.png",facecolor=CREAM); plt.close(fig)

# Cover (text-only, Claude register)
fig=plt.figure(figsize=(12,6.3),dpi=150,facecolor=CREAM)
ax=fig.add_axes([0,0,1,1]); ax.axis("off"); ax.set_xlim(0,12); ax.set_ylim(0,6.3)
ax.text(0.7,5.5,"GAME RESEARCH WRITER  /  19 NOV 2026",fontsize=11,color=GREY,fontproperties=mono,va="top")
ax.text(0.7,4.2,"The Memory Squeeze",fontsize=54,color=INK,va="center")
ax.text(0.7,3.0,"What AI-driven DRAM demand is doing to\nPC and console gaming, and what the\nevidence does not yet show",fontsize=20,color=INK,va="top",linespacing=1.4)
ax.text(0.7,0.6,"Evidence-graded analysis  |  claim ledger included",fontsize=11,color=TERRA,fontproperties=mono)
fig.savefig(f"{OUT}/cover.png",facecolor=CREAM); plt.close(fig)
print("ok")
