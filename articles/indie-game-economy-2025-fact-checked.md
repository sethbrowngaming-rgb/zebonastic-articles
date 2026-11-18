# Why Most Independent Games Don't Make Money: A Fact-Checked Look at the 2025 Steam Economy

*A Game Research Writer analysis. Compiled and fact-checked August 2026.*

---

## 1. Introduction

Every year, tens of thousands of independent developers release a game on Steam hoping to build a sustainable business. Most of them don't. This is not a new observation, but the scale of the gap between hope and outcome is worth stating precisely, because the precise numbers are frequently misreported — including, as the fact-check for this piece found, in earlier drafts of this very article.

This piece asks one question: **why do most independent games on Steam fail to generate a sustainable income for their developers, and what does the evidence actually show about the mechanisms behind that failure?**

Answering it requires separating three different kinds of claims that get blended together in most commentary on this topic: hard platform data (how many games were released, how much revenue they generated), analyst estimates (third-party tools inferring individual game performance from public signals), and developer-reported patterns (postmortems, marketing advice, community-collected benchmarks). Each carries a different level of reliability, and this piece labels them accordingly throughout.

A note on process: the first draft of this article contained a number of highly specific statistics — a five-tier revenue distribution table, a studio-size revenue-share breakdown, precise wishlist conversion percentages, and a specific cost-cutting trajectory attributed to Devolver Digital — that could not be traced to any real source after a dedicated fact-check pass. Those claims have been removed. Where a real, sourced number existed nearby, it replaces the invented one. Where no real number could be found, the article says so rather than filling the gap.

![Steam release volume, 2023-2025](charts/06_release_volume.png)

## 2. Context: A Market Defined by Oversupply

Steam's indie market operates under conditions that make failure structurally likely for the median release, independent of quality. Barriers to entry are low: a $100 Steam Direct fee (confirmed, Valve's own documentation) and free, powerful engines (Unity, Unreal, Godot) mean the pool of people who can publish a game on Steam is enormous relative to the pool of players with time and money to spend.

The result is measurable in raw volume. SteamDB, the standard third-party reference for platform-wide statistics, recorded **19,008 new game releases on Steam in 2025**, up from 18,558 in 2024 and 14,111 in 2023 — a 35% increase in two years. This is a count of listings, not an estimate; it is as close to a "confirmed" fact as this article contains.

Against that supply, Valve itself disclosed at a 2026 GDC presentation that **5,836 titles crossed $100,000 in gross lifetime revenue on Steam in 2025**, up from roughly 3,000 in 2020. That is Valve's own figure, not a third-party estimate, and it is the strongest piece of evidence in this article for both directions of the story: more games are reaching a meaningful revenue bar than five years ago, and that number is still a small fraction — well under a third — of the games released in a single year, before even accounting for the fact that some share of the 5,836 are back-catalog titles from prior years rather than 2025 releases. (An earlier version of this article cited a specific "70% back-catalog" breakdown for that figure; no source for that specific split could be located, and it has been removed rather than repeated as fact.)

## 3. Evidence: How Steam's Money Is Actually Distributed

### 3.1 Aggregate revenue and its concentration

According to a year-end 2025 report from Alinea Analytics (a third-party games-industry analytics firm, covered by Game World Observer and Notebookcheck), Steam generated approximately **$17.7 billion in total revenue in 2025** (measured January 1 through December 19), of which **independent games accounted for roughly $4.4 billion, or 25%**. This is a Tier 2/3 estimate — a reputable analytics firm's modeling, not an audited Valve financial disclosure — and should be read with that caveat, though its scale is broadly consistent with how the indie sector's growth has been discussed elsewhere in the trade press.

