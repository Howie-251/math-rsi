# Covered-target eight-hole geometry census

Date: 2026-11-01. Scope: the R8-covered geometry in
`EIGHT_HOLE_CONDITIONAL_REDUCTION_DRAFT.md`, with root 0 and covered target
v=1,7,31. These normalize the three odd distances 1,3,5 under coordinate
permutations. This is a geometry census only: no matching realizability
assertion, no matching enumeration, and no A6/P6 closure.

`review_independence: same-family`; `acceptance_status: provisional`.

## Complete domain and counts

For each target, enumerate all 3-subsets Z of the 31 nonzero even vertices,
then every 4-subset W of odd vertices other than v, subject only to no short
edge between Z and W. Adjacency to root 0 is allowed. Unlike the free-target
census, adjacency from Z to v is allowed because v is covered.

For each coordinate, A is its face containing v and
(a,b)=(|Z intersect A|,|W intersect A|). Retain a geometry if none of its six
rows belongs to {(0,1),(0,2),(1,1),(1,2),(1,3),(2,2),(2,3),(2,4),(3,3)}.

| v | All eligible geometries | No good cut | Orbits fixing 0 and v | Stabilizer order |
|---:|---:|---:|---:|---:|
|1|9168375|19530|278|120|
|7|9334641|22472|875|36|
|31|9347625|24125|345|120|

All 66127 retained geometries are saved, without orbit reduction, in
`covered_eight_residual_1.bin`, `_7.bin`, `_31.bin`. Each record consists of
seven unsigned bytes: sorted Z[3], followed by sorted W[4]; v is in the filename.
The three files contain 462889 bytes total. Every orbit representative,
orbit size, six rows and splitting signature is additionally saved in
`covered_eight_geometry_census_independent_check.json` (1498 orbits total).

## Splitting Z and the missing rows

Every retained geometry has at least three coordinates with a=1 or a=2.
The only bad rows on those coordinates are (1,0),(1,4),(2,0),(2,1).
All four row types do occur. All eleven bad rows in the draft occur somewhere
in the retained census, for every normalized target.

**Every retained geometry has a coordinate with (a,b)=(2,0) or (2,1).**
Thus an extension handling these two rows would cover the residual geometries
of this nine-row criterion, conditional on its other hypotheses. This is a
geometric observation and supplies no transfer proof for either new row.

The more favorable condition "there is a (1,4) or (2,1) cut" fails on 10,20,20
geometries for v=1,7,31 respectively. All 50 exceptions have exactly the same
six-row multiset: three copies of (2,0), three copies of (3,2). Their splitting
coordinates therefore offer only (2,0), and none offers (1,0), (1,4), or (2,1).
They form the following seven orbits under the target stabilizer:

| v | Z | W | Orbit size |
|---:|---|---|---:|
|1|3,5,9|14,31,47,62|10|
|7|3,5,6|8,16,32,56|1|
|7|3,5,15|8,25,41,56|9|
|7|3,15,23|25,26,56,59|9|
|7|15,23,39|56,59,61,62|1|
|31|15,23,27|1,2,32,35|10|
|31|15,23,63|32,35,37,38|10|

Splitting signatures indicate which of (1,0),(1,4),(2,0),(2,1) are available,
with bit values 1,2,4,8 respectively. This captures all possibilities rather
than just near-boundary exceptions:

| Signature mask | v=1 count | v=7 count | v=31 count |
|---:|---:|---:|---:|
|4|10|20|20|
|6|40|57|60|
|8|4665|5742|6210|
|9|1470|1440|1560|
|10|4560|5094|5430|
|11|1040|1086|1140|
|12|4710|5901|6360|
|13|1140|1050|1160|
|14|1895|2082|2185|

There are 54 distinct sorted multisets of the six rows for each target.
Their counts and representatives, every bad-row frequency, and splitting
coordinate counts are in `covered_eight_geometry_census.json`.

## Verification and reproduction

`covered_eight_geometry_census.cpp` exhaustively loops over the complete
domain and writes the JSON and three residual files. Its good-row lookup is
explicit and includes all nine rows. `verify_covered_eight_geometry_census.py`
independently rechecks every retained record, duplicate exclusion, hole
parities, independence, target exclusion, six rows, all summary distributions,
and orbit sizes. It independently recomputes eligible-domain totals as
sum over Z of binomial(number of allowed odd vertices,4), without iterating
over W quadruples. The Python program does not independently rerun the entire
28-million-geometry no-good-cut selection; completeness of that selection is
from the transparent exhaustive C++ loops. Orbit sets are generated under
all coordinate permutations preserving v, and must partition the retained
record set exactly. JSON evidence includes source and record SHA-256 hashes.

```powershell
g++ -O3 -std=c++17 research/six_directions/covered_eight_geometry_census.cpp -o research/six_directions/covered_eight_geometry_census.exe
research\six_directions\covered_eight_geometry_census.exe research/six_directions
D:\anaconda\python.exe research/six_directions/verify_covered_eight_geometry_census.py
```

Both programs completed successfully. These results identify the remaining
geometry for further proof work; they do not establish that any particular
retained hole set admits a short matching or solves R8-covered.
