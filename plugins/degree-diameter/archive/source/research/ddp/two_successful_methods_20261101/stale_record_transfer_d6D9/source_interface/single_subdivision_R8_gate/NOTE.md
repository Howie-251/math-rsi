# Three single-edge-subdivision endpoint gates

Actual status: COMPLETE_NO_SINGLE_EDGE_SUBDIVISION_D9_ON_FIXED_SOURCE

- Generator[25, 1254]: covered317299, missing14088; first target20=[0, 20]. New subdivision root has distance at least10 to that target.
- Generator[18, 541]: covered317512, missing13875; first target6=[0, 6]. New subdivision root has distance at least10 to that target.
- Generator[47, 4642]: covered317359, missing14028; first target20=[0, 20]. New subdivision root has distance at least10 to that target.

The one depth8 multi-source traversal per type computes B8_H(1) union B8_H(s), H=G−{1,s}. A shortest path from new degree2 z first uses one endpoint and then stays in H, so its old-vertex distances are1+the endpoint minimum. No original-source radius9 check is needed or performed. A radius8 miss is a proved lower bound of10 for the new point; no unsupported exact distance10 or path is claimed.

Every edge of the right Cayley graph is a left translate of {1,s} for one of the three positive generators; inverse orientations give the same representatives by translating with s. Left translation also transports the subdivided graph. Thus three failures exclude exactly every single-edge subdivision on this fixed source. A hypothetical pass would only certify new-root coverage, not old-old routes.

The old source is reconstructed only implicitly from inherited group constants and true inverses; no raw adjacency is read/generated or AUTHOR main run. The author left/right convention is handled by the inherited inversion isomorphism. Old field/order/degree/D9 facts are not rechecked.

Budget inherits0.222025744, charges preparation0.15, compiler0.386869000, actual queries and driver. Cumulative0.827465255/10CPU, one worker. All work stops after these gates; no old-pair BFS, other edge modification, generator, field, solver, Lean or review follows.
