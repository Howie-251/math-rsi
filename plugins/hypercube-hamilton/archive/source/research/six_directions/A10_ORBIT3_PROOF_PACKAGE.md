# A10 final five-geometry orbit: reduction and current obstruction

2026-11-01. ARIS proof-writer exploration. This package is a producer
document and requires a different fresh proof-checker for semantic acceptance.

## Claim

Let $F$ be any matching of $K(Q_5)$ with holes

$$H=\{0,1,2,4,8,15,23,27,29,30\}.$$

The desired assertion is a simple cycle on precisely $Q_5\setminus\{0\}$,
containing $F$, with every edge outside $F$ short. All eleven required
edges may be long or join equal parities. The marked coordinate orbit has
five geometries. The original assertion is preserved unchanged.

## Status

**NOT CURRENTLY JUSTIFIED.** No full closure or small certified remainder
has been derived in this package. The results proved below are structural
reductions, exact obstructions to specific stitching templates, and a
conditional exchange lemma. They are not counterexamples to A10.

## Assumptions and notation

Use the accepted complete Q5 A8 theorem and accepted K8 only where explicitly
stated. The previously accepted first A10 orbit does not contain this marked
geometry and is not silently applied here. The prospective local-cycle
approach uses GQ4-avoid on the target face. No additional condition is imposed
on $F$.

The majority holes are $\{0,15,23,27,29,30\}$ and the minority holes are
$\{1,2,4,8\}$. Let $V=\{0,\ldots,31\}$ and $K=V\setminus H$.
For a cut bit $b$, let $A$ be its zero face and $B$ its one face. For an
original A hole $t$, its short mirror is $t\mathbin\oplus b$.

## Proof strategy and dependency map

1. Establish why the direct coordinate-face GQ4 bridge constructions do
   not yield the closed-set restrictions used in earlier successful orbits.
2. Normalize a mandatory long edge at vertex $31$ under the exact marked
   stabilizer, obtaining five fixed-edge families with full matching scope.
3. Record a valid short-edge exchange criterion using complete A8. Its
   universal witness-existence statement remains the exact open step.

The standalone producer `A10_ORBIT3_geometry_check.py` verifies the bit
identities, marked orbit, stabilizer, partner orbits and finite counts. It
does not enumerate original matching instances or establish cycle existence.

## Proof

### 1. Covered support and a mandatory long edge

The covered even vertices are exactly the ten weight-two vertices. The
covered odd vertices are the ten weight-three vertices together with
$16$ and $31$. Consequently, if $o$ and $e$ denote the numbers of odd--odd
and even--even required edges, counting covered endpoints gives

$$2o+x=12,\qquad 2e+x=10,\qquad o-e=1.$$

Thus at least one odd--odd required edge exists. Moreover

$$N(31)=\{15,23,27,29,30\}\subset H.$$

The required partner $F(31)$ is covered, so the edge incident with $31$
is necessarily long. This is a universal fact about every input, not a
restriction to a special finite family.

### 2. Why the direct target-face bridge template is blocked

Every zero face $A$ has exactly two original majority holes, including $0$.
For $b\in\{1,2,4,8\}$ it has three minority holes; for $b=16$ it has four.
To use GQ4-avoid after pairing all ports and selected hole sources, the
remaining majority-minus-minority hole excess must be two. If $p$ majority
and $q$ minority holes are consumed, this requires

$$2-|H\cap A\cap\mathrm{odd}|-p+q=2.$$

Since $q$ cannot exceed the number of minority A holes, it follows that
$p=0$ and every minority A hole must be selected. Hence the corresponding
mirror set $Y$ is forced in this template.

| $b$ | Forced $Y$ | B vertex preventing a cycle on $B\setminus Y$ | Available short neighbors there |
|---:|---|---:|---|
| $1$ | $3,5,9$ | original hole $1$ | $17$ only |
| $2$ | $3,6,10$ | original hole $2$ | $18$ only |
| $4$ | $5,6,12$ | original hole $4$ | $20$ only |
| $8$ | $9,10,12$ | original hole $8$ | $24$ only |
| $16$ | $17,18,20,24$ | original covered vertex $16$ | none |

For the first four cuts the displayed singleton is an original B hole.
It remains a hole of the compressed required matching and is not omitted.
It would need two distinct new short incident cycle edges but has only
one available short neighbor. Therefore that local extension is impossible.

For the final cut, vertex $16$ is originally covered. If the transfer and
compression yielded a B matching, it would cover $16$ with one required
edge. Every other incident cycle edge would have to be short. All its
in-face short neighbors are in $Y$, so no second edge is available. That
local extension is also impossible.

