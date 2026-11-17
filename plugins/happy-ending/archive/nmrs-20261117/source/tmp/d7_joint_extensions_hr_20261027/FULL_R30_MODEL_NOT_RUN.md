# Complete R30 endpoint split: mathematical model only, NOT RUN

No CNF generation or solver invocation is authorized by this document.
No new budget is allocated. The prior sealed R30 run stays untouched.
This specification records the smallest presently justified complete-order
decision with a direct independent-capacity exit; it is not a proved theorem.

## Actual quantified model

V={0,...,29}, one Boolean color for every actual triple. Require every
rank3 packet to have at most one change, no B5, no weak7, and no actual
EndR5(V)/SrcB4(V) joint point. All paths and endpoint identities are
computed in this same full coloring. No fixed core, path witnesses,
exceptional-state type or endpoint locations are imposed.

Define E_i iff an actual R6 ends at i. Any auxiliary encoding that uses
E_i positively or counts E_i must establish this equivalence, not merely
actual path implies flag. Exact path recurrences or fully enumerated
actual paths are admissible. Existing one-way flags cannot supply it.

The accepted scoped b25 and R7 transversal proof imply alpha=25,tau=5
in every actual order30 solution. All E points are right roots and
|E|<=6. Since E itself is a transversal, |E|>=5. Thus the branches are
exactly |E|=5 and |E|=6; neither branch fixes their actual positions.

In E5 take T=E. In E6 enumerate the selected actual endpoints
e1<...<e6 and take T=E\{e2}. In both cases Y=V\T is the same actual
25-point safe complement for the branch. No separate Y coloring is
allowed. For every A subset T the induced Y+A has alpha25,tau=|A|;
no additional all-four-deletion clauses are needed to infer this.

## Proved redundant constraints available to improve expression

1. E_i implies every triple (i,j,k), i<j<k, is red.
2. For e=min E, every actual R6 starts<=e<=ends.
3. For x<e<y<z, red(x,e,y) implies red(x,e,z).
4. In E6, every R6 ending at e2 starts at e1.

These apply to all paths, including paths using several selected endpoints.
They do not determine all cross-cut colors. Redundancy/soundness has a
mathematical proof in R7 and the new/prior main records; actual encoding
must still receive its own source/formula binding and bounded checks.
Any future runtime must be a fresh snapshot, never alteration of the
sealed order30 runtime. No endpoint-count assertion is licensed on
inexact flags.

## Conclusions

- Full SAT plus complete actual-color checking: refutes independent D<=29,
  retains an actual R30 for canonical H–R embedding research.
- Both exhaustive branches bound/proof-checked UNSAT: no order30 D7;
  by hereditary D7, D<=29 and Q<=79 using C<=50.
- A single branch UNSAT: closes only that branch; no D<=29.
- Raw UNSAT, timeout or unavailable execution: no capacity improvement.
- The order26 SAT in single_root26 refutes its candidate, not this model.

The missing mathematical step is still an actual full-family conflict or
strict safe-set augmentation. This model is not presented as such a step,
and it does not silently authorize a new run.
