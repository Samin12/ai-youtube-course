---
name: new-video
description: Start, continue or list YouTube video projects in this course folder. Use when the user says "make a new video", "new video", "start a video", "start my first video", "continue my video", "next stage", or "show my videos". Creates a numbered project folder in videos/ from videos/_template/, fills in the brief from my-channel/, shows the 8-stage plan, and runs each stage with the matching chapter.
---

# New video

This course folder is the user's content operating system. Every video gets its own folder in `videos/`, and every stage saves into it. Keep messages short and plain, and ask one question at a time.

## "Make a new video"

1. **Check the foundation.** Read `CLAUDE.md`, `my-channel/about-me.md`, `my-channel/viewer-avatar.md`, `my-channel/offer.md` and `my-channel/lane.md`. If they're still blank templates (full of [brackets]), say so in one line and offer to run onboarding first (`ONBOARDING.md`). Don't make a video without knowing who it's for.
2. **Ask one question:** "What's this video about? A rough idea is fine. Or say 'help me find one' and we'll start with Ideation."
3. **Make the folder.**
   - Number: look in `videos/` for folders named like `001-...`. Use the next number, starting at `001`.
   - Name: a short slug from the working title (lowercase, hyphens, up to 5 words), like `001-ai-agents-for-solopreneurs`. No idea yet? Use `001-untitled`, and rename the folder once Ideation picks the idea.
   - Copy everything in `videos/_template/` into it (including the empty `assets/` and `exports/` folders).
4. **Fill in the brief** in the new folder's `README.md`: replace `[Working title]` in the heading, and fill in the working title, today's date, who it's for, the problem it solves (in the viewer's words where you have them), the lane topic it fits, and how it leads to their offer. Pull everything from `my-channel/`. Leave anything unknown in [brackets], and never invent facts.
5. **Point CLAUDE.md at it.** In the "What I'm working on" section of `CLAUDE.md`, set the current video to the new folder's path.
6. **Kick it off** with a short message in this shape:

   > **Here's our new video.**
   > - **Working title:** ...
   > - **Who it's for:** ...
   > - **The problem it solves:** ...
   > - **How it leads to your offer:** ...
   > - **Folder:** `videos/001-.../`
   >
   > **Here's what we're going to do:** Ideation → Research → Packaging → Script → Film → Edit → Repurpose → Publish. Each stage saves into this folder.
   >
   > **First up: Ideation.**

7. **Start Stage 1.** Follow `chapters/02-ideation/README.md` and its prompts, using their `CLAUDE.md` and `my-channel/` files. Save the result in the video's `01-idea.md`. If they already have a firm idea, check it against their viewer and lane instead, and save it.

## Running each stage

- Each stage has a guide in `chapters/` (listed in the video's `README.md`). Read that chapter's `README.md` and use its prompts and templates.
- Save the stage's work in the matching file in the video folder.
- When a stage is done, tick its box in the video's `README.md`, say what's next in one line, and ask if they want to keep going.
- If a chapter says "build coming soon", still use its concepts, prompts and templates. They work today.
- Raw footage goes in `assets/`, and the finished video, thumbnails and shorts go in `exports/`.

## "Continue my video"

1. Find the current video: the path in `CLAUDE.md` under "What I'm working on", or else the highest-numbered folder in `videos/`.
2. Read its `README.md`, find the first unticked stage, and say: "We're on [video title], Stage [n]: [stage]. Let's go."
3. Run that stage as above.

## "Show my videos"

List every folder in `videos/` (skip `_template`) with its working title and how many of the 8 stages are ticked, and mark the current one.
