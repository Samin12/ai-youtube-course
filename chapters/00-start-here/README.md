# Chapter 0: Start here

**Time:** about 15 minutes.

## Why this matters

This chapter shows you how the course works and gets your tools ready. Once it's done, every other chapter is just "open the folder, follow the steps."

## What you'll learn

- **Concepts first, then a real video.** For each stage, you learn the concepts, tips and things to watch out for. Then we build one real video together, start to finish. *(The course video: [Samin to fill])*
- **The self-driving car.** The car does most of the driving, but you're still in the driver's seat, and you still need to know how to drive so you can grab the wheel. AI is the same. You learn how each stage works so you can judge what the AI gives you.
- **Tools change, concepts don't.** Tools change every month. If something breaks or updates, you'll know how to rebuild it.
- **My process.** Know your viewer. Know your business and your offer. Then pick ideas your viewer wants that also lead back to your offer.
- **The 8 stages.** Every video goes through the same stages: Ideation → Research → Packaging → Outline + script → Film → Edit → Repurpose → Publish. Then we turn views into customers (Funnel) and put it all on autopilot.
- **Every chapter has the same shape.** Why it matters → concepts → do it → check it → tips.
- **Model vs. harness.** The model is the engine: the part that thinks and writes (like Claude Opus, GPT or Gemini). The harness is the car built around it: the app you use (the Claude app, ChatGPT, Claude Code). The harness decides whether the AI can read your files and remember you.
- **Web vs. desktop.** The web version of Claude is great for chatting, with nothing to install. The desktop app can open the course folder on your computer, so that's what we use.
- **CLAUDE.md.** Think about your first day at a new job. Your boss hands you a doc that says who the company is, who the customers are, and how things get done. `CLAUDE.md` is that doc for your AI. Claude reads it every time.

## What you'll build

- This repo on your computer
- The Claude desktop app, installed
- Your onboarding, started: Claude fills in [`CLAUDE.md`](../../CLAUDE.md) as it interviews you

## Steps

1. **Get the repo.** On the GitHub page, click the green **Code** button, then **Download ZIP**. Unzip it somewhere easy, like your Desktop. (Using Git? `git clone https://github.com/Samin12/ai-youtube-course.git`)
2. **Install Claude.** Download the Claude desktop app from [claude.ai/download](https://claude.ai/download) and sign in. Any AI tool works for this course. I use Claude with the Claude Opus model.
3. **Paste the onboarding prompt.** Open the **Code** tab in the desktop app, pick the course folder, and paste the prompt from the [main README](../../README.md#start-here-copy-this-prompt). Claude checks your setup, then starts Chapter 1 with you, one question at a time. (Using a normal chat or another AI? Copy [`ONBOARDING.md`](../../ONBOARDING.md) into a new chat instead.)
4. **Optional: test it.** In a new chat in the course folder, paste the prompt in [`prompts/check-my-setup.md`](prompts/check-my-setup.md). Claude should already know who you are.
5. **Look around.** Open `chapters/`, `my-channel/` and `videos/` so you know where things live.

## How this repo is laid out

- `chapters/`: what to learn and do, one folder per chapter.
- `my-channel/`: files about you and your channel. You fill these in once.
- `videos/`: one folder per video, made for you when you say "make a new video". Each has a brief and one file per stage.
- `examples/samin/`: my filled-in versions, so you can see what "done" looks like.
- `.claude/skills/`: saved instructions Claude Code can run for you, like `/viewer-avatar`.

## Check it

- [ ] You pasted the onboarding prompt, and Claude started interviewing you.
- [ ] Claude can tell you your name and what you do, without you typing it again.
- [ ] You can find `chapters/`, `my-channel/` and `videos/`.
- [ ] You can see the hidden `.claude` folder (see Tips).

## Tips

- **Can't see `.claude`?** Folders that start with a dot are hidden. Mac: press **Cmd + Shift + .** in Finder. Windows: **View > Hidden items** in File Explorer.
- **Not technical?** You don't need to be. If you can copy and paste, you can do this.
- **Go in order.** Every chapter builds on the one before it.

## Status

**Step ready.** Next: [Chapter 1: Foundation](../01-foundation/README.md).
