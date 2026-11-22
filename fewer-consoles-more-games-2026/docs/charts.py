import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib import font_manager as fm
import textwrap
OUT="/home/claude/work/article/images"
CREAM="#FAF9F5"; INK="#3D3929"; TERRA="#D97757"; GREY="#6f6a5a"; LIGHT="#E8E4D8"
SERIF="/usr/share/fonts/truetype/google-fonts/Lora-Variable.ttf"; MONO="/usr/share/fonts/truetype/dejavu/DejaVuSansMono.ttf"
for f in (SERIF,MONO): fm.fontManager.addfont(f)
serif=fm.FontProperties(fname=SERIF); mono=fm.FontProperties(fname=MONO)
plt.rcParams.update({"font.family":serif.get_name(),"text.color":INK,"axes.labelcolor":INK,"xtick.color":INK,"ytick.color":INK,"axes.edgecolor":INK,"figure.facecolor":CREAM,"axes.facecolor":CREAM})
def frame(title,sub,src,w=11,h=6.2):
    fig=plt.figure(figsize=(w,h),dpi=150)
    fig.text(0.05,0.94,title,fontsize=20,va="top",fontproperties=serif)
    fig.text(0.05,0.875,sub,fontsize=10,va="top",color=GREY,fontproperties=mono)
    fig.text(0.05,0.03,"\n".join(textwrap.wrap(src,150)),fontsize=7.5,va="bottom",color=GREY,fontproperties=mono)
    return fig
def style(ax):
    for s in ("top","right"): ax.spines[s].set_visible(False)
    ax.tick_params(length=0)

# 1. PS5 H1 sell-in by fiscal year
fig=frame("PS5 sell-in, April to September, by fiscal year","Millions of units shipped to the channel (Q1 + Q2). FY2020 omitted: the console launched in November 2020.",
 "Source: Sony Interactive Entertainment, Business Data & Sales page (cumulative 'more than 100 million' as of 10 Nov 2026). H1 = Q1 + Q2, our addition. Sell-in includes returned and refurbished units.")
ax=fig.add_axes([0.08,0.22,0.88,0.55]); style(ax)
labs=["FY2021","FY2022","FY2023","FY2024","FY2025","FY2026"]; vals=[5.6,5.7,8.2,6.2,6.5,4.2]
cols=[LIGHT]*5+[INK]
b=ax.bar(labs,vals,color=cols,edgecolor=INK,width=0.55,linewidth=1.2)
for r,v in zip(b,vals): ax.text(r.get_x()+r.get_width()/2,v+0.15,f"{v}M",ha="center",fontsize=12,fontproperties=mono)
ax.set_ylim(0,9.5); ax.yaxis.grid(True,color=LIGHT); ax.set_axisbelow(True)
ax.annotate("-35% vs FY2025 (our arithmetic)",xy=(5,4.5),xytext=(2.6,8.6),fontsize=10,color=TERRA,fontproperties=mono,arrowprops=dict(arrowstyle="->",color=TERRA))
fig.savefig(f"{OUT}/chart-ps5-h1.png",facecolor=CREAM); plt.close(fig)

# 2. PS5 yoy by quarter
fig=frame("PS5 sell-in, change versus the same quarter a year earlier","Percent. The decline did not start in the latest quarter.",
 "Source: Sony Interactive Entertainment Business Data & Sales page; percentages are our arithmetic. Sony announced price rises in Aug 2025 (about +$50 in the US) and effective 2 Apr 2026 (+$100 for PS5 base models in the US).")
ax=fig.add_axes([0.08,0.22,0.88,0.55]); style(ax)
labs=["Apr-Jun\n2025","Jul-Sep\n2025","Oct-Dec\n2025","Jan-Mar\n2026","Apr-Jun\n2026","Jul-Sep\n2026"]
vals=[4.2,5.3,-16.8,-46.4,-36.0,-35.0]
cols=[LIGHT,LIGHT,GREY,GREY,INK,INK]
b=ax.bar(labs,vals,color=cols,edgecolor=INK,width=0.55,linewidth=1.2)
for r,v in zip(b,vals):
    y=v+3 if v>0 else v-9
    ax.text(r.get_x()+r.get_width()/2,y,f"{v:+.1f}%",ha="center",fontsize=11,fontproperties=mono)
