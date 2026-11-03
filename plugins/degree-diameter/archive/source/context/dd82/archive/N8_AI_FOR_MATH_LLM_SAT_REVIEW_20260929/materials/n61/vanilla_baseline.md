# Degree 8, Diameter 2, Order 61: Current SAT Results

**Snapshot date:** 2026-08-23  
**Overall status:** incomplete; no 61-vertex graph has been found, and global
nonexistence has not been proved.

## 1. Problem and complete rooted reduction

We ask whether there is a finite simple graph $G$ satisfying

\[
|V(G)|=61,\qquad \Delta(G)\le 8,\qquad \operatorname{diam}(G)\le 2.
\]

Every such graph is necessarily 8-regular. Indeed, a vertex of degree at most
7 can reach at most

\[
1+7+7\cdot 7=57
\]

vertices within distance two. Hence a candidate has 244 edges.

For a vertex $v$, let $t(v)$ be the number of triangles containing $v$.
The local defect identity is

\[
2t(v)+\sum_{w\in N_2(v)}
  \bigl(|N(v)\cap N(w)|-1\bigr)=4.
\]

Thus $t(v)\le2$. There must be a vertex $r$ with $t(r)\le1$, since
$t(v)=2$ for all 61 vertices would give $3T=122$.

Fix such a root and label

\[
r=0,\qquad X=N(r)=\{1,\ldots,8\},\qquad
Y=V(G)\setminus(\{r\}\cup X),\quad |Y|=52.
\]

For $y\in Y$, define its parent set $P(y)=N(y)\cap X$, and put
$H=G[X]$. The rooted defect equation becomes

\[
2|E(H)|+\sum_{y\in Y}(|P(y)|-1)=4.
\]

After quotienting by relabelings of $X$, the search consists of 60 rooted
templates:

| Root type | Exceptional parent-size profile | Orbits | Closed | Open |
|---|---:|---:|---:|---:|
| $H=\varnothing$ | $[5]$ | 1 | 1 | 0 |
| $H=\varnothing$ | $[4,2]$ | 3 | 3 | 0 |
| $H=\varnothing$ | $[3,3]$ | 4 | 3 | 1 |
| $H=\varnothing$ | $[3,2,2]$ | 14 | 6 | 8 |
| $H=\varnothing$ | $[2,2,2,2]$ | 23 | 2 | 21 |
| $H=\{1,2\}$ | $[3]$ | 3 | 3 | 0 |
| $H=\{1,2\}$ | $[2,2]$ | 12 | 3 | 9 |
| **Total** |  | **60** | **21** | **39** |

Here an “exceptional” parent set has size at least two. All remaining points
of $Y$ have singleton parent sets, whose multiplicities are forced by the
degrees of the vertices in $X$.

## 2. SAT encoding used in the run

For each rooted template, all edges incident with $r$ or $X$ are fixed.
Only the

\[
\binom{52}{2}=1326
\]

possible edges inside $G[Y]$ are primary variables. The CNF enforces:

1. exact degree $8-|P(y)|$ inside $Y$ for every $y\in Y$;
2. every uncovered $X$--$Y$ pair has a path of length at most two;
3. every pair of $Y$-vertices without a shared parent is adjacent or has a
   common neighbor in $Y$;
4. the local defect upper bound for every vertex of $X$;
5. a permutation-symmetry reduction inside each singleton-parent fiber.

The 60 formulas contain 88,398--89,048 variables and 223,330--233,342 clauses
each. The implementation is
`degree_diameter_sat/n61_all_templates_cnf.py`.

The run used 55 single-threaded workers for 72 hours. Solver attempts used:

- AE-kissat2025-MAB / Kissat 4.0.2;
- CaDiCaL sc2025, default and `--unsat` configurations.

The attempt schedule was 2 hours, then 8 hours, then the remaining global
budget. Across all 60 templates, the run consumed approximately 2,992.7
solver-hours. No SAT model was returned.

## 3. All 21 closed templates

