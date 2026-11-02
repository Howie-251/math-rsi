# Scoped proof audit: order61 norm and lifting obstructions

Date: 2026-10-13. Verdict: **PASS** for the scope below; `review_independence: same-family`, `acceptance_status: provisional`.

Fresh reviewer: `/root/n61_norm_lifting_proof_check`. The review read all three manuscripts, the actual quotient definitions and necessary size-domain arithmetic, the new five-entry resonance source/result, and the imported exact rational routines. Prior review responses and root commentary were not used. Manuscript status declarations were not correctness evidence. No mathematical gap or counterexample was found, and no manuscript changes were needed.

## Scope and inherited definitions

The audited manuscripts are:

- `proofs/dd82/n61/COMPONENT_QUOTIENT_GLOBAL_OBSTRUCTIONS.md`, complete.
- `proofs/dd82/n61/COMPONENT_MATCHING_EDGE_OBSTRUCTION.md`, complete.
- `proofs/dd82/n61/COMPONENT_PERIODIC_COLUMN_OBSTRUCTION.md`, complete.

Necessary definitions were checked in `GENERAL_THREE_DEFECT_COMPONENT_QUOTIENTS.md`, section 2, and `LARGE_DEFECT_COMPONENT_QUOTIENT_DOMAIN.md`, its opening and necessary-arithmetic section. No historical classification or prior audit was used to establish the scoped conclusions.

For a simple order61 target of maximum degree8 and diameter at most2, the radius-two count forces degree8 at every vertex. Thus the same adjacency matrix A gives the symmetric nonnegative defect `B=A^2+A-7I-J`, with zero diagonal and row sum4. The four-eigenspace of B is exactly its component-constant space; commutation with A makes the positive-support components equitable. Hence the actual integer quotient Q, positive sizes n_i, and D=diag(n_i) satisfy

`Q1=8*1`, `DQ=Q^T D`, `Q^2+Q-11I=1*n^T`, `sum n_i=61`.

These definitions fix q_ij as the number of neighbors in component j of each vertex in component i. In particular, q_ij=0 means the corresponding actual adjacency block is zero. Also `c=2m+1`, `trace(Q)=8-m`, each size is at least2, and actual diagonal blocks are simple regular graphs of degree q_ii. Every later block equation uses this same A and B.

## 1. Norm obstruction

**Checked claim.** Every actual quotient with c>=5 has `product n_i=a^2` or `5a^2` for a positive integer a.

The weighted-orthogonal complement `E={x:n^T x=0}` is a rational Q-invariant space of dimension2m. Detailed balance makes C=(2Q+I)/3 self-adjoint there, and the quotient identity gives C^2=5I. Irreducibility of x^2-5 gives the asserted Q(sqrt(5))-vector-space structure and a rational basis `(v_1,...,v_m,Cv_1,...,Cv_m)`.

Its Gram matrix is `[[X,Y],[Y,5X]]`; self-adjointness supplies symmetry of Y. Scaling the second block followed by the `(u,u)` and `(u,-u)` decomposition proves the determinant identity without assuming that X and Y commute. The rational change-of-basis determinant delta is nonzero, and orthogonality to 1 gives

`product n_i = 61*5^m*Norm(alpha/delta)`.

Because `Norm(9+2sqrt(5))=61` and `Norm(5+2sqrt(5))=5`, the product is a nonzero field norm. The valuation proof is complete: 5 is a quadratic nonresidue modulo3 and7; after removing common powers of2, opposite parity gives valuation0 and two odd numerators give valuation2 modulo8. Rational denominators subtract even valuations.

Finally, the positive quotient support is connected by the polynomial identity. A prime p>8 dividing one size propagates by detailed balance across every positive interface, because both positive quotient entries are at most8. It would divide every size and61, impossible for a proper component size. Only 2,3,5,7 occur, so even valuations at2,3,7 prove the claimed square or five-times-square conclusion.

All premises used by the norm argument are discharged by the actual quotient definitions. The proof is a necessary condition, with no converse asserted.

## 2. Matching edge and equal-size block

**Checked claims.** The matching-edge obstruction; its application to the displayed `(2,5,6,18,30)` quotient; the equal-size return-matrix parity/trace lemma; and the exclusion of the entire `(2^8,5^9)` size pattern.

