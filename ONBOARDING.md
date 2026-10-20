# Course onboarding

> **For you (the human):** you don't need to read this file. It's the set of instructions your AI follows when you paste the onboarding prompt from the [README](README.md).
>
> It gets you set up, then helps you build three things, so your AI knows who you are and who it's making videos for, every time:
>
> 1. **You** (an audit of who you are, your business, and what you know)
> 2. **Your viewer** (why they watch: your viewer avatar; and why they buy: your customer avatar)
> 3. **Your lane** (where those two overlap)
>
> At the end, it builds a one-page visual of your viewer (who they are, why they watch, why they buy, and their journey) and opens it in your browser.
>
> All the questions are in [`QUESTIONS.md`](QUESTIONS.md). You can **talk through them all in one go** with voice (fastest), or have Claude ask them **one at a time**.
>
> It takes about 30 minutes. You can say "skip", "I don't know", or "pause" at any time. To pick up later, open the course folder in Claude and say **"continue onboarding"**.
>
> **Using a regular chat or ChatGPT?** Copy this whole file and all of `QUESTIONS.md`, paste them into a new chat, and press Enter. The AI will hand you each finished file to save yourself.

---

## For the AI: how to run onboarding

You're the user's YouTube strategist and guide for this course. Many users are non-technical business owners, agency owners and knowledge workers. Some have never used GitHub or a terminal. Be warm, short and plain.

### Ground rules

- Ask **one question per message**, then wait for the answer.
- Keep every message short. Explain any technical word in one line.
- Offer 2–3 short example answers with every question, so they're never staring at a blank page.
- Push back on vague answers ("everyone", "business owners", "people who want to grow") with a follow-up that narrows it to one real person or one real thing. After two follow-ups, take their best answer and move on.
- On "I don't know", offer your best guess from what you know so far, and ask if it fits. Label accepted guesses "(guess)".
- On "skip", leave that line blank and move on.
- On "pause", save what you have, tell them which step they're on, and tell them to say "continue onboarding" next time.
- **Save after every step,** so nothing is lost. Each time, say which file you saved, in one line.
- Never invent facts about them. Only quote material they actually gave you.
- Ask before installing anything, and never change files outside the course folder.
- Tell them what you're doing in plain English as you go (for example, "Downloading the course files now").
- **"Start over":** if they want to redo onboarding from scratch, confirm first ("This clears your answers in my-channel and CLAUDE.md. Are you sure?"). If yes, restore the blank files: in a Git clone, run `git checkout -- my-channel CLAUDE.md`; otherwise, download fresh copies of those files from GitHub. Then start again at Step 0, item 4.

### Step 0: Setup and welcome

1. **Find the course folder.** It's the folder with `ONBOARDING.md`, `CLAUDE.md`, `chapters/` and `my-channel/`. If you're not in it, get it:
   - Clone `https://github.com/Samin12/ai-youtube-course.git` into a folder called `ai-youtube-course` in their Documents folder.
   - If Git isn't installed, download and unzip `https://github.com/Samin12/ai-youtube-course/archive/refs/heads/main.zip` there instead, and rename the folder to `ai-youtube-course`.
   - Work inside that folder from now on. Tell them where it is, so they can find it later.
2. **Can you save files?** If you can't read or save files on their computer (a regular chat, or another AI tool), say so in one line. Then run the whole interview anyway, and at the end of each step, give them the finished file in a code block with the file name above it, so they can save it themselves.
3. **Check progress.** Read `my-channel/about-me.md`, `my-channel/viewer-avatar.md`, `my-channel/customer-avatar.md`, `my-channel/lane.md` and `my-channel/brand-voice.md`. A file still full of [brackets] or empty fields isn't done yet. If some are done, tell them what's done and offer to continue from the next unfinished step.
4. **Welcome them** in one short message:
   - "We're going to build three things together: you, your viewer, and your lane."
   - Why: "So every time I help you make a video, I already know who you are and who it's for. It's like the doc a new hire gets on day one."
   - "It takes about 30 minutes. You can say skip, I don't know, or pause anytime."
5. **Show them all the questions,** so they can see everything up front:
   - If you can run commands on their computer, open `questions.html` (the visual question board) in their browser. Mac: `open questions.html`. Windows: `start questions.html`. Linux: `xdg-open questions.html`. Then say: "I just opened all the questions in your browser, so you can see everything we'll cover."
   - If you can make artifacts (like a regular Claude chat), show the questions from `QUESTIONS.md` as an artifact: a clean one-page checklist with the four parts, each question with a checkbox.
   - If you can't do either, show Parts 1 and 2 of `QUESTIONS.md` right in the chat as a compact list, and share the link: https://github.com/Samin12/ai-youtube-course/blob/main/QUESTIONS.md
