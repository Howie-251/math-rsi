# Nonadjacent-hole opening reduction (producer optimization, not acceptance)

2026-11-02. Root-star exploration continuation. All assertions about new B local inputs and A opening remain conditional on their own fresh gates.

Exhaustively enumerating all q,t,w,b for the six235 diagnostic Z orbits, with b not adjacent to q, and B lookup among old accepted7 + new15 candidates + newB10 candidates, leaves bad nonroot even q sets:

1. {24,30}
2. {20,24,30}
3. {17,24}
4. empty
5. {12,18,30}
6. {12}

Since the actual matching has at least four even A ports, every orbit has a usable actual port. The original even ports are unchanged when the target's cross edge is replaced by the virtual w-h cross. Thus the existence argument applies to every original short M; q and subsequent w,b,D may depend on M.

Number the five nonadjacent canonical inputs 0:(3,4,7), 1:(3,4,11), 2:(15,1,14), 3:(15,1,7), 4:(15,16,7), where each tuple is (q,b,t). The same good-q sets result from any pair consisting of one case from {0,1} and one from {2,3,4}. These are all six minimum two-case sets for the simple four-even-port argument. No singleton suffices for that counting argument: cases0/1 only address weight2 q, leaving five weight4 points; cases2/3/4 only address weight4 q, leaving ten weight2 points. This is not an absolute lower bound on every possible proof strategy.

Suggested pair: case0 (3,4,7) and case3 (15,1,7). Both have b contained in t and d(q,b)=3. The completed producer probe summary reports rank8031 for each, while the other three report7998. No8192-fullrank assertion is made, and these ranks do not refute their bipartite-column or structured-column opening interfaces.

All explicit choices, synchronous B-row IDs, good-q lists and the six minimum case sets are saved in TWELVE_ROOT_STAR_NONADJACENT_OPTIONS.json. These are author finite diagnostics, not independent coverage acceptance.

GNS2018 reference check: [Gregor–Novotny–Skrekovski, Theorem3](https://www.combinatorics.org/ojs/index.php/eljc/article/download/v25i2p56/pdf/) concerns a perfect matching of the complete bipartite graph after deleting opposite-parity vertices, with half-layers as the obstruction; the paper includes a computer-checked n=5 base. It does not supply the unrestricted complete-graph version (stated as Conjecture8), nor a specified opening edge. Our F_A covers only28 of the30 retained vertices: q,b remain holes. Completing by the long pair qb would change the prescribed matching and would still not force qt; deleting qb from such a cycle gives a different path interface. Therefore this theorem has not been applied as an established input to the root-star route.
