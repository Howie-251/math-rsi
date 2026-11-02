# Actual7531 object and capacity interface — new scope

Original ../PARAMETERS.json, ../PROOF.md, ../ORDERED_CENTERS.json and
../IMMUTABLE_SOURCE_PINS.json. This is the one7531 clone graph from the fixed
accepted7242 source, not a regular completion or another same-order variant.

Actual bodies, already compiled:
- formal/DegreeDiameter/Portfolio/OvoidSpreadCloneCapacity.lean: center,
  adjacent_centers_unique and load_le_one. Source is the original
  OppositeGQSpread.graph e Inc spread on V⊕J. Product center(i,j) is always
  inl(e.symm(ovoid i,spread j)). Hypotheses are only hO:two ovoid indices on
  one line are equal, and hS:two spread indices through one point are equal.
  For old source w, use its line for hO and its point for hS. For bonus source
  w=inr k, each adjacent center must be a flag with spread j=k; then hO on
  spread k identifies its ovoid index. This proves any two adjacent center
  indices equal, so the subtype of adjacent center indices has card≤1.
  No center injectivity or independence hypothesis occurs. Actual PASS2.161900CPU.
- OvoidProduct26Definitions.lean: actual17 ovoid IDs in original ascending
  order, actual center, graph, cloneLabel,label,all label/card theorems,
  auxiliary finite ovoid-owner/index data and FinalClaim. Actual PASS2.259311CPU.

The source constant is exactly OppositeGQ44Spread.graph from its completed
7242 theorem. `graph := FullNeighborhoodClones.graph source center` always
uses that ORIGINAL fixed source adjacency:
- old-old: source.Adj;
- old-new ij: source.Adj old (center ij), with its symmetric case;
- new-new: False.
There is no parameter for an evolving graph or current(center). Adjacent
centers are allowed; the producer's actual centers induce136K2+17 isolates.
They do not authorize new-new edges.

Actual carrier is Source25.Vertex ⊕ (Fin17×Fin17), where Source25.Vertex is
Fin7225⊕Fin17. `cloneLabel` is the explicit product equivalence to Fin289.
Full `label` combines the already-proved source label and product label,
then finSumFinEquiv, giving an explicit equivalence to Fin7531.
Proved label_new(i,j)=7242+17*i+j, label_old=source.label, and center source
label85*ovoid(i)+spread(j). Thus original ovoid outer/spread inner order is kept.

FinalClaim is the closed target definition:
card Vertex=7531 ∧ (∀v,graph.degree v≤26) ∧ trueWalkD3 ∧ nonD2.
It is not yet a proved concrete theorem at this checkpoint.
Highest remaining interface is actual hO:the new Inputs module uses17 owner
lookups and425 positive line positions with an85-line index certificate.
Actual hS reuses the completed source spread_unique theorem. Then load≤1 plus
source degree≤25 proves cap26. Source trueWalkD3 plus two distinct source old
vertices proves no isolates; unchanged generic full-neighborhood-clone Walk
lemmas prove D3 and preserve old-old bounded-Walk iff, inheriting nonD2.
All finite conditions must be internal proofs; none may remain a user premise.

Budget300CPU total,115/module,singleworker. No old25/6160/F4 source/cache
modification or rebuild, BFS, solver, install, hash,native_decide,new axiom,
regular completion or parameter ladder. New-scope review is root-coordinated;
prior reviews do not silently cover this actual product-center encoding.
