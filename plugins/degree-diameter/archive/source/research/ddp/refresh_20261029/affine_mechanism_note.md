# One D3 rule: complementary projective triples at q=5

Status: mathematical proposal and source reading only, 2026-10-29. No new finite-field enumeration, words, solver, graph generation, or BFS has run. This is not a new-record claim.

The concrete rule is to reuse the actual 30-vertex controller of the published (16,3)1920 graph, replacing its F4^3 fibers with F5^3 and choosing edge maps by complementary triples in PG(1,5). This predicts an explicit 20-regular diameter-3 graph of order 3750. Whether it improves the published (20,3) bound is still unbound: the current Comellas main table actually ends at degree16. Do not generate a full graph or call this a record until a primary comparison for degree20 is obtained.

## Bound source and old boundaries

Read local source files in research/ddp/breadth_20261027_wave4/mizuno_d3_source/:
construction.json, PROOF_ja.md, controller_structure.json, local_check.json, README.md, and the corresponding sole-Wiki experiment ddp-wave4-mizuno-d3-source.

The actual controller is simple quartic, order30, with inverse ports (1,0,3,2). There are ten disjoint triangles and an external factor of six C5s. The source's existing certificate provides all ordered controller pairs: 780 full-rank routes and 120 adjacent pencils. Its cached NB3 data say that every nonadjacent pair, including each equal pair, has a three-step nonbacktracking route. Missing NB3 slots are precisely the 120 directed adjacent pairs.

The source rule is (u,x) adjacent to (v,T_e x + lambda*l_q), with
l0=(1,0,0), l1=(0,1,0), l2=(0,0,1), l3=(1,1,1);
T_e*l_p=l_q, T_reverse=T_e^-1. Maps belong to individual directed edges, not merely four common label matrices. Do not reduce the source to four global maps without an explicit replacement argument.

The old F3 followup found 18 local patterns per port, each with two bad turns, but did not solve a global F3 certificate. The complete 2760 specific 31-controller triangle/C5 insertions all failed their required NB3 gate; old fixed31 joint, 32/33 skeleton and random profiles do not close arbitrary controllers. None is repeated here.

HS850 six-parameter fixed branch template is rigorously capacity-blocked (12 endpoints for a 17-point target). Its 26-parameter/ten-orbit relaxation raised thin formal capacity to18 but only received one finite heuristic batch; it remains open. This proposal does not reuse its parameters, topology, branch pattern, or old score optimization.

## Exact complement calculation

For a directed controller edge e:u->v with departure port p and reverse port q, project the other three l_i through the quotient V/<l_p> at the source and V/<l_q> at the target. Each gives three distinct points of a projective line.

At q=4, the line has five points; the source proof chooses the two triples to intersect in one point. Thus eight of the nine nonbacktracking turns are full-rank and one is not.

At q=5, the line has six points. A projectivity can send the source triple exactly onto the complement of the target triple: PGL(2,5) maps any ordered triple of distinct points to any other. Lift that quotient map to an invertible T_e with T_e*l_p=l_q. Then the two triples are disjoint.

Consequences for this fixed q=5 rule:

1. For every i!=p and j!=q, the three columns [T_e*l_i,l_q,l_j] are independent. All nine turns are full-rank, so every three-step nonbacktracking controller route covers the entire target F5^3, for every source coordinate.
2. The three pre-backtrack planes and the three post-backtrack planes have a common line and give all six projective directions. Their union has 6*(25-5)+5=125 points, so each adjacent fiber pair is fully covered in at most3.
3. Reversing e uses T_e^-1. Disjointness of the triples is preserved by inversion, so the reversed edge also satisfies both claims.
4. Consequently the constraints are simultaneously realizable edge by edge: choose one suitable T for each undirected edge, put its actual inverse on the reverse dart. There is no representation/holonomy condition requiring products around controller cycles to be identity. The central-edge rank criterion already factors out the arbitrary first/last invertible maps.

A literal port0->port1 example over F5 is

    T = [[0,2,4],
         [1,0,0],
         [0,1,3]].

It maps l0 to l1. In the target quotient basis (e1,e3), images of the other source directions have slopes 2,3,4; the target directions have slopes infinity,0,1. Determinant is3 mod5. The quotient 2x2 matrix is [[2,4],[1,3]], with determinant2.

All four frame points can be permuted by projective coordinate changes. Rescale representatives when necessary; the line relation only depends on their spans. This gives the remaining port types. Alternatively, choose the lexicographically first suitable invertible matrix for each of the two inverse port pairs, with the reverse matrix set to its inverse; do not independently choose reverse maps.

