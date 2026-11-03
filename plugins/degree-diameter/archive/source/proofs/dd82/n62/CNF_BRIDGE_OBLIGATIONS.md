# Order-62 A+B CNF bridge obligations

## Result and scope

**The inspected A+B encoding admits a complete paper-level satisfiability-preservation argument for the seven supplied, correctly interpreted templates. No constraint was found that unjustifiably discards an original graph in those templates.** The argument and its exact preconditions are below. This is a source review, not an UNSAT result or a completed Lean encoding bridge.

Two qualifications materially affect the proof:

1. The guarded exact-count helper is exact only under a threshold-depth condition. All actual A+B call sites meet that condition; its unrestricted docstring should not be treated as a theorem for arbitrary callers.
2. Some mathematical properties of the input JSON, including the formula for remaining degrees and the exact singleton classes, are consumed rather than comprehensively checked by the generator. The seven actual archived entries satisfy these properties; a theorem about an arbitrary schema-valid JSON would be too strong.

The generator is self-contained Python standard library code. A new representative base CNF can be generated from the supplied source and template JSON without the old project or solver installations. The current project also contains CaDiCaL 2.1.2 with LRAT output support and Lean's verified LRAT checker definitions. Original DIMACS instances, original variable maps, leaf clauses, and proof traces were not found in the extracted archive. They cannot be inferred from progress summaries.

This task read code and performed only small read-only metadata checks plus `cadical --help`/`--version`. It generated no CNF, ran no SAT instance, installed nothing, and did not access old external project paths.

## Inspected inputs

Let `ARCHIVE` denote `context/dd82/archive/N8_AI_FOR_MATH_LLM_SAT_REVIEW_20260929/` relative to this project.

* `ARCHIVE/code/n62/n62_ab_cnf.py`: read in full, including primitive encoders, all clause families, data loading, and command-line generation.
* `ARCHIVE/theory/n62/n62_root_templates.json`: the concrete seven-template input.
* `ARCHIVE/code/n62/n62_ab_resume_partition.py`: previously read in full; its mathematical symmetry coverage is recovered in `RECOVERED_REDUCTION.md`.
* `ARCHIVE/code/n62/n62_ab_verify.py`: read in full; it checks reconstructed original graphs independently of counter auxiliaries.
* `ARCHIVE/code/n62/n62_sms_solver.py` and `sms_n62_distance_main.cpp`: inspected only to distinguish the separate SMS path and its missing dependencies from the self-contained A+B path.

The principal code line references below refer to `n62_ab_cnf.py`.

## 1. Precise bridge statement

For one of the seven concrete templates $\tau$, let $F_\tau$ be the ordered clause list emitted by `ABEncoder(τ, emitter).encode()` and let $G$ be a simple graph on the labeled vertex set $\{0,\ldots,61\}$ satisfying:

* every degree is 8 and the diameter is at most 2;
* the fixed root, root-neighbor edges, parent sets, exceptional-point restrictions, and local double-repeat restrictions of $\tau$;
* $B=A^2+A-7I-J$ has values in $\{0,1,2\}$, or $\{0,1\}$ in a simple-$B$ template;
* the justified triangle and parity properties of that branch.

Then

$$\exists\alpha:\operatorname{Vars}(F_\tau)\to\{0,1\},\qquad \alpha\models F_\tau.$$

The extra bullet points are not restrictions on the original theorem: `RECOVERED_REDUCTION.md` supplies a relabeling into some template and derives these properties from the original graph. The two separate proof steps must be composed. An arbitrary original candidate is not assumed already labeled like one fixed template.

Conversely, for these concrete templates, any satisfying assignment of $F_\tau$ reconstructs an 8-regular graph of diameter at most 2 by taking the primary edge variables and the template-fixed edges. This reverse statement is useful to detect an underencoding, although only the forward statement is necessary when transferring UNSAT to nonexistence.

The following sections give the forward witness assignment and justify every emitted clause family. Formalizing the implementation-to-clause-list correspondence remains work.

## 2. Original variables and fixed pairs

Put $X=\{1,\ldots,8\}$ and $Y=\{9,\ldots,61\}$. There are 1,378 primary variables $e_{uv}$, one for each unordered pair in $Y$. Assign

