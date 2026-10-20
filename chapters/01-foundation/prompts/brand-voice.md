# Brand voice guide prompt

Talk into a voice memo, then have Claude turn it into a brand voice guide. *(Method from Nate Curtiss.)*

**How to use it:**

1. Record a short voice memo on your phone (a few minutes is plenty). Talk the way you'd talk to a viewer. Ideas: what you do and who you help, a story about a client or a win, your take on a common mistake in your field.
2. Get a transcript of it (many voice-memo apps can transcribe for you).
3. Optional: add a post, an email, or a video transcript you think sounds like you.
4. Open a new chat, paste the prompt below, paste your transcript and samples under it, and press Enter.

````text
You are my editor. Below is a transcript of me talking, plus any samples of my writing. Turn it into a short brand voice guide, so any AI can write like me.

RULES
- Base everything on what's actually in my transcript and samples. Quote my real phrases. Don't invent a personality.
- Keep it short and plain. Each line is one short answer.
- If something isn't clear from the material, write "(guess)" next to it.

FILL IN THIS TEMPLATE
## How I sound
- In 3 words:
- How I talk to my viewer:
## Words
- Words and phrases I use a lot:
- Words I never use:
## How I explain things
- Sentence style:
- How I explain an idea:
- How I open a video:
- How I end a video:
## Samples that sound like me
(2–3 short passages copied word for word from my transcript)

WHEN YOU'RE DONE
1. Write the finished guide as markdown in one code block, titled "# My brand voice".
2. Tell me: "Save this in my-channel/brand-voice.md, and put your 3 words in the 'My voice' part of your CLAUDE.md."
3. Ask if anything doesn't sound like me.

Here's my transcript and samples:
````
