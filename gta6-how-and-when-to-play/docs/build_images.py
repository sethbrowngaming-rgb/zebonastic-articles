"""Build all static images (charts + tables) for the GTA VI How & When to Play article.
Every time value is computed from the rule 'midnight local time on Nov 19, 2026'
(Rockstar Support) using the IANA tz database, not typed by hand."""
import sys, textwrap, json
from datetime import datetime, timedelta
from zoneinfo import ZoneInfo
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib import font_manager as fm

OUT = sys.argv[1]
FONTS = "/home/claude/work/fonts"
fm.fontManager.addfont(f"{FONTS}/EBGaramond.ttf")
fm.fontManager.addfont(f"{FONTS}/EBGaramond-Italic.ttf")
SERIF = "EB Garamond"
MONO = "DejaVu Sans Mono"

CREAM, INK, TERRA, BLUE, GREEN, GREY = "#FAF9F5", "#3D3929", "#D97757", "#6a9bcc", "#788c5d", "#B9B4A4"
TERRA_TINT, BLUE_TINT, GREY_TINT = "#F6E3DA", "#E4EDF5", "#EFECE2"
UTC = ZoneInfo("UTC")

REGIONS = [
    ("New Zealand (Auckland)", "Pacific/Auckland"),
    ("Australia (Sydney)", "Australia/Sydney"),
    ("Japan / South Korea", "Asia/Tokyo"),
    ("Singapore", "Asia/Singapore"),
    ("India", "Asia/Kolkata"),
    ("UAE (Dubai)", "Asia/Dubai"),
    ("Central Europe (DE, FR)", "Europe/Berlin"),
    ("United Kingdom", "Europe/London"),
    ("Brazil (Sao Paulo)", "America/Sao_Paulo"),
    ("US Eastern", "America/New_York"),
    ("US Central", "America/Chicago"),
    ("US Mountain", "America/Denver"),
    ("US Pacific", "America/Los_Angeles"),
]
US = {"US Eastern", "US Central", "US Mountain", "US Pacific"}

def unlock(tz):  # midnight local on Nov 19, 2026
    return datetime(2026, 11, 19, 0, 0, tzinfo=ZoneInfo(tz))

def fmt(dt, tz):
    l = dt.astimezone(ZoneInfo(tz))
    day = "Nov 19" if l.day == 19 else "Nov 18"
    return f"{day}, {l.strftime('%-I:%M %p')}"

rows = []
for name, tz in REGIONS:
    u = unlock(tz)
    rows.append(dict(name=name, tz=tz, utc=u.astimezone(UTC)))
ET0 = unlock("America/New_York").astimezone(UTC)
for r in rows:
    r["lead_vs_et_h"] = (ET0 - r["utc"]).total_seconds() / 3600
cloud = datetime(2026, 11, 19, 1, 0, tzinfo=ZoneInfo("America/New_York")).astimezone(UTC)

json.dump(
    {r["name"]: dict(utc=r["utc"].isoformat(), lead_vs_et_h=r["lead_vs_et_h"]) for r in rows}
    | {"xbox_cloud_utc": cloud.isoformat()},
    open(f"{OUT}/computed_times.json", "w"), indent=1)

# ---------- generic helpers ----------
def base_fig(w=16, h=9):
    fig = plt.figure(figsize=(w, h), dpi=100, facecolor=CREAM)
    return fig

