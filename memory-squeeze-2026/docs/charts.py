import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib import font_manager as fm
from matplotlib.patches import FancyBboxPatch
import textwrap, os

OUT="/home/claude/work/article/images"
CREAM="#FAF9F5"; INK="#3D3929"; TERRA="#D97757"; GREY="#8A8575"; LIGHT="#E8E4D8"; BLUE="#6a9bcc"
SERIF="/usr/share/fonts/truetype/google-fonts/Lora-Variable.ttf"
MONO="/home/claude/work/fonts/JetBrainsMono-Regular.ttf"
for f in (SERIF,MONO): fm.fontManager.addfont(f)
serif=fm.FontProperties(fname=SERIF); mono=fm.FontProperties(fname=MONO)
plt.rcParams.update({"font.family":serif.get_name(),"text.color":INK,"axes.labelcolor":INK,
  "xtick.color":INK,"ytick.color":INK,"axes.edgecolor":INK,"figure.facecolor":CREAM,"axes.facecolor":CREAM})

def frame(title, sub, src, w=11, h=6.2):
    fig=plt.figure(figsize=(w,h),dpi=150)
    fig.text(0.05,0.93,title,fontsize=20,va="top",fontproperties=serif)
    fig.text(0.05,0.865,sub,fontsize=11,va="top",color=GREY,fontproperties=mono)
    fig.text(0.05,0.03,"\n".join(textwrap.wrap(src,138)),fontsize=8,va="bottom",color=GREY,fontproperties=mono)
    return fig

def style(ax):
    for s in ("top","right"): ax.spines[s].set_visible(False)
    ax.tick_params(length=0)

# 1 DRAM revenue
fig=frame("DRAM revenue, Q3 2025 vs Q3 2026","Counterpoint Research: ~$200B, +369% YoY. Q3 2025 value is derived (200 / 4.69).",
 "Source: Counterpoint Global Memory Tracker Q3 2026 (5 Nov 2026) via Counterpoint release and The Register. Prior-year bar is our arithmetic, not a published figure.")
ax=fig.add_axes([0.12,0.24,0.5,0.52]); style(ax)
v=[200/4.69,200]; b=ax.bar(["Q3 2025\n(derived)","Q3 2026"],v,color=[LIGHT,INK],width=0.55,edgecolor=INK,linewidth=1.2)
for r,t in zip(b,["≈ $43B","≈ $200B"]): ax.text(r.get_x()+r.get_width()/2,r.get_height()+4,t,ha="center",fontsize=14,fontproperties=mono)
ax.set_ylim(0,235); ax.set_ylabel("USD billions"); ax.yaxis.grid(True,color=LIGHT); ax.set_axisbelow(True)
fig.text(0.68,0.62,"Bit shipments:\n~+4% in the quarter",fontsize=15,color=TERRA,va="top")
fig.text(0.68,0.47,"Sources give 4% for\n'this quarter' without a\nstated base period, so it\nis not plotted against\nthe YoY revenue figure.",fontsize=10,color=GREY,va="top",fontproperties=mono)
fig.savefig(f"{OUT}/chart-dram-revenue.png",facecolor=CREAM); plt.close(fig)

# 2 market share
fig=frame("DRAM revenue share by supplier","Share of revenue, Q3 2025 vs Q3 2026 (Counterpoint, as reported).",
 "Sources: SammyGuru and XenoSpectrum citing Counterpoint. SK hynix 2025 value is reported as 'matched Samsung' (33%). Remainder (~3% in 2026) not itemized.")
ax=fig.add_axes([0.09,0.24,0.86,0.52]); style(ax)
names=["Samsung","SK hynix","Micron","CXMT"]; a=[33,33,26,5]; c=[38,29,21,9]
import numpy as np
x=np.arange(4); w=0.36
b1=ax.bar(x-w/2,a,w,color=LIGHT,edgecolor=INK,label="Q3 2025"); b2=ax.bar(x+w/2,c,w,color=INK,edgecolor=INK,label="Q3 2026")
for bs in (b1,b2):
    for r in bs: ax.text(r.get_x()+r.get_width()/2,r.get_height()+0.8,f"{int(r.get_height())}%",ha="center",fontsize=11,fontproperties=mono)