![A quarter of Steam's revenue](charts/02_indie_share_donut.png)

That quarter of platform revenue is itself concentrated at the top. The same Alinea Analytics report estimates the five highest-grossing independent releases of 2025 as: **Schedule I** (~$151M), **R.E.P.O.** (~$147M), **PEAK** (~$87M), **Hollow Knight: Silksong** (~$75M), and **Escape from Duckov** (~$53M) — a combined ~$513M, or roughly 12% of estimated total indie revenue, concentrated in five titles out of 19,000+ annual releases.

**A specific caveat on Silksong:** Alinea's own separate tracking reported approximately $50M in revenue in Silksong's first three days alone, and Valve's own year-end "top tier" revenue rankings placed the game alongside titles like Battlefield 6, Marvel Rivals, and Counter-Strike 2 — a group whose members typically earn revenue in the hundreds of millions. The $75M full-year estimate may understate Silksong's actual performance; it is presented here as the source's figure, not as a confirmed final number.

![Top 5 indie releases of 2025 by estimated revenue](charts/01_top5_games.png)

### 3.2 What happens below the top of the curve

The earlier version of this article presented a five-tier revenue distribution table with precise percentages (30.0% under $100, 36.0% between $100–$1,000, and so on) attributed implicitly to platform analytics. **No source for that exact table could be found**, and it has been removed. What real, sourced data does show, via Gamalytic-derived analysis reported by game-developers.org and neonlightsmedia.com, is coarser but directionally consistent: an estimated **40% of 2025 releases failed to recoup the $100 Steam Direct fee**, **65.9% earned under $1,000 lifetime**, and roughly **8% crossed $100,000 gross** — figures that should be read as a third-party analytics estimate for a partial-year 2025 cohort, not an audited count.

![Most releases never clear a break-even bar](charts/03_revenue_reality.png)

**On the reliability of these estimation tools:** Gamalytic's own published methodology states that 77% of its individual-game revenue estimates fall within a 30% margin of error, and 98% fall within a 50% margin — a claim about the tool's own accuracy, disclosed by the tool's maker, which should be read as a best-case, self-reported figure rather than independently audited. An earlier draft characterized this as tools "maintaining" 30–50% error margins in a way that implied errors typically fall in that band; the source's own framing is closer to the opposite — most estimates are tighter than that, with the 30–50% figures marking the outer edge of Gamalytic's own confidence claim.

**A claim that was removed entirely:** the earlier draft included a studio-segmentation table (a "Triple-I" tier at 50+ developers capturing 53% of indie revenue, down to "Solo/Micro" developers capturing 8%) with specific revenue shares for each tier. No source for this table could be located. "Triple-I" is a real term — it names a 2024 marketing and showcase initiative launched by studios including Evil Empire (Dead Cells), Re-Logic (Terraria), and Mega Crit (Slay the Spire) — but it is not a revenue classification with defined developer-count thresholds, and no industry report classifies large commercial successes like Game Science (Black Myth: Wukong), Pocketpair (Palworld), or Larian Studios (Baldur's Gate 3) under a formal "indie revenue tier" the way the removed table implied. This distinction matters because blending genuinely small teams with studios generating hundreds of millions in revenue, under a shared "indie" label, is one of the more common ways aggregate indie statistics mislead.

## 4. Case Studies: Production Failure Patterns

Market oversupply sets the odds. What determines which specific projects fail within those odds is, according to developer postmortems and industry practitioners, a set of recurring production patterns. The available sources document these patterns clearly; they document the patterns' *prevalence* — how often each one is the decisive factor — far less clearly. Where this section describes a mechanism, it is because postmortems describe that mechanism recurring; it is not a claim that the mechanism explains a specific percentage of failures, because no source establishes that percentage.

**Late-stage scope cuts.** Postmortem accounts frequently describe teams removing partially built systems late in development after failing to trim scope earlier — a pattern consistent with sunk-cost reasoning, though no source in this research directly measures how often sunk-cost thinking specifically (versus optimism bias, publisher pressure, or other causes) drives the delay in cutting scope. The described consequence — schedule extension, cash burn, and a rushed final months of polish — is well documented anecdotally, though this article did not locate a quantitative study establishing its frequency across the industry.

**Mid-project engine migrations.** Developer accounts describe engine swaps mid-development as high-risk, since rebuilding shader pipelines, physics logic, and tooling knowledge consumes engineering time that a small team often cannot recover before running out of capital. This is a widely repeated piece of practitioner wisdom rather than a statistically measured failure mode; the available sources document the pattern being described, not its base rate.

**Deferred external playtesting.** Marketing and design practitioners (e.g., the Steam Next Fest demo-benchmark data below) consistently argue that structural problems in a core loop are far cheaper to fix if discovered early via external playtesting than late. The claim that avoidance is driven specifically by "quality anxiety" is a plausible interpretation offered by practitioners, not a documented psychological finding about developers as a population — it is presented here as an interpretation, not a confirmed cause.

### 4.1 A quantified early-warning signal: demo playtime

One place this general pattern becomes genuinely measurable is Steam Next Fest demo performance. A HowToMarketAGame survey of 130 games across the February and October 2022 Next Fest events (62 of which went on to release) found a strong association between median demo playtime and eventual revenue tier: games in the lowest eventual revenue tier ("Bronze," under $10,000 lifetime gross) had a median demo playtime of 7 minutes; the highest tier ("Diamond," $1M+) had a median of 65 minutes, with "Silver" (18 minutes) and "Gold" (38 minutes) in between.

![Demo engagement tracks with revenue tier](charts/05_demo_playtime.png)

This is a real, specific, well-documented finding — and it is worth stating plainly what it does and doesn't show. It is an **association** from a small, self-reported 2022 survey (n=130), not a controlled experiment, and not current data. A game with a highly engaging demo and a game with strong pre-existing marketing reach and audience trust would likely produce the same pattern — players who already want the game play the demo longer *and* buy it in higher numbers — without the demo's playtime being a cause of the sales outcome at all. The available sources document the correlation; they do not establish that longer demo playtime causes higher revenue, and a competing explanation (both variables driven by a third factor — game quality, or pre-existing audience size) remains plausible and is not ruled out by this data.

## 5. Evidence: Discovery, Wishlists, and Genre

### 5.1 Steam's discovery mechanics

Two claims from the earlier draft — a "Popular Upcoming" wishlist threshold of 5,000–7,000, and a separate "~100,000 wishlists for launch popups" — turn out to describe the same evolving mechanism at two different points in time, not two separate features. The 5,000–7,000 figure is an independent analyst estimate (Chris Zukowski, a practitioner who tracks Steam's discovery algorithm closely) that predates a mid-2026 refresh of Steam's "Popular Upcoming" shelf; after that refresh, the effective bar for front-page placement reportedly rose sharply, with industry estimates (not a Valve-published number) now citing figures near 100,000 wishlists for the same kind of placement. Neither figure is a Valve-confirmed threshold; both are analyst estimates, and the article's original framing — presenting them as two distinct mechanics — has been corrected.

One pattern is better documented: Steam's Discovery Queue algorithm appears, based on consistent developer observation over several years, to exclude titles with fewer than roughly 10 paid user reviews from automated recommendation to other players. This is not a Valve-published rule, but it is a widely and consistently observed pattern among developers and marketing practitioners, which is a meaningfully stronger evidence base than a single analyst's threshold estimate.

**A claim removed for lack of support:** the earlier draft stated that "high-performing titles convert 25% or more of their pre-launch wishlists into immediate sales" versus "3–5%" for weaker launches. No source uses this percentage framing. GameDiscoverCo's actual published wishlist-conversion research (Simon Carless) measures conversion as a *multiple* of wishlist count rather than a fixed percentage of a launch-week pool — a typical game converts roughly 0.10–0.17x its wishlist total in the first week, with strong performers reaching 0.6x–5x or more, and some outliers (the game Peak, per that research, at roughly 266x) far outside that range. The percentage-based claim has been removed and replaced with this multiplier-based framing, which is the actual documented methodology.

### 5.2 Genre selection changes the odds substantially

The clearest, most rigorously sourced quantitative finding in this research is a genre-level "hit rate" table — the share of 2025 releases in a given Steam genre tag that reached 1,000 or more user reviews, used here as a proxy threshold for commercial viability. This table, compiled by Chris Zukowski using VG Insights data as of January 2026, is exact enough — down to specific sample sizes per genre — that it can be checked and was confirmed to match its cited source precisely.

![Genre choice changes the odds by 60x](charts/04_genre_hitrate.png)

Open World Survival Craft games hit the 1,000-review bar in **20.8%** of 2025 releases (15 of 72 sampled titles) — the highest rate of any tracked genre. Farming Simulation follows at **8.3%** (5 of 60), Roguelike Deckbuilder at **5.1%** (11 of 212), Management Simulation at **3.4%** (19 of 549), Horror at **3.2%** (39 of 1,208), RPG at **2.4%** (28 of 1,158), and Puzzle — the most heavily saturated genre in the sample, with 4,022 releases — at just **0.34%** (14 titles).

This is a genuinely strong piece of evidence that genre selection materially changes a project's commercial odds, independent of execution quality. It should be read with two caveats the source itself notes: genre here means a self-reported Steam tag combination, which developers sometimes apply inconsistently or optimistically, and a genre's high hit rate does not mean it is easy to execute — Open World Survival Craft games are typically expensive, systems-heavy productions, and the high hit rate may partly reflect that only well-capitalized, more experienced teams attempt the genre in the first place (a selection effect competing with a pure demand-outpacing-supply explanation).

## 6. Capital, Publishers, and Industry Contraction

### 6.1 Layoffs and closures

Industry-wide contraction since 2022 is well documented, if imprecisely quantified across trackers. A dedicated Wikipedia tracking article, aggregating primary reporting, estimates **approximately 45,000 jobs lost across the games industry between 2022 and mid-2025**, and states that **more than 30 development studios closed entirely** in that period. Different trackers (layoffs.fyi, Aftermath, GameDevReports) produce somewhat different cumulative totals depending on methodology and cutoff date, so this figure should be read as a reasonable estimate rather than a precise count, but it is directionally well supported by multiple independent trackers.

### 6.2 Publisher deal structures

**A claim removed as unsupported:** the earlier draft stated that Devolver Digital's investor disclosures showed average per-title project spending falling from $3 million (2022) to $2 million (2024), with a stated target of $1 million by 2026. Devolver Digital is a publicly traded company (LSE: DEVO) whose actual FY2025 investor presentation was checked directly. It discloses aggregate capitalized development costs ($74.7M in FY25 versus $64.8M in FY24) and an average revenue figure of $2.5M per new release — but no per-title cost trajectory matching the $3M/$2M/$1M figures in the original draft appears anywhere in the company's actual disclosures. That claim has been removed as unsupported by the primary source it implicitly cited.

What is well documented, and consistent with the general direction of the removed claim, is that publisher risk tolerance for unproven original IP has genuinely tightened since 2022 — reflected in reduced advances, a shift toward sequels and established franchises, and tighter recoupment terms — though this article did not find a source that quantifies that shift with the precision the original draft implied.

The recoupment mechanic itself — a publisher recovering both its development advance and its external marketing spend before any revenue share reaches the developer — is real and standard industry practice, documented by practitioners including designer and consultant Rami Ismail. The earlier draft's specific figure of "$200,000+" in marketing spend as the typical recoupment threshold could not be traced to any source and has been removed; marketing spend recouped this way varies enormously by title and platform, and no representative figure is available.

### 6.3 Alternative capital: Outersloth

Outersloth, an indie development fund created by Innersloth (developer of Among Us), is real and independently confirmed via Innersloth's own announcement. Its actual published terms: developers receive an advance and repay it via 50% of net revenue until the advance is recouped, after which Innersloth retains 15% of net revenue going forward (the developer keeps 85%) — a split more favorable to developers than traditional publishing norms, per Innersloth's own framing. A confirmed **seven-year sunset clause** returns full revenue and IP rights to the developer after that period. **The earlier draft's specific grant range of "$50,000 to $2,000,000" is not publicly disclosed anywhere** and has been removed as unsupported; the fund's existence and split/sunset terms are confirmed, its specific grant sizing is not.

The earlier draft's claim that "approval rates at major indie funds hover around 1%" could not be traced to any source — no fund, including Outersloth or Indie Fund, publishes an approval-rate statistic — and has been removed.

## 7. Counterarguments and Alternative Interpretations

The framing of this article, like the original draft, emphasizes structural and algorithmic causes of failure — oversupply, discovery mechanics, genre saturation. A credible competing framing deserves direct statement: **quality and execution may explain more of the variance than structural factors do, and the available data cannot cleanly separate the two.**

Consider the genre hit-rate data in Section 5.2. It is presented here as evidence that genre selection changes commercial odds independent of execution. But an equally plausible reading is that the genres with high hit rates (Open World Survival Craft, Farming Simulation) are ones where only well-resourced, experienced teams attempt entry at all — meaning the high hit rate partly reflects a *pre-existing* quality and capitalization filter, not a demand imbalance that any team could exploit by simply choosing that genre. The data as reported cannot distinguish "this genre rewards any entrant" from "this genre selects for teams that were already likely to succeed." Both explanations are consistent with the same 20.8%-versus-0.34% gap.

Similarly, the demo-playtime findings in Section 4.1 are consistent with a reverse-causal or confounded explanation: a game that already has strong word-of-mouth or an established following will likely see both longer session times *and* better eventual sales, without the demo experience itself driving the outcome.

The macro oversupply argument also has a limitation worth stating: even in a market with 19,000 annual releases, the number of titles crossing $100,000 gross (5,836, per Valve, albeit including back-catalog titles) has grown over time (from roughly 3,000 in 2020), suggesting the market is not purely zero-sum — total addressable revenue and total viable-outcome slots both appear to be expanding, even as competition intensifies. A pure oversupply narrative understates this.

Finally, on the "structural vs. execution" question broadly: this research did not find — and did not expect to find — a study that cleanly isolates the causal weight of production failures (Section 4) versus market structure (Sections 2–3, 5) versus genre/timing luck. No source in this space runs that kind of controlled comparison, and any claim to have identified the dominant cause should be treated with skepticism, including from this article.

## 8. Limitations

This article relies heavily on third-party analytics estimates (Alinea Analytics, Gamalytic, VG Insights) rather than audited platform data, because Valve discloses very little in the way of granular financial data publicly. Those estimates carry real, stated uncertainty — Gamalytic's own disclosed margin of error (30% for the large majority of estimates, up to 50% for nearly all of them) applies to individual-title figures throughout this piece, including the top-5 game revenue estimates in Section 3.1.

Several figures in this piece — the demo playtime survey (n=130, from 2022), the wishlist threshold estimates, and the genre hit-rate table — come from independent practitioner research (chiefly Chris Zukowski / HowToMarketAGame) rather than platform-disclosed or peer-reviewed data. This research is unusually rigorous and transparent about its methodology by industry standards, but it remains one analyst's tooling and sampling choices, not an independently replicated academic study.

This piece also could not verify several categories of claim common in commentary on this topic — precise publisher recoupment terms, indie fund approval rates, per-title development cost trajectories — and removed them rather than presenting unsupported specifics as fact. Readers should treat the absence of a number in this piece as a deliberate choice, not an oversight.

## 9. Conclusion

**What we know:** Steam's indie market in 2025 combined genuine, well-documented growth in top-line numbers (19,008 releases, up from 14,111 two years prior; 5,836 titles crossing $100,000 gross, up from roughly 3,000 in 2020) with continued extreme concentration of revenue at the top (an estimated five titles capturing roughly 12% of all indie revenue). Genre selection produces a large and well-documented gap in commercial hit rates — a roughly 60-fold difference between the best- and worst-performing tracked genres. Industry-wide financial contraction since 2022 (an estimated 45,000 jobs lost, 30+ studio closures) is real and well-corroborated across independent trackers.

**What we think:** The available evidence is consistent with — though does not conclusively prove — a model where structural market conditions (oversupply, algorithmic discovery gates, genre saturation) set the baseline odds of commercial failure for a given release, and production execution choices (scope discipline, engine stability, early playtesting) determine which specific titles beat or fall short of those baseline odds. Demo engagement appears to be a genuine leading indicator of commercial outcome, though the direction of causality between "good demo" and "good outcome" is not established by the available data.

**What we don't know:** No source available to this research quantifies how much of aggregate indie failure is attributable to structural market conditions versus execution failures versus genre/timing luck. The relative contribution of publisher deal-structure changes, versus broader capital contraction, to the difficulty of financing new projects is not separable in the available data. And several specific, precise-sounding statistics that circulate in commentary on this topic — a five-tier revenue breakdown, a studio-size revenue-share table, exact wishlist-conversion percentages, per-title publisher cost trajectories — could not be traced to any real source in this research and should be treated as unverified wherever they appear, including in earlier versions of this piece.

---

## Sources

- Alinea Analytics, year-end 2025 Steam report, via Game World Observer: [gameworldobserver.com](https://gameworldobserver.com/2025/12/22/indie-projects-generated-a-quarter-of-the-total-game-revenue-on-steam-by-the-end-of-2025-analytics) and Notebookcheck: [notebookcheck.net](https://www.notebookcheck.net/Indie-games-accounted-for-25-of-Steam-s-revenue-in-2025.1189429.0.html)
- SteamDB annual release counts, via KitGuru: [kitguru.net](https://www.kitguru.net/gaming/joao-silva/steam-data-shows-over-19000-games-released-in-2025/) and GamingOnLinux: [gamingonlinux.com](https://www.gamingonlinux.com/2025/12/over-19000-games-have-released-on-steam-in-2025-with-nearly-half-seeing-fewer-than-10-reviews/)
- Valve/Tom Giardino, GDC Festival of Gaming presentation, via Game Developer: [gamedeveloper.com](https://www.gamedeveloper.com/business/valve-says-5-836-titles-earned-over-100-000-on-steam-in-2025)
- Steamworks official documentation, Steam Direct fee: [partner.steamgames.com](https://partner.steamgames.com/doc/gettingstarted/appfee)
- Gamalytic-derived 2025 revenue distribution analysis: [game-developers.org](https://game-developers.org/2025-steam-game-revenue-distribution) and [neonlightsmedia.com](https://www.neonlightsmedia.com/blog/steam-game-releases-2025-fail-gamalytic-data)
- Gamalytic methodology / stated accuracy: [gamalytic.com/about](https://gamalytic.com/about)
- "Triple-I" initiative background, Game Developer: [gamedeveloper.com](https://www.gamedeveloper.com/business/indie-focused-triple-i-initiative-launched-by-dead-cells-slay-the-spire-devs)
- Chris Zukowski / HowToMarketAGame, "What the hell happened in 2025?" (genre hit-rate table), via GamesRadar+: [gamesradar.com](https://www.gamesradar.com/games/a-terrifying-20-282-games-were-released-on-steam-in-2025-and-just-608-managed-to-get-1-000-reviews-expert-finds-we-might-be-in-a-bit-of-an-indie-golden-age/)
- HowToMarketAGame, Steam Next Fest demo playtime benchmark survey: [howtomarketagame.com](https://howtomarketagame.com/2022/10/26/what-is-a-good-median-play-time-for-a-demo-benchmark/)
- HowToMarketAGame, "Why your first 10 reviews are the most important": [howtomarketagame.com](https://howtomarketagame.com/2022/01/25/why-your-first-10-reviews-are-the-most-important/)
- Steam Page Analyzer / Chris Zukowski, Popular Upcoming wishlist thresholds: [steampageanalyzer.com](https://www.steampageanalyzer.com/blog/steam-popular-upcoming-list)
- PC Guide, 2026 Steam wishlist threshold reporting: [pcguide.com](https://www.pcguide.com/news/steams-new-100000-wishlist-rule-means-many-indie-devs-will-have-to-rely-on-a-different-feature-to-be-discovered/)
- GameDiscoverCo / Simon Carless, wishlist conversion research: [newsletter.gamediscover.co](https://newsletter.gamediscover.co/p/the-state-of-steam-wishlist-conversions)
- Wikipedia, "2022–2025 video game industry layoffs" (aggregated tracking): [en.wikipedia.org](https://en.wikipedia.org/wiki/2022-2025_video_game_industry_layoffs)
- Devolver Digital FY25 Investor Presentation (primary disclosure): [investors.devolverdigital.com](https://investors.devolverdigital.com/files/downloads-and-publications/2026/devo-fy25-investor-presentation.pdf)
- Innersloth, "Outersloth: Our New Indie Game Fund!" (official announcement): [innersloth.com](https://www.innersloth.com/outersloth-our-new-indie-game-fund/)
- 80.lv, Outersloth contract terms breakdown: [80.lv](https://80.lv/articles/indie-game-fund-by-among-us-developers-reveals-its-contract)
- Rami Ismail, "Upfronts, Guarantees, Recoups" (publisher recoupment mechanics): [ltpf.ramiismail.com](https://ltpf.ramiismail.com/upfronts-guarantees-recoups/)

*Full claim-by-claim fact-check ledger available on request.*
