# The Architecture of Player Progression

### Mathematical, Psychological, and Systemic Mechanics in Game Design — A Fact-Checked Analysis

*Game Research Writer | Claim-ledger and devil's-advocate review completed 2026-08-25. See `research/claim-ledger.md` for the full source-by-source audit behind every correction in this revision.*

---

## 1. Introduction

Player progression is the set of systems that change a player's state over time — through learned skill, accumulated numbers, acquired items, unlocked story, or social standing. Nearly every modern game uses some combination of these systems to sequence content, manage difficulty, and sustain engagement across dozens or hundreds of hours.

This piece asks a narrower question than "how does progression work": **which specific claims commonly made about progression design — mathematical formulas, named psychological effects, and cited case studies — are actually supported by primary evidence, and which are repeated because they sound authoritative rather than because they were confirmed?**

A prior draft of this analysis stated several formulas and case-study details as settled fact. Research for this revision could not confirm all of them. Where evidence was found, it is cited. Where it was not, the claim was either removed or rewritten as an open question. That process is documented in full in the accompanying claim ledger.

---

## 2. Context: A Taxonomy of Progression Types

Design writing commonly groups progression systems into a small number of archetypes based on what changes and why the player cares. The table below is an organizing framework for this article, not a citation to a single canonical industry source — no primary document was found that defines exactly these six categories with these labels. Treat it as an analytical lens.

| Paradigm | Core Mechanism | Primary Motivator (per SDT/PENS, §3) | Primary Balancing Challenge |
|---|---|---|---|
| Skill-Based | Player's own motor and tactical learning; avatar stats often static | Competence | High entry barrier; frustration risk |
| XP-Based | Numerical accumulation to discrete level thresholds | Competence / accomplishment | Pacing decay; repetitive grind |
| Item-Based | Gear acquisition, rarity tiers, crafting, loadouts | Autonomy / collection | Power creep, inventory bloat |
| Narrative | Branching story, dialogue, world-state change | Autonomy / curiosity | Production cost, narrative bloat |
| Social | Reputation, guild rank, leaderboards | Relatedness / status | Toxicity, entry barriers |
| Hybrid | Two or more of the above, interlocked | Multiple, simultaneously | Complexity, feature overload |

Most commercially successful open-world and live-service titles are hybrids: XP-driven stat growth layered over item crafting, gated behind narrative milestones, wrapped around skill-based combat. This is a widely repeated design-literature pattern (see, e.g., GDC-style postmortems and community formula archives), not a single confirmed statistic.

---

## 3. Evidence

### 3.1 The mathematics of leveling curves

Two quantities describe any numerical leveling system: the cumulative experience required to reach level *n* (P<sub>n</sub>), and the incremental gap between consecutive levels (S<sub>n</sub>):

**P<sub>n</sub> = Σ(i=1 to n−1) S<sub>i</sub>  and  S<sub>n</sub> = P<sub>n</sub> − P<sub>n−1</sub>**

This is a mathematical identity, not an empirical claim — it holds by definition for any leveling table. **Confidence: Confirmed** (as arithmetic; it says nothing about which curve a given game should use).

The choice of *curve family*, however, is a design decision with real behavioral consequences, and different genres consistently favor different families:

| Curve Class | Formula Shape | Behavior | Where it's commonly seen |
|---|---|---|---|
| Linear | f(x) = ax + b | Constant level-up cost; grows *easier* to reach relative to earlier levels | Arcade titles, flat seasonal battle passes |
| Polynomial / Power | P(L) = baseXP × (L−1)^exponent | Accelerating but controlled cost growth | JRPGs, action-RPGs, single-player campaigns |
| Exponential | E(L) = a × (1−b^L)/(1−b) | Fast early levels, extreme late-game cost | MMORPGs, long-lived live-service games, idle games |
| Sigmoidal / Logistic | S(x) = a / (1 + e^(−kx)) | Slow start, fast middle, tapering end | Skill-rank distributions, battle-pass tiers |

**Confidence: Strong inference.** This pattern is consistent across many independent designer write-ups and community formula archives (Tier 3 design-practice consensus), but no single Tier-1 document confirms it as a universal law — some titles deliberately mix curve families within one system.

