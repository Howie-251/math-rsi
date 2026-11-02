# N59 `c1`: Partial Raw-UNSAT Ledger and Theory Handoff

**Snapshot:** 2026-08-31 02:27 UTC  
**Overall status:** `UNRESOLVED`  
**Purpose:** summarize the current theory-guided SAT evidence for the connected repeat-support branch and identify the next useful human lemmas.

This document is deliberately named **partial raw UNSAT**. It does not claim that the `c1` branch, the 59-vertex case, or any SAT result has been certified.

## 1. Mathematical setting and notation

Assume that $G$ is an 8-regular graph on 59 vertices with diameter at most two. Let $A$ be its adjacency matrix and define

\[
B=A^2+A-7I-J.
\]

Then $B$ is a symmetric nonnegative integral matrix with zero diagonal and

\[
B\mathbf 1=6\mathbf 1.
\]

For distinct vertices $u,v$,

\[
B_{uv}=
\begin{cases}
|N(u)\cap N(v)|,&u\sim v,\\
|N(u)\cap N(v)|-1,&u\not\sim v.
\end{cases}
\]

The present report concerns only the branch

\[
c1:\qquad \operatorname{supp}(B)\text{ is connected}.
\]

Let $t(v)$ be the number of triangles containing $v$. The imported theory handoff gives

\[
m:=\min_v t(v)\le 2.
\]

Choose a minimum-triangle root $r$, set $P=N(r)$, and write $X=N_2(r)$. Thus $|P|=8$, $|X|=50$, and $H=G[P]$ has exactly $m$ edges. For $x\in X$, define

\[
S_x=N(x)\cap P,
\qquad
e_x=|S_x|-1=B_{rx}.
\]

The root identity is

\[
\sum_{x\in X}e_x=6-2m.
\]

In the case names:

- `defect_partition` is the multiset of positive $e_x$;
- `exception_parent_sets` are the corresponding sets $S_x$;
- `o####` indexes the orbit under $\operatorname{Aut}(H)$, including permutations of exceptional vertices with equal defect;
- parent labels in this report are local labels $0,\ldots,7$ on $P$;
- for `K2`, $E(H)=\{01\}$; for `2K2`, $E(H)=\{01,23\}$; for `P3`, $E(H)=\{01,02\}$.

## 2. What `RAW_UNSAT` means here

Every raw result below is one Kissat run returning the standard UNSAT exit code 20. The exploratory run did not generate a proof trace, so these are not independently checkable UNSAT certificates.

The reduced CNF intentionally omits the nonbipartiteness condition on $\operatorname{supp}(B)$, and may initially omit connectivity cuts. These omissions form a relaxation. Consequently, UNSAT of the relaxation is a sound exclusion **conditional on the correctness of the encoding and imported branch reduction**. The missing proof trace is why the status remains `RAW_UNSAT` rather than `CERTIFIED_UNSAT`.

No SAT model, disconnected-support model, bipartite-support model, build error, solver error, or queue error had appeared at the snapshot time.

## 3. Exact campaign snapshot

Run directory:

```text
/inspire/hdd/global_user/mahaitong-240108120090/mathagent/degree_diameter_sat/results/n59_c1_theory_v2/runs/c1_cpusolver--ba06158a4078-k6qilaokty_20260830T102815Z
```

Run configuration:

```text
54 solver workers
4 concurrent lazy CNF builders
6-hour timeout per case
18-hour campaign window
```

The complete canonical manifest contains 1,077 cases: 55 exact static rejections and 1,022 solver-ready cases.

| Branch | Canonical | Static rejected | Raw UNSAT | Timeout | Running at snapshot | Not run | Current interpretation |
|---|---:|---:|---:|---:|---:|---:|---|
| `m0_b5_present` | 4 | 0 | 4 | 0 | 0 | 0 | raw-closed |
| `m0_b5_absent` | 684 | 4 | 0 | 0 | 0 | 680 | open |
| `m1_b4_present` | 3 | 1 | 2 | 0 | 0 | 0 | static/raw-closed |
| `m1_b4_absent` | 326 | 34 | 39 | 106 | 54 | 93 | open |
| `m2_double_present` | 11 | 2 | 9 | 0 | 0 | 0 | static/raw-closed |
| `m2_double_absent` | 49 | 14 | 35 | 0 | 0 | 0 | static/raw-closed |
| **Total** | **1,077** | **55** | **89** | **106** | **54** | **773** | **UNRESOLVED** |