def draw_table(path, title, subtitle, headers, body, fracs, footnote="", tints=None, mono_cols=(), fs=15, hfs=14, mono_fs=12.5):
    W = 1600
    pad = 22
    colx = [0]
    for f in fracs:
        colx.append(colx[-1] + f * (W - 2 * 40))
    colw = [colx[i + 1] - colx[i] for i in range(len(fracs))]
    fs_px = fs * 100 / 72
    line_h = fs_px * 1.28

    def wrap(text, wpx, size_px, factor=0.53):
        cpl = max(4, int((wpx - 2 * 16) / (size_px * factor)))
        return textwrap.wrap(text, cpl) or [""]

    hdr_lines = [wrap(h, colw[i], hfs * 100 / 72) for i, h in enumerate(headers)]
    hdr_h = max(len(l) for l in hdr_lines) * hfs * 100 / 72 * 1.25 + 26
    wrapped, heights = [], []
    for row in body:
        wr = [wrap(str(c), colw[i], (mono_fs if i in mono_cols else fs) * 100 / 72, 0.62 if i in mono_cols else 0.53) for i, c in enumerate(row)]
        wrapped.append(wr)
        heights.append(max(len(c) * ((mono_fs * 100 / 72 * 1.35) if i in mono_cols else fs_px * 1.7) for i, c in enumerate(wr)) + pad)
    title_h = 128 if subtitle else 80
    foot_lines = textwrap.wrap(footnote, 150) if footnote else []
    foot_h = len(foot_lines) * 26 + 30 if foot_lines else 20
    H = int(title_h + hdr_h + sum(heights) + foot_h + 30)
    fig = plt.figure(figsize=(W / 100, H / 100), dpi=100, facecolor=CREAM)
    ax = fig.add_axes([0, 0, 1, 1]); ax.set_xlim(0, W); ax.set_ylim(H, 0); ax.axis("off")
    ax.text(40, 38, title, fontsize=30, family=SERIF, color=INK, va="top")
    if subtitle:
        ax.text(40, 90, subtitle, fontsize=15, family=SERIF, style="italic", color="#6b6552", va="top")
    y = title_h
    ax.add_patch(plt.Rectangle((40, y), W - 80, hdr_h, color=INK))
    for i, lines in enumerate(hdr_lines):
        ax.text(40 + colx[i] + 16, y + 13, "\n".join(lines), fontsize=hfs, family=SERIF, color=CREAM, va="top", fontweight="bold")
    y += hdr_h
    for ri, (wr, h) in enumerate(zip(wrapped, heights)):
        tint = (tints or {}).get(ri)
        ax.add_patch(plt.Rectangle((40, y), W - 80, h, color=tint or (CREAM if ri % 2 == 0 else "#F3F1E8")))
        ax.plot([40, W - 40], [y + h, y + h], color=GREY, lw=0.8)
        for ci, lines in enumerate(wr):
            ax.text(40 + colx[ci] + 16, y + pad / 2, "\n".join(lines), fontsize=(mono_fs if ci in mono_cols else fs),
                    family=MONO if ci in mono_cols else SERIF, color=INK, va="top", linespacing=1.28)
        y += h
    ax.plot([40, W - 40], [y, y], color=INK, lw=2)
    for k, l in enumerate(foot_lines):
        ax.text(40, y + 22 + k * 26, l, fontsize=12.5, family=SERIF, style="italic", color="#6b6552", va="top")
    fig.savefig(path, facecolor=CREAM)
    plt.close(fig)

# ---------- TABLE 1: unlock times ----------
hdr = ["Region", "Unlock (local)", "UTC", "US Eastern", "US Central", "US Mountain", "US Pacific"]
body, tints = [], {}
for i, r in enumerate(rows):
    star = " †" if r["name"] in US and r["name"] != "US Eastern" else ""
    body.append([r["name"] + star, "Nov 19, 12:00 AM",
                 r["utc"].strftime("%b %-d, %H:%M"),
                 fmt(r["utc"], "America/New_York"), fmt(r["utc"], "America/Chicago"),
                 fmt(r["utc"], "America/Denver"), fmt(r["utc"], "America/Los_Angeles")])
    if r["name"].startswith("New Zealand"):
        tints[i] = TERRA_TINT
