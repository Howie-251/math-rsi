# Homepage evolution replay · v6 C4-free, Q7 E16 & N(m,r,s)

[Visual tour](../../../docs/HOMEPAGE.md) · [Figure gallery](../README.md) · [Six results and scope](../../../case-studies/README.md)

[![Actual MathRSI homepage replay from v0 through v6 Current](evolution.gif?v=6-nmrs-20261117)](evolution.mp4?v=6-nmrs-20261117)

- [GIF](evolution.gif?v=6-nmrs-20261117): 1400 × 530, 10.88 seconds, 50 fps (`2 cs` exact frame delay, 1:1 native `16 ms` `rAF` step at `0.80×` browser clock), loops; 1,555,644 bytes.
- [MP4](evolution.mp4?v=6-nmrs-20261117): 2000 × 758, H.264/yuv420p, faststart; 10.88 seconds, 50 fps, 541,682 bytes.
- [Poster](poster.png): 2000 × 758, decoded from the final MP4 hold at v6 Current.
- [Recording receipt](RECORDING.json): actual v0/v1/v2/v3/v4/v5/v6 samples, source revision, crop geometry, durations, byte sizes and browser errors.
- [Recording source](record.py): resolves this clone from its own location.

This is a recording of the English homepage in `development/homepage-redesign-20261105/site/` ending at `v6 Current` (with `v7+ Future`). The real Replay control runs from v0 through v6 Current; all three v6 callout bubbles — Erdős 86 (`Q₇ 304 · Q₈ 682–683`, `Q∞ ≤ 0.5912405943`), Ruskey–Savage (`Q₇ · ≥56 edges`), and Happy Ending (`N(8,6,6) ≤ 61 · ES(9) ≤ 1148`, `m = 7–9 working · Run: v3`) — sit cleanly above all 23 opaque outcome blocks with zero text overflow. Research provenance stays separate from the receiving v6 release and `main` maintenance; fixed `v1`–`v6` tags remain unchanged.

## Reproduce

Python Playwright, its Chromium browser, ffmpeg and ffprobe must be available. From the clone root:

```sh
# Optional: inspect the measured final crop before recording.
python3 figures/mathrsi/media/record.py --preview

# Record the actual animation and replace the three distribution assets.
python3 figures/mathrsi/media/record.py
```

The recording viewport is 2000px wide (`2000 × 758` measured crop), fitting all eight columns (`v0`..`v6` and `v7+`) without horizontal scrolling (`scrollLeft == 0`). Capture-only CSS isolates `#evolution`, hides the detailed Base/Plugins rows and panel, disables wall-clock column-band fade desync under virtual-clock stepping, and sizes version and callout headlines cleanly without patching product JavaScript, CSS or data. Intermediates are written to the ignored `.local/evolution-media-v6-nmrs-20261117/` directory. Both README media URLs use `?v=6-nmrs-20261117` to refresh image/video caches.