ax.axhline(0,color=INK,lw=1.2); ax.set_ylim(-58,18); ax.yaxis.grid(True,color=LIGHT); ax.set_axisbelow(True); ax.tick_params(axis="x",labelsize=9)
ax.annotate("Aug 2025 price rise\n(US +$50)",xy=(1,6),xytext=(0.2,-30),fontsize=9,color=TERRA,fontproperties=mono,arrowprops=dict(arrowstyle="->",color=TERRA))
ax.annotate("Price rise effective 2 Apr 2026\n(US +$100)",xy=(3.85,-12),xytext=(2.6,12),fontsize=9,color=TERRA,fontproperties=mono,arrowprops=dict(arrowstyle="->",color=TERRA))
fig.savefig(f"{OUT}/chart-ps5-yoy.png",facecolor=CREAM); plt.close(fig)

# 3. Nintendo H1 hardware vs software
fig=frame("Switch 2: hardware down, software up (April to September)","Millions of units, sell-in. Fiscal 2026 half = launch half-year (console launched 5 Jun 2025).",
 "Source: Nintendo six-month results, 5 Nov 2026 (hardware 6.49M, -37.4%; software 24.49M, +18.8%). Prior-year units derived from those percentages and Nintendo's cumulative data (10.36M; 20.62M). Software includes units bundled with hardware.")
ax=fig.add_axes([0.08,0.22,0.55,0.55]); style(ax)
import numpy as np
x=np.arange(2); w=0.36
b1=ax.bar(x-w/2,[10.36,20.62],w,color=LIGHT,edgecolor=INK,linewidth=1.2,label="Apr-Sep 2025")
b2=ax.bar(x+w/2,[6.49,24.49],w,color=INK,edgecolor=INK,linewidth=1.2,label="Apr-Sep 2026")
for bs in (b1,b2):
    for r in bs: ax.text(r.get_x()+r.get_width()/2,r.get_height()+0.5,f"{r.get_height():.2f}M",ha="center",fontsize=11,fontproperties=mono)
ax.set_xticks(x); ax.set_xticklabels(["Switch 2 hardware","Switch 2 software"],fontsize=11); ax.set_ylim(0,29); ax.yaxis.grid(True,color=LIGHT); ax.set_axisbelow(True)
ax.legend(frameon=False,prop=mono,fontsize=9,loc="upper left")
fig.text(0.68,0.70,"-37.4%",fontsize=28,color=TERRA,va="top"); fig.text(0.68,0.62,"hardware",fontsize=10,color=GREY,va="top",fontproperties=mono)
fig.text(0.68,0.52,"+18.8%",fontsize=28,color=INK,va="top"); fig.text(0.68,0.44,"software",fontsize=10,color=GREY,va="top",fontproperties=mono)
fig.text(0.68,0.34,"Installed base: 26.35M\nvs 10.36M a year ago\n(+154%, our arithmetic).\nSoftware grew far less\nthan the base did.",fontsize=9,color=GREY,va="top",fontproperties=mono)
fig.savefig(f"{OUT}/chart-switch2.png",facecolor=CREAM); plt.close(fig)

# 4. Nintendo second-half requirement
fig=frame("What Nintendo's unchanged forecast now requires","Switch 2 hardware, October to March. Millions of units.",
 "Sources: Nintendo FY2027 forecast 16.5M (unchanged, 5-6 Nov 2026); FY2026 total 19.86M; H1 FY2026 10.36M; H1 FY2027 6.49M. Second-half figures are our subtraction.")
