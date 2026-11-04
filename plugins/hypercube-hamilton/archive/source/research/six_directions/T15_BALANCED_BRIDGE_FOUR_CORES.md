# Four more T15 cores via a balanced four-hole bridge

Date: 2026-11-01. ARIS proof-writer. Candidate complete proof for the stated
four orbits, pending independent finite-input and semantic audit.
Full T15, the whole eight-hole layer, and P6 remain unproved.

## Claim, assumptions and normalized geometry

For every arbitrary complete-graph matching on Q5 with a marked T15 hole
geometry in orbit 2, 7, 10 or 44 of `t15_analytic_geometry.json`, the two
prescribed majority holes can be omitted in a 30-vertex cycle containing
the matching, with only short added edges. All cube-automorphic images
and both parity orientations are included.

Take the cut in the following table, delete its coordinate, and apply the
same coordinate permutation to both faces so the retained B majority
hole is 7. The minority hole is 0 in B. The one-face A has three even
local holes x,r,s; omit x. B has three original holes 0,7,y; omit y.
The labels r,s are A original holes and their B mirrors are covered by
the original matching (internally or by a crossing).

| core | cut | x (A omitted) | y (B omitted) | r (preferred bridge) | s (other bridge) |
|---:|---:|---:|---:|---:|---:|
|2|1|0|1|9|3|
|7|0|0|1|9|10|
|10|1|0|1|9|15|
|44|3|9|11|10|6|

These labels follow by explicit coordinate deletion/permutation, not by
assuming a matching symmetry. Denote internal matchings by F_A,F_B,
crossings by C, port sets by X_A,X_B, and c=|C|. Each face has 13 covered
original vertices, so c is odd, 1<=c<=13, and the internal edge count is
(13-c)/2 on each face. Crossings may be arbitrary long edges; their
partner bijection is unrestricted.

## Dependencies and finite inputs

1. Q4 N14: a matching with two equal-parity holes extends to a 15-cycle
   omitting either specified hole, using short new edges. This is an
   explicit prior import, valid for arbitrary complete-graph matchings.
2. Complete Q4 tables for balanced holes {0,7,t,y}, omitting t,y, with
   a required matching on the other twelve vertices. Each table contains
   all 10395=11!! matchings. Files are
   `q4_balanced_two_avoided_<t>_<y>.bin`; the geometry list is
   `q4_balanced_two_avoided_generation.json`. There are 13 marked orbits
   covering all 49 choices of even t!=0 and odd y!=7, with retained free
   pair 0,7. Positive records give explicit 14-cycles; negatives must be
   independently checked by exhausting short degree completions.
3. For the preferred pair (r,y) in all four rows, the table has **no**
   negative matching: (9,1), or (10,11) in the orbit of (9,11).
4. For the other pair (s,y), the negative counts are respectively
   3,1,10,1. Only those exact complete negative lists, not failed bounded
   searches, are used below.
5. Fifteen B optional-edge spectra, stored with positive cycles in
   `t15_balanced_bridge_spectra.json`. A finite degree-factor obstruction
   outside each spectrum is recorded in
   `t15_balanced_bridge_spectrum_verification.json`.

The complete table generator is `q4_balanced_two_avoided_probe.cpp`.
The finite exceptional B inputs and positive spectra are prepared and
checked by `t15_balanced_bridge_probe.py`; fresh independent checking is
required for acceptance. No Q5 T15 theorem is used as an input.

## 1. General one-bridge transfer

Choose z in {r,s}. Pair the vertices of X_A union {z} into an artificial
matching D. F_A union D has exactly the two even holes x and the other
member of {r,s}; N14 gives a 15-cycle on A-x containing it.
Delete D, attach all C, and add the short bridge z_A z_B.

If z_B is not in X_B, it is covered internally by F_B. The graph from A,
C and the new bridge is a path forest with endpoint set X_B union {z_B},
interiors A-x. Compress these paths to a matching R. If F_B(z)=k and
R(z)=q, replace kz,zq by kq in F_B union R. The internal endpoint k
is not a crossing port, whereas q is a crossing port, so k!=q and this
replacement creates a matching. The resulting L_B has holes
{0,7,y,z}. A 14-cycle omitting y,z and containing L_B expands to a
30-cycle: restore z_B and all 15 A vertices, along with every original
edge. All artificial edges disappear by deletion or expansion.

