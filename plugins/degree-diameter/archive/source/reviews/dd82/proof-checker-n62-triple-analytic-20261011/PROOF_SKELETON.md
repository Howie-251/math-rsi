# Proof skeleton: analytic triple-repeat exclusion

Review date: 2026-10-11. Fresh reviewer: `/root/proof_review_n62_triple_analytic`.
Scope: the full paper proof of triple-repeat exclusion, including recovered Steps 1–3 and the actual quotient-trace import. Same-family review; acceptance is provisional.

## Quantified claim and symbols

For every finite simple undirected graph G with |V(G)|=62, maximum degree at most 8 and diameter at most 2, the actual integer matrix B=A²+A−7I−J satisfies Bxy≤2 for all distinct x,y. No repeat-support connectedness or entry bound B≤2 is assumed.

A is original 0–1 adjacency; B is the actual symmetric repeat matrix; S,E,U,V are the five-cell reduction's disjoint subsets (the local symbol V denotes a 24-point cell); N is a 4×4 nonnegative integral block; L=A[V] and Q=B[V] are 24×24 matrices. The symbol c is the number of actual positive-support components and R is their original-adjacency quotient, not the coarser five-cell quotient also called R in the imported source.

## Dependency DAG and obligations

Original graph → MC01–MC02 → MC03–MC07 → MC08–MC10 → MC11–MC13 → MC15.
Original graph → MC14 → MC15. There is no edge from triple-repeat exclusion back into MC14.

| ID | Sequent / rule | Source and discharge |
|---|---|---|
| MC01 | Original hypotheses imply 8-regularity, B≥0, diagonal 0, row sum 3, AB=BA and the point-pair identity. | Recovered Step 1; radius-two bound 57 if degree≤7, regular adjacency commutes with J. |
| MC02 | MC01 implies 2t(x)=sum over original neighbors of Bxy≤3, so t(x)≤1 and adjacent repeats≤1; B-harmonic vectors are constant along positive edges. | Recovered Step 1; triangle double count and finite nonnegative energy identity. |
| MC03 | Buv=3 implies a closed two-point component, u,v nonadjacent and triangle-free; S has size 4 and is a closed K4 repeat component. | Recovered Step 2; row saturation, common neighbors and independence of N(u), N(v). |
| MC04 | E± each have size 4 and their original cross-edges are a perfect matching; U has 24 distinct vertices and V has the remaining 24. | Recovered Step 2; each pair in S has exactly two common neighbors. |
| MC05 | The five cells are B-closed; B on E is bipartite. | Recovered Step 2; harmonic f=A(eu+ev), h=A1S distinguish all cells; g=A(eu−ev) has eigenvalue −3. |
| MC06 | U has original degrees 1 into S, 3 into U, 4 into V; V has 2 into E, 4 into U, 2 into V; E has 6 into V. | Recovered Step 2; pair counts with u,v and each s∈S, followed by degree 8. |
| MC07 | N is symmetric, zero-diagonal, row sum 3, with opposite entries equal; its weights are 300,210,111 up to relabeling. | Recovered Step 3; E,E commutation, Npp=2t(e+p)≤1, and S4 permuting the three opposite pairs. |
| MC08 | |Vpq|=1+Npq−δpq; Vpp is empty; L-neighbors of pq have types rs and sr for complementary labels r,s. | Recovered Step 3; all common neighbors of e+p,e−q lie in V, then pair counts for z,e±r. |
| MC09 | Q has first marginal Nrq and second marginal Nsp; L and Q have disjoint positive supports. | Recovered Step 3; actual E,V block of AB=BA; L is bipartite on each complementary block and no original triangle crosses B-closed cells. |
| MC10 | N300 and N210 are impossible. | Recovered Step 3; forced Q mass on unique forced L-neighbors. |
| MC11 | N111 implies two points of each ordered type; their shared two E parents force Q-twin weight 1. | New §§2–3; common-neighbor lower bound and integral unit marginal upper bound. |
| MC12 | The other two Q-neighbors have complementary ordered types, making exactly three closed connected eight-point components Wi. | New §3; twin saturates first p/second q; equal-label types are absent; twin fibers connected and contracted type graph K2,2 connected. |
| MC13 | Each Wi has original internal degree 2, hence tr(R)≥6; the pair, S and nonempty remaining 32 vertices imply c≥6. | New §§3–4; actual component status from MC12 and nonnegative quotient diagonals. |
| MC14 | Original hypotheses imply the actual-component trace identity c+2tr(R)=17. | Actual formal theorem and definitions inspected; harmonic equitability, quotient quadratic, size actions and integral trace argument. No B≤2 premise. |
| MC15 | MC13 and MC14 imply 17≥18, eliminating Buv=3 and hence proving all distinct entries≤2. | New §4; integer nonnegative row sum 3 gives the initial upper bound 3. |

All assumptions at each application are discharged above. There are no limits, asymptotic estimates, probabilistic modes or interchange obligations in this finite argument.
