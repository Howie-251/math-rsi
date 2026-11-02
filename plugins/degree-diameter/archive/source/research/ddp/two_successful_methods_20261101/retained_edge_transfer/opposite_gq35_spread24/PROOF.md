# GF4 opposite-GQ spread augmentation: literal6160 graph

This is one fixed GF4 construction and one fixed vertical spread. Public inheritance and current record status are being checked separately. A successful local construction is not evidence of novelty.

## Literal incidence structure

Use GF4=F2[w]/(w^2+w+1), represented by0,1,2=w,3=w+1. Addition is binary XOR. Encode a point(a,b,c) as a+4b+16c. The64 points are GF4^3. Vertical line i=b+4c consists of(a,b,c) for all foura.

For every point p=(a,b,c) and projective direction(d1,d2) in{(1,t):t inGF4} union{(0,1)}, form

    {p+t*(b*d2+c*d1,d1,d2):t inGF4}.

Deduplicate these literal four-point sets. The generating direction is constant along the line: replacing(b,c) by(b+t*d1,c+t*d2) changes its first component by t*(d1*d2+d2*d1)=0 in characteristic2. The actual finite checks find80 distinct ordinary lines and16 vertical lines, all96 distinct and each of size4. Every point lies on six lines, and any two distinct points are on at most one line. For each of5760 nonincident point-line pairs(p,l), exactly one point of l is collinear with p. Thus the explicit data satisfy the full GQ(3,5) incidence axioms. The16 vertical lines partition all64 points.

PARAMETERS.json lists every point, line, generating anchor/direction, and point-line incidence. GQ_AXIOM_CHECK.json records the finite counts and checked axioms. No assumption about an external labeling is needed for this literal graph.

## Old opposite graph

An old vertex is(p,l), encoded96p+l. Distinct vertices(p,l),(q,m) are adjacent exactly when p lies on m and q lies on l. A vertex has4*6=24 raw neighbors, one for each q on l and m through p. These pairs are distinct. A loop appears exactly for a flag p on l, and removing it gives degree23; all nonflags have degree24. There are64*6=384 flags and5760 nonflags, so the old graph has6144 vertices and73536 edges. Direct complete adjacency checks confirm simplicity, symmetry, all degrees, and precisely those384 degree23 flags.

The GQ axiom gives diameter at most3 without an old-source all-roots BFS. Given u=(p,l) and v=(q,m), choose a on l collinear with q, and b on m collinear with p. When the point is already on the line, choose that point and any through-point line as needed. Let k contain a,q and n contain b,p. Then

    (p,l), (a,n), (b,k), (q,m)

is an adjacency walk, except that consecutive equal vertices may be suppressed. The three incidence conditions follow directly from the choices. Therefore all old-old distances are at most3. Since6144 exceeds the degree24 diameter2 Moore bound1+24+24*23=577, its diameter is exactly3.

## Sixteen full pin sets

For each vertical spread line li, add new vertex vi with

    S_i={(a,b):a on li and a on b}.

Each S_i has4*6=24 flags. The16 S_i partition all384 old flags; every old degree23 vertex is used once, and every nonflag is unused. Adding all16 vertices therefore makes all6160 vertices degree24 and adds384 edges, yielding73920 edges. All73536 old edges are retained.

For an arbitrary old target(p,l), select a on li collinear with p. Choose n through a,p. Choose a line b through a meeting l, and q in b intersect l; such a b exists by the GQ axiom, including the trivial case a on l. Then flag(a,b) lies in S_i and

    (a,b), (q,n), (p,l)

is a length-at-most2 walk after suppressing consecutive repeats. Thus the full pins S_i have radius2 coverage of every old target. Hence vi is within3 of every old vertex.

For two distinct spread lines li,lj, pick a on li and choose c on lj collinear with a. Since the spread lines are disjoint, a differs from c. Let b be their joining line. Flags(a,b) and(c,b) are distinct and adjacent in the old graph. They belong to S_i and S_j respectively, giving

    vi, (a,b), (c,b), vj

of length3. This covers every new-new pair. Old-old distances stay at most3 because old edges are retained. The candidate therefore has diameter at most3, and6160>577 makes it exactly3.

## Actual dynamic construction checks

Before each vi insertion, the producer independently expands a multi-source radius2 ball from all24 pins over the complete current adjacency, including every previously inserted new vertex. All16 checks covered every current vertex: sizes6144 through6159, zero uncovered targets. Every pin degree was exactly23 before use, and the whole current degree cap remained24 after insertion. EXTENSION_STEPS.json saves all pins and distance histograms, not only the paper prediction.

The final unique graph_d24_D3_n6160.edges has header6160 73920 and every unordered edge once. The producer verified final simplicity, reciprocity,24regularity, preservation of every old edge, and a single ordinary connectivity BFS from final root0 covering all6160 vertices. No old-source or candidate all-roots BFS was run here; root is arranging the independent candidate check.

Construction CPU0.195456125 seconds, one worker, zero solver calls. No alternate spread, field family, seed search, installation, Lean step, or hash was used. Independent candidate acceptance and public inheritance/record status remain separate pending items. This graph is not yet claimed as a new public record.
