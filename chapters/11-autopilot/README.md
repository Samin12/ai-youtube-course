# Chapter 11: Autopilot

**The finale.** You've done every stage by hand. Now we put it on autopilot.

## Why this matters

Because you did every stage by hand, you know what good looks like, and you'll know when the AI gets it wrong. Remember the self-driving car: now the car does most of the driving, and you stay in the driver's seat. Agents give you a head start, not the final say.

## What you'll learn

- **Skills.** A saved set of instructions an agent follows for one job, like an ideation skill or a repurpose skill. You wrote most of them already, just by doing each stage by hand. (This repo's `/viewer-avatar` is one.)
- **Scheduled tasks.** Agents that run on a timer, like "every morning, find new outliers in my niche."
- **MCPs and connectors.** How agents reach your tools, like Poppy, Borumi and Blotato. (We met these in the Edit chapter.)
- **The board is the system.** Staying organized is what makes it run. Every video is one card moving left to right.
- **The pipeline board (Multica).** One column per stage: Ideation → Research → Packaging → Outline + script → Film → Edit → Repurpose → Publish. Drag a card to the next column, and that stage's agent picks it up.
- **The capture system.** Record a voice note anywhere, and it lands on the board as an idea card. Agents refine each idea against your viewer avatar and offer.
- **Ideas on autopilot.** A scheduled task finds outliers in your niche and nearby niches. Ideas get scored against your avatar and offer, so you only see the good ones.
- **From idea to film-ready.** Idea → research brief → outline → script. You review each step, using the "Check it" list from each chapter. Film from the script, or straight from the outline.
- **After you film.** An edit agent does the proof-based edit through Borumi's MCP. A repurpose agent makes scripts, tweets and carousels. Publishing is scheduled in Blotato.

## What you'll build

- **Now:** your first skill, made from one stage you've already done by hand.
- **Coming soon:** the starter autopilot setup you can copy. *[Samin to decide: the simple version, e.g. one board + 2–3 skills + one scheduled task]*

## Steps

1. **Pick one stage** you've done by hand at least once. Ideation is a good first one.
2. **Turn it into a skill.** Run [`prompts/stage-to-skill.md`](prompts/stage-to-skill.md). It turns that chapter's steps and "Check it" list into a skill.
3. **Save it.** In this repo, make a folder `.claude/skills/<skill-name>/` and save the result as `SKILL.md` inside it. Look at `.claude/skills/viewer-avatar/SKILL.md` for the format.
4. **Try it in Claude Code.** Type `/<skill-name>`. Check the output the same way you would by hand.
5. *[Coming soon: setting up the pipeline board, scheduled tasks and the capture system]*

**My setup:** *[Show: my real Multica board, "Youtube Video Production"]* *[Samin to fill: the tools I use for autopilot, e.g. Hermes, Claude Code scheduled tasks]*

## Check it

- [ ] Agents give you a head start, not the final say. Are you still judging every output?
- [ ] Does your skill include the "Check it" list from its chapter?
- [ ] Does it use your `CLAUDE.md`, viewer avatar and offer?
- [ ] Is every video one card, in one place, moving left to right?

## Tips

- **Start small:** one skill, then one scheduled task. Add more once those work.
- **Stay organized.** The board is what makes the system run.

## Status

**Coming soon.** Outline ready: the concepts and the skill prompt work now. The starter autopilot setup and walkthrough are coming.

Next: [Chapter 12: Tips and next steps](../12-tips-and-next-steps/README.md).
