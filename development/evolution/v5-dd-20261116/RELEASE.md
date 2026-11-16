# v5 DD maintenance integration — 2026-11-16

The user authorized publication as v5 maintenance on main. This record captures pre-merge integration; the linked pull request and Pages run are authoritative for the eventual merge/deployment status.

- Base: `80fd0ffcf291d39383dd7cec2e73f75dc2d875e0`.
- Technical adoption: `07fb68a4`; presentation: `4326fd94` cherry-picked as `97c2f778`; final layout/media repair: `94905c68` cherry-picked as `48cf14b8`.
- Fixed v5 tag commit: `903760da4432fd487ab767cb87b8bc8063b25298`. No tag change or v6 release is part of this maintenance.
- GitHub operator: `wanshuiyin`; author/committer: Yang Ruofeng, associated GitHub noreply email.
- [Evolution and actual adoption](EVOLUTION.md), [Gemini discussion disposition](discussion/DISPOSITION.md), [maintainer handoff](checks/presentation/HANDOFF.md).

## Completed verification

Both final graph edge sets were reproduced and compared exactly; all 161 D11 exterior/new roots and 31 D12 new roots passed complete BFS. Independent array, degree and source-retention checks passed. The D11 explicit core argument was separately read; D12 old–old distances inherit the accepted source. This does not add concrete whole-graph Lean certification.

Seven maintained-helper regression tests passed, including the actual eight-prefix archived receipt and a tiny compiled C++ control test. The final scoped implementation/documentation review found no substantive mismatch. No production search or Lean build was launched.

The integrated public output has 79 files (24,491,998 bytes), exactly matching the explicit allowlist, with zero broken local references. Its only newly published path is `dd-latest.html`; the 455-file scientific archive is not in the Pages output. The maintained-document check passed for 142 documents and 2,111 local targets after integration.

The presentation maintainer checked both languages at 1440/390 px, 24 dynamic reading links, zero page/request errors and no page overflow. Contributor tails, including Zheli Zhou, were preserved. GitHub's actual GFM response recognizes both new parameter formulas in both READMEs. Root inspected the actual desktop evolution and Chinese mobile reader captures. Final native animation: 24.9 seconds at 1900×742 (GIF 1400×546), including six seconds holding the final v5 frame; both Q7 and DD remain visible and all six DD outcome blocks sit below the cards. The [final layout handoff](checks/presentation/layout-fix/HANDOFF.md) and [six-view geometry checks](checks/presentation/layout-fix/LAYOUT_RESULTS.json) supersede the first presentation capture. Root viewed the repaired poster. [Recording receipt](../../../figures/mathrsi/media/RECORDING.json).

## Publication

Feature branch: `feat/v5-dd-followup-20261116`. [PR #37](https://github.com/lisresearchgroup/math-rsi/pull/37) contains the complete change; its checks tab records the final head validation. Initial pre-merge Pages build [43841273038](https://github.com/lisresearchgroup/math-rsi/actions/runs/43841273038) passed for `90e9e313`. Root then found a real v5 card/column overlap in the recorded poster and requested a scoped layout repair before merging; the final recording and checked head supersede that first presentation receipt. Merge and public deployment status are recorded on the PR and its linked main-branch Pages run. Public entry points after successful deployment: [homepage](https://lisresearchgroup.github.io/math-rsi/) and [DD reader](https://lisresearchgroup.github.io/math-rsi/dd-latest.html).
