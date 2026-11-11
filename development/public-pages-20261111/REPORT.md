# Public MathRSI Pages — 2026-11-11

Branch `feat/public-pages-20261111`, from origin/main `0784bdce88cab0b20f5801f727548c65d78ea7e6`, in the existing isolated worktree. Root reviewed and approved the 76-file source→destination map before publication preparation. The output is 77 regular files including `.nojekyll`, 24,433,308 bytes. [Full build record](BUILD_REPORT.json) confirms exact output membership and no broken local references. The output, staging caches and this private implementation record are not included in the published artifact.

The public list contains homepage runtime files, fonts/licenses/KaTeX, logo/display images and the selected six-topic HTML/PDF readers. Original source archives are not copied as trees. Nonselected source/evidence references link to the permission-restricted repository; unavailable references keep their labels with disabled links. No reference recursively adds another file. The 76 selected source files are all tracked in the current checkout, including both Q6 HTML reports; no new Q6 material was added.

The builder reuses URL resolution/link adaptation from the earlier offline packager, replacing its recursive small-file selection with the explicit map. Static references and dynamic Read links are adapted. Ordinary JS URLs are handled before `REPO + path`, preserving the public paths in the dynamic details. Source mathematics, version/evolution content and local clone use remain unchanged. README badges, documentation and public-access notes point readers to the public entry while keeping local instructions.

## Executed checks

- Build: exact allowlist, zero missing local runtime/navigation references; no plugins/archive/review/log/source-tree directory in output.
- Existing maintained-link helper: 135 documents / 1,968 local Markdown targets, zero missing.
- [Actual browser record](BROWSER_RESULTS.json): anonymous loopback serving at `/math-rsi/`; desktop 1280px and mobile 390px, EN and 中文. All four views have loaded images/formula markup, no pageerror, no failed request or HTTP error and no page overflow. The six real dynamic detail panels return the expected Read href and HTTP 200 in every view (24 checks).
- [EN desktop](public-en-1280.png) · [中文 desktop](public-zh-CN-1280.png) · [EN mobile](public-en-390.png) · [中文 mobile](public-zh-CN-390.png).
- No mathematical research, Lean, model or new design run. Root inspected the public preview and 24 dynamic links and accepted the scope. Final comment/doc-only cleanup did not rerun those browser checks.

## Workflow and handoff

The official Pages actions build on PR/main/manual events. PRs neither upload a Pages artifact nor deploy; only main uploads `_site` and deploys after build to the `github-pages` environment. Permissions are contents:read plus pages:write/id-token:write in the deployment job. Only the explicit public output is uploaded. [Maintainer instructions](../../docs/PAGES.md) and [official workflow reference](https://docs.github.com/en/pages/getting-started-with-github-pages/using-custom-workflows-with-github-pages) describe the publication.

Root owns final-head review, merge and the real Pages/anonymous-URL check. This agent does not alter organization settings, repository visibility or start the deployment manually.
