# A6 finite Q4 inputs: independent review

Review date: 2026-11-01. Requested reviewer: GPT-6.1-sol, high.
`review_independence: same-family`; `acceptance_status: provisional`.

**Result:** the two finite inputs pass independent deterministic verification,
including complete arbitrary matching coverage and the required geometric orbit
coverage. The old two-hole spectrum dependencies were also reverified. This
report does not establish A6 or P6, and does not change their status.

The machine-readable evidence is `A6_FINITE_INPUTS_REVIEW.json`. The independent
checker is `a6_finite_inputs_independent_check.py`. All paths here are relative
to this report's directory. Existing producers, certificates, checkers and main
proof state were left untouched. The existing producer PASS logs were not used
as evidence for validity or completeness.

## Precise statements audited

Write Q4 on vertices 0,...,15 with short edges joining vertices whose XOR has
Hamming weight one. KQ4 here means the complete graph on these vertices:
the prescribed matching can contain arbitrary long or same-parity edges.
Four distinct holes mean exactly the unmatched vertices, so the matching has
six edges. All paths and cycles below contain every prescribed matching edge.

1. For every matching with holes {v,b,z,d}, with v,b of one parity, z,d of the
   other parity, and z not adjacent to b, there is a simple 15-vertex path
   covering exactly Q4 minus v, starting at d and ending at a vertex e with
   parity(e)=parity(d) and e != z. Every edge outside the matching is short.
2. For every four-hole matching with a 1:3 parity split, and for **each specified
   hole h in the majority class**, consider all simple cycles covering exactly
   Q4 minus h with every new edge short. The union of their new edges contains
   at least 15 distinct short edges. For a 2:2 split, take cycles covering all
   16 vertices; the analogous union contains at least 18 short edges.

The second statement is a **spectrum/union** bound. It does not say that a
single cycle has 15 or 18 new edges. In the four-hole setting each such cycle
has respectively nine or ten new edges, so that reading would be false.
Likewise, a witnessed minimum union of 15/18 need not be the exact full spectrum.

## Independent verification method

The checker imports no producer or supplied-checker code. It reconstructs
matchings as unordered pair partitions. A separate recursive enumerator builds
the entire expected set on the covered vertex set, and the set of parsed
matchings must equal that expected set, with duplicates forbidden. This avoids
reusing the supplied checkers' mixed-radix rank mechanism. It independently
confirms 12-vertex matching counts 11!!=10395 and 14-vertex counts 13!!=135135.

For each record it checks exact holes, no fixed points, a symmetric matching
involution, distinct path/cycle vertices and exact required vertex set,
inclusion of all six (or seven for old two-hole inputs) matching edges, and
Hamming distance one for every remaining edge. Paths additionally satisfy
the prescribed root and endpoint restrictions. Cycles explicitly include the
closing edge. Each spectrum union is reconstructed from actual edges with
the matching edges removed, record by record. Parsing must consume the file
exactly, and counts and full matching sets must agree.

It constructs all 16*24=384 cube automorphisms explicitly and checks adjacency
preservation. Coordinate permutations fix 0; translations reduce any v to 0
and preserve parity equality/opposition as well as short edges. Relabeling also
preserves arbitrary complete-graph matching edges.

## Path input and orbit cover

After translating v to 0 there are 196 eligible ordered triples (b,z,d):
seven nonzero even b, four odd z at distance three from b, and seven distinct
odd choices of d. Their 13 orbits under the 24 coordinate permutations have
the following representatives and multiplicities:

| b | z | d | Orbit size |
|---|---|---|---|
|3|4|1|24|
|3|4|7|12|
|3|4|8|12|
|3|4|11|12|
|3|4|13|24|
|3|13|1|12|
|3|13|2|12|
|3|13|4|24|
|3|13|7|24|
|3|13|14|12|
|15|1|2|12|
|15|1|7|12|
|15|1|14|4|

