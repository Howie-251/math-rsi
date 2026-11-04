# Ten-hole covered targets from a marked six-hole split input

2026-11-01. ARIS proof-writer candidate. Independent acceptance pending.

## Claim and status

Relative to the complete Q5 T63 split theorem specified below, the
accepted 54222 remaining ten-hole covered-target geometries have 12916
additional uniformly positive geometries. The remaining set has size
41306. This is a conditional application, not a complete ten-hole or P6
proof, and not an assertion that those 41306 inputs are negative.

## Exact imported statement

Let $L$ be an arbitrary matching of the complete graph on a five-cube,
with exactly six holes $H$, all of one parity. Let $U\subset H$ have
size three. Suppose some coordinate splits $(H,U)$ into counts $(2,1)$
and $(4,2)$. The required imported theorem gives a single cycle on
$Q_5\setminus U$ containing $L$, with all other edges short, for every
such $L$, including those with zero matching edges across that cut.

The proposed full split proof uses Q4 N14 and Q4 T44 for a nonempty
crossing matching. For zero crossing it uses witnessed optional-edge
unions plus a complete finite exceptional gluing domain. This import
must receive its own independent acceptance before the application below
can be counted as closed.

## Reduction to that import

Use the accepted uniform transfer in `HIGHER_HOLE_UNIFIED_TRANSFER.md`.
The original Q6 matching is short with 27 edges; its free even root is
$u=0$, and the odd target $v$ is covered. Write the remaining holes
as even $Z$, $|Z|=4$, and odd $W$, $|W|=5$. The accepted input domain
already has $Z\cup W$ independent. Let $A$ be the coordinate face
containing $v$, and $B$ the other face; put $a=|Z\cap A|$, $b=|W\cap A|$.

For $(a,b)=(4,2)$, choose any three vertices $S\subset Z\cap A$.
The A completion has balanced four holes, so its prescribed endpoint
input is already proved. The B matching after the audited tagged
transfer and simultaneous suppression has hole counts $(0,6)$,
and must omit exactly the three odd mirrors $U=\overline S$.
Its six holes are precisely $(W\cap B)\cup U$.

For $(a,b)=(1,5)$, choose three vertices
$S\subset (W\cap A)\setminus\{\overline u\}$. There are at least four
eligible vertices, because $v$ is covered and hence is not in $W$.
Again the A completion has balanced four holes. The B matching has
hole counts $(6,0)$ and must omit exactly the three even mirrors
$U=\overline S$. Its six holes are precisely $(Z\cap B)\cup U$.

All these are actual distinct holes: the independence reduction excludes
an original hole at a bridge mirror, a free source excludes a crossing
matching port there, and the odd-consumption choice excludes $u$.
The B matching may have long edges; the proposed split theorem explicitly
allows them. Its marked geometry depends only on the holes, cut and
chosen $S$, not on the arbitrary completion matching in A.

Whenever an internal coordinate of B has the marked $(2,1)/(4,2)$ split,
apply the imported theorem to this actual B input. Expanding the
suppressed paths and deleting the tagged $uv$ edge gives a Hamilton
$u$--$v$ path preserving every original matching edge. The expansion
and degree accounting are exactly those of the accepted uniform
transfer, with no additional restrictions on the original matching.
If the original Q6 cut has no matching crossing, its already imported
five-direction endpoint theorem applies directly instead.

## Complete conditional coverage calculation

`ten_covered_t63_complete_split_profile.py` reads only the three frozen
residual files accepted by `Q5_A8_CONSEQUENCES_REVIEW.json`. It tests
every one of the six outer cuts, every eligible three-subset $S$ for
the two rows above, and the marked internal split counts. It records
an actual witness for each newly covered record and preserves all
other records byte for byte in separate output files.

| target | accepted input | newly covered if import accepted | remaining |
|---:|---:|---:|---:|
| 1 | 16920 | 4000 | 12920 |
| 7 | 17022 | 4296 | 12726 |
| 31 | 20280 | 4620 | 15660 |
| total | 54222 | 12916 | 41306 |

These are hole-geometry counts. Each successful row proves the result
for every realizing original matching, not just one matching sample.
Independent review must reconstruct the exact residual domain and each
actual marked split witness before these numbers enter the main ledger.

## Remaining obligations

The complete split theorem and this application require independent
acceptance. Complete ten-hole covered targets, the complete higher Q6
layers, and full P6 remain open.
