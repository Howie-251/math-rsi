# Candidate42343 Lean handoff: checked conditional extension, actual instances still open

Original formal target: exhibit a finite simple graph of order42343, maximum degree at most12 and diameter at most5, bound to the actual candidate construction. Mathematical construction, whole-graph checking and public-baseline review are recorded by root; this note does not turn those computations into a Lean theorem. Complete formal instances remain0.

## What was implemented and checked

The existing project uses Lean4.24.0 and pinned mathlib4.24.0. Existing graph definitions and finite verification concerned paused D2 work, so the new module imports only Mathlib.Combinatorics.SimpleGraph.Walk. No old D2 module or old root entrypoint was edited or rebuilt as a research target.

New module: formal/DegreeDiameter/Portfolio/SingleExtension.lean. Audit entry: formal/ReviewPortfolioSingleExtension.lean.

The definitions use real SimpleGraph walks. DiameterAtMost G D means every ordered vertex pair has some genuine walk of length at mostD, including the zero walk for equal vertices. singleVertexExtension G pins has carrier Option V: some v are old vertices and none is the new point. Old-old adjacency is exactly G.Adj, none--some v iff v belongs to pins, and no self-loop is introduced.

The checked theorems are:

- singleVertexExtension_diameter: old diameter<=D and pin radius<=r imply extended diameter<=max D (r+1).
- singleVertexExtension_diameterAtMostFive: the explicit D5/R4 specialization.
- parentDepthCertificate_sound: locally valid parent/depth data produce genuine bounded walks from pins to every old vertex.
- singleVertexExtension_diameterAtMostFive_of_parentDepth: combines an old D5 theorem with a valid R4 parent/depth certificate.

The parent/depth certificate's local obligations are depth(v)<=radius; depth0 implies pin membership; positive depth has a genuine old parent edge and depth(parent(v))+1=depth(v). Its soundness is proved by strong induction, appending the actual parent edge. It is not an assumed global-coverage property disguised as a field. However, building the actual finite instance still requires proofs of all local obligations.

The diameter theorem does not need a12-pin cardinality premise; twelve matters to the separate degree bound. It is conditional on the old graph's D5 theorem and never postulates that theorem as an axiom.

## Executed build and trust audit

From formal/ with the pinned environment and one worker:

    source ../.tools/lean-env.sh
    export LEAN_NUM_THREADS=1
    export RAYON_NUM_THREADS=1
    lake build DegreeDiameter.Portfolio.SingleExtension
    lake env lean ReviewPortfolioSingleExtension.lean

Both final commands exited0. build.log records a successful2.3-second module build;737 jobs is Lake's dependency target count, not737 new proofs. audit.log independently imports the built module, prints the actual definitions/types and transitive axioms.

parentDepthCertificate_sound depends only on propext. The extension theorems and combined caller depend on propext, Classical.choice and Quot.sound inherited from mathlib walk transport. There is no sorryAx, added mathematical axiom or native_decide in these proof chains. This is an incremental build using the existing pinned cache, not a fresh-environment reproduction or completed cross-family Lean audit.

Two intermediate elaboration errors were repaired before success: an implicit Option endpoint in Walk.cons, and a strong-induction zero-case substitution. They were implementation errors, not failed mathematical premises. No source or proof statement was weakened to fix them.

## Actual new12-pin certificate now exists

Root has exported new_vertex_R4_parent_depth.json, with42342 parent entries and42342 depth entries for the actual old graph. The associated new_vertex_R4_certificate_summary.json checks all parent edges against the raw source, all positive-depth decrements, and all depth0 vertices against the12 seeds:

    452,4633,6195,10312,12353,13822,
    20168,21068,24695,29805,36474,38101.

Depth counts are0:12,1:130,2:1292,3:10820,4:30088. The maximum is4. Export CPU was0.145506 seconds; root did not repeat its final all-source BFS. These are real existing instance data, not a proposed certificate and not the Lean instance itself.

The next small interface is a proved finite checker that reads the explicit old graph representation, these parents/depths and this literal pin list, and constructs ParentDepthCertificate oldGraph actualPins 4. It must verify raw vertex/index bounds, actual edge membership, depth bounds, root membership, and exact decrements, then connect its successful Boolean checks to those semantic fields. Kernel computation may use permitted decide-style proofs; compiler-backed native_decide is not an allowed shortcut. No kernel performance of this full finite instance is claimed here.

For size: parent indices fit uint16 and depths fit uint8, so the abstract arrays need about127KB in binary; the current compact JSON is327KB. A Lean literal format may be larger and should be profiled in a single relevant chunk before generating a huge source. The old graph has245217 edges; input binding to its actual adjacency is a separate requirement. A checker proof over unbound arrays would not certify the candidate.

## Remaining source and final-graph obligations

1. Define the exact old42342 graph from explicit reproducible data, and bind the actual candidate to Option(Fin42342) with none carrying label42342. The final edge file has245229 edges, comprising the old245217 and exactly12 new edges. This edge equality is computationally known but not yet a Lean theorem.
2. Construct the actual ParentDepthCertificate from the exported arrays, with proved checker semantics and a kernel-checked input instance. No missing=0 JSON is accepted as an axiom.
3. Prove old42342 diameter<=5. The source P3 file stores986 earlier-neighbor sets and empty-missing summaries, but not the full986 parent/depth forests. A possible purely finite sequential route would need41,262,621 local records over those986 prefixes (about118MiB at uint16 parent+uint8 depth), plus a genuine base proof for K41356. No such large export or Lean source is started here.
4. Prove the actual degree bounds: old degrees<=12, each of these12 pin vertices has old degree<=11, and the new pin set is distinct/cardinality12. The resulting Option graph then has maximum degree<=12 and cardinality42343. These actual finite obligations remain open in Lean.
5. Assemble the final existential graph theorem with all hypotheses discharged, and perform the required statement/axiom audit and cross-family review on that assembled result. The existing mathematical final review does not by itself review this new Lean source.

The conditional source-D5 parameter cannot remain in the final record theorem. Nothing here claims complete Lean acceptance or restores paused D2/old upper-bound tasks.

## Stored possible source-proof compression, not implemented

Root suggested using the coordinate action of SL3(F9), (u,s,v)->(A*u,s,A^-T*v) for detA=1. The proposed point orbits are s!=0; s0/pure-u; s0/pure-v; and s0/nonzero orthogonal u,v. A future finite symmetry proof could use explicit generator permutations, Schreier forests and a small set of incidence-root certificates instead of all-pairs distance data.

This is a candidate route only. It still needs genuine proofs of coordinate/Q/Pluecker preservation, automorphism correspondence, transitivity/forest coverage, the exact source point/line labels, and the tau/sigma/fold binding. None is introduced as an axiom, and no generator enumeration, incidence rebuild, BFS or large formal generation was launched by this module. A true K41356 D5 proof and the actual source extension chain remain mandatory even if this compression succeeds.

Current stopping point: the abstract extension and parent/depth soundness bridge is compiled and audited; actual source, certificate and degree instances are pending. The next useful work is the small finite-checker interface and a genuine old-source proof connection, not more candidate search.
