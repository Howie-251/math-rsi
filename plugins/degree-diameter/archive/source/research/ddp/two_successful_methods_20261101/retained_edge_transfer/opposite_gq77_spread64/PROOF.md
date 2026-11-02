# Fixed odd-characteristic opposite-GQ spread extension:160050 vertices,degree64,D3

This is one frozenGF7/GF49 incidence structure and its original50line slope
spread, listed in PARAMETERS.json. The classical source is the opposite
product of symplectic GQ(7,7). The new rule transfers the accepted spreadflag
augmentation to odd characteristic; it is a new parameter instance of the
existing retained-edge pin-cover mechanism, not an independent framework.
The source160000 reproduction is not counted as a new result. Parent-owned
public comparison and fresh literal acceptance are separate tasks.

## Literal fields and the corrected odd-characteristic form

GF7 uses ordinary addition/subtraction/multiplication modulo7. It does not
use XOR. Since3 is not a square in GF7, the quadratic beta²−3 is irreducible
and defines GF49=GF7[beta]/(beta²−3). Codea0+7*a1 denotes a0+a1*beta, and

    (a0+a1 beta)(b0+b1 beta)
      =(a0*b0+3*a1*b1)+(a0*b1+a1*b0) beta.

All operations on the right are modulo7. The generated table has a verified
inverse for each of its48 nonzero elements and beta²=3. Because beta^7=−beta,
the relative trace is

    Tr(z)=z+z^7=2*z0.

This formula was checked on all49 field elements. In particular the trace
is not the beta coefficient used by the earlier characteristic2 instance.

Write x=(u0,u1,v0,v1) as(u,v)∈GF49². The alternating form is

    B(x,y)=Tr(u*v'−v*u')
      =2*(u0*v0'+3*u1*v1'−v0*u0'−3*v1*u1') mod7.

The closed formula was compared with actual GF49 multiplication and trace
on all79800 unordered distinct projective point pairs. Alternation was
checked on all2401 ambient vectors. Its actual4×4 Gram determinant is4≠0,
so the form is nondegenerate. FIELD_TABLES.json records both fields and the
relative trace data.

## Points, lines and full finite GQ input

Normalize every nonzero GF7^4 vector by making its first nonzero coordinate1.
The400 tuples are sorted lexicographically and numbered0..399. For every
orthogonal point pair, projectivize its2-dimensional span. The resulting
400 distinct8point tuples are sorted lexicographically to give lineIDs0..399.
Each point's8 incident lineIDs are ascending.

The actual checks establish400points/400lines,8points per line,8lines per
point,3200 incidences, at most one joining line for any point pair, at most
one intersection point for any two lines, and exact equivalence of distinct
collinearity with B=0. There are11200 distinct collinear unordered pairs.
For every one of the156800 nonincident point-line pairs, exactly one point
on the line is collinear with the external point. The projected point and
joining line for every such pair are in PROJECTION_WITNESSES.json.

PROJECTION_INDEX_INPUTS.json additionally supplies three indices0..7 for all
160000 original point-line pairs: position of q on l, of joiningline m among
lines through p, and of q on m. Incident entries use q=p,m=l. These are
concrete input data, not a claim that the separate Lean task has completed.
GQ_AXIOM_CHECK.json records all finite checks, measured1.597632688CPU.
No source graph or graph BFS was generated during this geometry stage.

## Original ordered Desarguesian spread

For m∈GF49 take theGF7 subspace {(u,m*u):u∈GF49}; also take the infinity
subspace {(0,v):v∈GF49}. Every such2-dimensionalGF7 subspace is isotropic,
because u*m*u'−m*u*u'=0. A nonzero pair(u,v) with u≠0 belongs to the unique
slope m=v/u; if u=0 it belongs to infinity. Hence the50 projective lines
partition all400 points. The actual line membership and owner checks pass.

