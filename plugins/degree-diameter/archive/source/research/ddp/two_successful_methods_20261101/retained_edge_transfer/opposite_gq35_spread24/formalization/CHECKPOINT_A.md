# 6160 actual statement alignment (new scope)

Original source: ../PARAMETERS.json, ../PROOF.md and ../EXTENSION_STEPS.json.
This is the new fixed GF4 Payne-GQ opposite graph plus all16 vertical-spread
vertices, not the canceled4544 full-neighborhood-clone candidate.

Read actual bodies in:
- formal/DegreeDiameter/Portfolio/OppositeGQ35SpreadGeneric.lean: graph
- formal/DegreeDiameter/Portfolio/OppositeGQ35SpreadDefinitions.lean:
  linePointData,pointLineData,linePoint,pointLine,Inc,spread,spreadOwner,
  oldEquiv,old,graph,label,FinalClaim.

Point code a+4*b+16*c uses the PARAMETERS binary GF4 labels0,1,w,w+1.
The formal graph is defined by the actual96 ordered four-point line rows;
its definition does not reinterpret arithmetic as ZMod4. `Inc p l` means
literal occurrence of p among line l's four entries.
The source label equivalence is Fin6144 ≃ Fin64×Fin96 with old label96*p+l.
The actual carrier is Fin6144 ⊕ Fin16; `label` is the explicit equivalence to
Fin6160 and maps old v to v and new j to6144+j. Spread j is line j,0≤j<16.

Expanded graph body:
- old u,old v: u≠v and Inc(point u,line v) and Inc(point v,line u);
- old u,new j (and reverse): Inc(point u,line u) and Inc(point u,spread j);
- new,new: False.
Thus added neighbors are all flags whose point is on that vertical spread line.
All old edges are retained and loops excluded.

FinalClaim is exactly:
Fintype.card Vertex=6160 ∧ (∀v,graph.degree v≤24) ∧
DiameterAtMost graph 3 ∧ ¬DiameterAtMost graph 2.
DiameterAtMost is the existing SingleExtension definition: every ordered pair
has a genuine SimpleGraph.Walk of length at most the bound.
The final theorem will be unconditional; FinalClaim is presently a definition,
not a proof or completion claim.

Highest development interfaces, all to be supplied internally:
1. actual point-line `project`: ∀p l,∃q m,Inc q l ∧ Inc p m ∧ Inc q m;
2. actual every-incidence coverage by pointLine's6 indices, and unique
   spreadOwner for every incidence with a spread line;
3. generic projection→trueWalk≤3 proof; finite24-slot neighbor enumeration
   whose self-slot is replaced by the unique new spread neighbor;
4. generic D2→card≤1+24+24²=601, then6160>601.
No projection/capacity/coverage certificate may remain a final user premise.

Budget: generic proof600CPU + finite inputs600CPU, eachmodule115CPU, initially
one-j1 main compiler. Independent generic-lower helper has separate-j1 receipt
and root authorization. Reuse original pinned Lean4.24/cache/LEAN_PATH/directLean.
No old module rebuild, BFS, solver, installation, hash or native_decide.
This packet is new A scope; prior F4/clone reviews do not cover it. External A is
pending root coordination, while legal local implementation continues.
