# Borumi proof pipeline

The exact, validated route (2026-09-01, Borumi 0.30.5) for turning the presenter's own recording into a motion-first proof layer without re-recording anything. Follow it in order. Every step was run on a real project; the gotchas are the ones that actually bit.

## 0. What the user hands you

- A script for the scene (often a Heptabase card or a doc) and **screenshots of moments** from the user's own recording. Each screenshot is a timestamp into that recording (the player time is usually visible) or a tweet/page to show. Download every image and open every one. The screenshots are the index; nothing gets visualized that is not on it unless the user asks for "variety."
- The recording lives in Borumi: `<Projects dir>/<name>.bmprojbundle/` with `project.bmproj` and `medias/` (one UUID-named `.mov`/`.mp4` per captured track per take; screen tracks are captured at native display size, camera at 1920×1080).

## 1. Talk to Borumi through its MCP, persistently

Borumi ships an MCP server: `/Applications/Borumi.app/Contents/MacOS/borumi mcp` (stdio JSON-RPC). The app must be open with the project loaded.

- If the agent host cannot add an MCP server mid-session, run `scripts/borumi_mcp_session.py start` (a FIFO daemon that keeps one connection alive) and call tools with `borumi_mcp_session.py call <tool> '<json>'`.
- **Guides gate tools per connection.** First call `get_guides` with no arguments, then fetch each guide you need **one id at a time** (`project_edits`, `editing`, `importing_media`, `editing_layouts`, `editing_transitions`, `exporting`, `editing_segment_<type>_add|update`, `ui_navigation`). A batched request over ~30 KB is refused and registers nothing.
- Every content change is a transaction: `begin_project_edit` → hash-guarded edits → `inspect_timeline` with the `tx_id` → `commit_project_edit` with a one-sentence summary, or `abort_project_edit`. Re-read the `timeline_hash` after every structural change.

## 2. Map the recording before touching it

- `get_project_overview` and `get_scenes`: scene ids and bounds; scene scripts live here.
- `get_transcript` with `range {start_ms,end_ms}` per scene (a whole-project read is refused): word-level ms. This is the timing source for every cut.
- `get_timeline` with `detail:"segments"`, `layers:["screen_1"]`, `segment_fields:["media"]`: each segment carries `media.media_id` and `media.start_ms`. **Media id = the first four hex characters of the UUID filename in `medias/`**, and `media_time = media.start_ms + (project_time − segment.start_ms)`. That turns any project time into an exact file and offset.
- Find each proof moment by **what the presenter was saying** (grep the transcript for the claim's words), then confirm the visual with `inspect_timeline` (`view:{type:"layer_source",layer_id:"screen_1"}`, `presentation:"contact_sheet"`, `quality:"low"`). Do not trust timestamps written on old screenshots; the timeline has usually been trimmed since.

## 3. Get motion, not stills

The raw screen `.mov` files contain **no cursor**. The cursor lives in a `.cursor` sidecar that Borumi composites at render time, so an ffmpeg pull from `medias/` is a static screen with nothing moving. Get the motion from Borumi:

1. In one transaction, add a `layout` segment of kind `fullscreen` (`layer_id:"screen_1"`, `fit:"cover"`, `transition:{kind:"instant"}`) over each proof range. A fullscreen layout hides the camera. If a range already has a custom layout, read its `properties`, `update_segments` it to fullscreen, and restore the saved properties later. Commit.
2. `export_video` each range with `range:{type:"time",start_ms,end_ms}` and `settings:{type:"custom",width_px:1920,height_px:1080,fps:30}`; poll `get_export_status` no faster than `poll_after_ms`. The result is the screen alone, cursor, box-drawing, scrolls and clicks baked in.
3. In a second transaction delete the temporary layouts (`expand_groups:false`, `ripple:false`), restore any changed layout, commit. The project is back to its previous state.

Pick ranges where something visibly happens: the box gets drawn, the page scrolls, the cursor lands on the thing named. Start the clip on motion or on the decisive state, never on a loading skeleton or a chat pane. Qualify every candidate with dense frames before using it.

## 4. Compose one screen-source video

Build the whole scene's visual layer as a single 1920×1080 video the exact length of the scene (`scripts/compose_screen_source.py` with a slot plan). Treatment rules are in `samin-treatment.md`. Two ffmpeg facts that cost time when missed: put `fps=` **before** `zoompan` or the clip runs short, and use `-framerate 30 -loop 1` for stills. Render slot clips ~150 ms longer than their slot and trim at concat; finish with `-t <scene length>`.

## 5. Put it in the screen layer, not an overlay

- **Overlays render above the camera.** A full-frame `media_overlay` hides the presenter; a panel overlay leaves the desktop recording visible around it and that recording drifts because Borumi's cropped screen follows the cursor. Neither is acceptable.
- Instead: in a transaction, `import_media` the composed video; delete the scene's `screen_1` segments (`expand_groups:false`, `ripple:false`); `add_segments` a `take` at `at_ms:0` with `content:{media_id, video_kind:"screen"}`; set the new clip's `face_tracking_mode` to `disabled`; then **re-add the custom layout** (deleting the screen segment drops any layout that referenced it): kind `custom`, sources `[screen_1 full frame, camera_1 bottom-right]`, camera last so it draws on top. `inspect_timeline` the render with the `tx_id`, then commit.
- A take's duration extends the scene. Import a file that is exactly the scene length; a frame-rounding overshoot of one frame is harmless, but do not fix an overshoot with a ripple trim across edit sets (it eats the start of the next scene).

## 6. Export and check

`export_video` with `range:{type:"scene",scene_id}` and preset `balanced` (1080p60 H.264). Make a contact sheet and per-slot three-frame strips (start / middle / end) from the export and run the critic round in `gauntlet.md`. Ship a 720p copy as well when the user reviews on a phone.

## Receipts to keep in the project folder

`scene-index.md` (slot map: time, spoken line, visual, source project time), `broll/` (the screen-only exports), the slot plan and compose script, `borumi/` (tool list, guides, transcripts, timeline maps, render sheets), the critic JSON per round, and the Borumi commit ids.

## Gotchas added on the Higgs API build (2026-09-19, Borumi 0.30.x)

- Borumi quits on its own during long sessions: every tool call then fails with `app_not_running`. `open -a Borumi`, wait ~12 s, and confirm with `list_open_projects` before any transaction; export jobs die with it.
- Adding a layout over a range splits the layouts under it; after deleting a temporary layout the pieces are gone. Record the original layouts' ranges and properties first and re-add them over any uncovered piece before committing (`examples/higgs-api-intro/scripts/export_end.py` does this).
- Delete temporary layouts one call at a time; a single `delete_segments` over many ids fails with `project_operation_failed`.
- A take placed exactly on a scene boundary can land in the previous scene; place at `start_ms + 1`.
- `update_scenes` takes `updates: [{scene_id, name}]`, not `scenes`.
- Import a layer that is exactly the scene length in frames (5001 frames for an 83.355 s scene at 60 fps). One slot rendering a frame short shifts every later beat; `scripts/assemble_scene_layer.py` pads short slots by cloning their last frame.
- A full-project export omits `range`; a 4K master is `settings: {type: "custom", width_px: 3840, height_px: 2160, fps: 60}` and runs at roughly real time.
