# Proof Package: alternative T15 cores18,21,25

Date: 2026-11-01. ARIS proof-writer. New result only; no previously audited file or global state is modified.

## Claim

For each row below, every arbitrary complete-graph matching $F$ on $V(Q_5)$ whose holes are $\{0\}\cup O\cup I$ extends to a simple cycle on $V(Q_5)\setminus O$, with every added edge short. The marked omitted pair is $O$. Cube-automorphic images and either global parity orientation are included.

| Core | $O$ omitted | $I$ retained holes | cut coordinate |
|---:|---|---|---:|
|18|$\{1,7\}$|$\{11,14,28\}$|2|
|21|$\{1,7\}$|$\{11,22,28\}$|2|
|25|$\{1,7\}$|$\{14,26,28\}$|1|

## Status

**PROVABLE AS STATED**, relative to the previously imported Q4 N14 theorem and audited balanced Q4 tables. Every new finite input and every positive residual certificate described below has been checked by a separate implementation. Fresh-context semantic audit is pending. This package does not claim full T15 or eight-hole P6; parent coverage requires a separate geometry calculation.

## Assumptions and notation

Original matching edges may have arbitrary length and parity. A short edge joins binary labels differing in one coordinate. Delete the cut coordinate and use common local Q4 labels on the one-face $A$ and zero-face $B$. For core25 additionally send local bit positions $(0,1,2,3)$ to $(3,0,1,2)$ on both faces. The exact resulting geometry is independently verified in `t15_alternative_small_verification.json`.

| Core | A holes $\{x,r,s\}$, omit $x$ | B holes $\{0,7,y\}$, omit $y$ | negatives for bridges $r,s$ |
|---:|---|---|---|
|18|$\{3,6,12\}$|$\{0,7,1\}$|$2,1$|
|21|$\{3,10,12\}$|$\{0,7,1\}$|$1,1$|
|25|$\{9,3,6\}$|$\{0,7,8\}$|$10,10$|

Write $F_A,F_B$ for the internal matchings, $C$ for original crossing edges, $X_A,X_B$ for their endpoint sets, and $c=|C|$. Both faces have thirteen originally covered vertices, so $c$ is odd and $1\le c\le13$. The crossing partner bijection is arbitrary throughout.

For a bridge label $z\in\{r,s\}$, let $w$ be the other label. The imported balanced Q4 table concerns holes $\{0,7,y,z\}$, omits $y,z$, and classifies all $10395=11!!$ arbitrary required matchings on the other twelve vertices. The table has a positive explicit fourteen-cycle for every nonnegative entry. All table images used here are obtained by coordinate permutations preserving $0,7$.

## Proof strategy and dependency map

1. Import Q4 N14 at its arbitrary complete-graph scope: two equal-parity holes allow a fifteen-cycle omitting either specified hole.
2. Use N14 with an arbitrarily chosen artificial boundary pairing. Its output pairing must form one alternating cycle with the chosen pairing.
3. For cores18/21 a single negative table entry for bridge12 makes every $c\ge5$ input avoidable by a deliberately disconnected artificial pairing.
4. For core25 transport the fully checked core23 B inverse-blocker certificate to bridges3,6; the A omitted label plays no role in that certificate.
5. Exhaust all small-crossing B spectra, then verify every exceptional $c=1$ input by a direct positive cycle certificate.

## Proof

### Step1. The arbitrary boundary-pairing construction

Fix $z\in\{r,s\}$. For every perfect pairing $D$ of $E=X_A\cup\{z_A\}$, the matching $F_A\cup D$ has exactly the equal-parity holes $x,w$. N14 gives a fifteen-cycle on $A-x$ containing it. Delete $D$. The result is a spanning forest of paths inducing a pairing $R$ of $E$. The multigraph $R\cup D$ is connected: contracting the remaining paths in the original cycle yields this alternating cycle. Every surviving edge outside $F_A$ is short.

Attach all original crossings and the short bridge $z_Az_B$.

