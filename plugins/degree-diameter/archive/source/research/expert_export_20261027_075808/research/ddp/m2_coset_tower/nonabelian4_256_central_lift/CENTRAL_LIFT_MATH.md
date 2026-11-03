# Exact central-lift coverage for the four-orbit Q64 construction

## Target and status

**COHERENT AS STATED.** Fix all projected D32 edge voltages and derive
the exact diameter-three coverage objective as a function of thirteen
central bits. This note proves the walk formulas, the affine bad sets,
and the distinct-matching constraints. It performs no bit enumeration,
coordinate search, graph generation, or BFS.

The base and edge numbering are those in
`../nonabelian4_256_capacity/topology.json`: cross multiplicities
(3,3,2,2,3,3), tree edges [0,3,6], and free edges

    [1,2,4,5,7,8,9,10,11,12,13,14,15].

There are sixteen base matchings, four vertex orbits, and eight outgoing
darts at each base vertex. The intended simple lift is eight-regular
on 256 vertices.

## 1. Group, quotient, and coordinates

Write

    Q64 = {(x,s): x in Z32, s in F2},
    (x,s)(y,t)=(x+(-1)^s*y+16*s*t mod32, s xor t).

Let c=(16,0). It is central and has order two. Quotienting by <c>
gives D32 with coordinates (a,s), a in Z16, and multiplication

    (a,s)(b,t)=(a+(-1)^s*b mod16, s xor t).

For a projected element (a,p), choose the representative
h^0=(a,p) in Q64 with the integer a in {0,...,15}. The actual edge
voltage is

    h_e=h_e^0*c^(z_e)=(a_e+16*z_e,p_e),   z_e in F2.

All sixteen projected voltages are fixed. The three tree voltages are
the identity in Q64, so their central bits are zero; the other thirteen
bits form z in F2^13, in the free-edge order above.

This is a complete normalized central-lift range. If tree edges above
the fixed identity projection initially carry c rather than e, central
coordinate relabeling at the four base vertices removes their three
bits. It leaves every projected voltage unchanged and transfers the
bits into the free edges. Fixing the root vertex relabeling to e makes
this tree normalization unique. Thus no further central-bit gauge
is being silently omitted.

The chosen representatives h^0 are a section, not a homomorphism.
Baseline word constants must be computed using actual Q64 products
and inverses. In particular,

    (x,0)^(-1)=(-x mod32,0),
    (x,1)^(-1)=(x+16 mod32,1).

Carries from the representative interval 0,...,15 also contribute to
the central bit. A computation only in D32 cannot recover them.

## 2. Every word gives an affine Boolean form

Let w be a directed base walk of length at most three. Each step uses
one of the sixteen named edges, in either direction. The group identity

    (h_e^0*c^(z_e))^(-1)=(h_e^0)^(-1)*c^(z_e)

holds because c is central and c^(-1)=c. Consequently,

    value_w(z)=value_w(0)*c^(m_w dot z),

where m_w in F2^13 records the parity of the number of occurrences of
each free edge. **Direction does not change this coefficient.** An edge
occurring twice cancels from m_w, irrespective of its two directions.

Suppose the projected endpoint is (a_w,p_w), with a_w in 0,...,15,
and the actual baseline product is

    value_w(0)=(a_w+16*beta_w,p_w).

Then the lifted endpoint's central bit is exactly

    ell_w(z)=beta_w xor (m_w dot z).

The endpoint projection is fixed by the projected voltage assignment.
Only this affine Boolean bit depends on the thirteen lift choices.

The empty walk has endpoint identity, mask zero, and beta=0. Only an
immediately inverse dart of the same named edge may be removed when
enumerating walks. The lengths 0,1,2,3 give 1,8,56,392 walks per root.

### Projected parallel edges must retain their names

Distinct base matching IDs must remain distinct during this word
enumeration, even when their projected group voltages coincide. A
forward step on edge e followed by the inverse of a different edge f
is not an immediate inverse-dart cancellation.

For example, if h_e and h_f project to the same element and have
different central bits, then

    h_e*h_f^(-1)=c.

This is a genuine length-two route to the other central lift of the
same quotient vertex. Merging projected parallel matchings before
forming the walk masks would lose it. A simple quotient adjacency may
be used for necessary quotient distances, but it is not an adequate
replacement for the named-edge walk list used here.

## 3. The 512 target groups and exact missing count

There are four source representatives (i,e), four target base vertices,
and 32 possible projected group endpoints. Thus there are

    4*4*32 = 512

groups of words. Denote one by alpha=(i,j,a,p), and let F_alpha be its
set of distinct affine forms (m_w,beta_w). Deduplicating these forms
after correct word composition is safe. Each group has exactly two
possible original targets, distinguished by central bit zero or one.

For a fixed z:

- If F_alpha is empty, both targets are missing: contribution 2.
- If F_alpha is nonempty and all its forms evaluate to the same bit,
  exactly one target is missing: contribution 1.
- If its evaluations include both bits, neither target is missing:
  contribution 0.

Here “all forms have one value” is evaluated at the chosen z. The
forms need not be constant functions of z for this event to occur.

