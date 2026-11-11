# ARIS / SuperARIS reference discussion — accepted direction

Gemini thread `f7da0d0f-54dd-42a7-9244-b8cca40c5a29`, continuation returned SUCCESS, selected Gemini 4 Argon (High), high. This is Root's disposition of the actual response, not a verbatim model transcript. The model read the two supplied reference snapshots in this directory.

## What to implement

- Follow SuperARIS's short explanatory paragraphs, early runnable entry and reader-intent links into docs. Borrow ARIS's actual skill/workflow routes and collapsible version history. Avoid reproducing the badge/news density.
- README: concise product introduction and navigation; six meaningful result summaries; actual quick start; clear three-layer diagram; short explanation of research feedback; docs links. Match English/Chinese organization.
- Use a single overview of all six results (prefer the case-study index if implementation already chose it); do not create competing docs/RESULTS.md and case-studies/README.md that duplicate a second results ledger. Link to existing per-topic sources for full methods, proof scope, and reproduction.
- Preserve all base/plugin/case/archive paths. A stable local homepage entry may point to the actual existing source; no mass relocation. Keep old v2/v3 pictures as historical assets.
- The new architecture figure has no version in its title. README uses the editable SVG. The GPT Image alternative belongs to the figure gallery, so the same content is not repeated twice in the main page.

## Root corrections to Gemini's latest draft

The proposed reading order and source separation are accepted. Its claimed approximately 610-word full draft is visibly longer and its result bullets still contain too many audit details. Do not treat that word count as checked or paste the dense draft wholesale. Retain good Gemini wording and shorten using the intended split:

- Each result in README: result + why it matters + direct scope/detail link. Keep working-manuscript status beside Happy Ending. Detailed import premises, rank counts, formal C review state, and execution provenance belong in the results overview/details.
- The ECC A/B/C example caveat belongs where the example is shown; it need not interrupt the README result sentence.
- No full-domain result should be presented as certified merely because an example replay passed. Preserve exact known scope in the linked details.
- Maintenance learns from **research evidence**, including failures and partial work, not only completed research. The model's table row saying 'from completed research' must be corrected.
- Quick start should let users run a bounded example and then give a short real task. Long recovery/helper instructions belong in the full guide.
- Keep six-domain methods and quantities accurate; avoid making mathematical preservation a software-enforced guarantee or claiming measured autonomous speedups.

## Additional figure request

User now invites additional figures where they help GitHub readers. Root is preparing one additional compact figure explaining research evidence → separate maintenance → stronger Base / deeper plugins, with actual sourced examples. It must add explanation rather than repeat the architecture. Reserve a place in the evolution section but do not ship a placeholder. Root will supply the finished asset. Six-domain result plots stay in result/case entrances instead of six large images in README.
