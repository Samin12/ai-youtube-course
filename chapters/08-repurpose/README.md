# Chapter 8: Repurpose

**Stage 7 of 8:** Ideation → Research → Packaging → Outline + script → Film → Edit → **Repurpose** → Publish

## Why this matters

The video's done. The ideas inside it can become posts and reels. Use the finished edit so each piece matches what you actually said and showed.

## What you'll learn

- **Reuse what you made.** You make the video once. Repurposing brings its ideas to people who may not watch the full video.
- **Every post is another touchpoint.** Remember the 7-11-4 rule of thumb from the start of the course: before someone buys, they need about 7 hours with you, 11 touchpoints, in 4 different places. *(It's often credited to Google, but there's no published study, so treat it as a rule of thumb.)*
- **What one video turns into.** Shorts and Reels (clips of the best moments), short-form scripts, X/Twitter threads, carousels for Instagram and LinkedIn, and a newsletter or email.
- **How AI finds the pieces.** Claude Opus reads the finished video's transcript and finds the separate ideas inside it. `/content-cascade` turns the video into a blog post, an X/Twitter thread, and LinkedIn posts. `/reels` plans and renders short clips with hooks you can test. `/carousels` turns the best ideas into slides people save. `/publish-pack` puts it all in one folder with a plan.
- **Short-form amplifies long-form.** It doesn't replace it.

## What you'll build

[`videos/<your-video>/07-repurpose.md`](../../videos/_template/07-repurpose.md): your post drafts, reel plan, hooks to film, and checked render files.

And one `finished/` folder for the video. It has 7 numbered parts: the long-form, reels, hooks to film, carousels, articles, text posts, and your lead magnet. Each reel and carousel has a captions file for each platform. `PUBLISH PLAN.md` says where each piece goes and on which day. You'll follow it in Publish.

## My repurpose skills

I use the [Content Repurpose System](https://github.com/AI-Answer/ContentRepurposeSystem) plugin. It is included and enabled with the course's Claude Code setup. If it is missing from your session, install it in Claude Code:

```text
/plugin marketplace add AI-Answer/ContentRepurposeSystem
/plugin install content-repurpose-system@samin-content-marketplace
```

Restart Claude Code after installing. `/content-cascade` makes the blog, thread, and LinkedIn drafts. `/reels` handles the reel loop: plan → film the hooks it asks for → render. `/carousels` makes slide posts for Instagram, LinkedIn, and TikTok. `/publish-pack` packs everything into one folder you can post from.

Reel rendering needs FFmpeg, `whisper-cli`, Python 3, NumPy, and Pillow. On a Mac, install the video tools with `brew install ffmpeg whisper-cpp`. Install the Python packages with `python3 -m pip install numpy Pillow`, in a virtual environment if needed. Whisper also needs a local model file. The plugin's README has the full setup.

## Steps

1. **Use the finished video.** Give Claude the local edit or its YouTube URL. Keep the raw camera and matching mic files nearby for reels.
2. **Make the posts.** Run `/content-cascade <YouTube URL>` for a blog post, an X/Twitter thread, and LinkedIn drafts. Read them and fix anything that doesn't sound like you.
3. **Plan the reels.** Run `/reels <video path or YouTube URL>`. Claude uses word timestamps to pick 3-6 ideas. It saves `work/reels.json`, `repurpose-plan.md`, and `film-hooks.md`. Each reel has one hook from the footage and three new hooks to film.
4. **Hooks to film.** Read `film-hooks.md`. Record each line, at most 15 words and 4 seconds. Use the same outfit and light as the long-form. Record one take per line, with a 1 second pause before and after. Save each as `hooks-filmed/<reelId>-<hookId>.mov`. Then say "attach my filmed hooks."
5. **Render the reels.** Ask `/reels` to render all available hook variants. You get 9:16 reels with visuals on top, you on the bottom, and captions on the seam. Each variant keeps the same body and changes the hook. Missing filmed hooks can be added later.
6. **Make the carousels.** Run `/carousels`. Claude picks 1-5 ideas people would save: a list, prompts to copy, a framework. Each one gets 6-10 slides that look like posts on X, with a frame from your video on the cover and real proof on the other slides. You get PNG slides, a PDF for LinkedIn, and captions. Open every slide and check that nothing is cut off. The first time, Claude asks for the name, handle, and photo to show on the slides.
7. **Check and save.** Watch every render with sound. Check captions, camera sync, framing, and volume. Save the post drafts and reel file paths in `videos/<your-video>/07-repurpose.md`.
8. **Package it.** Say "make the finished products folder" or run `/publish-pack`. Claude copies every piece into `finished/`, numbered in posting order. It writes a captions file per platform for each reel and carousel, and a `PUBLISH PLAN.md`: what's here, where each piece goes, a day-by-day calendar, and a checklist. Then follow `PUBLISH PLAN.md` in [Chapter 9](../09-publish/README.md).

**Using another AI tool?** The prompts still work: start with [`find-the-ideas.md`](prompts/find-the-ideas.md), then [`make-the-posts.md`](prompts/make-the-posts.md). The plugin's render tools run locally through Claude Code.

Worked example: [the tips video](../../examples/samin/repurpose-tips-video.md)

## Check it

- [ ] Does each piece stand on its own, without the video?
- [ ] Does each one point back to the main video or your offer?
- [ ] Does it still sound like you?
- [ ] Did you watch every reel with sound and check captions, sync, and volume?
- [ ] Are missing filmed hooks marked in the reel table?
- [ ] Did you open every carousel slide and check nothing is cut off?
- [ ] Is everything in `finished/`, with captions files and a `PUBLISH PLAN.md`?

## Tips

- **Short-form amplifies long-form;** it doesn't replace it.
- **Pick one long-form and one short-form platform first,** so you don't spread yourself too thin. *(Ed Lawrence, Taki Moore)*
- **Test the hook.** Keep the reel body the same and compare different openings.

## Status

**Plugin workflow ready.** The course includes Content Repurpose System. Use `/content-cascade` for post drafts, `/reels` for the plan, filmed hooks, and vertical renders, `/carousels` for slide posts, and `/publish-pack` for the finished folder and its plan.

Next: [Chapter 9: Publish](../09-publish/README.md).
