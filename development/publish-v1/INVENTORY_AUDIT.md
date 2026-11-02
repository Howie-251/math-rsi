# v1 publication inventory audit

Read-only audit of the tracked checkout and all reachable Git history at `33fca90` on 2026-11-02. The audit wrote only this report. It did not modify source, configuration, original research workspaces, or any Goal. The authorized destination is the private `lisresearchgroup/math-rsi` repository; this is a publication inventory assessment, not a new mathematical acceptance.

## Decision

**No inventory, repository-size, obvious credential, or required-resource blocker found for publishing the current complete history to the private repository.** Final checkout execution checks remain the release owner's responsibility. Before release, replace the obsolete local-only wording in `AGENTS.md:7` and `README.md:81` with the current authorization and release state; the owner has already taken this documentation change.

## Counts and history

|Item|Observed|
|---|---:|
|Reachable commits|6|
|Tracked paths|8,297|
|Tracked bytes, including symlink text|157,539,481|
|Missing tracked paths|0|
|Reachable Git objects|9,066|
|Reachable blobs|8,234|
|Total reachable blob bytes|157,061,708|
|Files or historical blobs above 50 MiB|0|
|Files or historical blobs above 100 MiB|0|
|Tracked symlinks|89|
|Broken or outside-repository symlinks|0|
|Included Property B archive inventory rows|7,644|
|Included rows missing, untracked, or wrong size|0|
|Bundled paper PDFs / ZIP archives|21 / 1|

The largest tracked file is `plugins/propertyb/knowledge/archive/context/propertyb-k12-4664-20261029/COMPLETE.json` at 17,455,594 bytes. The full history contains no large-file threshold violation. No history rewrite or LFS migration is required by this inventory.

## Credentials and authentication artifacts

All reachable historical text blobs were checked for obvious private-key blocks and standard GitHub, provider, AWS, Google, JWT, literal credential-assignment, Bearer-token, and URL-userinfo patterns; binary blobs were excluded from content matching. No actual credential was identified. Historical filenames yielded no `.env`, credential store, private-key, `auth.json`, or `config.toml` candidate. The sole supplementary URL-userinfo match was `base/tools/overleaf_setup.sh:69`, which interpolates the runtime shell variable `OL_TOKEN`; it is source code rather than a committed token. The six-member `propertyB_k10_k11_bundle.zip` contains research Markdown, three Python files, and two verification logs, with no authentication filename candidate.

This is an obvious-secret inventory scan, not a guarantee against arbitrary encoded or unrecognized sensitive content. No secret values were printed or saved by the audit.

## Self-contained resources and author paths

`base/ARIS_SNAPSHOT.json` identifies the fixed 207-file upstream resource set, and the offline smoke consumes it directly. The four MCP Python services and their source/license record are present. Property B's declared 7,644 included resources are all tracked and retain their inventory byte lengths. Both skill-discovery trees use relative aliases resolving inside this repository. The tracked ECC source handoff documents are present even though their parent directory is generally ignored.

No author-machine absolute path was found in the maintained MathRSI/Property B skills or the active Python tools/MCP services searched. `AGENTS.md:10` identifies original source workspaces as provenance, not executable setup. Maintained integration instructions explicitly bind helpers to this checkout and disallow silently falling back to another ARIS installation. Generic upstream resolver fallback remains in the immutable ARIS copy and is documented in `base/README.md` and `docs/ARIS_REUSE.md`.

The archive intentionally omits toolchains, `.lake`, external software clones, large scan logs/binaries, and some historical JSON. Its README states that it is a research-source archive rather than a complete replay of every historical run. Old absolute paths, old HTML/ZIP links, timestamps, and historical Goal instructions in that archive are therefore not present-day release blockers. Maintained example/checker routes explicitly select bundled inputs; final isolated execution should confirm those routes rather than bulk-running historical scripts.

## Licensing and provenance

Root `LICENSE`, `base/LICENSE`, and `mcp-servers/LICENSE.ARIS` retain the upstream MIT notice. `docs/PROVENANCE.md`, `base/ARIS_SNAPSHOT.json`, and `mcp-servers/SOURCE.md` distinguish fixed upstream material, local adaptations, and domain research. The main README and provenance text explicitly exclude third-party papers/originals from any implied MIT relicensing; source URLs and versions are retained in the archive reference map. No additional license-file omission was identified. This assessment is for the authorized private repository and does not certify blanket redistribution rights for a future public release of every third-party PDF.

## Fresh-checkout verification assessed

Run from the complete final checkout, storing smoke output outside it:

```sh
python3 tools/check_links.py
python3 -B base/tests/smoke_bundle.py --out-dir /tmp/mathrsi-v1-smoke
python3 -m unittest discover -s mcp-servers/tests -p 'test_*.py' -v
```

The link checker covers maintained routes and aliases. The smoke reads bundled resources, copies `base` to a temporary path, and invokes its wiki, router, and both HTML templates from a separate task directory. Its nine commands use explicit relocated helper paths and do not require another author checkout, model account, network, Lean, or TeX. It validates source identity and local integration, not theorem truth or model execution. MCP tests use fake CLIs and temporary state, avoiding paid calls and global registration changes. CLI/login/network, optional search SDKs, Lean/Mathlib, TeX, and a C++ compiler for the explicitly compiled example remain documented environment dependencies.

These commands were assessed from source here, not rerun by this auditor; the release owner is executing them once on the final staged/committed checkout to avoid duplicate work. Exact counts above are for the audited commit and will increase with release documentation/example additions.