The 55 static rejections and 89 raw UNSAT cases must not be conflated. At this evidence level they exclude 144 of the 1,077 canonical cases, but only 89 of those exclusions came from the solver.

The overlapping static-rejection reasons were:

| Static condition | Number of occurrences |
|---|---:|
| fixed repeat-row lower bound exceeds 6 | 54 |
| fixed base triangle count exceeds 3 | 11 |
| fixed $B$ entry exceeds the branch cap | 10 |
| fixed nonedge $B$ entry exceeds the branch cap | 11 |
| fixed adjacent $B$ entry exceeds 3 | 4 |

One case may trigger more than one reason, so these occurrences sum to more than 55.

## 4. Strongest current solver-level reduction

The key result is not merely that 89 individual jobs returned UNSAT. All solver-ready cases in the high-repeat and $m=2$ families have returned raw UNSAT, while their remaining orbit cases were rejected statically.

### 4.1 The complete $m=2$ branch is raw/static closed

The theory splits $m=2$ into:

- a doubled nonedge-repeat edge: 11 canonical cases, of which 2 are static and 9 raw UNSAT;
- no doubled nonedge-repeat edge: 49 canonical cases, of which 14 are static and 35 raw UNSAT.

Thus all 60 canonical $m=2$ cases are excluded at the current solver level:

\[
60=16\text{ static}+44\text{ raw UNSAT}.
\]

### 4.2 The two high-repeat endpoint branches are raw/static closed

- If $m=0$ and some $B_{uv}=5$, the four exhaustive semantic cases `M_k0`, `M_k1`, `M_k2`, and `P_k0` are all raw UNSAT.
- If $m=1$ and some $B_{uv}=4$, the three five-parent-set orbits consist of one static rejection and two raw UNSAT cases.

### 4.3 Conditional solver-suggested statement

Conditional on the imported branch-tree theorem and the reduced encoding, every surviving `c1` candidate must therefore satisfy

\[
\boxed{
c1\text{ candidate}
\Longrightarrow
\begin{cases}
m=0\text{ and }\max B_{uv}\le4,\\
\text{or}\\
m=1\text{ and }\max B_{uv}\le3.
\end{cases}}
\]

This is the most useful statement to hand to a theorist. It is not yet a theorem because 50 of the 67 exclusions supporting it are raw rather than certified:

\[
67=17\text{ static}+50\text{ raw UNSAT}.
\]

## 5. Partial progress inside $m=1, B\le3$

The extra 39 raw UNSAT cases lie inside `m1_b4_absent`. They do not close a complete defect partition.

| Defect partition | Canonical | Static | Raw UNSAT | Timeout | Running | Not run |
|---|---:|---:|---:|---:|---:|---:|
| $(3,1)$ | 20 | 4 | 0 | 0 | 0 | 16 |
| $(2,2)$ | 19 | 4 | 0 | 0 | 0 | 15 |
| $(2,1,1)$ | 119 | 12 | 14 | 0 | 31 | 62 |
| $(1,1,1,1)$ | 168 | 14 | 25 | 106 | 23 | 0 |

The queue order explains why $(3,1)$ and $(2,2)$ were not run; this is not evidence that they are intrinsically harder.

For partition $(1,1,1,1)$, regard the four exceptional two-parent sets as the four edges of a multigraph $F$ on $P$, with the distinguished edge $01=E(H)$. All 25 raw UNSAT cases found in this stratum satisfy

\[
\Delta(F)\ge3.
\]

Among the attempted cases with $\Delta(F)\le2$, none closed quickly; they occur in the timeout/running residue. This is a controlled computational pattern, not a proved implication. It suggests testing the candidate lemma

\[
\text{feasibility in the }(1,1,1,1)\text{ stratum}
\Longrightarrow \Delta(F)\le2,
\]

and then studying the remaining path, cycle, matching, and repeated-edge shapes directly.

## 6. Recommended theory questions

### Target A: replace all 60 $m=2$ orbit cases by one proof

Try to prove directly that a `c1` candidate cannot have $m=2$. Available structure includes:

\[
t(v)\in\{2,3\},
\qquad
\sum_{u\not\sim v}B_{uv}=6-2t(v),
\]

so the nonedge-repeat multigraph on the $t=2$ vertices is a disjoint union of simple cycles and doubled edges. In addition,

\[
n_2:=|\{v:t(v)=2\}|>0,
\qquad
n_2\equiv0\pmod3,
\qquad
B+4I\succeq0.
\]

The no-$K_4$ result, connected/nonbipartite support of $B$, and the clean isolated-parent color-cover rule may provide the missing global contradiction.

### Target B: prove the high-repeat exclusions uniformly

Try to establish the two statements

\[
m=0\Longrightarrow B_{uv}\ne5,
\qquad
m=1\Longrightarrow B_{uv}\ne4.
\]

For $B_{uv}=5$, the two-vertex $B$-support cut has exactly two outgoing unit contributions, and the local graph reduces to the four `M/P` types listed below. For $B_{uv}=4$, the root has a unique triangle and only three five-parent-set orbits. The raw closures suggest that both orbit enumerations may be shadows of shorter row-sum or Gram-matrix arguments.

### Target C: compress the remaining $m=1,B\le3$ parent configurations

Instead of analyzing hundreds of SAT cases independently:

1. treat the exceptional parent sets as a small hypergraph on the eight root neighbors;
2. derive restrictions from the fixed $B$-row budget, triangle budget, and clean-color cover;
3. first attempt analytic exclusion of the only 31 solver-ready cases in partitions $(3,1)$ and $(2,2)$;
4. for $(1,1,1,1)$, classify $F$ by degree sequence and interaction with the distinguished edge $01$.

### Target D: do not brute-force the 680 $m=0,B\le4$ cases yet

The solver has not entered this family. Its ready cases split as follows:

| Defect partition | Ready cases |
|---|---:|
| $(4,2)$ | 4 |
| $(4,1,1)$ | 14 |
| $(3,3)$ | 5 |
| $(3,2,1)$ | 28 |
| $(3,1,1,1)$ | 64 |
| $(2,2,2)$ | 15 |
| $(2,2,1,1)$ | 116 |
| $(2,1,1,1,1)$ | 240 |
| $(1,1,1,1,1,1)$ | 194 |

A useful next theoretical step would eliminate all $e_x=4$ or $e_x=3$ cases, or turn the clean isolated-parent color-cover rule into a bound depending only on the defect partition.

## 7. Suggested SAT-to-theory feedback step

Before running the remaining hundreds of cases, rerun a small, structurally representative subset of the already raw-closed cases with proof output and clause-origin labels. The immediate goal is not full certification; it is to identify small repeated contradictions that can be translated into lemmas.

Good representatives include:

- `c1_m0_b5_present_M_k1`, the fast $B=5$ matching type;
- `c1_m0_b5_present_M_k2`, the much slower $B=5$ intersection type;
- `c1_m1_b4_present_k2_lam_4_o0002`;
- one `2K2` and one `P3` case from each $m=2$ branch;
- one concentrated and one balanced exceptional-parent pattern from `m1_b4_absent`.

The clause groups worth tracing are: $B$-row sum, nonedge-repeat budget, exact triangle count, clean-color cover, Gram 3-point cuts, and no-$K_4$. A short contradiction using the same groups across several orbit representatives is a plausible human lemma candidate.

## 8. Exact 89-case raw UNSAT ledger

`Wall` is the total task wall time recorded in `result.json`; it includes CNF construction and possible waiting for one of the four build slots, so it is not an exact solver-only time.

### 8.1 `m0_b5_present` — 4 raw UNSAT

| Case ID | Root / partition | Exceptional parent sets | Wall (s) |
|---|---|---|---:|
| `c1_m0_b5_present_M_k0` | empty / (5,1) | {0,1,2,3,4,5}; {6,7} | 1074.036 |
| `c1_m0_b5_present_M_k1` | empty / (5,1) | {0,1,2,3,4,5}; {0,6} | 344.204 |
| `c1_m0_b5_present_M_k2` | empty / (5,1) | {0,1,2,3,4,5}; {0,1} | 16605.905 |
| `c1_m0_b5_present_P_k0` | empty / (5,1) | {0,1,2,3,4,5}; {6,7} | 1380.189 |