The slope codes0..48 are interpreted(m%7,m//7), followed by infinity, and
their frozen lineIDs in that order are

    57,65,73,81,89,97,105,204,212,220,228,236,244,252,
    351,359,367,375,383,391,399,155,163,171,179,187,195,203,
    302,310,318,326,334,342,350,106,114,122,130,138,146,154,
    253,261,269,277,285,293,301,0.

This list is not subsequently sorted. PARAMETERS.json keeps each slope,
its original lineID and8point IDs, and the unique point_spread_owner index.

## Literal160000vertex source

An old vertex(p,l) has label400*p+l. Distinct(p,l),(q,m) are adjacent iff
p is incident with m and q is incident with l. For each vertex there are
8 choices q on l and8 choices m through p, giving64 raw neighbors. A raw
selfpair occurs exactly at an incident flag p∈l. Removing it leaves3200
flags ofdegree63 and156800 nonflags ofdegree64, with

    source_m=(3200*63+156800*64)/2=5118400.

The producer generates that source once in packed64slot adjacency. It
checks every degree, neighbor uniqueness/order and final reciprocity, with
exactly these counts; no old-root distance BFS is performed.

The inherited generic GQ route proves source diameter≤3. For endpoints
(p,l),(q,m), choose a on l collinear with q and b on m collinear with p;
let k pass through a,q and n through b,p. If the points coincide, use any
through-point line. Then

    (p,l), (a,n), (b,k), (q,m)

satisfies each cross-incidence relation. Remove consecutive equal vertices
to obtain a true simple-graph walk of length≤3. All required point/line
premises are the finite facts checked above. This argument is not a claim
of having BFSed all160000 source roots.

## Fifty actual pin groups and current-prefix coverage

For ordered spread index j, add newvertex v_j with label160000+j. Its pins
are all64 incident flags(a,b) for which a lies on the spreadline L_j:

    S_j={(a,b):a∈L_j and a∈b}.

Pin order is8 ascending pointIDs, then each point's8 ascending incident
lineIDs. These groups are disjoint and partition all3200 source flags.
Every sourceflag uses its single spare degree once; every nonflag stays
at64. Each of the50 new vertices hasdegree64. There are no new-new edges,
and every5118400 source edge is retained. Thus finaln=160050 and

    final_m=5118400+50*64=5121600=160050*64/2.

For a target oldvertex(p,l), choose a∈L_j collinear with p and n through
a,p. Choose a line b through a meeting l at q, by projection (or b=l,q=a
when a∈l). The pin(a,b) reaches that target along

    (a,b), (q,n), (p,l),

with consecutive repeats suppressed. Thus S_j has complete radius2
coverage of the old source.

For two distinct spreadlines L_i,L_j, pick a on L_i and project it onto
L_j to get c. These points are distinct, and their joiningline b makes
the two flags(a,b),(c,b) adjacent. Hence

    v_i, (a,b), (c,b), v_j

has length3. Equivalently S_j reaches each previously inserted v_i in2
steps. This explains coverage of the complete current graph, rather than
only the original source.

Before every insertion, the actual producer expands the64pins in the
complete current adjacency to radius2, checks every current vertex is
covered and every pin still hasdegree63, then adds only the64 specified
edges. All50 prefixes pass. At stepj, currentorder is160000+j and the
observed distance histogram is exactly

    radius0:64, radius1:3528, radius2:156408+j.

All earlier j bonusvertices have distance exactly2 from the pin union.
EXTENSION_STEPS.json saves every ordered pin list, prefixorder, histogram
and earlier-bonus distance count. Total prefix checking measured0.240287
internalCPU, with zero uncovered targets. This is50 complete multi-source
radius2 checks, not160050 all-source diameter BFS.

## Final graph and evidence boundaries

The final graph is simple, undirected and64regular, and the preceding
Walk arguments give diameter≤3. The degree64 diameter2 Moore bound is
1+64+64*63=4097<160050, so the diameter is exactly3. The generic formal
interface's looser2walk endpoint bound1+64+64²=4161 would also suffice;
no sharp-Moore Lean theorem is claimed here.

The complete graph_d64_D3_n160050.edges has header

    160050 5121600

and one u<v unorderededge per line, strictly sorted lexicographically. The
64,591,375-byte file was fully closed before being made available to the
fresh checker. The producer counts5118400 old-old,3200 old-new and0
new-new edges. It performs no source BFS, no all-root final BFS, no solver,
hash, install or Lean call.

Geometry plus actual compiler/production child receipts total3.871704688
CPU, one worker, within300CPU. Production childCPU is1.041868, including
startup/teardown; its internal clock is separately recorded. BUILD_RUN.json
keeps the actual commands and exit0 receipts.

Fresh independent RREFgeometry/literalformula/degree/50new-root validation
and the separate formalization are root-coordinated and are not certified
by this producer report. Parent alone counts the new graph after actual
independent acceptance. The best-located public source guarantee is160000,
so this candidate adds50 vertices relative to that located construction;
the narrow comparison does not certify global-record status or priority.
No degree65 cloning, ovoid task, other field or additional graph was started.
