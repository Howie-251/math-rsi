# Literal16389 candidate: full-neighborhood D4 and every-prefix proof

This is the fixed published15552 source and the first savedI31, with no
source/plane/packing continuation. Production is complete; independent final
allroot acceptance is pending. No Lean theorem or world-record claim follows
from this producer receipt.

## Actual source and exact edge interface

The source is the cached Zenodo23691325 adjacency literal with15552 vertices,
116316 edges, degree14:648/15:14904, published diameter4. This batch reads that
literal once, generates no source, runs no parent BFS, field or rank checks,
and preserves every old simple edge. Its original virtualself entries had
already been deleted at equal old global labels. For each newclone, the code
copies exactly the corresponding literal row after its leading oldvertex ID.
It never compares a virtual relation output against the newclone label and
never adds clone--oldcenter.

The31 selected controllers and their actual five-target sets are fixed in
PARAMETERS.json, inherited from the sole FOUND31 search. Each gives27 original
centers81*a+x0+9*x2+27*x3, orderedx3,x2,x0. Newj=27*i+offsetindex has label
15552+j. ALL837_ROLE_BINDINGS.tsv lists allj/center/newlabel/degrees and each
complete frozenN, not just an edge count.

The inherited exact affine recipe and Q_v-normalized matrices give the
neighborhood-packing bridge. B has pivot row0 and v has pivot coordinate1,
so imB intersects span(v) trivially. A common target of two plane centers
forces their difference into kerB. The five actual input-kernel lines all
have nonzero second coordinate, hence kerB intersects W={x1=0} only at0.
Thus all27 centers within a block have disjoint completed neighborhoods;
deleting virtualself only shrinks them. The31 target-controller sets are
pairwise disjoint, so different blocks have disjoint oldpins too. This does
not assert that the centers themselves are independent.

Actual production copies36 degree14 centers and801 degree15 centers, so
added edges=36*14+801*15=12519 and totalm=128835. All116316 oldedges remain,
newnew=0, maxoldpinload1, n=15552+837=16389. Final degree histogram is
14:72,15:4410,16:11907. Strict lexicographic edgesa<b are written by increasing
oldu, first its larger oldneighbors, then its ascending newneighbors; there
are no newnew rows. The header is16389 128835.

## Genuine all-pair Walk bound, with old-only interiors

LetS be the original source. Let sigma collapse each clone to its original
center and fix every oldvertex. Every clone has exactly its sourcecenter's
fullsimpleN, so an old source edge fromsigma(s) to an oldvertexw lifts to
s--w, and similarly an edgew--sigma(t) lifts tow--t. All original oldedges
are retained.

For arbitraryfinals,t choose an actual source Walk fromsigma(s) tosigma(t)
of lengthL<=4, using the published sourceD4 guarantee. IfL>=2, replace only
its two endpoints bys,t, retaining every interior vertex in the oldsource;
the lifted Walk still has lengthL. IfL=1, use the three-edge backtrack
s--sigma(t)--sigma(s)--t, valid by fullN at both endpoints. IfL=0, choose any
oldneighborw of their common collapsedcenter, possible since minimumsource
degree14; s--w--t is a two-edge Walk (or use thenil Walk when endpoints
coincide). Thus everyfinal pair has a real Walk of length<=4.

The same argument works for every subset/prefix of the837 clones, in their
actualorderedlabels, because it never uses any otherclone internally. In
particular no futureclone is needed. Adjacent oldcenters are covered by the
L=1 case; there is no false independence hypothesis or assumed distances.
This is the existing FullNeighborhoodClones mathematical argument atD=4,
not a Boolean matrix proxy or a new Lean claim.

Each newclone has distance exactly2 to its ownoldcenter: noedge because the
oldsimple source has no selfloop, and any oldneighbor supplies a two-edge
route. Distinctnew vertices have noedge and no commonneighbor since frozen
full neighborhoods are disjoint, so their distances are3or4 by the bound.
These predictions await the separate ordinaryBFS checks.

## Strong new every-root distance4 prediction

Project an oldvertex81*a+x tocontrollera, and a newclone to its center's
controllera. Every actualfinal edge projects to one of the saved five-target
controller relations, possibly a stay in the samecontroller. Removing these
stays gives an undirected simple projection graph of maximumdegree<=5 on
192 controllers. No projected graph BFS is needed for the counting bound:
from anycontroller the radius3 ball has at most1+5+5*4+5*4^2=106 controllers.
A final Walk of length<=3 to an oldvertex would project, after removing
stays, to a controller Walk of length<=3. Hence at least192−106=86 wholeold
fibers, containing86*81=6966 OLD vertices, are farther than3 from everyfinal
root, old ornew. The actual allpair bound<=4 above makes allthose distances
exactly4. Therefore everyfinalroot has eccentricity4. This is a new explicit
prediction for the fresh all16389-root suite, not a producer measurement.
The parent source was never locally checked by fullallrootD4BFS; the fresh
suite is authorized to do one finalgraph allroot run, with no extra parent
BFS or duplicate smallroot runs.

## Acceptance and public boundary

Root actually checked the2026-11-01 Comellas primary table and matching
URSA_16384 description: located16/D4 guarantee remains16384, so this candidate
is larger by5. The source15/D4 actual15552 is taken from its literalZenodo
and currentmain table, not the outdated13608 description. Exact global
priority remainsUNKNOWN. Production alone is not mathematical acceptance;
root must receive the independent fullgraph/fullN/allroot receipts. This
batch adds0 graph/parameter/Lean counts by itself. Lean for this case has
not been authorized. No root-owned files, oldsource17, expert or frozen
packages were changed.
