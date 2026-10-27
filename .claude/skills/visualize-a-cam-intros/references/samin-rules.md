# What Samin likes, in his own words

The rules below are the notes Samin actually gave while reviewing intros, dated, then the standing rules they add up to.
When a new note from him contradicts anything here, the new note wins and gets added.

## Higgs API hook, 19 Sep 2026 (approved as version 10, Borumi commit `9410`)

The brief:

> "Edit my intro so it's dynamic and like my current YouTube videos. Check it like a person. I want to see a lot of
> proof as visuals as I'm talking, or examples of what I will show in level 3, etc. Throughout the video there should
> be motion and a vignette around it. Look at my current YouTube videos."

Mid-edit notes (all applied by version 7):

> "When I say 'prompt it once or twice and hit a limit' put in an AI video of me doing that to show the frustration.
> Make that with Higgsfield."

> "Also show the frustration and empty wallet when the only option you had was to give money for an extra plan you
> didn't need."

> "When I say 'plan to make it 10x more efficient' show the strategies and GitHub repos in level 2."

> "When I say 'levels', look into how I show them in my other videos on YouTube, like my most popular one, and copy
> that style."

> "Math and strategy: quickly flash graphics over the level I discuss."

Review of version 7 on his phone (applied by version 10):

> "In the beginning I want you to have the end of the video. I don't want to start off with the smoking scene. The
> dancing part, that's fine."
> Clarified: "I meant the very start of the motion at 10:39, around there. That part of the clip is what I wanted to
> show in the very beginning." (The clip playing on screen at 10:32 to 10:41 of the recording: his STORM recast where the
> crowd drops and he stays standing. Its native file was on disk; the screen capture was not used.)

> "The frustration part started from when I say 'there have been days'. That's when you show the AI video, not the
> subscription graphic."

> "When I'm talking about the 'nearly impossible' part, show a scene where I'm talking to a client but I don't know
> what I can charge them. They say 'how much does it cost?' and I have question marks on top of my head."

> "For the upgrade, show it from the back, as if I have to keep upgrading, then I look at my wallet and it's empty."

Verdict on version 10: "Ok, this looks great."

Chapter cards, same day (see the `create-chapter-transitions` skill): "It should be like my current vids with the
sound and good chapter headings." When shown a dark card with a whoosh: "No. Look at my create-chapter-transitions
repo and my vids. It's white and black text. Use those assets in my git, and no sound effect [meaning: no whoosh]."
Then: "I don't hear the sound effect." Then: "That's not the right sound. Go rip it from my videos and use it."
Then: "In the GitHub skill, update it, put an example, the actual mp4, the sound file, everything, so we can reuse
the skill later, and get the exact type of chapter titles."

## Fable 5.1 hook, 1 Sep 2026 (approved after two critic rounds)

Rejected, in his words or close to them: static screenshots standing in for footage ("you're just showing me literal
pictures"); an 82 % overlay panel with the desktop recording drifting behind it; a full-frame overlay that hid the
camera; a tweet at 44 % width with black bars; a tweet whose fourth line ran under the camera; a dense chat/log scroll
where an agent grid was promised; a hype tweet on the release-date sentence; and any zoom that shimmered ("vibrating
puff"). The measured look he approved is in `samin-treatment.md`.

## Standing rules (each one traces to a note above)

1. **Open on the moment he names.** If he gives a timestamp, it is the clip playing on screen at that time; find the
   native file rather than cropping the screen capture. Never open on a smoking or vice shot, even when it is his own
   generation; his AI double moving ("the dancing part") is fine.
2. **Proof under every line, motion throughout.** Later footage carries the vignette and the bottom line. Static
   screenshots and paused players do not count as proof.
3. **A feeling gets an AI clip of him acting it.** When the line is frustration, disbelief or a story beat, generate a
   Higgsfield clip of Samin (his Soul `Samin Yasar`) doing literally what the words say, and start it on the first word
   of that line, not on a graphic first. The action beats land on the words: the limit banner pops on "boom", the
   hands go to the head on "there goes my limit", the shrug lands on "client work", the empty wallet opens on "limits
   I might not even use".
4. **A strategy line shows the strategy.** "10x more efficient" shows the Level 2 strategy slides and the GitHub repos,
   in the order he would show them later.
5. **"Levels" is shown his way.** The three blue circles pop on the white grid just before he says "levels", then
   each level gets the blue numbered circle, the bold italic title at the left, and its proof inside the dark device
   mock on the right, with the math and strategy graphics flashing quickly inside the mock of the level he is on
   (copied from his most-viewed video, *Claude Just Changed the Stock Market Forever*).
6. **Nothing that matters sits under the camera window.** Re-fit the card, or punch in for the last second when the
   subject lives bottom-right (the empty wallet).
7. **AI text must read right.** Check every generated frame like a person. If two AI edits still misspell a button,
   composite clean text onto the start image before animating. Fix object state (a wallet that should be empty) with a
   Seedance `video_edit` pass.
8. **Chapter cards come from his repo, with his click.** White canvas, faint grid, black Inter title typed in, 1.6 s,
   his own click at native level and audible in the export. Never a whoosh, never a synthesized tap, never a new style.
9. **He reviews on his phone and answers by line or timestamp.** Send a 720p copy of every committed version. Expect
   several committed iterations; the Higgs API hook took ten commits, the Fable hook three.
