---
name: video-outline
description: Build a video's one-page outline (the one-pager) with the user, as a session. Checks the idea doc and package, interviews them (one question at a time, or all at once by voice) to get their brain dump, organizes it in their words into 02-research.md and their Poppy board, then writes the one-pager (promise first, then Intro, Why this matters, Levels 1–3 and CTA) in the exact format of example.md and puts it on the board too. Use when the user says "outline this", "make the outline", "make the one-pager", "plan the video", "brain dump my video", "write the outline for my video", or at the start of Stage 4 (Script). Also folds the user's notes into an outline they paste back.
---

# Video outline (the one-pager)

The outline is where a video gets its structure. People learn when they can follow, so every video uses the same shape: Hook → Setup → Why this matters → Level 1 → Level 2 → Level 3 → CTA, with a transition between each part. The one-pager you make must look like `example.md` in this folder (also at `examples/samin/video-one-pager-ai-trader.md`): same fields, same order, same length. Another real one, the outline behind Samin's 1.8M video: `examples/samin/video-one-pager-stock-market.md`. Diagrams: `chapters/05-script/images/`. Blank template: `videos/_template/04-script.md`.

Run it as a session. Keep messages short and plain, and ask one question at a time.

## Step 0: Check the basics

- Read `CLAUDE.md` and `my-channel/` (viewer avatar, offer, brand voice).
- Find the current video: the path in `CLAUDE.md` under "What I'm working on", or the highest-numbered folder in `videos/`. Read its `01-idea.md`, `02-research.md` and `03-packaging.md`.
- **Can't find the video's context there?** Ask where it is, in one question: "Where's the context for this video: a folder here, your Poppy board, a doc or card, or do you want to paste it?" Read whatever they point to: the idea doc, research, outliers, and the title and thumbnail.
- **Still no title and thumbnail anywhere? Stop.** Say: "Let's do the title and thumbnail first (Chapter 4). The outline keeps the package's promise, so the package comes first."
- **Poppy connected?** Find the board for this video (`list_boards`, then `list_board_nodes`: the board with its idea doc or outliers). If it's unclear which board, ask. The brain dump and the one-pager go there too.
- Tell them in 3 short lines what you found (the video, the package, what's missing), then: "First I need your special sauce: the stuff only you know."

## Step 1: Get the brain dump (their special sauce)

The brain dump is what only they have: their stories, results, opinions, mistakes, and what their clients ask. Without it, the outline sounds like every other video on the topic.

Already have one in `02-research.md`? Show it in 3 bullets, ask "Anything to add?", and go to Step 2.

Otherwise, offer two ways:

> 1. **One by one:** I'll ask you each question, and you answer.
> 2. **All at once:** you see all the questions, then talk through everything in one go. Voice works best for this.

The questions, in this order. Skip any the idea doc already answers: say what you found, and ask them to confirm.

1. Why do you care about this video, and why now?
2. What did you build, try or test, and what happened? Any results, numbers or screenshots?
3. What in your background makes you the person to teach this? (a job, a client, a story)
4. What's the catch, or the thing people get wrong, that nobody explains?
5. What will you show on screen? Walk me through the demos in order.
6. What stories, examples or analogies do you already use when you explain this?
7. What do your clients, your community or your comments keep asking about it?
8. Who is this one for, and where are they stuck before they watch?
9. Which of your videos should they watch next?

**All at once:** show the list, then tell them how, in a few short lines: use the microphone button in Claude or built-in dictation (Mac: press Fn/🌐 twice; Windows: Windows key + H), or record a voice memo and paste the transcript. Any order, messy is fine, more is better. Paste client calls, DMs or comments too. Wait until they say they're done.

## Step 2: Organize it, in their words

Sort everything into these headings. Quote their exact phrases. Don't add research or new ideas.

- **My main points**
- **My stories and examples**
- **My opinions** (especially any that go against the usual advice)
- **Proof I have** (results, numbers, screenshots)
- **What I'll show on screen** (the demos, in order)
- **Questions I raised but didn't answer**

Then:

- Save it under "My brain dump" in the video's `02-research.md`.
- **Poppy connected:** add it to their board as a note titled "Brain dump: <working title>", in a new group "<video> · Brain dump + outline" next to the idea doc (`add_to_board` with `group_title`). If the board has a chat for this video, connect the group to it (`connect_to_chat`).
- Show it to them in a few bullets per heading, and ask: "Anything wrong or missing?" Fix it.
- If the outline still needs something only they know (a proof line, a result, the next video), ask for just that, one question at a time. Still unknown? It goes in `[brackets]`.

## Step 3: Write the one-pager

1. **Write the promise.** The title and thumbnail together make one promise. Write it in one sentence, in the viewer's words. Then fill in:
   - **Format:** what the package sets up: a tutorial, an experiment or story ("I tested it"), an explainer, a list.
   - **Circle:** who the package reaches. Package for the whole circle: the broader it is, the more people click.
   - **Slice:** the one specific thing this video goes deep on.
   - **The video must show:** what has to be on screen for the promise to be kept. (These are the acceptance criteria: what has to be true by the end for the title to be true. *Jake Trinder*)
   - **What breaks the promise:** e.g. a so-so result under "it's insane", paper money under "I gave Claude a trading account", or the payoff shows up too late.
   - Testing several packages? Don't write a promise per package. Find what they all share and write one broad promise that's true for every one of them. The hook keeps it, so whichever package wins the test, the viewer lands in the right place.
2. **Map the levels of awareness.** Who's inside the circle: never heard of it → heard of it, never tried it → tried it, got stuck → uses it, wants more. The less aware groups are the biggest. So the levels go easy to hard: Level 1 is a quick win for beginners, Level 2 goes further, Level 3 is the advanced payoff. Everyone stays.
3. **Intro.** Hook: keeps the promise in the first 30 seconds and hits every part of it (first line = the title, first shot = the thumbnail). Proof: one line, from their brain dump. Setup: "3 levels: …", the route.
4. **Why this matters.** 3 points, before any how-to. Each point is a bold one-liner plus its analogy or story. No demos here.
5. **Levels 1–3.** Each level is something concrete the viewer does, in the order of the demos they described. 2–5 points per level. Every point is built the same way:
   - a bold one-liner (the point)
   - **Example / story analogy:** lead with it. Use their own stories and results from the brain dump first; only invent an analogy when they have none. One per point, never two. Skip it when the point is already clear.
   - **Step by step (screenshare):** only when it's shown on screen.
   - Proof the viewer will see (a screenshot, a result, a number) goes inside the example or the steps. Unknown? `[brackets]`.
   - End each section with a **→ Transition:** line that pays off this part and sets up the next.
6. **Remind, don't just teach.** Repeat the basics the viewer needs (setup steps, core terms, a proven analogy) even if an older video covered them. Most viewers haven't seen it, and the rest forgot.
7. **CTA (end).** Point to one next video (their answer to question 9): what they can do now → the problem that's still left → the video that fixes it. No "and finally."
8. **Key things to create.** List every demo, prompt, asset and proof shot the outline needs.

## Step 4: Save it and show it

- Save it in the video's `04-script.md` under "Outline (one-pager)".
- **Poppy connected:** add it to the same group on their board as a note titled "One-pager: <working title>".
- Show them the one-pager, then one line: "Send me notes right inside it, and I'll fold them in."

## The format (match example.md exactly)

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
- Save it to `04-script.md`, and with Poppy connected, update the "One-pager" note on their board (`write_note`, replace).
- Return only the outline.

## After the outline: what to script

- **Word for word:** the hook and the intro.
- **Bullets:** everything else, straight from the outline.
- **Demos:** don't script them. Talk through them on screen.
- Then read it out loud and cut what you don't need.

## Rules

- Planning voice: written before filming, with no results from after the fact.
- Never invent results, numbers, costs or quotes. Anything only the user knows goes in `[brackets]`. Facts that change a viewer's decision (setup steps, prices, limits): mark `[verify]` unless you checked a current source.
- Their stories and words come first. Invent an analogy only where the brain dump has none.
- One page. Every line earns its place.
- Plain words and short lines, in the user's voice (`my-channel/brand-voice.md`).