draw_table(f"{OUT}/table-unlock-times.png",
           "GTA VI unlock times if the game unlocks at local midnight",
           "Derived from Rockstar Support's rule (midnight local time, Nov 19, 2026, PS5 and Xbox Series X|S). Rockstar publishes no regional table.",
           hdr, body, [0.185, 0.135, 0.115, 0.14, 0.14, 0.14, 0.145],
           "† Under the local-midnight rule. Secondary reporting of PlayStation Store listings (GTAVice via Vice) shows a single nationwide US unlock at midnight Eastern (9 PM Pacific on Nov 18), which conflicts with per-zone midnight for Central, Mountain and Pacific. "
           "Xbox per-country hours were not found in the sources reviewed. Check your own store's countdown. US was on standard time on these dates; New Zealand on NZDT (UTC+13).",
           tints=tints, mono_cols=(1, 2, 3, 4, 5, 6), fs=15)

# ---------- TABLE 2: native vs cloud ----------
cl_utc = cloud.strftime("%H:%M UTC")
draw_table(f"{OUT}/table-native-vs-cloud.png",
           "Three ways to play: what each route documents",
           "Only Xbox Series X|S can install the game; Xbox One is cloud-only.",
           ["Route", "Documented start", "Requirements stated", "Source"],
           [["PS5 (native)", "Midnight local, Nov 19", "Digital pre-load opened Nov 10 at midnight local; code-in-box needs activation", "Rockstar Support; Rockstar Newswire"],
            ["Xbox Series X|S (native)", "Midnight local, Nov 19", "Pre-load opened globally at 12 a.m. GMT on Nov 10; up to 212 GB depending on device", "Rockstar Support; Rockstar Newswire"],
            ["Xbox Series X|S (Xbox Cloud Gaming)", f"1 a.m. ET, Nov 19 ({cl_utc})", "Game bought separately; Series S graphics settings when streamed; availability may vary by market", "Xbox Wire, Nov 10"],
            ["Xbox One (Xbox Cloud Gaming)", f"1 a.m. ET, Nov 19 ({cl_utc})", "Cloud-only, no native version; cloud playtime purchasable from Nov 11 in supported markets; whether Game Pass is required for this title is not stated", "Xbox Wire, Nov 10"]],
           [0.22, 0.2, 0.40, 0.18],
           "Not documented in any source reviewed: whether changing an Xbox console's location changes when Xbox Cloud Gaming streaming opens for GTA VI. The Xbox Wire post gives one start time and no time zone other than ET.",
           tints={2: BLUE_TINT, 3: BLUE_TINT}, fs=15)

# ---------- TABLE 3: claim ledger summary ----------
draw_table(f"{OUT}/table-claim-ledger.png",
           "Claim ledger summary: how much each statement is worth",
           "Evidence tiers: 1 = official/primary, 2 = industry journalism, 3 = community measurement, 4 = forums/social media.",
           ["Claim", "Evidence and source", "Tier", "Confidence"],
           [["Release date is Nov 19, 2026 on PS5 and Xbox Series X|S", "Rockstar Newswire; Rockstar Support", "1", "Confirmed"],
            ["Unlock is midnight local time in all regions, both platforms", "Rockstar Support regional release times article", "1", "Confirmed"],
            ["Rockstar published a per-region unlock table", "The Rockstar article contains no regional table", "1", "Not found"],
            ["New Zealand unlocks at 11:00 UTC on Nov 18 (6 AM ET, 3 AM PT)", "Arithmetic from the Rockstar rule and NZDT = UTC+13", "1 (rule)", "Strong inference"],
            ["US PS5 unlocks at midnight Eastern nationwide", "PlayStation Store listings as relayed by GTAVice, Vice, Ginx; Rockstar says local midnight", "2-3", "Weak inference (conflicting)"],
            ["Xbox Cloud streaming starts 1 a.m. ET Nov 19 on Xbox One and Series X|S", "Xbox Wire, Nov 10 and Nov 13", "1", "Confirmed"],
            ["Cloud version uses Xbox Series S graphics settings", "Xbox Wire, Nov 10", "1", "Confirmed"],
            ["The NZ trick lets Xbox players start early", "Xbox Reddit thread relayed by Vice, Yahoo, Cybernews, Newsweek; no Rockstar or Microsoft statement", "4 via 2", "Reported, unverified"],
            ["The NZ trick causes PS5 account suspensions", "Reports unverified per Vice; no Sony statement found", "4", "Speculation"],
            ["The NZ trick shifts the Xbox Cloud start time", "No source addresses it", "none", "Unknown"]],
           [0.34, 0.40, 0.07, 0.19], "", tints={7: TERRA_TINT, 8: GREY_TINT, 9: GREY_TINT}, fs=15)

