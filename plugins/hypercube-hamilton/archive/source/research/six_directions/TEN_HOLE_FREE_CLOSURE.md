# Ten-hole P6 with both endpoints free

2026-11-01. ARIS proof-writer. Proposed complete proof relative to the
listed imports and a finite hole-geometry census; independent review pending.
The covered-target ten-hole branch and full P6 remain open.

## Exact claim

For every short 27-edge matching $M$ of $Q_6$, every free root $u$, and
every free target $v$ of opposite parity, there is a Hamilton $u$--$v$
path containing every edge of $M$. Only short new edges are used.

## Imports and dependency map

1. Full eight-hole P6, including covered targets, from
   `EIGHT_HOLE_FULL_CLOSURE.md` and its final independent review.
2. The unified cut transfer in `HIGHER_HOLE_UNIFIED_TRANSFER.md`, including
   its eight unconditional ten-hole rows and its marked T15 rows. This new
   transfer must itself pass independent review before this claim is accepted.
3. The 24 complete marked T15 cores accepted in the final eight-hole review:
   $\{0,1,2,4,5,7,8,10,13,14,15,18,19,21,23,24,25,27,31,32,35,37,38,44\}$.
   IDs refer to `t15_analytic_geometry.json`; all required matchings are
   arbitrary complete-graph matchings, and both specified omissions matter.
4. The full geometric T15 split case in `Q4_RICH_GLUING.md`, with accepted
   independent `Q4_RICH_GLUING_REVIEW.md/.json`. After translating the minority
   hole to 0, this case has a coordinate with exactly two of the five odd
   holes in its one-face and with the two omitted holes in different faces.
   It applies at both positive and zero original crossing counts.
5. Adjacent minority/included-hole augmentation to T44_5 is also permitted
   by the lookup, but does not occur in the independent input domain here.

No unrestricted T15 theorem, higher-hole P6 theorem, or matching sample
stands in for these imports. The finite work below is geometry coverage;
the full matching quantifiers are supplied by the imported local theorems.

## 1. Endpoint-symmetric short augmentation

Suppose two free vertices $x,y$ of $M$ are adjacent.

If $\{x,y\}\ne\{u,v\}$, at least one of $u,v$ remains free after adding
$xy$. Apply full eight-hole P6 to $M+xy$, rooted at that still-free endpoint
and targeted at the other endpoint. The other endpoint may now be covered,
which is explicitly allowed by the eight-hole import. Reverse the path if
necessary. It contains $M$ and has the required endpoints.

If $xy=uv$, apply full eight-hole P6 to $M+uv$ with any remaining free root
$r$ and a short neighbor $s$ as target. Close the Hamilton $r$--$s$ path
by the short edge $rs$. This edge cannot already be the endpoint edge of
a path on 64 vertices; it is also not a matching edge since $r$ is free.
The resulting Hamilton cycle contains $M+uv$. Delete $uv$ to obtain the
required $u$--$v$ path containing $M$.

Therefore the only new domain has **all ten holes independent**, including
both endpoints. Translate $u$ to 0, write the other even holes as $Z$ with
$|Z|=4$, and the odd holes as $W$ with $|W|=5$ and $v\in W$. A coordinate
permutation takes $v$ to 7 or 31 according to its distance 3 or 5 from 0;
distance 1 is excluded by independence.

## 2. Sufficient cuts tested on the independent domain

For every coordinate put A on the target side and calculate
$a=|Z\cap A|$, $b=|W\cap A|$.

The eight universally sufficient rows are

$$ (1,2),(2,3),(2,2),(3,3),(1,3),(2,4),(4,3),(2,5). $$

Otherwise use the two T15 rows:

* For $(a,b)=(3,2)$, choose any two of the three A even nonroot holes as
  bridge sources. The sole B nonroot even hole is the T15 minority; the
  three B odd holes are its included majority holes; the two bridge mirrors
  are its marked omissions.
* For $(a,b)=(1,4)$, choose any two A odd holes excluding the free target
  and any hole mirrored to the root. The sole B odd hole is the minority;
  the three B nonroot even holes are its included majority holes; the
  bridge mirrors are its two marked omissions.

Translate each B vertex by the minority and delete the cut coordinate.
This actual cube isomorphism normalizes the minority to 0 and all five
majority holes to odd labels of $Q_5$. Accept a choice only when it belongs
to one of the 24 audited marked cores, or the audited split case above.
The unified transfer supplies the full global path for every realizing
original matching of any geometry with such a choice.

## 3. Finite coverage obligation and producer evidence

The finite assertion to be independently checked is:

> Every set $\{0\}\cup Z\cup W$ of ten independent vertices of $Q_6$,
> with $|Z|=4$ even, $|W|=5$ odd, and target $v=7$ or $31$ in W,
> has a sufficient row or an accepted marked T15 choice from Section 2.

Producer files `higher_hole_geometry_census.cpp`,
`higher_hole_t15_lookup.py`, and `higher_hole_t15_filter.cpp` enumerate the
larger domain where only $Z\cup W$ is independent. There are 56805 residual
free-target geometries for $v=7$ after the eight basic rows, all handled
by accepted T15 choices. For $v=31$ the corresponding count is 51935;
51875 have accepted T15 choices. Each of the remaining 60 has a member
of W adjacent to root 0, and hence was already handled by Section 1.
No infeasibility exclusion is used in these free-target counts.

These producer counts are supporting diagnostics, not independent proof
certificates by themselves. The reviewer must independently regenerate
the complete independent-hole domain, reconstruct the actual marked
projections and accepted orbit maps, and confirm that no input remains.
No extrapolation from a random matching or from one Hamilton witness is used.

## 4. Conclusion and limits

Once the precise finite assertion in Section 3 and the new transfer are
independently accepted, Sections 1--2 prove the exact free-target ten-hole
claim. This does not prove ten-hole covered targets, any complete 12--18-hole
layer, full T15, or full P6. Those obligations remain in the active goal.