A structural tension follows directly from these shapes: if a game's *reward payout* (XP per kill, per quest) scales linearly or stays flat, but the *level-cost curve* is exponential, the time required per level rises faster than the reward that funds it. That mismatch — not "bad design" in the abstract — is the mechanical definition of what players call "the grind." Designers commonly counter it with piecewise or dynamically-scaled reward functions rather than flattening the underlying curve, since a flattened curve removes the milestone pacing the curve was chosen to create.

![XP required per level, by curve family](../charts/01_xp_curve_classes.png)

One previous version of this article presented a specific formula — ΔE(L) = ((8×L) + Diff(L)) × MXP(L) × RF(L) — as a real, sourced industry equation. **No primary source for this exact formula could be located.** Per the evidence-gap rule this analysis follows, the specific formula has been removed. What can be confirmed is the *general pattern* it was gesturing at: many level-scaled reward systems multiply a base per-level term by a difficulty factor, a per-encounter value factor, and a global rate-tuning factor. That pattern is common; this particular equation is not confirmed to belong to any specific shipped game.

Sigmoidal (S-curve) overlays on local progression tiers — the idea that a convex "safe exploration" phase, a steep "reinforcement" phase, and a concave "anticipation" phase can be nested inside a longer exponential curve — is a coherent and frequently described design *technique*, consistent with general S-curve skill-acquisition literature. It is presented here as **interpretation**, not as a confirmed mechanism inside any specific named game, because the original source material did not cite one.

### 3.2 Psychological frameworks

**Self-Determination Theory and the PENS model.** The Player Experience of Need Satisfaction (PENS) model was developed by Richard Ryan, C. Scott Rigby, and Andrew Przybylski and published in *Motivation and Emotion* (2006). It applies Self-Determination Theory's three basic psychological needs — competence, autonomy, and relatedness — to game design: competence maps to clear growth feedback (XP bars, rank titles), autonomy maps to meaningful choice (skill trees, loadouts), and relatedness maps to social context (guilds, leaderboards). **Confidence: Confirmed.** This is a real, peer-reviewed, frequently cited framework, and it is the strongest-evidenced psychological claim in this article.

**Operant conditioning and reinforcement schedules.** B.F. Skinner's operant conditioning research, and specifically the finding that *variable*-ratio reinforcement schedules produce the highest response rates and the greatest resistance to extinction (compared to fixed schedules), is well established in behavioral psychology and has been extended by peer-reviewed research specifically on loot boxes (including studies indexed in PubMed Central linking rare-reward reveals to elevated arousal and urge-to-continue responses). **Confidence: Confirmed** as a general psychological mechanism.

Where this claim is *not* fully evidenced is at the level of intent: saying "variable-ratio loot systems exploit a well-documented psychological mechanism" is supported; saying "Game X's loot table was designed specifically to exploit players psychologically" requires a developer statement this analysis does not have for any specific title, and none is asserted here. Per the causality test this analysis applies throughout, the correct phrasing is that such systems **are consistent with** variable-ratio conditioning, not that any particular studio **confirmed** designing around it.

**Cognitive Load Theory and Flow.** Sweller's Cognitive Load Theory and Csikszentmihalyi's Flow model are both well-established, decades-old academic frameworks. **Confidence: Confirmed** as theory. Their application to specific design practices — gating mechanics behind level thresholds to manage cognitive load, tuning challenge-to-skill ratio to preserve flow — is a widely repeated and reasonable *interpretation* of those frameworks, but individual claims about a specific game's pacing achieving "flow" are not independently testable from outside the studio and are labeled as interpretation, not measurement.

**The Zeigarnik Effect.** The Zeigarnik Effect — the tendency to better remember interrupted or incomplete tasks — originates from Bluma Zeigarnik's 1927 studies. It is worth noting, and the earlier draft of this article did not, that modern replication attempts of the classic Zeigarnik findings have produced inconsistent results, and the original methodology has been criticized by later researchers. Its application to quest logs and partially-filled XP bars is a popular and plausible design analogy repeated in game-psychology writing, but it is not the product of a controlled study of quest-log design specifically. **Confidence: Weak inference** for the applied game-design claim, despite the underlying effect being historically well known.

### 3.3 Vertical vs. horizontal progression and economic sinks