`M_k0` and `P_k0` have the same parent sets but different semantic cubes and are distinct cases.

### 8.2 `m1_b4_present` — 2 raw UNSAT

| Case ID | Root / partition | Exceptional parent sets | Wall (s) |
|---|---|---|---:|
| `c1_m1_b4_present_k2_lam_4_o0002` | K2 / (4) | {0,2,3,4,5} | 258.446 |
| `c1_m1_b4_present_k2_lam_4_o0003` | K2 / (4) | {2,3,4,5,6} | 1027.348 |

The omitted orbit `o0001`, with parent set `{0,1,2,3,4}`, is statically rejected by a fixed repeat-row lower bound exceeding 6.

### 8.3 `m2_double_present` — 9 raw UNSAT

| Case ID | Root / partition | Exceptional parent sets | Wall (s) |
|---|---|---|---:|
| `c1_m2_double_present_2k2_lam_2_o0001` | 2K2 / (2) | {0,1,2} | 228.845 |
| `c1_m2_double_present_2k2_lam_2_o0002` | 2K2 / (2) | {0,1,4} | 2817.068 |
| `c1_m2_double_present_2k2_lam_2_o0003` | 2K2 / (2) | {0,2,4} | 1183.131 |
| `c1_m2_double_present_2k2_lam_2_o0004` | 2K2 / (2) | {0,4,5} | 3053.430 |
| `c1_m2_double_present_2k2_lam_2_o0005` | 2K2 / (2) | {4,5,6} | 3513.137 |
| `c1_m2_double_present_p3_lam_2_o0003` | P3 / (2) | {1,2,3} | 4677.683 |
| `c1_m2_double_present_p3_lam_2_o0004` | P3 / (2) | {0,3,4} | 765.120 |
| `c1_m2_double_present_p3_lam_2_o0005` | P3 / (2) | {1,3,4} | 528.504 |
| `c1_m2_double_present_p3_lam_2_o0006` | P3 / (2) | {3,4,5} | 3917.357 |

The two remaining `P3` orbits, `o0001` and `o0002`, are statically rejected.

### 8.4 `m2_double_absent` — 35 raw UNSAT

#### Root type `2K2`

| Orbit | Exceptional parent sets | Wall (s) |
|---|---|---:|
| `o0001` | {0,1}; {0,1} | 536.577 |
| `o0002` | {0,1}; {0,2} | 3607.042 |
| `o0003` | {0,1}; {2,3} | 930.173 |
| `o0004` | {0,1}; {0,4} | 2529.373 |
| `o0005` | {0,1}; {2,4} | 4624.971 |
| `o0006` | {0,1}; {4,5} | 467.769 |
| `o0008` | {0,2}; {1,2} | 701.223 |
| `o0009` | {0,2}; {1,3} | 1392.537 |
| `o0010` | {0,2}; {0,4} | 3015.530 |
| `o0011` | {0,2}; {1,4} | 725.317 |
| `o0012` | {0,2}; {4,5} | 2298.339 |
| `o0014` | {0,4}; {1,4} | 1969.566 |
| `o0015` | {0,4}; {2,4} | 1158.724 |
| `o0016` | {0,4}; {0,5} | 4174.516 |
| `o0017` | {0,4}; {1,5} | 2319.993 |
| `o0018` | {0,4}; {2,5} | 6014.890 |
| `o0019` | {0,4}; {4,5} | 1490.034 |
| `o0020` | {0,4}; {5,6} | 2113.226 |
| `o0022` | {4,5}; {4,6} | 4446.843 |
| `o0023` | {4,5}; {6,7} | 1610.668 |

Every row has full case-ID prefix `c1_m2_double_absent_2k2_lam_1-1_`. The missing orbit IDs `o0007`, `o0013`, and `o0021` are statically rejected.

#### Root type `P3`

