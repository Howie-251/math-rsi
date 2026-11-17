# Separated red-five lock blocks: five blocks are checked impossible

2026-11-17. Linux-only exact local certificate. The necessary system for five
strictly ordered five-point red blocks is **checked UNSAT**, with every clause
independently audited against the intended finite specification. Subject to the
caller's proved extraction of q physical ordered red-five blocks with no
cross-block red five and no blue six, this yields **q <= 4**. Weak seven is not
needed for this exclusion. This is a local lock-family bound, not by itself
the original 74-point theorem or a new independent acceptance of its upstream
extraction theorem.

The actual Linux root is
`/data/ktqiu_hdd/math_agent/reports/n7-shared-arm-replay-20261117/lock-blocks`.
All code ran on `ubun` with `/opt/anaconda3/envs/forktqiu/bin/python3.10`.
The production solver was
`/data/ktqiu_hdd/math_agent/AE_kissat2025_MAB/build/kissat`, as required.
Existing external checker:
`/data/ktqiu_hdd/math_agent/cadical-sc2025/build/drat-trim`.

## Exact input and original-input connection

For q blocks, order vertices 0,...,5q-1 and let block i be
{5i,...,5i+4}. A positive variable means the corresponding increasing triple is
red. Variables cover every triple, in lexicographic order. The complete CNF has:

* Every internal triple of every block red.
* For every increasing four-point packet, its four colors have at most one
  change. All eight forbidden assignments are explicitly excluded.
* For every five-point subset not contained in one block, its three consecutive
  triple colors cannot all be red.
* For every six-point subset, its four consecutive triple colors cannot all be
  blue.

In a rank-3 signotope, a monochromatic consecutive-triple path is all-triples
monochromatic. Thus any actual input supplied by the caller's extraction
theorem gives a satisfying assignment of this necessary CNF. Preserving the
physical block order and forbidding **every** cross-block red five are essential
upstream hypotheses. A checked contradiction of the five-block system excludes
five extracted blocks and, by selecting any five blocks, every larger q.

## Actual computation and checks

| q | Variables | Clauses | Pure UP | Additional actual outcome |
| ---: | ---: | ---: | --- | --- |
| 6 | 4060 | 955575 | conflict, 3 rounds / 1510 units | RUP proof checked |
| 5 | 2300 | 331475 | no conflict, 7 rounds / 826 units | default Kissat UNSAT, proof checked |
| 4 | 1140 | 93060 | no conflict, 3 rounds / 320 units | full weak-seven-free actual SAT model, independently checked |
| 3 | 455 | 18955 | no conflict, 3 rounds / 144 units | no solver needed after the four-block witness |

For q=5 the source `up_small.py` first reached a genuine unit-propagation
fixpoint. A separately authorized controlled external solve then returned exit
20 and `s UNSATISFIABLE` in 0.164783 seconds. Its exact binary DRAT proof is
`q5/solver-proof.drat`, 3,830,851 bytes, SHA256
`0032af8edd0ff572b3d76440e3634dbcf289afedf4f8f8666b086e3300e3cf30`.
The external checker returned exit zero and **s VERIFIED** in 0.666562 seconds.
Its log reports 92 original clauses and 22 lemmas in the proof core, using 373
resolution steps. This is an actual successful checker, not a raw UNSAT claim.

The binding q=5 CNF SHA256 is
`e976ac4f3fa118e369ee3ee33c2017969999e7b6f58ff949ddf1aeb11cd87df4`.
Its 331475 clauses consist of 50 block-red units, 101200 packet clauses,
53125 cross-block red-five clauses and 177100 blue-six clauses.

`audit_core.py` separately regenerated the complete expected specification,
compared **every clause in order**, checked all triple-variable identities and
file end, and replayed every exported unit step with its actual original-CNF
reason clause. The q=5/4/3 audits all returned PASS and exit zero. The q=6 audit
did the same for all 955575 clauses and its complete unit contradiction.

## Small six-block hand certificate