ax=fig.add_axes([0.1,0.22,0.5,0.55]); style(ax)
b=ax.bar(["Oct 2025 - Mar 2026\n(actual, derived)","Oct 2026 - Mar 2027\n(needed to hit 16.5M)"],[9.50,10.01],color=[LIGHT,INK],edgecolor=INK,width=0.5,linewidth=1.2)
for r,t in zip(b,["9.50M","10.01M"]): ax.text(r.get_x()+r.get_width()/2,r.get_height()+0.2,t,ha="center",fontsize=13,fontproperties=mono)
ax.set_ylim(0,12); ax.yaxis.grid(True,color=LIGHT); ax.set_axisbelow(True); ax.tick_params(axis="x",labelsize=9)
fig.text(0.66,0.68,"+5.4%",fontsize=30,color=TERRA,va="top")
fig.text(0.66,0.56,"more than last year's\nsecond half, on a console\npriced higher and with\nmemory costs rising\nfrom Q3 (per Nintendo).",fontsize=10,color=GREY,va="top",fontproperties=mono)
fig.savefig(f"{OUT}/chart-nintendo-h2.png",facecolor=CREAM); plt.close(fig)

# tables
def table(name,title,sub,src,header,rows,widths,fs=10.5):
    cw=[int(w*105) for w in widths]
    wr=[[textwrap.wrap(t,max(8,int(cw[i]*(0.95 if i==0 else 0.8)))) for i,t in enumerate(r)] for r in rows]
    lines=[max(len(c) for c in r) for r in wr]
    unit=0.215
    body=sum(l*unit+0.18 for l in lines)
    H=1.9+body+0.55
    fig=plt.figure(figsize=(11,H),dpi=150)
    fig.text(0.05,1-0.3/H,title,fontsize=20,va="top",fontproperties=serif)
    fig.text(0.05,1-0.85/H,sub,fontsize=10,va="top",color=GREY,fontproperties=mono)
    fig.text(0.05,0.3/H,"\n".join(textwrap.wrap(src,150)),fontsize=7.5,va="bottom",color=GREY,fontproperties=mono)
    ax=fig.add_axes([0.05,0,0.9,1]); ax.axis("off"); ax.set_xlim(0,1); ax.set_ylim(0,H)
    xs=[];x=0
    for w in widths: xs.append(x); x+=w
    y=H-1.35
    for i,t in enumerate(header): ax.text(xs[i],y,t,fontsize=fs,fontproperties=mono,color=TERRA,va="top",weight="bold")
    y-=0.32; ax.plot([0,1],[y,y],color=INK,lw=1.5); y-=0.12
    for r,l,ws in zip(rows,lines,wr):
        for i,c in enumerate(ws):
            ax.text(xs[i],y,"\n".join(c),fontsize=fs-0.5,va="top",fontproperties=serif if i==0 else mono,linespacing=1.35)
        y-=l*unit+0.18; ax.plot([0,1],[y+0.07,y+0.07],color=LIGHT,lw=1)
    fig.savefig(f"{OUT}/{name}.png",facecolor=CREAM); plt.close(fig)

table("table-disclosure","What each company discloses, and how it defines it","Same industry, similar words, different measures.",
 "Sources: Nintendo six-month results presentation and Q&A summary (5-6 Nov 2026); Sony Interactive Entertainment Business Data & Sales page (updated 10 Nov 2026). Quarter ends: 30 Sep 2026 for both.",
 ["","Nintendo (Switch 2)","Sony (PS5)"],
 [["Hardware measure","Sell-in: sales by the Nintendo group to outside parties, including its own direct-sales websites","Sell-in: units shipped to the channel; includes returned and refurbished units"],
  ["Latest hardware figures","6.49M Apr-Sep (-37.4% Y/Y); 26.35M cumulative","2.6M Jul-Sep; 4.2M Apr-Sep (our sum); 97.9M cumulative to 30 Sep"],
  ["Software measure","Units, including software bundled with hardware","PS4 + PS5 units, physical and digital, including bundled software"],
  ["Latest software figures","24.49M Apr-Sep (+18.8% Y/Y)","88.2M Jul-Sep; 127M monthly active users (SIE estimate)"],
  ["Sell-through (what players bought)","Not published; Furukawa spoke qualitatively about Japan","Not published"],
  ["Holiday quarter","Not yet reported; forecast unchanged","Not yet reported; 'more than 100M' by 10 Nov"]],
 [0.2,0.4,0.4])

