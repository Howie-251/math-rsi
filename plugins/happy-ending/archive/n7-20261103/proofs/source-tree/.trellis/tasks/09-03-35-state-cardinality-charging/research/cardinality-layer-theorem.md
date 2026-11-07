# Formal theorem structure for the 35-state cardinality campaign

## Accepted instantiation (updated 2026-10-26)

The C1 obligations are discharged by accepted effective 10/10 coverage.
C2 is now also accepted with 9/9 fresh checker-qualified cells, accepted C1
as its dependency, and byte-equal independent final reconstruction. Thus
`e(X)>=2 => m(X)>=2` and `N<=33` hold in the precise domain defined here.
C3 has since been independently accepted with eight fresh checks and
byte-equal final reconstruction, establishing `e(X)>=3 => m(X)>=3` and
the scoped bound N<=32. Its receipt SHA-256 is
`8e2322334352eb2e9c5448c653422b991e7a23677dcd18ef2a06ba2482f669fd`.
C4 was independently accepted on September 24 at 17:25:36 UTC+8 with seven
fresh checks and byte-equal final reconstruction. It establishes
`e(X)>=4 => m(X)>=4` and the scoped bound N<=31. Its receipt
SHA-256 is `84a1f4aafa6d03ffb3a4413a33f901bb2a16e1a658c6c49203cd78f49be95cb8`.
C5 v2 was independently accepted on October 3 at 19:38:33 UTC+8 with six
fresh checks and byte-equal final reconstruction. It establishes
`e(X)>=5 => m(X)>=5` and the then-accepted scoped bound N<=30. Receipt SHA-256:
`4101b158a1516d603148194e34ed44e67769d26b4c47d27b9933020fee137ea3`.
C6 was formally accepted by the user on October 16 under the disclosed
provisional review assurance and the explicit waiver of fresh case checks.
It reuses bridges e6 and historical compact e7..10, establishing
`e(X)>=6 => m(X)>=6` and the then-accepted scoped bound **N<=29** in the domain
below. Acceptance authority is human_user; backend/model and effort remain
unverifiable. Fresh checker replay count is 0; five checked cases are reused.
Receipt SHA-256:
`9024a8f02078c1fae1037ced49bd545ae7f626e12ab5a8c67bd53d9e03ca30a1`.
See [C6 formal acceptance](c6-formal-acceptance-20261016.md) for exact
scope, assumptions, original proof bindings and provisional limitations.
C7 was formally accepted by the user on October 20 after the completed
fresh-context GPT row review, retaining **same-family/provisional** assurance.
It reuses four checked historical bridges cells e7..10, with no repeated
case checks, formula replay or proof hashes. Thus `e(X)>=7 => m(X)>=7` and
the then-accepted scoped bound was **N<=28**. Acceptance authority is human_user;
exact model/backend and actual effort remain unknown/unverifiable. Receipt
SHA256: `347bcf377f53102316c091ebdf9cd415acbaa33ffbe1f52f47061531f791ec96`.
See [C7 formal acceptance](c7-formal-acceptance-20261020.md).
C9 and C10 were formally human accepted on October22 after the fresh-context
GPT review, retaining **same-family/provisional** assurance and unverifiable
exact reviewer backend/model and actual effort. Five existing checked cells
are reused, with zero repeated case checks, formula replays or proof hashes.
Accepted C7 plus A[8,9]/A[8,10] proves the restricted `e>=9 => m>=8`, then
A[9,9]/A[9,10] proves C9 and A[10,10] proves C10. C10 also has the direct C7
plus three-e10-exclusions proof. At that October22 event, accepted rows were
**C1..C7,C9,C10**, full C8 was unaccepted, and the scoped bound was **N<=26**:
e<=7 gave N<=25; e8 gave N<=26 from C7; e9/e10 gave N<=25 from C9/C10.
That historical event and its original dependency graph remain unchanged.
Acceptance receipt SHA256:
`d826c19662823d50b90cf4641b022505e98329f2752a0e2044f3959bab0d1a9e`.
See [C9/C10 formal acceptance](c9-c10-formal-acceptance-20261022.md).
C8 was explicitly human accepted on October26 after the fresh-context GPT
review, retaining **same-family/provisional** assurance and unverifiable exact
backend/model and actual effort. Accepted C7 and the completed A[8,8] GRAT
plus retained A[8,9]/A[8,10] checks prove universally `e>=8 => m>=8`.
The additive indexing erratum changes no mathematical bound or sealed source.
Accepted rows are now **C1..C10**, pending rows **none**. At e=0, m>=e
trivially; at e=k in1..10 apply accepted Ck. Therefore **m>=e and N<=25**
in the quantified domain below at every finite order. No unrestricted
geometric conclusion or existence at order25 is asserted.
Acceptance receipt SHA256:
`70b32da5fe33e0e2e20e6bdb12684bd69ac45aeb765bcf51f5e00c83153ccc68`.
See [C8 formal acceptance](c8-formal-acceptance-20261026.md).
The earlier dated checkpoints retain their historical bounds. See the
[C4 audit/C5 search checkpoint](c4-audit-c5-search-20260922.md),
[scientific checkpoint](methods-and-results-20260913.md),
[C1 accepted evidence](evidence/c1-accepted-20260913/README.md), and
[C2 accepted checkpoint](c2-formal-acceptance-20260915.md) for exact hashes
and publication scope. C2's acceptance receipt SHA-256 is
`7b16c5f84bfdc643dda27828130a6659075f26b42a41b229ae3175c920fbe7c2`.

