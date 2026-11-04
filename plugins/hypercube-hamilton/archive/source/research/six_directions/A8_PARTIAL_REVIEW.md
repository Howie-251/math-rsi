# Independent audit of the partial A8 proof package

2026-11-01. Fresh reviewer `/root/ten_hole_free_closure_audit`; user-directed
`gpt-6.1-sol / high` overrides the ARIS proof-checker default model/effort.
Assurance: **same-family / provisional**.

**PASS for the explicitly partial scope:** augmentation to A6, every remaining
instance with a delta1/2/3 coordinate cut, and the exact reduction to160 marked
hole geometries in five coordinate-permutation orbits. This report does not
accept the full A8 statement printed under Claim. The draft explicitly marks
that statement NOT CURRENTLY JUSTIFIED and leaves its five residual families
open, which is the correct scope. The separate double-bridge and first-orbit
drafts are not used here. No production proof, census or main state is changed.

## Canonical statement and imports

For every arbitrary complete-graph matching F on Q5 with three minority and
five majority holes and every specified majority hole v, if either there is
a short edge between minority and nonforbidden majority holes, or there is
a coordinate face A containing v with majority-minus-minority hole imbalance
in{1,2,3}, then a simple cycle on exactly Q5−v contains F and has only short
edges outside F. In the cut branch assume no augmenting hole edge remains;
otherwise the augmentation branch has already solved the instance.

The complete A6 theorem is an explicit accepted import. GQ4-avoid and
GQ4-cycle are the stated arbitrary-complete-graph-matching theorems in
`Q4_GENERAL_AUGMENTATION.md`; their augmentation proofs were read together
with their exact N14_4, A4_4, N10_4, NC_4 and K4_4 base statements in
`Q4_CORE_AND_A4_SPLIT.md`. Their ultimate perfect-matching extension theorem
is a declared external input. O15 and O18 are the exact four-hole optional
edge union bounds of `A6_CLOSURE_DRAFT.md` Section2, with accepted independent
finite review. The full A6 review explicitly audits all these general Q4
inputs and optional-union consequences. Four relevant reports are PASS;
14 recorded source/artifact hashes agree with current inputs. Their large
finite matching certificates are imported, not rerun in this audit.

The acyclic dependency graph is Q4 base inputs and optional-union certificates
→ GQ4/O15/O18; separately accepted Q5 A6 → short-hole augmentation. The new
transfer proofs plus independently reconstructed geometry imply the stated
partial A8 theorem. No Q5 A8/A10, Q5 T15, higher-hole P6, or new double-bridge
mechanism is used to prove an upstream import.

## Proof-obligation ledger

E,O denote global minority/majority parity, not necessarily numerical even/odd.
Crossings C may be arbitrary long edges: their B endpoint need not be the
mirror of their A endpoint. A mirror always means the short coordinate edge.
D is an arbitrary artificial matching on currently uncovered A ports and
selected original holes. Compressed edges encode internally disjoint paths.

