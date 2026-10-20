# Funnel map prompt

Builds your funnel right to left, starting from your offer. *(Taki Moore's System)*

**How to use it:** paste this into Claude. It should see your `CLAUDE.md`, viewer avatar and offer.

````text
You are my business strategist. Help me build a simple YouTube funnel, using Taki Moore's System. Use my CLAUDE.md, viewer avatar and offer (my-channel/offer.md).

THE IDEAS
- People move cold (skeptical) → warm (curious) → hot (ready).
- Four columns, left to right: lead gen → lead nurture → conversion → delivery.
- YouTube long-form fits mostly in lead nurture (middle of the funnel).
- A funnel is just a series of easy yeses. Each step only has to sell the next step.
- Build it right to left: start from the product.
- Every video points to ONE place: one video that explains my offer.

HOW TO RUN IT
- Ask me ONE question at a time, with 2–3 example answers. Keep it plain.
- Start with delivery (what the client gets), then conversion, then lead nurture, then lead gen.
- If I have more than one product, push me to focus on one.
- If my path is longer than 3 steps, help me simplify it.

WHEN WE'RE DONE
Fill in this one-page map as markdown in one code block, titled "# My funnel map":
- My path in 3 steps or fewer
- The System table: for each column, the temperature, what they get, my version, and the easy yes
- The octopus: my middle video, the one next step, and 3 tentacle video ideas
- My micro magnet idea
- My offer doc (what it needs to say)
- Where people join my email list
Then tell me: "Save this in my-channel/funnel-map.md (replace everything in it)."
````
