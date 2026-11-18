# The Lost Art of the Diegetic UI: Why Modern Games Can't Stop Cluttering Your Screen

*A fact-checked rewrite. One outright factual error (a legal citation) and one misclassified example were corrected below; several specific claims that could not be sourced in this research pass were softened or removed. See the Claim Ledger for the full audit trail.*

---

## 1. Introduction

The central question this piece investigates: **why has mainstream game UI moved away from embedding information in the game world, even as the graphical fidelity of that world has improved?**

The tempting narrative — "designers got lazy" or "publishers stopped caring about immersion" — doesn't survive contact with the evidence. The more defensible answer is structural: several independent pressures (data-dense live-service systems, rendering fidelity that makes environments harder to read at a glance, playtest-driven usability iteration, and disability-accessibility law) each push toward flat, screen-space interfaces for reasons that have little to do with any individual designer's taste. This article traces each pressure with named sources, and is explicit about which parts of the argument are confirmed and which are this article's own synthesis.

## 2. Context: A Framework for Talking About UI

Game-design discourse commonly sorts interface elements using a framework introduced by Erik Fagerholt and Magnus Lorentzon in "Beyond the HUD: User Interfaces for Increased Player Immersion in FPS Games," a 2009 thesis at Chalmers University of Technology. **We know** this thesis exists and is the commonly cited origin of the diegetic/non-diegetic/spatial/meta terminology used throughout modern game-design writing; it is indexed under this title and author pair and is cited by name across independent secondary sources. One scope note the framework's own title makes explicit: it was developed by studying first-person shooters, and its extension to every other genre — which this article does, following common industry practice — is a later, informal generalization rather than a claim the original thesis makes about itself.

The framework sorts UI along two axes. **Diegesis**: is the player character aware of this element within the story? **Spatiality**: does the element exist inside the 3D world, or does it sit as a flat layer on the screen? Crossing these axes produces four categories.

### Chart 1 — The Four Quadrants

![The four quadrants of game UI: diegetic, spatial, meta, and non-diegetic, mapped by whether the character is aware of the element and whether it exists in 3D world space](../charts/01_quadrant.png)

| Quadrant | Character aware? | In 3D world space? | Representative examples |
|---|---|---|---|
| **Diegetic** | Yes | Yes | Dead Space's RIG suit health meter; Far Cry 2's paper map and GPS unit; Metro 2033's filter-timer watch |
| **Spatial** | No | Yes | Breath of the Wild's targeting reticles; Warcraft III–style unit selection rings; "yellow paint" on climbable ledges |
| **Meta** | Implied (represents a sensory/physical state) | No | Damage vignettes and blood-spatter screen effects; intoxication screen blur |
| **Non-diegetic** | No | No | Traditional HUD health bars; corner minimaps; floating ammo counters |

**One correction to the source material:** an earlier draft of this analysis classified a racing game's speedometer overlay as "Meta" UI, grouped with damage-vignette effects. Every secondary source located in this research pass that lists meta-UI examples (screen blur, blood-flash, intoxication effects) describes the category as screen-space representations of the avatar's *physical or sensory state* — not neutral instrument readouts. A floating speedometer is quantitative vehicle telemetry with no represented "feeling" attached to it; by the framework's own logic that makes it non-diegetic, not meta. The corrected table above removes that example.

## 3. Evidence: The Golden Age of Diegetic Design

Diegetic UI's most-cited case studies cluster in the mid-to-late 2000s, when 3D engines matured enough to let designers embed interface geometry directly into character models and environments.

**Dead Space (2008).** Visceral Games built player status into the protagonist's Resource Integration Gear (RIG) suit: health as a glowing strip down Isaac Clarke's spine, stasis charge as a shoulder-mounted gauge, and ammo counts on the weapons themselves. Lead UI designer Dino Ignacio discussed this design directly in industry talks covering the RIG, the front-end menus, and the "bench" crafting station. Inventory, star maps, and audio logs are displayed as in-world holographic projections that Isaac appears to physically manipulate. **We know**, from convergent independent design retrospectives, that these menus do not pause the simulation — a detail repeated consistently across sources, though this research pass did not locate a single primary quote stating it in those exact words.