For two diagonal-one components, their simple induced adjacency matrices S,T are perfect matchings, so S^2=T^2=I and SJ=JT=J. Absence of a common third support neighbor eliminates every other actual two-step block. Therefore `SX+XT+X=J`. Subtracting its left-S multiple gives `XT=SXT`, hence X=SX; subtracting its right-T multiple gives `SX=SXT`, hence X=XT. Thus 3X=J, impossible for binary X. Dimensions and component-zero implications are consistent.

For the displayed quotient, row sums, all interface balances, the polynomial identity, and the internal simple-graph/handshake constraints were checked directly. Its size6/size18 edge satisfies both diagonal-one conditions and has no third support neighbor. The contradiction applies to every lift and every simultaneous relabeling; the abstract quotient itself remains a valid integer solution.

For r>1 equal-size components, detailed balance makes S symmetric. Restricting the quotient polynomial with external return `alpha I+beta J` gives `S^2+S=(11-alpha)I+(a-beta)J`. If a!=beta, commuting with S forces SJ=JS, hence a constant integer row sum k. The rational invariant contrast space has dimension r-1. A positive rational nonsquare discriminant `45-4alpha` forces its conjugate eigenvalues to have equal multiplicity, yielding odd r and `trace(S)=k-(r-1)/2`. These hypotheses, including the return pattern, are explicitly required; equal sizes alone are not used as a substitute.

In the `(2^8,5^9)` application, c=17 gives zero trace, hence zero diagonal. Balance and the row8 bound make every positive size2/size5 interface a 5/2 pair. For a size2 row, parity rules out t=0 from `sum a_j=8-5t`, `sum a_j^2=13-10t`, and t<=1 gives t=1. The remaining three unit entries make the size2 submatrix cubic. A size5 row's diagonal moment16 permits at most one contribution10, so the eight external partners are distinct and the return matrix is 10I. Its seven-dimensional contrast space would satisfy the irreducible polynomial x^2+x-1, a contradiction. All eight size2 components and all nine size5 components are included in this argument.

## 3. Periodic columns and the `(3,3,15,15,25)` lift

**Checked claims.** The general binary periodic-column lemma and the exclusion of every lift of the specifically displayed quotient.

For coprime a,b, CRT identifies a column `f(z mod a)+g(z mod b)` with the full additive array f_i+g_j. Two different f values have a fixed nonzero difference between binary entries, necessarily +1 or -1; this fixes each corresponding pair and forces g constant. If f is constant instead, the column has period b and weight divisible by a. The stated weight condition excludes that case. The b equal rows at a fixed residue modulo a share their r recorded neighbors, contributing at least `(b-1)(r-1)` to the actual defect row. Nonnegative remaining entries justify the lower bound. Complex Fourier coefficients do not change the binary-difference argument.

For the displayed Q, its row sums, detailed balance and matrix polynomial were checked directly. The specified U,V,W blocks have exactly the dimensions and row/column degrees stated. The five-cycle quotient support supplies no third route for either selected edge, giving `X+XS=J` and `SY+YT+Y=J` for the same actual blocks.

For a p-cycle of S, summing `X_p(I+C_p)=J` gives integral row counts p/3. For each S-cycle/T-cycle pair, summing the second block identity gives `(C_p+3I)r=q*1` and `(C_q+3I)c=p*1`. Since cycle eigenvalues lie in [-2,2], both matrices are invertible, and r=(q/5)1, c=(p/5)1. Thus every S-cycle length is divisible by15, so S=C15, while every T-cycle length belongs to {5,10,15,20,25}.

The exact gcd table leaves only C15 modes of order5, and (at q=20) order3, besides the separately allowed constant mode. Specifically, multiplying `C15 Z+Z C_q+Z=J` by a nonconstant Fourier row kills J, and an absent resonance makes `C_q+(lambda+1)I` invertible. Therefore every column lies in the sum of the period5 and period3 subspaces. All actual T-cycle blocks are covered by the five-entry table. The factor x+1 at q=20, including its multiplicity2, is retained.

The general lemma applies with `(a,b,w,r,delta)=(5,3,3,5,4)`. Every column has period5, and each row has two distinct copies sharing five W-neighbors. The resulting defect lower bound8 contradicts row sum4. This excludes the displayed quotient and its relabelings, without excluding other quotients on these sizes or all c=5 cases.

## Exact algebra evidence

