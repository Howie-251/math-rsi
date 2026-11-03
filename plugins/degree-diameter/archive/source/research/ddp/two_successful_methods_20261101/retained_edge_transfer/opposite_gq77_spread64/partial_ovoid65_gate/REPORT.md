<!-- PUBLIC_W3F7_33_SUPERSEDES_TALLINI15_20261101 -->
> **当前公开比较已更正（2026-11-01）**：[原始33点证据与修订](../../../public_baseline_audit/W3_F7_PUBLIC_PARTIAL_OVOID_THRESHOLD25_20261101.md)实际读到Cimráková–Fack2007 p140 Table5的W(7)33点，公开一般复制保证65:161650／70:169900／77:181450。本地161150／166650分别少500／3250，条件175692少5758；图合法性与具体Lean/A/B/C不变。下文15点基线和正优势是保留历史，已被此处覆盖；不是独立公开数值边表／全球维护表。

# Ten-point partial-ovoid gate: finite PASS, public comparison STOP

This asks one new connection question: after the accepted 160050-vertex,
64-regular spread augmentation, can a partial ovoid replace the complete
ovoid used at q=4, and support one immutable full source-neighborhood clone
at each point × spread-line center when the degree cap becomes 65?
`PRED.json` was saved before the numerical check and public browsing. Only
the ten specified points were checked. No target graph was generated.

The actual `OvoidSpreadCloneCapacity.load_le_one` statement requires each
GQ line to contain at most one indexed chosen point, and each point to lie
on at most one indexed spread line. It does not require every GQ line to
meet the point set. Its proof also makes no assumption that centers are
independent. The complete-ovoid name therefore does not prevent using a
partial ovoid.

For the fixed source coordinates `(u0,u1,v0,v1)`, put

    B(x,y) = x0*y2 + 3*x1*y3 - x2*y0 - 3*x3*y1  (mod 7).

The frozen source uses `2B`, which has the same zero relation. The proposed
points are `p_t=(1,t,t^3,-t^2)` for t=0,...,6,
`p_inf=(0,0,1,0)`, `a=(1,0,6,4)`, and `b=(1,0,1,4)`.
Their frozen point IDs are

    57,119,165,251,265,347,399,1,103,68.

The prediction could fail if two points were collinear, if a source line
contained two chosen points, or if the bonus-neighbor substitutions caused
two product centers to load the same source vertex. The actual finite check
found none of these failures. All 45 distinct pairs have nonzero B; all 400
line intersections have sizes 0 or 1, with histogram 320/80. The polynomial
identity `B(p_s,p_t)=(t-s)^3` passed at all 49 ordered parameter pairs.
The two extra polynomials are `6+5t-t^3` and `1+5t-t^3`; their seven values
are respectively `6,3,1,1,4,4,2` and `1,5,3,3,6,6,4`, so neither vanishes.
Also `B(a,b)=2` and `B(p_t,p_inf)=1`.

For an original product center `(p,l)`, its raw neighbors are all
`(q,m)` with `q` on l and m through p. There are 64 raw pairs. A flag center
has one raw self-pair, which is removed; its actual source neighborhood
instead contains bonus vertex `160000+owner(p)`. A nonflag center retains
all 64 old neighbors. The checker equated the JSON geometry arrays to every
entry of the frozen production `TABLES_INPUT.txt`, and checked the actual
50 extension-step pin lists against the geometry and original spread order.
Thus the ten flag substitutions refer to the accepted source's actual bonus
vertices. Their original spread indices are

    0,12,41,33,30,36,9,49,34,29.

All 500 distinct point × spread centers have source degree 64. The checker
compared all 124750 pairs of their immutable source neighborhoods and found
every intersection empty. Their union contains 32000 source vertices:
31990 original vertices and ten bonus vertices. Maximum source load is 1.
The center-induced subgraph has 45 K2 components and 410 isolated vertices;
copying evolving neighborhoods would be a different construction.
`PRECHECK_RESULT.json` records all ten actual bonus bridges, the B matrix
and counts; `CENTERS.json` records the complete center list; `precheck.py`
is the deterministic finite check. It ran once with a 30 CPU-second limit,
one worker, and measured 0.177169576 CPU seconds. It did not read the source
edge file or run BFS, Lean, a solver, an install, or a hash operation.

