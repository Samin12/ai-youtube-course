# Claim → proof map prompt

Finds every claim in your script and suggests proof to show on screen. *(Proof-based editing: every claim gets proof.)*

**How to use it:** paste this into Claude. Your script should be in `my-video/04-script.md`, or paste it (or a transcript of your recording) under the prompt.

````text
Go through my script (my-video/04-script.md, or pasted below) and build a claim → proof map.

1. List every claim: any number, result, "this works", comparison, or statement a skeptical viewer might doubt.
2. For each claim, suggest the proof to show on screen: a screenshot, chart, tweet or post, result, screen recording, on-screen text, or a full-frame diagram. Be specific about what's in it.
3. Mark any claim where you can't see a real source in my notes as "NEEDS PROOF", so I can find it, soften it, or cut it.
4. Suggest on-screen text for each section: step numbers and the key point.

Give it to me as a table with these columns: # | Time or script line | The claim | Proof to show | Type | Have it?
Don't invent sources or numbers.
````
