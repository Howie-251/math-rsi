# Q4 T63: six same-parity holes with three prescribed avoided holes

Date: 2026-11-01. New finite input for A8 exploration; fresh review pending.

## Claim

Let $L$ be an arbitrary matching of $K(Q_4)$ with six holes $H$ of one
parity. Let $U\subset H$ be any prescribed three holes. Then a simple
cycle with vertex set exactly $Q_4\setminus U$ containing $L$ and using
only short new edges exists if and only if there is no covered vertex
$a$ of opposite parity having exactly one neighbor $b$ outside $U$ with
$ab\in L$.

## Status

**PROVABLE AS STATED** by analytic necessity and complete finite positive
certificates. This result awaits independent proof-checker review.

## Assumptions, notation, and dependency map

The vertices are the four-bit integers $0,\ldots,15$. A short edge has
endpoints differing in exactly one bit. The required matching can contain
arbitrary edges. The proof uses no Q5 extension theorem and no T15 input.
The finite positive files are listed in `A8_Q4_T63_manifest.json`.
The verifier is `A8_Q4_T63_verify.py`, with output
`A8_Q4_T63_verified.json`.

## Proof strategy and proof

### Step 1. Analytic obstruction

Every vertex of parity opposite to $H$ is covered by $L$. Suppose $a$
has just one short neighbor $b$ outside the avoided set $U$, and
$ab\in L$. In a proposed cycle the edge $ab$ must be present. Because
$L$ is a matching, every other edge incident to $a$ in the cycle would
be a new short edge. There is no distinct such edge available: the only
remaining short neighbor is already $b$. A simple cycle needs two
distinct incident edges at $a$. This is impossible, proving necessity.
This is an explicit degree obstruction, not a Hamilton-search failure.

### Step 2. Exhaustive normalization of the finite domains

First assume $H$ is even. There are
$\binom86\binom63=560$ marked geometries $(H,U)$. The automorphisms

$$x\longmapsto\pi(x\mathbin\oplus e),$$

where $e$ is any even vertex and $\pi$ is any coordinate permutation,
give seven orbits. Their representatives and orbit sizes are:

| $H$ | $U$ | orbit size | positive matchings | degree-obstructed matchings |
|---|---|---:|---:|---:|
| $0,3,5,6,9,10$ | $0,3,5$ | 96 | 945 | 0 |
| $0,3,5,6,9,10$ | $0,5,6$ | 96 | 840 | 105 |
| $0,3,5,6,9,10$ | $0,5,9$ | 96 | 945 | 0 |
| $0,3,5,6,9,10$ | $0,5,10$ | 96 | 945 | 0 |
| $0,3,5,6,9,10$ | $5,6,9$ | 96 | 945 | 0 |
| $0,3,5,10,12,15$ | $0,3,5$ | 32 | 840 | 105 |
| $0,3,5,10,12,15$ | $0,3,12$ | 48 | 945 | 0 |

The verifier regenerates each orbit directly, checks that they are
pairwise disjoint, and checks that their union equals the entire set of
560 marked geometries. Hence this is a complete geometry cover. If $H$
is odd, an odd translation makes it even and preserves short edges,
matching edges, avoided vertices, and the obstruction condition.

### Step 3. Complete matching coverage and explicit cycles

Every representative has ten covered vertices, admitting exactly
$9!!=945$ matchings. Each binary file has 945 records of 29 bytes:
16 mate bytes, followed by 13 cycle bytes. A mate byte of 255 marks a
hole. A 13-byte suffix consisting of 255 marks a negative record.

The verifier independently constructs the set of all 945 unordered
edge-set matchings. For each record it checks the exact holes and the
fixed-point-free mate involution, removes that matching from the set,
and finally checks that the set is empty. Thus there are no omitted
or duplicated matching inputs.

For every positive record, it checks 13 distinct vertices, exact vertex
set $Q_4\setminus U$, containment of every matching edge, and shortness
of every cycle edge outside the matching. These explicit cycles prove
sufficiency for all 6405 positive records. No assumption about the
completeness of the producer's search is needed.

For every negative record, the verifier directly checks the obstruction
of Step 1. There are exactly 210 such records: 105 in each of the two
negative-bearing representative files. In the second row the forced
obstruction edge is $4\,12$; in the sixth row it is $1\,9$. In each
case the three avoided vertices are three of the four short neighbors
of the first endpoint, leaving just the second endpoint. Fixing that
matching edge leaves eight other covered vertices with $7!!=105$
matchings. The count agrees with, and is independently checked against,
the explicit records. The verifier also checks absence of an obstruction
for each positive record.

### Step 4. Transfer back to arbitrary inputs

Choose an automorphism taking $(H,U)$ to one of the representatives.
It maps an arbitrary original matching to one of the 945 checked
matchings and preserves the obstruction. In the unobstructed case,
invert the automorphism on its explicit positive cycle. In the obstructed
case apply Step 1 directly. This proves the exact classification.

## Reproduction

Run `D:\anaconda\python.exe A8_Q4_T63_verify.py` in this directory.
The verified result records all seven binary hashes and the verifier
hash, with totals 560 geometries, seven orbits, 6615 matching records,
6405 positive cycles, and 210 analytic negative records.

## Corrections or missing assumptions

T63 is not universally positive. An application in a three-bridge Q5
transfer must exclude a degree-obstruction edge in the final compressed
matching, including edges created by suppression. Absence of the fixed
edge in the original face matching alone does not suffice.

## Open risks

Fresh independent review is pending. The local theorem by itself proves
no remaining A8 orbit, no full A8, and no higher-hole P6 layer.
