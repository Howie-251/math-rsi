# Proof package: forced triangles close two exceptional EP0 orbits

Date: 2026-11-01. Local ARIS proof-writer package; no global status change.
Independent semantic proof-checker review is still required.

## Claim

For every realizing short matching of either of the following eight-hole
geometries, some $(a,b)=(2,0)$ cut satisfies EP0 as defined in
`EIGHT_HOLE_COVERED_NEXT_DRAFT.md`:

| Odd target $v$ | Nonroot even holes $Z$ | Odd holes $W$ | Normalized orbit size |
|---:|---|---|---:|
| $1$ | $3,5,9$ | $14,31,47,62$ | $10$ |
| $7$ | $15,23,39$ | $56,59,61,62$ | $1$ |

The even free root is $u=0$. The conclusion transports under every cube
automorphism preserving the normalized root and target. Thus this closes
the **EP0 obligation for 11 of the 50 exceptional normalized geometries**.
It does not close their eight-hole Hamilton-path conclusion without the
corresponding T15 instances. Five EP0 orbits, containing 39 normalized
geometries, remain open by this route.

## Status

**PROVABLE AS STATED**, relative to the imported N10 theorem, for the above
two-orbit EP0 statement. The original universal seven-orbit EP0 problem is
**NOT CURRENTLY JUSTIFIED**. Full eight-hole extension and full P6 remain open.

## Assumptions and notation

The cube is the short-edge graph on binary integers $0,\ldots,63$;
$d(x,y)$ is the number of differing bits. All original edges belong to
this cube. The matching $M$ covers exactly the complement of
$H=\{0\}\cup Z\cup W$. Write $O$ for odd-parity vertices.

In cut coordinate $i$, $A$ is the face containing $v$, $B$ its opposite,
$X_A$ the endpoints in $A$ of matching edges crossing the cut, and $M_A$
the original edges internal to $A$. The short mirror is
$\bar x=x\mathbin{\oplus}2^i$. Put $S=\{\bar w:w\in W\}$.
The two members of $Z\cap A$ are $z_1,z_2$.

N10 is imported at its existing scope from `GENERAL_NEAR_PERFECT.md`:
a matching of $K(Q_5)$ with holes $r,q$ extends, using short new edges,
to a Hamilton $r$--$v$ path whenever $v\ne r$ has the parity of $q$.
It permits arbitrary long and same-parity edges in an auxiliary matching.
No optional-edge strengthening of N10 is assumed.

## Proof strategy and dependency map

1. A fixed-cut lemma forces an optional edge by adding a triangle-closing
   artificial edge to the input matching before invoking N10.
2. A covered even vertex in each representative has only three covered
   neighbors. Whichever edge matches it selects a cut satisfying that lemma.
3. An independent finite geometry check verifies all asserted adjacencies
   and the sizes of the symmetry orbits. It does not search Hamilton paths.
4. Only a later application of the existing two-bridge transfer imports T15.

## Proof

### Step 1. Fixed-cut forced-triangle lemma

Suppose an $(a,b)=(2,0)$ cut has $0\in A$. Suppose there is an odd
crossing port $q\ne v$ such that

$$N_A(q)\setminus S=\{z_1,z_2\}.$$

Here $N_A(q)$ is the set of five short neighbors of $q$ in $A$.
Then EP0 holds at this cut.

To prove the assertion, set $r=u=0$. Choose a perfect matching $D$ on

$$U=(X_A\setminus\{q\})\cup\{z_1,z_2\}$$

that contains the edge $z_1z_2$. Such a choice is always possible:
$z_1,z_2$ are distinct original holes, hence are outside $X_A$, and
$|X_A|$ is odd. The latter follows because $A$ has 32 vertices and
its original unmatched vertices are precisely $0,z_1,z_2$, so
$32=2|M_A|+|X_A|+3$. After removing $z_1,z_2$, $U$ has the even
cardinality $|X_A|-1$; pair the remaining vertices arbitrarily in the
complete graph. An empty remainder is allowed.

The union $L=M_A\cup D$ is a matching of $K(A)$ with exactly the
two holes $r,q$. Its covered target $v$ is odd and differs from $r$.
N10 gives a Hamilton $r$--$v$ path $P$ containing $L$, with all edges
outside $L$ short.

Since $q$ is a hole of $L$ and $q\notin\{r,v\}$, its two path edges
are distinct short edges. If neither meets $S$, the displayed neighbor
identity forces both $qz_1$ and $qz_2$ into $P$. The edge $z_1z_2$
also lies in $P$ because it belongs to $D$. These three edges form a
triangle, whereas the graph of a Hamilton path is acyclic. This is a
contradiction. Therefore $qs\in E(P)$ for some $s\in S$, exactly the
additional condition required by EP0. This argument establishes the
required existential $D,P$ after the matching and cut are fixed; indeed
every N10 extension for this chosen $D$ has the required edge.

