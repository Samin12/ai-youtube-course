---
name: video-outline
description: Turn a video's idea doc and package into a one-page outline (the one-pager). It writes the promise first, then the Intro, Why this matters, Levels 1–3 and CTA, where every point gets an analogy or example and, when it's shown on screen, step-by-step moves. Use when the user says "outline this", "make the outline", "make the one-pager", "plan the video", "write the outline for my video", or at the start of Stage 4 (Script). Also folds the user's notes into an outline they paste back.
---

# Video outline (the one-pager)

The outline is where a video gets its structure. People learn when they can follow, so every video uses the same shape: Hook → Setup → Why this matters → Level 1 → Level 2 → Level 3 → CTA, with a transition between each part. Example of a finished one-pager: `example.md` in this folder (also at `examples/samin/video-one-pager-ai-trader.md`). Match its format and length. Another real one, the outline behind Samin's 1.8M video: `examples/samin/video-one-pager-stock-market.md`. Diagrams: `chapters/05-script/images/`. Blank template: `videos/_template/04-script.md`.

## Before you start

- Read `CLAUDE.md` and `my-channel/` (viewer avatar, offer, brand voice).
- Read the video's `01-idea.md` (its draft outline, unique angle and research links), `02-research.md` and `03-packaging.md`.
- **No package yet? Stop.** Say: "Let's do the title and thumbnail first (Chapter 4). The outline keeps the package's promise, so the package comes first."
- Ask one question only if you must.

## The method (run it in this order)

1. **Write the promise.** The title and thumbnail together make one promise. Write it in one sentence, in the viewer's words. Then fill in:
   - **Format:** what the package sets up: a tutorial, an experiment or story ("I tested it"), an explainer, a list.
   - **Circle:** who the package reaches. Package for the whole circle: the broader it is, the more people click.
   - **Slice:** the one specific thing this video goes deep on.
   - **The video must show:** what has to be on screen for the promise to be kept. (These are the acceptance criteria: what has to be true by the end for the title to be true. *Jake Trinder*)
   - **What breaks the promise:** e.g. a so-so result under "it's insane", paper money under "I gave Claude a trading account", or the payoff shows up too late.
   - Testing several packages? Don't write a promise per package. Find what they all share and write one broad promise that's true for every one of them. The hook keeps it, so whichever package wins the test, the viewer lands in the right place.
2. **Map the levels of awareness.** Who's inside the circle: never heard of it → heard of it, never tried it → tried it, got stuck → uses it, wants more. The less aware groups are the biggest. So the levels go easy to hard: Level 1 is a quick win for beginners, Level 2 goes further, Level 3 is the advanced payoff. Everyone stays.
3. **Intro.** Hook: keeps the promise in the first 30 seconds and hits every part of it (first line = the title, first shot = the thumbnail). Proof: one line. Setup: "3 levels: …", the route.
4. **Why this matters.** 3 points, before any how-to. Each point is a bold one-liner plus its analogy or story. No demos here.
5. **Levels 1–3.** Each level is something concrete the viewer does. 2–5 points per level. Every point is built the same way:
   - a bold one-liner (the point)
   - **Example / story analogy:** lead with it. One per point, never two. Skip it when the point is already clear.
   - **Step by step (screenshare):** only when it's shown on screen.
   - Proof the viewer will see (a screenshot, a result, a number) goes inside the example or the steps. Unknown? `[brackets]`.
   - End each section with a **→ Transition:** line that pays off this part and sets up the next.
6. **Remind, don't just teach.** Repeat the basics the viewer needs (setup steps, core terms, a proven analogy) even if an older video covered them. Most viewers haven't seen it, and the rest forgot.
7. **CTA (end).** Point to one next video: what they can do now → the problem that's still left → the video that fixes it. No "and finally."
8. **Key things to create.** List every demo, prompt, asset and proof shot the outline needs.
9. **Save** it in the video's `04-script.md` under "Outline (one-pager)". Show the user.

## The format (keep it this short)

```
# Video one-pager: <working title>

**Package:** "<title>" · thumbnail: <text · elements> (testing several? list each one)
**The promise:** "<one sentence, in the viewer's words, true for every package>"
**Format:** … · **Circle:** … · **Slice:** …
**The video must show:** …
**What breaks the promise:** …

**Video idea:** …
**Goal of video:** who walks away able to do what
**Key things to create:**
- …

## Intro
- Hook: …
- Proof: …
- Setup: 3 levels: (1) … (2) … (3) …

## Why this matters
- **Point 1: <one-liner>**
  - Example / story analogy: …
- **Point 2 …** / **Point 3 …**
→ Transition: …

## Level 1: <action> (beginners: a quick win)
- **Point 1: <one-liner>**
  - Example / story analogy: …
  - Step by step (screenshare): …
→ Transition: …

## Level 2: <action> (go further)
## Level 3: <action> (the big payoff)

## CTA (end)
- Watch this next: …
```

## When the user sends notes

They'll often paste the outline back with notes inside it.

- Every note goes in, in their words.
- Deleted stays deleted. If they cut an example, a point or a section, it doesn't come back.
- Put their notes in a logical order, but keep everything they said.
- Leave what they didn't touch alone.
- Return only the outline.

## After the outline: what to script

- **Word for word:** the hook and the intro.
- **Bullets:** everything else, straight from the outline.
- **Demos:** don't script them. Talk through them on screen.
- Then read it out loud and cut what you don't need.

## Rules

- Planning voice: written before filming, with no results from after the fact.
- Never invent results, numbers, costs or quotes. Anything only the user knows goes in `[brackets]`. Facts that change a viewer's decision (setup steps, prices, limits): mark `[verify]` unless you checked a current source.
- One page. Every line earns its place.
- Plain words and short lines, in the user's voice (`my-channel/brand-voice.md`).
