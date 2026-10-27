# The Higgsfield clips of Samin (Soul `Samin Yasar`, id e4e198c2-0e58-482c-aa8d-47ed2dd72ae1)

Route: `generate_image` with `soul_2` + `soul_id` (16:9) → pick the still → fix any text → `generate_video`
`seedance_2_5`, `mode: omni_reference`, the still as `start_image`, 6–8 s, 16:9, 720p, `generate_audio: false`
(pass `declined_preset_id` if the server answers with a preset recommendation) → tile the clip every 0.5 s and read
it like a person → `mode: video_edit` with the clip as `video_references` to fix text or object state.

## clip-limit-edit.mp4 ("there have been days… boom, there goes my limit")

Still: "Cinematic medium shot of Samin Yasar at a modern home-office desk at night, warm desk lamp, sitting in front
of an open laptop, leaning back with both hands pressed to the sides of his head in frustration, exasperated
open-mouthed expression, eyes on the screen. The laptop screen shows a dark AI video app with a large red banner
reading 'Daily limit reached — try again in 3 hours' and a greyed-out Generate button. Photorealistic, shallow depth
of field, 35mm, natural skin, no text anywhere except on the laptop screen."

Video (6 s): "Continuous handheld shot, no cuts. The man sits forward, types a short prompt on the laptop and hits
enter with one finger, waits a beat, then the red 'Daily limit reached' banner flashes on the laptop screen; he
freezes, throws both hands to the sides of his head, leans back in the chair and exhales in frustration, then drops
his hands and stares at the screen in disbelief. Natural indoor lighting, realistic motion, the laptop stays in frame."

Text fix (`video_edit`): "Edit only the laptop screen: replace all text on the screen so the red banner reads exactly
'Daily limit reached — try again in 3 hours' in clean white sans-serif, with a small grey 'Generate' button below it.
Keep everything else identical: the man, his motion, the room, the lighting, the camera movement."

In the cut: `ss 0.4`, `speed 0.81`, so the banner pops on "boom" and the hands land on "there goes my limit".

## clip-client.mp4 ("nearly impossible to calculate generations and charge clients")

Still (`client-1.png`): "Cinematic medium shot of Samin Yasar sitting at a bright modern meeting table, facing a client
(a woman in a beige blazer seen from behind and slightly out of focus in the left foreground, mid-sentence with one
hand raised). Samin is on the right, short dark hair, clean-shaven, black polo shirt, puzzled expression, one hand
scratching the back of his head, eyebrows raised, mouth slightly open. Three large glossy white cartoon question marks
with thin black outlines float above his head. A clean white comic speech bubble beside the client reads exactly
'How much does it cost?' in bold black sans-serif. Photorealistic people, soft daylight, shallow depth of field, 35mm,
no other text anywhere."

Bubble text came back garbled; fixed with GPT Image 2.5 (`image_references`): "Edit this photo. Change only the text
inside the white speech bubble so it reads exactly 'How much does it cost?' in bold black sans-serif lettering, cleanly
spelled, two lines, same bubble size and position, same tail pointing toward the woman. Keep everything else
pixel-identical…" → `client-1-edit.png`.

Video (6 s): "Continuous shot, no cuts, subtle handheld camera. The woman in the beige blazer is asking her question,
nodding and gesturing with one hand toward the man. The man listens, then looks completely lost: he scratches the back
of his head, glances up at the three white question marks bobbing above his head, opens his mouth as if to answer and
nothing comes out, then gives a small helpless shrug with both palms up and an awkward uncertain smile. The white
speech bubble with the text 'How much does it cost?' stays fixed, sharp and fully readable the whole time; the question
marks stay above his head. Natural indoor light, realistic motion, no new text appears."

In the cut: `ss 0.3`, natural speed; the shrug lands on "client work".

## clip-behind-empty.mp4 ("the only option you had was to upgrade… limits I might not even use")

Still (`behind-1.png`): "Over-the-shoulder shot from directly behind Samin Yasar (short dark hair, black polo shirt)
sitting at a warm home-office desk at night, his head and shoulders in the lower foreground, slightly out of focus.
In front of him a large open laptop fills the center of the frame, its screen sharp and readable: a clean SaaS pricing
page with a bold heading that reads exactly 'Upgrade plan', three pricing tier cards beneath it and a big green button
that reads exactly 'Upgrade'. His right hand rests on the trackpad. A brown leather wallet lies closed on the desk
beside the laptop. Desk lamp glow, photorealistic, 35mm, no other text anywhere except on the laptop screen."

Two GPT Image edits still misspelled the button ("Ulagrande"), so a clean pricing page (heading, three rows, green
Upgrade button) was painted onto the laptop with PIL → `behind-1-clean.png`, uploaded with `media_upload` + `media_confirm`.

Video (8 s): "Continuous over-the-shoulder shot from behind the man, no cuts, the camera holds still. He moves the cursor
and clicks the green 'Upgrade' button; the pricing page immediately highlights a higher plan with a bigger price; he
clicks 'Upgrade' again and the price goes up again; he clicks a third time, then stops and exhales, annoyed. He reaches
for the brown leather wallet on the desk, picks it up and opens it wide: it is completely empty inside, no cash, no
cards. He turns his head to the side so his face is seen in profile, staring into the empty wallet in dismay, then lets
his shoulders drop. The laptop screen stays sharp and readable with the heading 'Upgrade plan' and the green 'Upgrade'
button the whole time. Natural indoor light, realistic motion, no new text appears."

The wallet came back with a bill in it; `video_edit`: "Edit only the inside of the brown leather wallet: from the moment
it opens until the end, the wallet must be completely empty, no cash, no bills, no cards, no receipts, just the bare
empty leather interior and empty card slots. Keep everything else identical…" → `clip-behind-empty.mp4`.

In the cut: `ss 0.8`, `speed 1.22` for the clicks, then a punch-in (`crop 900:506:382:212`) from clip time 6.44 s so the
open wallet clears the camera window.
