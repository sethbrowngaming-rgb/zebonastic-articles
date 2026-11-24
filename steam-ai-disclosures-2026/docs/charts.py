import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib import font_manager as fm
from matplotlib.patches import Patch
import glob
for f in glob.glob("/usr/share/fonts/truetype/google-fonts/ofl/dmsans/*.ttf"): fm.fontManager.addfont(f)
plt.rcParams["font.family"]="DM Sans"
SURF="#fcfcfb"; INK="#0b0b0b"; SEC="#52514e"; BLUE="#2a78d6"; ORG="#eb6834"; GREY="#b9b8b2"
OUT="/home/claude/steam-ai-disclosures-2026/images/"

def style(ax):
    for s in ("top","right","left"): ax.spines[s].set_visible(False)
    ax.spines["bottom"].set_color("#cfcfca")
    ax.tick_params(axis="y",length=0); ax.tick_params(axis="x",colors=SEC,labelsize=8)
    ax.xaxis.grid(True,color="#e6e6e2",lw=0.8); ax.set_axisbelow(True)

# Fig 1: share of new releases disclosing AI, months vs years (kept visually distinct)
rows=[("Jan 2024  (one month)",1.7,ORG),
      ("2024  (full year)",13.3,BLUE),
      ("2025  (full year)",24.0,BLUE),
      ("Oct 2025  (one month)",26.4,ORG),
      ("2026 through Nov 24  (partial year)",40.5,BLUE),
      ("Oct 2026  (one month)",49.9,ORG)]
fig,ax=plt.subplots(figsize=(8,4.8),dpi=200,facecolor=SURF); ax.set_facecolor(SURF)
y=list(range(len(rows)))[::-1]
for yi,(lab,v,c) in zip(y,rows):
    ax.barh(yi,v,height=0.58,color=c); ax.text(v+1,yi,f"{v:.1f}%",va="center",fontsize=10.5,fontweight="bold",color=INK)
ax.set_yticks(y); ax.set_yticklabels([r[0] for r in rows],fontsize=9.5,color=INK)
ax.set_xlim(0,60); ax.set_xlabel("Share of new Steam releases carrying an AI disclosure (%)",fontsize=9,color=SEC)
style(ax)
fig.legend(handles=[Patch(color=ORG,label="Single-month figure"),Patch(color=BLUE,label="Whole-year or year-to-date figure")],loc="lower center",ncol=2,fontsize=8.5,frameon=False,bbox_to_anchor=(0.55,0.0))
fig.suptitle("Steam AI disclosure rate: the 49.9% is one month; the year-to-date figure is 40.5%",x=0.02,ha="left",fontsize=12,fontweight="bold",color=INK)
fig.text(0.02,0.90,"Self-reported disclosure flag, not verified AI use. Months and years are different measures; do not read as one line.",fontsize=8.5,color=SEC)
fig.subplots_adjust(left=0.34,right=0.97,top=0.84,bottom=0.19)
fig.savefig(OUT+"fig1-disclosure-share-by-period.png",facecolor=SURF); plt.close(fig)

# Fig 2: counts of disclosing vs non-disclosing releases
yrs=["2024","2025","2026\n(to Nov 24)"]
disc=[2319,4937,12351]; non=[15073,15615,18123]
fig,ax=plt.subplots(figsize=(8,4.8),dpi=200,facecolor=SURF); ax.set_facecolor(SURF)
x=range(3)
ax.bar(x,non,width=0.55,color=GREY,label="Releases without an AI disclosure")
ax.bar(x,disc,width=0.55,bottom=non,color=ORG,label="Releases with an AI disclosure")
for i in x:
    ax.text(i,non[i]/2,f"{non[i]:,}",ha="center",va="center",fontsize=10,color=INK)
    ax.text(i,non[i]+disc[i]/2,f"{disc[i]:,}",ha="center",va="center",fontsize=10,color=INK,fontweight="bold")
    ax.text(i,non[i]+disc[i]+500,f"total {non[i]+disc[i]:,}",ha="center",fontsize=8.5,color=SEC)
