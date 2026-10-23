---
name: video-intro
description: Write a video's intro (the hook) word for word, as 3 options to pick from, each one hitting the 4 P's (promise, proof, plan, persona) and confirming the click in the first 5 seconds. Reads the outline (one-pager) and the package, writes in the user's voice using the opening patterns from Samin's top videos, checks every option, then saves the intros to 04-script.md and the Poppy board. Use when the user says "help me write the intro", "write the intro for this", "I like this outline, now the intro", "write my hook", "give me hook options", or right after the one-pager is done (Stage 4, Outline + script).
---

# Video intro (the hook, word for word)

The intro is the one part of the video you write out word for word. Its first job is to **confirm the click**: the first line matches the title, and the first shot matches the thumbnail, in the first 5 seconds. Then it gives them more than the title promised, and answers the 4 questions every viewer has:

1. **Promise:** is this what I clicked for?
2. **Proof:** why should I listen to you?
3. **Plan:** how are you getting me there? (the levels)
4. **Persona:** is this for me?

You write **3 options**, each in a different opening style, and the user picks one. Your output must look like `example.md` in this folder. The opening styles, with real intros from Samin's top videos: `intro-patterns.md`.

Keep messages short and plain.

## Step 0: Find the outline

- The user usually asks right after the outline ("help me write the intro for this, I like this outline"). Use the outline in this conversation.
- Not in this conversation? Look in the current video's `04-script.md` (the "Outline (one-pager)" section), then their Poppy board (a note called "One-pager: <title>"). Still nothing? Ask once: "Where's the outline for this video: a file here, your Poppy board, or do you want to paste it?"
- From the outline, pull:
  - every title and thumbnail being tested
  - the one promise
  - the levels (that's the Plan)
  - who it's for (that's the Persona)
  - their proof: results, numbers, experience, from the brain dump
- Read `my-channel/brand-voice.md` and `my-channel/about-me.md`: their proof line, and how they open a video. If they've pasted past intros of their own, copy their pattern first. Otherwise use `intro-patterns.md`.
- No outline and no title yet? Stop and say: "Let's make the outline first (say 'make the outline'). The intro keeps the promise the outline is built on."

## Step 1: Write 3 intros

Pick the 3 opening styles from `intro-patterns.md` that fit this video best. For a tutorial, the default is Result first, The experiment, and Pain first. Write each one word for word, in this order:

1. **Promise (confirms the click):** the first line says what the title says, in the first 5 seconds. Testing several packages? It has to work for every one of them.
2. **Give them more:** one or two lines that go past the title: something they didn't expect, the stakes, or a preview of the payoff.
3. **Proof:** one line: their result, their experience, or how much work went in. Only what's true for them. Unknown? `[my proof]` or `[real result]`.
4. **Plan:** "In this video, I'm going to be breaking down how you can [do it] in three levels." Then one short line per level, from the outline.
5. **Persona:** who it's for, and that they can do it: "Even if you've never [the scary thing], you'll be able to do this."
6. End with "Let's get into it." and one line into Why this matters: "Okay, before we get into anything, I need to give you some context on why this matters."

Add the **first shot**: what's on screen in the first 5 seconds, matching the thumbnail. Under each intro, mark each line with its P, and give the word count (aim for 100–150 words, so it's under a minute out loud).

## Step 2: Check every option

Fix anything that fails before you show them.

- [ ] The first line works for every title being tested, inside the first 5 seconds
- [ ] The first shot matches the thumbnail
- [ ] It gives more than the title promised
- [ ] All 4 P's are there
- [ ] Under a minute out loud (150 words max)
- [ ] No "hey guys", no subscribe ask, no logo, no long backstory, no vague hype ("you won't believe…")
- [ ] Anything that would break the promise is said up front (e.g. "paper" money)
- [ ] No made-up results, numbers or quotes

## Step 3: Show them, and let them pick

- Show the 3 intros in the format below, then one line: which one you'd pick and why.
- Ask: "Which one do you like? Or tell me what to mix."
- Fold in their notes, in their words. Deleted stays deleted.

## Step 4: Save it

- Save all 3 options in the video's `04-script.md` under "Intro (word for word)". When they pick, put the winner first and update the Intro in the one-pager.
- **Poppy connected:** add a note titled "Intros: <working title>" to the video's "<video> · Brain dump + outline" group (`add_to_board` with `group_title`). When they pick, update it with the winner at the top (`write_note`, replace).

## The format (match example.md)

```
# Intro options: <working title>

**Packages (testing):** …
**The promise:** "…"

## Option A: <style> (recommended)
**First shot:** …

"<line>" ← Promise (confirms the click)
"<line>" ← Give them more
"<line>" ← Proof
"<line>" ← Plan
"<line>" ← Persona
"Let's get into it."
→ Into why this matters: "…"

**<N> words · about <N> seconds**

## Option B: <style>
## Option C: <style>

**My pick:** Option A, because …
```

## Rules

- Write the way they talk: short sentences, one idea per line. Their own stock lines beat new ones.
- No analogies in the intro. Save them for Why this matters.
- Never name other creators or quote them in the intro.
- Never invent results, numbers, costs or quotes. Anything only they know goes in `[brackets]`.
