# Canonical GQ8 circle-pole C3 graph:3705 vertices, exactD5

The sole frozen graph is simple and undirected, with3705 vertices19500 edges and maximum degree11. Its1755 point vertices have degree10, and the1950 line/twin vertices have degree11. The first actual root0 has19 points outside radius4; the first target is220. A universal upper5 follows from the base generalized-quadrangle paths and the line/twin triangles. Thus this graph has **exact diameter5**, not the target4. It gives no new lower bound over the saved(11,4) baseline3645. Only one graph and one actual root were tested.

## Predictions and exact field

The original prediction of a balanced3/3/3 histogram on the nine pure four-step geodesics between canonical opposite spread lines was retained in PREDICTION.json. Before any phase numeric run, the parent supplied a refined paper prediction2/3/4; this is separately recorded in PRE_RUN_DERIVATION.json. The actual histogram is **[2,3,4]**. Thus the original balanced prediction is refuted and the pre-run refinement supported. All three colors occur, so the frozen gate required constructing the graph. The weaker prediction that the complete graph hasD4 is refuted.

PAPER_PRECHECK_ROOT.md preserves the parent's full pre-numeric derivation. The ordinary circle classes choose outside point t0=1 and contribute2/3/3 after the exceptional class is removed; the exceptional class chooses t0=2 and contributes character2. This changes the predicted observation, not the candidate or selection rule.

The specified field is F64=F2[t]/(t6+t+1), t encoded2, with fixed F8 basis1,j=t. The preliminary field check confirms irreducibility and primitive order63: t63=1,t21=59,t9=24, and Rabin gcd checks for t4+t and t8+t are1. The embedded F8 is exactly0,1,14,15,22,23,24,25. No field, basis or seed was changed.

## Complete deterministic recipe

V=F64² is four-dimensional over F8, with coordinates x=a+bj,y=c+dj. Point representatives are normalized by the first nonzero coefficient of(a,b,c,d) and ordered lexicographically. The native program enumerates all585 points,585 isotropic9-point lines for B=Tr64/8(det), and65 Desarguesian spread lines. The full coordinates, flags, poles and incidence voltages are literal in GEOMETRY.json. Every point has9 flags.

For a finite spread label the pole is(0,1); for the infinity spread it is(1,0). A nonspread line has9 distinct complex slopes. If its circle avoids infinity, the unique center c makes Norm(t+c) a common nonzero element ofF8 and the pole is(1,c). If it contains infinity, choose the smallest numeric outside slope t0, transform by(x,y)->(y+t0*x,x), find its unique finite center c and pull back the pole to(c,1+t0*c). There is no selection based on coverage. All flag determinants are nonzero, and chi(det)=log_t(det)mod3 is invariant under all7 nonzero F8 scalings. The program checks these conditions explicitly.

For every flag add P(p,s)-L(l,s+tau(p,l)). Every3-vertex line fiber isK3. For each spread line, add three twins with exactly its matched point-copy neighbors, and make those twinsK3. There is no point matching. Point IDs are3*p+s; line IDs1755+3*l+s; twin IDs3510+3*spreadlabel+s. This gives all19500 edges and the degree counts above.

The pure opposite-line routes are S0-P-M-Q-Sinfinity, with total phase -tau(P,S0)+tau(P,M)-tau(Q,M)+tau(Q,Sinfinity). The nine literal routes are in PHASE_PREFLIGHT.json. Three-color coverage for this line pair is necessary but does not guarantee all point-pair coverage.

## Exact failure and stopping scope

The complete actual radius4 traversal from vertex0 has layers[1,10,92,786,2797] as recorded in RESULT.json. FIRST_FAILURE.json contains all19 missing vertices and their types: all are point vertices. The first source is point0/sheet0, with F8 coordinates(0,0,0,1), F64 pair(0,2). The first missing target is point73/sheet1, coordinates(1,0,0,0), pair(1,0).

To justify the global upper5, use a base GQ incidence path: point-point and line-line distances are≤4, point-line distances≤3. One extra step inside a line fiber triangle can adjust any required sheet discrepancy. Twin endpoint routes copy their corresponding spread-line point neighbors and have their own triangle for the same adjustment; coincident line/twin cases use a shared point. This covers every vertex-type pair within5. The actual radius4 failure supplies the matching lower bound. No ordinary unordered bad-pair count or all-root distance survey was performed.

Native geometry/phase/graph work consumed0.007247 CPU seconds under the10CPU hard limit; compilation and driver total1.394181 seconds. The phase preflight checkpoint was reached at0.006031 CPU seconds. No old-source BFS, additional pole, field, basis, phase variant or seed was run. The graph was constructed in memory; no positive edge file was exported. Reproduce the single rule with python run.py. This canonical-rule experiment is terminal and does not exclude other circle-pole constructions or generalN(11,4).

The expert's subsequent cached-only diagnostic also refutes one proposed repair rule, without a new graph or BFS. Missing targets include point73=(1,0) and point137=(3,0). A single point q=(0,y) on Sinfinity cannot be collinear with both: it would require y and3y to lie in F8*, implying3 lies in F8, which is false. Thus that single common-intermediate, one-matching-plus-two-incidence-plus-triangle pencil rule cannot cover even these two targets. This does not exclude other joint matching mechanisms; no repair graph was generated.

The expert paper checks and cached diagnostic are captured in CIRCLE_POLE_THEORY_REPORT.md and CIRCLE_POLE_THEORY_FIELDS.json and merged into the same producer row. They add no graph, BFS or independent method record.