## Definitions and quantified domain

For each finite order `N`, let \(\mathcal T_N\) be the class of complete
ordered two-color rank-3 signotope colorings on `[N]` that satisfy the
blue-path-5 and red-path-6 bounds and contain no weak 7-gon.  Write
\(\mathcal T=\bigcup_N\mathcal T_N\).  Thus every theorem below that quantifies
over a target-free coloring `X` means precisely \(X\in\mathcal T\); path-bounded
colorings outside this signotope-and-target-free domain are not covered by a
strict-cell UNSAT result.

The polarity convention is fixed independently of legacy clause-group names:
a true triple variable is red, `cap` extends on `~x` and is the blue family
bounded at length 5, and `cup` extends on `x` and is the red family bounded at
length 6, exactly as in `STATE_756_SPEC`.  The historical names
`no_red_5_path` and `no_blue_6_path` are inverted relative to these literal
semantics and are not admissible evidence for a polarity claim.

Let `Ord` and `Exc` be the canonical families of 25 ordinary and 10
exceptional down-set states in the 3-by-4 box.  For \(X\in\mathcal T\), let `D_X(v)` be
the down-set state at endpoint `v`, and define

\[
\operatorname{Occ}(X)=\{D_X(v):v\in X\},\qquad
e(X)=|\operatorname{Occ}(X)\cap\mathrm{Exc}|,
\]

\[
m(X)=|\mathrm{Ord}\setminus\operatorname{Occ}(X)|.
\]

`TargetFree(X)` is shorthand for membership in this quantified domain.  The
path bounds, signotope axioms, and target prohibition are all checked
independently from any SAT state/count auxiliaries.

## Lemma 1: canonical state completeness

Every endpoint state is a nonincreasing triple

\[
4\ge h_1\ge h_2\ge h_3\ge0.
\]

Conversely these triples are exactly the down-sets in the 3-by-4 box.  There
are 35 of them.  Classification by bounding-box width plus height at most six
gives exactly 25 ordinary states; the remaining 10 are exceptional.

The implementation witness is the independent enumeration in
`lib/downset_state.py`, not the SAT variable table.  Production binds its
catalog order/hash and independently requires counts `35/25/10`.

## Lemma 2: endpoint-state injection

For `u<v`, write

\[
\sigma(u,v)=(d(u,v),e(u,v)),
\]

