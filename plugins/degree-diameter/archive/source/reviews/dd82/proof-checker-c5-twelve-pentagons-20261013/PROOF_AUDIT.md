# Local proof audit: the actual C5 quotient and twelve pentagons

Verdict: **PASS, same-family/provisional**. One fresh local reviewer read the
complete submitted argument and checked its imported K6,6 obstruction. No
mathematical gap or incorrect implication was found. This is a local semantic
judgment, not Gemini review, a solver result, or Lean acceptance.

Reviewer: `/root/c5_lift_proof_review`, a separate Codex child agent that did
not participate in writing the submitted proof. Actual inherited model/effort
metadata are not independently visible in this child context; no external
backend identity is asserted.

The project-local `proof-checker/SKILL.md` was actually read. The V3 and user
adaptation takes priority: one proportionate mathematical audit, no numerical
scorecard, hashes, extra agents, rendering, formalization, or shared-state
changes. The source proof was not edited. The companion skeleton and state
record the necessary proof obligations without a separate publication report.

## Reviewed input and precise scope

Main input: `proofs/dd82/construction/CYCLIC5_QUOTIENT_TWELVE_PENTAGONS_EXCLUSION.md`,
the complete 289-line draft read during this review. Task contract:
`prompts/26101309-1/task.md`. Actual data:
`computations/dd82/construction/cyclic5_full60_quotient_run/best_quotient.json`.
The graph predicate was checked against `context/dd82/FORMAL_SPEC_DD82.md`
and the orbit parameterization against
`proofs/dd82/construction/CYCLIC5_ORBIT_SWITCH_AND_QUOTIENT.md`.
Only §§2–4 of `CYCLIC5_K66_QUOTIENT_EXCLUSION.md` are required as the
substantive imported obstruction; their argument was checked directly.

The result excludes every voltage realization of this exact labeled quotient
under a free C5 action, allowing every permitted voltage set and both internal
steps. It also excludes diameter-at-most-two graphs with two halves of six
pentagons and an arbitrary anti-cycle perfect matching between each pair of
opposite pentagons. It does not exclude all free-C5 order-60 graphs, arbitrary
order-60 graphs, or all remaining orders 58–61. The global mathematical range
remains `57 <= N(8,2) <= 61`.

The parent subsequently supplied one proposed structural corollary for
inclusion in the source. It was checked as a direct consequence in this
same review, without a new round: for any degree quotient M of a hypothetical
target under twelve free C5 orbits, if `D=M²+M−7I−5J` is two K6 components
and, on each corresponding six-orbit block, M is a unit-interface C5
together with an isolated orbit of internal degree two, then M has no
target lift. Here the induced six-orbit M block is exactly the stated
cycle-plus-isolated-diagonal-two matrix, with all its other entries zero.
The two structural hypotheses give precisely §1's half-graph structure,
within-half degree two, cross-half degree six, and zero cross defect.
The proofs in §§2–8 use no particular remaining cross-block M entries.
Thus the corollary is valid with all those cross entries unrestricted
subject to the target quotient assumptions. **D being two K6 components
alone is not an exclusion established by this audit.** This supplements
the 289-line source actually read; the parent is responsible for inserting
its final wording and updating shared navigation.

## Main mathematical checks

1. **Actual graph and quotient (§1, lines 23–68).** In an 8-regular simple
   order-60 graph of diameter at most two, diagonal entries of
   `B=A²+A−7I−J` are zero, off-diagonal entries are nonnegative, and every row
   sums to `64+8−7−60=5`. The free action makes the orbit partition equitable;
   its B quotient is exactly `M²+M−7I−5J`. Exact integer recomputation
   confirmed the saved D is precisely the two K6 blocks on the stated U,V.
   Nonnegative actual entries with quotient sum zero force every cross B
   entry to vanish. The stated unit-interface pentagons and isolated
   degree-two orbits match M. Unit interfaces are equivariant translations;
   their total voltage gives five C5s or a C25, including all zero and
   nonzero total voltages. Each isolated step ±1 or ±2 gives a C5. The
   resulting block equation has the correct `+X` term and RHS `J30`.

2. **Cyclotomic and Fourier step (§§2–3, lines 72–135).** A zero exponent
   cannot occur in the five-term vanishing sum. The polynomial has degree
   at most 24, constant coefficient one, and coefficient sum five.
   `Phi25(x+1)` is monic, congruent to `x^20 mod 5`, and has constant term
   five, so Eisenstein establishes irreducibility over Q. Division by this
   monic integer polynomial yields an integer g of degree at most four;
   its five coefficient blocks are disjoint, so nonnegativity and g(1)=1
   force g=1. Repeated exponents do not evade this argument. In the
   rectangular Fourier equation the multiplier is `lambda_r+mu_s+1`;
   only the constant/constant coefficient has nonzero RHS. A row mode
   primitive of order 25 has no zero multiplier against any order-5 or
   order-25 column mode. Remaining row modes have indices divisible by
   five, giving exact period five. Four distinct nonadjacent companions
   then give B entries at least five each, contradicting row sum five.
   The transpose covers a C25 on either or both sides.