$$e_{uv}=A_{uv}.$$

The root edges, $X$-internal edges, and $X$–$Y$ edges are constants determined by the template. All unordered pairs not containing 0 and not wholly in $X$ are dynamic repeat pairs: $424$ pairs in $X\times Y$ and $1,378$ pairs in $\binom Y2$, for $1,802$ pairs total. For each assign

$$b^1_{uv}=[B_{uv}=1],\qquad b^2_{uv}=[B_{uv}=2],$$

omitting $b^2$ in simple-$B$ branches. Assign $\tau_u=[t(u)=1]$.

The 61 root pairs and 28 $X$-internal pairs have fully template-determined common-neighbor counts, despite the unknown $Y$-internal graph. For a root pair, every potentially unknown factor is multiplied by a zero root–$Y$ entry; for an $X$-internal pair, both incident edges to every possible common neighbor are fixed. Thus `_constant_common_count` and `_compute_fixed_B_values` (lines 268–295) compute their actual $B$ values. No pair is omitted from the semantics by avoiding dynamic variables for these 89 pairs.

The static checks ensure that these constant repeat values are nonnegative and within the selected branch range. Therefore their diameter constraints also hold in the reverse direction.

## 3. Auxiliary primitives and their actual contracts

### AND gates

`add_iff_and` (line 79) emits

$$\neg z\lor a,\quad\neg z\lor b,\quad z\lor\neg a\lor\neg b.$$

These are equivalent to $z=a\land b$. Setting every gate to its indicated Boolean function extends an original-graph assignment and satisfies all three clauses.

### XOR gates

`add_iff_xor` (line 85) emits the four clauses excluding exactly the assignments with $z\ne a\oplus b$. It is a full equivalence. Its outputs can be assigned recursively by prefix parity.

### Truncated unary thresholds

For input literals $\ell_1,\ldots,\ell_n$ and maximum depth $m$, `unary_thresholds` (line 92) constructs prefix variables

$$T_{i,k}=\left[\sum_{j\le i}\operatorname{truth}(\ell_j)\ge k\right],\quad 1\le k\le\min(i,m).$$

Its recurrence is

$$T_{i,1}=T_{i-1,1}\lor\ell_i,$$
$$T_{i,k}=T_{i-1,k}\lor(\ell_i\land T_{i-1,k-1})\quad(k\ge2),$$

with missing previous thresholds interpreted as false. At the first threshold and at a newly reachable level, the code emits the corresponding OR or AND equivalence. At an existing higher level it emits

$$\neg a\lor z,\quad\neg\ell_i\lor\neg b\lor z,\quad
\neg z\lor a\lor\ell_i,\quad\neg z\lor a\lor b,$$

where $a=T_{i-1,k}$ and $b=T_{i-1,k-1}$. These are exactly $z\leftrightarrow a\lor(\ell_i\land b)$. Induction on $i$ proves the threshold interpretation at every retained level. Truncation is harmless because the recurrence for level $k$ uses only levels $k$ and $k-1$.

Inputs need not be independent variables. Repeated occurrences contribute repeatedly to the integer sum, exactly as required when a $b^2$ selector is included twice. Signed literals are also covered by the truth-value interpretation. A returned `None` denotes an unreachable threshold and therefore false, not an unspecified auxiliary variable.

### Guarded exact counts: the necessary depth premise

`enforce_exact_under_condition` (line 146) negates the conjunction of its guard literals and appends the required sign of every supplied threshold. An impossible target $t<0$ or $t>n$ emits the negation of the guard, which correctly says that this state cannot occur.

For a feasible target $0\le t\le n$, the supplied thresholds enforce an exact count provided they include level $t+1$ when $t<n$, or level $n$ when $t=n$. The special case $n=t=0$ needs no threshold. Equivalently, retaining levels through $\min(n,t+1)$ suffices.

Without that premise the helper is not universally exact: retaining only the first two thresholds with target 3 and four inputs permits an actual count of 2. This is not a bug at an actual call site here:

| Call site | Feasible target bound | Threshold depth | Why sufficient |
|---|---:|---:|---|
| Core pair equation | $t=1+B-A-f\le3$ | $\min(4,n)$ | includes $t+1$ unless $t=n$ |
| Triangle membership | $t=0-f$ or $2-f\le2$ | $\min(3,n)$ | same argument |

