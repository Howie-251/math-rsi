# Logo C and numbered README sections — 2026-11-11

Branch `feat/logo-c-readme-headings-20261111`, based on fetched origin/main `d0c941f86cfd1b17aac0a1368a299bb3da6cc0b6`, in the existing isolated worktree. Prior merged branches are unchanged.

Both README files now have the six requested numbered emoji chapter headings. Existing section fragments are preserved with explicit anchors; GitHub GFM retains them with its normal `user-content-` prefix. The main MathRSI title and team/tagline remain unnumbered, with a theme-aware inline C symbol and one native MathRSI label. The four local navigation badges are unchanged.

The homepage places C's light symbol inside the existing wordmark plane, next to native interactive text. Hover/click transforms still apply to the combined mark and text; the separate team line remains. Only the hero HTML and scoped wordmark CSS changed; no JavaScript or translation entry needed modification. The light PNG is transparent; the dark README PNG has GitHub `#0D1117` background and is not transparent. Root supplied and inspected both symbol assets; no team signature is embedded.

Actual previews use GitHub GFM API HTML and the existing preview CSS at desktop and 390px widths. README was viewed in both languages and light/dark schemes; each scheme loaded the correct picture source, with one MathRSI title and no page overflow. The website was viewed in English/Chinese at 1280/390px, with no page errors, loaded symbols and working hover/click pulse. File access and a temporary HTTP server rooted at the full clone both loaded the shared repository asset. Compared with the recorded original English hero, height grew 6.09px desktop / 3.61px mobile. These are local rendered previews, not screenshots of GitHub's full repository UI.

- [Homepage desktop](site-en-1280.png) · [Homepage Chinese mobile](site-zh-CN-390.png)
- [README light desktop](readme-en-light-1280.png) · [README Chinese dark mobile](readme-cn-dark-390.png)
- [All preview measurements](PREVIEWS.json) · [Original hero baseline](BASELINE.json)

The existing link checker passed: **134 documents / 1,964 local Markdown targets, zero missing**. Staged whitespace/diff check is part of submission. Research text, versions, evolution results, skills and archived evidence remain unchanged. Actual previews were delivered to Root before submission; final actual-head acceptance and merge remain with Root.