where the two coordinates are the longest terminal-pair monochromatic path
lengths minus one, and

\[
D_X(v)=\downarrow\{\sigma(t,v):t<v\}.
\]

Then `sigma(u,v)` lies in `D_X(v)`.  For each `t<u`, the color of the triple
`(t,u,v)` extends one of the two paths ending in `(t,u)`:

- in the path5 color, `d(u,v) >= d(t,u)+1`; or
- in the path6 color, `e(u,v) >= e(t,u)+1`.

Hence `sigma(t,u)` does not dominate `sigma(u,v)`.  No generator of `D_X(u)`
dominates that cell, so `sigma(u,v)` is not in `D_X(u)`.  Thus

\[
D_X(u)\ne D_X(v).
\]

This proves injection for every order.  The path-extension recurrence, hence
the distinctness conclusion itself, uses completeness of the coloring and
exact terminal-path semantics.  The two path bounds play a different role:
they place every resulting down-set inside the finite canonical 3-by-4 box and
therefore inside the 35-state catalog.  Neither step uses N=25, the signotope
axioms, or weak-7 exclusion.  The SAT state CNF does not contain a
cross-endpoint all-different family, so the independent model checker must
still reject any decoded collision explicitly.

## Corollary 3: counting identity

By Lemma 2, the N endpoints occupy exactly N distinct state types.  Splitting
the occupied types into ordinary and exceptional gives

\[
N=|\operatorname{Occ}(X)|=(25-m(X))+e(X)=25+e(X)-m(X).
\]

This identity is recomputed from endpoint rows in every accepted SAT model;
the totalizer outputs and cached scalar fields are not trusted.

## Semantic bad cells and their CNF encodings

For plain integers `1<=r<=e<=10`, put `N=26+e-r` and define the mathematical
counterexample class

\[
\mathcal A_{r,e}:=
\{X\in\mathcal T_N:e(X)=e\text{ and }m(X)=r-1\}.
\]

Let \(\Phi^{\mathrm{strict}}_{r,e}\) be the corresponding CNF: the genuine
order-`N` strict base, the exact endpoint-state and occupancy equivalences, and
the exact-cardinality constraints `e(X)=e` and `m(X)=r-1`.  The campaign label
`A[r,e]` names this semantic/CNF pair; it must not blur the mathematical class
with one serialized formula.

There are

\[
\sum_{r=1}^{10}(11-r)=55
\]

such cells, in canonical `(r,e)` order.  The order in the formula is forced by
Corollary 3:

\[
N=25+e-(r-1)=26+e-r.
\]

The relaxed discovery companion replaces only the weak-7 prohibition by
allowing that target; it retains both path bounds, the signotope axioms, the
same state catalog, and the same exact occupancy conditions.  At the intended
constraint level it is obtained by deleting the weak-7 family, and after
projection to the triple coloring its semantic model class contains the
strict class.  The serialized CNFs are **not** literal clause subsets: omitting
the target-family construction changes later auxiliary IDs, so strict and
relaxed bytes are generated and hash-bound independently.  The semantic
containment is not claimed to be proper unless an audited relaxed witness
actually contains a weak 7-gon.  In particular, the relaxed CNF is not a
formula for \(\mathcal A_{r,e}\).

**Same-endpoint path-deletion sublemma.**  In a rank-3 signotope, the
at-most-one-sign-change rule on each four-point packet supplies an internal
point whose deletion shortens a monochromatic cap or cup while preserving its
two outer endpoints and its path type.  Iteration therefore proves the
same-endpoint monotonicity

\[
P(i,j,d)\Longrightarrow P(i,j,d-1)
\]

for the exact path predicates used by the base encoding.  This is the
nontrivial step that makes a semantic coloring extend to the base CNF's path
monotonicity clauses.  Target lifting is separate and direct: in this
`(7,5,6)` scope a weak 7-gon is exactly a blue cap4 and red cup5 with the same
outer endpoints, so weak-7-freeness satisfies the corresponding strict target
clauses without another reduction argument.

