# Text and control-plane check record

2026-11-15. Performed by the designated implementation agent, not an independent
mathematical reviewer. Existing files, SAT jobs, proof bindings, production
configuration and acceptance records were not changed.

## Document checks

PowerShell/.NET resolved each local Markdown target against its source file:

| File | Local targets | External targets | Missing local targets |
| --- | ---: | ---: | ---: |
| N7_N8_EVIDENCE_20261115.md | 42 | 0 | 0 |
| N7_N8_SYNTHESIS_20261115.md | 40 | 4 | 0 |
| This directory's README.md | 2 | 0 | 0 |

The synthesis has 20 matched display-math delimiter pairs, no ordered
unescaped-brace imbalance within them, and two matched `aligned` environments.
Its 352 unescaped dollar signs, including display delimiters, have even count.
These are text checks, not a rendered-math or proof verification.

Arithmetic transcribed from the main agent includes 56-3=53, 70-3=67,
22+53-1=74, 53+67=120, 74+120-1=193, 2*120-1=239,
120+22=142, 239+142=381, 381+1=382; 120-6=114 and
210-6=204 triangular cells. No mathematical program was run for these checks.

## Source checks and limits

The new PowerShell files were parsed with
`System.Management.Automation.Language.Parser.ParseFile`; both returned zero
syntax errors. This parser did not execute their contents. The Python source
was read and self-checked as text, but was not compiled, linted, type-checked
or executed because project/scientific workloads must run on Linux.

Prepared Python source SHA256:

```text
4428ed0a7a1e1ba8e5750baa258788e4e31c38a8e00dcc4e2ac594a86068daaa
```

The checker's Linux-only guard, finite case list, all-triple difference tests,
shared-endpoint/internal-disjointness tests and row-family disjointness checks
are code awaiting actual execution, not successful test results.

## Actual control-plane evidence

* `probe-receipt.json`: exit 255; strict host-key verification rejected the
  current endpoint because the existing pinned file lacks that endpoint key.
  No scientific script execution was requested.
* `pin-comparison.json`: separately authorized single public key scan, exit 1,
  zero keys returned. No comparison with the old authoritative pin was
  possible. This does not prove a key mismatch. No password authentication,
  key enrollment, known-host modification, public-key output, HostKeyAlias
  login, or further connection attempt followed.

No source upload, Linux verifier execution, SAT/solver/checker process, or
Windows scientific fallback occurred. There is no Python PASS/runtime receipt.
The README provides the exact Linux reproduction command and create-only
transport sequence for a future authorized restoration of the trusted route.
