# Chapter 1: Foundation (you, your viewer, your lane)

**Time:** about 30 minutes with the onboarding prompt.
**Required:** yes. Every other chapter builds on it.

## Why this matters

YouTube wants to show people videos they're glad they watched. So viewer satisfaction is what makes videos do well, and you can't satisfy someone you don't know.

And AI can only come up with good ideas if it knows who you're talking to and what you sell. This chapter gives it both.

## What you'll learn

- **Working backwards.** Amazon starts with the customer and works back from there. We start with the viewer. *(Samin, from his time as an Amazon engineer)*
- **Satisfaction is the metric.** Jake Trinder had a training video people watched only about 12% of on average, and it still got over 800,000 views, because the right people watched it and were happy. *(Jake Trinder)*
- **Audit yourself first.** A GPS can't route you anywhere without the "you are here" dot. Before the avatar, get clear on who you are, your business and offer, what you know, your proof, and what you could make 100 videos about.
- **Pick your lane.** A lane is audience + value: "Who are your videos for, and why do they care?" Random videos with no through-line confuse YouTube about who to show them to. Treat your lane as a hypothesis, not a forever decision. *(Aprilynne Alter)* "The best sushi restaurants, they just do sushi." *(Paddy Galloway, in Aprilynne Alter's course)*
- **Have a business? Your niche is your customer.**
- **Test the niche.** Is it still alive (check Google Trends)? Can you make 250+ videos on it? Is the audience big enough (a high-ticket offer only needs a few hundred of the right people)? Can you be the best or the first? *(Marcus Jones's niche funnel)*
- **Be different, not just better.** Don't open a knockoff Five Guys, make a "burgerito." *(DougDoug, in Aprilynne Alter's course)* Find your X factors: real traits your audience cares about. Exaggerate real ones, never fake them. *(Marcus Jones)*
- **The viewer avatar.** A short profile of one specific person: who they are, what they want, where they're stuck, what they've tried, the words they use. The questions come from Paddy Galloway's audience overview: Cluster, TAM and Personality. *(Paddy Galloway, YouTube strategist who's worked with MrBeast)*
- **Your viewer is your customer.** The person who watches is the person who buys. Like the free samples at Costco: the person tasting is the person who buys the box. Your videos are the sample, your offer is the box.
- **Your lane is the overlap.** Where what you know meets what your viewer needs. A taco truck needs tacos the chef is great at, and a street full of people hungry for tacos.
- **One main offer.** What you sell, who it's for, what problem it solves. A magnifying glass only starts a fire when the light is focused on one spot. Point every video at one offer.
- **Brand voice guide.** Talk into a voice memo, then have Claude turn it into a guide. *(Nate Curtiss)*

## What you'll build

1. [`my-channel/about-me.md`](../../my-channel/about-me.md): your audit. Who you are, what you know, your proof.
2. [`my-channel/offer.md`](../../my-channel/offer.md): your one main offer.
3. [`my-channel/viewer-avatar.md`](../../my-channel/viewer-avatar.md): a one-page profile of your ideal viewer (and customer).
4. [`my-channel/lane.md`](../../my-channel/lane.md): your lane, where your skills meet their problems.
5. [`my-channel/brand-voice.md`](../../my-channel/brand-voice.md): how you sound (optional for now).
6. A filled-in [`CLAUDE.md`](../../CLAUDE.md) that points to all of them.

Want to see a finished avatar? Here's mine (still in progress): [`examples/samin/viewer-avatar.md`](../../examples/samin/viewer-avatar.md)

## Steps

**Fastest way:** paste the onboarding prompt from the [main README](../../README.md#start-here-copy-this-prompt), or type `/onboarding` in Claude Code. It runs every step below for you, one question at a time, and saves the files. The steps below are the same thing by hand.

1. **Audit yourself.** Fill in [`my-channel/about-me.md`](../../my-channel/about-me.md): who you are, your story, your skills, your proof, and what you could make 100 videos about.
2. **Write your offer.** Run [`prompts/offer.md`](prompts/offer.md). Save the result in `my-channel/offer.md`, and paste the one-line summary into `CLAUDE.md`.
3. **Gather what you have (optional, but it makes your avatar much better).** Real words from real people beat guesses.
   - Have customers? Grab sales-call transcripts or customer emails. Claude pulls out their pains, words and objections.
   - Starting from scratch? Grab comments (on your videos or channels like yours), Reddit threads, and competitor video titles and comments.
4. **Run the viewer avatar interview.** Start a new chat. Paste the prompt from [`prompts/viewer-avatar-interview.md`](prompts/viewer-avatar-interview.md), paste your material under it, and press Enter.
5. **Answer the questions.** Claude asks one at a time. Short answers are fine. Stuck? Say "give me examples." Not sure? Give your best guess.
6. **Save it.** Open [`my-channel/viewer-avatar.md`](../../my-channel/viewer-avatar.md) and replace everything inside with Claude's finished avatar.
7. **Update your CLAUDE.md.** Paste Claude's 5-line summary into the "My viewer" part of [`CLAUDE.md`](../../CLAUDE.md).
8. **Find your lane.** Read your audit and your avatar side by side (or ask Claude to). Write your lane in one sentence and 3–5 lane topics in [`my-channel/lane.md`](../../my-channel/lane.md).
9. **Optional: make your brand voice guide.** Record a short voice memo (the prompt tells you what to talk about), get the transcript, and run [`prompts/brand-voice.md`](prompts/brand-voice.md). Save it in `my-channel/brand-voice.md`.

**Using Claude Code?** Skip the copy and paste for the avatar. Open this folder in Claude Code and type `/viewer-avatar`. Claude runs the same interview and saves the file for you.

The blank avatar form is in [`templates/viewer-avatar.md`](templates/viewer-avatar.md), if you'd rather fill it in by hand.

## Check it

- [ ] Is your audit honest about what you know and what you can prove?
- [ ] Can you describe your viewer in one sentence?
- [ ] Can you say your lane in one sentence?
- [ ] Does the avatar sound like your real customers, or generic?
- [ ] Would 80% of the people who liked your last video want your next one? *(Aprilynne Alter's 80% rule)*
- [ ] Do you have one main offer every video can point to?
- [ ] Does your brand voice guide sound like you when you read it out loud?

## Tips

- **Pick one person.** Your main viewer, not everyone who might watch.
- **Be specific.** "Small business owners" is too broad. "Owners of 5-person cleaning companies who want more clients" is much better.
- **Guessing is fine.** Update it as you learn more. Come back to it every few months.
- **Don't overthink branding early, and be decisive.** *(Marcus Jones)*
- **Give a lane at least 10 focused videos before you switch.** *(Aprilynne Alter)*
- **No offer yet?** That's fine. Make content about what you can do and cool things you've done.

## Status

**Step ready.** Done? Share your avatar in the community: [Community link]

Next: [Chapter 2: Ideation](../02-ideation/README.md).
