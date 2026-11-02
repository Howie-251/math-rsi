# Two further partner cases for a twelve-vertex D1 heavy component

## Statement and dependencies

New paper derivation, awaiting independent review. Under the actual graph
hypotheses and notation of `D1_COMPONENT_MINIMUM_SIZES.md`, the two cases

    (h,k,a,b,s,t) = (12,20,5,3,1,2), (12,24,6,3,0,2)

are impossible. Here H and K are distinct actual B support components,
h,k are their sizes, a,b their cross degrees, and s,t their internal original
degrees. These exclusions do not require that H,K arise from D1 except to
place them in the current list.

Use the exact exterior moments and domains in that paper. Each nonempty
exterior type (x,y) has even size at least four: neighbor counts to H,K are
constant on a B component, its size is even, and B≤2 rules out size two.
This applies to type (0,0) as well.

For any B component C, define d_C(v)=|N(v)∩C|. Component equitability and
the actual identity imply

    (A d_C)(v)+d_C(v)=|C|  for every v outside C.             (1)

Indeed (A²+A)1_C=10·1_C+|C|·1. This identity will contradict the forced
exterior types without any graph search or floating computation.

## 1. The partner of size twenty and internal degrees one, two

There are 30 exterior vertices. Their moments are

    Σx=24, Σx(x−1)=36, Σy=60, Σy(y−1)=120, Σxy=0.

Thus x and y cannot both be positive at any exterior vertex. Let X be the
positive-x support and Y the positive-y support. Cauchy's inequality and
Σy²=180 give |Y|≥60²/180=20, so |X|≤10.

The pointwise domain 5x+3y≤20 gives x≤4. A nonempty type with x=4 has at
least four vertices and contributes at least 48 to Σx(x−1), exceeding 36.
Thus x≤3. Let u,v,w be the numbers of exterior vertices with x=1,2,3.
All have y=0. Their two moments give

    u+2v+3w=24, v+3w=18,
    u=3w−12, v=18−3w, |X|=6+w.

Nonnegativity gives w≥4, whereas |X|≤10 gives w≤4. Therefore X consists
of six vertices of type (2,0) and four of type (3,0). Its size is ten,
so Y has exactly twenty vertices and exhausts the complement. Equality
in Cauchy's inequality makes y=3 on all of Y. The exterior types are
exactly

    (2,0):6, (3,0):4, (0,3):20.

Take any v in X. It has no neighbor in K. The function d_K equals five
on H, three on Y, zero on X, and two on K. Therefore (1), with C=K,
becomes

    20 = 5x_v + 3|N(v)∩Y|.

But x_v is either two or three. The difference 20−5x_v is respectively
ten or five, neither divisible by three. This contradiction excludes the
case. The value on H is the outgoing degree a=5, not the reverse degree
b=3; keeping that distinction is essential in this final step.

## 2. The partner of size twenty-four and internal degrees zero, two

There are 26 exterior vertices, with moments

    Σx=24, Σx(x−1)=24, Σy=72, Σy(y−1)=168, Σxy=72.

The domain is x+3y≤12, 2x+y≤8, and x+y≤8. In particular x≤4.
A type with x=4 would contribute at least 48 to Σx(x−1), impossible.
If a type with x=3 occurs, its at least four vertices exhaust the entire
second factorial moment. There are then exactly four vertices with x=3,
no vertices with x=2, and twelve with x=1. The domain gives y≤2 when
x=3 and y≤3 when x=1. Consequently Σxy≤4·3·2+12·1·3=60, contradicting
72. This argument also permits multiple x=3 types: their combined size
would have to be four, so at most one could occur.

It follows that x≤2. The two x moments now force twelve vertices with
x=2, no vertices with x=1, and fourteen with x=0. Write X for the first
set. The cross moment gives Σ_X y=36. Since the domain gives y≤3 on X,
all twelve vertices have type (2,3).

On the remaining fourteen vertices, let n_j count those with y=j.
Here 0≤j≤4, every nonzero n_j is even and at least four, and

    Σn_j=14, Σj n_j=36, Σj(j−1)n_j=96.

Subtracting twice the first y moment from the second gives

    2n_4−n_1−n_2=12.

Hence n_4≥6; the y sum gives n_4≤9, and evenness leaves n_4=6 or8.
If n_4=6, then n_1=n_2=0, and the remaining equations give n_3=4,n_0=4.
If n_4=8, then n_1+n_2=4 and n_1+2n_2+3n_3=4. Thus n_1=4,n_2=n_3=0,
leaving n_0=2, forbidden for a nonempty type. The only possible exterior
type distribution is therefore

    (2,3):12, (0,3):4, (0,4):6, (0,0):4.

Choose v of type (0,3). The function d_H equals zero on H, three on K,
two on X, and zero on the other exterior vertices. Thus (1), with C=H,
gives

    12 = 3·3 + 2|N(v)∩X|,

which is impossible by parity. This excludes the second case.

## Combined remaining list and scope

Combining these two paper exclusions with the finite
integer inequalities and the separate twelve-by-twelve exclusion leaves,
when h=12, only

    (k,a,b)=(16,4,3), with (s,t) in
       {(0,0),(0,1),(0,2),(1,1),(1,2),(2,0),(2,1)},
    (k,a,b,s,t)=(20,5,3,0,2).

This combined list is conditional on those source results and their actual
review status. None of its eight entries is asserted feasible or excluded.
Cases h≥14 remain. No universal order62 or exact N(8,2) result is claimed.
