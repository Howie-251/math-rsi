# Independent prediction before the one-copy joint-helper toy test

Independent attack of JOINT_BATCH_ONE_COPY_PRED.md. One worker, <=15CPU for one finite toy experiment and aggregation; no q8 clonegraph, field/projection recheck, oldgraph BFS, Lean, solver or newq.

Paper target: in the exact full-product one-copy graph at fixed cap Delta=delta+1, every old non-D vertex is saturated; D and each single clone have just one spare edge. New helpers may have arbitrary internal edges, but cannot change existing edges. For an off-diagonal center c and partner T(c), classify all helper-to-c walks of length<=3. Predict the exact necessary center condition

  owner(c)=h OR owner(T(c)) belongs to closed_N_B(h).

D pins and diagonal clone pins cannot furnish another short route to these saturated off-diagonal centers. Unused clone c would force every helper to own its unique partner clone when t>=2, impossible. Thus all M off-diagonal clones are assigned uniquely. An active owner h must have internal degree>=t-2, so M<=t(Delta+2-t)<=floor((Delta+2)^2/4). Inactive helpers still count in t.

Finite test: exhaust every owner assignment, including unused=-1, and every simple internal helper graph for M in{2,4,6}, t in{2,3,4}. T pairs indices c xor1. Accept a center condition only if it covers every helper/center pair, then test every implication above and degree bound with actual minimal helper cap=max_h(pins_h+deg_B(h)). Save all case counts and any counterexample. This validates the bounded center-route model, not the full source extension.

Sharp toy prediction: t4, M12, three clones per owner, cap5; pair ownergroups0/1 and2/3 under T. Let B=K4 minus(0,1),(2,3), so internaldegree2 and totaldegree5. Verify all48 helper-to-center conditions and explicit length<=3 route witnesses in a small auxiliary route graph. No assertion that the auxiliary graph has full diameter3, is a generalized quadrangle, or realizes all constraints of a q8 source.

If supported, the consequence is only same-cap immutable one-copy arbitrary helper-batch impossibility for the two q8 cases. It excludes neither k>=2 with multiple spare slots, unsaturated center codes, altered old edges, batches introduced earlier, nor higher cap. No new graph or record is claimed.
