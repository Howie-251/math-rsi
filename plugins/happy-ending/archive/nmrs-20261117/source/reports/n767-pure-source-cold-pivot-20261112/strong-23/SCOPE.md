# Pure-source early-terminal projection, branch (i)

Use physical order 1..23, with cold-in through set A0={6,7,8,15}, cold-out through set B={15,16,17,18}, T=A0 union B. Point p=9 is not T: it is a pure red-six source. Freeze R6(1..6), R5(6,7,8,9,15), R6(9..14), R4(15..18), R6(18..23). The last-but-one red-six family witnesses a strict early terminal q=14<c=15. Require no R6 ends at p=9, and no B5 ends at p, the latter being a necessary condition for any red-six source. Allow p to end B4 or begin B5.

Keep complete packets, no R7, no B6, all actual same-endpoint weak-seven splits, A0 no-in-B4, B no-out-B4, T no-B5 endpoints, and no T-to-T B4. The before-a1/after-b4 red-six extrema are vacuous in this selected order. Delete every p-as-T/p-cold-in condition, the private x2 no-in-B5 restriction, both gap blue-fan families, and the p-terminal-at-most-c rule. Do not require a red six from p to c. This is a fresh formula; no earlier CNF/proof is edited.

Each physical triple has one true-red variable. Independent full-clause reconstruction precedes the controlled Linux Kissat solve. SAT must pass complete literal and exact physical endpoint DP checking; UNSAT must have a successfully checked bound DRAT proof. No global theorem transfer or ambient realizability is assumed. The pure-source prohibition is local necessary data, not a claim of a complete ambient role representation.
