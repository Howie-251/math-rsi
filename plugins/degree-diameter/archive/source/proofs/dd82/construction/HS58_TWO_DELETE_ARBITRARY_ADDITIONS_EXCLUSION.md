# HS58: at least three original HS edges must be deleted

Date: 2026-10-12. Computer-assisted mathematical construction-family
exclusion, with pure combinatorial arguments closing the final branches.
This is not an exclusion of arbitrary 58-vertex graphs or a Lean theorem.

## Statement

Let Q be the Hoffman–Singleton graph on fifty old vertices. Add eight
new vertices, arbitrary old-new edges and an arbitrary new-vertex graph.
Among the old vertices allow arbitrary additions of original nonedges,
but delete at most two original Q edges. The resulting simple graph
cannot have maximum degree eight and diameter at most two.

Equivalently, any successful 58-vertex construction with such a specified
HS base must delete at least three original edges. Its additions and its
eight-vertex auxiliary graph are unrestricted in this conclusion.

## Exhaustion of the remaining cases

Every target on 58 vertices is eight-regular: a vertex of degree at most
seven reaches at most 1+7+7*7=57 vertices in distance at most two.

The case of zero or one original deletion, including arbitrary additions,
is already closed by
[HS58_ONE_DELETE_ARBITRARY_ADDITIONS.md](HS58_ONE_DELETE_ARBITRARY_ADDITIONS.md),
with its explicitly documented finite-computation dependencies.

For exactly two deletions, write a for the addition count,
p_v=1+d_D(v)-d_A(v) for the attachment count, and
E=sum_v max(p_v-1,0). The complete earlier assembly in
[HS58_TWO_DELETE_SIX_ADDITION_REMAINDER.md](HS58_TWO_DELETE_SIX_ADDITION_REMAINDER.md)
leaves only the following possibilities:

| Deletions | Additions | Excess endpoints |
|---|---:|---|
| D={tu,vw} disjoint | six, forming a matching | t,u both full; v,w have one port |
| D={tu,wv} disjoint | six, forming a matching | t,u,w full; v has one port |

Full means two ports and no added edge at that deletion endpoint.
This assembly covers all addition counts, both adjacent and disjoint D,
and all original adjacencies between the deletion endpoints. No H or
attachment labels have been fixed.

The first row is excluded by
[HS58_A6_TWO_FULL_EXCLUSION.md](HS58_A6_TWO_FULL_EXCLUSION.md).
Lost old paths force at least three ordinary neighbors to repeat the
singleton label c in the no-cross case, and at least four in the cross
case after exchanging the two nonfull endpoints. Hence d_H(c)<=4 or
<=3. The other nonfull endpoint obtains at most two labels through old
intermediaries, so it reaches at most 1+4+2=7 or 1+3+2=6 new vertices.

The second row is excluded by
[HS58_A6_THREE_FULL_EXCLUSION.md](HS58_A6_THREE_FULL_EXCLUSION.md).
Its repeated-label degree count bounds the new vertices reachable from
the sole nonfull endpoint by 7,6,7 in the no-cross, cross-at-full, and
cross-at-nonfull cases. Both final exclusions are pure counting proofs;
no additional solver input or enumeration was needed to finish them.

## Computational dependencies and scope

The complete proof remains computer-assisted. Lower addition counts use
the checked joint formulas and finite auxiliary domains assembled in
[HS58_TWO_DELETE_FIVE_ADDITIONS_EXCLUSION.md](HS58_TWO_DELETE_FIVE_ADDITIONS_EXCLUSION.md).
The last saturated case uses the complete four-zero-set/56-addition
domain and one checked joint free-B/H formula in
[HS58_A6_SATURATED_JOINT_COMPLETION.md](HS58_A6_SATURATED_JOINT_COMPLETION.md).
The complete deletion-orbit checks are linked by those reports. Broad
UNKNOWN and OUTPUT_LIMIT inputs are not nonexistence evidence.

Root read the final proofs, saturated source/input metadata, result and
independent certificate log. The last two-full proof additionally received
an independent agent's full path-and-count check. These are local checks;
external review and Lean formalization remain distinct pending items.

An arbitrary target graph need not contain a near-HS fifty-vertex core.
General orders 58–61 remain open, and 57<=N(8,2)<=61 is unchanged.