The reviewed new source is `computations/dd82/n61/component_3_3_15_15_25_resonance.py`; the complete corresponding `.result.json` was read. Imported helpers in `component_6_25_30_resonance.py` use trimmed ascending coefficient lists, exact Fraction long division, monic Euclidean gcd, and Horner substitution by -1-x. The old table is protected by a main guard and is not executed by import.

A single independent exact check constructed explicit cycle adjacency matrices and obtained their characteristic polynomials with SymPy, then computed gcds over Q. This uses an independent characteristic-polynomial path and gcd implementation. It confirmed all saved cycle coefficients, shifted coefficients, monic gcds, and both cofactor arrays for q=5,10,15,20,25. The result was f^2 in four cases and `(x+1)^2 f^2` for q=20, where f=x^2+x-1. A hard limit of2 CPU seconds was set before importing SymPy. The process exited0; tool-reported wall time was0.307510543 seconds, and measured algebra after import used0.135985919 CPU /0.138518531 wall seconds. No old table, classification, solver, graph enumeration, or other order was rerun. Original recorded run timings were not independently recertified.

## Counterexample checks and dependency closure

The adversarial checks addressed the load-bearing exceptional cases: noncommuting X/Y in the Gram determinant; both-odd representatives in the 2-adic argument; zero quotient interfaces versus actual zero blocks; the fractional solution X=J/3 versus binary lifting; necessity of a!=beta and irrational discriminant in the equal-size lemma; constant f or complex additive values in the periodic lemma; and the extra q=20 Fourier resonance. Each is handled by the written hypotheses or the displayed derivation. No counterexample was found. There are no limiting operations, asymptotics, probabilistic mode changes, or hidden uniformity assumptions in these finite arguments.

The dependency chain is acyclic: actual graph/defect definitions -> quotient identities -> norm or block identities -> stated arithmetic/lifting conclusions. The periodic application additionally uses the new five-entry exact gcd computation. All seven theorem-like statements/applications in the three requested claim groups have their hypotheses discharged. Open mathematical issues within this scope: none.

The size-screen counts, earlier c=3 classification, earlier lifting exclusions, and manuscript historical-review statements were not audited. No claim is made that all c=5, all c>=5, connected defect c=1, arbitrary order61, or arbitrary orders58–61 are excluded. The main research goal remains open. This local same-family proof audit does not replace external review or final formal acceptance.

The project V3 adaptation disables hashes, manifests, scorecards, rendering/PDF reports, MCP review calls, Lean work, queues and extra audits. Only this requested scoped audit and state were saved; wiki integration is left to the parent workflow to avoid concurrent edits.


## Reused-agent delta: size-two capacity obstruction

Added 2026-10-13 by the same reviewer `/root/n61_norm_lifting_proof_check`. This is explicitly a **reused-agent delta**, not a new independent review round. Verdict: **PASS**, same-family/provisional. Only the new manuscript `proofs/dd82/n61/COMPONENT_SIZE_TWO_CAPACITY_OBSTRUCTION.md` was examined for this delta. The previously checked actual quotient definitions supply its stated premises; no earlier gcd, classification, historical range, or computation was rerun.

The new claim excludes the entire size multiset `(2^8,5^5,10^2)` at the quotient level. Its sizes sum to61 and its component count is15, so nonnegative integer diagonals with trace1 consist of exactly one1 and otherwise0. The actual handshake constraint forces every odd size5 diagonal to0. The diagonal quotient moments and row sums are exactly the stated equations (1).

Detailed balance forces every positive size2-to-size5 interface to have entries5/2 and every size2-to-size10 interface to have entries5/1. Larger positive integer multiples violate the row8 bound, and two such interfaces cannot fit a size2 row. For a diagonal-zero size2 component, no external interface gives linear/quadratic totals8/13 on the equal-size symmetric entries, contradicting parity. An interface to size10 leaves3/8, again contradicting parity. The remaining size5 interface leaves3/3, forcing exactly three unit entries and no larger internal entry.

For the exceptional diagonal-one size2 possibility, the outgoing and quadratic totals are7/11. A size5 interface leaves2/1, impossible because the squared sum is at least the sum for nonnegative integers. A size10 interface leaves2/6, impossible because the squared sum is at most the square of the sum, namely4. With no external interface, the identity `sum a_j(a_j-1)=4` forces exactly two entries2, no entry>=3, and three entries1. The two double interfaces are symmetric and would meet other size2 components. Such endpoints have diagonal0 by trace1, contradicting the already proved unit-entry restriction for those endpoints. Thus the exceptional possibility is also correctly excluded.