ax.set_xticks(x); ax.set_xticklabels(names,fontsize=13); ax.set_ylim(0,45); ax.yaxis.grid(True,color=LIGHT); ax.set_axisbelow(True)
ax.legend(frameon=False,loc="upper right",prop=mono)
fig.savefig(f"{OUT}/chart-dram-share.png",facecolor=CREAM); plt.close(fig)

# 3 retail kits
fig=frame("Retail DDR5 kits: Aug 2025 vs Aug 2026","Approximate prices in USD. Secondhand reporting of retail-tracker series.",
 "Sources: Tom's Hardware and TechTimes kit series as compiled by Tech Insider. The three kits differ in size and speed; percentages are not comparable across them.")
ax=fig.add_axes([0.09,0.24,0.86,0.52]); style(ax)
labs=["2x16GB\nDDR5-4800","2x32GB\nDDR5-5600","64GB (2x32GB)\nDDR5-6000"]; p0=[90,191,222]; p1=[425,1118,1272]
x=np.arange(3)
b1=ax.bar(x-w/2,p0,w,color=LIGHT,edgecolor=INK,label="Aug 2025"); b2=ax.bar(x+w/2,p1,w,color=INK,edgecolor=INK,label="Aug 2026")
for bs in (b1,b2):
    for r in bs: ax.text(r.get_x()+r.get_width()/2,r.get_height()+20,f"${int(r.get_height()):,}",ha="center",fontsize=10,fontproperties=mono)
for i,t in enumerate(["+372%","+485%","+473%"]): ax.text(i,max(p1[i],0)+130,t,ha="center",fontsize=13,color=TERRA,fontproperties=mono)
ax.set_xticks(x); ax.set_xticklabels(labs,fontsize=11); ax.set_ylim(0,1500); ax.yaxis.grid(True,color=LIGHT); ax.set_axisbelow(True)
ax.legend(frameon=False,loc="upper left",prop=mono)
fig.savefig(f"{OUT}/chart-retail-ddr5.png",facecolor=CREAM); plt.close(fig)

# 4 forecast deceleration
fig=frame("Contract-price growth is slowing, not reversing","TrendForce quarter-over-quarter forecast ranges, 3Q26 vs 4Q26.",
 "Sources: TrendForce 30 Sep 2026 (conventional DRAM, via Evertiq) and 11 Nov 2026 update (PC DRAM, via iConnect007/CryptoBriefing). Bars span the forecast range.")
ax=fig.add_axes([0.2,0.24,0.74,0.52]); style(ax)
rows=[("Conventional DRAM\n3Q26",13,18),("Conventional DRAM\n4Q26 (F)",10,15),("PC DRAM\n3Q26",18,23),("PC DRAM\n4Q26 (F)",13,18)]
for i,(l,lo,hi) in enumerate(rows[::-1]):
    ax.barh(i,hi-lo,left=lo,height=0.5,color=(INK if "(F)" in l else LIGHT),edgecolor=INK)
    ax.text(hi+0.6,i,f"+{lo}% to +{hi}%",va="center",fontsize=11,fontproperties=mono)
ax.set_yticks(range(4)); ax.set_yticklabels([r[0] for r in rows[::-1]],fontsize=11); ax.set_xlim(0,30); ax.set_xlabel("% change quarter over quarter")
ax.xaxis.grid(True,color=LIGHT); ax.set_axisbelow(True)
fig.savefig(f"{OUT}/chart-contract-forecast.png",facecolor=CREAM); plt.close(fig)

