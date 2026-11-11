# README navigation badges — 2026-11-11

Implemented in `/Users/rfy_naiveai/Desktop/MathRSI-github-redesign-20261111`, branch `docs/readme-badges-20261111`, from fetched origin/main `23be32be69bf667b0774d0b3b954f62f26f3489e`. The earlier merged branch is unchanged. GitHub is wanshuiyin; Git identity is Yang Ruofeng with the associated noreply address.

The two README navigation paragraphs now use four local editable, two-part SVG badges: quick start, six-domain results, bilingual visual tour and agent workflow/wiki guide. Language switching stays separate. The eight assets in `figures/mathrsi/badges/` use the palette and labels forwarded from Gemini by Root: 24px high, 4px corners and 12px text. Inline spacing is approximately 8px; badges wrap naturally. No badge service or build step is required.

Actual previews reuse the existing `development/github-redesign-20261111/preview.py` CSS with GitHub GFM API HTML and Playwright; dark previews apply GitHub's dark background/text palette. These are local rendered reading columns, not captures of GitHub's full repository UI. All badge images loaded; all four links in each language point to the requested existing documents. Desktop navigation occupies one row; at 390px English uses three rows and Chinese two, without page overflow. The existing link checker reports **134 documents / 1,964 local targets, zero missing**. No test suite was added for this visual change.

- [English, desktop/light](en-light-1280.png) · [English, mobile/dark](en-dark-390.png)
- [Chinese, desktop/light](cn-light-1280.png) · [Chinese, mobile/dark](cn-dark-390.png)
- [All eight preview measurements](PREVIEWS.json); corresponding light/dark 1280/390 screenshots are in this directory.

Root inspected the actual README diff, SVGs and desktop/mobile previews and accepted the navigation and layout for PR submission. Scope is limited to the two README navigation blocks, badge assets and these preview/handoff files. Homepage, mathematical state and logo remain unchanged. Root handles separate logo candidates and final actual-head merge; this implementation does not merge.