| Orbit | Exceptional parent sets | Wall (s) |
|---|---|---:|
| `o0005` | {0,1}; {1,3} | 2550.841 |
| `o0006` | {0,1}; {2,3} | 2206.296 |
| `o0007` | {0,1}; {3,4} | 2072.091 |
| `o0013` | {0,3}; {1,3} | 5539.036 |
| `o0014` | {0,3}; {0,4} | 3241.921 |
| `o0015` | {0,3}; {1,4} | 5081.635 |
| `o0016` | {0,3}; {3,4} | 5758.962 |
| `o0017` | {0,3}; {4,5} | 1728.710 |
| `o0019` | {1,3}; {2,3} | 2763.655 |
| `o0020` | {1,3}; {1,4} | 1420.210 |
| `o0021` | {1,3}; {2,4} | 3938.792 |
| `o0022` | {1,3}; {3,4} | 2575.809 |
| `o0023` | {1,3}; {4,5} | 1262.695 |
| `o0025` | {3,4}; {3,5} | 2677.945 |
| `o0026` | {3,4}; {5,6} | 2440.223 |

Every row has full case-ID prefix `c1_m2_double_absent_p3_lam_1-1_`. The other 11 `P3` orbits are statically rejected.

### 8.5 `m1_b4_absent` — 39 partial raw UNSAT

#### Partition $(1,1,1,1)$: 25 cases

| Orbit | Exceptional parent sets | Wall (s) |
|---|---|---:|
| `o0014` | {0,1}; {0,2}; {0,2}; {1,2} | 3840.850 |
| `o0046` | {0,2}; {0,2}; {0,2}; {1,2} | 3461.607 |
| `o0047` | {0,2}; {0,2}; {0,2}; {0,3} | 831.901 |
| `o0049` | {0,2}; {0,2}; {0,2}; {2,3} | 324.622 |
| `o0051` | {0,2}; {0,2}; {1,2}; {1,2} | 3307.736 |
| `o0070` | {0,2}; {0,2}; {2,3}; {2,3} | 8901.563 |
| `o0126` | {0,2}; {2,3}; {2,3}; {2,3} | 41.858 |
| `o0128` | {0,2}; {2,3}; {2,3}; {3,4} | 42.277 |
| `o0134` | {0,2}; {2,3}; {3,4}; {3,4} | 54.199 |
| `o0135` | {0,2}; {2,3}; {3,4}; {3,5} | 41.998 |
| `o0141` | {0,2}; {3,4}; {3,4}; {3,4} | 53.865 |
| `o0142` | {0,2}; {3,4}; {3,4}; {3,5} | 97.157 |
| `o0145` | {0,2}; {3,4}; {3,5}; {3,6} | 138.323 |
| `o0149` | {2,3}; {2,3}; {2,3}; {2,4} | 39.025 |
| `o0150` | {2,3}; {2,3}; {2,3}; {4,5} | 84.897 |
| `o0151` | {2,3}; {2,3}; {2,4}; {2,4} | 70.659 |
| `o0152` | {2,3}; {2,3}; {2,4}; {3,4} | 139.685 |
| `o0153` | {2,3}; {2,3}; {2,4}; {2,5} | 159.780 |
| `o0154` | {2,3}; {2,3}; {2,4}; {3,5} | 188.126 |
| `o0155` | {2,3}; {2,3}; {2,4}; {4,5} | 181.975 |
| `o0156` | {2,3}; {2,3}; {2,4}; {5,6} | 211.686 |
| `o0160` | {2,3}; {2,4}; {3,4}; {3,5} | 344.605 |
| `o0162` | {2,3}; {2,4}; {2,5}; {2,6} | 263.148 |
| `o0163` | {2,3}; {2,4}; {2,5}; {3,6} | 335.339 |
| `o0164` | {2,3}; {2,4}; {2,5}; {6,7} | 201.188 |

Every row has full case-ID prefix `c1_m1_b4_absent_k2_lam_1-1-1-1_`.

#### Partition $(2,1,1)$: 14 cases

| Orbit | Exceptional parent sets | Wall (s) |
|---|---|---:|
| `o0007` | {0,1,2}; {0,2}; {1,2} | 348.426 |
| `o0011` | {0,1,2}; {0,2}; {3,4} | 3021.833 |
| `o0013` | {0,1,2}; {0,3}; {1,3} | 126.207 |
| `o0019` | {0,1,2}; {0,3}; {4,5} | 6771.708 |
| `o0021` | {0,1,2}; {2,3}; {2,4} | 34.136 |
| `o0022` | {0,1,2}; {2,3}; {3,4} | 2602.575 |
| `o0023` | {0,1,2}; {2,3}; {4,5} | 30.006 |
| `o0024` | {0,1,2}; {3,4}; {3,4} | 751.437 |
| `o0025` | {0,1,2}; {3,4}; {3,5} | 31.060 |
| `o0026` | {0,1,2}; {3,4}; {5,6} | 37.947 |
| `o0035` | {0,2,3}; {0,2}; {0,2} | 46.748 |
| `o0052` | {0,2,3}; {2,3}; {2,3} | 34.231 |
| `o0053` | {0,2,3}; {2,3}; {2,4} | 38.088 |
| `o0054` | {0,2,3}; {2,3}; {4,5} | 33.788 |