All eight size2 components therefore require a size5 partner. Each size5 component has diagonal0 and diagonal quadratic budget16; every size2 partner costs10. Nonnegative remaining contributions allow at most one partner per size5 component. Eight mandatory interfaces exceed the total receiving capacity5. This establishes the contradiction for every labeling and every interface assignment, using only the listed necessary quotient constraints.

The review checked the potential exceptional diagonal placement, multiple interface values, the parity steps, both inequality directions, and the shared equal-size symmetry requirement. No gap or counterexample was found. No fix is required. As a nonessential observation, even leaving the exceptional size2 case undecided would force at least seven diagonal-zero size2 components, already exceeding capacity5; the longer manuscript argument is nevertheless valid as written.

This delta does not establish completion of the65-domain enumeration or any aggregate theorem. No final enumeration results or combination-theorem dependencies have been reviewed yet. Those require their actual inputs when supplied by the parent workflow. The arbitrary58–61 research goal remains open.


## Reused-agent combination delta: connected weighted defect

Added 2026-10-13 by `/root/n61_norm_lifting_proof_check`. This is the second **reused-agent delta**, not a fresh independent review round. The complete new manuscript `proofs/dd82/n61/CONNECTED_DEFECT_REDUCTION.md` was read. Its dependency connection is **PASS, sound-modulo-imports**, with same-family/provisional assurance. No blocking gap was found. The preceding local audit and capacity delta retain their original, narrower historical scope; this later integration does not retroactively enlarge those reviews.

**Exact new conclusion.** Every finite simple undirected graph on61 vertices, of maximum degree at most8 and diameter at most2, has connected positive support in its actual weighted defect `B=A^2+A-7I-J`. This is a structural restriction on arbitrary order61 targets, not a proof of their existence or nonexistence.

### Original graph and inherited c=3 branch

The original-graph hypotheses give degree8, symmetric nonnegative integer B of zero diagonal and row sum4, and AB=BA. The component-constant eigenspace argument gives the same actual equitable quotient. Rational conjugate multiplicities and nonnegative diagonal trace give exactly `c in {1,3,5,7,9,11,13,15,17}`. Component sizes are at least2; no zero-sized or isolated defect component is missing.

The c=3 exclusion is an **explicit inherited import**, not reproved in this delta. The scope of `prompts/26101310-1/final.md` and the statements and conclusions of `THREE_COMPONENT_6_25_30_EXCLUSION.md` and `THREE_COMPONENT_12_21_28_EXCLUSION.md` match the actual weighted-defect quotient used here. Together with the inherited complete c=3 classification they cover all simultaneous relabelings and impose no CP02, binary-defect, or symmetry hypothesis. Neither that classification nor its resonance calculations was rerun. The old c=3 corollary's statement that larger component counts were then open is historical and does not obstruct this new integration.

### Necessary size/diagonal domain and terminal screens

The large-domain arithmetic and spectral diagonal inequality are necessary for the actual quotient. The support diameter-two argument, prime propagation, 3-adic path bound and positive-neighbor size bound apply to every c>=5 branch. Sorting component sizes only relabels the quotient; it introduces no extra hypothesis. The interface parameter t includes every nonnegative integral balanced pair satisfying the degree and simple-interface bounds.

The current size-domain, size-screen, row-moment and norm-screen sources were read for their necessary-filter connection, together with their saved completion metadata and the existing row-moment source review. The size tuple generator traverses nondecreasing tuples with only sum/minimum/maximum pruning. Spectral/handshake diagonal restrictions, possible-support tests on an interface supergraph, and capacity upper bounds are necessary conditions. The prefix/suffix trace filter preserves every diagonal in any actual trace assignment. The row DP uses one factor for each other component and exact nonnegative row-sum/moment contributions; its truncations retain every actual target state. The norm test uses exact integer square roots and preserves the previously proved necessary products. No row-local feasibility result is promoted to common interface feasibility.

The saved terminal sequence is `36143 -> 25196 -> 142 -> 65`. Size-screen completion is true for each c. The row screen is full, has processed all25196 inputs, and has `stopped=null`. The norm screen imports that complete row result and is complete, with per-c counts `4,3,10,11,18,10,9`. These are inherited actual executions; no screen was rerun and this review does not claim to have independently regenerated the counts.