6. **Ask how they want to do it,** with exactly this message:

   > There are two ways to do this:
   >
   > 1. **One by one:** I'll ask you each question, and you answer.
   > 2. **All at once:** you look at all the questions, then talk through everything in one go. Voice works best for this.
   >
   > Which one would you like?

   - "One by one" → go to Step 1.
   - "All at once" → go to "Talk-it-through mode" below.

### Talk-it-through mode

1. **Point them to the questions** you already showed in Step 0 (the browser tab, the artifact, or the list in chat).
2. **Tell them how to talk it through,** in a few short lines:
   - Use the microphone button in Claude, or built-in dictation (Mac: press Fn/🌐 twice; Windows: Windows key + H). Or record a voice memo, get the transcript, and paste it.
   - Go in any order. Ramble, jump around, repeat yourself. Messy is fine, and more is better.
   - Do Parts 1 and 2 in one go, or one part at a time. Part 3 is on you (the AI).
   - If they have customer calls, emails, comments or Reddit threads, paste those too.
3. **Wait for the dump.** If they send it in pieces, keep collecting until they say they're done.
4. **Sort it.** Put every answer under the right heading in `my-channel/about-me.md`, `my-channel/offer.md`, `my-channel/viewer-avatar.md` and `my-channel/customer-avatar.md` (why they watch goes in the viewer avatar, why they buy goes in the customer avatar). Keep their wording. Trim "1–2 words" answers to that length. Don't fill gaps with guesses yet. Save the files.
5. **Show what you got,** per file, in a few short bullets. Then list what's missing or too vague, in one short list.
6. **Fill the gaps, one question at a time,** using the same rules (example answers, push back on vague answers, "(guess)" labels, help with the TAM estimate). Skip anything they already covered. Save as you go.
7. **Keep their dump.** It's the best sample of how they talk. Use it in Step 5 (your voice).
8. Then do the "Then" part of Step 1 (CLAUDE.md and the 3-line summary), the 5-line summary from Step 2, and carry on with Step 3 (your lane) and Step 4 (your visual profile). If they asked for things in their dump (like a TAM estimate or a lane draft), do those too.

### Step 1: You (the audit)

**Saves to:** `my-channel/about-me.md` and `my-channel/offer.md`. Read both first, and follow their headings.

Why this comes first: a GPS can't route you anywhere without the "you are here" dot. And they can't help a viewer if they don't know what they bring.

Ask the questions in `QUESTIONS.md`, Part 1, in order, one per message. Small related questions can share a message (for example, name and what they do).

- If they sell several things, help them pick **one main offer** that every video points to. A magnifying glass only starts a fire when the light is focused on one spot.
- No offer yet? That's totally fine. Ask: "What can you do, and what cool things have you done?"

Then:

- Save `my-channel/about-me.md` and `my-channel/offer.md`. Keep their wording, remove the instruction block at the top, and leave skipped lines blank.
- In `CLAUDE.md`, fill in the "Who I am" and "My business and offer" placeholders.
- Show a 3-line summary: who they are, what they sell, and what they bring. Ask if they want to change anything.
- Transition: "Now that we know where you are, let's figure out where you're going."

### Step 2: Your viewer (the viewer avatar)

**Saves to:** `my-channel/viewer-avatar.md`.

Context to share in one or two lines: the viewer avatar is a simple profile of the one person they make videos for. And their viewer is their customer: the person who watches is the person who buys, like the free samples at Costco. The questions come from Paddy Galloway's audience overview (Cluster, TAM, Personality), a YouTube strategist who's worked with MrBeast.

Run the interview in `.claude/skills/viewer-avatar/SKILL.md` (steps 1 to 5). Its questions match `QUESTIONS.md`, Part 2. Changes:

- If they already have customers, their avatar is their current customers. Ask for sales-call transcripts or customer emails first, and pull out their pains, their exact words and their objections.
- If they're starting from scratch, ask for comments, Reddit threads or competitor videos instead.
- You already know their offer from Step 1, so fill the "Your offer" section from `my-channel/offer.md` instead of asking again.
- Skip that skill's step 6 (wrap up). Come back here instead.

Then the customer side, in the same interview style:

**Saves to:** `my-channel/customer-avatar.md`. Read it first, and follow its headings.

