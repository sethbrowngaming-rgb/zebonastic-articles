# Claim Ledger: "The Restraint Question: What DLSS 5 in Hogwarts Legacy Does and Doesn't Settle"

Central question: Does the shipped DLSS 5 implementation in *Hogwarts Legacy* (Nov 5, 2026) answer the March 2026 artistic-intent criticism, and what can the available evidence establish?

Source numbers match the article's Sources section. Date of research: Nov 22, 2026.

## Claim ledger

| # | CLAIM | CLASS | EVIDENCE | SOURCE | CONFIDENCE | ALTERNATIVE EXPLANATION |
|---|-------|-------|----------|--------|------------|-------------------------|
| 1 | DLSS 5 takes color and motion vectors per frame and adds lighting/material detail; Nvidia says structure is preserved | Observation (vendor statement) | Nvidia describes inputs, outputs, "deterministic, temporally stable" | S1 | Confirmed (what Nvidia says), not independently verified | Vendor description may not match behavior in all scenes |
| 2 | Hogwarts Legacy was the second game with official DLSS 5 support, on Nov 5, 2026 | Observation | Nvidia post; PCWorld | S2, S4 | Confirmed | None |
| 3 | NBA 2K27 was first, available Sept 3 | Observation | Nvidia post | S3 | Confirmed | None |
| 4 | Avalanche (Jose Villeta) said the team tuned environment lighting, tone and skin structural parameters to stay faithful to artistic intent | Observation | Statement published on Nvidia's page | S2 | Confirmed that it was said; hosted by vendor | Statement is promotional; reasons for specific settings not given |
| 5 | Nvidia says developers have model selection, Structure/Tone Intensity, semantic masking (incl. faces) and engine-level masking; players get on/off | Observation (vendor statement) | Nvidia post | S2 | Confirmed (what Nvidia says) | Not independently tested |
| 6 | Intensity and color-grading controls were described in March | Observation | Nvidia, GameStar, PC Gamer relaying Nvidia | S1, S6, S16 | Confirmed for intensity/color grading; masking in March not relied on (Nvidia page has conflicting date metadata) | Nvidia page may have been edited after March |
| 7 | March reaction criticized altered faces/art direction | Observation | Multiple outlets | S4, S5 | Confirmed that criticism occurred; no population-level sentiment claimed | Criticism may have been about unfinished demos |
| 8 | Some Ubisoft and Capcom developers learned of the reveal alongside the public | Observation (anonymous, secondhand) | Insider Gaming via PC Gamer | S6 | Weak (reported, unnamed) | Unrepresentative of all developers |
| 9 | Nvidia's Hogwarts comparison images concentrate on environmental lighting/materials; faces look essentially unchanged | Interpretation | PC Gamer, TweakTown, PCWorld read promo images | S4, S5, S12 | Strong inference for the promo images only | Images are vendor-selected; may not represent all scenes |
| 10 | Characters are not affected at all in the shipped build | Interpretation | Contradicted in part by DSOGaming (coat and hair look different/better) | S9 | NOT CLAIMED; evidence mixed | Sliders/masks may exclude faces but not clothing/hair |
| 11 | Difference from March reflects chosen settings | Interpretation | Controls existed in March | S1, S6, S16 | Weak inference | Retrained model (S5); pre-tuning demo clips; backlash response (S5, inference) |
| 12 | Independent tests of the September model on RTX 5090 at 4K show 51.2% (128.4 to 62.7 fps) and 60.4% (192 to 76 fps) loss | Observation | Digital Foundry data via Notebookcheck; TechSpot | S7, S8 | Confirmed as reported (7 is secondary) | Different settings/builds |
| 13 | Shipped Hogwarts on RTX 5090 4K DLSS Quality: 123 to 98 fps (20.3%) in Hogsmeade; 173 to 100 fps (42.2%) in opening area | Observation | DSOGaming excerpt; page could not be fetched in full | S9 | Moderate (excerpt only) | Hogsmeade CPU-limited hides GPU cost |
| 14 | Nvidia claims the October model is ~24% smaller (~118M params), uses 20% less 4K VRAM, ~2x performance | Observation (vendor claim) | Nvidia post; PC Gamer notes no independent verification | S2, S5 | Confirmed as a claim; unverified | Gains may vary by GPU/game |
| 15 | Lower Hogwarts cost is consistent with Nvidia's speedup | Interpretation | Claim 13 vs 12 | S2, S7-S9 | Weak inference | Game, scene, CPU limit and upscaler differences |
| 16 | TechSpot's per-frame cost: 7.9 ms (5090) to 53.1 ms (5050) at 4K | Observation (derived estimate) | TechSpot, one day, early access | S8 | Moderate | Estimates, not direct measurements; September model |
| 17 | "If 2x applied evenly: ~4 ms on 5090, ~27 ms on 5050" | Arithmetic | 7.9/2, 53.1/2 | S2, S8 | Arithmetic only; labeled as such | Claim may not apply evenly |
| 18 | Nvidia's 300 fps figure used 6x Multi Frame Generation and ray tracing | Observation | Nvidia, PCWorld | S2, S4 | Confirmed | None |

