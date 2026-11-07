# Complete Closure fixed-rule run: FAIL in control harness

The single authorized Linux invocation exited **1**, after **8.648002411006019
seconds**. It completed all fixed-row checks, then stopped with
`KeyError: 'core_source_nonempty'` in `controls()`. No repair or rerun was made.
The complete SSH/SFTP transport finished in 132.156 seconds; its duration
includes uploading inputs and downloading the 27,489,878-byte mapped ledger.
The scientific invocation stayed within its 120-second / 3-GiB limits.
Max RSS was 136,208 KiB; user/system CPU were 8.478969 / 0.13192099999999998
seconds. Stderr was empty.

## Completed evidence, before the failure

All **151,801 name rows** decoded with the exact source codec. Semantic keys
had no duplicates; dictionary indices are based at zero. All **190,932 rule
rows** decoded, passed their exact source `Valid` predicates, and had every
surviving symbolic atom mapped to the decoded dictionary. Every source
constant reduction was nontrivial; no row was skipped.

| Wire group | Source family | Rows checked |
|---|---|---:|
| 0 | base | 77,368 |
| 1 | ambient | 21,238 |
| 2 | core | 30,987 |
| 3 | low | 1,922 |
| 4 | counting | 1,561 |
| 5 | packet | 54,009 |
| 6 | terminal | 649 |
| 7 | prefix | 3,198 |

The full result contains per-constructor counts and per-group wire, symbolic
and mapped-ledger hashes. `mapped_rule_rows.jsonl` preserves every original
row index, raw wire and reduced dictionary literals.

## Exact failure and missing cases

The harness incorrectly assumed there would be an actual nonempty
`sourceAttain` row available to mutate. The complete acquired fixed rule
table has **no sourceAttain or sourceForward rows**. It also has **no low
impossible or counting internalBound rows**. These constructors have source
translations in the implementation but received no fixed-row exercise.
The missing sourceAttain example caused the harness lookup to raise after
the first three controls. This is a harness inventory assumption failure,
not a reported Valid or atom-mapping counterexample.

Completed controls rejected: omitted base pairChoice label; ambient name 39;
core witness slot 7. Remaining controls did **not** run: omitted sourceAttain
successor, omitted witness successor, low name bound, counting zero threshold,
population tag, invalid packet indices, terminal cover omission, prefix sector
omission and unsupported wire group. Thus the full control suite remains
incomplete and the overall result remains FAIL.

## Bindings and limits

- Parser SHA256: `7e641a902c61f81c9dfde7e366517b38611b0b12a2768ac6c50cfd2bfea36fc5`.
- Raw result SHA256: `429dcf100849b06a459570137354d8a69a0b7367a9ef02aad2977142c9a6ecbf`.
- Full mapped ledger SHA256: `0ad49d462a9c48a45c8ec4fedd95e678e4d69d7335983cedb27251daa776e238`.
- Decoded names SHA256: `0703b14efacf7d4a2bcc76b4ac6d612fc121624b30115b6389780e70734ca752`.
- Exact snapshots and original paths: `input_manifest.json`, repeated in
  `result.json`. Original sources and the prior prefix directory were read-only.

This supplies retained fixed-row evidence before a failed control harness.
Actual Closure CNF equality and UNSAT remain unchecked because ClosureLiteral
is unavailable. Universal semantic lifting and population dependencies remain
main-session obligations. There was no solver, replay, acquisition, Lean
compilation, independent review, acceptance update, or second validation.