If $z_B\notin X_B$, it is internally matched to $k=F_B(z)$. The paths have distinct B endpoints in $X_B\cup\{z_B\}$ and cannot close a component. Add $F_B$, suppress $z_B$, and compress all paths. The resulting matching $L$ has holes $\{0,7,y,z\}$. The map from $R$ to $L$ is injective: identify the mate $q$ of the fixed internal vertex $k$ in $L$, restore $kz,zq$, remove the other fixed edges of $F_B$, and pull crossing labels back to A. Thus a table with $b$ negatives forbids at most $b$ possible output pairings $R$.

If $z_B\in X_B$ and $c\ge3$, let $d=C^{-1}(z_B)$ and prescribe
$$D=\{z_Ad\}\cup D',$$
where $D'$ is any pairing of $X_A\setminus\{d\}$. Because at least two edges of the original A cycle are deleted, $z_A$ and $d$ are in different remaining path components. Adding the bridge joins these components through the crossing at $d$, with no closed component. Their resulting pairing on the remaining boundary is $Q$. Suppression of the distinguished edge $z_Ad$ in the alternating cycle shows that $Q\cup D'$ is connected. After transport to B, the compressed required matching is $L=F_B\cup Q_B$, with holes $\{0,7,y,z\}$. Again at most $b$ output pairings are negative.

Whenever $L$ is positive in its table, expand its required edges through the remembered disjoint paths. The fourteen-cycle restores fifteen A vertices and the suppressed B vertex $z$, hence becomes a thirty-cycle on exactly $Q_5-\{x_A,y_B\}$. It contains all original internal and crossing edges. Only short A edges, short bridges, and short B cycle edges survive as added edges.

### Step2. All large crossing counts for cores18 and21

Choose $z=12$, whose table has exactly one negative matching in either geometry. In the internal case there is at most one forbidden pairing $R_0$. For $c\ge3$, the boundary has $c+1\ge4$ vertices. If a forbidden pairing exists, take $D=R_0$. Then $R_0\cup D$ is a union of at least two doubled matching edges, so is disconnected. The N14 output must be connected with $D$ and therefore differs from $R_0$. If there is no forbidden pairing, any $D$ works.

In the occupied case, for $c\ge5$ the remaining boundary has $c-1\ge4$ vertices. If a forbidden $Q_0$ exists, choose $D'=Q_0$. The same disconnected-union argument forces the N14 output to differ from $Q_0$. Thus bridge12 handles every $c\ge5$ input, uniformly in the original matching and crossing bijection. The internal $c=3$ case is also handled here, but Step4 treats all $c=3$ cases together.

### Step3. All large crossing counts for core25

The B geometry is $\{0,7,8\}$ with bridges3,6. Swap local bits0 and1 in the already developed B geometry with bridges3,5. This permutation fixes $0,7,8,3$ and sends5 to6. It sends the complete negative table families and every boundary pairing to the target families, preserving graph connectivity.

`verify_t15_alternative_core25_blockers.py` reruns the complete inverse-family and graph-connectivity check of `r3_boundary_blocking_3_8.json` into new output files, then independently checks this coordinate transport against the complete negative lists for both target bridges. It verifies2644 explicit blockers for bridge3, including complete reconstruction of every inverse family, and checks the mapped bridge6 families. No original audited file is rewritten.

The checked property is: for every fixed $F_B$, all possible bad output pairings can simultaneously be disconnected from a suitable artificial pairing whenever the bridge mirror is internal and $c\ge5$, or occupied and $c\ge7$. Pull that artificial pairing back through the arbitrary crossing bijection and apply Step1. Its connected output avoids every bad pairing and is positive.

For occupied $c=5$, there are precisely two unblocked internal B matchings for each bridge. Each has all three possible output pairings bad. The two target null families are explicitly listed in `t15_alternative_core25_blockers_verification.json` and have empty intersection. If either bridge mirror is internal, its internal blocker already works. If both mirrors are occupied, at least one bridge lies outside its null family and has a valid blocker. Consequently every $c=5$ input is handled as well.

The blocker calculation depends on the B geometry, internal B matching, boundary pairing and crossing bijection. It does not use $x$, the third A hole, or the particular A internal matching. Therefore the fact that this coordinate swap would move the core23 omitted A label9 to10 does not affect its application to core25 with omitted A label9. N14 in Step1 is applied directly to the actual core25 A geometry.

