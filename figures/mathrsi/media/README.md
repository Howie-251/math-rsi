# Homepage evolution replay · v5

[Visual tour](../../../docs/HOMEPAGE.md) · [Figure gallery](../README.md) · [Six results and scope](../../../case-studies/README.md)

[![Actual MathRSI homepage replay from v0 through v5 Current](evolution.gif?v=5)](evolution.mp4?v=5)

- [GIF](evolution.gif?v=5): 1400 × 474, 23.75 seconds, 12 fps, loops; 1,299,554 bytes.
- [MP4](evolution.mp4?v=5): 1900 × 642, H.264/yuv420p, faststart; 23.75 seconds, 20 fps, 471,146 bytes.
- [Poster](poster.png): 1900 × 642, decoded from the final MP4 hold at v5 Current.
- [Recording receipt](RECORDING.json): actual v0/v1/v2/v3/v4/v5 samples, source revision, crop geometry, durations, byte sizes and browser errors.
- [Recording source](record.py): resolves this clone from its own location.

This is a recording of the existing English homepage in `development/homepage-redesign-20261105/site/`, at source commit `e260c4c0680cbae5fbb804fd4ed7fa7b0a282a9c`. The real Replay control runs from v0 to v5 Current; the Q7 ≥57-edge bubble is fully visible at the end. Research provenance stays separate: Q7 ran with v3 (local adaptation) and feeds v5. Result and manuscript scopes remain in the linked case records.

## Reproduce

Python Playwright, its Chromium browser, ffmpeg and ffprobe must be available. From the clone root:

```sh
# Optional: inspect the measured final crop before recording.
python3 figures/mathrsi/media/record.py --preview

# Record the actual animation and replace the three distribution assets.
python3 figures/mathrsi/media/record.py
```

The script serves this full clone on a temporary loopback port, waits for fonts and runs the real Replay button. It advances the browser clock by 0.25 milliseconds per encoded-video millisecond. Playback ends when the native Play control stops at the page's Current release, rather than at a hard-coded timeline value. The captured stream has a one-second opening hold and a six-second settled final hold. For this export, v5 first appears at 15.9 seconds, playback settles by 17.75 seconds, and the video ends at 23.75 seconds.

The recording viewport is 1900px wide. Its measured version-row bottom is 621.90625px; rounding that bound plus 20px padding gives the **1900 × 642** crop. All seven columns fit without horizontal scrolling. The crop retains every result bubble, the complete version axis and v5 Current's name; it does not trim the right edge. Capture-only CSS isolates the evolution section, hides the detailed Base/Plugins rows and panel, and enlarges version labels and the Q7 headline for the README. Their full explanations remain on the interactive homepage. Product JavaScript, CSS, mathematical values and version data are unchanged.

The script encodes real PNG screenshots to MP4, exports a 1400px-wide GIF with a 128-color palette, decodes the final MP4 frame to `poster.png`, and separately decodes the last GIF frame. The resulting 900px README preview and both decoded endings were visually checked: v5 Current and Q7 ≥57 edges remain visible, with the full rightmost column inside the frame. Open the MP4 or interactive page for finer labels.

Intermediates, state stills, the 900px preview, capture log and attempt/failure log go to the ignored clone-root `.local/evolution-media-v5-20261116/`. They are not distribution assets. The receipt records the successful capture's source and actual parameters; regeneration refreshes them. A fast-seek preflight exposed a still-settling opacity transition, so the script allows a 350ms compositor settling interval before final stills. The complete replay/encoding succeeded with no browser errors or failed requests.

Both README media URLs use `?v=5` on the same asset paths to refresh image/video caches. No extra asset copies are needed.
