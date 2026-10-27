# Intro Visualization Gauntlet

Run this finite worklist on the staged edit or final render. Repair one highest-value failure at a time, then rerun the affected checks. Stop at success or when a named terminal condition applies.

## Pass 1: Editorial coverage

- The opening promise is visible, not only spoken.
- Every major claim in the requested range has a matching proof beat.
- Every advertised use case appears once in the rapid preview when real source proof exists.
- Transcript coverage has no unplanned visual or layout gap, including bridge words between claims.
- The visual actually demonstrates the claim; it is not merely topic-adjacent.
- Adjacent beats vary by source, visual role, scale, or motion language.
- The same footage is not repeated unless it reveals new information.
- The edit contains at least one attention reset after a dense sequence when the narration allows it.

Evidence: compare the timed transcript or beat map with a broad contact sheet.

## Pass 2: Framing and readability

- Each proof beat establishes what the viewer is looking at before moving closer.
- Interfaces retain enough context to understand the action.
- Comparisons show both states at a readable scale with breathing room.
- Essential faces, labels, controls, and results are not cropped or covered.
- Full-screen proof is the readable-evidence default; any 22–27% corner PiP is limited to an intentional question or progress beat.
- The presenter PiP is stable, cleanly cropped, and not double-framed.
- The PiP moves, hides, or yields when it obstructs the proof.

Evidence: inspect exact high-quality frames at the start, emphasis point, and end of every major layout.

## Pass 3: Motion and pacing

- Setup clicks, cursor hesitation, loading, and dead interaction time are trimmed.
- Every interaction claim contains visible state change: a scroll, selection, file open, tool action, touch, cursor response, transformation, or result.
- The decisive action or result remains long enough to understand.
- Still images have one purposeful motion treatment.
- Motion settles before text or a comparison must be read.
- No black, blank, frozen, or accidental flash frames appear at boundaries.
- A rapid cluster is followed by a calmer hold when appropriate.

Evidence: use two views. Scan a broad contact sheet for coverage and variety, then use dense frames or real-time playback to prove motion. Inspect a frame triplet immediately before, at, and after every replaced boundary.

## Pass 4: Audio and continuity

- Original narration remains synchronized and intelligible.
- B-roll overlays are silent unless their audio is explicitly required.
- No typing, click, transition, or source audio leaks into the mix unintentionally.
- The replacement begins and ends on the intended Project-time boundaries.
- Content before and after the edited range remains unchanged.
- For reused later-project footage, the extraction ledger agrees with the staged edit: donor Project and media ranges, desired range, speed, expected media offsets, destination range, and duration all reconcile.
- Donor segments remain unchanged, scratch fragments are removed, and no source audio or linked group member was copied unintentionally.

Evidence: compare source and staged timeline ranges, destination media offsets, segment/group membership, scratch space, boundary frames, and audio streams.

## Pass 5: Technical render

- HyperFrames lint/check reports no errors or warnings when HyperFrames is used.
- Runtime, layout, motion, and contrast checks pass.
- Required media resolves locally without a network dependency.
- The output plays from start to finish.
- Rendered pixels and timeline metadata agree at every changed beat; a structurally valid segment that displays the wrong source moment fails this gate.
- Resolution, frame rate, duration, codecs, pixel format, and audio streams match the delivery contract.
- `scripts/analyze_intro.py` reports no unintended black segments.

Evidence: retain command output, metadata JSON, and the generated contact sheet.

## Repair order

Choose the first failing category in this order:

1. missing or misleading proof;
2. unreadable framing or occlusion;
3. dead pacing or repeated source;
4. unintended audio or sync drift;
5. technical render failure;
6. decorative polish.

Make one bounded repair, rerender only the affected range when possible, and rerun that gate plus the boundary checks. Continue until all gates pass or another pass produces no measurable improvement.

## Receipt fields

Record:

- scope and exact timeline range;
- source state or commit inspected;
- checks and conditions;
- failures found;
- repairs kept;
- final result: `success`, `clean-no-op`, `blocked`, `approval-required`, or `no-progress`;
- evidence paths or Borumi commit ID.

## Critic round (multi-agent, run before or instead of a solo gauntlet when fresh critics are available)

Adapted from the Loop Library capture-and-critic pattern (#021). Validated on the Fable 5.1 hook, 2026-09-01: round 1 returned 13 frame-cited findings, round 2 confirmed 10 resolved and found one blocker, round 3 was not needed.

1. Cut evidence from the actual export, never from the plan: a contact sheet (one frame every 2 s) and a three-frame strip per slot (start +50 ms, middle, end −80 ms).
2. Give three fresh critics the same packet: the user's brief verbatim, the beat map, the word-timed transcript, the user's reference screenshots, the strips and the sheet. One lens each:
   - proof accuracy and intent: is this the marked moment, is it the strongest proof for the words at that ms, is it readable without narration;
   - legibility and motion: text size at 1080p, crop tightness, dead space, empty or half-built frames, real motion versus a freeze, presenter window unobstructed;
   - sync and pacing: does the visual arrive on its sentence, slots too short or too long, calm versus busy, exact boundary moves in ms.
   Every finding must cite the image and give one concrete fix (crop numbers, ms, a different source moment). No praise padding.
3. A synthesizer merges the three lists, drops anything not backed by a cited frame, keeps disagreements only when both sides cite frames, and ranks by proof clarity, then legibility, then pacing. Output: an ordered fix list plus a verdict of `ship`, `fix-then-ship`, or `rework`.
4. Apply the fixes as one bounded rebuild, re-export, and run one verifier over the same packet plus the fix list: it reports each prior item as resolved, partly, open, or superseded, adds anything new, and checks the brief line by line (presenter on top everywhere, assets full frame, motion not stills, text centered, treatment marks present but slight).
5. Stop when the verifier has no blocker or major left; minor items ship with a note. Keep both rounds' JSON as receipts next to the render.