| | Vertical Progression | Horizontal Progression |
|---|---|---|
| Definition | Direct numerical inflation of stats/gear power | Lateral expansion of options, utility, cosmetics |
| Legacy content | Rapidly obsoleted | Stays relevant |
| Player-base friction | High (stat gaps between veterans/newcomers) | Low |
| Main failure mode | Power creep, stat inflation | Choice overload, muted feedback |

![Vertical vs. horizontal progression: power level across content tiers](../charts/05_vertical_vs_horizontal.png)

This distinction, and the associated concepts of power creep and resource sinks (mechanics that permanently remove currency/materials to counter inflation from rising player efficiency), are extensively documented in live-service and MMO economy design writing. **Confidence: Strong inference to confirmed** for the general mechanisms. No specific numeric inflation claim about any single game is asserted here, consistent with none being sourced in the original material.

---

## 4. Case Studies

### 4.1 Resident Evil 4 — the hidden "Rank" system

Resident Evil 4 is widely cited as an early, influential example of invisible real-time difficulty adjustment. Community analysis (the Resident Evil Fandom wiki's "Game Rank" page and independent speedrunning-community technical write-ups) describes a background score that shifts based on player performance: landing hits and evading attacks raises it; getting hit, missing, and — most heavily — using a continue lowers it. Higher rank is described as increasing enemy damage and evasiveness while reducing the damage the player deals; lower rank does the reverse and increases beneficial item drops.

**This needs an important qualification the earlier draft omitted.** No official Capcom developer interview, GDC talk, or technical document confirming the exact rank range, a default starting value, or the precise numeric weighting of each trigger was located during this research pass. Everything specific about RE4's rank system that circulates publicly — including figures like "ten discrete ranks" or "rank 6 by default" — traces back to community reverse-engineering and observational play analysis, not a Capcom-confirmed source.

- **Confidence in the system's existence and general direction of effect:** Strong inference — it is independently corroborated across multiple unrelated community analyses and is observable in play.
- **Confidence in specific numeric parameters (rank count, default value, exact multipliers):** Weak inference / unverified. These should be read as community-estimated, not developer-confirmed.

The design logic attributed to the system — keep struggling players from getting stuck, keep dominant players challenged, without ever surfacing the mechanism to preserve the feeling that outcomes reflect the player's own skill — is a reasonable *interpretation* consistent with the observed behavior, not a quoted design rationale from Capcom.

### 4.2 A documented real-time DDA framework (Skyrim boss-battle research, 2026)

The mathematical DDA model in the earlier draft — a "dominance ratio" R = D<sub>n</sub>/(D<sub>n</sub>+D<sub>p</sub>) built from player-damage-taken and boss-damage-dealt rates, smoothed with an exponential filter D<sub>new</sub> = D<sub>current</sub> + α×(D<sub>raw</sub> − D<sub>current</sub>) at α = 0.45 — is real, but it was misattributed. It does not describe a generalized industry standard, and it is not connected to Resident Evil 4. It comes from a specific, identifiable, peer-reviewed source:

> Klarkowski et al., "A Modular Framework for Dynamic Difficulty Adjustment in Boss Battles: A Case Study in *The Elder Scrolls V: Skyrim*," *Applied Sciences* (MDPI), vol. 16, no. 15, article 7554 (2026).

That paper proposes a modular DDA framework for boss encounters, tested via a Skyrim case study, with a difficulty range constrained to [1.0, 1.35], phase thresholds at 1.10/1.20/1.28, a 0.07 step size per adjustment, a 1.6× "dominance boost" multiplier when the target difficulty exceeds current difficulty by more than 0.10, and a 10-second cooldown between updates.

- **Confidence: Confirmed — as this paper's proposed model.** It is a real, citable, peer-reviewed formula.
- **Confidence that this represents "how DDA generally works" industry-wide: Not supported.** It is one research team's framework, validated in one case study, not a documented description of how any specific commercial game engine (including Resident Evil 4's) actually implements difficulty adjustment internally.

![Exponential smoothing of the combat dominance ratio](../charts/04_dda_smoothing.png)

Presenting this formula immediately after the RE4 case study, as the earlier draft did, created a false impression that the two were connected or that the formula explains RE4's engine behavior. No evidence supports that link, and this revision separates the two cases explicitly.

### 4.3 Pseudo-Random Distribution — Dota 2