Negative targets are explicitly forbidden, and oversized targets are explicitly forbidden. The proof must use these bounds rather than the helper's broad docstring alone.

`enforce_exact` (line 167) independently chooses $m=\min(n,t+1)$, asserts threshold $t$ when $t>0$, and forbids threshold $t+1$ when $t<n$. Its zero-target and empty-input cases are correct. Invalid targets emit an empty clause; for an actual graph meeting its branch conditions those invalid calls cannot occur.

## 4. Every clause family and its original-graph justification

| Encoder method | Emitted meaning | Required justification |
|---|---|---|
| `_encode_template_units`, line 348 | Fixed extra edges/nonedges, repeat values, triangle membership | The seven-template relabeling theorem and the local double-repeat lemma |
| Same method, parent-intersection units | $w$ has no neighbor whose parent set meets its triple parent set | Otherwise a triangle contains $w$; a double-repeat endpoint is triangle-free |
| `_encode_B_selectors`, line 386 | $\neg(b^1\land b^2)$ | $B$ has a single integer value |
| Same method, adjacent-$B=2$ prohibition | $A_{uv}=1\Rightarrow B_{uv}\ne2$ | An adjacent pair has $B_{uv}=c_{uv}$; two common neighbors give two triangles at each endpoint |
| `_encode_degrees`, line 401 | $\deg_Y(y)=8-|P(y)|$ | Correct remaining-degree metadata and 8-regularity |
| `_encode_core_pair_equations`, line 443 | $f_{uv}+q_{uv}+A_{uv}=1+b^1_{uv}+2b^2_{uv}$ | Exact repeat identity and correct common-neighbor split |
| Same method, fourth-threshold prohibition | $q_{uv}\le3$ | From the identity, $B\le2$, $A\ge0$, $f\ge0$; no extra structural assumption |
| `_encode_B_row_sums`, line 475 | $\sum_v B_{uv}=3$ | $64+8-7-62=3$ |
| `_encode_triangle_membership`, line 516 | $\sum_v[A_{uv}=1\land B_{uv}=1]=2\tau_u$ | At most one triangle per vertex, and adjacent repeat entries at most 1 |
| Same method, optional global XOR | $\bigoplus_u\tau_u=1$ in the two S branches | Simple $B$ implies an odd triangle count; each triangle contributes three members |
| `_encode_double_local_counts`, line 560 | Exact counts from $w$ into selected singleton classes | The detailed double-edge classification in the recovered reduction |

For the core equation, `_fixed_f` counts common neighbors in $\{0\}\cup X$. For an $X$–$Y$ pair $(x,y)$, `_q_inputs` consists exactly of $e_{yz}$ for the points $z\ne y$ whose parent set contains $x$. This includes exceptional parent sets, not just the singleton class. For a $Y$–$Y$ pair it constructs one AND gate $e_{uk}\land e_{vk}$ for every $k\in Y\setminus\{u,v\}$. Thus the sum really is the remaining common-neighbor count.

The guards generated by `_B_states` deserve an explicit check. In a double branch they are $\neg b^1\land\neg b^2$, $b^1$, and $b^2$. The last two omit a negated other selector, but the separate at-most-one clause makes these three states mutually exclusive and exhaustive. Combining them with the two possible edge states gives exactly one active core equality. In a simple branch the two guards are just $\neg b^1,b^1$.

For repeat row sums, the input list contains $b^1$ once and $b^2$ twice. The constant contributions of fixed pairs are subtracted from target 3. Repetition is intentional and correctly handled by the unary recurrence.

For triangle membership, every pair contributes once to each endpoint. Fixed contributions are subtracted from the targets, dynamic original edges use an AND gate with $b^1$, and fixed original edges use $b^1$ directly. Both possible values of $\tau$ are guarded, so the equation is enforced rather than only implied in one direction. Optional parity is emitted only when the template supplies it; it is not a valid unconditional assumption for every double-$B$ branch.

All auxiliaries can now be assigned in creation order to the described Boolean functions and prefix counts. Their clauses hold; the graph identities and template lemmas satisfy all endpoint assertions and guards. This constructs the forward satisfying assignment.

