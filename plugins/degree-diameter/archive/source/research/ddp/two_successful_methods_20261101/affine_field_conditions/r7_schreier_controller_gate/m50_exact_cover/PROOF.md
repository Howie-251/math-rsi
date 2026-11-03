# Complete fixed-m50 gate: no controller passes

The one authorized run exhausted its domain and returned `COMPLETE_NO_M50_FIXED_FAMILY_CONTROLLER`. This is a complete result for the fixed three-base A/B/S/T/R topology at m=50, under the simple seven-neighbor conditions and exact three-walk coverage requirement. It is not an exclusion of arbitrary seven-regular controllers, other topologies, other moduli, or other F11 constructions.

The actual public gate was supplied by root before execution: the proposed 150-controller full F11³ lift would have order199650, above the located degree77 guarantee169750. This comparison authorized the experiment; no graph at199650 was produced.

## Exact symbolic decomposition

`check_symbolic_identity.py` independently constructs the proposed formal support and compares its integer coefficient vectors with the saved 50 root00 forms in `../DISTINCT_FORMS.tsv`. Only the half-shift coefficient is reduced modulo2. The two formal sets are equal, with no missing or extra vectors. The first part has 26 vectors and the three d-dependent blocks have eight vectors each. This symbolic check does not repeat the earlier residue enumeration.

Writing a=alpha0, s=sigma, t=tau, h=25 and (d1,d2,d3)=(alpha1,-alpha2,rho), the support is

```
{±a,±3a,h,h±2a}
union {±a±s,h±s,±a±t,h±t}
union {0,±s,±t,±(s-t)}
union block(d1) union block(d2) union block(d3),
block(d) = ±(d+{0,s,-t,s-t}).
```

At m50, covering 50 residues with exactly 50 formal vectors forces all evaluated values to be distinct. Thus the base26 must have 26 residues, each block must have eight, the blocks must avoid the base, and their disjoint union must fill its 24-residue complement. These are exact necessary and sufficient conditions for root00 support coverage.

## Exhaustive reductions

The already completed mod2 uniformity gate forces alpha0 even. Simple controllers exclude alpha0=0. Every remaining alpha0 has gcd(alpha0,50) equal to2 or10. Multiplication of all coordinate shifts by a unit u modulo50 is a controller isomorphism; u is odd, so u*25=25 modulo50. The unit action is transitive on each gcd class. It is therefore complete to use a=2 and a=10.

Simple controllers also require s,t nonzero and d1,d2,d3 nonzero and pairwise distinct. Permuting these three d values preserves the underlying graph: the base1-to-base2 shifts are exactly {0,d1,d2,d3}, the reverse shifts are their negatives, and all other neighbor sets stay fixed. Assigning sorted d1<d2<d3 to (alpha1,-alpha2,rho) supplies one valid port labeling for every such graph. Both simplicity and unlabelled three-walk coverage are preserved by this permutation. Consequently no sixfold repetition of the full-support test is necessary.

For every one of the 2*49²=4802 normalized choices (a,s,t), `gate.cpp` evaluates the 26-base mask. If it has 26 distinct residues, it evaluates all49 nonzero d blocks and keeps precisely the eight-residue blocks disjoint from the base. For every ordered index pair i<j with disjoint masks, the third mask must equal the eight-residue complement of their union. Testing k>j enumerates every unordered exact-cover triple once.

Each tiling is then tested against all nine saved symbolic endpoint-support classes, using the actual parameter assignment (a,d1,-d2,s,t,d3,25). The test evaluates every saved distinct symbolic vector and requires all50 residues in every ordered base pair. It stops at the first failing base pair. These saved classes enumerate all three-port words; thus a support failure means an actual missing three-walk endpoint, not a field-rank failure.

## Actual completed counts

| Quantity | Actual count |
| --- | ---: |
| Normalized outer pairs visited / total | 4802 / 4802 |
| Outer pairs with 26 distinct base residues | 844 |
| Nonzero d blocks tested | 41356 |
| Admissible eight-residue blocks | 3736 |
| Block-pair nodes | 8140 |
| Root00 exact tilings | 32 |
| Full-support candidates tested | 32 |
| Candidates failing first at base0 to base1 | 32 |
| Controllers passing all nine supports | 0 |

The runtime returned normally, without a CPU stop. Preparation, the independent symbolic comparison, compilation and the run wrapper account for **0.919086454 CPU seconds** under the20-second single-worker budget. The child process counter measured0.00405seconds for the gate; its internal coarse `clock()` reading rounded to0. `RESULT.json` records both rather than replacing one with the other. There were no failed compilations or retries.

## Consequence and scope

All32 remaining graphs have a missing root-base0 to target-base1 three-walk endpoint. An adjacent controller pair always has a three-walk by an edge followed by a backtrack, so such a missing pair is nonadjacent. Even if it has two-walks, at most seven intermediate controller vertices give at most7*11²=847 possible endpoint-fiber vectors within two lifted steps from a fixed source, below the full1331-point fiber. With no controller three-walk, no lifted three-walk can repair the gap. Hence the fixed full-fiber F11³ construction at m50 cannot have diameter at most3.

No controller/port-word certificate is exported because there is no passing controller. No fiber graph, BFS, Lean, solver, external review, lower-modulus run or extra parameter family was started. `TERMINAL.json` records complete exhaustion and no active process. Lower even moduli remain outside this batch rather than being automatically searched.
