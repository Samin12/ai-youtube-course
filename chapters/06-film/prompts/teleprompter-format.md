# Teleprompter format prompt

Turns your script into something easy to read on camera: either teleprompter lines (how I do it) or bullets you riff from (how Nate Curtiss suggests).

**How to use it:** paste this into Claude. Your script should be in `videos/<my-video>/04-script.md`, or paste it under the prompt.

````text
Format my script (videos/<my-video>/04-script.md, or pasted below) for filming.

Give me BOTH versions:

1. TELEPROMPTER: one sentence per line, a blank line between each. Section headings in bold. Keep every transition. Don't change my words, except to split long sentences.

2. BULLETS: the hook word for word, then 3–6 short bullets per section that I can riff from. Mark any screen-recording demo as "DEMO: talk through it".

Then list any sentence that's hard to say out loud, and suggest a simpler version.
````