table("table-hypotheses","Why did console hardware shipments fall?","Competing explanations. The disclosures do not choose between them.",
 "Reasoning table built from Nintendo's Q&A summary (6 Nov 2026), Sony's published data, and coverage cited in the Sources section. 'Status' reflects how directly a source supports the claim.",
 ["Hypothesis","What supports it","What cuts against it","Status"],
 [["Lifecycle and launch concentration: buyers who wanted a console already bought one","Nintendo said launch-year sales were unusually concentrated and forecast a decline. Sony's CFO described PS5 sales as declining as expected at this life-cycle stage (secondhand report).","Does not explain the speed. PS5 shipments fell 35-46% in each of the last three quarters.","Stated by both firms; magnitude unexplained"],
  ["Price rises reduced demand","Both firms raised prices in 2026. Nintendo's May guidance cited price revisions beside launch concentration. PS5 Y/Y shipments were -36% in the quarter after the Apr 2026 rise.","Sony's decline began in Oct-Dec 2025, before that rise. Nintendo's November materials did not apportion its half-year decline to price.","Plausible contributor; not shown"],
  ["Purchases were pulled forward ahead of price rises","Furukawa described a Japan sell-through spike before the May rise, then a settling.","Outside Japan, Nintendo said the Sept rise was announced early and came with bundles, so the before/after gap was smaller.","Supported for Japan only"],
  ["Memory and component costs limited supply","Reuters tied Sony's rise to memory costs. Nintendo flagged rising component costs.","Nintendo placed the higher procurement cost impact from Q3 and the Q&A summary does not cite supply limits for Jul-Sep.","Not established for the quarter"],
  ["Weaker consumer demand for hardware generally","Secondary outlets cite the economy.","Nintendo's presentation does not state it; no sell-through data.","Unsupported"]],
 [0.24,0.31,0.3,0.15],fs=10)

table("table-ledger","Claim ledger (summary)","The full ledger, with evidence and alternative explanations, is in the docs folder.",
 "Confidence: Confirmed = stated in a Tier 1 source; Strong inference = arithmetic on Tier 1 figures; Weak inference = plausible, thinly supported. Tier 1 = company filings and data pages.",
 ["Claim","Source (tier)","Confidence"],
 [["Switch 2 H1 hardware sell-in was 6.49M, down 37.4%","Nintendo results (T1)","Confirmed"],
  ["Switch 2 H1 software was 24.49M, up 18.8%","Nintendo results (T1)","Confirmed"],
  ["Nintendo kept its 16.5M forecast, which needs about 10.01M in Oct-Mar","Nintendo (T1) + subtraction","Strong inference"],
  ["Nintendo apportioned the H1 decline to price rises","Not stated in Nov presentation or Q&A (T1); May guidance cited price among reasons (T2)","Not established"],
  ["PS5 shipped 2.6M in Jul-Sep vs 4.0M a year earlier (-35%)","SIE data page (T1) + arithmetic","Confirmed"],
  ["PS5 decline began before the April 2026 price rise","SIE data page (T1), quarterly","Strong inference"],
  ["PS5 passed 100M cumulative sell-in by 10 Nov 2026","SIE data page (T1)","Confirmed"],
  ["Software growth shows deeper engagement per player","None","Unsupported"],
  ["Price rises caused the fall in shipments","None direct","Not established"]],
 [0.5,0.32,0.18])

# cover
fig=plt.figure(figsize=(12,6.3),dpi=150); fig.patch.set_facecolor(INK)
fig.text(0.06,0.88,"GAME RESEARCH WRITER  /  21 NOV 2026",fontsize=12,color=TERRA,fontproperties=mono,va="top")
fig.text(0.06,0.74,"Fewer Consoles,\nMore Games?",fontsize=56,color=CREAM,va="top",fontproperties=serif)
fig.text(0.06,0.27,"What Nintendo's and Sony's September-quarter\nreports do, and do not, show about hardware",fontsize=20,color=LIGHT,va="top",fontproperties=serif)
fig.savefig(f"{OUT}/cover.png",facecolor=INK); plt.close(fig)
print("done")
