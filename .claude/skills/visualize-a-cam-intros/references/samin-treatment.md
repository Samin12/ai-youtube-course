# Samin's treatment (the look that got approved)

Measured from the scene 1 hook of the Fable 5.1 video, approved 2026-09-01 after two critic rounds. Use these as the defaults; deviate only when the footage forces it and say why.

## Frame

- **Asset full frame, presenter on top.** The proof fills 1920×1080. The camera is a custom-layout source drawn last: bottom-right at x 0.775, y 0.715, width 0.21, height 0.25 of the canvas, `squircle_v2` corners, radius ratio 0.0284, soft shadow (blur 0.0185, black at alpha 100). The camera is never covered, never resized per slot, never vignetted.
- No panels, no rounded card around the proof, no desktop showing at the edges, no letterbox in a different black than the background. When a source is not 16:9, it sits centered on near-black `#0f0d0b` so the padding reads as background, not bars.
- Keep the object of the sentence out from under the camera window (x ≥ 1488, y ≥ 772 at 1080p). Crop or nudge the source so labels, the last bar of a chart, or the output node of a diagram stay visible.

## Later-footage B-roll ("this is happening later")

Every clip pulled from later in the same recording gets the same two marks so the viewer reads it as a preview, not the present:

- **Slight vignette:** `vignette=angle=PI/8:mode=forward` (corners ≈78 % of center brightness, edge centers ≈88 %). `PI/4.6` is too heavy; it reads as a dirty frame edge on light graphics.
- **Thin line:** 3 px, white at 35 % opacity, full width, 28 px above the bottom edge (`drawbox=x=0:y=1052:w=1920:h=3:color=white@0.35`). Subtle; sits just below the camera window.
- Real motion inside the clip: the presenter's cursor, a box being drawn, a scroll, a click landing. Add only a slow push (1.04–1.08 over the slot) on top; never let the push be the only motion.
- Crop to the proof region and scale to fill: the benchmark table, the cost table, the right two-thirds of a chart where the marked bars are, the top row of an agents grid where the model tags are readable (~18 px or larger at 1080p).

## Text on screen (tweets, posts, results pages)

- Centered, big, on near-black: 1250–1450 px wide at 1080p depending on the card's aspect, so the text block ends before the camera window. Slow push 1.06–1.07 anchored on the line that carries the proof. Vignette yes, bottom line no (it is not later footage).
- Crop the card to the words and the one element that proves the point (the author row, the quote, the red-boxed bar). Drop rotated axis labels and menu chrome. Never leave a line half under the camera.
- A results page (YouTube search, a feed) pans: scale to 1920 wide, slide down ~900 px over the slot.
- Never composite a screenshot that has the presenter's own player or camera baked into it.

## Rhythm

- One visual per spoken clause. Slots run 2.4–6.5 s; the hook opens on the strongest proof, not on the presenter.
- Every cut leads the spoken word by ~120 ms so the eye lands before the ear. Cut on the clause boundary the visual proves.
- Render slot clips at 60 fps so boundaries do not drift when slots are re-cut.
- Stills (a thumbnail, a roster hold) get one motivated push (1.15 anchored on the subject); never more than two stills in a row.
- When the presenter says "posts," show the post and the wall of posts. When he says "the agent team," show the faces and the model tags, not the chat log. When he says a number, the number is the biggest thing in the frame with the cursor on it.

## What the presenter rejected, so do not ship it

- Static screenshots standing in for footage ("you're just showing me literal pictures").
- An 82 % overlay panel with the desktop recording visible around it and drifting behind it.
- A full-frame overlay that hides the camera (Borumi draws overlays above the camera).
- A tweet at 44 % width with black bars, or a tweet whose fourth line runs under the camera.
- A dense chat/log scroll or a loading skeleton where an agent grid was promised.
- A hype tweet on a sentence about the release date; the tweet belongs on the sentence about posts.

## Zooms must glide, not shimmer or stutter

Never render a push with ffmpeg `zoompan`: it rounds the crop offset to whole pixels every frame and reads as a vibrating shimmer on every slot (the presenter called it a "vibrating puff"). A per-frame `scale` with integer sizes is no better: the motion lands on alternate frames as a stutter. Render pushes as a `perspective` remap with `interpolation=cubic` and `eval=frame`, zoom driven by `in/N` on a 3840×2160 frame, then downscale to 1920×1080. Measured on a tweet card at 60 fps: per-frame difference alternation 0.03 (perspective) versus 0.74 (zoompan) and 0.94 (stepped scale). `scripts/compose_screen_source.py` does this in `smoothzoom()`.
