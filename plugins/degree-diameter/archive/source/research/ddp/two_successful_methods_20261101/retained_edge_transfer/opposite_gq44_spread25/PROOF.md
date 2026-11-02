# Fixed GF4 balanced-GQ spread extension: literal 7242 graph

This proof is for the one frozen incidence structure and one frozen spread listed in PARAMETERS.json. The source is the classical symplectic GQ(4,4) opposite product; this is another source/rule variant of the accepted retained-edge current-radius-2 mechanism, not a new independent framework. See [the limited public comparison](../../public_baseline_audit/DEGREE25_EXTENSION_20261101.md). Global-record status and priority of the augmentation are not certified.

## Literal fields, points, lines and spread

GF4 is F2[w]/(w^2+w+1), with codes 0,1,2=w,3=w+1. Addition is XOR. This is not arithmetic modulo 4. GF16 is GF4[beta]/(beta^2+beta+w); code a0+4*a1 means a0+a1*beta. Its product is

    (a0,a1)*(b0,b1)
      = (a0*b0 + w*a1*b1, a0*b1 + a1*b0 + a1*b1).

All additions and products on the right are in GF4. The polynomial has no GF4 root. The generated finite multiplication table passed field-law checks and inverses, beta^2=beta+w, and Trace_GF16/GF4(a)=a+a^4=a1 for all 16 elements. FIELD_TABLES.json contains both complete finite field tables and the relative trace table; prepare_geometry.py is the generator.

Write a GF4 vector as x=(u0,u1,v0,v1), interpreted as (u,v) in GF16^2. Projectivize all 255 nonzero vectors by scaling their first nonzero coordinate to 1. The 85 resulting tuples are sorted lexicographically and numbered 0..84. The form

    B((u,v),(u',v')) = Trace(u*v' + v*u')

is GF4 bilinear and alternating in characteristic 2. It is nondegenerate: for nonzero u one can choose v' so Trace(u*v') is nonzero; the analogous choice of u' works when v is nonzero. The implementation also checked its alternating property and zero radical on all 256 ambient vectors.

For every two distinct projective point IDs p<q with B(p,q)=0, form their full two-dimensional GF4 span, projectivize its nonzero vectors, and obtain its five point IDs. Deduplicate these five-point tuples and sort them lexicographically to define line IDs 0..84. Every line tuple has ascending point IDs. Each point's five incident line IDs are also ascending. PARAMETERS.json contains all literal point tuples, all line point tuples and generating pairs, and both incidence directions. The actual checks find 85 lines, five points per line, five lines per point, at most one joining line for two points, and at most one intersection for two lines. Collinearity of distinct points agrees exactly with B=0. For every one of the 6800 nonincident point-line pairs, exactly one point on the line is collinear with the external point. PROJECTION_WITNESSES.json saves the unique projected point and joining line for every such pair. These finite facts establish the full GQ(4,4) axioms for this literal incidence structure, independently of any published numbering.