## Lemma 4: encoding faithfulness

For every registered cell,

\[
\Phi^{\mathrm{strict}}_{r,e}\text{ is SAT}
\quad\Longleftrightarrow\quad
\mathcal A_{r,e}\ne\varnothing.
\]

### Proof

For the forward direction, soundness of the order-generic strict base implies
that a satisfying assignment restricted to the triple variables decodes to a
member of \(\mathcal T_N\).  The state clauses define each `S[v,g]` exactly
from the terminal-path recurrence, the occupancy clauses impose `O[g]` iff
some endpoint has state `g`, and the four deterministic at-most encodings
jointly impose the two requested equalities.  Independent recomputation
therefore gives `e(X)=e` and `m(X)=r-1`.

For the reverse direction, take any `X` in \(\mathcal A_{r,e}\).  Completeness
of the order-generic strict base extends its coloring by the canonical
path/target auxiliary values to an assignment satisfying every base clause.
The same-endpoint path-deletion sublemma justifies the downward path
monotonicity clauses, while weak-7-freeness directly justifies the target
clauses.  Extend the base assignment further by the uniquely determined
terminal-path, state, and occupancy values.  Completeness of each of the four
deterministic at-most encodings guarantees the **existence** of auxiliary
values for the two true exact-cardinality equalities; uniqueness of those
totalizer auxiliaries is neither needed nor claimed.  The resulting extension
satisfies the whole CNF.

Cross-endpoint injection is not a hidden clause family in
\(\Phi^{\mathrm{strict}}_{r,e}\).  Its role is external: it gives the counting
identity that fixes the order of an arbitrary counterexample and proves that
the 55 semantic cells exhaust all such counterexamples.  The production SAT
checker nevertheless recomputes injection as a defensive consistency check.

Consequently proof/checker-qualified UNSAT of the exact sealed CNF implies
that the corresponding mathematical class is empty.  SAT model replay is a
necessary implementation audit of the forward direction, but SAT replay alone
would not establish the reverse implication needed to interpret UNSAT.  A
production theorem may invoke this bridge only after the sealed builder and
its full runtime closure have been hash-bound and fresh replay has shown that
the sealed CNF is exactly an instance of the audited construction.

## Theorem 5: layer induction

Let

\[
C_r:\quad
\forall X\in\mathcal T,\quad e(X)\ge r\Longrightarrow m(X)\ge r.
\]

If every \(\Phi^{\mathrm{strict}}_{r,e}\) with `e=r,...,10` is
proof/checker-qualified UNSAT, then `C_r` follows from `C_1,...,C_{r-1}`.

### Proof

For `r=1`, a counterexample to `C_1` has `e>=1` and `m<=0`, hence `m=0`.
Putting `e=e(X)` places it in exactly \(\mathcal A_{1,e}\).

For `r>1`, suppose the earlier layers hold and `X` is a counterexample to
`C_r`.  Then `e(X)>=r`, while `m(X)<=r-1`.  Since `e(X)>=r-1`, layer
`C_{r-1}` gives `m(X)>=r-1`.  Therefore `m(X)=r-1`.  With `e=e(X)`,
Corollary 3 fixes `N=26+e-r`, so `X` belongs to
\(\mathcal A_{r,e}\).  Lemma 4 and the proof-qualified UNSAT result say that
this class is empty, a contradiction.  This proves `C_r`.

Consequently the 55 cells admit a finite triangular proof graph. The full-row
induction route above is sufficient: accept the earlier rows and qualify every
cell in the current row before publication. This route is not a necessity
claim about all possible proofs of `C_r`. An alternative dependency DAG may
replace full earlier rows with explicitly stated narrower premises, provided
it exhausts the relevant counterexamples, binds its qualified case evidence,
and receives independent review and explicit human acceptance. For example,
the [C9/C10 joint proof](c9-c10-formal-acceptance-20261022.md) uses accepted C7
and checked A[8,9]/A[8,10] to prove only `e>=9 => m>=8`, then derives C9/C10
without full C8. Its GPT review is complete with same-family/provisional
assurance; C9/C10 were subsequently human accepted with the then-scoped
bound26. C8 was separately human accepted on October26, giving the current
scoped bound25 after combining all ten accepted rows. These publications and
wording clarifications do not modify the original sealed candidates or
exported primary inputs, and the C9/C10 DAG still does not require full C8.