ax.set_xticks(list(x)); ax.set_xticklabels(yrs,fontsize=10,color=INK)
ax.set_ylim(0,35500); ax.set_ylabel("New Steam releases",fontsize=9,color=SEC)
for s in ("top","right"): ax.spines[s].set_visible(False)
ax.spines["left"].set_color("#cfcfca"); ax.spines["bottom"].set_color("#cfcfca"); ax.tick_params(colors=SEC,labelsize=8)
ax.yaxis.grid(True,color="#e6e6e2",lw=0.8); ax.set_axisbelow(True)
ax.legend(loc="upper left",fontsize=8.5,frameon=False)
fig.suptitle("Where the growth is: disclosing releases rose far faster than the rest",x=0.02,ha="left",fontsize=12,fontweight="bold",color=INK)
fig.text(0.02,0.90,"Counts from the PCGame.com statistics page (data as of Nov 24, 2026). 2026 is a partial year. Non-disclosing = flag not set.",fontsize=8.5,color=SEC)
fig.subplots_adjust(left=0.10,right=0.97,top=0.84,bottom=0.12)
fig.savefig(OUT+"fig2-disclosing-vs-other-counts.png",facecolor=SURF); plt.close(fig)

# Fig 3: disclosure rate by current review count (2026 releases)
b=[("Fewer than 10",8981,19176),("10 to 49",2119,6393),("50 to 99",432,1533),("100 to 999",708,2635),("1,000 or more",109,724)]
fig,ax=plt.subplots(figsize=(8,4.4),dpi=200,facecolor=SURF); ax.set_facecolor(SURF)
y=list(range(len(b)))[::-1]
for yi,(lab,a,n) in zip(y,b):
    v=a/n*100; ax.barh(yi,v,height=0.55,color=ORG); ax.text(v+1,yi,f"{v:.0f}%   ({a:,} of {n:,})",va="center",fontsize=9.5,color=INK)
ax.set_yticks(y); ax.set_yticklabels([r[0]+" reviews" for r in b],fontsize=9.5,color=INK)
ax.set_xlim(0,75); ax.set_xlabel("Share of 2026 releases with an AI disclosure (%)",fontsize=9,color=SEC)
style(ax)
fig.suptitle("Games with few reviews disclose AI far more often",x=0.02,ha="left",fontsize=12,fontweight="bold",color=INK)
fig.text(0.02,0.89,"2026 releases through Nov 24; size = current Steam review count. Review count is also affected by release date and by player reaction.",fontsize=8.2,color=SEC)
fig.subplots_adjust(left=0.22,right=0.97,top=0.82,bottom=0.15)
fig.savefig(OUT+"fig3-disclosure-by-review-count.png",facecolor=SURF); plt.close(fig)

# Fig 4: uses named in disclosures
u=[("Art",63),("Text and translations",32),("Store page and marketing",27),("Music and sound",22),("Code",17),("Voices",8),("AI active during play",3)]
fig,ax=plt.subplots(figsize=(8,4.6),dpi=200,facecolor=SURF); ax.set_facecolor(SURF)
y=list(range(len(u)))[::-1]
for yi,(lab,v) in zip(y,u):
    ax.barh(yi,v,height=0.55,color=BLUE); ax.text(v+1,yi,f"{v}%",va="center",fontsize=10,color=INK)
ax.set_yticks(y); ax.set_yticklabels([r[0] for r in u],fontsize=9.5,color=INK)
ax.set_xlim(0,80); ax.set_xlabel("Share of 10,723 analyzed disclosures naming each use (%)",fontsize=9,color=SEC)
style(ax)
fig.suptitle("What disclosing developers say the AI was used for",x=0.02,ha="left",fontsize=12,fontweight="bold",color=INK)
fig.text(0.02,0.895,"2026 releases. Bars overlap (one disclosure can name several uses) and sum to more than 100%. Vague statements are excluded.",fontsize=8.3,color=SEC)
fig.subplots_adjust(left=0.30,right=0.97,top=0.83,bottom=0.14)
fig.savefig(OUT+"fig4-uses-named-in-disclosures.png",facecolor=SURF); plt.close(fig)
print("charts ok")