Omitted for lack of verifiable evidence: a secondary-aggregator claim (attributed to ComputerBase) that shipped NPC faces are not processed; the original could not be located.

## Devil's Advocate Review (hostile pass on first draft)

| Attack | Verdict | Action |
|--------|---------|--------|
| Title "Restraint by Setting" presupposes a cause (settings) | Valid | Retitled "The Restraint Question" |
| Draft omitted that the model itself was retrained between March and November (PC Gamer) | Valid, significant | Added retrained model as a competing explanation in section 4 and Table 3 |
| "Visibly gentler" in the deck overstates what vendor stills show | Valid | Changed to "Nvidia's own comparison images show a gentler presentation" |
| "Second game to ship" cited only Nvidia | Minor | Added PCWorld |
| Oct 16 model claim in Table 1 not cited in body | Minor | Added PCGH citation in 3.3 |
| "Player restraint is a developer-side decision" stated as fact | Valid | Prefixed "On Nvidia's description" |
| Performance comparison could be read as showing improvement | Valid | Figure 1 caption and section 3.3 state tests are not like-for-like |
| Reliance on a search excerpt for DSOGaming | Valid | Disclosed in text, Sources and Limitations |

## Fact-check pass (sentences with numbers, dates, names, causal or absolute words)

| Statement | Class | Note |
|-----------|-------|------|
| Nov 5, 2026 Hogwarts launch; Sept 3 NBA 2K27; Mar 16 reveal; Oct 16 model; Nov 23 Where Winds Meet | CONFIRMED | Nvidia, PCWorld, PCGH. Mar 16 per page byline |
| 24% smaller, ~118M parameters, 20% less 4K VRAM, ~2x | CONFIRMED as vendor claims | Not independently verified; labeled |
| 60% to ~30% expected NBA 2K27 hit | CONFIRMED as reported by PC Gamer | Nvidia-sourced |
| 51.2% (128.4 to 62.7); 60.4% (192 to 76); 20.3% (123 to 98); 42.2% (173 to 100) | CONFIRMED arithmetic | Percentages computed from reported fps |
| 49 to 39 fps on RTX 5080 | CONFIRMED (headline only) | Full test unread |
| 7.9 / 53.1 ms | CONFIRMED as TechSpot estimates | |
| ~4 ms / ~27 ms | INFERRED (arithmetic) | Labeled as not a measurement |
| 65% of PC Gamer readers not interested | CONFIRMED as reported | Self-selected poll, flagged weak |
| "Faces essentially unchanged" in promo images | INFERRED | PC Gamer, TweakTown, PCWorld; images not inspected by the author |
| "Difference reflects settings" | SPECULATIVE | Presented as one of four candidates |
| "Backlash prompted the pullback" | SPECULATIVE | Attributed to PC Gamer's author; no developer confirmation |
| Kellams (Epic) said intent can't be inferred until a director states it | INFERRED | Read from search excerpt of PC Gamer; paraphrased |
| Any claim that characters are wholly unaffected | UNSUPPORTED | Removed; contradicted in part by S9 |
