# Chapter 7: Edit

**Stage 6 of 8:** Ideation → Research → Packaging → Outline + script → Film → **Edit** → Repurpose → Publish

## Why this matters

Raw footage isn't a video yet. Editing is where we keep people watching and back up every claim on screen. But know its limits: "Editing can remove friction… but it cannot rescue a weak idea." *(Jake Trinder)*

## What you'll learn

- **Proof-based editing.** Every claim gets proof on screen: the tweet, the chart, the result, the screenshot. "If a visual does not clarify, prove, or help the viewer follow the video… it's just movement." *(Jake Trinder)*
- **The edit matches the packaging.** A raw promise needs a raw edit. *(Jake Trinder)*
- **Less is more: the anti-edit.** Ed Lawrence dropped stock footage, heavy b-roll (extra footage cut over you talking), music, sound effects and zooms, and got more comments, leads and sales. Cut mistakes and pauses, then cut every line that doesn't change anything. Punch-ins (quick zooms) only for emphasis, at the end of a sentence. *(Ed Lawrence)*
- **On-screen text does most of the work.** Step numbers, key points beside you, full-frame diagrams. Show the problem physically, then build the solution on screen. *(Ed Lawrence)*
- **Pacing.** Cut where you get bored; rewatch and cut any second that doesn't add value. Pacing is momentum and rhythm, not cramming in cuts. *(Jon Dorman)* Put your best visual work in the intro. *(Aprilynne Alter)*
- **Three AI words you need:**
  - **Skills:** saved instructions an AI follows for one job.
  - **MCPs:** let the AI use your apps directly.
  - **Connectors:** plug the AI into your accounts and files.
- **The AI edit.** Claude Opus plus an editing skill can do the tight cut, proof visuals, captions, chapters and cleaned-up audio. Borumi has an MCP, so the AI can open and edit the project directly. You keep the style and the decisions; AI does the execution.
- **"Isn't AI editing bad?"** Some creators say it isn't good enough yet. *(Nate Curtiss)* It is when you give it a clear skill and check its work. That's why you learned the theory first.

## What you'll build

[`videos/<your-video>/06-edit-notes.md`](../../videos/_template/06-edit-notes.md): your claim → proof map, cut notes, and chapters. The map format, with an example, is in [`templates/claim-proof-map.md`](templates/claim-proof-map.md).

## Steps

1. **Map your proof.** Run [`prompts/claim-proof-map.md`](prompts/claim-proof-map.md) on your script. Every claim gets a piece of proof.
2. **Gather the proof:** screenshots, charts, results, tweets.
3. **Find the cuts.** Get a transcript of your raw recording and run [`prompts/tighten-cut.md`](prompts/tighten-cut.md).
4. **Edit.** Any editor works: cut tight, add the proof and on-screen text, captions, chapters, clean audio.
5. **Review.** Watch it once with no sound, then once as your viewer. Fix anything that drags.

**How I do it:** two passes with Claude, through Borumi's MCP: **the cut first, then visualize.** You never design a visual for a line you're about to cut.

## My editing skills

1. **The cut and the visuals: the `borumi` plugin** ([Samin12/opencutagent-borumi](https://github.com/Samin12/opencutagent-borumi)). It removes silences, ums and retakes, cuts ranges, adds chapter cards and captions, and visualizes a scene with a rendered animation behind or in front of your camera. Built on [OpenCutAgent](https://github.com/leonardogrig/opencutagent) by Leonardo Grigorio.
   - **Install:** open this course in Claude Code and say yes when it offers the plugin. Or run:
     ```bash
     claude plugin marketplace add Samin12/ai-youtube-course
     claude plugin install borumi@ai-youtube-course
     ```
   - **Use:** open your project in Borumi, then `/borumi:setup` once, then `/borumi:silences`, `/borumi:retakes`, and `/borumi:visualize scene 1`.
2. **The proof-first intro: `visualize-a-cam-intros`** ([in this course](../../.claude/skills/visualize-a-cam-intros)). It turns your talking-head intro into a proof-first visual story: you stay pinned on top, every sentence gets real proof on screen, and a critic round checks it before you see it.
   - **Install:** nothing to do. It's in this course's `.claude/skills/` folder.
   - **Use:** open your project in Borumi, then `/visualize-a-cam-intros` and say which scene is your intro.

**Want a different look?** Just tell Claude: "make it light mode," "use my brand colors," "put my face on the right." The skills are a starting point, not a template you're stuck with.

## Check it

- [ ] Does every claim have proof on screen?
- [ ] Watch it with no sound: can you still follow it? *(Aprilynne Alter)*
- [ ] Does the edit match the promise of the title and thumbnail?
- [ ] Did you cut every line that doesn't change anything?

## Tips

- **Turn off YouTube's automatic chapters** and make your own. *(Nate Curtiss, Marcus Jones)*
- **Learn your own style** before you hand editing off. *(Aprilynne Alter)*
- **After posting, check the retention graph** (the chart of how many people are still watching at each moment). A dip points to a script, filming or edit problem. *(Nate Curtiss)*

## Status

**Coming soon.** Outline ready: the concepts, prompts, template and my editing skills work now. The full walkthrough is coming.

Next: [Chapter 8: Repurpose](../08-repurpose/README.md).