**Far Cry 2 (2008).** Ubisoft Montreal replaced the HUD's minimap and compass with a paper map and GPS device the player physically raises to check position. Confirmed directly by Benoit Perreault, a UI designer on the project, describing the design intent in his own account: the game world does not pause while the map is open — "bullets whizzing through the air prior to opening the map will continue to whiz straight into your body" — and the map becomes "dark and difficult to read" if the character is standing in shade. This is a stated, deliberate design choice, not an incidental limitation: the team wanted checking your position to carry real tactical risk.

**Metro 2033 (2010).** 4A Games tied gas-mask filter life to an analog wrist watch worn by the player character; as the filter degrades, the watch ticks down and the character's breathing grows labored. This mechanic is consistently documented across community wikis and cited as a worked example in secondary design literature. **The evidence suggests** this is an accurate description of the mechanic — no source disputes it — but no primary developer interview or GDC talk confirming 4A's own account of the design was located in this research pass, so this claim is reported at "strong inference" rather than "confirmed."

**Ghost of Tsushima (2020).** Sucker Punch replaced the conventional minimap with the "Guiding Wind" — a player-summonable gust that blows toward the currently marked objective, letting the camera and environment carry navigational information instead of a corner icon. This mechanic is independently confirmed across multiple sources. Commonly cited secondary cues — golden birds leading toward hidden shrines, smoke columns marking camps — are widely repeated in player guides; this article reports them at moderate confidence, since a Sucker Punch developer statement specifically confirming those two secondary cues was not located in this pass.

**Pacific Drive (2024).** Ironwood Studios centers the game's interface on a station wagon's dashboard. Game director Seth Rosen described the intent directly: "We tried to place as much as we could physically into the world, because that helps sell the relationship with the car, but also the sense that this is a real place that's threatening." **We know** this reflects a deliberate, stated design goal — this is a direct developer quote, not an inference. One specific from the original draft — a trip-computer screen mounted specifically on the passenger seat — could not be verified in this pass and has been removed rather than presented as fact.

### Chart 3 — Verified Timeline

![Timeline from 2008 to 2024 showing Dead Space, Far Cry 2, the Fagerholt-Lorentzon thesis, Metro 2033, the CVAA accessibility deadline, Ghost of Tsushima, and the yellow-paint debate years](../charts/03_timeline.png)

## 4. Case Study: The Visual Clutter Crisis

**Verified mechanics.** Contemporary live-service and looter-shooter titles frequently combine, on one screen: character/level indicators, health and shield meters, a compass strip with floating objective markers, segmented boss health bars, quest-tracking text, crosshair and hit-marker feedback, floating damage numbers, spatial highlight effects on interactable geometry, a corner minimap, squad status feeds, chat logs, ability cooldown rings, and ammo counters.