# ---------- TABLE 4: discrepancies ----------
draw_table(f"{OUT}/table-source-conflicts.png",
           "Where published sources disagree",
           "These conflicts are why the article leans on Rockstar Support and Xbox Wire first.",
           ["Topic", "What one source says", "What the primary source says", "Our handling"],
           [["New Zealand unlock date", "MP1st lists New Zealand as Nov 18 at 12:00 AM", "Rockstar: midnight local on Nov 19", "Treated as a likely error; Auckland midnight Nov 19 is Nov 18 in the US"],
            ["One global moment", "GameGPU reports a simultaneous release at 05:00 UTC on Nov 19", "Rockstar: midnight local, staggered by time zone", "Not used; 05:00 UTC matches only US Eastern midnight"],
            ["Pre-load date", "Some guides say pre-load opened Nov 12", "Rockstar: Nov 10 (Nov 12 is when code-in-box copies reach retailers)", "Nov 10 used"],
            ["US unlock moment", "PS Store listings reported as one US time: midnight ET", "Rockstar: midnight local", "Both shown; unresolved"]],
           [0.18, 0.30, 0.28, 0.24], "", tints={3: TERRA_TINT}, fs=15)

# ---------- FIG 1: head start vs US Eastern ----------
fig = base_fig(16, 9.2)
ax = fig.add_axes([0.2, 0.12, 0.74, 0.70], facecolor=CREAM)
names = [r["name"] for r in rows][::-1]
vals = [r["lead_vs_et_h"] for r in rows][::-1]
cols = []
for n, v in zip(names, vals):
    cols.append(TERRA if n.startswith("New Zealand") else (BLUE if n in US else INK))
bars = ax.barh(names, vals, color=cols, height=0.62)
for b, n in zip(bars, names):
    if n in US and n != "US Eastern":
        b.set_hatch("///"); b.set_edgecolor(CREAM)
ax.axvline(0, color=INK, lw=2)
for n, v, b in zip(names, vals, bars):
    lab = f"{v:+.1f} h".replace(".0 h", " h").replace("+0 h", "0 h")
    ax.text(v + (0.35 if v >= 0 else -0.35), b.get_y() + b.get_height() / 2, lab, va="center",
            ha="left" if v >= 0 else "right", family=MONO, fontsize=13, color=INK)
ax.set_xlim(-5.2, 21)
ax.tick_params(axis="y", labelsize=17, length=0)
for l in ax.get_yticklabels(): l.set_family(SERIF)
ax.tick_params(axis="x", labelsize=13)
for l in ax.get_xticklabels(): l.set_family(MONO)
ax.set_xlabel("Hours before US Eastern midnight (negative = after)", family=SERIF, fontsize=16, color=INK)
for s in ("top", "right", "left"): ax.spines[s].set_visible(False)
ax.grid(axis="x", color=GREY, lw=0.6, alpha=0.6); ax.set_axisbelow(True)
fig.text(0.04, 0.93, "Fig. 1  How early each region unlocks, relative to US Eastern midnight", family=SERIF, fontsize=26, color=INK)
fig.text(0.04, 0.885, "Computed from the local-midnight rule. Hatched bars: US zones where the PlayStation Store reportedly uses one Eastern time instead.", family=SERIF, style="italic", fontsize=14, color="#6b6552")
fig.text(0.04, 0.03, "Sources: Rockstar Support (rule); tz database (conversion). Figures are arithmetic, not separately announced times.", family=SERIF, style="italic", fontsize=12.5, color="#6b6552")
fig.savefig(f"{OUT}/fig1-head-start.png", facecolor=CREAM); plt.close(fig)

