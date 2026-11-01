# Seven degree-six vertices suffice in the 24-vertex T34 branch

## Target and status

Let H be a simple five-uniform hypergraph on 24 vertices with exactly 34 edges,
covering every vertex pair. If at least seven vertices have degree six, H has
Property B. This is a complete paper candidate using the earlier local catalogue
and new exact certificates; no new Lean theorem is asserted here.

## Invariant, assumptions, and route

For a degree-six vertex x,

    sum(y != x) (codegree(x,y)-1) = 4*6-23 = 1.

Consequently x has exactly one nonunit partner, of codegree two, and exactly one
unordered bad pair of incident edges. Fix each such actual pair before changing
the lock layout. Its trace slot lies in the positive-capacity slot inventory.
The invariant is the random greedy failure bound, with these actual bad pairs
deducted before taking the minimum of A, B, and C.

1. If two degree-six vertices have nonunit codegree, the previously established
   six-low matching branch applies (181 orbits, independent exact checks).
2. Otherwise choose seven pairwise-unit degree-six vertices S. If some edge has
   at least four vertices in S, choose four of them and two members of S outside
   that edge. This gives six unit low locks and an exact four-point trace. The
   previous quad / quad-plus-triple certificates apply. Such two outside vertices
   exist because an edge has size five and |S|=7.
3. The remaining seven-lock traces have size at most three. Their multi-point
   traces form a linear triple family completed by all uncovered pairs. The
   earlier complete catalogue contains 5,596 labelled inputs / 14 S7 orbits.
   Twelve orbits were already handled. The two remaining orbits now also have
   strict finite rational mixtures, as detailed below.

## Exact new mixtures

The catalogue IDs refer to
`context/propertyb34-hour1-20261013/high-math/SEVEN_LOW_CATALOGUE.json`.

| ID | Triple family | Exact upper bound | Positive layouts |
|---:|---|---|---:|
| 5 | Pasch configuration on six vertices plus an isolated seventh | 219195871/220993370 | 44 |
| 6 | Three-triple linear chain covering all seven vertices | 482859401/486200000 | 52 |

`SEVEN_MIXTURE.json` gives every original trace count, admissible actual slot,
positive layout with its rational weight, slot average, and center maximum.
Positions are stored per original lock label, not as an unordered position set.
The finite candidate layouts use four position templates and all S7 label
orders. A floating LP proposed weights; rounding followed by exact normalization
produced the displayed rational certificates.

The validity argument is finite and does not assume independent actual slots.
Fix H and its actual slot a_i at each center. For each layout l write

    U_l = F_l + sum_i g_(i,l)(a_i),
    g_(i,l)(a) = min(A_(i,l), B_(i,l), C_(i,l) - loss_(i,l)(a)).

For the saved nonnegative rational weights pi_l summing to one,

    sum_l pi_l U_l
      <= sum_l pi_l F_l + sum_i max_a sum_l pi_l g_(i,l)(a) < 1.

Hence one layout has U_l<1 and supplies a proper two-coloring. The slot choice
stays fixed while averaging; no interchange of max and expectation is used.

## Independent verification and remaining work

`verify_mixtures.py` independently expands all 34 edge trace stubs, recomputes
all A/B/C rows with falling-factorial injection probabilities, replays every
positive layout and every listed slot, and verifies mass one and the displayed
strict bounds. `SEVEN_MIXTURE_INDEPENDENT.json` records both checks passing.
Runtime was about 0.56 seconds for this independent replay; discovery took about
15 seconds. No whole-hypergraph enumeration is involved.

The original target is unchanged. The new paper range is all 24-vertex inputs
with at least seven degree-six vertices, improving the previous at-least-eight
range. The remaining mathematical branches include one through five low
vertices and the four unresolved all-unit six-low types. Lean implementation
must connect actual traces, the catalogue, the slot inventory, and the finite
averaging argument; model review and numerical replay do not replace those
connections.
