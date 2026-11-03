# One bounded m33 global parameter batch

The completed symbolic table has minimum capacity51, versus33 residues required at m33. The previous three-base maximum m50 had a50-form zero-redundancy bottleneck and was strictly excluded. This batch tests whether the new18-form slack can support all sixteen endpoint classes. This prediction is not an existence claim.

The sole target is this fixed four-base topology at m33, e=11, controller order132 and conditional F11³ lift order175692, a margin5942 over the located public degree77 guarantee169750. Root has cleared that actual public gate. No m36, alternate topology, local hillclimb, solver, full F11 graph, BFS, Lean or external review is authorized.

Use the exact deck gauge with base0/1/2 unchanged and base3 coordinate increased by a3. It sets A3=0, adds a3 to a2,sigma23,tau13,rho03, and preserves B's zero voltages and e=11. Units u modulo33 with u=1 modulo3 preserve e. Their action on nonzero a0 has five orbits represented by1,2,3,11,22, with sizes10,10,10,1,1. The batch cycles uniformly through these five representative branches. It does not assert that uniform representatives produce uniform labelled graphs.

With A3=0 the exact simple-controller conditions are

```
a0 != 0; sigma01 not in {0,a0};
a1 != 0; rho12 not in {0,a1};
tau02 != 0; rho03 != 0;
a2 != sigma23; tau13 unrestricted.
```

Generate independent legal values directly: a1,tau02,rho03 are nonzero, sigma01 and rho12 exclude the two specified values, a2 and tau13 are unrestricted, sigma23 excludes a2. Use one std::mt19937_64 stream with decimal seed2026110107 and unbiased rejection-based bounded draws, recording every actual candidate in order. No values are updated by a hillclimb or a previous candidate's score.

For each candidate, evaluate the complete saved symbolic support masks at e=11. Check source3/target3 first (51forms), then the remaining classes in increasing symbolic size and lexicographic order. Stop each candidate at the first incomplete class. Return the first candidate that covers all33 residues in all16 classes. Before exporting it, separately construct its literal132-vertex step table and check no loops, seven distinct neighbors, all inverse-port equations, every B triangle, all1372 symbolic-word bindings, and a full17424 ordered-pair three-port-word certificate.

Stop at the first actual controller,2,000,000 legal candidates, or the cumulative30CPU-second limit including preparation, compilation and export, whichever comes first. A sample or CPU stop is UNKNOWN for the fixed family, not an exclusion. Record first-failure distributions, a complete16-class coverage signature for a representative actual candidate, seed, all candidate attempts, CPU receipts and no-active-process terminal state. The packed attempts file has12 unsigned bytes per row in voltage order(a0,a1,a2,a3,sigma01,sigma23,tau02,tau13,rho03,rho12), then first-failed source*4+target (255if none), then that class's support size (33if all pass); row number minus one is the branch-cycle index.