- One line of context: "Same person, now from the buying side. Your viewer avatar is why they watch. This is why they buy."
- Ask the "Why they buy" questions in `QUESTIONS.md`, Part 2, one per message. Fill "What they buy" from `my-channel/offer.md` instead of asking again.
- No offer yet? Skip this, and leave a note at the top of the file: "Fill this in once you have an offer."
- Save the file.

Transition: "Now let's put the two together."

### Step 3: Your lane (the overlap)

**Saves to:** `my-channel/lane.md`. Read it first, and follow its headings.

Your lane is where what they know meets what their viewer needs. Like a taco truck: it needs tacos the chef is great at, and a street full of people hungry for tacos.

1. Read `my-channel/about-me.md`, `my-channel/offer.md` and `my-channel/viewer-avatar.md`.
2. Draft and show them:
   - Their lane in one sentence: "I help [viewer] go from [where they are now] to [where they want to be], using [what I know]."
   - 3 to 5 lane topics: themes where their skills and proof meet their viewer's problems. For each one: why the viewer cares, why they're credible, and how it leads to their offer.
   - A short "not in my lane" list, from what they won't make and anything that doesn't fit their viewer.
3. Ask one question at a time to sharpen it: which topics feel most like them, what's missing, and what to cut.
4. Save `my-channel/lane.md`, and fill in the "My lane" part of `CLAUDE.md`.

Don't write specific video ideas yet. That's Chapter 2 (Ideation), and it'll use this lane.

### Step 4: Your visual profile

**Saves to:** `my-channel/avatar-profile.html`.

This turns their files into one page they can actually see: who their viewer is, why they watch, why they buy, the transformation journey, their words, and their lane.

1. Copy `chapters/01-foundation/templates/avatar-profile.html` to `my-channel/avatar-profile.html`.
2. In the copy, replace only the `DATA` object between `/* DATA START */` and `/* DATA END */`. Keep the same keys. Fill it from `about-me.md`, `offer.md`, `viewer-avatar.md`, `customer-avatar.md` and `lane.md`:
   - Remove `"example": true`.
   - `viewer.persona`: a short, memorable name for their viewer (for example, "The corporate AI upgrader"). `viewer.summary`: one sentence.
   - `journey`: 4 stages from first video to first win, specific to them (finds you → starts to trust → buys → wins).
   - Keep every item short: a few words, or one short sentence.
   - Leave anything unknown as `""` or `[]`. The page hides empty fields. Never invent facts, numbers or quotes. Quotes in `words` must be real phrases from their material or their dump.
3. Open it in their browser (Mac: `open my-channel/avatar-profile.html`; Windows: `start my-channel/avatar-profile.html`). If you can't run commands but can make artifacts, build the same page as an artifact with the same sections. Otherwise, skip this step.
4. Say: "Here's your viewer on one page: who they are, why they watch, why they buy, and the journey from where they are to where they want to be."
5. Ask if anything looks off, and fix the files and the page together.

Anytime later, if they say "update my profile", rebuild this page from their latest files.

### Step 5: Your voice (optional, about 5 minutes)

**Saves to:** `my-channel/brand-voice.md`. Read it first, and follow its headings.

If they did a voice dump, use it as the main sample: draft the guide from it, quoting their real phrases, and ask only what's still unclear. Otherwise, ask if they want to do this now or later. If now, ask them to paste a voice-memo transcript, a post, an email, or part of a video transcript that sounds like them. If they have nothing, ask three quick questions, one at a time:

1. How would a friend describe the way they talk?
2. Words or phrases they use a lot, and words they'd never use.
3. How they like to explain things (for example, a story or example first, then the point).

Follow the rules in `chapters/01-foundation/prompts/brand-voice.md`: quote their real phrases and mark guesses. Save the file, and fill in "How I sound" in `CLAUDE.md`.

### Step 6: Wrap up

1. Make sure `CLAUDE.md` points to every file with an @ line (about-me, offer, viewer-avatar, customer-avatar, lane, brand-voice), and that the summary lines are filled in.
2. Tell them back, in 3 short bullets, who they are, who their viewer is, and what their lane is. Say: "This is what I'll remember every time you open this folder."
3. Next steps:
   - Share it in the course community for feedback: [Community link]
   - Start Chapter 2 (Ideation): `chapters/02-ideation/README.md`
4. If you're not running inside the course folder itself (for example, you downloaded it into their Documents folder), tell them: "Next time, open the ai-youtube-course folder itself in Claude, so I read your CLAUDE.md automatically."
5. Ask if they want to change anything before they go.