In the table below, $H$ is the fixed graph on $X$. The listed parent sets
are the exceptional sets $P(y)$; singleton parent sets are omitted. “Final
time” is the decisive UNSAT attempt, while “total time” includes earlier
timed-out attempts for the same template.

| Case | $H$ | Exceptional parent sets | Vars | Clauses | Decisive solver | Final time | Total time | Evidence |
|---|---|---|---:|---:|---|---:|---:|---|
| `t0_01_p5` | ∅ | {1,2,3,4,5} | 88,398 | 224,052 | AE-Kissat | 0:08 | 0:08 | raw UNSAT |
| `t0_02_p4_2` | ∅ | {1,2,3,4}; {1,2} | 88,448 | 225,671 | CaDiCaL-unsat | 1:39:37 | 3:39:38 | raw UNSAT |
| `t0_03_p4_2` | ∅ | {1,2,3,4}; {1,5} | 88,398 | 224,450 | AE-Kissat | 4:20 | 2:04:20 | raw UNSAT |
| `t0_04_p4_2` | ∅ | {1,2,3,4}; {5,6} | 88,398 | 223,330 | AE-Kissat | 2:51 | 2:51 | raw UNSAT |
| `t0_05_p3_3` | ∅ | {1,2,3}; {1,2,3} | 88,498 | 227,081 | AE-Kissat | 19:43 | 10:19:44 | raw UNSAT |
| `t0_06_p3_3` | ∅ | {1,2,3}; {1,2,4} | 88,448 | 226,049 | AE-Kissat | 6:23:09 | 8:23:09 | raw UNSAT |
| `t0_08_p3_3` | ∅ | {1,2,3}; {4,5,6} | 88,398 | 224,086 | CaDiCaL-unsat | 2:37:52 | 4:37:52 | raw UNSAT |
| `t0_09_p3_2_2` | ∅ | {1,2,3}; {1,2}; {1,2} | 88,548 | 228,267 | AE-Kissat | 4:32:53 | 6:32:53 | raw UNSAT |
| `t0_10_p3_2_2` | ∅ | {1,2,3}; {1,2}; {1,3} | 88,498 | 227,977 | CaDiCaL-unsat | 51:37:45 | 61:37:46 | raw UNSAT |
| `t0_11_p3_2_2` | ∅ | {1,2,3}; {1,2}; {1,4} | 88,448 | 226,945 | AE-Kissat | 26:02:31 | 36:02:32 | raw UNSAT |
| `t0_20_p3_2_2` | ∅ | {1,2,3}; {4,5}; {4,5} | 88,448 | 226,203 | AE-Kissat | 55:01 | 10:55:01 | raw UNSAT |
| `t0_21_p3_2_2` | ∅ | {1,2,3}; {4,5}; {4,6} | 88,398 | 224,982 | AE-Kissat | 5:35:38 | 7:35:38 | raw UNSAT |
| `t0_22_p3_2_2` | ∅ | {1,2,3}; {4,5}; {6,7} | 88,398 | 223,862 | CaDiCaL-unsat | 8:16:26 | 18:16:27 | raw UNSAT |
| `t0_23_p2_2_2_2` | ∅ | {1,2}; {1,2}; {1,2}; {1,2} | 88,698 | 233,342 | CaDiCaL-unsat | 8:35 | 2:08:35 | raw UNSAT |
| `t0_24_p2_2_2_2` | ∅ | {1,2}; {1,2}; {1,2}; {1,3} | 88,548 | 231,919 | AE-Kissat | 44:59 | 2:44:59 | raw UNSAT |
| `t1_01_p3` | {1,2} | {1,2,3} | 88,998 | 228,023 | AE-Kissat | 0.31 s | 0.31 s | direct local contradiction |
| `t1_02_p3` | {1,2} | {1,3,4} | 88,998 | 227,019 | CaDiCaL-default | 59:45 | 59:45 | raw UNSAT |
| `t1_03_p3` | {1,2} | {3,4,5} | 88,998 | 225,989 | AE-Kissat | 6:48:08 | 8:48:09 | raw UNSAT |
| `t1_04_p2_2` | {1,2} | {1,2}; {1,2} | 89,048 | 229,455 | AE-Kissat | 0.33 s | 0.33 s | direct local contradiction |
| `t1_05_p2_2` | {1,2} | {1,2}; {1,3} | 88,998 | 228,246 | CaDiCaL-default | 0.36 s | 0.36 s | direct local contradiction |
| `t1_07_p2_2` | {1,2} | {1,3}; {1,3} | 89,048 | 228,449 | AE-Kissat | 8:20 | 8:20 | raw UNSAT |

