<!-- Publication excerpt: mathematical content retained; local paths/control-plane metadata redacted, links relocated. Original SHA256 in INVENTORY.json. Historical snapshots are superseded by HANDOFF.md. -->
# Fixed-abscissa geometric test of the17-point shared-lock witness

2026-11-20. The existing complete17-point signotope witness was tested on the
authoritative Linux host. The four specified increasing abscissa patterns are
all **exactly infeasible**. No planar realization was obtained. This does not
prove that the coloring is geometrically nonrealizable with other abscissas.
The optional geometric branch stops here; the global upper bound is independent.

Input:[the full17-point coloring](../../inputs/signotopes/shared-lock17.json), SHA256
`d1c7515ee4171e668c519efb4f451624f94bafb3a80b1a8611b8737ef9e1d0b8`.
Source:[geometry_probe.py](../../SOURCE_MAP.md#excluded-sources), SHA256
`27757fe9a976dbfa02424192c026777474aae97d7683690039b7dd926b4f820f`.

## Exact test and certificates

For each actual$i<j<k$, use the oriented determinant

$$D_{ijk}=(x_j-x_i)(y_k-y_i)-(x_k-x_i)(y_j-y_i).$$

The required signs are$D>0$for red/cup and$D<0$for blue/cap. For a fixed$x$
vector these are680linear strict inequalities in the$y$coordinates. Feasibility
is equivalent to signed determinants at least1, by positive scaling of$y$.
Subtracting an affine function of$x$does not change any determinant, so
$y_0=y_{16}=0$may be fixed without losing any realization for those abscissas.

For every reported infeasible pattern, HiGHSsupplied only a numerical support.
The program then solved that support's equations over exact rational numbers
and checked nonnegative weights$\mu_\tau$, total weight1, and zero weighted
coefficient sum in **all17original ycolumns**. With$A_\tau y$the prescribed
signed determinant, this is

$$\mu_\tau\ge0,\qquad\sum_\tau\mu_\tau=1,\qquad
\sum_\tau\mu_\tau A_\tau=0.$$

If all prescribed signed determinants were positive, their weighted sum would
be positive; the last identity makes that sum zero. Thus these are exact
Farkas witnesses for the respective fixed$x$vectors, not floating-infeasibility
claims and not claims about arbitrary increasing$x$.

| Fixed abscissas, $i=0,\ldots,16$ | Exact certificate terms | Receipt |
|---|---:|---|
|$x_i=i$|14|[uniform](../../SOURCE_MAP.md#excluded-sources)|
|$x_i=i^2$|10|[quadratic](../../SOURCE_MAP.md#excluded-sources)|
|$x_i=i^3$|11|[cubic](../../SOURCE_MAP.md#excluded-sources)|
|$x_i=256-(16-i)^2$|10|[reflected quadratic](../../SOURCE_MAP.md#excluded-sources)|

The [complete result](../../SOURCE_MAP.md#excluded-sources) records all LPstatuses and exact
certificate SHA256bindings. All four LPs, dual supports and exact rational
checks took0.121675819seconds. Runtime was the already installed Linux
`<private-python-runtime> -I -B`, SciPy1.15.3andNumPy2.2.6.
The preferred3.12environment lackedSciPyand performed no LP. Isolated import
mode avoids the repository's known `inspect.py`shadow; no dependency was
installed or environment changed.

No coordinates, geometric coexistence assertion, general nonrealizability
conclusion, external review, new solver campaign or modification of preserved
jobs follows from this result.
