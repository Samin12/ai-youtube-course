# Rubric: judging an intro

Judge the export, never the plan. Every finding cites a frame (a strip or contact-sheet tile with its time) and names
one concrete fix. Verdicts: `ship`, `fix-then-ship`, `rework`. Samin's own notes on the cut override any line here.

Reference points are the two approved hooks: Fable 5.1 (1 Sep 2026, `samin-treatment.md`) and Higgs API
(19 Sep 2026, `examples/higgs-api-intro`). Where a number appears below it is what those cuts measured, not a target
he set; use it to notice drift, not to pad or trim a cut.

## Gates (pass / fail, in repair order)

| # | Gate | Passes when | Check with |
|---|---|---|---|
| A | Opening | The first frames show the moment he named (or the strongest proof), the camera is already pinned bottom-right, and there is no smoking or vice shot. | `x-0.05s` frame and the first contact tile |
| B | Coverage | Every spoken clause from 0 ms to the end has a planned visual; bridge words inherit a proof or a deliberate A-cam reset; no accidental gap, black, or freeze. | beat map vs transcript; `analyze_intro.py` (black and freeze segments must be empty) |
| C | Literal match | A line that names a feeling or a story shows him doing exactly that (Soul clip), starting on the line's first word, with the action beat on the word it belongs to. | the strip of that beat plus the word timings |
| D | Proof, not topic | Each visual proves the sentence: the strategy slide for the strategy line, the repos for "repos", the cost line for "what it cost", the working product for "platform". Topic-adjacent footage fails. | contact sheet vs beat map |
| E | Levels | Circles pop before the word "levels"; each level has its blue circle, italic title, and a device mock with the level's own graphics flashing inside it. | strips of the level beats |
| F | Legibility | Nothing the sentence is about sits under the camera window (x ≥ 0.775, y ≥ 0.715 of the frame). Text that must be read is about 18 px or larger at 1080p. AI-rendered text is spelled correctly. Crops drop browser chrome and half-words at the edges. | full-size frames at start, emphasis and end of each beat |
| G | Motion | Every beat has real motion (cursor, scroll, playback, a person moving) or one motivated push on a still; never two stills in a row; no paused player; later footage carries the vignette and the bottom line; pushes glide (perspective remap, never zoompan). | dense frames or playback; frame-difference check on suspected freezes |
| H | Rhythm | One visual per clause; cuts lead the word by about 120 ms; a calm hold or A-cam reset follows a dense run. Approved cuts measured 27 cuts in 83 s (Higgs API) and 2.4–6.5 s slots (Fable). | `analyze_intro.py` cut list vs word timings |
| I | Truth | No invented UI states, numbers or results; narration untouched and in sync; the camera never covered, resized or vignetted; treatment marks present but slight. | boundary frames; audio stream unchanged |
| J | Receipts | Beat map as built, contact sheet, strips, critic JSON, Borumi commit id, and a 720p phone copy are delivered. | the delivery folder |

## How to run it

1. Cut the packet from the export with `scripts/make_critic_packet.py` (contact sheet plus a three-frame strip per beat).
2. Three fresh critics, one lens each (proof and intent; legibility and motion; sync and pacing), each fill the sheet
   below against the beat map and the word-timed transcript. No praise padding.
3. A synthesizer merges the sheets, drops anything without a cited frame, ranks by the gate order above, and returns
   the fix list with a verdict.
4. Apply the fixes as one bounded rebuild, re-export, and run one verifier over the same packet plus the fix list. It
   marks each item resolved, partly, open or superseded, and re-reads Samin's notes line by line.
5. Stop when no blocker or major item is left. Minor items ship with a note.

## Sheet (one per critic, JSON)

```json
{"critic": "proof | legibility | pacing",
 "verdict": "ship | fix-then-ship | rework",
 "gates": {"A": "pass", "B": "pass", "C": "fail", "D": "pass", "E": "pass", "F": "pass", "G": "pass", "H": "pass", "I": "pass", "J": "pass"},
 "findings": [
   {"beat": 5, "gate": "F", "severity": "major", "evidence": "strip-05.jpg [end] 26.9s",
    "problem": "the open wallet's lower third sits under the camera window",
    "fix": "punch in for the last 1.3 s: crop=900:506:382:212 so the wallet clears y 0.715"}
 ]}
```

Severity: `blocker` (a gate fails on the thing the sentence is about), `major` (a gate fails elsewhere), `minor`
(polish). A verdict of `ship` requires no blocker and no major.
