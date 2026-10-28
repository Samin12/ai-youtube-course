# Worked example: repurposing my "10 Opus 5.5 tips" video

This is the real `/reels` run on one of my videos. The long-form is 15 minutes. It turned into 5 reels and a list of 15 hooks for me to film. Then it became a full pack: 5 carousels, an article, text posts and a playbook, all in one folder (see the end of this page).

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

## The full finished products pack

After the reels, I ran `/carousels` and `/content-cascade`, then packaged everything with `/publish-pack`. This is the folder I post from. It has 7 numbered parts, plus a plan and a README.

| Folder | What's in it |
|---|---|
| `1 YouTube long-form/` | The 15:11 edit, 3 title ideas, the description with chapters, and the links for each tip |
| `2 Reels - Instagram, TikTok, YouTube Shorts/` | 5 reels, numbered in posting order. Each has a captions file with a section for Instagram, TikTok, Shorts and LinkedIn/X, plus the hooks still to film for it |
| `3 Hooks to film/` | `film-hooks.md`: 15 lines to record, about 20 minutes |
| `4 Carousels - Instagram, LinkedIn, TikTok/` | 5 carousels with 8 slides each: 10 Opus 5.5 tips, Steal my 2 prompts, Opus brain, Haiku hands, Your AI operating system, and 3-layer agent memory. Each has the slides, a LinkedIn PDF, `config.json` and `captions.txt` |
| `5 Articles - blog, LinkedIn, Substack/` | The blog article (about 2,300 words, Markdown and HTML), 8 images, a LinkedIn article, and a note on cross-posting to Substack and Medium |
| `6 Text posts - X, LinkedIn, Threads, newsletter/` | A 13-tweet X thread, 5 single X posts, 2 LinkedIn posts (a story and a lead magnet), 5 Threads posts, a newsletter email, and a Claude Club post |
| `7 Claude Club - Opus 5.5 playbook/` | The playbook as HTML and a 26-page PDF, plus how to post it in Skool |

`PUBLISH PLAN.md` sits at the top. It says what's in each folder, where each piece goes, which day to post it, and what to check first.

### Where each piece goes

| Piece | Goes to |
|---|---|
| Long-form | YouTube |
| All 5 reels | YouTube Shorts, Instagram Reels and TikTok, same file, same day |
| R1 (docs) and R3 (2 prompts) | Also LinkedIn, as native video. These "work smarter" ideas land with business people |
| R2 (Opus + Haiku), R3 and R4 (voice) | Also X. They have numbers or a dev angle |
| R5 (memory) | Only the short-form apps. It's the most technical one |
| Carousels | Instagram, LinkedIn (as a PDF document post) and TikTok photo mode |
| Article | My blog first, then the LinkedIn article and Substack or Medium, linking back to the blog |
| Text posts | Each on its own platform: X, LinkedIn, Threads, email, Claude Club |
| Playbook | Claude Club. It has to be live before the video goes public, because every CTA points to it |

The calendar starts on day 0: the video goes live and the playbook is up. Then one reel a day, in order: R1, R3, R2, R4, R5. The 5 single X posts run on days 1 to 5 too. The first four go with that day's reel.

Back to [Chapter 8: Repurpose](../../chapters/08-repurpose/README.md).
