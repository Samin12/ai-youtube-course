---
name: visualize-a-cam-intros
description: Turn talking-head A-cam intros into proof-first visual stories by keeping the presenter pinned on top as a stable anchor while cherry-picking, reframing, timing, and animating B-roll, product footage, screenshots, slides, comparisons, and prior-video clips. Use for YouTube or course intros, podcast hooks, transcript-matched B-roll edits, presenter picture-in-picture layouts, Borumi timeline edits, HyperFrames intro composites, or QA of dense A-cam/B-roll openings.
---

# Visualize A-Cam Intros

Build an intro in which the presenter carries the narration while the rest of the frame proves each claim. Favor real outputs, action, and visual variety over decorative motion. The approved references for this skill are the Fable 5.1 hook (2026-09-01) and the Higgs API hook (2026-09-19, [examples/higgs-api-intro](examples/higgs-api-intro)). The look is measured in [references/samin-treatment.md](references/samin-treatment.md), the presenter's own notes and the standing rules they add up to are in [references/samin-rules.md](references/samin-rules.md), the build route is in [references/borumi-proof-pipeline.md](references/borumi-proof-pipeline.md), and the cut is judged with [references/rubric.md](references/rubric.md). Read all four before planning.

## Route the work

- For an open Borumi Project, use the Borumi MCP tools and required Borumi guides. Inspect and edit through a transaction; do not modify Project files directly. If the agent host cannot add an MCP server mid-session, drive Borumi with `scripts/borumi_mcp_session.py` (a persistent stdio client) and follow `references/borumi-proof-pipeline.md` step by step.
- For authored composites, motion graphics, or a standalone render, read `hyperframes` first, then the companion skills it requires.
- For source extraction, transcription, cropping, or transcoding, use `media-use` and `talking-head-recut`.
- Use ordinary timeline media when a clip only needs a trim or reframe. Use HyperFrames when the beat needs a designed layout, synchronized motion, or several layered sources. For a whole scene's visual layer built from the presenter's own recording, compose one screen-source video with `scripts/compose_screen_source.py` and make it the scene's screen layer.

This skill owns editorial selection, A-cam/B-roll composition, and the acceptance loop. Companion skills own their technical contracts.

## Establish the edit contract

Resolve these from the user's request or inspectable project state before editing:

- target intro range;
- A-cam and narration source;
- transcript or timed spoken content;
- available B-roll, screenshots, slides, outputs, and prior-video footage;
- supplied reference video or style target;
- protected material, including audio, existing cuts, or surrounding timeline content.

Ask one short question only when a missing answer would materially change the edit. Preserve the original sources and work on the smallest requested range.

Inventory the complete user-authorized source pool before choosing visuals: the full current Project, attached asset folders, reusable footage later in the video, and permitted prior videos. Index useful moments by transcript claim, source time, visual role, and whether the clip contains motion or only a still result.

When the user supplies screenshots of moments (a Heptabase card, a doc, a folder), treat every screenshot as a pointer into their own recording or a card to show, download all of them, open all of them, and locate each moment by the words being spoken at that time rather than by any timestamp printed on the screenshot; timelines get trimmed after screenshots are taken.

## Build the visual beat map

Read [references/editorial-playbook.md](references/editorial-playbook.md), then map each semantic narration beat to visible proof.

For each beat, record:

