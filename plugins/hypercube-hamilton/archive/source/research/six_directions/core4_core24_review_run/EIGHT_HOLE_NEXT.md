# Next full P6 layer: eight holes

Date: 2026-11-01. Full six-hole P6 is now established by A4 closure and the
earlier reductions, relative to their stated theorem imports and finite
certificates. This file is a research handoff, not an eight-hole proof.

## Exact eight-hole target

For every short matching M of Q6 with 28 edges, every free root u and
every opposite-parity target v, construct a Hamilton u--v path containing M.
Both free and covered targets must be included. No matching-size sampling
or local cut restriction replaces this quantifier.

## Reductions now available

If two holes other than u are adjacent, add their short edge. The result
has six holes and still leaves u free, so SIX_HOLE_CLOSED applies. Thus
the remaining seven nonroot holes can be assumed pairwise nonadjacent.

If v is free and adjacent to u, add uv to M. This gives a six-hole short
matching. The six-hole theorem gives a Hamilton circle containing this
matching: take a remaining free root, find its Hamilton path to a short
neighbor, and close that path. Deleting uv yields the desired u--v path.

If v is covered, the existing swap M*=M-vh+hu, h=M(v), changes the hole
parity counts from 4/4 to 3/5 (including v in the larger class). The edge
hu may be long and same-parity; all applications must preserve it until
the final deletion/append restoration. The six-hole SHORT-matching theorem
cannot be applied directly to arbitrary long-edge auxiliary matchings.

## Candidate next Q5 input, not yet proved or known sufficient for all eight holes

Define A6 as follows: every matching of K(Q5) with six holes, two of one
parity and four of the other, extends to a 31-cycle avoiding any specified
hole of the larger class, with all new edges short.

An adjacent pair consisting of a minority hole and a majority hole other
than the forbidden one reduces immediately to the now proved A4 by adding
that short edge. Remaining A6 geometries have no such pair.

A6 would imply the balanced six-hole endpoint property K6 on K(Q5): a free
root r can connect to any opposite-parity y. If y is covered, swap yk to
kr, obtaining a 2/4 hole matching with y in the majority; use A6 avoiding
y, delete kr, append original ky. If y is free, add auxiliary ry, leaving
balanced four holes; the already established K4 implies a full circle
for that four-hole matching, and deleting ry gives the desired path.
These are conditional reductions, not a proof of A6 or complete eight-hole P6.

The general Q4 lemmas in Q4_GENERAL_AUGMENTATION.md provide arbitrary
balanced-hole paths/circles and arbitrary parity-difference-two avoided
circles. They are available as lower-dimensional inputs when deriving
new Q5 transfers. Before committing to A6 as the next sufficient core,
prove the exact eight-hole reduction and check all its geometric cases.

## Full goal remains

Even an eight-hole theorem would leave the 10,12,14,16,18-hole rooted-maximal
levels. Full P6 must remain marked unproved until every remaining level
and every endpoint condition is proved and reviewed.