Valve's Dota 2 uses a documented alternative to true independent-probability rolls for proc-based effects (critical strikes, on-hit abilities). Instead of a constant chance each trial, the probability of success on the *N*-th attempt since the last success is P(N) = C×N, where C is a constant lower than the nominal listed rate. Each failure increases the next attempt's probability by C; a success resets the counter.

The C constants themselves (approximately 0.38% for a nominal 5% effect, roughly 1.5% for a nominal 10% effect, and so on) were **derived by the community** — through empirical play-data logging cross-checked against a mathematical derivation, not published by Valve as a raw formula. Valve has acknowledged using "bad luck protection" in general terms without publishing the underlying constants.

- **Confidence: Strong inference** for the mechanism and formula shape (extremely high internal consistency across large empirical samples); **not** developer-published documentation.

![Pseudo-Random Distribution: probability climbs with each failure](../charts/02_prd_ramp.png)

### 4.4 Gacha pity systems — soft/hard pity as exemplified by Genshin Impact

Soft-pity/hard-pity structures — a rising success probability that begins ramping well before a hard cap, followed by a guaranteed drop at the cap — are common across gacha-monetized games. Genshin Impact is the most extensively documented public example: independent large-sample pull trackers converge on a hard pity of 90 pulls for character banners and a soft-pity ramp beginning around pull 74, with most 5-star rewards landing around pulls 75–78 in practice.

HoYoverse has publicly confirmed some aggregate figures (e.g., a roughly 55% consolidated rate under its "Capturing Radiance" mechanic as of the version-5.0-era update) but has not published the exact soft-pity ramp curve or its underlying constant. **Confidence: Strong inference** — very large, independently-collected samples are highly consistent — but these are community-measured figures, not official developer documentation, and pull-74/pull-90 should be read as *a* well-documented example rather than *the* universal gacha standard.

![Gacha soft/hard pity: cumulative chance of a 5-star drop](../charts/03_gacha_pity.png)

---

## 5. Counterarguments and Alternative Interpretations

A fair reading of this subject has to grant several points that cut against the framing above:

**The taxonomy is a convenience, not a discovery.** The six-paradigm table in Section 2 is a useful organizing device, but it is authored for this article, not drawn from a single citable industry standard. A different analyst could split "item-based" and "crafting-based" progression, or fold "narrative" into "hybrid," and produce an equally defensible scheme. Readers should treat it as a lens, not a taxonomy with independent empirical status.

**Academic frameworks describe player experience, not proven designer intent.** PENS, Cognitive Load Theory, and Flow are genuinely well-supported psychological models — but citing them to explain *why* a level-gating system or an XP curve exists risks reverse-engineering intent from outcome. A designer may have arrived at the same structure through playtesting and iteration without ever invoking Ryan, Rigby, Sweller, or Csikszentmihalyi by name. The frameworks are a legitimate *lens* for analysis; they are not evidence of what any specific studio was thinking.

**The strongest counter-evidence concerns the Zeigarnik Effect specifically.** Because the classic 1927 findings have replicated inconsistently in later research, building confident claims about quest-log retention on the Zeigarnik Effect is weaker ground than the earlier draft implied. A competing, equally plausible explanation for why partially-completed quest logs and near-full XP bars correlate with return sessions is simple **loss aversion or sunk-cost framing** — players return to avoid "wasting" progress already made, a distinct behavioral-economics mechanism that does not require invoking Zeigarnik at all. Both explanations are consistent with the same observed behavior, and this analysis cannot adjudicate between them with the evidence available.

**PRD and pity systems are frequently over-generalized.** Community-reverse-engineered constants from one game (Dota 2's PRD constants, Genshin's pull-74/pull-90 pity) are sometimes cited as if they describe an industry-wide standard. They describe those specific, well-documented implementations. Other games' probabilistic systems may use different constants, different ramp shapes, or true independent randomness with no pity mechanism at all — this article makes no claim about titles that were not directly researched.

**The RE4/DDA-paper pairing in the earlier draft is a clear case of unsupported causal linking.** Presenting a 2026 academic Skyrim-modding paper's formula directly after a 2005 game's community-reverse-engineered rank system implied a connection — shared methodology, shared industry standard — that the evidence does not support. This is exactly the kind of "common industry practice incorrectly attributed to a specific game" error the causality test is designed to catch, and it was present in the source material this analysis was asked to check.

