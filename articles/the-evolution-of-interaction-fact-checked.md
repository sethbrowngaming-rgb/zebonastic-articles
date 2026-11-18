# The Evolution of Interaction: Why Hard Fail States Are Disappearing in Modern Game Design

*A fact-checked rewrite. The original draft's core thesis holds up under research, but it presented one single-author framework (a five-tier failure-penalty hierarchy) as neutral field-wide consensus without attribution, misdescribed one case study game, misapplied one academic term to a claim it wasn't coined for, overstated the origin of "failing forward," and included one direct quotation that could not be sourced. All five are corrected below. See the Claim Ledger for the full audit trail.*

---

## 1. Introduction

The central question this piece investigates: **has video game design actually moved away from punishing failure with hard resets, and if so, what replaced it, and why?**

The intuitive story is that games have simply gotten "easier" or more forgiving as the medium matured and chased broader audiences. That story is too flat to survive the evidence. What has changed is not primarily how hard games are — Dark Souls, Elden Ring, and Bloodborne remain some of the best-selling mechanically punishing games of the last fifteen years — but how failure is *processed* by the game's systems once it happens. Where a 1980 arcade cabinet terminated play outright and asked for another quarter, a 2026 game is more likely to route failure back into the story, into a currency, or into a status effect that changes the next attempt without erasing it.

**We know** the arcade-era hard fail state was shaped substantially by coin-operated business economics. **We know** several specific, well-documented games (Hades, the Nemesis System in Shadow of Mordor, Disco Elysium) route failure into narrative or systemic consequence rather than a stop condition. **The evidence suggests**, but no single source fully proves, that this shift is best explained by a combination of changed monetization incentives, storage and save-state technology, and applied psychology about player retention — three explanations that overlap rather than compete. This article traces that evidence, attributes the frameworks it borrows, and is explicit about where a claim is confirmed versus inferred.

## 2. Context: The Economic and Technical Origins of the Hard Fail State

The hard fail state is not a design ideal that later designers betrayed — it began substantially as an artifact of hardware limits and a specific business model. During the arcade era of the late 1970s and 1980s, cabinets earned revenue per credit inserted. Publishers and operators favored steep, escalating difficulty curves that reliably ended a session within a few minutes of play, converting a "Game Over" screen into what amounted to a point-of-sale prompt: continued play required another quarter. This pattern is documented consistently across independent game-history retrospectives rather than resting on a single contested claim. **We know** this was an industry-wide pattern; **the evidence suggests**, without being separately confirmed for any one title's original design documents, that any individual game's specific difficulty tuning also reflected simpler engineering (escalating enemy speed and spawn rate is cheaper to implement than new content) alongside the monetization incentive — the two explanations reinforce rather than compete with each other.

When games moved to home consoles and PCs through the 1980s and 1990s, the coin-slot rationale disappeared, but the mechanical habit — steep difficulty, full restarts on failure — persisted for a time, partly because limited storage meant a full level or game restart was often the only "save" a machine could offer. As storage capacity, internal memory, and later online infrastructure expanded, the structural incentive shifted from artificial gatekeeping toward retention: keeping a player inside the game rather than pushing them toward a restart or a purchase decision. In contemporary design, the ground-truth "Game Over" screen (full stop, no continuation) is comparatively rare outside genres that use it deliberately, such as roguelikes.

## 3. Evidence: A Taxonomy of Failure Penalties — and Whose Taxonomy It Is

Failure is not a single event but a spectrum of design sanctions of different severity. The original draft organized this spectrum into a five-tier hierarchy without saying where it came from. That was a citation gap: the specific structure — Time, Progress, Resources, Power, Everything, in that order, with Bloodborne as the resource-tier example — closely tracks games-design writer Josh Bycer's "The Hierarchy of Fail States." **We know** this is Bycer's stated framework, not neutral field-wide consensus; a separate, differently organized academic taxonomy of videogame failure exists (presented at the 2020 Foundations of Digital Games conference), which categorizes failure by cause rather than purely by penalty severity. The two are not contradictory, but their coexistence means Bycer's hierarchy is one useful lens among more than one, and this article credits it as such.