The decisive UNSAT calls used approximately 117.0 solver-hours. Including
earlier attempts that reached their limits, these 21 templates used
approximately 185.0 solver-hours.

## 4. Three templates with a direct local contradiction

The following three eliminations do not require trusting the internal search
of a SAT solver. For every vertex $x$,

\[
2e(G[N(x)])+
\sum_{z\notin N[x]}\bigl(|N(z)\cap N(x)|-1\bigr)=4.
\]

In each case below, terms already fixed by the rooted template exceed four:

- `t1_01_p3`: for $x=1$ and $x=2$, there are already two fixed edges in
  $G[N(x)]$ and at least one unit of repeat excess, giving $2\cdot2+1=5$.
- `t1_04_p2_2`: for $x=1$ and $x=2$, there are already three fixed edges
  in $G[N(x)]$, giving $2\cdot3=6$.
- `t1_05_p2_2`: for $x=1$, there are already two fixed neighborhood edges
  and at least one unit of repeat excess, again giving 5.

Thus these three rooted templates are mathematically impossible once the
root-template classification is accepted.

## 5. Remaining 39 templates

The unresolved templates are

\[
\begin{aligned}
&\texttt{t0\_07},\\
&\texttt{t0\_12},\ldots,\texttt{t0\_19},\\
&\texttt{t0\_25},\ldots,\texttt{t0\_45},\\
&\texttt{t1\_06},\texttt{t1\_08},\ldots,\texttt{t1\_15}.
\end{aligned}
\]

All 39 reached the 72-hour global deadline. They must be reported as
unresolved, not SAT and not UNSAT.

## 6. Exact evidentiary status

There are two distinct levels of result:

1. **Direct mathematical contradiction:** 3 templates (`t1_01`, `t1_04`,
   `t1_05`). Their local fixed contribution already violates the defect
   identity.
2. **Solver-level or raw UNSAT:** 18 additional templates. A mature SAT solver
   returned exit code 20 and printed `UNSATISFIABLE`, but the run did not
   request a DRAT/LRAT proof trace and no independent proof checker was run.

Consequently the correct current claim is:

> Subject to the complete 60-template rooted reduction, 3 templates have a
> direct local contradiction, 18 additional templates have reproducible
> solver-level UNSAT results, and 39 templates remain unresolved. No
> 61-vertex candidate graph has been found.

It is not yet correct to claim that 21 branches have independently certified
UNSAT proofs, or that order 61 has been globally excluded.

## 7. Reproducibility locations

- Generator and model verifier:
  `degree_diameter_sat/n61_all_templates_cnf.py`
- Ordered 60-instance manifest:
  `degree_diameter_sat/results/n61_all_templates/manifest.jsonl`
- Run state:
  `degree_diameter_sat/results/n61_all_templates/runs/20260816T140107Z/state.json`
- Final progress snapshot:
  `degree_diameter_sat/results/n61_all_templates/progress.json`
- Per-attempt solver logs:
  `degree_diameter_sat/results/n61_all_templates/runs/20260816T140107Z/logs/<case>/`
- Queue implementation:
  `degree_diameter_sat/run55/run_n61_template_queue.py`

The next certificate-quality step is to rerun the 18 raw-UNSAT templates with
proof output enabled and check each trace independently. This still would not
settle order 61 until the remaining 39 templates were also closed or a valid
SAT model were found.