Every row has full case-ID prefix `c1_m1_b4_absent_k2_lam_2-1-1_`.

## 9. Timing summary

The following values summarize recorded total wall time for raw UNSAT jobs; they are useful only as rough indicators of structural difficulty.

| Family | Raw cases | Median wall (s) | Maximum wall (s) |
|---|---:|---:|---:|
| `m0_b5_present` | 4 | 1227.113 | 16605.905 |
| `m1_b4_present` | 2 | 642.897 | 1027.348 |
| `m2_double_present` | 9 | 2817.068 | 4677.683 |
| `m2_double_absent` | 35 | 2319.993 | 6014.890 |
| partial `m1_b4_absent` | 39 | 139.685 | 8901.563 |

The long tail in `m1_b4_absent/(1,1,1,1)` is qualitatively different from the complete high-repeat and $m=2$ closures. This supports stopping broad enumeration temporarily and asking for a structural compression.

## 10. Provenance and unresolved dependencies

The implementation and local tests establish agreement between the supplied JSON/specification, the canonical manifest, the reduced formulas, and the queue. They do not independently prove every mathematical input used to construct the branch tree.

The following files named by the expert handoff were not present in the local handoff material inspected for this implementation:

```text
N59_THEORY_CONTINUATION_C1_20260828.md
n59_c1_t3_audit.py
n59_c1_t3_audit_output.txt
n59_c1_t3_quotient_independent.py
n59_c1_t3_quotient_independent_output.txt
n59_c1_t3_circulant_exhaustive.py
n59_c1_t3_circulant_exhaustive_output.txt
n59_c1_sat_compiler_audit.py
n59_c1_sat_compiler_audit_output.txt
```

Accordingly, this report imports rather than locally reproves the following claims:

- $\min_v t(v)\le2$;
- no $K_4$ in `c1`;
- the high-repeat endpoint/root-selection lemmas;
- completeness of the $B=5$, $B=4$, and $m=2$ branch splits;
- the special $B=5$ `M/P` classification;
- the clean isolated-parent rule and the full Gram-derived package.

The most useful response from the theory side would therefore be:

1. supply or independently audit those missing dependencies;
2. attempt Targets A and B as uniform mathematical lemmas;
3. use the exact raw ledger above to propose a smaller structural split for the remaining $m=1,B\le3$ cases.

## 11. Reproducible source locations

```text
Case manifest:
degree_diameter_sat/results/n59_c1_theory_v2/c1_case_manifest.json

Job manifest:
degree_diameter_sat/results/n59_c1_theory_v2/c1_jobs.json

Campaign snapshot and per-case results:
degree_diameter_sat/results/n59_c1_theory_v2/runs/
  c1_cpusolver--ba06158a4078-k6qilaokty_20260830T102815Z/

Theory branch generator:
degree_diameter_sat/sat59/theory/c1_high_repeat_splits.py

Reduced encoder:
degree_diameter_sat/sat59/branches/c1_reduced.py

Independent model verifier:
degree_diameter_sat/sat59/verify/verify_c1_model.py
```

To regenerate a machine-readable ledger from the run directory:

```bash
cd /inspire/hdd/global_user/mahaitong-240108120090/mathagent/degree_diameter_sat

python3 -m sat59.jobs.collect_c1_results \
  --run-dir results/n59_c1_theory_v2/runs/c1_cpusolver--ba06158a4078-k6qilaokty_20260830T102815Z \
  --output results/n59_c1_theory_v2/runs/c1_cpusolver--ba06158a4078-k6qilaokty_20260830T102815Z/c1_ledger.json
```

No proof-producing rerun has yet been performed for these 89 cases.