If z_B is a port and c>=3, let d=C^{-1}(z_B) and prescribe zd in D.
This is a legitimate pairing because z is an original A hole and d is
a covered A port. D contains at least two edges. After deleting D, the
endpoints z,d of its distinguished edge lie in different path components:
the remainder of their former cycle is broken by another deleted D edge.
Attaching crossings supplies distinct B endpoints. Adding z_A z_B joins
those two distinct components at the leaf attached to d, making no cycle.
The resulting forest has endpoints X_B-{z_B} and interiors (A-x)+z_B.
Compress it to R. Now L_B=F_B union R is a matching with holes
{0,7,y,z}. Its 14-cycle omitting y,z expands to the required 30-cycle.

For c>=3 choose z=r. Its table has no negatives, so the transfer always
works, independently of the crossing bijection and internal matchings.
For c=1 it also works unless X_B={r}.

## 2. One crossing and the alternate bridge

The only outstanding case has one original crossing d_A r_B. Choose z=s,
which is internally covered in B because r!=s. The pairing is necessarily
D={ds}. Deleting ds from the N14 cycle gives a path through A-x with
endpoints d,s; attaching d_A r_B and the s bridge compresses to the edge
rs on B. If k=F_B(s), suppress s to obtain

    L_B = F_B - {sk} + {rk},   holes {0,7,y,s}.

If this L_B is positive in the complete table, Section 1 finishes.
Otherwise the original B matching is recovered uniquely as

    F_B = L_B - {r L_B(r)} + {s L_B(r)}.

The vertex r is covered in every negative L_B, because it is different
from 0,7,y,s. This gives exactly 3,1,10,1 possible B matchings for the
four rows, respectively. No other F_B can obstruct this alternate bridge.
Their reconstruction is entirely independent of F_A and d.

## 3. Exceptional B matchings: force a shared optional edge

Fix one of these 15 exceptional B matchings. It has holes {0,7,y,r}.
The preferred (r,y) table is universally positive. Let U be the union of
short edges outside F_B that occur in the saved valid 14-cycles on
B-{y,r}. Only a certified lower set of possible edges is needed; we do
not assume every possible edge is saved.

On the common Q4 labels let A'=Q4-x, and form the short-edge graph

    G = E(Q4[A']) minus U.

The finite check proves there is **no simple spanning graph H in G**
whose degree is 2 at s and 1 at every other A' vertex. This is an exact
small enumeration: choose the two distinct G-neighbors of s; on the
remaining twelve vertices enumerate every perfect matching using G
edges. None exists for any of the 15 B inputs. This enumeration does not
mention F_A, d, or any chosen A path; its absence therefore applies
uniformly to all of them. The saved U sizes range from 17 to 22.

Now take the N14 A cycle using D={dr}, and delete dr to get a path P on
A-x from d to r containing F_A. The vertex s is its remaining free hole
and is internal. The edge set H=P-F_A consists of short edges and has
degree 2 at s and degree 1 at every other A' vertex: covered vertices
are internal with one F_A edge, and the two endpoints d,r are free in
F_A. Consequently H cannot lie in G. There is an edge uv in H intersect U.
Choose a B cycle C_B witnessing this particular edge uv.

This proves the correct existential order: choose any permitted A path,
find one of its edges in the *union*, then select a B cycle witnessing
that edge. It does not assume one B cycle contains the entire union.

## 4. Finish the one-crossing construction

Attach the original crossing d_A r_B and the new short bridge r_A r_B
to P. Since d!=r, this gives a simple 16-cycle C_A supported on
(A-x) union {r_B}. It is disjoint from C_B on B-{y,r}.
The common optional edge uv is inside A-x in C_A and inside B-{y,r}
in C_B. It is in neither original matching. Delete its copy from each
cycle and add the two short bridges u_Au_B and v_Av_B. Each opened cycle
is a path, and the two bridges join these two disjoint paths into one
simple 30-cycle. Its support is exactly Q5-{x_A,y_B}. It retains F_A,
F_B and the sole original crossing; all surviving new edges are short.

This handles all fifteen exceptional B matchings and every A matching
and root d without enumerating those A matchings. Sections 1--4 exhaust
all c and prove the four-orbit claim, conditional only on the listed
finite inputs and N14 import being verified.

## Limits

The other hard T15 cores, the seven Q6 exceptional geometries' full
path obligations, and full eight-hole P6 are not closed by this proof.
Any new eight-hole parent count requires separate exact coordinate
projection and integration with the earlier eight-core theorem.