- exact Project-time range;
- spoken claim;
- chosen visual and source (for the presenter's own recording: source project time, media id, and media offset);
- why it proves the claim;
- presentation mode: `fullscreen`, `a-cam-pip`, `split`, `graphic`, or `a-cam-reset`;
- source in/out points and any speed change;
- important UI, faces, hands, or labels that must remain visible.

Treat every spoken claim as a continuous coverage interval. Proof may change inside it, but the visual and layout must stay intentional from the first content word through the semantic handoff. Bridge words such as “so,” “and then,” and “because” must inherit a planned proof or a deliberate A-cam reset—never an accidental B-roll or layout gap.

Write the map as a table the user can approve (time, spoken line, visual, source, motion) and keep it updated to what actually plays; the next critic works from it.

Use `scripts/validate_beat_map.py --require-continuous` when the beat map is JSON. Repair overlaps, invalid ranges, missing proof, and accidental source repetition before building the edit.

## Select proof in this order

1. A moving result or completed output named by the speaker.
2. A before/after or problem/solution comparison.
3. A real interface action that directly demonstrates the claim.
4. User-owned footage from elsewhere in the current or prior video.
5. A supplied slide, screenshot, or diagram with purposeful motion.
6. A purpose-built visualization when no real proof exists.

Two cases the presenter has ruled on (see `references/samin-rules.md`):

- A line that is a feeling or a story ("there have been days…", "the only option was to upgrade", "nearly impossible to charge clients") gets a Higgsfield clip of the presenter acting exactly those words (his Soul → a still → Seedance `omni_reference`), starting on the line's first word. The action beats land on the words. Read every generated frame like a person; fix text on the still before animating, and object state with a `video_edit` pass. `examples/higgs-api-intro/ai-clips/prompts.md` holds the working prompts.
- "Levels" is shown in his levels style (`scripts/levels_style.py`, spec in `examples/higgs-api-intro/levels-spec.json`): three blue circles pop on the white grid just before the word, then each level gets its numbered circle, bold italic title, and its own math or strategy graphics flashing inside a dark device mock.

The cold open is the moment he names. A timestamp from him means the clip playing on screen at that time; find its native file. Never open on a smoking or vice shot, even from his own generations.

Do not treat an asset folder as a slideshow. Choose clips because they prove the sentence, not because they are available.

Motion is non-negotiable for later-footage proof. Raw Borumi screen media has no cursor; render the range through Borumi (screen-only export) so the cursor, box-drawing, scrolls, and clicks are baked in. A still may stand in only with one motivated push, and never two stills in a row.

## Compose the presenter and B-roll

- The asset fills the frame; the presenter is a custom-layout source drawn last, bottom-right, at the measured rect in `references/samin-treatment.md`. The presenter window is never covered, never resized per slot, never vignetted. Overlays in Borumi render above the camera, so a full-frame overlay is never the vehicle; the composed proof video becomes the scene's screen layer instead.
- Keep the object of the sentence out from under the presenter window: crop or nudge the source so the last bar, the label, or the output node stays visible. When the subject lives bottom-right (an object in the presenter's hand), re-fit the card on the left or punch in for the last second of the beat (a `seq` with a cropped second part).
- A generated clip may run slower or faster to cover its line (`speed` on a `clip` part: 0.81x let the limit clip span the whole sentence, 1.22x tightened the upgrade clicks). Keep the action beat on its word.
- Use a clean crop of the presenter once. Never place a new card or border around a crop that already contains a framed PiP.
- Return briefly to full A-cam at a major idea change or when the viewer needs a visual reset.
- Promote screen recordings to readable size: crop to the proof region (a table, the right two-thirds of a chart, the top row of a grid where labels are readable) and scale to fill.
- Start interface clips on motion or on the decisive state, after setup clicks, never on a loading skeleton or a chat pane.
- Speed up dead interaction time only; keep the meaningful action legible.
- Text cards (tweets, posts, results pages) are centered and big on near-black, cropped to the words plus the one element that proves the point, with a slow push; a results page pans. No line runs under the presenter window.
- Later-footage B-roll carries the "this is from later" marks: a slight vignette and a thin line near the bottom, values in `references/samin-treatment.md`.
- When one sentence contains two visual subclaims, cut at the spoken clause boundary: establish the context first, then show the decisive action. Do not split at an arbitrary time midpoint.

The first frame of every proof beat should answer: “What am I looking at?” The final frame should answer: “What changed or why does it matter?”

## Pace the intro

- Match a supplied reference's measured cadence and density, treating them as a ceiling. Prefer fewer, longer, legible holds; never add cuts, layers, or motion merely to make the hook feel busy.
- One visual per spoken clause; every cut leads the spoken word by about 120 ms so the eye lands before the ear.
- When the hook promises N use cases or examples, preview N distinct micro-beats when real evidence exists. Reveal them in narration order, use optional one-to-four-word labels, then settle briefly on the complete map before the deep dive. Do not reuse one UI shot to imply several use cases.
- Cut on a new claim, result, example, or visual world—not merely to hit a fixed duration.
- Let later explanation beats hold longer, but keep internal action alive.
- Avoid repeating the same source or framing in adjacent beats unless the second beat reveals a genuinely new result.
- After a rapid cluster, use one calmer hold or A-cam reset so the viewer can absorb the point.
- Render slot clips at 60 fps so re-cut boundaries do not drift. Assemble the layer with `scripts/assemble_scene_layer.py`: every slot boundary lands on `round(end_ms × fps / 1000)` and a slot that renders a frame short is padded by cloning its last frame, so the layer is exactly the scene length and later beats never slide.

## Preserve editorial truth

- Preserve narration and sync unless the user requests dialogue editing.
- Keep B-roll overlays silent unless their sound is explicitly part of the story.
- Do not invent metrics, customers, results, product behavior, or interface states.
- Treat third-party reference videos as style evidence. Do not reuse their face, camera, or audio without authorization.
- Keep labels short and subordinate to the narration.
- Never composite a screenshot that has the presenter's own player or camera baked into it.

## Edit in bounded ranges

1. Inspect the current timeline and surrounding cuts.
2. Build one coherent range or story cluster.
3. Render or stage it without disturbing protected audio or adjacent material.
4. Inspect the result at exact user-reported moments and across a broad contact sheet.
5. Keep the change only when it improves clarity, proof, and flow.

When replacing an existing composite, preserve its exact timeline range unless the user requested timing changes. Verify the first and last boundary frames so no flash, overlap, or gap is introduced. A take's duration extends a Borumi scene, so import a file that is exactly the scene length; never fix an overshoot with a ripple trim across edit sets.

When extracting later-project footage, keep a ledger with donor Project in/out, donor media in/out, desired Project in/out, expected media in/out, speed, and destination in/out. Run `scripts/validate_extraction_ledger.py` before moving the kept fragment. After staging, verify the donor is unchanged, the destination media offsets and duration match the ledger, scratch fragments are gone, and no source audio was copied. When the donor footage is exported through temporary fullscreen layouts, remove those layouts and restore any changed layout in a follow-up commit before delivery.

## Run the gauntlet

Read [references/gauntlet.md](references/gauntlet.md) and judge with [references/rubric.md](references/rubric.md); run the complete finite worklist before delivery. Cut the critic packet from the export with `scripts/make_critic_packet.py`. Use `scripts/analyze_intro.py` on the final render to generate metadata, scene-cut evidence, black-frame findings, and a contact sheet.

When fresh critics are available, run the critic round described in `references/gauntlet.md`: cut three-frame strips per slot from the export, have three independent critics (proof accuracy, legibility and motion, sync and pacing) judge against the beat map with frame citations, merge and rank the findings into exact fixes, apply them, and verify with a second pass. Stop when no material finding is left; two rounds were enough on the reference edit.

A timeline plan or metadata-only check is not acceptance evidence. Before commit, render or capture the staged affected window, inspect a broad contact sheet, watch the motion, and inspect one frame before, at, and after every replaced boundary. Rendered pixels and timeline metadata must agree.

Stop with one of these honest outcomes:

- `success`: every required gate passes;
- `clean-no-op`: the requested result already exists;
- `blocked`: required source or tool access is unavailable;
- `approval-required`: the next action exceeds the user's authority;
- `no-progress`: another pass would not measurably improve a failed gate.

Never report a render or tool error as success.

## Deliver

Return:

- the committed Borumi change or editable composition path;
- the final render when one was produced, plus a phone-sized copy when the user reviews on a phone;
- the beat map as built, a contact sheet or saved inspection evidence, and the critic receipts;
- actual duration, resolution, frame rate, and streams;
- a compact gauntlet receipt naming passed gates and any unresolved limitation, including anything in the source footage the edit cannot fix.

## Resources

- `references/samin-treatment.md` — the approved look: presenter rect, full-frame proof, vignette and line values, text-card sizing, rhythm, and what the presenter rejected.
- `references/samin-rules.md` — the presenter's notes in his own words (Fable 5.1 and Higgs API) and the standing rules they add up to.
- `references/rubric.md` — the gates a cut must pass, the critic sheet, and the verdict vocabulary.
- `examples/higgs-api-intro/` — the second approved hook: the cut, beat map, plan, levels spec, the three Soul clips with their prompts, QA receipts, and the exact scripts.
- `references/borumi-proof-pipeline.md` — the validated Borumi MCP route: session, guides, transcript-to-media mapping, screen-only b-roll export, screen-source swap, layout re-add, export.
- `references/editorial-playbook.md` — visual selection, layouts, pacing, and failure patterns.
- `references/gauntlet.md` — bounded QA loop, acceptance gates, and the multi-critic round.
- `scripts/borumi_mcp_session.py` — persistent Borumi MCP stdio client for hosts that cannot add an MCP server mid-session.
- `scripts/compose_screen_source.py` — composes slot videos from a JSON slot plan with the treatment applied (kinds: broll, clip, raw, tweet, still, pan, black, seq with per-part `dur`, `crop`, `speed`).
- `scripts/assemble_scene_layer.py` — renders every slot (hash cache) and concatenates them into the exact scene-length layer.
- `scripts/levels_style.py` — renders the levels intro and per-level pieces from a spec.
- `scripts/make_critic_packet.py` — contact sheet plus three-frame strips per beat from the export.
- `scripts/validate_beat_map.py` — validates timed beat-map JSON.
- `scripts/validate_extraction_ledger.py` — checks donor-to-destination trim and media-offset arithmetic.
- `scripts/analyze_intro.py` — probes a render and creates objective QA artifacts.
