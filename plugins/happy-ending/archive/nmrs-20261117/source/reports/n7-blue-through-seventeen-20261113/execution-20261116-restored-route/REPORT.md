# Frozen H17 25-point projection: independently verified SAT

The single authorized frozen Linux execution finished with
`VERIFIED_SAT_NECESSARY_SUBDOMAIN`. Its 3850-variable, 1,406,008-clause CNF
is SAT. Independent schema reconstruction found zero missing and zero extra
clauses; the complete model and all specified physical/virtual semantics
passed independent verification. This projection cannot exclude 17 ambient
blue-five-through points or lower the original 767 bound.

The old remote directory and matching probe processes were checked absent
before this fresh execution. The previous local 2026-11-13 failure receipts
are untouched. This new directory is
`execution-20261116-restored-route`; all four frozen input files match their
2026-11-13 source identities exactly. The new launcher has a create-only claim,
and the original worker records exactly one solver invocation.

## Observed execution

- Linux hostname: `ubun`.
- Kissat exit 10 in 4.627 seconds, with the original
  `--no-binary --time=600` arguments and 615-second outer process-group limit.
- Independent schema audit exit 0 in 8.285 seconds.
- Independent SAT audit exit 0 in 5.428 seconds.
- Whole frozen worker elapsed 26.212 seconds; no timeout.
- No second formula or solver invocation, no retry and no external review.

CNF SHA256: `f2a3a7ae641c3dbac5190012ac940727cfe27769c99fffb87fb6fac3c2fb0e44`.

Frozen probe SHA256: `cec94b66416b267facdfadcdccece96868f621dd82b2b06935c169a2e18e80d4`.

Frozen verifier SHA256: `26431292246a16af03228ffb2efc3050a583337aa92fcf7f586febfab6dbc3c0`.

The independent verifier reads all 3850 model values and all CNF clauses,
then reconstructs paths directly from the 2300 triple colors. It checks all
packets, no red seven, no blue six, every same-endpoint weak7 combination,
both blue anchors, the K red-five/red-six exclusions, required one-way flags,
virtual-red-five closure and both M0 directions. It finds maximum local red
path size 6, blue size 5, 17 local blue
five paths and 12904 local red five paths. No required
auxiliary flag is interpreted as exact population.

## Concrete missing simultaneous blue-path support

K={5,...,21} contains 17 marked points. In this exact verified coloring,
only **4** have both a local incoming and
outgoing blue five: **[5, 15, 20, 21]**.

Marked points with no incoming blue five:
`[7, 8, 9, 10, 11, 12, 14, 16, 19]`.

Marked points with no outgoing blue five:
`[6, 7, 8, 10, 11, 12, 13, 14, 16, 17, 18, 19]`.

For example, point 7 lacks both directions, point 6 has an incoming but
no outgoing blue five, and point 9 has an outgoing but no incoming blue five.
`marked-through-summary.json` is read from the already independently checked
`physical-witness.json` and verifies its binding; no solve or path search was
repeated. Thus this valid finite coloring does not supply the 17 actual
ambient-through witnesses needed by the original mother object. The frozen
spec deliberately did not require finite anchors at intermediate marked points.

## Evidence, bindings and replay

Read `SPEC.md`, `result.json`, `schema-audit.json`,
`independent-verification.json`, `marked-through-summary.json`, `colors.tsv`
and `physical-witness.json`. The latter contains all local blue-five paths,
virtual closures and all 300 endpoint dynamic-program tables. Raw solver and
audit streams, process receipts, source identities and invocation claim remain.

The original worker collects its `result.json` bindings before its final
print, so that snapshot records `run.stdout` as empty. The final completion
line is written afterward. This exact one-file timing difference is preserved
and checked; the final `MANIFEST.json` binds the stable actual stream.
Core CNF/model/color/witness/verifier bindings all match exactly. The frozen
worker was not edited to alter this behavior.

`h17-complete-evidence.tgz` retains all Linux artifacts; `h17-replay.tgz`
retains the actual CNF, full model, colors/witnesses, all receipts and source,
omitting only the unused SAT-run `proof.drat`. That file is not an UNSAT
certificate and is retained in the full Linux archive with its hash.
`RETENTION.json` states the exact split. No DRAT checker success is claimed
for a SAT run.

Replay only in a fresh directory on Linux, preserving the frozen files:
`/opt/anaconda3/envs/forktqiu3/bin/python3.12 -B probe.py`.
The create-only worker refuses an existing formula. This describes replay;
the authorized execution above was the only run performed here. Windows
performed only source copies, SSH/SFTP control, archive extraction and hashes.
