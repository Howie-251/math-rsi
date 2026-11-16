# Homepage evolution replay · v5 DD follow-up

[Visual tour](../../../docs/HOMEPAGE.md) · [Figure gallery](../README.md) · [Six results and scope](../../../case-studies/README.md)

[![Actual MathRSI homepage replay from v0 through v5 Current](evolution.gif?v=5-dd-20261116)](evolution.mp4?v=5-dd-20261116)

- [GIF](evolution.gif?v=5-dd-20261116): 1400 × 546, 24.91 seconds, 12 fps, loops; 1,394,587 bytes.
- [MP4](evolution.mp4?v=5-dd-20261116): 1900 × 742, H.264/yuv420p, faststart; 24.9 seconds, 20 fps, 488,096 bytes.
- [Poster](poster.png): 1900 × 742, decoded from the final MP4 hold at v5 Current.
- [Recording receipt](RECORDING.json): actual v0/v1/v2/v3/v4/v5 samples, source revision, crop geometry, durations, byte sizes and browser errors.
- [Recording source](record.py): resolves this clone from its own location.

This is a recording of the existing English homepage in `development/homepage-redesign-20261105/site/`, at base commit `4326fd943cb4efcc2c74b232a728a36f54679b5d` with this handoff's presentation edits. `RECORDING.json` lists those source files; the handoff commit contains the exact recorded source. The real Replay control runs from v0 to v5 Current; both the Q7 ≥57-edge bubble and DD 37,632 / 42,433 bubble are fully visible at the end. Research provenance stays separate: Q7 ran with v3 (local adaptation); DD ran with v4 + local updates. Both feed v5 maintenance, while the fixed v5 tag stays unchanged. Result and manuscript scopes remain in the linked case records.

## Reproduce

Python Playwright, its Chromium browser, ffmpeg and ffprobe must be available. From the clone root:

```sh
# Optional: inspect the measured final crop before recording.
python3 figures/mathrsi/media/record.py --preview

# Record the actual animation and replace the three distribution assets.
python3 figures/mathrsi/media/record.py
```

The script serves this full clone on a temporary loopback port, waits for fonts and runs the real Replay button. It advances the browser clock by 0.25 milliseconds per encoded-video millisecond. Playback ends when the native Play control stops at the page's Current release, rather than at a hard-coded timeline value. The captured stream has a one-second opening hold and a six-second settled final hold. For this export, v5 first appears at 15.9 seconds, playback settles by 18.9 seconds, and the video ends at 24.9 seconds.

The recording viewport is 1900px wide. Its measured version-row bottom is 720.796875px; rounding that bound plus 20px padding gives the **1900 × 742** crop. All seven columns fit without horizontal scrolling. The page reserves callout space above each version’s tallest final outcome stack, including its 40px drop entrance. At v5 all six DD blocks remain below both bubble surfaces, with 58.69px final clearance in the recording. The crop retains every result bubble, the complete version axis and v5 Current's name; it does not trim the right edge. Capture-only CSS isolates the evolution section, hides the detailed Base/Plugins rows and panel, and enlarges version labels and the Q7/DD headlines for the README. Their full explanations remain on the interactive homepage. The recorder does not patch product JavaScript, CSS, mathematical values or version data.

The script encodes real PNG screenshots to MP4, exports a 1400px-wide GIF with a 128-color palette, decodes the final MP4 frame to `poster.png`, and separately decodes the last GIF frame. The resulting 900px README preview and both decoded endings were visually checked: v5 Current, Q7 ≥57 edges and both DD endpoints remain visible, with all six DD blocks unobscured and the full rightmost column inside the frame. The English and Chinese page layouts were also measured at 1900px, 1440px and 390px: all six views retained six complete DD blocks and no bubble/block intersections, including sampled native entrance frames. Open the MP4 or interactive page for finer labels.

Intermediates, state stills, the 900px preview, capture log and attempt/failure log go to the ignored clone-root `.local/evolution-media-v5-dd-layout-20261116/`. They are not distribution assets. The receipt records the successful capture's source and actual parameters; regeneration refreshes them. The script allows a 350ms compositor settling interval before final stills. The complete replay/encoding succeeded with no browser errors or failed requests.

Both README media URLs use `?v=5-dd-20261116` on the same asset paths to refresh image/video caches. No extra asset copies are needed.
