# Three nonfaithful reflection families: finite capacity diagnosis

The requested quotient and formal-path diagnosis is **complete**. The single
CPU run took **4.222501 CPU seconds**, including JSON serialization. No
translation assignment was evaluated, and no graph search was launched.
The implementation has a 30 CPU second hard limit and a 28 CPU second stop
before starting another skeleton; neither limit was reached. `terminal.json`
records `COMPLETE` and a null cursor.

The smallest next complete translation batch is the 48 surviving mixed
skeletons for `(p,m,r)=(13,28,5)`: exactly **105,456** assignments, all legal,
with graph order 728. The `(17,24,2)` mixed branch offers order 816 in
**771,341** assignments. These are finite candidate ranges, not constructions
or existence claims. The parent decides any subsequent actual search.

## Exact scope and counts

All graphs have two orbits of size `p*m`, internal degree 2 on each orbit,
three cross edges, degree 5 and target diameter 5. Put `h=m/2`, and use

`(x,i)(y,j)=(x+r^i*y mod p, i+j mod m)`.

The fixed first internal set is `A={(0,h),(1,h)}`. Mixed means that `B` is
one noninvolutory inverse pair; both means that `B` consists of two distinct
involutions. The three cross labels are `S={e,s,t}`.

| `(p,m,r)` | order `n` | action order | compatible quotient units |
|---|---:|---:|---|
| `(13,28,5)` | 728 | 4 | `1,5,9,13,17,25` |
| `(17,24,2)` | 816 | 8 | `1,17` |
| `(29,12,12)` | 696 | 4 | `1,5` |

“Raw” below already chooses `0<=sigma<=tau<m` and chooses the inverse-pair
representative `0<=beta<h` for mixed, or `beta=h` for both; it retains only
connected quotient candidates. “Anchor” allows any of the three actual cross
labels as the identity anchor. “Side” additionally allows side exchange only
for both. “Units” adds exactly the compatible units in the preceding table.

| Parameters | Branch | Raw | Anchor | Side | Units / final | Walk capacity passes | Affine-form capacity passes |
|---|---|---:|---:|---:|---:|---:|---:|
| `13,28,5` | mixed | 4,932 | 1,742 | 1,742 | 303 | 86 | 48 |
| `13,28,5` | both | 294 | 102 | 54 | 10 | 0 | 0 |
| `17,24,2` | mixed | 3,008 | 1,072 | 1,072 | 562 | 190 | 157 |
| `17,24,2` | both | 196 | 68 | 36 | 20 | 0 | 0 |
| `29,12,12` | mixed | 388 | 148 | 148 | 82 | 68 | 47 |
| `29,12,12` | both | 50 | 18 | 10 | 6 | 3 | 2 |

| Parameters | Branch | Surviving raw translation tuples | Surviving legal tuples |
|---|---|---:|---:|
| `13,28,5` | mixed | `48*13^3 = 105,456` | 105,456 |
| `13,28,5` | both | 0 | 0 |
| `17,24,2` | mixed | `157*17^3 = 771,341` | 771,341 |
| `17,24,2` | both | 0 | 0 |
| `29,12,12` | mixed | `47*29^3 = 1,146,283` | 1,136,191 |
| `29,12,12` | both | `2*29^4 = 1,414,562` | 1,365,784 |
| All three | both branches | **3,437,642** | **3,378,772** |

No residual translation symmetry or internal-label ordering was used to reduce
these assignment counts. They count assignments, not distinct graphs.

The two surviving `(29,12,12)` both skeletons are `(beta,sigma,tau)=(6,1,3)`
and `(6,1,4)`, with minimum affine-form capacities 29 and 31. For comparison,
`(6,1,2)` passes the walk count with minimum 29 but fails the form count with
minimum 27.

There is no uniform obstruction for the mixed branches from this test. In
contrast, every both skeleton for `(13,28,5)` has a root/target quotient cell
with at most **1** nonbacktracking walk of length at most 5, and every both
skeleton for `(17,24,2)` has one with at most **4**. These fail even before
translations are chosen, since the cells need 13 and 17 vertices respectively.
This is an exhaustive finite obstruction for these specified both families;
it is not an exclusion of other mechanisms or groups.

## Why the normalization preserves candidates

In all three cases `ord_p(r)=d` divides `m`, `m/d` is odd, and
`r^(m/2)=-1`. Because `p` is odd, an involution must have quotient `h`, and
every `(x,h)` is an involution. Thus these are all the involutions.

For two distinct reflections `R(u)=(u,h), R(v)=(v,h)`, the automorphism

`F_(lambda,t)(x,i)=(lambda*x+(1-r^i)*t,i)`

with `lambda=(v-u)^(-1)` and `t=-lambda*u/2` sends their unordered set to
`{R(0),R(1)}`. The remaining same-quotient affine stabilizer is the identity
and `T(x,i)=(-x+(1-r^i)/2,i)`, which exchanges these two reflections. It does
not justify another projective normalization of the remaining translations.
In particular, those remaining translations must not be assumed nonzero.

