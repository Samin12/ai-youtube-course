# Stage to skill prompt

A skill is a saved set of instructions an agent follows for one job. You already wrote most of yours by doing each stage by hand. This prompt turns one stage into a skill.

**How to use it:** paste this into Claude Code (or any Claude chat). Under it, paste that chapter's README (or point Claude to the folder) and the `videos/<my-video>/` file you filled in for that stage.

````text
Turn one stage of my YouTube process into a Claude skill.

The stage: [e.g. Ideation]
The chapter: chapters/[folder]/README.md, plus its prompts/ folder (or pasted below).
My filled-in example: videos/<my-video>/[file].md (or pasted below).

Write a SKILL.md file with:
1. A header block:
   ---
   name: [short-name-with-dashes]
   description: [one sentence: what it does and when to use it]
   ---
2. Files: which files to read first (CLAUDE.md, my-channel/viewer-avatar.md, my-channel/offer.md, my-channel/brand-voice.md, and the videos/<my-video>/ files from earlier stages) and which file to save to (the videos/<my-video>/ file for this stage).
3. Steps: the chapter's steps, in order, using its prompts.
4. Check it: the chapter's "Check it" list. The skill must run these checks on its own output and tell me what passed and what didn't.
5. Rules: ask me before guessing; don't invent facts, numbers or sources; keep my voice.

Use .claude/skills/viewer-avatar/SKILL.md as the format example if you can see it.
Give me the finished file in one code block, and tell me to save it as .claude/skills/[short-name]/SKILL.md.
````
