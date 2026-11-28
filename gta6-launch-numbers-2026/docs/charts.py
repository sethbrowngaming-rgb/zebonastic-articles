import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from matplotlib import font_manager as fm
from matplotlib.patches import Patch
from matplotlib.lines import Line2D
import glob, datetime as dt

for f in glob.glob("/usr/share/fonts/truetype/google-fonts/ofl/dmsans/*.ttf"):
    fm.fontManager.addfont(f)
plt.rcParams["font.family"] = ["DM Sans", "DejaVu Sans"]
SURF = "#fcfcfb"; INK = "#0b0b0b"; SEC = "#52514e"; BLUE = "#2a78d6"; ORG = "#eb6834"; GREY = "#b9b8b2"
OUT = "/home/claude/gta6-launch-numbers-2026/images/"


def style_h(ax):
    for s in ("top", "right", "left"):
        ax.spines[s].set_visible(False)
    ax.spines["bottom"].set_color("#cfcfca")
    ax.tick_params(axis="y", length=0)
    ax.tick_params(axis="x", colors=SEC, labelsize=8)
    ax.xaxis.grid(True, color="#e6e6e2", lw=0.8)
    ax.set_axisbelow(True)


# ---------- Fig 1: the dollar figures side by side ----------
rows = [
    ("GTA V, 2013\nfirst 24 hours (Guinness)", 0.8157, GREY, "$0.82B"),
    ("Sensor Tower, Nov 16\nPS + Xbox digital, net of returns", 1.45, BLUE, "$1.45B"),
    ("Sensor Tower, at launch\n(19.05M units)", 1.84, BLUE, "$1.84B"),
    ("Sensor Tower, reported Nov 20\n(24.5M units, one source)", 2.36, BLUE, "$2.36B"),
    ("Take-Two, through end of Nov 19\n(\"day one retail sales\")", 3.79, ORG, "$3.79B"),
]
fig, ax = plt.subplots(figsize=(8.4, 5.0), dpi=200, facecolor=SURF)
ax.set_facecolor(SURF)
y = list(range(len(rows)))[::-1]
for yi, (lab, v, c, t) in zip(y, rows):
    ax.barh(yi, v, height=0.58, color=c)
    ax.text(v + 0.06, yi, t, va="center", fontsize=11, fontweight="bold", color=INK)
ax.set_yticks(y)
ax.set_yticklabels([r[0] for r in rows], fontsize=8.8, color=INK)
ax.set_xlim(0, 4.6)
ax.set_xlabel("Billions of US dollars, nominal (not adjusted for inflation)", fontsize=9, color=SEC)
style_h(ax)
fig.legend(handles=[Patch(color=ORG, label="Company estimate (Take-Two press release)"),
                    Patch(color=BLUE, label="Third-party estimate (Sensor Tower)"),
                    Patch(color=GREY, label="2013 comparison")],
           loc="lower center", ncol=3, fontsize=8, frameon=False, bbox_to_anchor=(0.5, 0.0))
fig.suptitle("Five dollar figures for one launch: they do not measure the same thing",
             x=0.02, ha="left", fontsize=12, fontweight="bold", color=INK)
fig.text(0.02, 0.905, "Different publishers of the numbers, scopes and cut-off times. Read the labels before comparing bar lengths.",
         fontsize=8.5, color=SEC)
fig.subplots_adjust(left=0.37, right=0.97, top=0.85, bottom=0.2)
fig.savefig(OUT + "fig1-five-dollar-figures.png", facecolor=SURF)
plt.close(fig)

# ---------- Fig 2: implied dollars per unit ----------
pts = [
    ("Sensor Tower\nNov 16", 1.45e9 / 14.94e6, BLUE),
    ("Sensor Tower\nat launch", 1.84e9 / 19.05e6, BLUE),
    ("Sensor Tower\nNov 20 report", 2.36e9 / 24.5e6, BLUE),
    ("Take-Two\n$3.79B / 32.5M", 3.79e9 / 32.5e6, ORG),
]
fig, ax = plt.subplots(figsize=(8.4, 4.8), dpi=200, facecolor=SURF)
ax.set_facecolor(SURF)
x = range(len(pts))
for xi, (lab, v, c) in zip(x, pts):
    ax.bar(xi, v, width=0.56, color=c)
    ax.text(xi, v - 8, f"\\${v:,.1f}", ha="center", fontsize=11, fontweight="bold", color="white")
