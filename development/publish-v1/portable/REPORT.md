# Independent v1 fresh-clone validation

**PASS**, 2026-11-02, source commit `4b08fc114d12fb2ae9939530d2bc3b36d195250f` on `publish/v1`.

A new temporary checkout was created with `git clone --no-hardlinks --single-branch --branch publish/v1 /Users/rfy_naiveai/Desktop/MathRSI <fresh-temp>/math-rsi`. All checks below read that clone, not another author source directory. The initial remote README merge and the new quickstart/example were part of the tested commit. The clone remained Git-clean after validation.

|Check|Actual result|
|---|---|
|`python3 tools/check_links.py`|exit 0; 67 maintained documents, 1,048 local link targets, zero missing|
|`python3 -B base/tests/smoke_bundle.py --out-dir <temp>/smoke`|exit 0; 207 upstream source files and nine relocated helper commands PASS|
|`python3 -m unittest discover -s mcp-servers/tests -p 'test_*.py' -v`|exit 0; 61 tests in 26.376 seconds; OK|
|`python3 examples/proof-repair/replay.py` from clone root|exit 0; exact 32-coloring counterexample and union-bound arithmetic|
|Absolute clone path to `replay.py` from an unrelated directory|exit 0; identical successful output|
|Clone-local absolute `base/tools/research_wiki.py --help` from unrelated directory|exit 0; confirms documented helper path and `ARIS_REPO` binding|
|Documented starter-copy shell recipe|exit 0; workspace contains only `REQUEST.md` and `PROOF.tex`, both byte-for-byte equal to the cloned starter|
|Starter/reference theorem environment comparison|exact text equality, including theorem label; saved in `THEOREM.txt`|
|All cloned symlinks|89; every target is relative, existing, and inside the canonical clone root|
|Final cloned `git status --short`|exit 0, empty output|

The replay prints `P(Be)=1/8`, `P(Bf)=1/8`, `P(both)=1/16`, and independence product `1/64`; all budgets `m=0,...,7` retain a good-coloring lower bound of at least `1/8`. This is an exact check of the faulty intermediate claim and the repair arithmetic. The full universal theorem is supplied by the reference proof; this run did not re-execute agent reviews.

Versions: Python **3.14.6**; Git **2.50.1 (Apple Git-155)**. These are actual versions, not evidence that the documented minimum Python version was separately tested.

`RESULT.json` records the source commit, clone/workspace paths, command arguments, working directories, exits, versions, and scope. Each command has separate raw stdout/stderr logs. `STARTER_COPY_COMMAND.sh` preserves the exact shell recipe used. `smoke-RESULT.json`, `smoke-academic.html`, and `smoke-dashboard.html` retain the small smoke artifacts; the smoke result also contains its nine commands and raw captured helper outputs. `SYMLINKS.json` records every alias.

The temporary verification harness initially compared canonical `/private/var/...` symlink targets against a noncanonical `/var/...` clone path on macOS. The audit comparison was corrected by resolving the clone root. Every symlink then passed; no product file, test outcome, or suite execution changed.

This check exercised the runnable offline commands from README/QUICKSTART and the documented starter-copy setup. It did not start Codex/Claude, register MCP services, call models, clone from authenticated GitHub, compile TeX/Lean, or resume archived research Goals. Reviewer accounts, host startup, external services, PDF rendering, and formal proof compilation remain in their documented separate scopes.
