import matplotlib; matplotlib.use("Agg")
import matplotlib.pyplot as plt, numpy as np
from matplotlib import font_manager as fm
OUT="/home/claude/work/video/"
CREAM="#FAF9F5"; INK="#3D3929"; TERRA="#D97757"; GREY="#8A8575"; LIGHT="#E8E4D8"
SERIF="/usr/share/fonts/truetype/google-fonts/Lora-Variable.ttf"; MONO="/home/claude/work/fonts/JetBrainsMono-Regular.ttf"
for f in (SERIF,MONO): fm.fontManager.addfont(f)
mono=fm.FontProperties(fname=MONO)
plt.rcParams.update({"font.family":fm.FontProperties(fname=SERIF).get_name(),"figure.facecolor":CREAM,"axes.facecolor":CREAM,"text.color":INK,"xtick.color":INK,"ytick.color":INK,"axes.edgecolor":INK})
def mk():
    fig=plt.figure(figsize=(8.4,8.4),dpi=125); ax=fig.add_axes([0.14,0.14,0.82,0.80])
    for s in("top","right"): ax.spines[s].set_visible(False)
    ax.tick_params(length=0,labelsize=20); ax.set_axisbelow(True); return fig,ax
# revenue
fig,ax=mk(); b=ax.bar(["Q3 2025\n(derived)","Q3 2026"],[200/4.69,200],color=[LIGHT,INK],edgecolor=INK,linewidth=2,width=0.6)
for r,t in zip(b,["≈ $43B","≈ $200B"]): ax.text(r.get_x()+r.get_width()/2,r.get_height()+5,t,ha="center",fontsize=30,fontproperties=mono)
ax.set_ylim(0,240); ax.yaxis.grid(True,color=LIGHT); ax.set_ylabel("USD billions",fontsize=20); fig.savefig(OUT+"vc-revenue.png"); plt.close(fig)
# retail
fig,ax=mk(); x=np.arange(3); w=0.38; p0=[90,191,222]; p1=[425,1118,1272]
ax.bar(x-w/2,p0,w,color=LIGHT,edgecolor=INK,linewidth=2,label="Aug 2025"); ax.bar(x+w/2,p1,w,color=INK,edgecolor=INK,label="Aug 2026")
for i,t in enumerate(["+372%","+485%","+473%"]): ax.text(i+w/2,p1[i]+40,t,ha="center",fontsize=26,color=TERRA,fontproperties=mono)
ax.set_xticks(x); ax.set_xticklabels(["2x16GB\nDDR5-4800","2x32GB\nDDR5-5600","64GB\nDDR5-6000"],fontsize=19); ax.set_ylim(0,1500); ax.yaxis.grid(True,color=LIGHT)
ax.set_yticks([0,500,1000,1500]); ax.set_yticklabels(["$0","$500","$1,000","$1,500"]); ax.legend(frameon=False,loc="upper left",prop={"family":"monospace","size":20}); fig.savefig(OUT+"vc-retail.png"); plt.close(fig)
# forecast
fig,ax=mk(); ax.set_position([0.26,0.14,0.70,0.80]); rows=[("PC DRAM\n4Q26 (forecast)",13,18,True),("PC DRAM\n3Q26",18,23,False)]
for i,(l,lo,hi,f) in enumerate(rows):
    ax.barh(i,hi-lo,left=lo,height=0.5,color=INK if f else LIGHT,edgecolor=INK,linewidth=2); ax.text(lo-0.6,i,f"+{lo}% to +{hi}%",fontsize=24,fontproperties=mono,ha="right",va="center")
ax.set_yticks([0,1]); ax.set_yticklabels([r[0] for r in rows],fontsize=19); ax.set_xlim(0,26); ax.set_ylim(-0.6,1.6); ax.set_xlabel("% change, quarter over quarter",fontsize=20); ax.xaxis.grid(True,color=LIGHT)
fig.savefig(OUT+"vc-forecast.png"); plt.close(fig)
print("ok")