## Corollary 6: the C1 numerical bound

If all ten strict `C1` cells are proof/checker-qualified UNSAT, Theorem 5 gives
`C1`.  Now let \(X\in\mathcal T\).  If `e(X)=0`, then Corollary 3 gives

\[
N=25-m(X)\le25.
\]

If `e(X)>=1`, then `C1` gives `m(X)>=1`; because there are only ten exceptional
types, `e(X)<=10`, and hence

\[
N=25+e(X)-m(X)\le25+10-1=34.
\]

Thus the complete C1 row proves `N<=34` without any heredity argument.  A
single cell, including the order-35 cell, may exclude one order but does not
establish the universally quantified statement `C1`.

## Corollary 7: full charging bound

If all ten layers hold, consider any \(X\in\mathcal T\).  When `e(X)=0`, the inequality
`m(X)>=e(X)` is immediate.  Otherwise set `k=e(X)`, where
`k in {1,...,10}`; layer `C_k` gives `m(X)>=k=e(X)`.  Therefore Corollary 3
gives

\[
N=25+e(X)-m(X)\le25.
\]

No individual raw UNSAT result, incomplete row, or repaired aggregate is
sufficient for this statement.

## The N26 spine and its exact scope

At N=26, Corollary 3 says `e(X)=m(X)+1`.  Therefore every strict target-free
N26 model belongs to exactly one semantic diagonal cell

\[
\mathcal A_{r,r},\qquad r=e(X)=m(X)+1\in\{1,\ldots,10\}.
\]

Proof-qualified UNSAT for all ten diagonal CNFs excludes \(\mathcal T_{26}\).
To pass from that exclusion to a bound for arbitrary orders, suppose that
\(X\in\mathcal T_N\) with `N>=26` and restrict its complete coloring to any ordered
26-point subset.  Completeness, the two path bounds, the signotope axioms, and
weak-7-freeness are all hereditary.  The endpoint states, occupancy set,
`e`, and `m` must then be **recomputed on the restricted coloring**; the
original occupancy mask is not itself inherited.  Corollary 3 applied after
this recomputation places the restriction in a unique
\(\mathcal A_{r,r}\), contradicting diagonal closure.  Thus the spine alone
yields the numerical bound `N<=25`.  It does **not** prove the stronger
off-diagonal statements `C_r`; those require the full 55-cell triangle and
the row induction above.

## Proof/evidence graph

```text
complete coloring + exact terminal-path recurrence --> endpoint injection
path bounds ----------------------------------------> membership in 35-state catalog
                                                        |
endpoint injection + 25/10 catalog split --------------+
                                                        v
                                                N = 25 + e - m
                                                        |
signotope + path bounds + no weak 7-gon define T_N     |
                                                        v
counterexample to C[r] + prior layers --> X lies in semantic A[r,e]

strict-base lifting:
  packet path-deletion + direct weak-7 target semantics
  + exact S/O definitions + complete exact-count encodings
                                                        |
                                                        v
                 [ Phi[r,e] SAT  <==>  semantic A[r,e] nonempty ]
                          |
                proof/checker-verified UNSAT
                          |
                          v
                  semantic A[r,e] is empty
                          |
            all e=r..10 + prior C[1]..C[r-1]
                          |
                          v
                         C[r]
```

SAT evidence follows a different edge: a complete independently replayed
strict SAT assignment for any cell is a counterexample and stops the entire
negative campaign.  Relaxed SAT is only a construction/discovery witness in
the target-allowed class; it proves neither strict nonvacuity nor any strict
theorem edge.