The local prediction therefore passes: retaining the accepted source and
adding 500 clones connected only to the 64 original source neighbors would
give 160550 vertices, 5153600 edges, maximum degree 65, and degree histogram
`64:128550,65:32000`. The existing full-neighborhood clone theorem would
preserve diameter at most 3; order greater than `1+65+65^2=4291` would make
it exactly 3. These remain conditional graph parameters, not a produced,
independently accepted or concretely formalized graph.

The public comparison stops this ten-point rule. The introduction of
[Ceria, De Beule, Pavese and Smaldore, arXiv:2203.04553, §1](https://arxiv.org/html/2203.04553#S1)
explicitly records Tallini's construction of a maximal partial ovoid of
W(3,q), for odd q, with 2q+1 points. In particular q=7 supplies a published
15-point construction. Its reference [13] is G. Tallini, *Fibrations through
lines in a nonsingular quadric Q4,q of PG(4,q)*, Atti Accad. Peloritana
66 (1988), 127–146 (1989). The Tallini original, its explicit recipe and
coordinates were not obtained in this bounded review; the available evidence
is the later primary research paper's explicit account of that construction.
The latter paper's new odd-square construction does not apply to q=7.
Within the same paper's §1, Table 1 and §3.1, no construction larger than
15 applicable to W(3,7) was located. The odd-exponent row records 2q+1;
the quantity q^2-q+1=43 is an upper bound, not a 43-point construction.
The explicit coordinate and orbit recipe in §3.1 and Theorem 3.3 requires
an odd square q. A partial spread of W(3,q), which dualizes to a partial
ovoid of Q(4,q), cannot be substituted for a partial ovoid of W(3,q).
These are statements about the inspected paper, not a classification of
all published constructions.

The classical opposite-GQ formula in
[arXiv:2608.27253v2, §3.4.2](https://arxiv.org/html/2608.27253v2#S3.SS4.SSS2)
gives order 160000, maximum degree 64 and diameter at most 3 for q=7.
[Delorme, *Grands Graphes*, EJC6 (1985), §8(a), p298](https://web.mat.upc.edu/francesc.comellas/old-files/delta-d/papers/81981341.pdf)
provides the 50-line symplectic spread. His general induced-subgraph
duplication theorem in §7, p297 applies with
`A0=O15 × spread50` and `A1=empty`. Condition (a) is vacuous. For condition
(b), an outside product vertex can be adjacent to at most one center:
its line contains at most one partial-ovoid point, and its point lies on
exactly one spread line. The theorem requires at most one, not exactly one.

For condition (c), no spread line contains two of the 15 points. A center
can therefore have at most one distinct center neighbor. The induced graph
has 105 K2 components and 540 isolated centers. Each component has a source
neighbor outside A0, since the source minimum degree is 63 and the induced
degree is at most 1. For a K2 choose such a neighbor z of one endpoint: the
two endpoint distances to z are at most 1 and 2, with sum at most 3.
For an isolated center the repeated-endpoint distance sum is 2. These verify
the diameter-three condition. Delorme's theorem consequently gives

    N(65,3) >= 160000 + 15*50 = 160750 > 160550.

This is a direct mathematical guarantee inferred from published construction
statements and a published theorem. It uses the classical source throughout
and does not depend on the project's 160050-vertex source. No separately
published 160750 numerical graph or edge table was located. This comparison
is sufficient to stop the fixed ten-point rule; it is not a claim that
160750 is globally best or that no larger partial ovoid is known.

The next meaningful choice belongs to root. The published 15-point object
can inherit the same partial-ovoid interface abstractly, but a local
coordinate recipe has not yet been retrieved or bound. Recovering a
published witness would be a new bounded task. This task does not select a
larger seed, search for points, instantiate the 15-point case, generate a
graph, or start another field/degree branch. The accepted graph counts,
concrete Lean counts and public-record counts do not change.