These statements concern only the specific template in which all selected
mirrors are suppressed and omitted on the second face. They do not imply
that the global input is negative. In particular one cannot infer a useful
matching-closed set by treating every such local failure as a fixed-edge
obstruction: the failure already occurs independently of the matching.

### 3. Exact fixed-partner normalization

The coordinate permutations preserving $H$ and the specified omission $0$
are exactly the permutations of the four coordinates $1,2,4,8$, with bit
$16$ fixed. The group has order $24$ and fixes $31$.

Its action on the possible partners of $31$ has five orbits:

| Partner representative | Full partner orbit | Stabilizer order |
|---:|---|---:|
| $3$ | $3,5,6,9,10,12$ | $4$ |
| $7$ | $7,11,13,14$ | $6$ |
| $16$ | $16$ | $24$ |
| $17$ | $17,18,20,24$ | $6$ |
| $19$ | $19,21,22,25,26,28$ | $4$ |

For any original matching, choose a marked coordinate permutation taking
its actual partner of $31$ to one of these representatives. The remaining
twenty vertices have an arbitrary perfect matching; no other original edge
is constrained. Therefore proving the desired conclusion separately for
these five fixed-edge families suffices for the full marked orbit.

For each fixed partner there are

$$19!!=654729075$$

remaining matchings before further symmetry. The complete unnormalized
domain has

$$21!!=13749310575$$

matchings. A Burnside calculation on the marked stabilizer gives exactly
$572977731$ matching orbits. This is still too large to describe as a small
finite remainder, and no such large certificate run is asserted or launched.

For completeness, the fixed-matching count for a permutation is computed
from its cycle counts $m_\ell$ on the covered support. Distinct vertex cycles
can be matched equivariantly only if their lengths agree; two length-$\ell$
cycles have $\ell$ equivariant pairings. A single cycle can match internally
only for even $\ell$, uniquely by antipodal pairing. Thus an odd-$\ell$ group
contributes zero if $m_\ell$ is odd, and otherwise contributes

$$\frac{m_\ell!}{2^{m_\ell/2}(m_\ell/2)!}\ell^{m_\ell/2}.$$

An even-$\ell$ group contributes

$$\sum_{r=0}^{\lfloor m_\ell/2\rfloor}
\frac{m_\ell!}{(m_\ell-2r)!2^r r!}\ell^r.$$

Multiply over lengths and average over the $24$ permutations. The producer
also checks that the sum of the corresponding five partner-stabilizer
orbit counts equals this same result. These counts concern symmetry only;
they supply no positive cycle witnesses.

### 4. A valid A8 exchange criterion

Choose a majority hole $z\ne0$ and a minority hole $w$. Their edge is not
short, but $F^+=F\cup\{wz\}$ is a legitimate arbitrary matching with
$6-1=5$ majority and $4-1=3$ minority holes, an exact A8 input.
Apply full A8 with omitted majority hole $0$ to obtain a cycle $C$ containing
$F^+$, with only short edges outside $F^+$.

Orient the cycle so that the artificial edge is directed $w\to z$.
Suppose some other directed cycle edge $a\to b$ satisfies

$$ab\notin F^+,\qquad wa\in E(Q_5),\qquad zb\in E(Q_5),$$

with $w,z,a,b$ distinct. In cyclic order the four endpoints occur as
$w,z,\ldots,a,b,\ldots,w$. Remove $wz,ab$ and insert $wa,zb$.
The two residual paths have endpoints $(z,a)$ and $(b,w)$; the inserted
edges join them into one simple cycle on the same $31$ vertices. Every
edge of $F$ is retained because $ab$ was optional. The only artificial
long edge $wz$ disappears, and both replacement edges are short. This
proves the desired extension for every input admitting such a witness.

The existence of a suitable $C,a,b$ is an additional condition. Full A8
alone does not promise an optional edge in these locations or its correct
orientation. No optional-edge-union or path-orientation theorem has yet
been proved to discharge this condition for all five fixed-partner families.

## Corrections or missing assumptions

The original universal claim remains open in this package. A sufficient
new lemma would be: for every original matching, some choice of $w,z$
has an A8 extension satisfying the directed optional-edge criterion above.
This condition is not assumed true. A different route must either change
the coordinate-face interface so its degree obstruction disappears, or
derive additional sufficient conditions reducing the exact matching domain
to a genuinely small positive-certifiable family.

## Open risks

The producer geometry and Burnside arithmetic require independent checking.
No whole-matching extension sampling, failed Hamilton search, or closed-set
claim unsupported by a local positive theorem is used as evidence of full
closure. This package proves neither the final A10 orbit nor full A10/P6.
