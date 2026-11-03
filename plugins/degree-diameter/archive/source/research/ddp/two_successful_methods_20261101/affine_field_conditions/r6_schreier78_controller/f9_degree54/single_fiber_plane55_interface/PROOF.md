# One explicit transverse plane gives81 disjoint original neighborhoods

This is a finite interface for the already accepted concrete54-regular56862-vertex F9/C78 graph. It does not construct a new full graph, certify public novelty, or complete a new Lean instance. Its exact ordered centers and4374 proposed old pins are in `PARAMETERS.json`, `CENTER_SEQUENCE.csv`, and `PINS.csv`. No source edge file or BFS was read or run.

## The problem and falsifiable prediction

For full-neighborhood cloning at cap55, the54-regular old graph allows each old pin to be used at most once. The specific question was whether a large set of centers in a single controller fiber can have pairwise disjoint immutable full neighborhoods. The prediction in `PRED.md` was that an explicit81-point plane avoids all six port directions and hence partitions each neighboring fiber into the required nine-point lines. This tests a concrete expansion rule, rather than continuing the previous controller search or reducing bad-pair counts.

## Actual plane and ordered centers

Work in F9=F3[w]/(w²+1), with code a+3b representing a+bw. The square set is exactly `{0,1,2,3,6}`; eta=4 represents1+w and is a nonsquare. Put

    W={(a,b,eta*a): a,b∈F9}, n=(-eta,0,1)=(8,0,1).

Then W is the kernel of x↦n·x and has81 elements. For the six actual directions

    (0,0,1), (1,0,0), (1,1,1), (1,2,1), (1,3,2), (1,6,2),

the n-pairings are respectively `(1,8,6,6,7,7)`, all nonzero. This also follows from n·(1,t,t²)=t²−eta and n·ell_infinity=1. Therefore W meets each port line F9*ell_p only at0.

Choose only controller fiber0. The ordered center with j=9a+b is

    c_j=(0,(a,b,GF9mul(4,a))), a=0..8 outer, b=0..8 inner.

Its original source label is `a+9*b+81*GF9mul(4,a)`. The proposed clone label, in a future separate generation scope, would be56862+j. The sequence is not sorted by the numerical old labels; the stated (a,b) order is the literal recipe.

## Why the full neighborhoods are disjoint

Let x,y be coordinates in the same controller fiber0. Over source port p, write v=controller[0][p], q=reverse(p), and T for the actual source dart matrix. The old neighbors of (0,x) in controller fiber v form the affine line

    T*x+F9*ell_q.

The source controller has six distinct neighbors `[2,24,26,52,31,62]`, so two neighborhoods can intersect only in corresponding port layers. Since T is invertible and T*ell_p=ell_q, the two affine lines for x,y intersect if and only if

    T*(x−y)∈F9*ell_q, equivalently x−y∈F9*ell_p.

If x,y are distinct elements of W, their nonzero difference lies in W and cannot lie in any of the six port lines. Thus their complete54-neighborhoods are disjoint. At each of the six neighboring controller fibers, the81 lines each have9 points and are pairwise disjoint, so they partition all729 old coordinates in that fiber.

The actual finite check uses only the declared original source parameters, with a separately implemented GF9 arithmetic. It checks the actual six source darts and their reverse matrices, all81 full54-neighborhoods, all3240 center pairs, and every proposed pin. The4374 pin occurrences are4374 distinct old vertices, exactly729 in each of the six specified target fibers. Every predicted property was supported.

## Every prefix has current full radius2 pin coverage

Let G denote the immutable accepted source, and suppose the earlier clones x_0,...,x_(i−1) have been added, with N(x_j)=N_G(c_j) and no new-new edges. Set S_i=N_G(c_i), of size54. We prove that the radius2 balls about S_i cover every vertex of this current graph, including the earlier clones.

For any old target y≠c_i, choose a shortest source walk from c_i to y. It has length at most3. Removing its first edge gives a walk of length at most2 from some member of S_i to y. For y=c_i, use any source neighbor in S_i and its incident source edge.

For an earlier clone x_j, the centers c_i,c_j are distinct and lie in the same controller fiber. They are not adjacent, because the source has no within-fiber edges; and they have no common neighbor by the packing proof. Their source distance is therefore exactly3. Choose a source path

    c_i — a — b — c_j.

Here a∈S_i and b∈N_G(c_j), so `a — b — x_j` is a current length2 walk from S_i to x_j. All its interior vertices are old source vertices. It uses neither future clones nor a hypothetical new-new edge.

Consequently every new clone can be added by the inherited retained-edge pin-cover lemma in the actual current graph. The same proof handles all prefixes and all final vertex pairs. This is stronger than checking only old-source coverage; it explicitly includes all earlier clones.

## Predicted complete extension, conditional on a separate production scope

All old source degrees are54. Distinct pin sets give old load at most1, while every new clone has54 old neighbors. Keeping the entire1535274-edge source and adding81 clones would therefore yield

    n=56862+81=56943,
    m=1535274+81*54=1539648,
    degree54:52569 vertices; degree55:4374 vertices,
    no new-new edges; diameter≤3.

For every prefix, 54*i previously used old pins are distinct; an unadded center's54 pins are unused and retain degree54. Thus each literal insertion respects cap55, not just the final graph. The source center vertices themselves remain unpinned, because they lie in controller fiber0 whereas all pins lie in neighboring fibers.

The exact diameter of such a fully generated extension would be3, because the cap55 radius2 bound is `1+55+55*54=3026<56943`. This does not claim that a new full edge file, independent validation, or Lean theorem already exists.

## Sharpness and limits

For any one fixed controller fiber and any chosen neighbor fiber, each full original neighborhood uses9 vertices in the729-point neighbor fiber. At cap55, the old54-regular vertices may receive at most one clone incidence. Therefore any full-neighborhood clone packing whose centers all lie in this one controller fiber has at most729/9=81 centers. The explicit W packing reaches that single-fiber bound.

This is not a global packing optimum for the56862-vertex source, a bound for arbitrary pin sets, or an upper bound on N(55,3). It does not authorize multiple fiber searches, new controller/field ladders, or repeated copies. The actual plane is a standard linear transversal condition used with the inherited full-neighborhood clone mechanism, not a new general framework. The next decision belongs to the root's separate public55 gate; no complete extension is generated here.

## Execution

`run_precheck.py` completed successfully in0.061380544CPU seconds, one worker, below15CPU. The measurement includes imports, parameter read, finite checks and CSV/JSON writes. There was no compiler, complete graph generation, source edge-file read, BFS, Lean, solver, installation or hashing. `TERMINAL.json` records all processes terminal. The source graph's accepted D3 and exact formula are inherited; they were not rerun.