For a in GF16, use the projective line from the GF4 subspace {(u,a*u):u in GF16}. Also use the infinity subspace {(0,v):v in GF16}. Each is totally isotropic because u*(a*u')+(a*u)*u'=0, with the infinity case immediate. Every projective point lies on exactly one such line: if u is nonzero, a=v/u is unique, and if u=0 the point belongs to infinity. The actual line membership and partition checks passed. In slope-code order a=0..15 followed by infinity, the frozen spread line IDs are

    21,26,31,36,57,54,67,64,77,82,71,76,49,46,43,40,0.

PARAMETERS.json records each slope, its five point IDs, and the unique point_spread_owner[p] index 0..16. No later sorting or relabeling was performed.

## Literal opposite source

An old vertex is (p,l), encoded 85*p+l. Distinct vertices (p,l),(q,m) are adjacent exactly when p is on m and q is on l. This cross-incidence relation is symmetric. There are five choices of q on l and five choices of m through p, giving 25 distinct raw neighbor pairs. A raw self-pair occurs exactly when p is on l. Removing it gives degree 24 at the 425 incident flags, and degree 25 at the 6800 nonflags. Thus the source has 7225 vertices and (425*24+6800*25)/2=90100 edges. Direct complete source adjacency checks confirm those numbers, simplicity and reciprocity, and that precisely the flags have degree 24; see SOURCE_CHECK.json. No source BFS was run.

Here is a source diameter bound using the literal GQ axioms. For old endpoints (p,l),(q,m), choose a on l collinear with q and b on m collinear with p. If the external point already lies on the respective line, choose that point. Choose a line k through a and q, and a line n through b and p; when the two selected points coincide, any line through that point suffices. Then the sequence

    (p,l), (a,n), (b,k), (q,m)

satisfies every cross-incidence condition. Suppress consecutive equal vertices to obtain a walk of length at most 3 in the loopless graph. Hence every old-old distance is at most 3. The source order 7225 exceeds the degree-25 diameter-2 Moore bound 1+25+25*24=626, so its diameter is exactly 3.

## The seventeen literal pin sets

For frozen spread index j and line L_j, add new vertex v_j with label 7225+j and pin set

    S_j = {(a,b): a is on L_j and a is on b}.

The exact pin order is the five ascending point IDs of L_j, followed for each point by its five ascending incident line IDs; EXTENSION_STEPS.json lists all 25 labels at every actual step. Each S_j consists of 25 flags. Since the 17 spread lines partition the points, the sets S_j partition the 425 old flags. Every old degree-24 vertex gains one edge, all nonflags remain degree 25, and each new vertex has degree 25. Thus the final graph has 7242 vertices and 90100+425=90525 edges, all degrees 25, and retains every old edge.

For an old target (p,l), select a on L_j collinear with p. If p is on L_j, use a=p. Choose n through a,p, taking any through-point line if a=p. Next choose a line b through a meeting l and let q be an intersection point: if a is on l, take b=l,q=a; otherwise use the unique projection of a onto l. Then (a,b) is a pin and

    (a,b), (q,n), (p,l)

satisfies both cross-incidence conditions. Suppressing consecutive repeats gives distance at most 2 from the pin set to this target. Therefore v_j is within 3 of every old vertex.

For two distinct spread lines L_i,L_j, pick a on L_i and project it onto L_j, obtaining c on L_j collinear with a. The lines are disjoint, so a and c are distinct; let b be their joining line. The distinct flags (a,b) and (c,b) are adjacent in the old graph, and the sequence

    v_i, (a,b), (c,b), v_j

has length 3. This proves every new-new distance is at most 3. Since old edges are retained, the old-old bound survives. The final graph has diameter at most 3; 7242>626 makes the diameter exactly 3.

## Actual finite construction and scope

The root release was saved before the one execution of generate_once.py. The producer read the frozen PARAMETERS.json literal tables rather than regenerating or changing the geometry. Before inserting each new vertex, it checked all 25 pin degrees were 24 and expanded the pin union to radius 2 in the complete current adjacency, including every earlier new vertex. Every one of the 17 checks covered all current vertices, of orders 7225 through 7241. Each distance histogram is exactly 25 at radius 0, 480 at radius 1, and 6720+j at radius 2. EXTENSION_STEPS.json stores every pin list, histogram, and earlier-new distance. The checks observed zero uncovered vertices and preserved the degree cap 25 at each step.

The unique complete graph_d25_D3_n7242.edges has header 7242 90525 and one ascending unordered edge per line, with the edge rows sorted lexicographically. The producer checked all final degrees, simplicity, reciprocity, exact retention of all 90100 old edges, and one ordinary final root-0 connectivity BFS covering 7242 vertices. It performed no source BFS, no source or candidate all-roots BFS, and no solver call. Production cost was 0.252167557 CPU seconds, one worker, within the 30-CPU-second budget. Prior geometry preparation cost was 0.050489278 CPU seconds, separately recorded.

The mathematical routes above and actual construction checks support the one candidate. Fresh independent literal acceptance, concrete Lean, and public comparison are separate tasks; this producer does not claim their completion. Public best located on 2026-11-01 is the classical 7225 formula, so the candidate has 17 more vertices than that located source. The limited comparison does not certify a global record or originality, and the old 7225 reproduction is not counted as another new graph.
