# Three canonical cases for the order-62 S_TOUCH template

## Statement and scope

Every actual order-62 candidate in the S_TOUCH template can be relabeled into
one of the following three cases. This is a new paper-level coverage reduction;
it is not a recovery of the historical eight solver leaves, nor an exclusion.
It uses the actual graph and exact repeat matrix, not an independent cubic graph.

Let the root be 0, its neighbors X={1,...,8}, and its triangle be 012.
The exceptional vertex w=9 has parents {1,3}. All other vertices in Y have
exactly one parent; write C_i for the singleton class with parent i.
The class sizes are (5,6,6,7,7,7,7,7). In S_TOUCH the matrix
B=A²+A−7I−J is simple, symmetric, and has row sum 3, with AB=BA.
Every vertex lies in at most one triangle. These statements follow from the
original graph assumptions and the recovered seven-template reduction.

| Case | The six neighbors of w in Y | Full B-neighborhood of w |
|---|---|---|
| A | one point of C3 and one of each C4,...,C8 | {0,3,the selected C3 point} |
| C2 | two points of C4 and one of each C5,...,C8 | {0,4,one point of C2} |
| C3 | two points of C4 and one of each C5,...,C8 | {0,4,one point of C3} |

In the last two cases the third B-neighbor is not adjacent to w. Permutations
of labels 4,...,8 and permutations within each singleton class are relabelings
preserving the template, so all selected points can be fixed canonically.
No automorphism of the actual graph is asserted.

## The saturated row at vertex 1

The pairs 01 and 12 are triangle edges, so B10=B12=1. Vertices 1 and 3
are nonadjacent and have exactly the two fixed common neighbors 0,w.
Thus B13=1. Row sum 3 gives the exact support

    N_B(1)={0,2,3}.

The original neighborhood is N_G(1)={0,2,w} union C1. Evaluate AB=BA
at (1,w). The right side is A0w+A2w+A3w=1. On the left B0w=1,
Bww=0, hence

    B2w + sum_{y in C1} Byw = 0.                    (1)

Every term is nonnegative. Therefore B2w=0 and Bwy=0 for every y in C1.
For a singleton y in C4 union ... union C8, the right side of the same row
identity is A0y+A2y+A3y=0. The left side contains Bwy, so

    Bwy=0 for every y in C4 union ... union C8.     (2)

These are exact consequences of a saturated known B row.

## The six Y-neighbors of w

Vertex w already has parents 1 and 3 and therefore six Y-neighbors.
It cannot have a neighbor in C1: that would create a second triangle at 1.
For each x in {4,...,8}, the nonadjacent pair (w,x) has a common neighbor.
Neither parent 1 nor parent 3 is adjacent to x, and w is not adjacent to 0.
Thus this common neighbor must be a selected point in Cx. Consequently at
least one point is selected in each of these five classes.

The sixth point lies either in C2, in C3, or is a second point in one of
C4,...,C8. It cannot lie in C1 as just proved. The C2 possibility is
impossible: (w,2) already has common neighbor 1, so a selected C2 point
would make Bw2≥1, contradicting (1).

If the sixth point a lies in C3, then w,3,a form a triangle. Its two B
edges from w have weight 1; together with Bw0=1 they exhaust the row.
This is case A. Each of C4,...,C8 supplies exactly one selected point.

Otherwise, permute {4,...,8} so that C4 supplies the extra point. The pair
(w,4) has exactly these two common neighbors, giving Bw4=1. Together with
Bw0=1 this leaves one further B-neighbor b.
For x in X the exact common-neighbor counts are: c(w,1)=c(w,3)=0,
c(w,2)=1, c(w,4)=2 and c(w,x)=1 for x=5,...,8. Accounting for adjacency
to 1 and 3 shows that no other vertex of X is a B-neighbor of w.
Thus b lies in Y and is distinct from w. Equations (1) and (2) restrict b
to C2 or C3. Neither class has any selected Y-neighbor, so b is not
adjacent to w. This yields cases C2 and C3, and also shows t(w)=0.

## Canonical labels and exact input meaning

Using the archived template's singleton labels, the representatives are:

| Case | A-neighbors of 9 inside Y | Dynamic B-neighbors of 9 |
|---|---|---|
| A | 21,27,34,41,48,55 | 3,21 |
| C2 | 27,28,34,41,48,55 | 4,15 |
| C3 | 27,28,34,41,48,55 | 4,21 |

The fixed B-neighbor 0 is not a dynamic variable. For each row, every other
dynamic A or B entry is zero. The designated points within each class can
be moved to these labels independently. In cases C2/C3, the B-neighbor is
in a class unused by A9, so no incompatible simultaneous relabeling occurs.

The fresh base CNF and variable map are under
computations/dd82/n62/s_touch_certificate_profile/. Any branch run must
append these exact unit clauses to that base using its actual map, preserve
the base variable meanings, and distinguish UNKNOWN from a checked proof.
This paper proves only original-graph coverage and the stated rows. The
existing source-level CNF preservation argument is in CNF_BRIDGE_OBLIGATIONS.md;
the Lean encoding bridge and whole S_TOUCH contradiction remain separate work.
