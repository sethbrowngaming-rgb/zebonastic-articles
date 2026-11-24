# Claim Ledger: "What 49.9% Counts: Reading Steam's AI Disclosure Numbers"

Central question: What does the 49.9% figure (share of October 2026 Steam releases with an AI disclosure) measure, and what can it support?

Source numbers match the article's Sources section. Research dates: Nov 23-24, 2026. PCGame.com figures are as of Nov 24, 2026 (live page, updates daily).

## Claim ledger

| # | CLAIM | CLASS | EVIDENCE | SOURCE | CONFIDENCE | ALTERNATIVE EXPLANATION |
|---|-------|-------|----------|--------|------------|-------------------------|
| 1 | 49.9% of Oct 2026 Steam releases carried the AI disclosure; 26.4% in Oct 2025; 1.7% in Jan 2024 | Observation (community tally) | Reddit post by u/ploz as reported by Dexerto, Destructoid, others | S3, S4 | Confirmed as reported; original post not fetchable (blocked) | Analyst error; method partly undocumented |
| 2 | Yearly shares: 13.3% (2,319/17,392), 24.0% (4,937/20,552), 40.5% 2026 to Nov 24 (12,351/30,474) | Observation | PCGame.com statistics page | S2 | Confirmed as stated by the analyst; not independently verified | Release counts depend on an unexplained release-date method |
| 3 | Early-Nov coverage gave 13.2% and 40.1%; page later showed 13.3% and 40.5% | Observation | Dexerto, Destructoid vs PCGame page | S2, S3, S4 | Confirmed | Live dataset drift |
| 4 | Oct 2025 to Oct 2026: +23.5 points, factor about 1.9 | Arithmetic | 49.9 - 26.4; 49.9 / 26.4 | S3 | Confirmed (arithmetic) | None |
| 5 | Jan 2024 baseline is 1.7% | Observation | Most outlets say 1.7%; Kantan says 1.4% | S3, S14 | Moderate; conflicting | Rounding or different denominators; one-month baseline |
| 6 | Valve requires developers to describe AI use in the Steamworks Content Survey; pre-generated vs live-generated; live requires guardrails | Observation | Valve documentation; GamesRadar | S1, S9 | Confirmed | None |
| 7 | Valve's form is scoped to AI content that ships with the game and is consumed by players; efficiency gains not the focus | Observation | Valve documentation | S1 | Confirmed | None |
| 8 | Valve rewrote the form in Jan 2026 (reported Jan 16), keeping the requirement; coding helpers fall outside it; spotted by Simon Carless | Observation | PC Gamer | S8 | Confirmed (secondary) | None |
| 9 | Flag is never an index of all AI use; a game with only dev-tool AI has no reason to set it | Interpretation | Claims 6-8 | S1, S8 | Strong inference | Developers may over-disclose |
| 10 | Disclosure is self-reported; undisclosed AI not counted; figures are likely lower bounds | Observation | PCGame methodology page | S2 | Confirmed | None |
| 11 | Totally Human Media (Jul 2025): 7,818 flagged titles, about 7% of library, a little under 1 in 5 of 2025 releases to date | Observation | Tom's Hardware | S10 | Confirmed as reported (secondary) | Different date and denominator |
| 12 | Two analyses of the same flag agree on direction; this does not show the flag tracks real AI use | Interpretation | Claims 2, 11 | S2, S10 | Strong inference for direction; magnitudes not validated | Both could share the same reporting bias |
| 13 | Flagged releases rose about 5.3x (2,319 to 12,351); unflagged rose about 20% (15,073 to 18,123), 2026 partial | Arithmetic | PCGame table | S2 | Confirmed (arithmetic) | Total counts may not be comparable across years |
| 14 | Share rose mainly because flagged releases multiplied | Interpretation | Claim 13 | S2 | Moderate | Unflagged includes undisclosed AI; counting method |
| 15 | Use categories among 10,723 analyzed 2026 disclosures: art 63%, text 32%, store/marketing 27%, music 22%, code 17%, voices 8%, live 3%; 8% marketing-only | Observation | PCGame page | S2 | Confirmed as stated | Keyword program may misclassify |
| 16 | 1,628 flagged games missing from use breakdown (1,295 signed-in-only pages, 333 no statement) | Observation | PCGame page | S2 | Confirmed as stated | None |
| 17 | Most disclosures concern pre-made assets, not live AI | Interpretation | Live = 3% | S2 | Strong inference | Category parsing |
| 18 | Code (17%) is ambiguous given the exclusion of efficiency tools | Interpretation | Valve scope; Gadget Review caution | S1, S7 | Moderate | Code could be shipped AI scripts |
| 19 | Disclosure rate 47% (8,981/19,176) for under 10 reviews vs 15% (109/724) for 1,000+ | Observation | PCGame page | S2 | Confirmed as stated | Review count confounded (claim 24) |
| 20 | High-output developers 64% vs 38% single-release; group is 62 developers; earlier coverage 68% / 37% | Observation | PCGame page; Dexerto | S2, S3 | Confirmed as stated; small group | Small-n volatility |
| 21 | Flagged games are 41% of 2026 releases but 14% of reviews | Observation | PCGame page | S2 | Confirmed as stated | Reviews are a proxy, not sales |
| 22 | Positive-review rate about 78% vs 83% (50+ reviews); does not show AI caused lower ratings | Observation | PCGame page; Power Up Gaming | S2, S6 | Confirmed as stated | Selection and confounding |
| 23 | 49.9% does not mean half of games were made with AI; one disclosure can cover one image | Interpretation | Gadget Review; Valve scope | S7, S1 | Strong | None |
| 24 | Review count confounds size: recent releases have fewer reviews; players avoiding flagged games would also lower counts | Interpretation (reasoned) | Method of the dataset | S2, S3 | Weak to moderate; untested | Confounds may be small |
| 25 | GDC 2026: 36% of respondents use generative AI at work; 52% say negative impact (30%, 18% prior years) | Observation | GDC; GamingOnLinux | S11 | Confirmed | Survey sample unknown |
| 26 | Another survey (via press): 29% early 2026 vs 36% early 2025 | Observation | Outlook Respawn | S12 | Moderate (second-hand) | Different sample |
| 27 | Most common work uses were research/brainstorming, then admin, then code help | Observation | Global Sources summary | S16 | Moderate (secondary) | None |
| 28 | Tim Sweeney argued storefront AI labels make little sense | Observation | PC Gamer | S8 | Confirmed (paraphrased) | None |
| 29 | Population difference may explain Steam vs survey divergence | Interpretation (hypothesis) | Claims 19, 25, 26; 19,176 of 30,474 releases have under 10 reviews | S2, S11, S12 | Weak inference | Sentiment effects; different definitions |
| 30 | Jan 2026 narrowing would alone lower disclosures | Interpretation (inference) | Claim 7-8 | S1, S8 | Weak inference; effect unmeasured | Clarity could raise disclosures |

