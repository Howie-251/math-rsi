# Pairing criterion: valid sufficiency, false universal coverage guarantee

The proposed sufficient condition is correct. The hypotheses “pair coverage, 35 five-edges, total degree 175, minimum degree seven” do not guarantee it: the explicit colorable 24-vertex example below admits no vertex matching hitting 20 edges. Its universal hit upper bound is 19. Thus this condition cannot by itself cover the entire 22–24-vertex range under the proposed degree assumptions.

## Sufficient condition

Let H have at most 35 five-element edges. Suppose there is a vertex matching P such that at least 20 edges contain both endpoints of some pair in P. For each matched pair independently choose one of its two opposite color assignments with probability one half; color unmatched vertices independently and fairly. Every hit edge is deterministically bichromatic.

An unhit edge contains at most one vertex from each matched pair. Its five vertices therefore belong to five distinct independent random components, each giving a fair bit. Its monochromatic probability is exactly

    2*(1/2)^5 = 1/16.

There are at most 15 unhit edges. The union bound puts the probability of at least one monochromatic edge at most 15/16, strictly below one. A proper coloring exists. This proof does not assume independence between different edge events.

## Explicit counterexample to the matching guarantee

All coordinates below are in F5. Take the 24 points

    V = F5^2 minus {(0,0)}.

The 30 affine lines on F5^2 are the five vertical lines x=c and the 25 lines y=mx+c, with m,c in F5. Every line has five points and every pair lies on exactly one line, by solving the linear equation for its slope or using its common vertical coordinate.

Let v=(0,0), a=(0,1), b=(1,0). The six lines through v leave six disjoint four-element sets after v is deleted; these partition V. Denote the vertical one by G_vertical and the five slope blocks by G_m. Form 30 base edges as follows:

* retain all 24 lines that avoid v;
* replace the vertical line through v by G_vertical union {b};
* replace each of the five slope lines through v by G_m union {a}.

These are 30 distinct five-element sets. Each altered edge contains four points of one original line and one point outside it, so it is not any original affine line. Distinct altered edges contain disjoint four-point blocks and cannot coincide. Every pair of points in V remains covered: its unique original affine line either is retained or has only v replaced while both points remain in its four-point block.

Add these five further edges:

| Edge | Points |
| --- | --- |
| E1 | (0,2), (0,3), (0,4), (1,1), (1,2) |
| E2 | (1,3), (1,4), (2,0), (2,1), (2,2) |
| E3 | (2,3), (2,4), (3,0), (3,1), (3,2) |
| E4 | (3,3), (3,4), (4,0), (4,1), (4,2) |
| E5 | (4,3), (4,4), (0,2), (0,3), (0,4) |

Each contains two points with the same first coordinate and another point with a different first coordinate, so cannot be an affine line. They avoid a and b, whereas every altered base edge contains a or b. They are mutually distinct. Consequently the full H has exactly 35 simple five-edges and covers all 276 vertex pairs.

In the base, a has degree 11, b has degree seven, and the other 22 points have degree six. The five extra edges cover each of those 22 points once and the three points (0,2),(0,3),(0,4) twice. The full degree spectrum is therefore

    7^20 8^3 11^1,

with degree sum 175 and minimum degree seven.

## Why every matching hits at most19 edges

For a pair p, let lambda_0(p) be its codegree in the 30 base edges. Its original affine-line occurrence contributes exactly one. All additional occurrences arise from the inserted points a or b. The pair {a,b} gains two extra occurrences, one from the altered vertical edge and one from the altered horizontal edge. Every other pair gains at most one extra occurrence, and only if it contains a or b.

Define alpha(a)=alpha(b)=1 and alpha(u)=0 for every other vertex. For every pair {u,w},

    0 <= lambda_0({u,w})-1 <= alpha(u)+alpha(w).

Thus any vertex matching P satisfies

    sum_{p in P} (lambda_0(p)-1) <= sum_{u in V} alpha(u) = 2.

If B(P) is the number of base edges hit by P, summing their hit indicators gives

    B(P) <= sum_{p in P} lambda_0(p)
          <= |P|+2 <= 12+2 = 14.

The five added edges can contribute at most five further hits. Every matching therefore hits at most 19 full-H edges. This proves absence of a matching hitting 20 without enumerating matchings. It does not assert that the upper bound 19 is attained.

The example is colorable. One red set is

    {(0,1),(0,3),(0,4),(1,0),(1,2),(1,3),
     (2,1),(2,3),(2,4),(3,0),(3,1),(3,4),(4,1)};

all other points are blue. The literal-edge verifier checks both colors on every one of the 35 edges. This is a counterexample only to the auxiliary matching guarantee, not to Property B.

## A universal weak matching bound

For a uniform random perfect matching on an even n-point set, a fixed pair occurs with probability 1/(n-1), and two prescribed disjoint pairs occur together with probability 1/((n-1)(n-3)). A five-element set has ten possible pairs and 15 choices of two disjoint pairs. It can contain at most two matching pairs, so exact inclusion-exclusion gives hit probability

    10/(n-1) - 15/((n-1)(n-3)).

For n=22 and 35 edges the expected number of hit edges is 875/57>15, proving a matching hitting at least 16 edges. For n=24 the expectation is 325/23>14, proving at least 15 hits.

For n=23 use a uniformly random near-perfect matching with one unmatched point. The same two probabilities become 1/23 and 1/(23*21), yielding the same expectation 325/23 and a guarantee of at least 15 hits. These weak bounds do not use pair coverage or degree assumptions. No claim is made that they are sharp, or that the 24-point counterexample settles the separate optimal matching guarantee at 22 or23 points.

## Exact artifacts and independent verification

`COUNTEREXAMPLE.json` contains all 35 literal edges, their coordinates and degrees, the coloring, all 276 base pair codegrees and the two-vertex dual. `construct.py` generates this single explicit control example. `verify.py` independently reads the literal edge data, without regenerating the affine construction or searching for a matching or coloring, and checks simplicity, all 276 pair incidences, the degree spectrum, all 276 dual inequalities and the given proper coloring. `VERIFICATION.json` records PASS, with universal matching-hit upper bound19. Runtime was under0.002 seconds.

```sh
python3 -B context/propertyb35-paper/round01/middle/pairing_global/verify.py
```

The pairing sufficiency can remain a useful conditional lemma. Its proposed unconditional 20-hit selection step is false even in the minimum-seven 24-point branch. Further work using this approach would need an additional hypothesis excluding the explicit control structure or a weaker sufficient condition; no such extra assumption follows merely from the budgets tested here.
