# PR11 integration readback — 2026-11-08

**Recommendation: incorporate the already reviewed PR11 case into the authorized publication, preserving the current v4 README text when integrating the two root README hunks.** No new substantive source changes were found. This readback did not merge, push, comment, fetch into Git, or modify implementation files. PR13 is untouched.

## Remote facts

Authenticated GitHub REST returned PR11 open, head **7bd5a0cf34db9454cb0badf79c8622fb5fb7b833**, base **58c77f0b75d49a426b2629dafab8b82222d40041**, `mergeable=true`, `mergeable_state=clean`. All **48 changed-file metadata/patch records are exactly equal** to the fixed-head intake saved previously. Thus the mathematical attribution, final formal C incomplete and compact-receipt scope are unchanged.

Checks API returns **no check runs**. Combined status returns `state=pending` with **statuses=[]**; this is absence of status contexts, not evidence of a running or passing CI job. The current checkout has **no `.github/workflows/` directory**, so there is no local GitHub Actions workflow command list to execute.

46 paths are within `case-studies/degree-diameter/`; the only paths outside the case are **README.md and README.zh-CN.md**, two-line overview updates for this case. No service/runtime/configuration, unrelated domain or credential file is introduced. Read changed plotting/replay/render code and metadata. Targeted key/private-key-pattern scan of all text patches found no hits; this is a bounded content check, not an exhaustive secret-scanner certification. Preserved historic researcher paths/session IDs in receipts are provenance, not authentication material.

Binary payloads are small presentation/source assets: new construction PNG **168,582 bytes**, modified results PNG **215,786 bytes**, compressed seed **40,063 bytes**. New construction SVG is 15,208 bytes and results SVG 24,264 bytes. No large graph dump, full Lean/cache or large binary is added.

## Integration overlap and dependency

GitHub reports no remote merge conflict. Local tracked v4 modifications overlap PR11 only at **README.md** and **README.zh-CN.md**. Preserve current v4 version/release narrative and absorb the PR11 2567-result attribution; do not replace those whole files with PR11's older main/v3 versions. Other 46 case paths are not locally modified tracked paths at readback.

V4 plugin runtime is **self-contained** in `plugins/degree-diameter/archive/pr11-2567/`: no canonical case path or homepage source is needed for finite replay. The local homepage's DD detail similarly uses its packaged `assets/dd-2567/` materials. However root README and homepage “Earlier research” navigation link to canonical `case-studies/degree-diameter/`; current main's older case still says 153/43/47 and three comparisons. Integrating PR11 makes these canonical readers consistent with 163/44/49 and four comparisons, while retaining earlier ARIS versus v2+DD attribution.

## Proportionate final commands

After combining the actual publication changes, run **`git diff --check`** (and for a staged publication, **`git diff --cached --check`**) and **`python3 tools/check_links.py`**. Confirm intended path list and README overlap in the final staged diff. Preserve existing v4 bounded usage and browser results; no mathematical rerun is warranted solely by this unchanged case integration. If any canonical asset or generated HTML is altered during conflict resolution, inspect that changed rendering/link only. Embedded ARIS source is unchanged, so a fresh full ARIS resource smoke is not required for this case merge.

Already available evidence: v4 `VALIDATION.md` (124 maintained documents/1869 targets and 35 changed curated documents/620 targets), DD ten-graph replay and literal degree checks, and the previous mobile/desktop homepage browser report. These have their original scopes; they do not supply remote CI or a completed final external formal C.