For a quotient unit `k`, the map `phi_k(x,i)=(x,k*i)` is a group automorphism
exactly when `r^k=r`. Equivalently `k=1 mod d`, with `gcd(k,m)=1`. These
conditions give exactly the three unit lists above. Every such unit is odd,
so `k*h=h mod m`; consequently it fixes both elements of the normalized A.
No other quotient unit is used. An independent paper check by the source
agent confirmed these lists and the preservation of A.

Reanchoring at a cross label `s0=(z,j)` replaces `S` by `S*s0^-1` and B by
`s0*B*s0^-1`, while leaving A unchanged. Explicitly,

`(x,k) in S -> (x-r^(k-j)*z,k-j)`,

`(b,beta) in B -> (r^j*b+(1-r^beta)*z,beta)`.

Thus the cross quotient multiset `{0,sigma,tau}` may be translated by any
one of its entries and then sorted after removing one zero. Repeated quotient
entries do not mean repeated actual labels; legality is imposed on the full
labels only.

For mixed, an inverse pair may be represented by either its element or its
inverse, so `beta` becomes `min(beta,-beta)` after applying a unit. Quotient
`h` is forbidden, since every element there is self-inverse. At quotient 0,
only translation 0 is forbidden. **Side exchange is not used for mixed:** it
would put a noninvolutory inverse pair in A, outside this normalized slice.

For both, exchanging sides gives `S^-1` and exchanges A and B. Since B also
has two distinct reflections, the displayed affine normalization restores A
and preserves the quotients. Thus both may additionally negate all cross
quotients. The canonical representative is the minimum over compatible
units, the three anchors, cross-label order, independent mixed B inversion,
and this both-only sign. These transformations compose within the stated
family. No claim is made that every incidental graph isomorphism is removed.

The product of the two normalized A reflections is a nonzero translation,
so A generates the whole additive `F_p` subgroup. With the identity cross
edge available, connectivity therefore reduces exactly to

`gcd(m,h,beta,sigma,tau)=1`.

This gives the declared raw connected skeleton ranges. For both, `beta=h`,
so it simplifies to `gcd(m,h,sigma,tau)=1`.

## Formal-path capacity and legality

Mixed has variables `(b_x,s_x,t_x)` and

`B={(b_x,beta),(-r^-beta*b_x,-beta)}`.

Both has variables `(b_x,d_x,s_x,t_x)` and

`B={(b_x,h),(d_x,h)}`.

For either case, `s=(s_x,sigma)` and `t=(t_x,tau)`. Every path endpoint has
a fixed quotient and a translation that is an affine linear form in these
variables over `F_p`. The evaluator retains the entire coefficient vector,
including its constant coefficient; a step of quotient voltage q and form L
from current quotient i updates the translation by `r^i*L`.

For each of the two orbit roots it enumerates every named nonbacktracking
path of length at most 5, including the empty path. There are exactly
`1+5+20+80+320+1280=1706`; this is asserted separately for every root and
skeleton. Every shortest path occurs in this enumeration. Left group
translations act within each orbit, so the two identity roots suffice for
the necessary diameter condition.

For each destination orbit and quotient cell, the number of walks is an
upper bound on reachable vertices, and the number of distinct affine forms
is a possibly smaller upper bound, valid for every translation assignment.
Each cell contains p vertices. Fewer than p forms therefore excludes the
entire skeleton. At least p forms is only necessary: different forms can
evaluate to the same field element simultaneously, and all cells must be
covered by one common assignment.

Legality requires `b_x!=0` for mixed beta=0, `b_x!=d_x` for both, and the
three actual cross labels to be distinct. For sorted cross quotients,
the number of legal `(s_x,t_x)` is `(p-1)(p-2)` if both quotients are zero,
`p(p-1)` if exactly one is zero or both are equal and nonzero, and `p^2`
otherwise. Multiply by `p-1` or p for mixed, and by `p(p-1)` for both.

## Saved material and read scope

- `capacity.py`: the complete three-case generator and bounded evaluator.
- `capacity_results.json`: all raw and canonical skeletons, every root/cell
  walk and form count, every deficient cell, and the summaries.
- `terminal.json`: actual runtime and complete status.
- `profile_metadata.json`: exact multiplication, coordinate order, legality,
  unit lists, survivor counts and filenames for a future approved profile.
- `p*_m*_r*_mixed_skeletons.txt` and `p*_m*_r*_both_skeletons.txt`: six
  complete survivor lists. First line is the count, then `beta sigma tau`.

The implementation read the existing F41 `capacity.py` and `SEARCH_REPORT.md`
and used the already established normalization derivation. All new writes
are in this directory. The diagnostic did not read or modify the wiki,
HTML, old DD82 work, graph-search profiles, or any other parameter family.
