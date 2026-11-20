import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib import font_manager as fm
import textwrap, numpy as np
OUT="/home/claude/work/article/images"
CREAM="#FAF9F5"; INK="#3D3929"; TERRA="#D97757"; GREY="#6f6a5a"; LIGHT="#E8E4D8"
SERIF="/usr/share/fonts/truetype/google-fonts/Lora-Variable.ttf"; MONO="/usr/share/fonts/truetype/dejavu/DejaVuSansMono.ttf"
for f in (SERIF,MONO): fm.fontManager.addfont(f)
serif=fm.FontProperties(fname=SERIF); mono=fm.FontProperties(fname=MONO)
plt.rcParams.update({"font.family":serif.get_name(),"text.color":INK,"axes.labelcolor":INK,"xtick.color":INK,"ytick.color":INK,"axes.edgecolor":INK,"figure.facecolor":CREAM,"axes.facecolor":CREAM})
def frame(title,sub,src,w=11,h=6.2):
    fig=plt.figure(figsize=(w,h),dpi=150)
    fig.text(0.05,0.93,title,fontsize=20,va="top",fontproperties=serif)
    fig.text(0.05,0.865,sub,fontsize=10,va="top",color=GREY,fontproperties=mono)
    fig.text(0.05,0.03,"\n".join(textwrap.wrap(src,150)),fontsize=7.5,va="bottom",color=GREY,fontproperties=mono)
    return fig
def style(ax):
    for s in ("top","right"): ax.spines[s].set_visible(False)
    ax.tick_params(length=0)

# 1 AMD gaming revenue
fig=frame("AMD Gaming revenue, three quarters","USD millions. Radeon graphics plus semi-custom (console) chips, as AMD defines the segment.",
 "Source: AMD Q3 2026 results release, 3 Nov 2026 (Q3'26 $773M, Q2'26 $779M, Q3'25 $1,298M). AMD does not split semi-custom from graphics.")
ax=fig.add_axes([0.1,0.22,0.55,0.55]); style(ax)
b=ax.bar(["Q3 2025","Q2 2026","Q3 2026"],[1298,779,773],color=[LIGHT,GREY,INK],edgecolor=INK,width=0.55,linewidth=1.2)
for r,t in zip(b,["$1,298M","$779M","$773M"]): ax.text(r.get_x()+r.get_width()/2,r.get_height()+25,t,ha="center",fontsize=12,fontproperties=mono)
ax.set_ylim(0,1500); ax.yaxis.grid(True,color=LIGHT); ax.set_axisbelow(True)
fig.text(0.7,0.66,"-40% Y/Y",fontsize=26,color=TERRA,va="top")
fig.text(0.7,0.55,"-1% Q/Q",fontsize=26,color=INK,va="top")
fig.text(0.7,0.43,"Most of the gap to a\nyear ago was already\nopen before Q3.\n(Our reading of two\nreported figures.)",fontsize=10,color=GREY,va="top",fontproperties=mono)
fig.savefig(f"{OUT}/chart-amd-gaming.png",facecolor=CREAM); plt.close(fig)

# 2 share of revenue
fig=frame("Gaming-related share of total revenue","Percent. The last bar is NOT the same thing as the others.",
 "Sources: AMD release (773/13,377; 1,298/9,246); Nvidia Q3 FY26 release (Gaming $4.3B of $57.0B); Nvidia Q3 FY27 release (Edge Computing $8.2B of $115.8B). Percentages are our arithmetic.")
ax=fig.add_axes([0.08,0.24,0.88,0.52]); style(ax)
labs=["AMD Gaming\nQ3 2025","AMD Gaming\nQ3 2026","Nvidia Gaming\nQ3 FY26 (Oct 2025)","Nvidia EDGE COMPUTING\nQ3 FY27 (Oct 2026)"]
vals=[14.0,5.8,7.5,7.1]
cols=[LIGHT,INK,LIGHT,CREAM]
b=ax.bar(labs,vals,color=cols,edgecolor=INK,width=0.55,linewidth=1.2)
b[3].set_hatch("///"); 
for r,v in zip(b,vals): ax.text(r.get_x()+r.get_width()/2,r.get_height()+0.4,f"{v}%",ha="center",fontsize=13,fontproperties=mono)
ax.set_ylim(0,17); ax.yaxis.grid(True,color=LIGHT); ax.set_axisbelow(True); ax.tick_params(axis="x",labelsize=9)
ax.annotate("Broader segment: adds workstation,\nautomotive, robotics, telecom,\nPC laptops. Gaming share unknown.",xy=(3.0,8.6),xytext=(1.75,12.8),fontsize=9,color=TERRA,fontproperties=mono,arrowprops=dict(arrowstyle="->",color=TERRA))
fig.savefig(f"{OUT}/chart-share.png",facecolor=CREAM); plt.close(fig)