| Penalty Tier | Structural Mechanism | Impact on Player Experience | Representative Mechanic |
|---|---|---|---|
| Time | Loss of temporal investment; retry at or near the failure point | Minimal friction if the core loop stays engaging | Instant respawns (*Super Meat Boy*, *Celeste*) |
| Progress | Retracing completed content | Frustration scales with repetition and lack of novelty | Bonfire/checkpoint networks (*Dark Souls*, *Elden Ring*) |
| Resources | Depreciation of inventory, currency, or durability | Forces "dead time" farming; compounding deficit | Blood vial/bullet repurchasing (*Bloodborne*) |
| Power | Reduction of character capability or attributes | Can trigger a downward spiral, making retries harder | Max-health reduction on death (*Dark Souls II*) |
| Everything | Total wipe of progress and state; permanent death | High stakes, but often *less* demoralizing than Power loss because variance is expected going in | Classic roguelikes (*NetHack*), Iron Man modes |

*(Source: adapted from Josh Bycer, "The Hierarchy of Fail States," Game Developer / Game-Wisdom. See Chart 1 below for a visual rendering of this same data.)*

Bycer's own central claim, and the one this article's thesis leans on most, is that risk of player attrition rises as penalties move up this hierarchy from Time toward Power — not because harsher penalties are inherently worse, but because Resource- and Power-tier penalties force a "dead time" recovery loop before a player can even re-attempt the challenge that beat them. *Bloodborne*'s requirement to farm blood vials and quicksilver bullets after repeated boss failures is the most consistently cited example of this: it pulls players out of the high-skill challenge loop and into low-level resource acquisition. **This is a strong inference, not a settled fact** — FromSoftware itself treated blood-vial friction as a real but fixable problem, later adding a dedicated farming area and a trading mechanic in the Chalice Dungeons, which suggests the studio agreed friction existed without necessarily agreeing the mechanic was a design failure.

### Chart 1 — The Failure Penalty Hierarchy

![A five-step ascending bar chart showing Time, Progress, Resources, Power, and Everything penalty tiers on the x-axis, with player attrition risk increasing on the y-axis for the first four tiers before dropping slightly for the Everything tier, annotated with one representative game per tier](charts/01_penalty_hierarchy.png)

## 4. Psychological Framework: Flow, Friction, and the Paradox of Failure

Game scholar Jesper Juul's 2013 MIT Press book *The Art of Failure: An Essay on the Pain of Playing Video Games* is the field's most cited treatment of this subject and is accurately represented in the original draft's core claim: Juul argues that players voluntarily seek out an activity — games — that reliably makes them feel, however briefly, personally inadequate, and that this is only tolerable because the game simultaneously offers a legible path to redemption through skill improvement. **We know** this is the book's stated thesis.

The mechanism by which harsh penalties undermine that tolerable paradox is well supported by flow theory. Designer Jenova Chen's MFA thesis, "Flow in Games," directly applies psychologist Mihaly Csikszentmihalyi's flow theory to game design, arguing that sustained engagement requires keeping players in a dynamic channel between boredom (insufficient challenge) and anxiety (excessive challenge or penalty). **We know** this thesis exists and makes this argument; it is Chen's own primary academic work, not a secondhand summary of it.

The original draft also attributed a specific claim to designer Will Wright — that failure states should be "fast, intelligible, and instantly absorbed into the next action loop." **This quotation could not be verified in this research pass.** No primary interview, talk, or written source using this or closely equivalent phrasing was located. Per the evidence-gap rule, it has been removed rather than presented as fact. What remains defensible, and is supported by the sourced material above, is the narrower claim that hard resets interrupt flow by forcing what Chen's framework would describe as a jarring context switch from immersed play to frustrated meta-evaluation — a mechanism the flow literature supports in general terms, even without a specific Wright quotation to anchor it to.

