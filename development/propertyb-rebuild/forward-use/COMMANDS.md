# Actual executable commands and artifacts

CWD for all calls: MathRSI repository root. Source inputs were copied by standard-library shutil into owned work/archive, preserving the context and propertyB_small_k relative tree. See READ_SET.md and SPEC.md.

Executed check sequence:

```sh
python3 -B development/propertyb-rebuild/forward-use/run_checks.py
python3 -B development/propertyb-rebuild/forward-use/diagnose_scope.py > development/propertyb-rebuild/forward-use/scope.stdout.log
python3 -B development/propertyb-rebuild/forward-use/write_wiki.py
```

All three returned exit0. `run_checks.py` logs the two actual subprocess argv/cwd/exit/time in COMMANDS.json. Diagnostic results are SCOPE_RESULTS.json and scope.stdout.log. `write_wiki.py` logs all nine capture/helper commands with actual absolute repository helper argv, ARIS_REPO binding and exit codes in WIKI_COMMANDS.json. Its note inputs and individual stdout/stderr remain here. The helper mutations and edges are also recorded in research-wiki/log.md and graph/edges.jsonl.

The two checker calls may be repeated from this working copy with the same run_checks.py command; they intentionally overwrite CANDIDATE.json and independent/RESULTS.json only inside this owned working copy. write_wiki.py is retained as the exact command-generating script, not a claim that the original library wiki has been changed.
