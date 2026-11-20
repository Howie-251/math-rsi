# Homepage evolution replay · v6 main Q7 full author working proof

[Visual tour](../../../docs/HOMEPAGE.md) · [Figure gallery](../README.md) · [Six results and scope](../../../case-studies/README.md)

[![Actual MathRSI homepage replay from v0 through v6 Current](evolution.gif?v=6-q7-20261120)](evolution.mp4?v=6-q7-20261120)

- [GIF](evolution.gif?v=6-q7-20261120): 1400 × 554, 13.1 seconds, 50 fps (`2 cs` exact frame delay, one native `16 ms` rAF step per frame at `0.80×` browser clock), loops; 1,640,544 bytes.
- [MP4](evolution.mp4?v=6-q7-20261120): 2000 × 792, H.264/yuv420p, faststart; 13.1 seconds, 50 fps; 556,937 bytes.
- [Poster](poster.png): 2000 × 792, decoded from the final MP4 hold at v6 Current.
- [Recording receipt](RECORDING.json): actual v0/v1/v2/v3/v4/v5/v6 samples, source revision, crop geometry, durations, byte sizes and browser errors.
- [Recording source](record.py): resolves this clone from its own location.

The real Replay control runs the English homepage from v0 through v6 Current, with v7+ Future retained. The final state holds for **5.5 seconds**. All three v6 bubbles — Erdős 86 (`Q₇ 304 · Q₈ 682–683`, `Q∞ ≤ 0.5912405943`), Ruskey–Savage (`Q₇ · every matching`, author working proof), and Happy Ending (`N(8,6,6) ≤ 61 · ES(9) ≤ 1148`) — sit above all **24 opaque outcome blocks**, without intersections or text overflow. The original Q6 result, v5 ≥57-edge milestone and fixed-v6 E16 ≥56-edge milestone remain in the live timeline and reader.

The full R7 author working proof was accepted in its source project on 2026-11-19, following v3 local adaptation, and is incorporated in v6 main maintenance on 2026-11-20. External peer review is pending, no Lean proof is supplied, and bounded local E38 recomputation is separate from end-to-end replay of the older imports. Fixed v1–v6 tags remain unchanged. [Q7 scope and sources](../../../case-studies/ruskey-savage-q7/README.md).

## Reproduce

Python Playwright, its Chromium browser, ffmpeg and ffprobe must be available. From the clone root:

```sh
# Optional: inspect the measured final crop before recording.
python3 figures/mathrsi/media/record.py --preview

# Record the actual animation and replace the three distribution assets.
python3 figures/mathrsi/media/record.py
```

The viewport is 2000px wide (`2000 × 792` measured crop), fitting all eight columns (v0..v6 and v7+) with `scrollLeft == 0`. Capture-only CSS isolates the evolution diagram, hides the detailed Base/Plugins rows and panel, disables column-band wall-clock fade under virtual-clock stepping, and sizes version/callout labels. It does not patch application state, product JavaScript or mathematical data. Intermediates, the separately decoded GIF last frame and the 900px README preview remain in ignored `.local/evolution-media-v6-q7-20261120/`. README media URLs use `?v=6-q7-20261120` to refresh caches.