# ---------- FIG 2: UTC timeline ----------
fig = base_fig(16, 7.4)
ax = fig.add_axes([0.04, 0.2, 0.92, 0.55], facecolor=CREAM)
t0 = datetime(2026, 11, 18, 9, 0, tzinfo=UTC); t1 = datetime(2026, 11, 19, 10, 0, tzinfo=UTC)
def x(dt): return (dt - t0).total_seconds() / 3600
ax.set_xlim(0, x(t1)); ax.set_ylim(-3.2, 3.6)
ax.axhline(0, color=INK, lw=3)
for h in range(0, int(x(t1)) + 1, 3):
    d = t0 + timedelta(hours=h)
    ax.plot([h, h], [-0.15, 0.15], color=INK, lw=1.5)
    ax.text(h, -0.55, d.strftime("%H:%M"), ha="center", family=MONO, fontsize=11, color=INK)
mid = x(datetime(2026, 11, 19, 0, 0, tzinfo=UTC))
ax.plot([mid, mid], [-2.9, -0.2], color=GREY, lw=1.2, ls="--"); ax.text(mid + 0.15, -1.15, "Nov 19 UTC \u2192", family=MONO, fontsize=11, color="#6b6552")
ax.text(mid - 0.15, -1.15, "\u2190 Nov 18 UTC", family=MONO, fontsize=11, color="#6b6552", ha="right")
events = [("NZ", rows[0]["utc"], 1.2), ("Sydney", rows[1]["utc"], 2.3), ("Japan", rows[2]["utc"], 1.2), ("India", rows[4]["utc"], 2.3),
          ("Germany", rows[6]["utc"], 1.2), ("UK", rows[7]["utc"], 2.3), ("Brazil", rows[8]["utc"], 1.2),
          ("US East", rows[9]["utc"], 2.3), ("US Pacific*", rows[12]["utc"], 1.2)]
for lab, dt, yy in events:
    c = TERRA if lab == "NZ" else (BLUE if lab.startswith("US") else INK)
    ax.plot([x(dt), x(dt)], [0, yy - 0.15], color=c, lw=1.6)
    ax.plot(x(dt), 0, "o", color=c, ms=9)
    ax.text(x(dt), yy, f"{lab}\n{dt.strftime('%H:%M')}", ha="center", va="bottom", family=SERIF, fontsize=15, color=c, fontweight="bold")
ax.plot([x(cloud), x(cloud)], [0, -2.0], color=GREEN, lw=1.6); ax.plot(x(cloud), 0, "s", color=GREEN, ms=10)
ax.text(x(cloud), -2.1, "Xbox Cloud streaming\n1 a.m. ET = 06:00", ha="center", va="top", family=SERIF, fontsize=15, color=GREEN, fontweight="bold")
ax.axis("off")
fig.text(0.04, 0.9, "Fig. 2  The rollout on one clock (UTC)", family=SERIF, fontsize=26, color=INK)
fig.text(0.04, 0.84, "Round markers: native unlock at local midnight. Square marker: Xbox Cloud Gaming start stated by Xbox Wire.", family=SERIF, style="italic", fontsize=14, color="#6b6552")
fig.text(0.04, 0.05, "* US Pacific local midnight under Rockstar's rule; PS Store listings reportedly use US Eastern nationwide. Sources: Rockstar Support, Xbox Wire, tz database.", family=SERIF, style="italic", fontsize=12.5, color="#6b6552")
fig.savefig(f"{OUT}/fig2-timeline-utc.png", facecolor=CREAM); plt.close(fig)