The artificial edge $z_1z_2$ joins two even vertices. It is deliberately
allowed to be long. Treating $D$ as a short or bipartite matching would
invalidate this proof device.

### Step 2. First representative

Let $v=1$, $Z=\{3,5,9\}$, $W=\{14,31,47,62\}$. The even
vertex $h=15$ is covered. Its six neighbors are

$$N_{Q_6}(15)=\{14,13,11,7,31,47\}.$$

The neighbors $14,31,47$ are holes. Thus the unique original edge
covering $h$ is one of $15\!-!13$, $15\!-!11$, $15\!-!7$.
Choose respectively the cut $i=1,2,3$. In each case $h\in B$ and its
partner $q$ is an odd crossing port in $A$. All three cuts have $0\in A$,
exactly two nonroot even holes in $A$, and no odd holes in $A$.
The exact remaining neighbor sets are

| Cut $i$ | $q$ | $N_A(q)\setminus S$ | $N_A(q)\cap S$ |
|---:|---:|---|---|
| $1$ | $13$ | $5,9$ | $12,29,45$ |
| $2$ | $11$ | $3,9$ | $10,27,43$ |
| $3$ | $7$ | $3,5$ | $6,23,39$ |

Each $q$ differs from $v=1$. Step 1 applies to the selected cut, for
every possible realizing matching $M$.

### Step 3. Second representative

Let $v=7$, $Z=\{15,23,39\}$, $W=\{56,59,61,62\}$.
The even covered vertex $h=63$ has neighbors

$$N_{Q_6}(63)=\{62,61,59,55,47,31\}.$$

The first three listed vertices are holes, so $M$ matches $h$ to one
of $55,47,31$. Choose respectively the cut $i=3,4,5$. Again these cuts
have $0\in A$, two nonroot even holes in $A$, and no odd holes there.

| Cut $i$ | $q$ | $N_A(q)\setminus S$ | $N_A(q)\cap S$ |
|---:|---:|---|---|
| $3$ | $55$ | $23,39$ | $51,53,54$ |
| $4$ | $47$ | $15,39$ | $43,45,46$ |
| $5$ | $31$ | $15,23$ | $27,29,30$ |

All three $q$ differ from $v=7$. Step 1 establishes EP0 for the
selected cut, uniformly in $M$.

### Step 4. Finite certificate and symmetry transport

The solver-free program `eight_ep0_fast_route_check.py` constructs
the cube's neighbors from bit flips. It verifies hole independence,
each $(2,0)$ cut, and every neighbor identity needed in Step 1.
It deletes every crossing edge sufficient for that lemma and then
checks Hall obstructions. For the two proved representatives the
vertices $15$ and $63$ respectively become isolated, reproducing the
direct universal argument in Steps 2 and 3.

For the other five representatives it constructs actual 28-edge
matchings avoiding every crossing edge sufficient for this triangle
lemma. These are **not counterexamples to EP0**; they prove only that
the present sufficient rule cannot settle all seven orbits.

Finally, it enumerates all $6!$ coordinate permutations preserving each
normalized target and computes distinct images of $(Z,W)$. The seven
orbit sizes are $10,1,9,9,1,10,10$, summing to $50$. The proved first
and fifth orbits contain $10+1=11$ geometries. Coordinate permutations
preserve matching realizability, parity, shortness, and every quantifier
in EP0. This proves the claimed transported scope. $\square$

## Corrections or missing assumptions

This proof never asserts EP0 for an arbitrary fixed cut. The selected
cut depends on the unique original matching edge at $15$ or $63$.
It does not merely infer a prescribed path edge from an eligible
adjacency; the required edge is forced by an acyclicity contradiction.

In a cut with $0\notin A$, EP0 requires $r$ to be one of $z_1,z_2$.
Then $D$ cannot contain $z_1z_2$. Avoiding $qS$ may force an initial
path $r,q,z_{\mathrm{other}}$ rather than a cycle. The triangle proof
does not apply to such a cut.

## Open risks and exact remaining scope

- The two-orbit EP0 proof imports N10's already recorded external basis.
- The program's PASS checks finite geometry, not the N10 theorem or
  an independently formalized semantic proof.
- For the five remaining orbits, strong-edge-avoiding matching witnesses
  are saved in `eight_ep0_fast_route_check.json`; EP0 remains open.
- Applying the audited two-bridge transfer still requires the resulting
  T15 inputs to be proved. This file establishes no new unconditional
  eight-hole Hamilton-path closure and no full P6 conclusion.
