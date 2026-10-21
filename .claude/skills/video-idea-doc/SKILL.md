---
name: video-idea-doc
description: Research a video idea and write a short, one-page video idea doc (topic, idea, unique angle, why it'll work, TAM analysis, title and thumbnail, spaced outline, research links, make-it-ours placeholders, sponsor). Use when the user says "make a video idea doc", "research this idea", "is this a good video idea", "make idea docs for…", or during Stage 1 (Ideation) of a video. Uses the Poppy AI MCP when connected; otherwise works from links the user pastes.
---

# Video idea doc

One short doc per video idea, so several ideas can be compared side by side in a minute. Short beats complete: every line earns its place. Example of a finished doc, copied exactly from Samin's card: `example.md` in this folder (also at `examples/samin/video-idea-doc-ai-trader.md`). Match its format and length. Blank template: `videos/_template/01-idea.md`.

## Before you start

- Read `CLAUDE.md` and `my-channel/` (about-me, viewer avatar, customer avatar, lane, offer). Every idea must fit this viewer and lead back to the offer.
- Ask one question only if you must: "What's the idea, in a sentence? Or should I find ideas for you?"

## The method (run it in this order)

1. **Copy yourself.** Pull the user's own channel, best outliers first (Poppy: `get_creator_posts` on their YouTube handle). Note their typical views and which topics beat it, and by how much. New channel? Skip and say so.
2. **Proven demand.** Search the topic on YouTube, last 12 months (Poppy: `live_search_posts`, platform youtube). Keep the outliers: videos that massively beat their channel's average.
3. **Competitors.** Note channels that show up again and again; pull their outliers too if useful.
4. **TAM of the idea.** Floor = median views of the topic's videos. Ceiling = the best one (and the user's own best on it). Expected range = user's typical views × how much this topic beat their typical before. Bad case = their typical.
5. **Demand type and wave.** Direct demand, or none (then bridge the mechanism to an outcome people already want)? Is something new launching that makes it early?
6. **Watch-outs.** Look for the same idea underperforming elsewhere (a low multiplier) and say what to avoid, usually in the packaging.
7. **Packaging.** One title in the user's proven formats, two backups, one thumbnail concept (logos, an object or place, their face, 1–3 words). Keep any sponsor's name out of the title and thumbnail.
8. **Unique angle.** What only this creator can bring: something new, a catch nobody explains, their background, their past hit (season two).
9. **Outline.** Intro, Why this matters (3 points, each with its analogy in brackets), Levels 1–3 as concrete actions the viewer does on screen, with 2–4 short points each, then CTA END pointing to their related video.
10. **Sponsor.** If the user has a deal that fits (check `my-channel/offer.md` or ask), add the payout math at the expected range.
11. **Save** to the video's `01-idea.md` (or `ideas/<slug>.md` when comparing several ideas). Show the user the doc.

With Poppy connected, add the outliers to their Poppy board in an "Outliers" group as you go, so they can see the evidence.

## The doc format (keep it this short)

```
# Idea doc: <working title>

- **Topic:** …
- **Idea:** one or two sentences
- **Unique angle**
  - 3–6 short bullets

- **Why it'll work:** one line: own proof, outside outliers, the wave
- **TAM analysis**
  - Floor: … (median of N videos, last 12 months)
  - Ceiling: … · my own: …
  - My typical video: … · this topic did …x–…x that
  - My expected range: … · bad case …
  - Watch out: … (only if there is one)

- **Title:** "…"
  - Backups: "…" · "…"
- **Thumbnail:** …

- **Outline**
  - **Intro** (hook · proof · 3 levels)
  - **Why this matters** (3 points, analogy in brackets)
  - **Level 1: <action>** (2–4 points)
  - **Level 2: <action>**
  - **Level 3: <action>**
  - **CTA END:** …

- **Research links**
  - linked titles with view counts: the user's own, then the best outside outliers, then the one to beat

- **Make it ours:** [placeholders only the user can fill]
- **Sponsor:** … (payout at the expected range)
```

## Rules

- Real numbers only, from the searches. Round them (419K, 1.8M). Never invent views, results, prices or quotes.
- Anything only the user knows goes in `[brackets]`.
- Facts that change a viewer's decision (setup steps, prices, limits): mark `[verify]` unless you checked a current source.
- Every research link is a real URL from the search results.
- Making several ideas? One doc each, same format, so they're easy to compare.
