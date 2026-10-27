# visualize-a-cam-intros

Turn a talking-head intro into a proof-first visual story: the presenter stays pinned on top, bottom-right, while every sentence gets real motion from the presenter's own recording (cursor, boxes, scrolls), centered text cards, and a slight vignette plus a thin line on anything pulled from later in the video. Built for Borumi projects, with a multi-critic QA loop before delivery.

## Install

It's already in this course: open the course folder in Claude Code and the skill is there. To use it in any other project:

```bash
cp -R .claude/skills/visualize-a-cam-intros ~/.claude/skills/
```

## Use

- Claude Code: `/visualize-a-cam-intros` then describe the scene, or say "visualize scene one with this skill."
- Codex: `$visualize-a-cam-intros`.

Give the agent: the Borumi project (open in Borumi), the scene to visualize, and your screenshots or notes of the moments to show. It reads everything, maps each spoken line to proof, renders the motion through Borumi, composes the scene's screen layer, pins your camera on top, runs the critic round, and hands back the export plus the beat map.

## What's inside

- `SKILL.md` — the workflow agents follow.
- `references/samin-treatment.md` — the approved look, with numbers.
- `references/samin-rules.md` — Samin's notes in his own words and the standing rules.
- `references/rubric.md` — the gates, the critic sheet, and the verdicts used to judge an intro.
- `references/borumi-proof-pipeline.md` — the validated Borumi MCP route.
- `references/editorial-playbook.md`, `references/gauntlet.md` — selection rules and the QA loop (including the three-critic round).
- `scripts/borumi_mcp_session.py` — persistent Borumi MCP client for hosts that cannot add an MCP server mid-session.
- `scripts/compose_screen_source.py`, `scripts/assemble_scene_layer.py` — render the slot plan and assemble the exact scene-length layer.
- `scripts/levels_style.py` — his levels treatment (circles, numbered level cards with a device mock).
- `scripts/make_critic_packet.py` — the critic packet cut from the export.
- `examples/higgs-api-intro/` — the Higgs API hook: cut, beat map, plan, prompts, receipts, scripts. (The videos and images are left out of the course copy to keep it small.)
- `scripts/validate_beat_map.py`, `scripts/validate_extraction_ledger.py`, `scripts/analyze_intro.py` — checks.

Reference builds: the Fable 5.1 hook (2026-09-01) and the Higgs API hook (2026-09-19, in `examples/`).
