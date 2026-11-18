"""Short-form (9:16) video for the GTA VI How & When to Play article.
Audio-first: Kokoro am_onyx narration is generated and measured; its durations drive every visual cue.
Visual register: brutalist.art 'Claude' register (cream / warm ink / terracotta, serif lead, mono chrome)."""
import json, os, subprocess, sys, math, shutil
import numpy as np
import soundfile as sf
from PIL import Image, ImageDraw, ImageFont
from kokoro_onnx import Kokoro

W, H, FPS = 1080, 1920, 30
BASE = "/home/claude/work"
OUT = f"{BASE}/video"
FR = f"{OUT}/frames"
os.makedirs(FR, exist_ok=True)
CREAM, INK, TERRA, BLUE, GREEN, SOFT = (250, 249, 245), (61, 57, 41), (217, 119, 87), (106, 155, 204), (120, 140, 93), (107, 101, 82)
times = json.load(open(f"{BASE}/gta6-guide/images/computed_times.json"))

# ---------------- narration (audio first) ----------------
BEATS = [
    dict(id="B0", text="Grand Theft Auto Six unlocks at midnight local time on November nineteenth. That is Rockstar's own rule, for PlayStation Five and Xbox Series X and S.",
         cues=[("", 0), ("unlocks at midnight", 1), ("That is Rockstar's", 2), ("PlayStation Five", 3)], dark=False),
    dict(id="B1", text="New Zealand reaches midnight first: six A.M. Eastern and three A.M. Pacific, on November eighteenth. That is eighteen hours before US Eastern midnight.",
         cues=[("", 0), ("six A.M. Eastern", 1), ("eighteen hours", 2)], dark=False),
    dict(id="B2", text="In the United States, sources disagree. Rockstar says midnight local time. Reported store listings use midnight Eastern for everyone. Check your own store's countdown.",
         cues=[("", 0), ("Rockstar says", 1), ("Reported store", 2), ("Check your own", 3)], dark=True),
    dict(id="B3", text="The New Zealand trick: on Xbox, players set the console location to New Zealand and restart. Players report it works. No confirmation from Rockstar or Microsoft was found.",
         cues=[("", 0), ("on Xbox", 1), ("Players report", 2), ("No confirmation", 3)], dark=False),
    dict(id="B4", text="Xbox One has no native version. Xbox Cloud Gaming opens at one A.M. Eastern on November nineteenth, with Series S graphics. You still buy the game.",
         cues=[("", 0), ("opens at one", 1), ("Series S graphics", 2), ("You still buy", 3)], dark=False),
    dict(id="B5", text="What we don't know: whether the New Zealand trick changes the cloud start time. No source says.",
         cues=[("", 0), ("whether the New Zealand", 1), ("No source says", 2)], dark=False),
    dict(id="B6", text="The full article, with every table, chart and source, is linked below.",
         cues=[("", 0), ("every table", 1)], dark=False),
]
PAD_START, PAD_BEAT = 0.5, 0.55

os.makedirs(f"{OUT}/audio", exist_ok=True)
kok = Kokoro(f"{BASE}/tts/kokoro.onnx", f"{BASE}/tts/voices.bin")
sr_out = 24000
segs, t = [], PAD_START
timeline = []
voice = [np.zeros(int(PAD_START * sr_out), dtype=np.float32)]
for b in BEATS:
    samples, sr = kok.create(b["text"], voice="am_onyx", speed=1.0, lang="en-us")
    assert sr == sr_out, sr
    samples = samples.astype(np.float32)
    dur = len(samples) / sr
    sf.write(f"{OUT}/audio/{b['id']}.wav", samples, sr)
    n = len(b["text"])
    cue_t = []
    for phrase, step in b["cues"]:
        frac = (b["text"].index(phrase) / n) if phrase else 0.0
        cue_t.append((t + frac * dur * 0.97, step))   # slight lead so visuals land with the words
    timeline.append(dict(id=b["id"], start=t, dur=dur, cues=cue_t, dark=b["dark"], end=t + dur + PAD_BEAT))
    voice.append(samples)
    voice.append(np.zeros(int(PAD_BEAT * sr), dtype=np.float32))
    t += dur + PAD_BEAT