3. **Anti-cycle matching (§4, lines 139–164).** From
   `CP+PC+P=J`, row sums solve `(C+3I)y=5·1`; C's spectrum lies in [-2,2],
   so y=1 uniquely. The transposed equation gives column sums one.
   Binary P is thus a permutation, and multiplication by P transpose
   yields `PCPᵀ=J−I−C`. Any isomorphism from a standard C5 to its complement
   is `t -> 2 epsilon t+a`, with both signs and all five translations.
   Coordinate choices therefore cover the full matching domain.

4. **Six-route coverage (§5, lines 168–198).** Distinct pentagons on one
   side have neither direct edges nor internal two-step routes between
   them. The six opposite pentagons give precisely six permutation routes.
   Anti-cycle maps compose to cycle automorphisms. Diameter two makes
   their excess over J nonnegative integral with row/column sums one;
   hence it is a permutation W, and commuting with C makes W dihedral.
   The transformation `(t,u)->(u−t,u+t)` is invertible over F5. After
   subtracting W, `A'_x+B'_y=1` makes each count family constant. Even
   though the subtracted entry could initially appear negative, the
   other four entries in that family are unaltered nonnegative counts;
   constancy proves the required nonnegativity without assuming W was
   already a selected route. Rotation counts are 0,1,5,6. Both sides give
   the row and column Hamming conditions.

5. **Switching (§6, lines 202–219).** Independent coordinate reversals are
   valid relabelings and multiply the relevant sign row or column by −1.
   Pairwise allowed distances remain in `{0,1,5,6}`: some distances stay
   fixed, and the others change from d to 6−d. Normalize the first row
   positive, then every row to at most one negative. Different negative
   columns would create distance two. With all negatives in one column,
   its distance from any positive column is 0,1,or5 because its first
   entry is positive. Five negatives become one after reversing that
   column. Thus no additional orientation class is omitted.

6. **All-positive import (§7, lines 223–234).** Translating left coordinates
   by one and right coordinates by two preserves each `t -> 2t+a` matching
   and every internal pentagon, and is a free order-five automorphism.
   Its orbits are exactly the twelve pentagons and its quotient is the
   old `2I+A(K6,6)` quotient. More explicitly, group coordinates on the
   right may be taken as `3t`; then the matchings have ordinary voltage
   form `t -> t+3a`, with internal steps 1 and 2 on the two sides. Thus
   every hypothesis of the old exclusion is met even if this action is
   different from the original action defining M. Direct review of old
   §§2–4 verifies simultaneous row/column sum normalization over F5,
   `HH*=H*H=5I+J`, common row/column sum of squared modulus 11, and the
   impossible five counts with sum six and square sum sixteen. No old
   graph-classification or exactly-one-independent-orbit result is needed.

7. **Single-negative Gram contradiction (§8, lines 238–272).** For a route
   from row 0 to regular row i through j>0, the map is
   `t -> t+3(a_0j−a_ij)`; through j=0 it is a reflection. The five
   rotations must be all translations. Thus the tail differences are
   exactly F5, tail sums agree, and `Zw*=0`. For two regular rows all
   inverse slopes are 3, including column zero; the six route shifts are
   `3(a_ij−a_kj)`. Removing the common nonzero factor preserves complete
   coverage plus one repeat. Equal tail sums identify the repeated
   difference as `a_i0−a_k0`, so cancellation of the j=0 character term
   gives orthogonality of the five rows of Z. The factors, sign convention,
   complex conjugations, and dimensions all agree: `ZZ*=5I5` makes Z
   invertible whereas `Zw*=0` with w nonzero is impossible.

For the broader architecture, §§5–8 apply directly under the target
diameter condition; the stipulated anti-cycle matchings supply §4's
conclusion. That extension therefore does not require the original M.

## Focused counterexample pass and deterministic evidence

The review explicitly challenged zero/repeated exponents in the root lemma,
one or both C25 factors, zero and nonzero total voltage, an initially absent
residual W in the covering count, five negatives in the exceptional column,
mixed orientations before switching, both internal orbit steps, and the
change of free action in the all-positive case. Each is covered by the
derivations above. No counterexample or unresolved counterexample candidate
remains. These checks are algebraic, not a claim of enumeration over the
voltage family.

One short exact-integer Python calculation read the actual JSON and confirmed:
M is symmetric with all row sums eight; computed D equals saved D and
the specified two K6 blocks; all within-half degrees are two and all
cross-half degrees are six; the two listed internal quotient cycles and
isolated diagonal twos match the data. It also independently confirmed the
coefficients used in the stated 5-Eisenstein test. No floating-point spectral
test, voltage search, solver, graph-distance run, or repeated computation was
used. The proof's semantic obligations are discharged by the arguments,
not by this finite input check.

There are no limits, asymptotic bounds, measure/probability statements, or
analytic interchanges requiring extra conditions. All matrices and sums are
finite; the dependency chain is acyclic. No repair or statement weakening
was necessary. Cross-family review and later formal acceptance remain
separate from this local PASS.
