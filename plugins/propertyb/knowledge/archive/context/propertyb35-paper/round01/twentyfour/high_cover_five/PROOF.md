# Twenty-four vertices, no all-seven edge, five higher-degree vertices

Let H be a finite simple five-uniform hypergraph with 24 vertices and 35 edges, minimum degree seven, and exactly five vertices of degree greater than seven. Suppose that no edge consists entirely of degree-seven vertices. Then H has Property B.

## Actual high-cover set and the two degree spectra

Let P={v:d(v)>7}. By hypothesis |P|=5, and the other nineteen vertices all have degree seven. Since the degree sum is 5*35=175,

    sum_{v in P} d(v) = 175-19*7 = 42.

All five degrees in P are at least eight, so their nonnegative integer excesses above eight sum to two. Up to relabeling, the only degree vectors are

    (10,8,8,8,8) or (9,9,8,8,8).

Every edge meets P, because an edge avoiding P would consist entirely of degree-seven vertices. Thus P is an actual vertex cover. If no edge is contained in P, color P red and its complement blue. Every edge then meets both colors, proving the claim in this case.

It remains to consider the case that an edge is contained in P. Since it has five points and |P|=5, it is exactly P; by simplicity there is exactly one such edge.

## Complete exact-trace classification

For T subseteq P, let mu(T) be the number of edges whose intersection with P is exactly T. These are actual nonnegative integer counts with

    mu(empty)=0,   mu(P)=1,
    sum_T mu(T)=35,   sum_T |T| mu(T)=42.

Subtracting the full P-edge gives

    sum_{empty != T proper subset P} (|T|-1) mu(T) = 3.

The terms of size one contribute zero, size two contributes one per edge, size three contributes two, and size four contributes three. Therefore the complete possibilities for the multi-point proper traces are exactly:

1. Three pair traces, with repetition allowed.
2. One triple trace and one pair trace.
3. One quadruple trace.

Repeated pair traces refer to distinct original edges with the same two-point intersection with P. They are permitted and are included, with multiplicities two or three, in the domain.

There are ten pair masks, ten triple masks and five quadruple masks. The three categories give respectively

    binom(10+3-1,3)=220,   10*10=100,   5

labelled multi-trace patterns, for a total of 325 for each degree vector. For a chosen pattern the singleton counts are forced:

    mu({i}) = d_i - 1 - sum_{T proper, |T|>=2, i in T} mu(T).

The subtraction by one accounts for the full P-edge. All these counts are nonnegative: the multi-trace contribution at any fixed vertex is at most three, whereas d_i>=8. Consequently every one of the 325 patterns produces a valid abstract nonnegative inventory of 35 edges with the stated degrees. An abstract inventory need not extend to a whole hypergraph; what matters is that the classification includes the inventory of every actual H in this case.

## Degree-preserving quotient and strict original ABC bounds

Label P so that its degree vector is one of the two displayed vectors. Only permutations preserving that vector are used. The groups have orders 4!=24 and 2!*3!=12, respectively. Simultaneously permuting all subset masks by those permutations gives 31 orbits for the first degree vector and 50 for the second. `DOMAIN.json` records all 650 labelled inventories, all 81 representatives, and one concrete degree-preserving transport permutation for every labelled inventory.

For each of the 81 representatives, `FIXED.json` gives explicit positions of the five labelled locks in a permutation of the 24 vertices. The existing conditional permutation-counting lemma bounds the expected number of failures by the sum over all positions k of min(A_k,B_k,C_k), where A,B,C are the original exact one-sided and sandwich counts for the actual trace multiplicities. The remaining nineteen vertices are uniformly permuted, with sample-space denominator 19!.

All 81 original ABC bounds are strictly below one. This conclusion uses no link-pair quota deduction or joint-layout certificate. The exact largest bound is

    11061/12376 < 1.

The maximum is 11061/12376 for degree vector (10,8,8,8,8) and 15441/18088 for degree vector (9,9,8,8,8). The chosen layouts place one lock at position 11 and the other four at positions 21,22,23,24, with the label order specified in each certificate. The finite data include repeated-pair patterns and every degree-preserving orbit; the result is not a sample assertion.

Transport the representative's five lock labels and its specified positions by the stored single permutation to the actual labelled inventory. This preserves the trace counts and therefore the ABC bound. The expected number of failures for that actual H is strictly less than one, so the conditional permutation argument supplies a proper two-coloring. Together with the earlier explicit red/blue case, this proves the statement.

The outside vertices' individual degree-seven incidences are used to derive the degree sum on P; no further assumed independence or unproved outside-marginal condition enters the strict count.

## Independent domain and arithmetic verification

The discovery generator `domain.py` constructs the three categories explicitly, using combinations with replacement for the three pair traces. The independent `replay.py` instead recursively enumerates all nonnegative proper multi-trace multiplicities solving the single weighted integer equation

    sum_T (|T|-1) mu(T)=3.

It independently recovers exactly 325 patterns, with category counts 220,100,5, then reconstructs the two singleton degree inventories. It verifies equality with the full 650-inventory labelled domain, independently computes the two degree-preserving quotient sizes 31 and 50, checks representative-orbit distinctness, and checks all 650 stored transport permutations.

For arithmetic, the replay expands each representative into 35 labelled edge stubs and uses the separate labelled-injection implementation to recompute every A,B,C row at the fixed positions. It checks all 24*81=1,944 rows against the stored values and sums the original minima, without reading a quota deduction or running DP, LP, or position search. `REPLAY.json` records PASS, 81 strict raw ABC certificates, and the exact maximum above. The replay took about 0.39 seconds on this run; the full fixed discovery took 0.95 seconds after reusing sixteen pilot cases.

Reproduce from the project root:

```sh
python3 -B context/propertyb35-paper/round01/twentyfour/high_cover_five/replay.py
```

This closes the stated actual five-point high-cover branch. It makes no claim that the complementary cases of the entire 24-vertex problem are covered.