**Developer/critic statements.** Suicide Squad: Kill the Justice League (Rocksteady, 2024) is a frequently cited example: multiple independent outlets — Dexerto ("visual mess"), Dualshockers (players calling the UI's density comparable to mobile games), Niche Gamer, and ScreenRant (arguing the HUD undermined the game as much as its combat systems did) — reported widespread criticism of its interface density at launch.

**Design analysis.** **A correction to the source draft:** the original article described this game's HUD with a precise element-by-element screen-position map (specific claims about exactly what occupies the top-left, top-center, top-right, and lower corners of the screen). No source located in this research pass corroborates that level of positional specificity. Per the evidence-gap rule, this rewrite reports the *categories* of clutter that reviewers actually documented — listed above — without asserting an unsourced layout diagram.

### Illustration — What "Layered HUD" Criticism Looks Like

![Two side-by-side abstract mockups: a minimal screen with health shown on the character versus a cluttered screen with many overlapping HUD elements](../images/04_clutter_comparison.png)

*(This is an original illustrative composite built for this article, not a screenshot of any specific game — actual game interfaces are copyrighted assets this research pass did not have rights to reproduce.)*

**Limitations.** Attributing screen clutter purely to monetization incentives is a plausible but not fully evidenced causal claim. **The available sources document the criticism but do not establish, with confirmed internal design documentation, the specific weighting between monetization pressure, genre convention (looter-shooters have historically carried dense stat displays), and time-to-ship constraints for any single title.**

**Counterarguments.** Complex loot-tier, elemental-status, and cooldown-timer systems are difficult to convey diegetically without inventing an in-fiction justification for every stat (a "1.5% critical damage buff," for instance, has no obvious physical analogue). This is a structural argument in the genre's favor, not an excuse for any specific game's execution — reviewers criticizing Suicide Squad's HUD were responding to a real, testable player experience, not a hypothetical.

## 5. Why the Retreat From Diegesis: Four Named Pressures

### 5.1 Data density

Diegetic UI communicates simple, low-cardinality state well: one health pool, one ammo count, one cardinal direction. Modern RPG/live-service systems layer tiered loot rarities, elemental status effects, percentage-based buffs, and stacked cooldowns — a data volume that is difficult to represent through physical character models or world geometry without inventing new in-fiction devices for every new stat. **This is a structural, mechanical argument** (more variables require more display bandwidth), not a claim about any specific developer's motivation, and it holds regardless of a game's monetization model.

### 5.2 The legibility paradox and "yellow paint"

As rendering fidelity rose, environments grew visually denser — more foliage, more photogrammetric detail, more competing light sources — making an interactable ledge or door harder to distinguish from decorative geometry by eye alone. The industry's most visible response has been "yellow paint": bright, non-diegetic coloring applied to climbable or interactable surfaces. This is now a named, actively debated discourse (Wikipedia hosts a dedicated article on the topic), documented in Final Fantasy VII Rebirth, Resident Evil 4 Remake, and God of War Ragnarök. **We know**, from a developer quote reported by GamesRadar+ regarding Resident Evil 4 Remake, that at least one studio has defended the practice on legibility grounds directly: "Realism is less immersive" was the framing given for why unmarked realistic environments can produce worse player outcomes than a clearly marked, less "realistic" one.

### 5.3 Playtesting and the telemetry loop

AAA studios commonly run structured playtests instrumented to flag friction — missed doorways, circling, failure to find a path — as usability defects. **The evidence suggests**, and this is standard, widely repeated industry methodology, that when playtesters get lost, a frequent production response is to add an explicit non-diegetic aid: a waypoint, a minimap trail, an NPC hint line. **This article did not locate a primary source tying a specific named studio's internal telemetry directly to a specific clutter decision** — the causal mechanism described here (repeated across general industry-methodology literature) is reported as a documented industry pattern, not a proven cause for any single title's UI choices, per the Causality Test.

A secondary, more speculative claim in this space deserves its own confidence label: that reliance on waypoint-following measurably degrades players' independent spatial reasoning over time. This is a plausible, frequently asserted idea in design commentary. **This remains unverified** as a controlled empirical finding in the sources reviewed for this article — it is presented here as **a widely held hypothesis**, not as a settled result.

### 5.4 Accessibility law

In the United States, the 21st Century Communications and Video Accessibility Act (CVAA) requires that Advanced Communications Services (ACS) built into a game — voice chat, text messaging, peer-to-peer communication — be accessible to players with disabilities. **We know**, from the FCC's own published guidance, that this obligation falls under **Title I** of the CVAA, and that the FCC's "usability" standard extends to the full path of controls needed to reach and operate an ACS feature, not just the feature's core function. **A correction to the source draft:** the original article cited both "Title I and Title II" as governing this requirement. Title II of the CVAA is a separate obligation covering video-programming accessibility (closed captioning and audio description for television and video distribution) and does not itself govern in-game chat or messaging interfaces. This citation error is corrected here; the substantive claim (that reaching ACS features requires accessible UI paths) is accurate and Title I is the correct citation. Non-compliance carries real financial exposure: FCC guidance cited in this research pass lists per-violation forfeitures in the low six figures.

Because diegetic elements are bound to in-world lighting, camera motion, and perspective distortion, they are structurally harder to make compliant with contrast, scaling, and screen-reader requirements than a flat 2D overlay is. **This is a reasonable structural inference** from how accessibility standards are typically implemented (text scaling, high-contrast modes, colorblind palettes) rather than a claim sourced to a specific accessibility researcher's study of diegetic UI specifically.

## 6. Counterarguments and Alternative Interpretations

**The strongest opposing view:** this article's four-pressure framing risks over-explaining a trend that may be simpler than it looks — genre convention and production-cost minimization. Building a fully diegetic status system (custom animations, in-world holograms, physically modeled instruments) is expensive and slow; a floating 2D HUD is a decades-old, well-understood, cheap-to-implement default. Some of the retreat from diegesis may be ordinary cost discipline rather than a response to any of the four pressures argued above.

**Supporting evidence for that criticism:** this article's own comparative table (Chart 2, below) rates diegetic UI as maximum engineering complexity — the same table used to argue diegetic UI's immersive strengths also documents its cost. A studio under schedule pressure has a direct incentive to default to the cheaper non-diegetic option independent of accessibility law, data density, or playtesting outcomes.

**Weaknesses in this article's own argument:** several claims here (5.1, 5.3's telemetry mechanism, 5.4's structural-inference paragraph) rest on general industry literature and internal reasoning rather than a named studio's specific, on-record account of its own decision-making. Where that is true, this article has flagged the claim's confidence level explicitly rather than presenting it with the same certainty as, for example, the FCC's own published ACS rules.

**Unresolved questions:** whether the recent wave of hybrid, context-sensitive HUDs (fading UI during exploration, surfacing it in combat) represents a genuine synthesis of these four pressures or simply a new default that will itself be criticized in five years is not something the sources reviewed here can settle.

## 7. Comparative Synthesis

The chart below is this article's own qualitative synthesis of trade-offs discussed in the sections above — it is **not** measured data, and is presented as an analytical summary rather than an empirical finding.

### Chart 2 — Comparative Synthesis

![Heatmap comparing diegetic, spatial, meta, and non-diegetic UI across immersion, cognitive readability, data density capacity, accessibility compliance, and engineering complexity, rated low to maximum](../charts/02_comparative.png)

## 8. Limitations of This Analysis

This research pass relied primarily on web-searchable secondary design commentary, a small number of direct developer quotes located via trade press and one designer's own portfolio writeup, one government regulatory source (the FCC), and Wikipedia/community-wiki documentation for well-established mechanics. It did not include a direct reading of the full Fagerholt–Lorentzon thesis PDF (only secondary summaries of its content), a 4A Games or Sucker Punch developer interview obtained firsthand, or systematic review coverage of every title mentioned. Two claims from the original draft were identified as outright errors and corrected (the CVAA Title II citation; the meta-UI speedometer example); several others were downgraded from unqualified statements to explicitly hedged language per the evidence-gap rule.

## 9. Conclusion

**What we know:** the diegetic/non-diegetic/spatial/meta framework is a real, named academic contribution (Fagerholt & Lorentzon, 2009) that the design industry has since generalized beyond its original FPS-specific scope. Dead Space, Far Cry 2, and Pacific Drive's diegetic design choices are confirmed by direct developer statements. The CVAA's ACS accessibility requirement is a real, Title I legal obligation with disclosed enforcement penalties. "Yellow paint" is a real, named, actively contested design discourse with developers on record defending it for legibility reasons.

**What we think:** the four pressures this article identifies — data density, the legibility paradox, playtesting-driven iteration, and accessibility law — are each independently well-evidenced as real forces acting on modern UI design, and together offer a more complete explanation than any single-cause narrative. Their *relative weighting* against each other, and against simple cost discipline (Section 6), is this article's own synthesis rather than a fact established by any cited source.

**What we don't know:** the precise causal mechanism by which any single studio's playtesting data led to a specific clutter decision; whether player spatial reasoning measurably degrades from waypoint reliance, as a controlled finding rather than a widely-asserted hypothesis; and whether adaptive/contextual HUDs represent a durable industry direction or a transitional compromise.

---

## Sources

- [Fagerholt & Lorentzon — "Beyond the HUD" (thesis record)](https://www.researchgate.net/publication/277202228_Beyond_the_HUD_-_User_Interfaces_for_Increased_Player_Immersion_in_FPS_Games)
- [Semantic Scholar — "Beyond the HUD" paper record](https://www.semanticscholar.org/paper/Beyond-the-HUD-User-Interfaces-for-Increased-Player-Fagerholt-Lorentzon/16ee02a8839923752c6bc93f294bec67d73a586e)
- [nastyrodent.com — Diegetic vs Non-Diegetic UI: The 4-Type Framework](https://nastyrodent.com/diegetic-and-non-diegetic-ui/)
- [Medium / Lorenzo Ardeni — Types of UI in Gaming](https://medium.com/@lorenzoardeni/types-of-ui-in-gaming-diegetic-non-diegetic-spatial-and-meta-5024ce6362d0)
- [Game Developer — Video: Designing Dead Space's immersive user interface](https://www.gamedeveloper.com/design/video-designing-i-dead-space-i-s-immersive-user-interface)
- [Dead Space Wiki (Fandom) — Resource Integration Gear](https://deadspace.fandom.com/wiki/Resource_Integration_Gear)
- [Benoit Perreault — Immersive UI Design for Far Cry 2](https://www.benoitperreault.com/farcry2)
- [Metro Wiki (Fandom) — Gas Mask](https://metrovideogame.fandom.com/wiki/Gas_Mask)
- [Ghost Franchise Wiki (Fandom) — Guiding Wind](https://ghostfranchise.fandom.com/wiki/Guiding_Wind)
- [Ludonode Studios (Medium) — The Invisible Hand: How Ghost of Tsushima Guides Players Without a Traditional HUD](https://ludonodestudios.medium.com/%EF%B8%8F-the-invisible-hand-how-ghost-of-tsushima-guides-players-without-a-traditional-hud-70f6772fcacc)
- [Game Developer — How Pacific Drive uses a diegetic UI to help players fall in love (with a car)](https://www.gamedeveloper.com/business/how-pacific-drive-uses-a-diegetic-ui-to-help-players-fall-in-love-with-a-car-)
- [Dexerto — Players rip Suicide Squad: Kill the Justice League for "visual mess" of a UI](https://www.dexerto.com/gaming/players-rip-suicide-squad-kill-the-justice-league-for-visual-mess-of-a-ui-2467063/)
- [Dualshockers — Suicide Squad: Kill The Justice League Mocked For Mobile Game-Like UI](https://www.dualshockers.com/suicide-squad-ui-berated-online/)
- [Niche Gamer — Suicide Squad: Kill the Justice League UI draws criticism for being cluttered](https://nichegamer.com/suicide-squad-kill-the-justice-league-ui-draws-criticism-for-being-cluttered/)
- [ScreenRant — Suicide Squad: Kill The Justice League's Biggest Problem Isn't Even Its Gameplay](https://screenrant.com/suicide-squad-kill-justice-league-problem-hud-gameplay/)
- [FCC — 21st Century Communications and Video Accessibility Act (CVAA)](https://www.fcc.gov/consumers/guides/21st-century-communications-and-video-accessibility-act-cvaa)
- [National Law Review — FCC Rules Require Communications in Video Games to Be Accessible and Usable](https://natlawreview.com/article/federal-communications-commission-rules-require-communications-video-games-to-be)
- [Wikipedia — Yellow paint in video games](https://en.wikipedia.org/wiki/Yellow_paint_in_video_games)
- [TechRadar — The infamous yellow paint discourse is back for Final Fantasy 7 Rebirth](https://www.techradar.com/gaming/the-infamous-yellow-paint-discourse-is-back-for-final-fantasy-7-rebirth)
- [GamesRadar+ — Debate over Resident Evil 4 Remake's yellow paint resurfaces as devs explain just how much help players really need](https://www.gamesradar.com/debate-over-resident-evil-4-remakes-yellow-paint-resurfaces-as-devs-explain-just-how-much-players-really-need-realism-is-less-immersive/)
- [SVG — Yellow Vs Red Circles In God Of War Ragnarok Explained](https://www.svg.com/1094276/yellow-vs-red-circles-in-god-of-war-ragnarok-explained/)
