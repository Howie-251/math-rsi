# v4 release — 2026-11-08

The user authorized pushing the completed increment and updating the HTML, then confirmed that v4 should become the current version rather than Preview. `main` and the fixed `v4` tag are the release entry points; v1/v2/v3 remain at their original commits. The repository stays private. No public website hosting or access change is part of this operation.

The completed base/plugin implementation is recorded in [EVOLUTION.md](EVOLUTION.md) and [V4_CHANGES.md](../../../docs/V4_CHANGES.md). Earlier local/unreleased labels in implementation or review receipts refer to that stage, not the subsequent release operation.

[PR #11](https://github.com/lisresearchgroup/math-rsi/pull/11), merged as `cf186b55`, had fixed head `7bd5a0cf34db9454cb0badf79c8622fb5fb7b833` was checked against the already reviewed intake and merged before v4 integration. It supplies the canonical DD case, while the plugin remains self-contained. Its result was produced with v2 + DD + PR7, and the new Happy Ending upper-bound manuscripts retain their own working-proof status. PR #13 remains with the collaborator the user selected.

The existing English static homepage is now included in the repository at [site/index.html](../../homepage-redesign-20261105/site/index.html). It shows v4 Current, three connected base improvements and deeper existing plugins. Six result cards, historical mathematical attributions and detailed proof-status disclosures remain. Open it after cloning or use the separately generated self-contained `MathRSI_homepage_v4_20261108.zip`; GitHub source viewing is not HTML hosting.

Bounded checks reuse the actual mathematical-command outputs already accepted for this increment. Final release checks cover Git diff whitespace, repository links, the exact publish files, desktop/mobile current-version behavior, and navigation in the new offline bundle. Browser evidence lives in `development/homepage-redesign-20261105/checks/release-v4-20261108/`. The old offline preview ZIP remains unchanged.

GitHub PR/merge commits and the v4 ref provide the immutable publication identity. Final operation receipts are recorded after the remote reports success; release prose is not itself a claim that a pending network operation succeeded.

The rebuilt offline bundle contains 1,211 files (15,990,422 compressed bytes). Its 18 offline checks and the 16 desktop/mobile checks passed. Inherited unavailable source links are explicitly disabled and listed in the build inventory; the viewing bundle does not claim to provide the full mathematical reproduction environment.