---

## 6. Limitations

This analysis is limited by what is publicly documented. Internal engine code, telemetry dashboards, and design documents for the specific games discussed are not available to outside researchers, including this one. Where this piece states "confirmed," it means confirmed *in a public, citable source* — not independently verified against a studio's source code. Community reverse-engineering (RE4's rank system, Dota 2's PRD constants, gacha pity ramps) is often highly reliable at the level of large-sample statistical convergence, but it is not the same evidentiary category as a developer-published specification, and this piece has tried to keep that distinction visible rather than flattening it for readability.

This analysis also could not verify the specific formula ΔE(L) = ((8×L) + Diff(L)) × MXP(L) × RF(L) from the original draft against any primary source, and removed it rather than presenting it as real. It is possible such a formula exists in an undocumented or non-English-language source not surfaced by this research pass; if a reader has a primary citation for it, it should be reinstated with that citation attached, not restored from memory.

---

## 7. Conclusion

**What we know:** The mathematical relationship between cumulative and incremental XP is a definitional identity. PENS/Self-Determination Theory is a real, peer-reviewed framework connecting competence/autonomy/relatedness to player motivation. Operant conditioning's variable-ratio schedule is a well-established mechanism with peer-reviewed evidence connecting it to loot-reveal engagement. Dota 2's pseudo-random distribution and Genshin Impact's soft/hard pity are real, well-documented (if community-derived) systems. A 2026 peer-reviewed paper proposes a specific, citable dominance-ratio DDA formula for Skyrim boss battles.

**What we think:** Curve-family choice (linear/polynomial/exponential/sigmoidal) maps to genre in the pattern described, based on strong but Tier-3 design-practice consensus. Resident Evil 4 almost certainly runs some form of invisible rank-based difficulty adjustment, based on strongly convergent community analysis, though its exact parameters remain unconfirmed by the developer. Vertical/horizontal progression's economic consequences (power creep, resource sinks) follow the described pattern in live-service design writing generally.

**What we don't know:** Whether any specific named game's designers consciously invoked Skinner, Zeigarnik, or Csikszentmihalyi when building their systems. Whether the Zeigarnik Effect, given its replication problems, is actually the correct explanation for quest-log retention behavior as opposed to loss-aversion framing. Whether Resident Evil 4's rank system uses exactly ten levels with a default of six, or any other undocumented internal detail. Whether the Skyrim-paper DDA formula, or anything resembling it, is used in any shipped commercial game engine.

---

## 8. Sources

- Ryan, R. M., Rigby, C. S., & Przybylski, A. — PENS model; selfdeterminationtheory.org, "[Player Experience of Needs Satisfaction (PENS)](https://selfdeterminationtheory.org/player-experience-of-needs-satisfaction-pens/)"
- Klarkowski et al., "[A Modular Framework for Dynamic Difficulty Adjustment in Boss Battles: A Case Study in The Elder Scrolls V: Skyrim](https://www.mdpi.com/2076-3417/16/15/7554)," Applied Sciences (MDPI), 16(15):7554, 2026
- Resident Evil Fandom Wiki, "[Game Rank (RE4)](https://residentevil.fandom.com/wiki/Game_Rank_(RE4))"
- Speedrun.com, "[Rank / Difficulty adjustment analysis — Resident Evil 4](https://www.speedrun.com/re4console/guides/3sahj)"
- Dota 2 Fandom Wiki, "[Random Distribution](https://dota2.fandom.com/wiki/Random_Distribution)"; Liquipedia, "[Pseudo Random Distribution](https://liquipedia.net/dota2/Pseudo_Random_Distribution)"
- PlayAware, "[Genshin Impact pity system guide](https://playaware.gg/guides/genshin-pity)"
- PMC/NIH, "[Rare Loot Box Rewards Trigger Larger Arousal and Reward Responses](https://pmc.ncbi.nlm.nih.gov/articles/PMC7882574/)"
- Psychology Today, "[The Zeigarnik Effect and Quest Logs](https://www.psychologytoday.com/us/blog/mind-games/201303/the-zeigarnik-effect-and-quest-logs-8)" (popular-press application; see Limitations for replication caveats on the underlying effect)
- Full internal audit: `research/claim-ledger.md` (this project folder)
