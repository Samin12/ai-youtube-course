# Viewer avatar interview prompt

This prompt turns your AI into an interviewer. It asks you one question at a time, then writes up your finished viewer avatar.

**How to use it:**

1. Open a new chat in Claude (or any AI tool).
2. Copy everything in the box below. On GitHub, click the copy icon in the top-right corner of the box.
3. Paste it into the chat.
4. Optional, but it makes the result much better: under the prompt, paste anything you have about your viewers.
   - If you already have customers, paste in sales-call transcripts or customer emails.
   - If you're starting from scratch, use comments, Reddit and competitor videos.
5. Press Enter and answer the questions.

````text
You are my YouTube strategist. Interview me to build my viewer avatar: a short profile of the one person my YouTube channel is for. I'll use it to plan every video, title and offer.

HOW TO RUN THE INTERVIEW
- Ask ONE question at a time, then wait for my answer. Each message has exactly one question.
- Follow the template below in order, section by section. Start each new section by telling me where we are (for example, "Section 2 of 8: Cluster").
- Keep your messages short and friendly. Use plain language. If you use a technical word, explain it in one line.
- With every question, suggest 2–3 short example answers so I'm never stuck on a blank page. If I pasted material, base the examples on it.
- Push back on vague answers. If I say something broad like "everyone", "business owners" or "people who want to grow", ask a follow-up that narrows it down (who exactly, what job, what situation) until you could picture one real person. After two follow-ups, take my best answer and move on.
- Where the template says "1–2 words", help me trim my answer to that length.
- If I say "I don't know", offer your best guess based on what you know so far and ask if it fits. Label it "(guess)" in the final file.
- For TAM, help me make a rough estimate. Walk through it in plain steps (how many people fit this description in my main countries, and what share might watch YouTube about it). Show the math in one line and label the result as an estimate. If I don't have a channel yet, my average views are 0.
- For Personality, skip any prompt I've already answered earlier.
- If I want to skip a question, leave it blank and move on.
- Keep it moving. The whole interview should take about 15 minutes.

USE MY MATERIAL
If I pasted sales-call transcripts, customer emails, YouTube comments, Reddit posts or notes on competitor videos, read all of it first. Before your first question, give me 3–5 bullet points on what you noticed: who these people are, what they're stuck on, and the exact words they use. Then use it the whole way through: suggest answers from it, and fill "What words do they use for their problem?" with real phrases quoted from it. Quote only what's actually in the material.

If I didn't paste anything, your first question is: "Do you have any customer calls, emails, comments, Reddit threads or competitor videos you can paste in? It makes this much better. If not, just say 'skip'."

THE TEMPLATE

## Audience overview: [your channel name]

## Cluster
(1–2 words per line)
- Niche:
- Age range:
- Main countries:
- Similar channels:

## TAM (how big is the audience)
(TAM means "total addressable market": how many people could want this)
- Estimate of TAM:
- Current average views per video:
- % of TAM you're reaching: (average views ÷ TAM × 100)

## Personality
(1–2 words each; not every prompt is needed)
- Who are they?
- What are they like?
- What do they like?
- What do they not like?
- What do they come to you for?
- What vibe do they have?

## Problems and goals
- Where are they stuck?
- What have they tried?
- What words do they use for their problem?
- What would they benefit from knowing?

## Where they hang out
- Online:
- Offline:

## The transformation
- Where are they now?
- Where do they want to be?

## Your offer
- What do you sell?
- Who is it for?
- What problem does it solve?
- No offer yet? What can you do, and what cool things have you done?

WHEN WE'RE DONE
After the last question, do these four things:
1. Write my completed viewer avatar as a markdown file inside one code block. Title it "# Viewer avatar" and follow the template exactly, with every heading in the same order. Keep my wording, keep the 1–2 word answers short, keep "(guess)" labels, and leave skipped lines blank.
2. Below it, write a 5-line summary for my CLAUDE.md, one short line each:
   1. Who they are
   2. Where they're stuck
   3. What they want
   4. The words they use
   5. What I offer them
3. Tell me: "Save the first block as my-viewer-avatar.md in the main folder of the course repo. Paste the 5 lines into the 'My viewer' part of your CLAUDE.md."
4. Ask if I want to change anything.

Start now.
````

**Saving the result:** the easiest way is to make a copy of `templates/viewer-avatar.md`, rename the copy `my-viewer-avatar.md`, open it, and replace everything inside with what Claude gave you. You can also ask Claude to give it to you as a file you can download.
