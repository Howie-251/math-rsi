# Q5 six same-parity holes: complete marked 2/4 split criterion

2026-11-01. ARIS proof-writer producer package. Complete proposed proof
relative to accepted Q4 inputs and new explicit finite positive certificates;
independent checker review is pending. Full T63_5 and full P6 remain OPEN.

## Exact claim and status

Let F be any matching of K(Q5) with exactly six holes H, all of one parity.
Let U subset H be any prescribed three omitted holes. Suppose a coordinate
cut puts two holes and one omission in one face, and four holes and two
omissions in the other face. Then there is a simple 29-cycle on exactly
Q5-U containing F, with every edge outside F short. All thirteen original
matching edges may be arbitrary, including long and same-parity edges.
No hypothesis is imposed on the number or partners of original crossings.

**Status: PROVABLE AS STATED relative to the declared finite certificate
inputs, pending fresh independent review of all source-domain coverage.**
This proves a marked-geometry sufficient family, not the original universal
six-hole/three-omission claim. A geometry without such a cut is not declared
infeasible or proved here.

## Assumptions, notation and dependency map

Use the accepted Q4 N14 and T44 theorems and the N14 rich optional-edge
positive tables. The first face A has two same-parity holes and one
marked omission; B has four same-parity holes and two marked omissions.
Identify face coordinates by the short mirror map. Because their GLOBAL
hole parities agree, their hole parities are opposite in these common
LOCAL Q4 labels. The original internal matchings are F_A,F_B and the
crossing matching is C with count c and endpoint sets X_A,X_B.

The positive-crossing argument uses only N14 and T44. The zero-crossing
argument uses the new finite gluing lemma below, which has a self-contained
domain reduction plus positive cycle certificates. No full T63_5 theorem,
ten-hole Q6 claim, or higher-layer P6 input is used. The proof DAG is
acyclic. Existing production proof files and claim ledgers are unchanged.

## 1. Positive original crossing count

The equality 2|F_A|+c=14 implies c is even. If c>0, choose a perfect
matching D on X_A; it is nonempty. N14 supplies a cycle K_A on A minus
its marked omission containing F_A union D. Delete D, attach each actual
original crossing edge, and compress the resulting disjoint paths to R
on X_B. No B endpoint repeats, and X_B is disjoint from F_B, so F_B union R
is a matching with exactly its original four B holes. Apply T44 avoiding
the two marked B omissions and expand R. All A vertices except its omission
are restored exactly once; every required edge is retained. The artificial
D edges are deleted and all compressed edges expanded, so every surviving
new edge is short. The result is a single cycle with 15+14=29 vertices.

## 2. General mirror-port gluing lemma

Let K_A,K_B be the corresponding local extending cycles. Select t disjoint
optional short edges in each cycle, with the same projected set S of 2t
endpoints. Deleting those edges leaves t paths in each face. Let Q_A,Q_B
be their endpoint pairings on S, with path edges treated as separately
labelled objects. If Q_A union Q_B is connected as a multigraph, add the
short mirror bridges at every point of S. Each port regains degree two;
all other degrees stay two. Contracting the local paths and the mirror
identification shows that the resulting graph is connected. It is therefore
one simple cycle on all 29 retained vertices. No required edge was deleted.

This argument applies to every t>=1 for which such witnesses exist. At
t=1 it is the usual one-common-optional-edge construction. At t=2 the two
path pairings must differ. At t=3 connectedness is checked directly and
cannot be replaced by mere inequality of pairings. The finite exceptions
below use t=2 or 3. Each has, additionally, a complete positive 29-cycle,
so its validity does not rely on reconstructing a pairing argument.

## 3. Complete zero-crossing N14/T44 gluing input

**Finite gluing lemma.** Let L have two same-parity holes in Q4, one
specified omission a. Let R have four same-parity holes of the opposite
local parity, with any specified two omissions. There are extending local
cycles joined by 2,4 or 6 mirror bridges as in Section 2, preserving all
required edges and omitting exactly these three vertices in the two faces.

### 3.1 Exhaustive marked normalization

Apply one common Q4 automorphism to both faces, taking a to 0 and the
other hole of L to 3 or 15. These are the only possible nonzero distances
between two same-parity Q4 vertices. L is now one of exactly 135135
matchings on fourteen covered vertices for each representative, totaling
270270 canonical L inputs. R's holes are odd in these common labels.

For R certificates only, translate one of its marked omissions to 0 and
permute the other to 3 or 15. Its two other holes are any pair of the six
remaining even vertices. This gives 30 canonical marked geometries, each
with exactly 10395 matchings on twelve covered vertices, totaling 311850
canonical R inputs. Transporting these R data under every coordinate
permutation and every odd translation gives all actual R inputs relative
to the fixed A coordinates. There are 24*8=192 such maps. This transport
does not independently relabel A; it enumerates all B placements relative
to the already normalized A.

The input byte format is eighteen bytes: sixteen mate bytes (255 means a
hole), then two omission bytes. N14's second omission byte is the sentinel
255 and its first is 0. T44 has the actual pair {0,3} or {0,15}. The new
rich positive certificate records append one byte n followed by n cycles,
each of length 15 for N14 or 14 for T44. For every record, each supplied
cycle must have exactly the declared retained vertices, contain every
required edge, and have every other edge short. Their union of optional
edges is a positively witnessed lower bound on the true optional union.

### 3.2 Large positive unions cover all but 6978 canonical R inputs