### Step4. Complete three-crossing classification

For $c=3$ there are three pairings of each four-vertex A boundary $X_A\cup\{z\}$. At least two are realizable: if only $R_0$ were realizable, selecting $D=R_0$ in Step1 would make its output union disconnected, contradicting N14.

For each B internal partial matching and each ordering of its three crossing ports, test these three abstract pairings for each bridge. Map endpoints through the specified crossing order, add $F_B$, reject loops or closed components, suppress the bridge mirror, and consult the exact balanced table. This determines the B-admissible pairing subsets without referring to an A matching.

The separate checker `verify_t15_alternative_small_B.cpp` independently traces graph paths and reads the original audited binary tables. For each core it exhausts all
$$\binom{13}{3}9!!\,3!=1621620$$
B partial matchings with ordered ports. Every input has a bridge with at least two of its three pairings admissible. This property is asserted for every nonzero histogram entry by `verify_t15_alternative_small_results.py`; producer and independent histograms coincide exactly. Therefore that bridge's at-least-two realizable A pairings and at-least-two admissible B pairings intersect. Step1 expands their common pairing to the required cycle.

Ordering all B ports covers every original crossing bijection: order the actual A ports once, and then list their B mates in that order. No restriction on lengths, positions, or partner order is imposed.

### Step5. Complete one-crossing classification and certificates

For $c=1$ the A boundary has just two vertices, hence its unique pairing is realizable by N14. The complete B enumeration has $13\cdot11!!=135135$ inputs per core. The only inputs with neither bridge admissible number respectively3,2,20 for cores18,21,25. The independent graph checker regenerates these exact lists. `verify_t15_alternative_small_results.py` checks equality with the lists supplied to the residual producer, including duplicate and count checks.

For each exceptional B input, enumerate all thirteen A port choices and all $10395$ pairings of the other twelve originally covered A vertices. The crossing is uniquely determined by the chosen A port and the exceptional B port. The certificate outcomes are:

| Core | Exceptional B inputs | Complete residual inputs | Positive | Unknown or exhausted |
|---:|---:|---:|---:|---:|
|18|3|405405|405405|0|
|21|2|270270|270270|0|
|25|20|2702700|2702700|0|

The three independent checkers `verify_t15_alternative_core*_c1_residual.cpp` regenerate every original required matching, compare all thirteen required edges to the saved record, and verify thirty distinct cycle vertices, exact omitted pair, containment of all required edges, shortness of all other edges including the closing edge, exact record counts, and absence of trailing data. All three report PASS. Each binary record has26 required-edge endpoint bytes and30 cycle vertex bytes.

These certificates use the isomorphic labels $2a+1$ on A and $2b$ on B. They omit $2x+1$ and $2y$ respectively. This is a common coordinate insertion, preserving every local short adjacency and every short cross-face bridge; transport back through the explicit original cut and coordinate permutation yields exactly the marked global omissions in the Claim.

The search caps have no logical role: every residual input has a checked positive witness, and none is omitted or classified negative by timeout.

The possible crossing counts are $1,3,5,7,9,11,13$. Steps2--5 exhaust them in all three geometries. Step1 preserves every original edge and produces exactly the required support. The claim follows.

## Corrections or missing assumptions

No narrowing of the three-core claim is made. The perfect-matching and table imports must retain their arbitrary complete-graph scope. Only the inverse B certificate is transported from core23; the entire marked core23 geometry is not asserted isomorphic to core25.

## Open risks and reproducibility

- Fresh-context semantic audit remains pending.
- Global eight-hole coverage and whether these cores replace core26 must be checked separately.
- Compile each C++ source with `g++ -O3 -std=c++17` and run from `research/six_directions`, where the imported tables are located.
- New verification reports are `t15_alternative_small_verification.json`, `t15_alternative_core25_blockers_verification.json`, and the three `t15_alternative_core*_c1_residual_verification.json` files.
- The earlier core4 zero-crossing proof package is preserved separately; no assertion about full core4 is made here.
