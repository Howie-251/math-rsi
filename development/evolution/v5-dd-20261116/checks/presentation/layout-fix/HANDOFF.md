# v5 callout clearance fix

Parent commit:4326fd943cb4efcc2c74b232a728a36f54679b5d. This is an additional fix commit, not an amend. No push/PR/merge.

Cause: callout stack bottom was fixed at154 SVG units, while six DD outcomes rose to97 units. The earlier check compared bubbles with each other but omitted outcome rectangles. The new geometry computes each column's final maximum depth, reserves the complete callout stack plus14-unit padding and the40-unit drop entrance, and adds91 SVG units of headroom. Text, block size/count, horizontal centering, native playback and v6+Future remain unchanged.

Validation: actual public page EN/ZH at1900/1440/390. Each has six opaque DD rectangles, two visible v5 callouts, zero bubble/block intersections at12 native replay samples and final state, no page overflow or pageerror. Final page clearance is48.67px at1900 and47.66px at1440/390. Evidence:LAYOUT_RESULTS.json and evolution-{en,zh-CN}-{1900,1440,390}.png. Public build remains79 files, exact allowlist, zero broken local references. No unrelated card/math/link-matrix tests were repeated.

Re-recorded native Replay:v0→v5 Current;1900×742 MP4,24.9s,488096 bytes;1400×546 GIF,24.91s,1394587 bytes. Final hold6s. Crop includes both bubbles, six unobscured DD blocks and v6+Future. Recorder asserts final rectangle count, opacity, clearance and crop inclusion. Actual final MP4 poster, decoded last GIF frame and900px preview inspected. Recording receipt is figures/mathrsi/media/RECORDING.json; local video/stills/logs are .local/evolution-media-v5-dd-layout-20261116/. No recording failures.

Only presentation JS, recorder/receipt/media and media documentation changed. Root retains technical integration and publication ownership.