For the reverse direction, the root and $X$ degrees are fixed at 8 by the audited template, the $Y$ degrees are enforced by exact counters, and every pair satisfies $c_{uv}+A_{uv}=1+B_{uv}\ge1$. Hence every pair is adjacent or has a common neighbor. No external lazy propagator is used by this A+B formula.

## 5. Template-data preconditions versus runtime checks

`load_manifest` (line 631) checks the schema, $n=62$, the declared seven-instance count, and seven distinct IDs. `_static_audit` checks the fixed root labels, the fixed degrees of $X$, the root repeat row sum, fixed repeat ranges, selected fixed-repeat consistency, and an edge/nonedge conflict case. These checks are useful but are not the seven-template coverage proof.

In particular `_encode_degrees` reads `residual_degree_inside_Y` directly; it does not recompute and compare it with $8-|P(y)|$. `_encode_double_local_counts` reads `singleton_classes` directly; the encoder does not independently check those sets equal the points with singleton parent set $\{x\}$.

A read-only check of the actual archived JSON confirmed, for every one of the seven entries and every relevant vertex/class:

$$\texttt{residual\_degree\_inside\_Y}[y]=8-|P(y)|,$$
$$\texttt{singleton\_classes}[x]=\{y\in Y:P(y)=\{x\}\}.$$

Thus these are satisfied concrete-input obligations, not discovered faults in these instances. The formal bridge should either prove these facts for the fixed template data or define the fields from the parent map, instead of quantifying over all JSON records accepted by the limited runtime validator.

The archive's additional descriptive fields, such as `triangle_free_at_w`, are not individually converted into clauses merely because they appear in JSON. Their relevant consequences are supplied by the actual triangle variables, fixed memberships, units, and local counts listed above. A metadata assertion is neither automatically an encoded condition nor automatically a theorem.

## 6. Symmetry and extra cuts

The A+B base generator contains no adjacency-row lex ordering, signature sorting, fiber-cap cuts, saturated-fiber cuts, component-connectivity assumption, or dynamic graph-isomorphism rejection. These belong to other historical encodings and must not be silently imported into this bridge.

Its normalization is the fixed root template itself, followed by the mathematically justified local units and counts already listed. Fixing labels is justified by the explicit relabeling theorem, not by assuming a nontrivial automorphism of a candidate graph.

The S_DISJOINT 80-case builder is separate. Its row assignments and endpoint cases require the symmetry-coverage proof in `RECOVERED_REDUCTION.md`. To transfer that proof to generated literals, the variable map must correctly identify the edge, repeat, and triangle variables. The 80 representatives cover actual graphs up to relabeling; unique task IDs and distinct literal lists alone do not prove coverage, and they do not constitute a partition of all labeled assignments.

If a base formula is certified directly, no old leaf partition is needed. If leaf formulas are certified, their exact appended clauses and their exhaustive cover must accompany the certificates. The historical S_TOUCH eight-leaf assumptions are absent from this extracted archive, as is the referenced `n62_ab_make_cubes.py`.

## 7. What can actually be regenerated

The imports of `n62_ab_cnf.py` are only Python standard library modules. Python 3.11.9 is available. No PySAT, SMT package, old graph-model module, solver binary, or network access is needed to emit a base DIMACS file.

The default input path in `main` is the nonexistent neighboring file `n62_root_templates_theory.json`. The supplied data instead live at `ARCHIVE/theory/n62/n62_root_templates.json`; an explicit argument resolves this packaging difference without modifying the archive.

For example, this command would regenerate only S_TOUCH, its variable map, statistics, and a one-case manifest (shown for a future task; **not executed here**):

```bash
python3 context/dd82/archive/N8_AI_FOR_MATH_LLM_SAT_REVIEW_20260929/code/n62/n62_ab_cnf.py \
  --template-manifest context/dd82/archive/N8_AI_FOR_MATH_LLM_SAT_REVIEW_20260929/theory/n62/n62_root_templates.json \
  --case-id S_TOUCH \
  --output-dir computations/dd82/n62/certification_base
```

The generation order is explicitly determined by the vertex loops and template lists. This permits fresh reconstruction from the available inputs; it does not establish equality with absent historical DIMACS files or variable maps. The old recorded variable/clause counts are useful comparisons but cannot identify a formula by themselves.