Both `q4_balanced_avoid_path_configs.txt` and every entry and multiplicity in
`q4_balanced_avoid_path_orbits.json` agree with the independently computed
orbits. Every representative file covers all 10395 matchings and supplies
one valid path per matching: 135135 path records total. By equivariance,
these witnesses establish statement 1 for every allowed configuration.

## Four-hole spectrum orbit cover and adjacent-hole reduction

Let M have holes H and let e=ab be a short edge joining two holes. Then
M'=M union {e} is an arbitrary matching with two holes. Any legal completion
of M' is a legal completion of M with the same avoided vertex, if any:
it contains M, and its newly added edges relative to M are the new edges
relative to M' together with e. Consequently the old spectrum is a subset
of the spectrum for M; no distinct optional edges are lost in this reduction.

For the 1:3 case, fix the avoided majority hole h. If the minority hole has a
short edge to either of the other two majority holes, choose it as e. The two
remaining holes are h and another majority vertex, at distance two or four.
The old L15 two-hole result applies, avoiding exactly h. Translation maps h
to 0, and coordinate permutation maps the other hole to 3 or 15, respectively.
Its seven-edge matching is arbitrary, as required by the old certificates.

If no such e exists, normalize the minority hole to 0. The other two majority
holes are distinct weight-three vertices, and coordinate permutation carries
their unordered pair to {7,11}. The three residual marked-hole orbits have
representatives (H,h)=({0,7,11,t},t) with t=1,4,13. Explicit complete
automorphism enumeration verifies this classification, including both choices
of majority parity: there are 2688 marked configurations in total, 2112
handled by the adjacent reduction and 576 residual configurations, exactly
192 in each of the three orbits. The residual condition concerns adjacency
between the minority hole and the **other two** majority holes; adjacency to
the avoided hole does not permit the old avoided-hole reduction.

For the 2:2 case, any short hole-hole edge e leaves two opposite-parity holes,
at distance one or three. The old L18 two-hole result applies after translation
and coordinate permutation to the representative other hole 1 or 7. Among
all binomial(8,2)^2=784 balanced four-hole sets, 760 admit this reduction.
The remaining 24 sets form exactly the automorphism orbit of {0,3,13,14}.
The independent enumeration checks equality with that orbit, rather than only
checking a list of selected examples.

## Numerical evidence

| New spectrum input | Matchings | Cycle witnesses | Minimum witnessed union |
|---|---:|---:|---:|
|q4_four_spectrum_A_1.bin|10395|37204|15|
|q4_four_spectrum_A_4.bin|10395|37600|15|
|q4_four_spectrum_A_13.bin|10395|37153|15|
|q4_four_spectrum_balanced.bin|10395|48592|18|

These are 41580 new spectrum records and 160549 cycle witnesses. The old
inputs `q4_spectrum_A_3.bin`, `q4_spectrum_A_15.bin`,
`q4_spectrum_B_1.bin`, and `q4_spectrum_B_7.bin` were also parsed and checked
independently: all 540540 matching records and 2448249 cycle witnesses pass,
with witnessed union minima 15,15,18,18. Thus the adjacent-hole reductions
do not rest on unexamined producer declarations.

The complete independent run checked **717255 matching records and 2743933
positive path/cycle witnesses across 21 certificate files**. The JSON report
records each input's SHA-256, source-checker hashes, per-file counts, minima,
and geometry counts.

Reproduction from the workspace root:

```powershell
D:\anaconda\python.exe research/six_directions/a6_finite_inputs_independent_check.py
```

No counterexample exists within these finite quantified statements, as
witnesses have been checked for every matching in each complete orbit cover.
No FATAL, CRITICAL or MAJOR issue was found for these scoped inputs. The supplied
checkers' record format and conclusions agree with the independent checks;
the independent audit additionally checks the orbit JSON and the complete
four-hole-to-two-hole geometric reduction. Producer algorithms need not be
assumed complete or correct for this conclusion: complete coverage and
positive witnesses were verified directly from their output artifacts.

The remaining A6/P6 proof obligations and any use of these bounds in a
higher-dimensional argument are outside this report. Mathematical semantic
acceptance remains same-family/provisional pending a cross-family overlay.
