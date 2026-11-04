# Full Q5 endpoints add the ten-hole row (4,5)

2026-11-01. Conditional application; fresh independent review pending.

Use the accepted uniform transfer with a covered target $v$, five holes
of each parity, free root $u=0$, and independent remaining holes $Z\cup W$.
Suppose the target face A contains all four vertices of Z and all five
vertices of W. Then $(a,b)=(4,5)$ and no bridge source is consumed.

If $u\in A$, pair the crossing ports and use $r=u$. If $u\notin A$,
the original short internal matching in A has one more even port than
odd ports, so choose an even port as $r$ and pair the others. In both
cases the A completion has exactly five holes of each parity with free
root $r$. The full balanced-hole Q5 endpoint theorem, conditional on
accepted A10 assembly, gives a Hamilton $r$--$v$ path. This is exactly
the even-consumption branch with $s=0$ of the uniform transfer; only
the previously limited local endpoint input is extended to ten holes.

The B hole counts after tagging and transfer are $(0,0)$; there are no
conflicts to suppress or marked holes to omit. Apply the arbitrary
perfect-matching cycle theorem on B. Expand transferred paths and delete
the tag to obtain the required Hamilton $u$--$v$ path containing the
original short matching. If the original crossing set is empty, use
the already imported five-direction endpoint theorem as before.

`ten_covered_full_q5_endpoint_filter.py` scans the accepted 54222 residual
records and stores a real cut witness for each record with this row.
There are 10/30/30 at targets 1/7/31, so 70 new geometries, leaving
54152 before any new T63 application. All 70 belong to the separate
T63 candidate residual; thus they are disjoint from that route's 12916
new records. The exact intersection residual after both accepted routes
would be 12910/12696/15630, total 41236.

The producer writes exact remaining bytes and SHA-256 pins. A fresh
checker must independently replay the row witnesses and residual sets.
Neither numerical subtraction nor a producer report alone accepts the
combined coverage. Complete ten-hole and P6 remain open.