# tables
def table(name,title,sub,src,cols,rows,widths,h=None,fs=10):
    n=len(rows); h=h or (1.9+0.95*n)
    fig=plt.figure(figsize=(11,h),dpi=150)
    fig.text(0.04,0.97,title,fontsize=19,va="top",fontproperties=serif)
    fig.text(0.04,0.97-0.30/h*1.0,sub,fontsize=10,va="top",color=GREY,fontproperties=mono)
    fig.text(0.04,0.015,"\n".join(textwrap.wrap(src,150)),fontsize=7.5,va="bottom",color=GREY,fontproperties=mono)
    ax=fig.add_axes([0.04,0.09,0.92,0.97-0.09-0.75/h*1.0]); ax.axis("off"); ax.set_xlim(0,1); ax.set_ylim(0,n+1)
    xs=[0]; 
    for wd in widths: xs.append(xs[-1]+wd)
    for j,cn in enumerate(cols): ax.text(xs[j]+0.005,n+0.5,cn,fontsize=fs,va="center",fontproperties=mono,color=INK)
    ax.plot([0,1],[n+0.05,n+0.05],color=INK,lw=2)
    for i,row in enumerate(rows):
        y=n-i-0.5
        for j,cell in enumerate(row):
            wrapped="\n".join(textwrap.wrap(cell,int(widths[j]*118)))
            col=TERRA if (j==len(row)-1 and cell.startswith(("Strong","Weak","Spec"))) else INK
            ax.text(xs[j]+0.005,y,wrapped,fontsize=fs,va="center",color=col,fontproperties=(mono if j==len(row)-1 else serif))
        ax.plot([0,1],[n-i-1+0.02,n-i-1+0.02],color=LIGHT,lw=1)
    fig.savefig(f"{OUT}/{name}",facecolor=CREAM); plt.close(fig)

table("table-console-posture.png","What the two console makers said, 5 Nov 2026","Earnings-day statements on memory. Company statements are Tier 1/2; press paraphrase is flagged in the article.",
 "Sources: Nintendo briefing via GamesRadar, Nintendo Everything, GodisaGeek; Sony Q2 FY2026 results via Playday, GodisaGeek, Kotaku, Insider Gaming, Engadget.",
 ["Company","Reported hardware data","Memory statement","Price action"],
 [["Nintendo","Switch 2 first-half hardware sales down 37.4% YoY","President Furukawa: memory situation unchanged, enough secured; no further price increase under consideration","Switch 2 raised $450 to $500 earlier this fall"],
  ["Sony","PS5: 2.6M sell-in in Jul-Sep; cumulative 97.9M","CFO: memory secured for FY starting Apr 2027; offset cost rises via promotions, pricing, cost cuts","PS5 raised in March 2026 (US +$100, per Outlook Respawn)"]],
 [0.10,0.30,0.37,0.23],h=4.6)

table("table-supply-outlook.png","Who says the squeeze lasts how long","Forward-looking statements are forecasts, not measurements.",
 "Sources: TweakTown RAM-price hub (dates as listed there); TrendForce 30 Sep and 11 Nov 2026. Tiering follows GRW source hierarchy; attributions via TweakTown are secondhand.",
 ["Speaker","Date","Statement (paraphrased)","Source tier"],
 [["TrendForce","30 Sep 2026","PC DRAM supply could contract in 2027 as capacity shifts to servers","Tier 2 analyst release"],
  ["Samsung, Micron","3 Oct 2026","Shortages likely through at least 2028 (as headlined by TweakTown)","Tier 2, secondhand"],
  ["SK hynix CEO","31 Aug 2026","Memory crisis continues through 2030 (as listed by TweakTown)","Tier 2, secondhand"],
  ["Apple, TeamGroup","5 Nov 2026","Pressure could worsen through 2027; relief may not come until late 2028","Tier 2, secondhand"]],
 [0.17,0.13,0.45,0.25],h=5.2)

table("table-claim-ledger.png","Claim ledger (summary)","Every major claim, its evidence, and how far it can be trusted.",
 "Full ledger with alternative explanations is published alongside this article.",
 ["Claim","Evidence","Confidence"],
 [["Q3 2026 DRAM revenue was ~$200B, up 369% YoY","Counterpoint tracker, widely reproduced","Confirmed (as reported by analyst)"],
  ["Demand from AI data centers drove that growth","Counterpoint's stated attribution; TrendForce capacity-shift language","Strong inference"],
  ["Retail DDR5 kits cost several times more than a year ago","Tracker series via secondhand compilation","Strong inference"],
  ["Contract-price growth is decelerating","TrendForce 3Q vs 4Q forecast ranges","Confirmed (forecast)"],
  ["Memory costs drove console price increases","Company statements; tariffs also cited by Nintendo","Strong inference"],
  ["Switch 2 sales fell because of memory prices","No source establishes this","Speculation: removed"]],
 [0.40,0.38,0.22],h=6.4)
print("ok")
