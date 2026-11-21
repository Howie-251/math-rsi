# Exact replay entry

From the repository root on Linux, with Python 3.10 or newer (standard library
only):

```bash
python3 -B plugins/happy-ending/tools/verify_nmrs.py > nmrs-replay.json
```

The command reads only the supplied archive and prints JSON. A successful run
exits 0 with `status=PASS_BOUNDED_EXACT_REPLAY`. The corrected portable entry was executed successfully on macOS on
2026-11-21; Linux execution remains pending. The original preparation had no
execution because its Linux server was unreachable. See
[VERIFICATION.md](VERIFICATION.md).

It recomputes the following directly from public inputs:

- All endpoint profiles for five retained normalized seeds at heights
  44, 45, 48, 56, 64, and the historical height-44 seed. The accepted height-64
  file is `inputs/window/normalized-a5-v64-repaired.json`.
- The old row/private face predicates, all 123410 union profiles, their exact
  objectives and transported partial red-hole cost; then the integer nested-window
  recurrence at every height 44 through 1024 and the named-envelope examples
  at 64, 100, 128, 256, 1024. The two old comparators are reported separately.
- Sector-budget arithmetic for m=8,9,10, and the ten-parameter incidence
  contradiction. The sector equation alone gives Q8<=293; Q8<=292 needs the
  additional common-budget mathematical bridge.
- Every triple and four-packet and exact same-endpoint path maxima of the
  supplied actual 36-point and 17-point signotopes. For owners 5 and 6 of the
  17-point example it checks the incoming red-six prefix and **every** actual
  red-seven / blue-six path, including the common lock 12.
- Each of the 6126 supplied scalar types, distinctness, all displayed scalar
  predicates, and the h=0,...,187 envelope giving maximum 292. It does not
  regenerate a complete scalar listing or realize any type as a signotope.
- Consistency of the retained 866/858 success records, frozen 866 source hashes,
  reconstructed CNF identities and two saved 858 checker logs. This step reads
  historical receipts; it does not rerun DRAT.

A useful negative control is the preserved rejected raw height-64 seed:

```bash
python3 -B plugins/happy-ending/tools/verify_nmrs.py \
  --seed plugins/happy-ending/archive/nmrs-20261120/inputs/window/rejected-v64.json
```

Expected: nonzero exit with `ValueError: infeasible face`. This negative control was executed on macOS on 2026-11-21 and produced the
expected failure. The old source's successful and
failed checks are documented in the original preparation record.

For an independent source directory preserving Git symbolic links, create a
`git archive HEAD` **after committing the prepared files**, extract it on Linux,
and run the above command there. Do not archive the Windows working directory:
its Git symbolic-link entries may be text placeholders. Then run:

```bash
python3 -B tools/check_links.py
python3 -B tools/build_public_site.py --output /tmp/nmrs-public-site \
  --report /tmp/nmrs-public-site-report.json
```

Use a fresh output directory. The site builder checks its exact public allowlist
and local references; it does not publish. These two repository checks are also
pending Linux execution for the final prepared tree.

## Large historical proofs

The archive includes inspection sources and compact records for ordinary
N(8,6,6)<=56 and N(8,5,8)<=64, not their multi-gigabyte CNF/proof streams or every
historical builder dependency. It is **not** a self-contained replay of those
upper bounds. A separate acquisition of the exact original streams and a
compatible `drat-trim` is required. File identities are in
[evidence/866/seal.json](evidence/866/seal.json) and
[evidence/858/ordinary858-64-final-receipt.json](evidence/858/ordinary858-64-final-receipt.json).

| Historical formula | CNF bytes | Proof bytes | Historical checks |
|---|---:|---:|---|
| 866 / 57-point full physical query | 1920462700 | 2608906477 | one successful DRAT; separate byte-identical reconstruction |
| 858 / 65-point query | 170799880 | 2438439752 | two successful processes using the same checker implementation; separate byte-identical reconstruction |

After acquiring these exact files, verify their SHA256 against those records
and run, in a controlled external process with a fresh log:

```bash
"$DRAT_TRIM" "$ACQUIRED_CNF" "$ACQUIRED_PROOF" -t 2147483647 > fresh-checker.log 2>&1
```

A checked result requires exit 0 and the actual successful checker output tied
to those files. A hash, saved `VERIFIED`, raw UNSAT, or reconstructed CNF alone
is not a new proof check. No large proof was rerun for this preparation.

Private workspace prefixes in compact evidence JSON were replaced with
`<private-linux-workspace>`; the original and public-projection identities are
listed in [PUBLIC_PROJECTIONS.json](evidence/PUBLIC_PROJECTIONS.json). Scientific
hash fields and saved checker logs are unchanged. Inputs retain their original bytes except the scalar list, which is only gzip-decompressed. Five inspection source snapshots also contain neutral private-path placeholders: they are source projections, not self-contained runnable builders. The checker verifies the public projection hashes separately and binds the recorded historical original hashes to the original source records. Unchanged sources are hashed against their original records directly. [PUBLIC_INPUT_MAP.json](PUBLIC_INPUT_MAP.json) records the
source-to-package mapping. No credentials or SSH configuration are needed for
these portable commands.
