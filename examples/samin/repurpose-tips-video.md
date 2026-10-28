# Worked example: repurposing my "10 Opus 5.5 tips" video

This is the real `/reels` run on one of my videos. The long-form is 15 minutes. It turned into 5 reels and a list of 15 hooks for me to film.

Files from this run:
- [`repurpose-tips-video/reels.json`](repurpose-tips-video/reels.json): the plan the render tool reads
- [`repurpose-tips-video/film-hooks.md`](repurpose-tips-video/film-hooks.md): the hooks I still have to film, written for a teleprompter

## What I gave Claude

- The finished edit (`tips - edited.mp4`, 1920x1080, visuals on the left, me in a small tile on the right)
- The raw recordings from Borumi: a camera file and a mic file for each take

That's it. Claude transcribed the edit with word timestamps and read the whole thing.

## The 5 reels

| Reel | The one idea | Length | Hook in the footage | Best hook to film |
|---|---|---|---|---|
| R1 | Stop reading docs. Ask Claude for an interactive HTML page (/eli5) and click through it. | 57 s | "Next time you need to learn something, don't read the docs." | "I learned SEO without reading a single guide. Here's the one prompt." |
| R2 | Opus 5.5 as the main agent, Haiku 5.5 subagents for the cheap work. | 49 s | "So this is probably one of my favorite hacks." | "Same task. Opus alone: three minutes thirty-seven. With Haiku helpers: fifty-eight seconds." |
| R3 | Two prompts: one makes your agent work while you sleep, one hands you your decisions in the morning. | 56 s | "It's just two prompts. So one makes your agent work while you sleep." | "I wake up to new features my agent built while I slept." |
| R4 | Talk to your agent instead of typing (/voice). | 42 s | "Remember when Karpathy coined the term vibe coding?" | "You type forty words a minute. You speak two hundred fifty." |
| R5 | A 3-layer memory setup makes your agent cheaper and actually know you. | 45 s | "Your agent can burn way more tokens just to read a code base..." | "If Claude keeps forgetting what you did yesterday, this fixes it." |

Every reel has 1 hook that's already in the video and 3 hooks to film. The hooks are scored with the hooks skill (power words out of 6, plus the Four Commandments out of 4). Notice that the footage hooks often score lower. In the long video I didn't need a scroll-stopping first line for each tip. That's exactly why the tool asks me to film new ones.

## What a reel looks like

9:16, 1080x1920:
- **Top:** the proof visual from that part of the video (the tweet, the benchmark, the screen recording), zoomed to fill the space
- **Bottom:** me, from the raw camera, not the small tile, so it stays sharp
- **Middle:** captions on the seam, the current word in orange
- **First 2.5 s:** the hook's on-screen text

The tool finds the right moment in the raw camera by matching the edited audio against the raw mic files. It does this in short windows, so jump cuts are handled. All 5 reels matched the raw camera the whole way, with no fallback to the small tile.

## The loop

1. **Plan.** `/reels "tips - edited.mp4"`. Out come `reels.json`, `repurpose-plan.md` and `film-hooks.md`.
2. **Render what you have now.** `make_reel.py --all` renders each reel with its footage hook. I can post these today.
3. **Film the hooks.** I read `film-hooks.md` and record the 15 lines in one sitting (about 20 minutes). Each file is saved as `hooks-filmed/R1-H1.mov`, `R2-H1.mov` and so on.
4. **Render again.** `make_reel.py --all` now makes every reel with every hook. Same body, different first 3 seconds. Post them and see which hook wins.

## What I'd check before posting

- Watch each reel with sound. Captions match, lips match, no word cut in half.
- The top visual makes sense on its own at the start.
- The ending lands on a full sentence, then the CTA.

Back to [Chapter 8: Repurpose](../../chapters/08-repurpose/README.md).
