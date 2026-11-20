# Six-result README overview

Editable bilingual SVGs and actual 900px PNG previews for the GitHub results section. Each is 900 × 934, white background, two columns × three rows. PNGs were rendered with Chromium and visually inspected at native 900px width in both languages.

- `results-overview.en.svg` / `.png`: English.
- `results-overview.zh.svg` / `.png`: Chinese.
- `render.py`: standard-library SVG generator; optional Playwright Chromium step renders both PNG previews.
- `data.json`: domain names, pointwise gains, ECC ranges and DD comparisons. Remaining compact theorem/status wording and numberline constants are explicit in `render.py`.

From this directory, regenerate SVGs: `python3 render.py` (Python standard library only). Add `--png` to export PNG previews; this optional step requires Python Playwright and installed Chromium. Importing the module has no output side effects.

## Sources and adaptation

Repository-relative source: `development/homepage-redesign-20261105/site/result-visuals.js` (CONFIG pb/ecc/dd/e86/q6/he), plus that directory's `index.html` for current result/status wording and `styles.css` for the six domain colors. This derivative reuses those actual result motifs, not app.js's original problem illustrations. It is newly drawn vector layout, not a screenshot of cards.

- PB: linear pointwise gain plot, k5…12: 3,3,3,4,5,27,30,31. Raw lower bounds:35,67,131,267,543,1112,2275,4664. Uniform theorem covers every k≥12, adding Δ=floor(sqrt(B_RS)/(8(1+ln k))) to the accepted RS edge budget; the overview only states the scope. Detailed original: `case-studies/property-b/assets/delta.svg`.
- ECC: five parameter rows preserve prior/result intervals. (42,16) is marked as literature corollary; (45,11) stays open. Case index: `case-studies/README.md#error-correcting-codes`.
- DD: four showcased settings retain our best constructions: (10,4)=2,567, (11,5)=37,632, (12,5)=42,433, (16,4)=16,416. `settings` drives the overview; `rows` keeps the historical comparison and `latest` keeps the 2026-11-16 D5 follow-up data. Dates and public/local baselines stay in the case/reader rather than a common cross-setting gain scale. These four constructions are not a claim of current global records.
- E86: density upper ceiling0.60318 to <0.59155154. Linear numberline0.5…0.61 marks the new/prior ceilings;1/2 remains conjectural. Source: `plugins/hypercube-extremal/archive/source/START_HERE.html`.
- Q6 / Q7: the Q7 panel presents the complete author working proof covering every matching (source accepted 2026-11-19; external peer review pending; no Lean), alongside the retained Q6 theorem and ≤6-direction consequence using prescribed-endpoint P6 and published lifting results. Q7 research used v3 local adaptation; v6 main incorporates the full R7 proof on 2026-11-20. Fixed v5 ≥57-edge and v6 ≥56-edge snapshots remain historical. Sources: `case-studies/ruskey-savage-q7/README.md` and the proof/replay links below.
- HE:78→77 compares the same ES(7) upper threshold;77 is not claimed exact. Working-manuscript and review-pending status remain visible. Source: `case-studies/happy-ending/n7-20261103/figures/bounds.svg` and `case-studies/happy-ending/README.md`.

This is presentation work, not new mathematical verification or changed proof acceptance. Link the full overview to the six-case index so detailed proof and verification scopes remain available.

From the repository root, run `python3 figures/mathrsi/results-overview/render.py` (or add `--png`). Both READMEs link their language-specific SVG to the six-case index. Root inspected and approved the supplied figures; later updates retain their dated comparisons and original verification status.

## Q7 main follow-up · 2026-11-20

The Q7 panel now shows the complete author working proof for every matching, accepted in the source project on 2026-11-19. External peer review is pending and no Lean proof is supplied. The Q6 theorem and six-direction corollary using prescribed-endpoint P6 and published lifting results remain. Fixed v5 (≥57 edges) and v6 (≥56 edges) snapshots are unchanged. [Source guide](https://github.com/lisresearchgroup/math-rsi/blob/main/plugins/hypercube-hamilton/knowledge/q7-closure-proof.md) · [Recomputation scope](https://github.com/lisresearchgroup/math-rsi/blob/main/plugins/hypercube-hamilton/archive/q7-closure/README.md). Only this domain’s panel changes; all other five domains retain their existing values and scope.