# tables
def table(name,title,sub,src,header,rows,widths,h=6.2,fs=10.5):
    fig=frame(title,sub,src,h=h)
    ax=fig.add_axes([0.05,0.2,0.9,0.6]); ax.axis("off")
    x=0; xs=[]
    for w in widths: xs.append(x); x+=w
    y=1.0
    for i,t in enumerate(header): ax.text(xs[i],y,t,fontsize=fs,fontproperties=mono,color=TERRA,va="top",weight="bold")
    y-=0.1; ax.plot([0,1],[y+0.015,y+0.015],color=INK,lw=1.5)
    rh=0.9/len(rows)
    for r in rows:
        for i,t in enumerate(r):
            ax.text(xs[i],y,"\n".join(textwrap.wrap(t,int(widths[i]*(118 if i==0 else 80)))),fontsize=fs-0.5,va="top",fontproperties=serif if i==0 else mono)
        y-=rh; ax.plot([0,1],[y+0.015,y+0.015],color=LIGHT,lw=1)
    fig.savefig(f"{OUT}/{name}.png",facecolor=CREAM); plt.close(fig)

table("table-disclosure","What each company lets you see","Same industry, different disclosure. This is why the two numbers cannot be subtracted or compared.",
 "Sources: AMD Q3 2026 release; Nvidia Q3 FY27 release; Nvidia Q3 FY26 release. Quarter-end dates differ (AMD 26 Sep 2026; Nvidia 25 Oct 2026).",
 ["","AMD","Nvidia"],
 [["Gaming line reported?","Yes: 'Gaming' ($773M)","No. Folded into 'Edge Computing' since Q1 FY27"],
  ["What the line contains","Radeon GPUs and semi-custom console chips","PC and laptop products, GeForce, workstation, auto, robotics, telecom. No formal definition."],
  ["Latest figure","$773M, -40% Y/Y, -1% Q/Q","Edge Computing $8.2B, +42% Y/Y, +14% Q/Q"],
  ["Stated driver","'Lower semi-custom and graphics revenue'","Not stated for Q3. Q1 FY27: workstation demand up, consumer PC demand slower"],
  ["Gaming profit visible?","No (Client+Gaming combined: $573M, 15% margin)","No"]],
 [0.2,0.36,0.44])

table("table-hypotheses","Why did Nvidia's Edge Computing grow 42% while AMD Gaming fell 40%?","Competing explanations. The public disclosures do not choose between them.",
 "Reasoning table. Nvidia Q3 FY27 release lists RTX Spark laptops, DLSS 5 on GeForce, DGX Spark, automotive and robotics under the segment; no split is given. Q1 FY27 commentary via Wccftech quoting Nvidia.",
 ["Hypothesis","Support in sources","Status"],
 [["Edge growth is driven by non-gaming lines (workstation, robotics, automotive)","Nvidia cited workstation demand for Q1 FY27 growth; these lines sit in the same segment","Plausible, unquantified"],
  ["New PC products (RTX Spark laptops) added revenue","Nvidia says they ship from six PC makers; no revenue figure","Plausible, unquantified"],
  ["Gaming GPUs also grew","Nvidia's own Q1 FY27 text mentions slower consumer PC demand","Weakly contradicted (Q1 text only)"],
  ["The two companies' gaming businesses diverged","Both claims rest on different definitions and different quarters","Unsupported"],
  ["Higher selling prices lifted segment revenue","No source breaks out price versus units","Speculation"]],
 [0.3,0.5,0.2])

table("table-ledger","Claim ledger (summary)","Full ledger with alternatives is in the docs folder.",
 "Confidence scale: Confirmed, Strong inference, Weak inference, Speculation. Tier = source hierarchy of this project.",
 ["Claim","Source (tier)","Confidence"],
 [["AMD Gaming revenue was $773M in Q3 2026, down 40% Y/Y","AMD IR release (T1)","Confirmed"],
  ["AMD attributes the drop to 'lower semi-custom and graphics revenue'; no split given","AMD IR release (T1)","Confirmed"],
  ["Most of AMD's year-over-year gap predates Q3 (Q2 was $779M)","AMD IR release (T1) + arithmetic","Strong inference"],
  ["Nvidia no longer reports a separate Gaming segment","Nvidia releases (T1); PCGamesN, Wccftech (T2)","Confirmed"],
  ["Nvidia Edge Computing: $8.2B, +42% Y/Y in Q3 FY27","Nvidia IR release (T1)","Confirmed"],
  ["Edge growth says anything about gaming sales","None","Unsupported"],
  ["Memory/component costs weighed on PC demand late in AMD's quarter","Lisa Su via HWBusters transcript (T2, secondhand)","Confirmed as statement"],
  ["Why Nvidia changed its segments","Only 'better reflects growth drivers' (T1 via T2)","Not established"]],
 [0.5,0.32,0.18],h=6.8)

# cover
fig=plt.figure(figsize=(12,6.3),dpi=150); fig.patch.set_facecolor(INK)
fig.text(0.06,0.88,"GAME RESEARCH WRITER  /  20 NOV 2026",fontsize=12,color=TERRA,fontproperties=mono,va="top")
fig.text(0.06,0.74,"Two Ledgers,\nOne Market",fontsize=58,color=CREAM,va="top",fontproperties=serif)
fig.text(0.06,0.27,"What Nvidia's and AMD's latest earnings can,\nand cannot, tell us about gaming hardware",fontsize=20,color=LIGHT,va="top",fontproperties=serif)
fig.savefig(f"{OUT}/cover.png",facecolor=INK); plt.close(fig)
