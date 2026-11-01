# Degree-sensitive Γ-prefix: independent bounded pilot

Scope: 21 original vertices, 35 distinct original five-edges. This checks the new analytic theorem and five aggregate moment rows only. The retained `t≤13` frontier is conditional on its separate actual four-core gate. No original hypergraph is constructed, no complete A2/A3 branch is closed, and no Lean command or v2 access occurs.

## Analytic coefficients and deletion direction

I independently recomputed the centered Gram expansion. Each diagonal entry is `5−25/21=80/21`; an off-diagonal entry for intersection j is `(j−1)−4/21`. Thus its square is `(j−1)^2−8(j−1)/21+16/441`, and summing ordered pairs and diagonal entries gives exactly

`tr(B²)=16N(N+399)/441+2Q−16T/21`.

The centering projection has rank 20 and B is positive semidefinite. Applying `tr(B²)≥tr(B)²/20` gives `Q−8T/21≥152N(N−21)/441`. The identity `Q=T+2a0+2a3+6a4` then gives the coefficient 273 in the numerator and denominator 882 of the first lower bound. The five per-pair coefficients are `29,0,13,68,165`, divided by 21. Bounding them by `68e/21+97a4/21` gives exactly `1428e+2037a4≥152N(N−21)`.

Deleting k actual original edges loses

`Σdeleted F Σv∈F (d(v)−1) − Σv C(r_v,2)`.

The first term is at least `k(S5−5)` and the subtracted term is at most `4C(k,2)`. Hence the remaining first intersection moment is **at most** `min(W,W−k(S5−5)+4C(k,2))`. This direction is the required one: the e lower bound decreases with T, so replacing T by this upper bound weakens it validly. Also replacing remaining a4 by original t weakens both lower bounds. For the top k Γ degrees, the remaining Γ edge count is `E−prefix+h`, with `h≤C(k,2)`, giving the stated prefix upper bound. No A1 center or role constraint was used.

The root proof's example giving `q1+q2≤52` is valid but not the strongest combined result: for W655/S5=35/E78/t10, (4) supplies B2=28, so the actual combined cap is **51**. The proof's first bound alone gives B2≥27 and cap52.

## Exact finite domain and dominance

The separate imported old ≤34 / 21-point low-degree local result implies the **original** non-B H is edge-critical in A2/A3. Each original edge then has at least five distinct singleton neighbors, giving q≤29. The new universal Γ-minimum theorem gives q≥3. No whole-T34 import is made.

Every actual Γ degree list sorts nonincreasingly into precisely 35 slots q∈[3,29], has sum 2E, and obeys all 13 new prefix inequalities. We optimize over every integer sequence with these necessary conditions. Graphicality and original-H realizability are not imposed, so this is a valid upper relaxation. The objective is `Σ f(34−q)`, where f is the maximum wedge count of five groups with that total; balancing the five integer groups proves its formula.

`PREFIX_DP.cpp` contains two exact solvers:

* Position DP: after n slots the state is (last degree, prefix sum). It considers every next q from 3 through last. The prefix cap and the elementary remaining-sum feasibility checks are necessary conditions. At fixed state, all later admissibility conditions depend only on n, last and sum; therefore retaining only the largest accumulated objective loses no optimum. Parent pointers reconstruct an optimizer.
* Independent multiplicity DP: assigns the count of each q from 29 down to 3. Its state is (current q, number of slots, sum), enumerates all possible counts, and checks every newly crossed prefix, including positions inside an equal-degree block. This enumerates every sorted list exactly once. Its maximum must equal the first DP.

Both DPs agreed on all five complete finite optimizations. `RUN_PILOT.py` independently recomputes all prefix caps using Python integer ceiling, recomputes f as explicit pair products between balanced groups, checks every returned optimizer, and reallocates the actual saved moment row's shared P budget. Neither solver imports the old A1-specific R bound, zero/one-degree rules, 13th-position rule, or A1 caps.

The closed box cap uses singleton degrees s∈[5,31], total 2n1. Its endpoint allocation is valid because `f(s+1)−f(s)=s−floor(s/5)` is nondecreasing: shifting mass from a smaller interior value to a larger one cannot lower the objective.

## Preselected five inputs and results

The source file contains 20995 rows; its t≤13 subset has 6953 rows. The previous critical-box re-sieve leaves 5813. After the mandatory witness, selection was fixed before running any additional DP: closest surviving critical-box witness; largest surviving margin; largest E (tie largest margin); and largest margin among W657. Thus this is a five-case diagnostic, not a frontier sample estimate.

|W,S5,E,t|Threshold T|Box cap|Prefix maxP|Final L|L−2722720|
|---|---:|---:|---:|---:|---:|
|655,35,78,10|12989|12696|12597|2715342|−7378|
|656,35,77,9|13031|12707|12608|2716788|−5932|
|660,35,53,12|13939|13416|13416|2812356|89636|
|660,35,87,0|12645|12386|12114|2708226|−14494|
|657,35,53,13|13939|13416|13416|2805384|82664|

Three tested saved rows now lie strictly below the repair threshold. The two worst-margin rows remain above it, with **zero improvement** in their P cap. Both have E53, so sum q=106 and q≥3 force the unique sorted sequence `(4,3^34)`. It meets every prefix bound and gives maxP13416. Consequently this entire family of prefix inequalities cannot reduce these two necessary-relaxation witnesses: the q-domain already has only one sequence. More original-H coupling, stronger capacities, or a different necessary condition is needed there. These are aggregate witnesses, not noncolorable examples.

The mandatory witness optimizer is `(29,22,6,6,3^31)`. The close surviving witness uses `(29,19,7,6,3^31)`. The largest-E optimizer is `(29,14,9,8^5,4,3^26)`. Full original moment rows, caps, exact optimizer lists, capacities and objectives are in `RESULT.json`.

## Reproduction and budget

```
c++ -std=c++17 -O2 PREFIX_DP.cpp -o prefix_dp
python3 RUN_PILOT.py
```

The pilot script and all five double-DP child runs used approximately 0.098 CPU seconds and 0.101 wall seconds. The preceding compile/write/first-run command took 1.502 wall seconds; its compiler CPU was not separately metered. Each child execution has a five-second timeout. This is far below the 20-second computation budget and five-minute wall limit. No full 35083-row DP, new H search or local-lock search was run.

This independent check is same-family/provisional; its reproducible exact finite optimization and coefficient calculations are the substantive evidence. The root remains responsible for the final theorem scope and acceptance.