## 5. Case Studies: "Failing Forward" in Practice

**Verified mechanics.** *Hades* (Supergiant Games, 2020) sends the player back to a central hub, the House of Hades, on every death. **We know**, from converging games journalism and at least one academic thesis on the game's narrative-gameplay structure, that this is not merely a respawn point: new dialogue becomes available specifically *because* a run failed, and a meta-currency (Darkness) persists past death to purchase permanent upgrades through the Mirror of Night system. Failure and narrative progression are the same mechanical event, not two separate systems bolted together.

**Developer-confirmed mechanics.** The Nemesis System in *Middle-earth: Shadow of Mordor* (Monolith Productions, 2014) is the best-evidenced case study in this article: the mechanism by which an orc who kills the player is promoted, gains new abilities, and retains a specific memory of the encounter is documented not only by games journalism but by Warner Bros.' own granted U.S. patent covering the system — a primary technical/legal document, not an inference. **We know** this mechanically and precisely.

**Design analysis.** *Disco Elysium* (ZA/UM, 2019) treats failed skill checks as narrative material rather than dead ends. **The evidence suggests**, based on converging critical analysis rather than a single located primary developer quote, that a failed check is frequently written to be more revealing of the protagonist's fractured psyche than a success would have been — the narrative continues, but the character's flaws become visible in the process.

**A corrected case study.** The original draft cited an unnamed "narrative spy RPG" using dice checks where failure "continues the scene," without identifying the game. That game is real: *ZERO PARADES: For Dead Spies*, developed and published by ZA/UM — the *Disco Elysium* studio — released for PC on May 21, 2026, with a PlayStation 5 version following later in the year. **We know** the developer and release details from games journalism and store listings. Its actual failure system is more specific than "continues the scene": it centers on three accumulating status effects — Delusion, Anxiety, and Fatigue — that build from dialogue and skill-check outcomes and progressively worsen future checks, managed through in-fiction coping actions like sleep or substance use. A contemporaneous review states plainly that "you're inevitably going to fail in dialogue checks, and a core part of the experience is dealing with the fallout and figuring out how to push on." This is a clean, corrected example of a studio building failure directly into a compounding character-state system rather than a binary pass/fail gate.

**Origin of the underlying philosophy.** "Failing forward" as a general design principle — where an unsuccessful action still advances the fiction rather than halting it — is closely associated with tabletop RPG design, and in particular with Vincent Baker's *Apocalypse World* (2010) and the "Powered by the Apocalypse" system it spawned, in which move resolution is built so that even failure produces a GM-driven complication rather than simply nothing. **This is a strong inference, not a confirmed origin claim.** Tabletop design discourse discusses "fail forward" as a broader school of thought with roots that predate and extend beyond any single game, and this research pass found no single uncontested primary source crediting Baker or *Apocalypse World* as the specific coinage. The original draft's claim that the concept "originated" there overstated a real and influential connection into an origin story the evidence doesn't fully support.

### Chart 2 — Failure Routing: Stop vs. Continue

![A simple two-path flow diagram: on the left, the traditional hard-fail path (Failure leads to Game Over leads to Restart); on the right, the failing-forward path (Failure leads to Narrative Consequence or Systemic Consequence, which feeds back into Continued Play), illustrating the structural difference described in this article](charts/02_failure_routing.png)

## 6. Non-Punitive Ludology: Removing the Fail State Entirely

