# Order61: a size-two interface capacity obstruction

## Statement and scope

There is no actual order61 defect-component quotient with size multiset

`(2^8,5^5,10^2)`.

In fact the contradiction already follows from nonnegative integer
quotient entries, the row sums, detailed balance, diagonal quadratic
moments, diagonal handshake conditions and the required trace. No
off-diagonal quadratic equation or adjacency-block lifting is needed.
The proof eliminates this complete size domain, not merely one labeling
or a subset of its interfaces.

Status: root/writer checked, pending the current mechanism's next review.
No new computation, solver, MCP call or graph enumeration was used.
Previously reviewed manuscripts and the stored enumeration results are
unchanged. This note belongs to
`dd82-v3-defect-components61-20261013` and applies the already-read
formula-derivation/proof-writer skills with the V3 DD82 adaptation.

## 1. Exact row resources

Use the actual quotient from
[GENERAL_THREE_DEFECT_COMPONENT_QUOTIENTS.md](GENERAL_THREE_DEFECT_COMPONENT_QUOTIENTS.md).
For a component i of size n_i, write `d_i=q_ii`. The row sum and the
diagonal entry of the quotient polynomial give

`sum_(j!=i) q_ij = 8-d_i`,
`sum_(j!=i) q_ij q_ji = n_i+11-d_i^2-d_i`.                      (1)

Detailed balance is `n_i q_ij=n_j q_ji`. Entries between equal-size
components are symmetric. All entries are nonnegative integers.

There are fifteen components, so the required trace is
`8-(15-1)/2=1`. Hence exactly one diagonal entry is1 and all others
are0. The five size5 components all have diagonal0, since the actual
induced-graph handshake condition requires `5d_i` to be even. The
unique diagonal1 is therefore initially allowed only on a size2 or
size10 component.

For a size2 component, every positive interface to a size5 component
has entries `(q_ij,q_ji)=(5,2)`, and every positive interface to a
size10 component has entries `(5,1)`. Indeed balance requires those
ratios, and the row bound8 excludes positive multiples larger than1.
Each uses five units of its outgoing row sum, so at most one such
external interface is possible. Their respective contributions to
the quadratic moment in (1) are10 and5.

## 2. Every diagonal-zero size2 component requires one size5 interface

Let i have size2 and diagonal0, and let a_j be its entries to the
other size2 components. Its row and quadratic totals are8 and13.

If it has no interface to sizes5 or10, then

`sum a_j=8`,       `sum a_j^2=13`,

contradicting `a_j^2=a_j (mod 2)`.

If its unique external interface goes to size10, then

`sum a_j=3`,       `sum a_j^2=8`,

again contradicting parity. Consequently its unique external
interface must go to a size5 component. Its remaining moments are

`sum a_j=3`,       `sum a_j^2=3`.

For nonnegative integers, this forces exactly three entries equal
to1 and all other entries zero. Thus every diagonal-zero size2
component demands one size5 interface and has only unit interfaces
to other size2 components.

## 3. A diagonal-one size2 component is impossible

Suppose instead that i has size2 and diagonal1. Its row and quadratic
totals in (1) are7 and11.

An external size5 interface would leave
`sum a_j=2`, `sum a_j^2=1`, impossible because `a_j^2>=a_j` for
nonnegative integers. An external size10 interface would leave
`sum a_j=2`, `sum a_j^2=6`, impossible because
`sum a_j^2 <= (sum a_j)^2=4`.

Thus it has no such external interface and

`sum a_j=7`,       `sum a_j^2=11`,
`sum a_j(a_j-1)=4`.

The last identity forces exactly two entries equal to2, no entry
at least3, and all remaining positive entries equal to1. The first
identity then forces three unit entries. Each of the two double
interfaces is symmetric, since its two components both have size2.
Its other endpoint cannot have diagonal0, because Section2 proved
that every such endpoint has only unit interfaces inside the size2
group. It would therefore be a second diagonal-one component,
contradicting the total trace1.

Hence all eight size2 components have diagonal0.

## 4. Demand exceeds the receiving capacity

By Section2, all eight size2 components require one interface to a
size5 component. A size5 row has diagonal0 and quadratic moment
`5+11=16`. Each interface from a size2 component contributes10
to that moment. It can therefore receive at most one such interface.

There are only five size5 components, giving total capacity at most5
for eight required interfaces. This contradiction proves the claim.

## Reusable mechanism

The proof combines three shared constraints without choosing any
particular quotient: detailed balance fixes the smallest possible
interface costs; row sums and diagonal quadratic moments force a
small component's permitted row types; symmetry between equal-size
components rules out an exceptional type; finally the remaining
mandatory demand exceeds the aggregate quadratic-moment capacity of
the receiving components.

The numerical forcing in Sections2--4 is proved here only for
`(2^8,5^5,10^2)`. No assertion is made that every other screened size
domain satisfies the same demand or capacity bounds.