Let N_empty be the number of empty groups, independent of z. Let
B_alpha be the set of z for which a nonempty group's forms all have
one value. The exact sum of missing targets over the four roots is

    M(z)=2*N_empty + sum_{alpha: F_alpha nonempty} 1_{z in B_alpha}.

The ordinary simultaneous left Q64 action is a graph automorphism and
is free on each of the four vertex orbits. Therefore, for legal voltages,

    full_bad_unordered_pairs(z)=32*M(z),

where bad means distance greater than three or unreachable. The factor
is |Q64|/2=32. This is exact, rather than a lower bound or an estimate.

Diameter at most three is equivalent to M(z)=0, subject to the
distinct-matching constraints in Section 5. In particular, an empty
group already rules out all central lifts of this fixed projection.

## 4. Each nonempty group's bad set is an affine solution set

Choose any first form (m_0,beta_0) in F_alpha. All forms agree with it
exactly when, for every other form (m_w,beta_w),

    (m_w xor m_0) dot z = beta_w xor beta_0.

Stack these equations into A_alpha*z=b_alpha over F2. Then

    B_alpha = {z in F2^13 : A_alpha*z=b_alpha}.

The choice of the first form does not change this solution set.
This characterization includes all degenerate cases:

- An inconsistent equation system gives B_alpha empty: this target
  group is always fully covered, for every z.
- A consistent rank-r system gives an affine subspace of size 2^(13-r).
- Rank zero and consistent right side gives the whole cube: this group
  always misses one lift. A single distinct form is an instance.
- Equal masks with unequal beta give a row 0=1, so the group always
  covers both lifts. Equal masks and equal beta are redundant forms.

There is no claim that solving each individual system separately
solves the lift problem. D3 requires a legal z **outside the union**
of all these bad solution sets, as well as N_empty=0.

For a group with exactly two distinct forms, full coverage is the
single complementary equation

    (m_1 xor m_0) dot z = 1 xor beta_1 xor beta_0.

Such forced equations can be combined with the legality equations.
For more forms, the general condition is that at least one row of
A_alpha*z=b_alpha fail; replacing that disjunction by an arbitrary
selected complementary equation would incorrectly discard lifts.

## 5. Exact legality of parallel matchings

Compare edges in the same unordered endpoint class, oriented in the
same canonical direction. If their projected voltages (a,p) differ,
their Q64 voltages can never be equal, for any central bits.

If their projected voltages agree, they use the same baseline h^0,
so their actual voltages are distinct exactly when

    z_e xor z_f = 1.

A tree edge's bit is the fixed constant zero. Thus a free edge sharing
its identity projection must have central bit one.

Three or more edges in one endpoint class with the same projection
cannot be lifted to three distinct group voltages: that projected
element has only two preimages. Equivalently, demanding pairwise
inequality for three bits is inconsistent over F2. Such a projected
assignment has no legal distinct-matching lift.

Conversely, if every equal-projection cluster has size at most two,
the displayed pair equations are the complete legality conditions.
Each base edge belongs to only one such cluster. In the present
spanning tree there is at most one tree edge per endpoint class, so
there is no cluster of two fixed tree bits. The remaining equations
are independent, on disjoint free-bit supports. If there are d
duplicated-projection pairs, the legal center choices form an affine
space of dimension 13-d.

Thus **a repeated projected matching is allowed and must not be
pre-excluded**. Its two lifts are valid precisely when their center
bits differ. The resulting two-step central route described above
can be useful for coverage.

One may express the legal choices as z=z_*+T*t. A bad-set equation
then becomes

    A_alpha*T*t = b_alpha + A_alpha*z_*.

If this restricted system is inconsistent, the group is covered by
every legal lift. If it is identically satisfied, every legal lift
misses one target in that group. Restricting to the legal affine
space therefore preserves the exact objective and can simplify it.

## 6. Self-target pairs automatically handled by the formulas

For a word returning to its source base vertex with odd quotient
phase, reverse the word. Its Q64 endpoint is the inverse, differing
by c. The occurrence mask is unchanged, while beta is toggled. Hence
every reachable self/odd quotient target has two forms with identical
masks and opposite beta, so its bad solution set is empty.

If the quotient target is unreachable, the group is empty and misses
both lifts. This recovers the earlier exact self/odd modulo-16 rule:
central bits cannot alter self/odd coverage at a fixed projection.

The same inversion observation applies to the self-target quotient
element (8,0): its Q64 lifts (8,0) and (24,0) are mutual inverses and
also differ by c. It does not apply to the identity quotient element,
whose lifts e and c are each self-inverse. A duplicated projected
matching pair, however, supplies a separate legal length-two route
to c and makes that self/identity group fully covered.

These consequences are already encoded by the affine bad-set systems;
they require no separate graph assumption or extra enumeration.

## Scope and remaining decision

The criterion is exact for every fixed projected assignment on this
base, with all normalized central lifts retained. It allows duplicate
projected matchings when they admit distinct lifts. It includes the
baseline Q64 cocycle and carries, so it does not treat Q64 as a direct
product of D32 and C2.

The unresolved construction step is to find a projected assignment
whose legal central-bit space has a point outside all nonempty bad
sets. No such point, no infeasibility claim for a new projection, and
no actual graph has been produced in this paper-only task. In
particular, the old best's 8192 central assignments were not enumerated.