The complete N14 positive data give 270270 inputs and witnessed optional
union size at least 15 for every input. The new complete T44 data give
311850 inputs. Of these, 304872 have witnessed union size at least 18.
For such a transformed R and any L, intersection follows from 15+18>32,
because the shared Q4 has exactly 32 short edges. Choose one common
optional edge and local witnessing cycles; delete these edges and use
two mirror bridges. Both choices are simultaneous only for the one chosen
edge, so no invalid prescription of a whole optional union occurs.

The other 6978 canonical R inputs have witnessed union sizes:

| Size | 8 | 12 | 13 | 14 | 15 | 16 | 17 |
|---|---:|---:|---:|---:|---:|---:|---:|
| Inputs | 60 | 426 | 224 | 652 | 988 | 1632 | 2996 |

The producer's local unit enumeration completes all cycles on a low
input, but exactness is not a premise for coverage. It suffices that all
other inputs have positive >=18 unions and every one of these marked
low records is carried forward to the exception-domain test.

### 3.3 Exact controlled exception domain

The complete N14 rich masks have the following size distribution:

| Size | 15 | 16 | 18 | 19 | 20 | 21 | 22 | 23 | 24 | 25 | 26 | 27 | 28 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Inputs | 36 | 6 | 182 | 330 | 220 | 658 | 2238 | 6346 | 22200 | 48056 | 78920 | 77014 | 34064 |

Transport every low R record under all 192 maps. Deduplicating its full
mate array and unordered marked omission pair gives exactly 163152
distinct actual R states. The transformed union mask must agree for any
duplicate description; the producer checks this. For each R, retain only
L masks whose size plus R's size is at most 32, then test bitwise mask
intersection. Pairs above that size bound already have a common optional
edge. The remaining mask comparisons total 65760096, and exactly 1320
distinct ordered (L,R) matching pairs have disjoint witnessed masks.

Each pair is encoded as 34 bytes: sixteen L mate bytes, sixteen R mate
bytes, and the two actual R omission labels. L's omission is fixed at 0.
The canonical L domain is unique; transformed R states are unique; hence
the domain contains no duplicates. Its SHA-256 is
`754c496aa2c853de9f6f21941b268d822bbf9400070e0348496fbab611d50b2c`.
The producer `Q5_T63_disjoint_domain.cpp` builds this domain without
enumerating a blind matching Cartesian product. Independent acceptance
must reconstruct the full canonical matching domains, all transforms,
mask-based filters and exact final pair set, not merely trust this count.

### 3.4 Complete positive certificates for all 1320 pairs

`Q5_T63_four_port_complete.py` supplies actual local-cycle and simultaneous
edge-deletion witnesses for every pair: 1308 use four bridges; 12 need
six bridges after the four-port interface has no witness. The latter
failure is only failure of that interface, never a global nonexistence
claim. All 1320 inputs have an explicit positive global 29-cycle.

`Q5_T63_exception_positive_cycles.bin` contains exactly 1320 records of
63 bytes: its 34-byte domain pair followed by the 29 cycle vertices in
Q5 with A at bit16=0 and B at bit16=1. The cycle must omit 0_A and the
two actual marked B vertices, contain all thirteen original required
edges, and use only short edges outside those requirements, including
the closing edge. Every record was checked by the producer. The file's
SHA-256 is
`40993fde32fabaa38ab133eaf19708fb5aa5d2079c6de1c50b7681d40dcabe36`.
Its existence and complete domain coverage, rather than search
completeness or negative results, prove the needed finite sufficiency
once independently verified.

All nonexception pairs have a witnessed common optional edge; every
exception has a direct positive cycle. The two branches prove the finite
gluing lemma after its independent certificate/domain checks.

## 4. Completion of the marked split theorem

When the original c=0, F_A and F_B are independent face matchings with
exactly the local hole and omission patterns of Section 3, with opposite
LOCAL hole parities. Apply the finite gluing lemma. Its global cycle has
the exact original required matching, original H and prescribed U after
undoing the common normalization. All introduced bridges are short.
Together with Section 1 this handles every original crossing count and
proves the exact marked split theorem.

## 5. Geometry and potential ten-hole application

The producer hole-only census finds a good marked 2/4 split in 133760 of
the 160160 even-hole Q5 marked geometries, in 106 of 135 automorphism
orbits. The other 26400 geometries occupy 29 orbits and are not proved by
this theorem. These geometry counts require a separate independent check.
Odd translation handles the other global parity.

Root's separate producer profile reports that applying this strict marked
split theorem to the actual ten-hole rows (4,2) and (1,5), over all legal
three-bridge selections, would cover 12916 of the current 54222 residual
geometries and leave 41306. That decrement is not accepted or entered
in a ledger by this file: both the new Q5 finite gluing input and the Q6
application/profile need fresh independent review first.

## Corrections and open risks

The universal one-common-optional-edge N14/T44 gluing claim is false;
the frozen `Q5_T63_SPLIT_AND_FOUR_PORT.md` and its explicit example contain
local matchings with disjoint true optional unions. A valid four-port
positive repair is supplied for that example. The full exception domain
also contains twelve pairs requiring the six-port interface in the
current construction. No uniform two- or four-bridge bound is asserted.

All computational inputs and positive witnesses are producer artifacts
pending independent proof-checker review. No full T63_5, full A10,
ten-hole Q6 theorem, higher Q6 layer or full P6 conclusion follows solely
from this marked split result. No failed search is used as a negative
certificate for the original universal target.
