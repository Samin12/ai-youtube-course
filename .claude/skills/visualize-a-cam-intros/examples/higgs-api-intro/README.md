# Higgs API hook (approved 19 Sep 2026, version 10, Borumi commit `9410`)

The second approved reference for this skill, after the Fable 5.1 hook. Scene 1 of Samin's Higgsfield API video:
83.355 s of A-cam turned into a proof layer with his camera pinned bottom-right. Watch `intro-v10-720p.mp4` first,
then read `beatmap-lines.txt` next to it.

## What is here

| Path | What |
|---|---|
| `intro-v10-720p.mp4` | the approved cut, phone copy (1080p60 lives in Borumi) |
| `beatmap-lines.txt`, `beat-map.json` | 16 beats: spoken line, visual, source, why it proves the line |
| `plan.json` | the slot plan `scripts/compose_screen_source.py` rendered (paths relative to this folder; `broll/` are screen-only Borumi exports you regenerate with `scripts/export_broll.py`, `native/` is his STORM file) |
| `levels-spec.json`, `levels/` | the levels treatment: circles intro plus one piece per level, rendered by `levels_style.py` |
| `ai-clips/` | the three Higgsfield clips of Samin used in the cut, their start images, and `prompts.md` |
| `assets/` | the savings card (padded left so it clears the camera), the Explore Cheaply card, the hoodie pair |
| `qa/` | contact sheet and analysis of the export, the word-timed transcript, critic round 1, verifier round 2, the punch-in and opening frame checks |
| `scripts/` | the exact scripts of this build (`ship.sh` = assemble → commit → export → analyze → packet → 720p) |

## The beats

| Time | He says | It shows |
|---|---|---|
| 0.00–4.84 | "I spent an unhealthy amount of time and money creating AI images and videos with Higgsfield" | his STORM recast at the start of the motion (crowd drops, he stays standing), then his AI double dancing in the hoodie pair |
| 4.84–8.47 | "I gotta get this off my chest. Their usage limits suck." | full camera (reset) |
| 8.47–15.40 | "There have been days where I've prompted once or twice, and boom, there goes my limit…" | Soul clip: he types, the red "Daily limit reached" banner pops on "boom", hands to head on "there goes my limit" (played at 0.81x to cover the line) |
| 15.40–21.07 | "…nearly impossible to calculate generations and charge clients…" | Soul clip: a client asks "How much does it cost?", question marks over his head, shrug on "client work" |
| 21.07–27.02 | "the only option you had was to upgrade, pay for a bigger plan, with limits I might not even use" | Soul clip from behind: he clicks Upgrade three times, opens his wallet, empty; punch-in on the wallet for the last 1.3 s |
| 27.02–33.61 | "instead of paying for a plan… ten times more efficient" | savings card ($49 → $8.40), then Which Model, Explore Cheaply, the higgsfield-api-studio README, the open-higgsfield repo |
| 33.61–37.97 | "only pay for what I generate… clients on my own platform" | the Codex cost receipt line, then the Samin Studio board |
| 37.97–44.55 | "everything I learned generating for hundreds of clients" | the avatar remake playing, the before/after hoodie page |
| 44.55–45.97 | "…three levels" | three blue circles pop on the white grid |
| 45.97–67.78 | level one / two / three lines | level card with circle, italic title, and the level's own graphics inside the device mock |
| 67.78–72.61 | "track all the costs… clients cover their own generations" | the README cost table, then the API-key form |
| 72.61–75.25 | "you get paid for the expertise behind it" | the "Now the connection becomes useful" slide |
| 75.25–78.76 | "even if you've never touched anything technical" | full camera (reset) |
| 78.76–83.36 | "all we're doing is simply speaking to ChatGPT" | Codex's plain-English reply pushing into frame |

## How it was built

1. Word-timed transcript of the scene; beat map written as a table he could approve.
2. 18 cursor-baked screen ranges exported from later in the recording through temporary fullscreen layouts
   (`export_broll.py`), plus one late-video range for the cold open (`export_end.py`, later replaced by the native file).
3. Three Soul clips generated with Higgsfield (Soul still → Seedance 2.5 `omni_reference`, 6–8 s, 16:9, 720p, no audio);
   text fixed with a GPT Image 2.5 edit or a PIL composite on the still; the wallet emptied with a `video_edit` pass.
4. Levels pieces rendered with `levels_style.py` from `levels-spec.json`.
5. One 5001-frame screen layer assembled from the plan (`assemble.py`), inserted as the scene's screen take with the
   camera layouts re-added (`insert_intro.py`), exported, analyzed, and cut into a critic packet (`make_packet.py`).
6. Ten committed versions: d6a8 → 6162 → f994 → c508 → 1010 (his five mid-edit notes) → 72f2 → b2bf → 934b → a5fc
   (his four review notes) → 9410 (the cold open he pointed at). Three critics ran on v1, a verifier on v2, and every
   version was checked frame by frame on the export.

His notes and what each one changed are in `references/samin-rules.md`; the gates are in `references/rubric.md`.
