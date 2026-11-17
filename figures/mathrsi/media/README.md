# Homepage evolution replay · v6 C4-free & Q7 E16 release

[Visual tour](../../../docs/HOMEPAGE.md) · [Figure gallery](../README.md) · [Six results and scope](../../../case-studies/README.md)

[![Actual MathRSI homepage replay from v0 through v6 Current](evolution.gif?v=6-dd1block-20261117)](evolution.mp4?v=6-dd1block-20261117)

- [GIF](evolution.gif?v=6-dd1block-20261117): 1400 × 488, 29.0 seconds, 12 fps, loops; 1,536,875 bytes.
- [MP4](evolution.mp4?v=6-dd1block-20261117): 2000 × 696, H.264/yuv420p, faststart; 29.0 seconds, 20 fps, 691,968 bytes.
- [Poster](poster.png): 2000 × 696, decoded from the final MP4 hold at v6 Current.
- [Recording receipt](RECORDING.json): actual v0/v1/v2/v3/v4/v5/v6 samples, source revision, crop geometry, durations, byte sizes and browser errors.
- [Recording source](record.py): resolves this clone from its own location.

This is a recording of the English homepage in `development/homepage-redesign-20261105/site/` ending at `v6 Current` (with `v7+ Future`). The real Replay control runs from v0 through v6 Current; both v6 callout bubbles—Erdős 86 (`Q₇ 304 · Q₈ 682–683`, `Q∞ ≤ 0.5912405943`, `≤304 source · 682 open · Run: v3`) and Ruskey–Savage (`Q₇ · ≥56 edges`, `all 16-hole classes · Run: v3`)—are fully visible above all 22 opaque outcome blocks with zero text overflow (the v5 D5 follow-up adds a single Degree–Diameter result-family block from 4 at v4 to 5 at v5). Research provenance stays separate from the receiving v6 release; fixed `v1`–`v6` tags remain unchanged unless explicitly updated.

## Reproduce

Python Playwright, its Chromium browser, ffmpeg and ffprobe must be available. From the clone root:

```sh
# Optional: inspect the measured final crop before recording.
python3 figures/mathrsi/media/record.py --preview

# Record the actual animation and replace the three distribution assets.
python3 figures/mathrsi/media/record.py
```

The recording viewport is 2000px wide (`2000 × 696` measured crop), fitting all eight columns (`v0`..`v6` and `v7+`) without horizontal scrolling (`scrollLeft == 0`). Capture-only CSS isolates `#evolution`, hides the detailed Base/Plugins rows and panel, and sizes version and callout headlines cleanly without patching product JavaScript, CSS or data. Intermediates are written to the ignored `.local/evolution-media-v6-c4free-rs7-20261117/` directory. Both README media URLs use `?v=6-dd1block-20261117` to refresh image/video caches.
