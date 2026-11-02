# Paired core-interface replacement with unchanged seven-route matrices

Date: 2026-10-12. A new complete 60-vertex eight-regular graph was generated
by simultaneously replacing core interfaces 01 and 23 and retaining the
previously constructed exact 4--5 route partition. It has **175 bad pairs**
and diameter three. One subsequent exact assembly call returned
**RAW_UNSAT** in 0.025319 CPU seconds. No proof file or checked UNSAT claim
is attached to this call, and it was not repeated.

## Why this boundary change is structurally different

The preceding
[boundary-rigidity proof](PETERSEN_FOUR_FIBER_REASSEMBLY.md)
forces the old 01 matching if all nine interfaces outside the module
\(\{0,1,4,5\}\) remain fixed. We now change 23, one of those nine, while
preserving the two identical fixed routes from 4 through 2 or 3 to 5.
Changing 23 changes the fixed eight-route boundary rows used by that proof;
it therefore does not repeat the closed six-interface input.

For any interface define its seven-route matrix

\[
L_{ij}(M)=M+P_iM+MP_j.
\]

In the new assembly, the four intermediate routes from 2 to 3 are still
fixed. The routes through 4 and 5 are an identical permutation \(\Psi\);
write the other two as \(R_0,R_1\). The row budget of eleven route slots
then forces

\[
L_{23}(M)=J-\Psi-R_0-R_1.
\tag{1}
\]

The right side is exactly the original \(L_{23}\). Thus an arbitrary
replacement for 23 would immediately violate a necessary local equation.
Instead, the experiment enumerated the complete matching domain of (1).
For an arrow \(u\mapsto v\), its seven contributions occupy

\[
\{(u,v)\}\cup\{(w,v):w\sim_{P_2}u\}
\cup\{(u,w):w\sim_{P_3}v\}.
\]

An arrow is allowed only when these seven cells lie in the required
support. Backtracking chooses one arrow in each row and column and requires
their seven-cell sets to be pairwise disjoint. A complete assignment fills
all seventy required cells, so this is both necessary and sufficient for
(1), with no omitted permutation.

The complete 23 domain has just two solutions, obtained in 22 nodes:

\[
\begin{aligned}
M_{23}^{\rm old}&=(0,3,9,2,8,6,7,5,4,1),\\
M_{23}^{\rm new}&=(8,4,7,3,1,0,2,6,9,5).
\end{aligned}
\]

Coordinates here and below are local labels 0,...,9. The new matching
changes every row while preserving the complete seven-route matrix.
The analogous complete local domain for 01 has two solutions, in 24 nodes:

\[
\begin{aligned}
M_{01}^{\rm old}&=(2,5,4,6,0,9,1,8,3,7),\\
M_{01}^{\rm new}&=(7,0,8,4,1,3,2,9,6,5).
\end{aligned}
\]

The 01 equation is a deliberate seed-design restriction; the subsequent
SAT call allows every matching on 01 except the original matching. It
does not force this particular new 01 solution.

## Complete constructed graph and actual failure

Use the exact two-channel decomposition \(Q_0,Q_1\) from the preceding
four-fiber experiment. Replace both core matchings by their new local
solutions above. This produces a simple graph with 60 vertices, 240 edges,
and degree eight everywhere, replacing forty original edges by forty
edges. No fiber deletion yields HS50. Independent BFS finds 175 bad pairs,
all at distance three; total cycle energy is 208.

The three disjoint interface blocks 01,23,45 all have zero bad pairs and
zero energy. The remaining failures are:

| Block | Bad pairs | Energy |
|---|---:|---:|
| 02 | 19 | 19 |
| 03 | 10 | 11 |
| 04 | 9 | 10 |
| 05 | 29 | 41 |
| 12 | 10 | 13 |
| 13 | 16 | 16 |
| 14 | 10 | 11 |
| 15 | 21 | 29 |
| 24 | 8 | 10 |
| 25 | 16 | 18 |
| 34 | 9 | 10 |
| 35 | 18 | 20 |

This is an actual failure of common assembly despite three exact local
blocks. It is neither an improved lower bound nor a graph closer in bad-pair
count to the original twenty-pair seed.

## One bounded exact assembly call

Fix the new \(M_{23}\) and the other eight original interfaces outside
\(\{01,04,05,14,15,45\}\). All six listed interfaces are arbitrary independent
perfect matchings, with the original 01 matching forbidden. The exact 4--5
partition remains necessary because the routes through 2 and 3 are still
the original identical \(\Phi\).

The encoding is the same direct-edge/two-edge coverage construction as in
the preceding report, but its actual fixed edge set now contains ten new
23 edges. It has 10,600 variables and 68,161 clauses, including 690 direct
coverage clauses and 32,550 clauses added for the exact 4--5 partition.
The new boundary produces forty more coverage clauses than the old input.
The saved input is consequently not the previously closed CNF.

The single CaDiCaL call had a 25-CPU-second limit, one pinned CPU, and 4 GiB
memory limit. It returned exit code 20 in 0.025319 CPU seconds and
0.133348342 wall seconds. No proof file was written; **RAW_UNSAT** is the
precise solver status. No rerun or certificate upgrade was performed.

A small subsequent read-only boundary diagnostic found mixed missing-set
sizes two and three. The very simple proposed test requiring three missing
labels in both boundary fibers with fewer than two compatible twin
signatures did not fail at any source. This diagnostic does not provide a
new analytic exclusion; the RAW solver result is not promoted through it.

Resources were: local 23 domain 0.001102477 CPU seconds; preparation,
including the 01 domain, 0.102172317 parent CPU seconds plus 0.030758
independent-BFS child CPU seconds, 0.141748626 wall seconds; the optional
read-only boundary diagnostic 0.000746247 CPU seconds. All processes have
finished. This scope remains separate from the later binary-palette
enumeration, which changes all fifteen interfaces but restricts each to its
own fixed seven-route matrix.

Artifacts:

- [23-domain source](../../../computations/dd82/construction/petersen_paired_core_exchange.py)
  and [complete local result](../../../computations/dd82/construction/petersen_paired_core_exchange_run/domain.json).
- [Construction and solver source](../../../computations/dd82/construction/petersen_paired_core_reassembly.py),
  [both local domains](../../../computations/dd82/construction/petersen_paired_core_reassembly_run/core_domains.json),
  [complete seed with edits](../../../computations/dd82/construction/petersen_paired_core_reassembly_run/seed.json),
  [edge list](../../../computations/dd82/construction/petersen_paired_core_reassembly_run/seed.edges),
  [full independent BFS](../../../computations/dd82/construction/petersen_paired_core_reassembly_run/seed.verification.json),
  [block diagnostic](../../../computations/dd82/construction/petersen_paired_core_reassembly_run/seed.diagnostic.json).
- [Actual encoding](../../../computations/dd82/construction/petersen_paired_core_reassembly_run/encoding.json),
  [CNF](../../../computations/dd82/construction/petersen_paired_core_reassembly_run/input.cnf),
  [result](../../../computations/dd82/construction/petersen_paired_core_reassembly_run/result.json),
  [solver log](../../../computations/dd82/construction/petersen_paired_core_reassembly_run/solver.log).
- [Boundary diagnostic source](../../../computations/dd82/construction/petersen_paired_core_boundary_witness.py)
  and [actual rows](../../../computations/dd82/construction/petersen_paired_core_reassembly_run/boundary_rectangles.json).
