# Order61 component quotients: a matching-edge lifting obstruction

Status: root/writer checked, pending the current mechanism's review.
This short note uses actual adjacency/defect blocks and introduces no
symmetry or binary-defect assumption. No solver or quotient enumeration
was run here. The norm manuscript already under review is unchanged.

## 1. A triangle-free quotient edge between two matching components

Let G be an order61 target and let Q be its actual weighted-defect
component quotient, as defined in
[GENERAL_THREE_DEFECT_COMPONENT_QUOTIENTS.md](GENERAL_THREE_DEFECT_COMPONENT_QUOTIENTS.md).
Suppose two different components i,j satisfy

`q_ii=q_jj=1`,       `q_ij>0`,
`q_ik q_kj=0` for every k different from i,j.                    (1)

Then Q cannot arise from G. Equivalently, every support edge of an
actual quotient between two diagonal-one components must lie in a
triangle of the off-diagonal support.

To prove this, write `S=A_ii`, `T=A_jj`, `X=A_ij` for the same actual
adjacency matrix. The diagonal-one condition makes S and T matching
matrices, so

`S^2=I`,       `T^2=I`,       `SJ=J`,       `JT=J`.

For every other k, (1) makes at least one of `A_ik,A_kj` zero. The
off-diagonal block of the actual defect is zero, hence

`SX+XT+X=J`.                                                    (2)

Left-multiplying (2) by S and subtracting gives `XT-SXT=0`.
Right-multiplication by T then gives `X=SX`. Likewise, subtracting
the right-T-multiple of (2) gives `SX-SXT=0`, and left-multiplication
by S gives `X=XT`. Equation (2) now reads `3X=J`, impossible for
the binary adjacency block X. This proves the obstruction.

The proof concerns lifting an actual quotient. The integer quotient
equation alone permits the constant fractional solution `X=J/3`,
which is exactly why a separate adjacency argument is needed.

## 2. Application to an explicit surviving five-component quotient

The size vector and matrix

```
n=(2,5,6,18,30),

Q=[[0,5,3,0,0],
   [2,0,0,0,6],
   [1,0,1,6,0],
   [0,0,2,1,5],
   [0,1,0,3,4]]
```

really satisfy the abstract quotient identities. All rows sum to8;
the positive-interface balances are

`2*5=5*2`, `2*3=6*1`, `5*6=30*1`,
`6*6=18*2`, `18*5=30*3`.

Direct multiplication gives

`Q^2+Q-11I = 1 (2,5,6,18,30)`.

Its diagonal is `(0,0,1,1,4)`, with the required simple-graph and
handshake conditions. The off-diagonal support is a five-cycle.
In particular, the adjacent size6 and size18 components both have
diagonal1 and have no common third support neighbor. Section1 excludes
every graph lift of this Q, including every simultaneous relabeling.

Thus an argument claiming that *no abstract quotient exists* for all
c>=5 would be false: this is an explicit abstract quotient. A complete
order61 disconnected-defect exclusion must also address lifting for
surviving quotients. This note does not assert that all five-component
quotients have the same obstruction.

## 3. An equal-size block lemma and the (2^8,5^9) size pattern

There is a reusable quotient-level counterpart. Let I consist of r>1
components of the same size a, put `S=Q_(I,I)`, and suppose the external
return matrix has the form

`Q_(I,Ic) Q_(Ic,I)=alpha I_r+beta J_r`.

The actual quotient polynomial restricts to

`S^2+S=(11-alpha)I_r+(a-beta)J_r`.                              (3)

Detailed balance makes S symmetric. If `a!=beta`, commuting S with
(3) gives `SJ=JS`; therefore S has constant integer row sum k.
If `45-4alpha` is positive and nonsquare in Q, the restriction to
`1^perp` satisfies the irreducible quadratic

`x^2+x-(11-alpha)=0`.

The conjugate roots have equal multiplicities in the characteristic
polynomial of this rational restriction. Consequently r is odd and

`trace(S)=k-(r-1)/2`.                                          (4)

These conclusions require the stated external return pattern; equal
component sizes alone do not imply it.

For a concrete application, consider the surviving size pattern of
eight size2 components and nine size5 components, with c=17. The
quotient trace is zero, so every diagonal is zero. Detailed balance
forces a positive size2-to-size5 entry to be5 and its reverse to be2;
a size2 row can contain at most one such interface.

Let t be its number of size5 interfaces, and a_j its entries to the
other size2 components. Its linear and diagonal-quadratic equations are

`sum_j a_j=8-5t`,       `sum_j a_j^2=13-10t`.

If t=0, these equations contradict `a_j^2=a_j (mod 2)`. Thus t=1,
and the remaining entries sum to3 and have squared sum3: precisely
three of them are1. Conversely a size5 row can meet at most one size2
component, since each such interface contributes10 to its diagonal
moment, whose total is16.

The eight size2 components therefore attach to distinct size5
components. On their index set, S is the adjacency matrix of a cubic
simple graph on8 vertices, and the external return matrix is `10I8`.
Equation (3) becomes

`S^2+S=I8+2J8`.

Its seven-dimensional contrast space would satisfy `x^2+x-1=0`,
impossible because the irrational conjugate roots must have equal
multiplicities. Hence the entire `(2^8,5^9)` size pattern is excluded
already at the quotient level.

This last application is one size pattern, not a classification of
the65 norm-screen survivors. No one-by-one sweep of those patterns
was performed.