TOTAL = t + 0.6
voice.append(np.zeros(int(0.6 * sr_out), dtype=np.float32))
voice = np.concatenate(voice)
sf.write(f"{OUT}/audio/voice.wav", voice, sr_out)
json.dump(timeline, open(f"{OUT}/timeline.json", "w"), indent=1, default=float)
print("TOTAL seconds", round(TOTAL, 2), [round(x["dur"], 2) for x in timeline])

# ---------------- music (original, synthesized) ----------------
SR = 44100
n = int(TOTAL * SR) + SR
tt = np.arange(n) / SR
chords = [(220.00, 261.63, 329.63), (174.61, 220.00, 261.63), (130.81, 196.00, 261.63), (196.00, 246.94, 293.66)]  # Am F C G (inverted, low)
chord_len = 6.0
mus = np.zeros(n)
for ci in range(int(math.ceil(TOTAL / chord_len)) + 1):
    f0 = chords[ci % 4]
    s0, s1 = int(ci * chord_len * SR), int(min(n, (ci + 1) * chord_len * SR + 1.5 * SR))
    if s0 >= n: break
    seg_t = np.arange(s1 - s0) / SR
    env = np.minimum(seg_t / 1.8, 1.0) * np.clip((chord_len + 1.5 - seg_t) / 1.5, 0, 1)
    for f in f0:
        for det in (-0.6, 0.0, 0.6):
            mus[s0:s1] += 0.08 * env * np.sin(2 * np.pi * (f + det) * seg_t) + 0.03 * env * np.sin(2 * np.pi * 2 * (f + det) * seg_t)
    mus[s0:s1] += 0.10 * env * np.sin(2 * np.pi * (f0[0] / 2) * seg_t)   # sub root