The first q=6 contradiction forces a blue six
`(7,13,14,15,16,22)`. Its causal unit core uses only 36 original clauses and
35 variables, including 17 internal-red units. It uses **no packet clause**:
the remaining deductions use cross-block red-five and blue-six prohibitions.
The short extracted `first/core.cnf` and `first/core.drat` were independently
checked again by drat-trim, exit zero / s VERIFIED. The readable 35-step unit
chain is `first/core-readable.txt`; original rows, actual triples and reason
clauses are in `first/core-readable.json`.

Although that final blue six itself meets four blocks, its derivation uses all
six blocks. It does not prove the four-block system impossible. A standalone
hand-readable derivation is provided in `HAND_PROOF_Q6.md`.

## Raw evidence

`evidence.tgz` returns complete CNFs, exact triple maps, unit traces, q=6 full
and small proofs, the q=5 checked proof, all checker and solver logs, all exit
files, all independent encoding audits, and source hashes. Its Linux SHA256 is
`5a7eb329b28a8ddd7e966bee2314b5b3da9c5126ff33884cf737e6d1a2e74b31`.
Transport and command receipts are in the parent `receipts/lock-*.json`.
Scientific code never ran on Windows; Windows only edited files, transported
artifacts and checked bytes. Old report evidence and production code are
unchanged.

Recheck the key result on Linux:

```bash
/opt/anaconda3/envs/forktqiu/bin/python3.10 audit_core.py q5
/data/ktqiu_hdd/math_agent/cadical-sc2025/build/drat-trim \
 q5/formula.cnf q5/solver-proof.drat
```

The q<=4 local family bound is established relative to the stated upstream
extraction. Any stronger q<=3 or q<=2 claim requires its own actual evidence.

## Completed lower calibration: four blocks are genuinely feasible

The newly authorized bounded completion found an actual 20-point ordered
rank-3 signotope with four ordered red-five blocks, no cross-block red five,
no blue six, and no weak seven. The first necessary-system SAT model had weak
seven violations; it was not accepted as a full model. `weak_cex.py` added 51
valid same-end weak-seven clauses over 16 short default-Kissat calls. Each cut
is the negation of a particular blue/red path pair with common endpoints and
length sum nine. All seven vertices and every literal are preserved in
`weak-completion/q4/cuts.json`. The final model is
`weak-completion/q4/iter015-colors.json`, SHA256
`7e91c62e641eee929d54b8aed3f8fb03c5ed1052b255e61b5b21a62549e78639`.

The separate `audit_weak.py` enumerated all monochromatic four-, five- and
six-point subsets using **all** their triples, checked all 4845 packets and
each internal block, and excluded both same-end B4/R5 and B5/R4 combinations.
It found B4=1273, R4=156, B5=583, exactly four R5 (the four prescribed blocks),
and B6=R6=0. Thus weak seven is absent. It additionally verified all 51 cuts
against their original actual counterexample colorings and checked the precise
CNF bytes/bindings of all 16 iterations. Its actual result is PASS, exit zero.

Therefore four is the **exact maximum for this abstract block projection**.
The witness does not realize four original forward/mirror locks or satisfy
unmentioned upstream lock hypotheses. It prevents reducing the bound to three
using only these four-block, no-cross-R5, no-B6, packet and weak7 properties.
No q=3 solve was needed: any three blocks of this actual model provide the
corresponding smaller calibration.

The complete remote `weak-evidence.tgz` has Linux SHA256
`89d18a95673079e3f7fc56c44b59b481d2c6bb48b9fd308d059e4216d1392ee5`.
Its first transfer timed out because it included all unneeded SAT proof streams;
the returned partial bytes are preserved as `weak-evidence.partial.tgz`, and
that partial archive is not accepted evidence. The remote complete archive is
unchanged. The successful smaller return `weak-evidence-light.tgz` has matching
Linux/local SHA256
`8f8208a4ed1b0d05e784f9da48341ee6b3125c4800343e89ad1b70432d63e5ed`.
It retains every candidate coloring, actual formula, solver log, cut list,
independent audit, execution output and exits, with a manifest of the omitted
SAT proof stream sizes. Those streams are not used for any UNSAT assertion;
all q=5 UNSAT evidence is already returned in the separate first archive.
All research and transport processes have completed.