A separate and more radical trend removes mechanical fail states altogether. *Gone Home*, *Firewatch*, and *What Remains of Edith Finch* discard health bars, combat, and lose conditions entirely in favor of environmental storytelling and observation. **We know** this design choice is real and consistently documented by both their own developers and critics, and that it triggered a genuine, sustained critical and academic debate — sometimes summarized under the label "walking simulators" — over whether such works fall outside conventional definitions of "game" that require explicit rules and win/lose conditions. This debate has produced its own academic literature, including a dedicated journal special issue and monograph-length treatment, rather than being a purely informal argument. **The evidence suggests** that this design choice reflects a considered position (that interactivity exists on a continuum, and that removing fail states shifts player agency from tactical survival toward interpretation) rather than a simplification of the medium — but this is this article's own synthesis of the critical debate, not a single settled academic consensus, since the "is this a game" question is explicitly still contested in the sources reviewed.

## 7. Counterarguments and Alternative Interpretations

**The strongest opposing view:** softened fail states could just as easily be read as commercial casualization — broadening the audience by removing the exact friction that gave earlier games their identity and difficulty-driven prestige — rather than as the deeper structural or narrative advancement this article argues for. Genres and titles that retain harsh Power- and Everything-tier penalties (*Iron Man* modes, classic roguelikes, *Darkest Dungeon*'s permanent stat loss on failure) remain commercially and critically successful in 2026, which complicates any claim that softer failure is a one-directional industry trend rather than one popular strategy among several coexisting ones.

**Supporting evidence for that criticism:** Bycer's own hierarchy explicitly documents that harsher penalty tiers survive and are still deliberately chosen by some studios — the existence of a hierarchy at all implies designers are still actively choosing points along it, not converging on the softest option available.

**A weakness in this article's own argument:** several of the strongest examples above (Hades, the Nemesis System, Disco Elysium, Zero Parades) are single, celebrated, high-profile titles. This article did not attempt — and does not claim — a systematic, quantified survey of how failure penalties have shifted across the full population of games released each year; the case-study method used here is illustrative of a real pattern, not proof of its statistical prevalence across the medium.

**Unresolved questions:** whether the shift toward softer, narratively integrated failure is driven primarily by retention economics (keeping players in a live-service or story-driven game rather than losing them to frustration), by storage/technology changes that simply made better failure-state design *possible*, or by a genuine evolution in design taste, is not something the sources reviewed in this pass settle definitively — the honest position is that these three explanations likely overlap and reinforce each other rather than any one being the sole cause.

## 8. Limitations of This Analysis

This research pass relied on web-searchable game-history retrospectives, games journalism, wiki and community documentation, one primary patent document (Nemesis System), one primary academic thesis (Chen), one primary published monograph (Juul), and store/review listings for the most recently released case study (*Zero Parades: For Dead Spies*). It did not include primary developer interviews for several claims (Disco Elysium's failure-writing philosophy, the precise causal weight of monetization versus technology versus design taste in the industry-wide shift), and one claim from the original draft (the Will Wright quotation) could not be sourced at all and was removed rather than softened. The Dark Souls II "removed in Scholar of the First Sin" claim from an earlier draft of this fact-check could not be confirmed and has been dropped; the mechanic is described only as it exists in the base game.

## 9. Conclusion

**What we know:** the arcade-era hard fail state was shaped substantially by coin-operated business economics; several specific, well-documented contemporary games (Hades, Shadow of Mordor, Disco Elysium, Zero Parades: For Dead Spies) route failure into narrative or systemic consequence rather than a stop condition, with the Nemesis System case confirmed to an unusually high standard via its own patent documentation; and Jesper Juul's and Jenova Chen's published academic work directly supports the psychological logic of why hard resets disrupt engagement.

**What we think:** the shift away from hard fail states is best explained by an overlapping combination of changed monetization incentives, expanded storage and save-state technology, and applied retention psychology, rather than any single cause — and the widely repeated five-tier failure-penalty hierarchy used to explain *why* harsher penalties risk player attrition is a useful, but single-author (Bycer), framework rather than settled field-wide theory.

**What we don't know:** how this shift distributes statistically across the full population of released games rather than a set of celebrated case studies; the precise weighting between the three overlapping causes above; and whether "failing forward" is accurately described as originating in *Apocalypse World* specifically, as opposed to being one influential expression of a broader tabletop design tradition. The honest framing is not that punishment has disappeared from game design — genres built on high-stakes loss remain commercially healthy — but that failure has been re-engineered, in a specific and traceable set of well-documented titles, from a wall that stops the game into a mechanism that keeps generating it.

---

## Sources

- [Wikipedia — History of arcade video games](https://en.wikipedia.org/wiki/History_of_arcade_video_games)
- [Betson — The History of Coin-Operated Arcade Games](https://www.betson.com/the-history-of-arcade-games/)
- [Jesper Juul — The Art of Failure (author's own page)](https://jesperjuul.net/artoffailure/)
- [MIT Press — The Art of Failure](https://mitpress.mit.edu/9780262529952/the-art-of-failure/)
- [Jenova Chen — "Flow in Games" MFA Thesis (PDF)](https://www.jenovachen.com/flowingames/Flow_in_games_final.pdf)
- [Wikipedia — Jenova Chen](https://en.wikipedia.org/wiki/Jenova_Chen)
- [Josh Bycer — The Hierarchy of Fail States, Game Developer](https://www.gamedeveloper.com/design/the-hierarchy-of-fail-states)
- [ACM Digital Library — A Diagnostic Taxonomy of Failure in Videogames (FDG 2020)](https://dl.acm.org/doi/fullHtml/10.1145/3402942.3402979)
- [GamesRadar+ — Shadow of Mordor's Nemesis system was patented by Warner Bros](https://www.gamesradar.com/middle-earth-shadow-of-mordors-nemesis-system-was-patented-by-warner-bros/)
- [Engadget — Shadow of Mordor's Nemesis system is locked behind a patent until 2036](https://www.engadget.com/gaming/shadow-of-mordors-innovative-nemesis-system-is-locked-behind-a-patent-until-2036-195437208.html)
- [Game Developer — How Supergiant weaves narrative rewards into Hades' cycle of perpetual death](https://www.gamedeveloper.com/design/how-supergiant-weaves-narrative-rewards-into-i-hades-i-cycle-of-perpetual-death)
- [TheGamer — Hades' Mirror Of Night Does Upgrades Right](https://www.thegamer.com/hades-mirror-of-night-roguelite-progression/)
- [RPG Site — Zero Parades: For Dead Spies Review](https://www.rpgsite.net/review/20391-zero-parades-for-dead-spies-review)
- [TechRaptor — Zero Parades: For Dead Spies Release Date](https://techraptor.net/gaming/news/zero-parades-for-dead-spies-release-date)
- [Wikipedia — Ludonarrative dissonance](https://en.wikipedia.org/wiki/Ludonarrative_dissonance)
- [The Ringer — The Subversive Genius of Far Cry 2, 15 Years Later](https://www.theringer.com/2023/10/20/video-games/far-cry-2-15th-anniversary-clint-hocking-ubisoft-open-world-fps)
- [Gnome Stew — Failing Forward: How to Make Failure Interesting In RPGs](https://gnomestew.com/failing-forward-how-to-make-failure-interesting-in-rpgs/)
- [The Daily Apocalypse — Beyond Success & Failure: Failing Forward and moves in Apocalypse World](https://daily-apocalypse.com/daily-apocalypse/143-beyond-success-failure-failing-forward-and-moves-in-apocalypse-world)
- [Fextralife — Dark Souls 2 Wiki: Human Effigy](https://darksouls2.wiki.fextralife.com/Human+Effigy)
- [Press Start — Special Issue on Walking Simulators](https://press-start.gla.ac.uk/press-start/announcement/view/17)
- [MIT Press — Real Games: What's Legitimate and What's Not in Contemporary Videogames](https://mitpressbookstore.mit.edu/book/9780262042604)