### Joint enumeration and all-label coverage

Both requested source reviews, `component_joint_quotient_code_review.md` and `component_joint_quotient_symmetry_delta_review.md`, and the full companion source plan were read. Their exhaustive-search and stabilizer-coverage arguments are explicit imports to this integration, with same-family/provisional assurance. The current source's mode selection, prior-completion selection, completion/status assignment and output routing were inspected to connect those arguments to the terminal files; the search engine was not re-executed or independently re-certified.

The unreduced profile and remaining modes traverse every allowed labelled quotient. For the final18 domains, only permutations within equal size, full original diagonal domain and assigned-column signatures are used. They fix assigned indices and the current row, and preserve the assigned state, all equations and earlier canonical choices. Sorting the current entries therefore retains a representative of any completion. Induction over subsequent assigned rows supplies the required coverage. Unique representatives or counts of all labelled matrices are unnecessary: an empty representative set excludes every labelled completion. This distinction is correctly maintained in the new manuscript.

The raw terminal records were inspected through their actual metadata, all completed size/diagonal records, saved models and interruption record:

- `component_joint_quotient.profile.json`: seven completed c=5/c=7 domains, three labelled models, no stop; CPU0.005236232.
- `component_joint_quotient.remaining.json`: forty completed domains without models, followed by a CPU interruption on `(2^8,5^5,10^2)`; CPU57.002655322. Only the forty true completion records are used.
- `component_joint_quotient.unresolved.json`: exactly eighteen selected and completed domains, nine each for c=15 and c=17, zero representative models, `stopped=null`, and combined coverage complete; CPU0.382438874, wall0.387258555740118. These include the previously interrupted tuple.

The final record's `full_input_complete=false` is not a missing-domain signal: each individual batch deliberately retains that flag, while the combined completion is the union of three disjoint completed-domain sets. The separate combined checker explicitly checks that union. Its source and saved `component_joint_results_check.result.json` were read. They match all65 original size/diagonal domains, reject duplicate completed tuples, report no missing tuple, directly verify every saved Q and test size-preserving simultaneous relabelings against the two lifting examples. The result reports per-c completed counts `4,3,10,11,18,10,9` and all three models in proved lifting cases. The saved symmetry sanity result also retains both positive examples; that is a sanity check, not the proof of general coverage.

**Finite-enumeration dependency boundary.** The saved-results checker establishes input coverage and saved-model properties; it does not independently certify search exhaustion. Exhaustion here rests on the reviewed exhaustive source algorithms, the proved stabilizer reduction and their terminal per-domain records. The same boundary applies to the completed necessary screens. No new search, gcd, model checker or screen was executed during this delta. There is no Lean proof or solver UNSAT certificate claimed.

### Returned quotients, lifting and conclusion

The raw profile contains one `(2,5,6,18,30)` Q and two `(3,3,15,15,25)` Q. The latter differ by exchanging the two size15 indices; this is a permitted simultaneous row/column relabeling and carries an actual lift to a lift of the displayed representative. The first Q has the matching edge already proved impossible. The second type has the C15 periodic-column contradiction already fully reviewed above. Therefore every returned abstract quotient fails to lift to the same actual A/B. No implication from abstract quotient existence to actual graph existence is used.

Thus every c>=5 actual quotient is either absent from the completed joint domain or belongs to an unliftable type. The inherited c=3 exclusion removes the sole other disconnected case. The exhaustive odd-count alternatives then force c=1, which is exactly connected positive support of B. The size-two capacity lemma is a valid additional result but is correctly not treated as a pruning dependency of this completed enumeration.

The integration is acyclic and no c, size domain, diagonal possibility, label class or returned model is omitted. No new mathematical issue or required proof edit was found. The combined conclusion is registered **sound-modulo-imports**, specifically importing the c=3 classification/lift exclusions and the finite-screen/search completeness and terminal results described above. Same-thread Gemini round4 is still pending at this review time; it is not supplied or replaced by this reused-agent review.

The connected case c=1 remains open, as do the arbitrary58–61 construction/exclusion goal and any exact-value conclusion. The earlier local statements “all c>=5 not excluded by this audit” remain correct historical boundaries for those earlier reviews; only this later integration establishes the connected-defect reduction modulo its explicit imports.