`--stats-only` still emits maps and statistics and does not emit the DIMACS needed by a proof-producing solver. The archived root-template Python script need not be run: its historical hard-coded output path is outside this proof's recovery route, and the actual JSON is already available.

The S_DISJOINT canonical partition builder can then use a newly generated one-case manifest, map, CNF, and the template JSON. It needs no solver library. Its `scope=all` alternative also expects three D-case bases, so a one-case manifest would not suffice for that mode.

## 8. Available proof-output and proof-checking components

The current project contains

```text
.tools/lean-4.24.0-linux/bin/cadical
```

Its observed version is **2.1.2**. Its actual help reports positional input/proof arguments, `--lrat` to select LRAT, `--frat`, and `--no-binary` to select text proof output. It is not on the current PATH, so a bare `cadical` command would not locate it. No new installation is needed for this binary.

A future proof-producing invocation could therefore have the form

```text
.tools/lean-4.24.0-linux/bin/cadical --lrat --no-binary INPUT.cnf OUTPUT.lrat
```

No such solver invocation was performed. Availability of a proof-output option does not establish that any particular instance will finish or that any existing RAW result has a corresponding proof.

The installed Lean source includes

```text
.tools/lean-4.24.0-linux/src/lean/Std/Tactic/BVDecide/LRAT/Checker.lean
```

with definitions in namespace `Std.Tactic.BVDecide.LRAT`:

```text
check (lratProof : Array IntAction) (cnf : CNF Nat) : Bool
check_sound : check lratProof cnf → cnf.Unsat
```

The associated parser, conversion, and internal soundness modules are present. This provides a concrete kernel-verified checker interface to investigate. The project has not yet connected an emitted order-62 clause list and an LRAT file to this theorem, established the parsing/clause-index correspondence, or evaluated a checker proof within the project's prohibition of `native_decide` and new axioms. No standalone external `drat-trim`/`lrat-check` binary was found by the scoped checks; the direct LRAT route avoids making their installation a prerequisite in this bounded assessment.

The separate SMS wrapper accepts `--lrat-output`, but it imports absent `n62_all_templates_cnf`, `n62_graph_model`, and `n62_lemma_compiler` modules. Its C++ file depends on absent SMS core headers and adds external distance-two propagation; its wrapper also describes dynamic symmetry rejection. An option name in that incomplete path cannot certify those external clauses or substitute for the self-contained A+B formula. It is not the minimum recovery route from the files currently present.

## 9. Minimum certification route and remaining obligations

The smallest presently concrete route is to regenerate one A+B base from the available source/JSON and validate the complete formula-to-LRAT-to-Lean connection before spending work on all branches. This document does not initiate that experiment.

The mathematical and formal obligations can be kept separate:

1. **Primitive compiler lemmas:** AND, XOR, the prefix-threshold recurrence including repeated literals, guarded equality with the depth premise, and fresh-variable allocation/composition.
2. **Concrete template interpretation:** prove parent-map correctness, remaining-degree values, singleton classes, fixed repeat calculations, and the template units from the recovered original-graph reduction.
3. **Whole-formula forward bridge:** the witness assignment and clause-family reasoning in Sections 1–4, tied to the exact emitted or independently defined clause list.
4. **Certificate checking:** a new complete LRAT proof for each selected base or covering leaf formula, and a checked `check_sound` application to precisely that formula. Source inspection and solver exit code 20 discharge neither of these.
5. **Cover and final composition:** the seven-template theorem, plus any additional leaf or symmetry cover used. Certifying only the two S branches still leaves the five D branches; the old 02–04 RAW results do not close them formally.

There is no need to resurrect the old signature-ordering/SMS frontends merely to reconstruct an A+B instance. There is also no need to treat an absent old leaf list as recoverable from a summary: certifying a freshly generated base directly, or a newly specified exhaustive split, avoids that dependency while keeping the exact graph problem unchanged.

## Final boundary

No UNSAT theorem, certificate, or graph counterexample was produced in this review. The actual semantic bridge appears supportable, with its call-site and concrete-input premises now explicit. The outstanding work is implementing that bridge in the chosen proof framework and obtaining and checking contradiction certificates for a complete covering family.