# soft plucks on a slow pulse (arpeggio of the chord tones)
bpm = 76; beat = 60 / bpm
k = 0
while k * beat < TOTAL:
    ch = chords[int((k * beat) // chord_len) % 4]
    f = ch[(k % 3)] * 2
    s0 = int(k * beat * SR); L = int(0.9 * SR)
    if s0 + L < n:
        pt = np.arange(L) / SR
        mus[s0:s0 + L] += 0.05 * np.exp(-pt * 4.5) * np.sin(2 * np.pi * f * pt) * (1 if k % 2 == 0 else 0.6)
    k += 1
mus *= np.clip(tt / 1.5, 0, 1) * np.clip((TOTAL + 0.5 - tt) / 1.8, 0, 1)
mus = mus / np.max(np.abs(mus)) * 0.9
sf.write(f"{OUT}/audio/music.wav", np.stack([mus, mus], 1).astype(np.float32), SR)

# ---------------- visuals ----------------
GAR = f"{BASE}/fonts/EBGaramond.ttf"
MONO = "/usr/share/fonts/truetype/dejavu/DejaVuSansMono-Bold.ttf"
def gar(size, wght=500):
    f = ImageFont.truetype(GAR, size)
    try: f.set_variation_by_axes([wght])
    except Exception: pass
    return f
def mono(size): return ImageFont.truetype(MONO, size)

def wrap(draw, text, font, maxw):
    words, lines, cur = text.split(), [], ""
    for w in words:
        trial = (cur + " " + w).strip()
        if draw.textlength(trial, font=font) <= maxw: cur = trial
        else: lines.append(cur); cur = w
    if cur: lines.append(cur)
    return lines

def text_block(d, xy, text, font, fill, maxw, lead=1.12, anchor="la"):
    x, y = xy
    for ln in wrap(d, text, font, maxw):
        d.text((x, y), ln, font=font, fill=fill, anchor=anchor)
        y += int(font.size * lead)
    return y

M = 90
def canvas(dark):
    bg = INK if dark else CREAM
    im = Image.new("RGB", (W, H), bg)
    return im, ImageDraw.Draw(im), (CREAM if dark else INK), bg

def chrome(d, fg, kicker, source=None):
    d.text((M, 96), kicker, font=mono(30), fill=TERRA)
    d.rectangle([M, 150, W - M, 154], fill=fg)
    if source:
        d.text((M, H - 110), "SOURCE  " + source, font=mono(26), fill=(SOFT if fg == INK else (185, 180, 164)))

def tag(d, xy, label, fill, fg_text=CREAM, size=34):
    f = mono(size); x, y = xy
    w = d.textlength(label, font=f) + 44
    d.rectangle([x, y, x + w, y + size + 28], fill=fill)
    d.text((x + 22, y + 12), label, font=f, fill=fg_text)
    return y + size + 28

def draw_beat(bid, step):
    dark = bid == "B2"
    im, d, fg, bg = canvas(dark)
    if bid == "B0":
        chrome(d, fg, "NOV 18-19, 2026", "Rockstar Support, regional release times")
        y = text_block(d, (M, 260), "GTA VI:", gar(150), fg, W - 2 * M, 1.0)
        y = text_block(d, (M, y - 10), "How & When to Play", gar(150), fg, W - 2 * M, 1.0)
        if step >= 1:
            d.rectangle([M, 880, W - M, 884], fill=fg)
            text_block(d, (M, 930), "Midnight local time", gar(116), TERRA, W - 2 * M, 1.0)
            text_block(d, (M, 1180), "November 19, 2026", gar(70, 450), fg, W - 2 * M)
        if step >= 2: tag(d, (M, 1330), "CONFIRMED", INK)
        if step >= 3: text_block(d, (M, 1470), "PS5  +  Xbox Series X|S", mono(48), fg, W - 2 * M)
    elif bid == "B1":
        chrome(d, fg, "UNLOCK ORDER", "Rockstar Support rule, computed")
        text_block(d, (M, 230), "New Zealand goes first", gar(112), fg, W - 2 * M, 1.0)
        rows = [("New Zealand", "Pacific"), ]
        regions = [("New Zealand (Auckland)", "New Zealand", TERRA), ("Australia (Sydney)", "Sydney", INK), ("Japan / South Korea", "Japan", INK),
                   ("India", "India", INK), ("Central Europe (DE, FR)", "Germany", INK), ("United Kingdom", "UK", INK),
                   ("Brazil (Sao Paulo)", "Brazil", INK), ("US Eastern", "US Eastern", BLUE)]
        y0, bh, gap, maxbar = 640, 66, 50, 520
        show = 1 if step == 1 else (len(regions) if step >= 2 else 0)
        for i, (key, lab, col) in enumerate(regions[:show]):
            v = times[key]["lead_vs_et_h"]
            y = y0 + i * (bh + gap)
            d.text((M, y - 6), lab, font=gar(44, 450), fill=fg)
            bx = M + 300
            d.rectangle([bx, y + 6, bx + max(4, int(maxbar * v / 18)), y + bh], fill=col)
            vt = (f"{v:g} h")
            d.text((bx + max(4, int(maxbar * v / 18)) + 16, y + 8), vt, font=mono(38), fill=fg)
        if step >= 1 and step < 2:
            text_block(d, (M, 780), "Nov 18:  6 AM Eastern  /  3 AM Pacific", mono(36), fg, W - 2 * M)
        if step >= 2:
            d.text((M, 1560), "Hours before US Eastern midnight", font=gar(42, 450), fill=SOFT)
    elif bid == "B2":
        chrome(d, fg, "THE US QUESTION", "Rockstar Support; Vice (PS Store listings)")
        text_block(d, (M, 230), "Sources disagree", gar(120), fg, W - 2 * M, 1.0)
        if step >= 1:
            d.rectangle([M, 560, W - M, 940], outline=CREAM, width=5)
            d.text((M + 40, 590), "ROCKSTAR", font=mono(30), fill=TERRA)
            text_block(d, (M + 40, 660), "Midnight local time, in every region", gar(66, 450), fg, W - 2 * M - 80, 1.08)
            d.text((M + 40, 860), "Eastern, Central, Mountain, Pacific each at their own midnight", font=gar(34, 400), fill=(185, 180, 164), anchor="la") if False else None
        if step >= 2:
            d.rectangle([M, 990, W - M, 1370], outline=CREAM, width=5)
            d.text((M + 40, 1020), "PS STORE LISTINGS (REPORTED)", font=mono(30), fill=TERRA)
            text_block(d, (M + 40, 1090), "One nationwide time: midnight Eastern", gar(66, 450), fg, W - 2 * M - 80, 1.08)
        if step >= 3:
            text_block(d, (M, 1470), "Check your own store's countdown.", gar(72, 500), TERRA, W - 2 * M, 1.05)
    elif bid == "B3":
        chrome(d, fg, "THE NEW ZEALAND TRICK", "Vice, Cybernews (player reports)")
        text_block(d, (M, 230), "The New Zealand trick", gar(116), fg, W - 2 * M, 1.0)
        if step >= 1:
            steps = ["Settings", "System", "Language & location", "Location: New Zealand", "Restart"]
            y = 640
            for i, s_ in enumerate(steps):
                d.rectangle([M, y, M + 86, y + 86], fill=INK)
                d.text((M + 43, y + 43), str(i + 1), font=mono(44), fill=CREAM, anchor="mm")
                d.text((M + 130, y + 14), s_, font=gar(62, 450), fill=fg)
                y += 128
        if step >= 2: tag(d, (M, 1330), "REPORTED BY PLAYERS", TERRA, size=38)
        if step >= 3: text_block(d, (M, 1470), "No confirmation from Rockstar or Microsoft was found.", gar(58, 450), fg, W - 2 * M, 1.1)
    elif bid == "B4":
        chrome(d, fg, "XBOX ONE", "Xbox Wire, Nov 10, 2026")
        text_block(d, (M, 230), "Xbox One:", gar(130), fg, W - 2 * M, 1.0)
        text_block(d, (M, 380), "stream it", gar(130), fg, W - 2 * M, 1.0)
        if step >= 1:
            d.rectangle([M, 700, W - M, 704], fill=fg)
            text_block(d, (M, 760), "1:00 AM ET", gar(150), TERRA, W - 2 * M, 1.0)
            text_block(d, (M, 1000), "Nov 19, 1 AM ET is 10 PM Pacific, 11 PM Mountain, 12 AM Central on Nov 18", gar(52, 450), fg, W - 2 * M, 1.15)
        if step >= 2: text_block(d, (M, 1240), "Xbox Series S graphics settings", gar(64, 450), fg, W - 2 * M, 1.08)
        if step >= 3: tag(d, (M, 1460), "GAME BOUGHT SEPARATELY", INK, size=36)
    elif bid == "B5":
        chrome(d, fg, "EVIDENCE GAP", "No source reviewed addresses this")
        text_block(d, (M, 230), "Not established", gar(128), fg, W - 2 * M, 1.0)
        if step >= 1:
            text_block(d, (M, 700), "Does the New Zealand trick change when Xbox Cloud Gaming opens?", gar(84, 450), fg, W - 2 * M, 1.08)
        if step >= 2: tag(d, (M, 1380), "NO SOURCE SAYS", TERRA, size=44)
    elif bid == "B6":
        chrome(d, fg, "FULL ARTICLE", None)
        text_block(d, (M, 400), "The full article", gar(150), fg, W - 2 * M, 1.0)
        if step >= 1:
            text_block(d, (M, 760), "Every table, chart", gar(86, 450), fg, W - 2 * M, 1.1)
            text_block(d, (M, 880), "and source.", gar(86, 450), fg, W - 2 * M, 1.1)
        d.rectangle([M, 1180, W - M, 1184], fill=fg)
        text_block(d, (M, 1230), "Link in the description", mono(46), TERRA, W - 2 * M)
    return im

# ---------------- frame timeline ----------------
frames = []   # list of (path, duration)
cache = {}
def state_img(bid, step):
    key = (bid, step)
    if key not in cache:
        p = f"{FR}/{bid}_{step}.png"
        draw_beat(bid, step).save(p)
        cache[key] = p
    return cache[key]

# build list of (start_time, bid, step) change points
changes = []
for tl in timeline:
    for ct, st in tl["cues"]:
        changes.append((tl["start"] - (PAD_START if tl is timeline[0] else 0) * 0 if st == 0 else ct, tl["id"], st))
# make first cue of each beat begin at the end of previous beat (so the new card shows before narration)
changes = []
prev_end = 0.0
for tl in timeline:
    first = True
    for ct, st in tl["cues"]:
        changes.append((prev_end if first else ct, tl["id"], st)); first = False
    prev_end = tl["end"]
changes.sort()
XF = 6 / FPS   # crossfade length at beat boundaries
seq = []   # per-frame list of image paths
total_frames = int(TOTAL * FPS)
def at(tsec):
    cur = changes[0]
    for c in changes:
        if c[0] <= tsec: cur = c
    return cur
for fi in range(total_frames):
    tsec = fi / FPS
    c = at(tsec)
    seq.append((c[1], c[2], c[0]))
# crossfade only across beat changes
lines = []
last_path, last_run = None, 0
out_dir = f"{FR}/seq"; os.makedirs(out_dir, exist_ok=True)
def img_for(bid, st): return Image.open(state_img(bid, st)).convert("RGB")
prev_bid_state = None
count = 0
concat = []
i = 0
while i < len(seq):
    bid, st, t0 = seq[i]
    # find run length
    j = i
    while j < len(seq) and seq[j][:2] == (bid, st): j += 1
    # if previous run was a different beat, emit crossfade frames at the start of this run
    xf_frames = 0
    if prev_bid_state and prev_bid_state[0] != bid:
        xf_frames = min(6, j - i)
        a = img_for(*prev_bid_state); b = img_for(bid, st)
        for k in range(xf_frames):
            blend = Image.blend(a, b, (k + 1) / (xf_frames + 1))
            p = f"{out_dir}/xf_{i + k:05d}.png"; blend.save(p)
            concat.append((p, 1 / FPS))
    rest = (j - i) - xf_frames
    if rest > 0: concat.append((state_img(bid, st), rest / FPS))
    prev_bid_state = (bid, st)
    i = j
with open(f"{OUT}/concat.txt", "w") as f:
    for p, d_ in concat:
        f.write(f"file '{p}'\nduration {d_:.5f}\n")
    f.write(f"file '{concat[-1][0]}'\n")
print("segments", len(concat), "frames", total_frames)

# ---------------- encode + mix ----------------
sil = f"{OUT}/silent.mp4"
subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-f", "concat", "-safe", "0", "-i", f"{OUT}/concat.txt", "-vf", f"fps={FPS},format=yuv420p",
                "-c:v", "libx264", "-preset", "veryfast", "-crf", "20", "-t", f"{TOTAL:.3f}", sil], check=True)
final = f"{OUT}/gta6-how-and-when-to-play-short.mp4"
subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-i", sil, "-i", f"{OUT}/audio/voice.wav", "-i", f"{OUT}/audio/music.wav",
                "-filter_complex",
                "[1:a]aresample=44100,volume=1.0[v];[2:a]aresample=44100,volume=0.12[m];[v][m]amix=inputs=2:duration=first:normalize=0,loudnorm=I=-14:TP=-1.5:LRA=7[a]",
                "-map", "0:v", "-map", "[a]", "-c:v", "copy", "-c:a", "aac", "-b:a", "192k", "-t", f"{TOTAL:.3f}", "-movflags", "+faststart", final], check=True)
print("done", final)