Because all nonadjacent/equal controller pairs already have an NB3 route, and adjacent pairs have the six-plane pencil, this would prove D<=3 for all3750 vertices. Simplicity and degree20 follow from a simple quartic controller and five distinct points per neighboring fiber. The Moore bound for diameter2 is401<3750, giving exactD3.

This is a sufficient construction, not a necessary characterization. In particular, q4/q3 failures of a chosen full-rank-route certificate do not exclude multi-route affine unions, and the old controller capacity exclusions retain their original scopes.

## Proposed finite test and stop

Before any full graph, freeze the following explicit prediction: four port types admit inverse-consistent F5 edge maps with all nine turn ranks3 and all six adjacent pencil planes union125.

One short deterministic test can check the displayed matrix, construct the remaining port types, and check the two conditions for each. Reuse the old controller's cached nonadjacent NB3 coverage; no old source BFS is needed. This is a matrix/pencil test with no controller or voltage search.

Only if a primary degree20/D3 bound is confirmed below3750 should the full3750 graph be generated and verified. If a known bound is >=3750, stop this transfer as a non-record mathematical control; do not automatically change q or increase the controller. A claim of a record cannot be based on the absent degree20 table cell.

## Source reading and novelty limit

Freshly read:
- Comellas main table, https://web.mat.upc.edu/francesc.comellas/delta-d/table_degree_diameter.html : its listed degree range is3..16; no degree20 comparison was supplied.
- Author's actual proof, https://raw.githubusercontent.com/rmizuno42/ddp/main/results/degree16-diameter3/certificate/PROOF_ja.md : a specific F4 construction, local-pencil mechanism, and source data; it does not state an arbitrary-q 30q^3/4q theorem or establish novelty of pencils/edge-local lifts.
- The author explicitly does not claim larger controllers or all global/edge-local alternatives impossible.

No primary (20,3) lower bound was obtained in this bounded read. A direct CombinatoricsWiki fetch did not return its contents; that is an unfilled source gap, not evidence of no stronger construction. No novelty claim or full-field sweep follows.

## Followup requested by root: one bounded 33-controller rule (unexecuted)

The old 33-point experiment fixed eleven disjoint K3s and allowed an otherwise arbitrary external2factor. It sampled eight Hamilton initial factors, then800000 external2switch proposals (606948 exact scores). The entire factor family was not excluded. Its old objective was the F3 raw endpoint-capacity sum I+3A+9A2+27A3, not a jointly realized F4 one-exception-per-edge certificate.

The one new concrete rule is a parallel-triangle insertion into the actual30-point source:

1. Choose one of the ten old triangles {v0,v1,v2}.
2. For each vi choose one of its two external C5 neighbors ri. These three selected edges belong to three distinct old C5s, by the saved source incidence design.
3. Delete vi-ri for all three i. Add three new vertices wi forming a triangle, and add vi-wi and wi-ri.
4. Keep every other source controller edge.

This gives exactly33 vertices and66 edges, all degree4. The old ten disjoint triangles remain and the wi form the eleventh. Exactly three old external C5s become C6s, the other three remain C5s. There are exactly10*2^3=80 literal parameter settings before any duplicate accounting.

This is different from the old2760 n31 constructions, which moved two old vertices from different triangles/five-cycles into a new overlapping triangle and subdivided one remaining cycle edge. The old33 random profile could in principle have visited individual isomorphic examples, but its finite failure did not exclude this explicit80-setting rule; no record of those full old trajectories is treated as a complete domain exclusion.

The proposed falsifiable first question is only: does at least one of these80 controllers have an NB3 route for every nonadjacent/equal ordered pair? A zero slot rejects that controller before any field lift. If all80 fail, stop this rule. If any pass, the next unresolved question is the F4 assignment of one exceptional turn per edge that leaves every required pair a good route; raw NB3 positivity alone is not a diameter certificate. There is no automatic preservation theorem for old-old D3 after the three cuts.

The F4 count leaves room but does not prove existence: good turns total32n, while required nonadjacent/equal ordered pairs totaln(n-4); for n33 these are1056 and957, slack99. The F3 count28n forcing n<=31 does not apply to this F4 target2112/degree16. A future candidate still needs its actual local matrices, complete route certificate and final graph check.

This is a small design-derived new structural rule, not an instruction to restart SA. No33 controller generation or scoring has run here. Its chance of passing is unknown; if this limited structural basis is insufficient, the honest state is that no explicit33 passer has been obtained.