# ---------- FIG 3: NZ-trick head start by US zone ----------
fig = base_fig(16, 7.2)
ax = fig.add_axes([0.1, 0.18, 0.84, 0.56], facecolor=CREAM)
nz = rows[0]["utc"]
zs = [("US Eastern", "America/New_York"), ("US Central", "America/Chicago"), ("US Mountain", "America/Denver"), ("US Pacific", "America/Los_Angeles")]
hrs = [(unlock(z).astimezone(UTC) - nz).total_seconds() / 3600 for _, z in zs]
b = ax.bar([n for n, _ in zs], hrs, color=[BLUE, BLUE, BLUE, BLUE], width=0.55)
for bb, v, (n, z) in zip(b, hrs, zs):
    ax.text(bb.get_x() + bb.get_width() / 2, v + 0.5, f"{v:.0f} h", ha="center", family=MONO, fontsize=18, color=INK)
    ax.text(bb.get_x() + bb.get_width() / 2, v / 2, f"NZ midnight =\n{fmt(nz, z)}", ha="center", va="center", family=SERIF, fontsize=15, color=CREAM)
ax.set_ylim(0, 25)
ax.tick_params(axis="x", labelsize=17, length=0)
for l in ax.get_xticklabels(): l.set_family(SERIF)
ax.tick_params(axis="y", labelsize=12)
for l in ax.get_yticklabels(): l.set_family(MONO)
ax.set_ylabel("Hours earlier than local midnight", family=SERIF, fontsize=16)
for s in ("top", "right"): ax.spines[s].set_visible(False)
ax.grid(axis="y", color=GREY, lw=0.6, alpha=0.6); ax.set_axisbelow(True)
fig.text(0.04, 0.9, "Fig. 3  The most a New Zealand location could buy, by US time zone", family=SERIF, fontsize=26, color=INK)
fig.text(0.04, 0.84, "Maximum gap between Auckland midnight and each zone's local midnight. Player-reported, not confirmed by Rockstar or Microsoft.", family=SERIF, style="italic", fontsize=14, color="#6b6552")
fig.text(0.04, 0.04, "If a US store unlocks at one Eastern time nationwide, the Central, Mountain and Pacific gaps shrink to 18 hours. Source: tz database; Rockstar Support rule.", family=SERIF, style="italic", fontsize=12.5, color="#6b6552")
fig.savefig(f"{OUT}/fig3-us-zone-gap.png", facecolor=CREAM); plt.close(fig)

# ---------- HERO ----------
fig = plt.figure(figsize=(16, 8.4), dpi=100, facecolor=CREAM)
ax = fig.add_axes([0, 0, 1, 1]); ax.set_xlim(0, 16); ax.set_ylim(0, 8.4); ax.axis("off")
ax.add_patch(plt.Rectangle((0.6, 0.6), 14.8, 7.2, fill=False, ec=INK, lw=4))
ax.text(1.2, 6.7, "NOV 18–19, 2026  ·  GRAND THEFT AUTO VI", family=MONO, fontsize=17, color=TERRA, fontweight="bold")
ax.text(1.2, 4.9, "How & When\nto Play", family=SERIF, fontsize=92, color=INK, va="center", linespacing=0.95)
ax.text(1.2, 2.35, "Unlock times by time zone  ·  the New Zealand trick  ·  Xbox Cloud Gaming", family=SERIF, style="italic", fontsize=26, color=INK)
ax.text(1.2, 1.35, "An evidence-first guide: what Rockstar and Xbox confirmed, and what players only report.", family=SERIF, fontsize=19, color="#6b6552")
ax.add_patch(plt.Rectangle((11.6, 4.3), 3.2, 2.5, color=TERRA))
ax.text(13.2, 5.95, "18 h", family=MONO, fontsize=44, color=CREAM, ha="center", fontweight="bold")
ax.text(13.2, 5.0, "NZ midnight vs\nUS Eastern midnight", family=SERIF, fontsize=17, color=CREAM, ha="center", va="center")
fig.savefig(f"{OUT}/hero.png", facecolor=CREAM); plt.close(fig)
print("ok")
for r in rows: print(f"{r['name']:28s} {r['utc']:%b %d %H:%M} UTC  lead_vs_ET={r['lead_vs_et_h']:+.1f}")
print("cloud", cloud)
