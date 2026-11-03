# Actual final7531 theorem — new clone composition scope

The requested concrete7531 graph is now kernel complete. Read ../PARAMETERS.json,
../PROOF.md,../ORDERED_CENTERS.json and ../IMMUTABLE_SOURCE_PINS.json plus the actual source
bodies below. Original7242source and previous FullNeighborhoodClones generic
proofs are unchanged and reused, not rebuilt. Review this new composition and
its actual caller, not a hypothetical independent-center special case.

Actual final source chain:
- formal/DegreeDiameter/Portfolio/OvoidSpreadCloneCapacity.lean: center and
  adjacent_centers_unique,load_le_one. Only hO and hS are hypotheses. For old
  source w, hO uses line(w),hS point(w). For bonus source k, hS forces each
  adjacent center's spread index to k, then hO uses spread k. Two adjacent
  center INDEX values agree; cardinality of that subtype is≤1. No center
  injectivity or independence hypothesis is present. PASS2.161900CPU.
- OvoidProduct26Definitions.lean: actual17 ovoid IDs; center=old(ovoid_i,spread_j)
  in the ORIGINAL fixed source graph. Actual graph is
  FullNeighborhoodClones.graph OppositeGQ44Spread.graph center. It retains every
  original source edge, new pins use only source.Adj(center,..), new-new False.
  No current graph appears. Product Fin17×Fin17≃Fin289 and total Fin7531
  equivalences explicitly preserve original source labels and new7242+17*i+j.
  center_source_label is85*ovoid_i+spread_j. PASS2.259311CPU.
- OvoidProduct26Inputs.lean: owner_of_ovoid's17 finite checks and
  line_index_certificate's425 positive original line positions give actual hO
  on all85 lines. hS is supplied by the completed source spread_unique theorem.
  Actual load_le_one has no hypothesis. PASS10.249949CPU. No Q algebra or
 7242×289 adjacency enumeration is substituted for the argument.
- OvoidProduct26Exact.lean: source_no_isolated uses actual accepted source
  trueWalkD3 and explicit distinct source old0/old1. Source regularity is not
  assumed. FullNeighborhoodClones.degree_le supplies≤25+1; its actual Walk
  construction supplies D3, including the center-distance1 detour. Its
  old_walk_bound_iff preserves ALL old-old bounded-Walk statements, and
  not_diameterAtMost inherits the source nonD2. Final theorem is closed.
  PASS2.207549CPU.
- formal/OvoidProduct26Audit.lean plus actual log: separate import, expanded
  center/FullNeighborhoodClones adjacency body, label types, actual final
  type/body and axioms. PASS2.143142CPU.

Final actual declaration at Exact.lean:37:
DegreeDiameter.Portfolio.OvoidProduct26.concrete_order_degree_and_exact_D3 :
 card Vertex=7531 ∧ (∀v,graph.degree v≤26) ∧
 DiameterAtMost graph3 ∧ ¬DiameterAtMost graph2.
`final_claim : FinalClaim` is also proved. DiameterAtMost is the existing
SingleExtension real SimpleGraph.Walk length bound. Carrier is
(Fin7225⊕Fin17)⊕(Fin17×Fin17), explicitly equivalent to Fin7531 via label.
A separately transported SimpleGraph(Fin7531) is not claimed. The theorem proves
an upper degree bound; exact histogram/source regularity/capacity optimality
are external paper/producer results and were not added as user premises.

Actual receipt FINAL_COMPILE_RESULT.json: all5 new modules first-attempt exit0,
measured Lean child CPU19.021851<300, singleworker,115CPU/module. Final and actual
load axioms exactly propext,Classical.choice,Quot.sound; hO only propext.
No sorryAx/new axiom/native_decide. No old25/6160/F4 source/cache changed or
rebuilt, no BFS/solver/install/hash/regular completion or candidate variant.

INPUT_BINDING_CHECK.json is actual external readback:17 ovoid IDs and inherited
original17spread order; all289 owner labels equal ORDERED_CENTERS,
IMMUTABLE_SOURCE_PINS and EXTENSION_STEPS at the SAME index. All7225 pin labels
are sorted ORIGINAL7242source neighbors and below7242, never current(center).
The source's completed90525edge formula binding is reused unchanged. New formula
matches all97750 literal edges with0newnew. Actual centers may be adjacent
(the original producer records136K2+17isolates); no independence condition was
introduced to evade that fact. This is not an ASCII-parser theorem or a new
independent BFS. Separate fresh acceptance actually PASSed289newroots and
checked0oldroots, reusing the retained accepted source as authorized.

Newscope A is root cell140 pending at packet creation; B packet and this actual
finalC packet are root-coordinated. Do not silently promote prior source/clone
reviews to this composition. Public guarantee7514 and7531's17-vertex difference
are parent-owned comparison; global-record status and priority remain unconfirmed.