Omitted: Games.gg tally (30% to mid-July 2026; 10.9% Jan 2024), untraceable and conflicting; cited only as an example of disagreement (S15). The "29-fold rise" is noted as arithmetic but not relied on.

## Devil's Advocate Review (hostile pass on first draft)

| Attack | Verdict | Action |
|--------|---------|--------|
| Section 3.2 called the Totally Human count a "different method"; both read the same self-reported flag | Valid | Rewrote: separate analysis of the same flag; agreement supports direction only |
| Cited "114,000 library" and "Steam API" without a source in the list | Valid | Removed both; kept the 7% as reported |
| "78% of reviews are positive" may misstate an average-per-game metric | Valid | Reworded to "positive-review rates" |
| "October releases have least time to collect reviews" ignores November releases | Valid | Changed to "most recent weeks" |
| "Steam's release flow is dominated by small and high-volume releasers" over-claims | Valid | Replaced with the count: 19,176 of 30,474 have under 10 reviews |
| "Surveys do not show a rise" overstated from one trend | Valid | Qualified: "in the sources I found" |
| Table said Jan 2026 narrowing "would lower disclosures" as fact | Valid | Marked as inference in table, text and ledger |
| Research/brainstorming "would not ship to players" asserted flatly | Minor | Reworded; attributed to the trade summary |
| Jan 2024 start date lacked a supporting citation for the rule's date | Minor | Added S13 |
| Table numbering out of order | Minor | Renumbered by order of appearance |

## Fact-check pass (sentences with numbers, dates, names, causal or absolute words)

| Statement | Status |
|-----------|--------|
| All percentages and counts in Figures 1-4 and Tables 1-3 match S2/S3 (recomputed: 1.47/13.33/24.02/40.53%; buckets 46.8/33.1/28.2/26.9/15.1%; 5.33x; +20.2%) | CONFIRMED |
| Reported bucket totals on the PCGame page differ slightly from the sums (12,349 vs 12,351; 30,461 vs 30,474); the page notes this | CONFIRMED (disclosed) |
| "49.9% ... highest month in the dataset" | CONFIRMED (S3) |
| Valve January 2024 start; January 16, 2026 rewrite; Carless | CONFIRMED (S1, S8, S9, S13) |
| "Share rose mainly because flagged releases multiplied" | INFERRED |
| "Most disclosures concern pre-made assets" | INFERRED |
| Population-difference and sentiment explanations | SPECULATIVE, labeled as hypotheses |
| Review-count confound | INFERRED, labeled untested |
| Nothing left UNSUPPORTED after the devil's advocate pass | - |

Image check: all 7 images are embedded in the HTML as data URIs; loaded in headless Chrome with no broken images and every one has alt text.