| ID | Obligation and discharge |
|---|---|
| P01 | Augmentation uses two originally free vertices, excludes v, and leaves exactly two minority/four majority holes. The full arbitrary-matching A6 theorem therefore applies. Its added requirement edge was short relative to original F. |
| P02 | In either Q4 parity class, two different vertices have six or eight distinct neighbors. Thus they cannot avoid three opposite-parity vertices. This statement is symmetric in the two parity classes and invariant under face projection. All56 same-parity pairs are checked independently. |
| P03 | The face equation2|F_A|+c=16−|H_A| determines c parity without assuming required edges bipartite or short. Delta2 has even c, while delta1/3 have positive odd c. |
| P04 | Deleting a nonempty matching from one simple cycle leaves a forest with exactly its endpoints. Restoring a proper subset of the deleted gaps through fresh vertices preserves a forest. Crossings attach at distinct ports, disjoint from F_A and original holes. No endpoint tag is necessary: the target object is a single cycle avoiding v. |
| P05 | Delta2,c>0: D pairs all A ports and leaves exactly original H_A of excess2. GQ4-avoid omits v. Deletion and all crossings give a matching R on precisely X_B, disjoint from F_B. B holes are exactly original H_B, balanced, so GQ4-cycle applies and expansion gives the31-cycle. |
| P06 | Delta2,c=0: with k minority A holes, counts are(k,k+2) in A and(3−k,3−k) in B. At k=0 B contradicts P02 and no-augmentation; at k≥2 A does, using three majority holes other than v. Hence k=1. The exact O15 and O18 hypotheses are(1,3), omit specified v, and(2,2), full cycle. Both unions project into the same32 Q4 short edges, so15+18>32 yields a common optional edge. Choose a separate witnessing cycle for that edge on each face, remove optional edges and add both corresponding short bridges. Every required edge survives and the two disjoint cycles become one31-cycle. |
| P07 | Delta3: at least two nonforbidden majority A holes exist. If c=1 their distinct mirrors cannot both be the unique B port, so select an internal mirror. No-augmentation ensures each such mirror is covered and of global minority parity. Pair X_A plus selected t; its even size and disjointness make D valid. The new A hole excess is2 and v is untouched. |
| P08 | Delta3 internal mirror w: all original crossings and tw attach to different B vertices. Compression gives endpoints X_B plus w. Its F_B mate k is outside those endpoints: internally covered, not a port, not w. Thus with q the other endpoint of w's compressed path, k≠q. Replacing wk,wq by kq is a valid matching. Holes become H_B plus w, of excess−2; w is a newly free majority vertex in this orientation. GQ4-avoid omits it, and expansion restores w, all A−v and every original edge. |
| P09 | Delta3 port mirror w: its actual crossing partner x is an A port distinct from t; prescribe tx in D. Here c≥3, so D has at least two edges. Endpoints of the removed tx edge lie in different residual components. Adding tw and the required xw restores exactly that gap and leaves at least one other gap. The forest compresses onto X_B minus w, its interiors include A−v and w, and F_B has no edge at port w. Its holes are H_B plus w; GQ4-avoid omits w before expansion. |
| P10 | Delta1: writing A counts(k,k+1), k=0 or1 would place two minority and three nonforbidden majority holes in B, contradiction. Hence k≥2. For c=1 choose y with mirror outside the unique B port, possible with at least two y choices. It is covered: v is in A and any other majority hole adjacent to y is excluded by preprocessing. |
| P11 | For delta1 choose port d, pair other ports into D and add dy. These edges are disjoint from F_A and each other. Holes are H_A minus y, of majority excess2, containing v. GQ4-avoid supplies a cycle containing dy; delete dy to get a path on A−v from d to y, retaining F_A+D. This works for arbitrary required dy length/parity. |
| P12 | Delta1 internal mirror: delete D and attach crossings plus yw. The endpoint set is X_B plus w. The sole overlap with F_B is w; its original mate cannot be another endpoint, by the matching condition. Suppression yields holes H_B plus w, now majority excess2. GQ4-avoid avoids w, then expansion restores it. The c=1 case has D empty but the initial dy deletion already supplied a path, so no nonempty-D hypothesis is needed here. |
| P13 | Delta1 port mirror: c≥3 and choose d to be w's actual crossing partner, not its mirror. Then D is nonempty. Deleting D from the simple d–y path puts d and y in different components. Adding required dw and short yw joins those components without a cycle; other crossing attachments are distinct. Compression and B avoidance have exactly holes H_B plus w. No A6 k=c=1 exceptional endpoint input is needed because k≥2. |
| P14 | Every compression has disjoint path interiors, B theorem quantifiers allow arbitrary auxiliary long or same-parity edges, and the omitted B bridge vertex is outside its local cycle. Expansion therefore produces one cycle with exactly31 vertices, all original F edges and no artificial long edges remaining. All added bridges and every surviving optional local edge are short. |
| P15 | Translating v to0 makes majority holes even. Write its other four holes Z and the three minority holes W. No-augmentation means precisely no Z–W adjacency; adjacency from0 to W is allowed. All15 nonzero even four-subsets and all eligible odd triples are covered without matching realizability assumptions. Coordinate permutations fix0 and transport every matching and specified forbidden vertex. |
| P16 | The independently reconstructed domain, full sorted-delta histogram, residual members, ordered member deltas, empty good-cut lists, five representatives and orbit sizes agree exactly with the writer's census and the prior independent Q5 geometry review. The residual160 geometries remain explicit open obligations for all arbitrary matchings on24 covered vertices. |

## Independent finite verification

`A8_PARTIAL_REVIEW_check.py` imports no producer or supplied checker and does
not execute them. It reverses this writer's geometry loops, choosing the
three odd holes first and then all allowed even quadruples. It reconstructs
all2700 marked hole configurations and confirms2540 have a delta1/2/3 cut.
The remaining160 are expanded independently under adjacent coordinate swaps,
which generate the full stabilizer of0. Every one of the writer's residual
members, including ordered deltas and good-cut fields, is compared; no orbit
or histogram statistic is merely accepted from a prior report.

| Z | W | Residual orbit size | Ordered deltas |
|---|---|---:|---|
|3,5,6,15|8,25,26|60|0,0,−1,4,4|
|3,5,6,15|25,26,28|20|0,0,0,4,5|
|3,5,15,23|25,26,28|30|−1,0,0,4,4|
|15,23,27,29|1,2,4|30|−1,0,0,−1,−1|
|15,23,27,29|2,4,8|20|−2,0,0,0,−1|

Feasible cut populations in this exact domain have(delta,k) equal to(1,2),
(2,1), or(3,1). Delta1/3 have c in{1,3,5,7,9,11}; delta2 has c in
{0,2,4,6,8,10,12}. These finite checks corroborate the symbolic proof's
broader sufficient hypotheses without narrowing any matching quantifier.

The checker also examines all1363 nonempty matchings of deleted edges from
a labeled15-cycle. For each possible bridge endpoint it checks the internal
mirror and, with a proper gap left, prescribed port-gap restoration for
delta3 and delta1. It validates exact endpoints, degrees, distinct compression
endpoints and absence of cycles by graph traversal. This gives1363 delta2
checks,11310 internal checks per odd-delta branch, and11280 port checks per
odd-delta branch. It explicitly constructs the30 one-gap oriented port-mirror
cases that would close a circle prematurely; those are excluded by the c=1
bridge selection, exactly as required by the proof. These are topology checks
on all relevant cyclic gap orders, not tests of sampled matching extensions.

Counterexample attempts also targeted c=0, a same-parity long crossing,
internal mate equal to a compression endpoint, v chosen as source, mirror
equal to a free original minority/majority hole, a port bridge at c=1,
prescribing an entire optional-edge union simultaneously, and full A8 inferred
from the geometry counts. Each is excluded by the explicit hypotheses or
scoped conclusion. No unresolved issue was found in the partial theorem.
No analytic interchange, probability or asymptotic-uniformity claims occur.

The machine-readable report binds the three submitted inputs, all imported
theorem/review files and the independent checker/results by SHA256. The full
A8 claim remains unproved by this package; later first-orbit or double-bridge
results require separate independent acceptance and do not change this scope.
