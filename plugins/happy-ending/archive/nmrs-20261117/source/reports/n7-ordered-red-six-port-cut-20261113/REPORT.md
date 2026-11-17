# Six-by-six ordered port-cut projection is compatible

**Result: verified SAT at (|U|,|V|)=(6,6).** The specified necessary
12-point projection does not exclude two six-point pools. The test stopped
here: 6/5 and 5/5 were not launched. This result yields no reduction of the
current general center-selection fee 11 and does not prove that fee optimal.

The frozen physical order is U={1,2,3,4,5,6} < V={7,8,9,10,11,12}.
The [complete 220-triple coloring](6-6/colors.tsv) is an ordered rank-3
signotope satisfying every requested predicate in [SCOPE.md](SCOPE.md).
Its longest red and blue paths both have four vertices. U has exactly one
red four-path, (1,2,3,6), and V has none. All six blue four-paths lie wholly
inside one pool. No ambient suppliers, red-six anchors or additional
same-terminal-pair restrictions were introduced.

The three red-five prohibitions (inside U, inside V, and across the cut)
together exclude every induced R5 in this 12-point domain. The formula
retains separate groups for their physical meanings. Weak7 uses the same
outer endpoints and red/blue lengths summing to 9; paths are not required
to have disjoint interiors. Every packet is checked in standard ordered
triple order. The simultaneous-R4 prohibition is included explicitly as
requested, even though it is known redundant for actual cut projections.

## Raw evidence and checks

- [Linux run and source/binary bindings](runtime.json),
  [solver/check receipts](6-6/result.json), and
  [complete Kissat output](6-6/solve.stdout).
- [CNF](6-6/formula.cnf): 220 physical color variables, no auxiliaries,
  54,426 distinct clauses. True means red.
- [Independent complete schema reconstruction](6-6/schema-audit.json):
  PASS, zero missing and zero extra clauses; verifier imports no builder.
- [Independent physical verification](6-6/independent-verification.json):
  PASS for the complete assignment, all clauses, all packets, R7/B6,
  weak7, both pools' R5/B5, crossing R5, mixed B4, and simultaneous R4.
  It enumerated **all 4,083 subsets of sizes 2 through 12**, computing every
  actual monochromatic path and every exact endpoint length, without
  relying on SAT auxiliaries or a path-shortening assumption.
- [Full physical path/endpoint witness](6-6/physical-witness.json):
  red path counts at lengths 2/3/4 are 66/152/119; blue counts are 66/68/6.
  There are no paths of either color of length at least 5.

Kissat ran on the authoritative Linux server as a controlled external process
with a 60-second solver budget and a 75-second process timeout. It returned
exit code 10 after 8.5921 seconds. Schema and physical audits returned exit
code 0. The retained `proof.drat` contains the solver's SAT-run trace and is
**not** an UNSAT certificate; no UNSAT or DRAT-check claim is made.

Primary hashes:

| Artifact | SHA256 |
|---|---|
| probe.py | c5f861c823383154f5de827cb60a6abbc3f7f153d81fa6225d544182819809bf |
| verify.py | 09ff0fe8e698dc7985168de9428bfbcb40a9f7203581ebda1ab5131c126b0d0d |
| formula.cnf | ef93c80f7c1b1fa09da07828d44576cda648cadb48f31ffc469d66f2010b44fd |
| colors.tsv | 3443ae1269ef86f6c964ea5ef3977861fc195e324da239543c582ff801d82503 |

## Interpretation and return to caller

The supplied necessary projection is consistent. Consequently, an argument
excluding simultaneous six-point cut pools must use additional proved
consequences of their real ambient red-six suppliers, rather than these
12-point conditions alone. This witness does not realize those suppliers,
does not establish a 75-point extension, and supplies no planar coordinates.
It does not contradict a stronger true-cut theorem. No external review was
requested or run, and no general mathematical claim was upgraded.

Sources: [old general-cut proof §7](../n7-shared-crossing-and-joint-charts-20261107/PROOF.md)
and the caller's current explicit necessary-projection specification. This
directory is the only task output; prior campaigns, evidence and jobs remain
unchanged.

To replay, copy `probe.py`, `verify.py`, and `SCOPE.md` into a **fresh** Linux
directory and run its `probe.py` using the bound Python and existing binaries
in `runtime.json`. The driver is create-only and must not rerun in this sealed
directory. To recheck the frozen case without solving, invoke `verify.py`
with `--root <absolute-path>/6-6 --schema`, then with `--sat`, on Linux.