ax.axhline(100, color=INK, lw=1.4, ls="--")
ax.text(-0.4, 103, "\\$99.99 Ultimate list price (US)", ha="left", fontsize=8.5, color=INK)
ax.axhline(80, color=SEC, lw=1.0, ls=":")
ax.text(0.0, 72, "dotted line = \\$79.99 standard list", ha="center", fontsize=8, color="white")
ax.set_xticks(list(x))
ax.set_xticklabels([p[0] for p in pts], fontsize=9, color=INK)
ax.set_ylim(0, 135)
ax.set_ylabel("Implied dollars per unit", fontsize=9, color=SEC)
for s in ("top", "right"):
    ax.spines[s].set_visible(False)
ax.spines["left"].set_color("#cfcfca"); ax.spines["bottom"].set_color("#cfcfca")
ax.tick_params(colors=SEC, labelsize=8)
ax.yaxis.grid(True, color="#e6e6e2", lw=0.8); ax.set_axisbelow(True)
fig.suptitle("Dollars divided by units: Sensor Tower lands near \\$96-97, Take-Two's pair at \\$116.6",
             x=0.02, ha="left", fontsize=11.5, fontweight="bold", color=INK)
fig.text(0.02, 0.905, "Simple division of each source's own dollar and unit figures. Take-Two's units are pre-release; its dollars run through end of launch day.",
         fontsize=8.2, color=SEC)
fig.subplots_adjust(left=0.09, right=0.97, top=0.84, bottom=0.14)
fig.savefig(OUT + "fig2-implied-dollars-per-unit.png", facecolor=SURF)
plt.close(fig)

# ---------- Fig 3: Sensor Tower trajectory vs the Take-Two point ----------
d = dt.date
st = [(d(2026, 8, 18), 0.429), (d(2026, 10, 13), 0.594), (d(2026, 10, 21), 0.630),
      (d(2026, 11, 16), 1.45), (d(2026, 11, 18), 1.65), (d(2026, 11, 19), 1.84)]
fig, ax = plt.subplots(figsize=(8.4, 4.8), dpi=200, facecolor=SURF)
ax.set_facecolor(SURF)
ax.plot([p[0] for p in st], [p[1] for p in st], color=BLUE, lw=2.2, marker="o", ms=6)
ax.plot([d(2026, 11, 19), d(2026, 11, 20)], [1.84, 2.36], color=BLUE, lw=1.6, ls=":")
ax.plot([d(2026, 11, 20)], [2.36], marker="o", ms=7, mfc=SURF, mec=BLUE, mew=2, ls="none")
ax.plot([d(2026, 11, 19)], [3.79], marker="D", ms=9, color=ORG, ls="none")
ax.annotate("Take-Two: $3.79B\n(company estimate, through end of Nov 19)", (d(2026, 11, 19), 3.79),
            xytext=(d(2026, 9, 14), 3.55), fontsize=8.8, color=INK,
            arrowprops=dict(arrowstyle="-", color=ORG, lw=1.2))
ax.annotate("Sensor Tower, Nov 19: $1.84B", (d(2026, 11, 19), 1.84), xytext=(d(2026, 9, 20), 2.35),
            fontsize=8.8, color=INK, arrowprops=dict(arrowstyle="-", color=BLUE, lw=1.0))
ax.annotate("Nov 20 report, one source:\n$2.36B (hollow marker)", (d(2026, 11, 20), 2.36), xytext=(d(2026, 10, 3), 2.95),
            fontsize=8.5, color=SEC, arrowprops=dict(arrowstyle="-", color=GREY, lw=1.0))
ax.set_ylim(0, 4.3)
ax.set_xlim(d(2026, 8, 10), d(2026, 11, 28))
ax.xaxis.set_major_locator(mdates.MonthLocator())
ax.xaxis.set_major_formatter(mdates.DateFormatter("%b %Y"))
ax.set_ylabel("Cumulative billions of US dollars", fontsize=9, color=SEC)
for s in ("top", "right"):
    ax.spines[s].set_visible(False)
ax.spines["left"].set_color("#cfcfca"); ax.spines["bottom"].set_color("#cfcfca")
ax.tick_params(colors=SEC, labelsize=8)
ax.yaxis.grid(True, color="#e6e6e2", lw=0.8); ax.set_axisbelow(True)
fig.suptitle("Sensor Tower's tracker climbed steadily; Take-Two's figure sits above the whole path",
             x=0.02, ha="left", fontsize=11.5, fontweight="bold", color=INK)
fig.text(0.02, 0.905, "Sensor Tower points are as reported in the press on the dates shown (PlayStation + Xbox, net of returns). Different measures from Take-Two's.",
         fontsize=8.2, color=SEC)
fig.subplots_adjust(left=0.09, right=0.97, top=0.84, bottom=0.11)
fig.savefig(OUT + "fig3-sensor-tower-trajectory.png", facecolor=SURF)
plt.close(fig)
print("charts ok")
