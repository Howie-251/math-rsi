# Cartesian and strong graph products: complete optimistic screen

A small integer dynamic program checked all27 degree/diameter cells against the saved2026-10-26 baseline. Each factor is allowed the ordinary Moore upper bound, even when that bound is unattainable. Thus rejection is valid without constructing factors; a surviving numerical bound would not prove existence. This task generated no graph and ran no BFS.

## Scope and formulas

Every factor is nontrivial, finite, connected, simple and undirected. With actual maximum degree d and diameter r, its order is at most M(d,r)=1+d*sum((d-1)^j,j=0..r-1). A connected graph of degree one is exactly K2 and has diameter one, so this exceptional factor contributes(d,r,M)=(1,1,2). Factors of degree at least two have r>=1.

For a Cartesian product, vertex counts multiply, maximum degrees add, and diameters add. A product path must change coordinates separately; shortest paths in each coordinate concatenate, proving the exact sum distance formula. Therefore enumerate all factor parameters with sum d_i<=Delta and sum r_i<=D, and maximize product M(d_i,r_i). At least two factors are required.

For a strong product, vertex counts multiply and maxdegree+1=product(d_i+1); its diameter is max r_i. At a product vertex, its closed neighborhood is the Cartesian product of the factor closed neighborhoods. Maximum-degree factor vertices can be chosen independently, proving the degree formula even for nonregular factors. Each coordinate advances at most one edge per step, and shortest coordinate paths can be followed simultaneously, proving the maximum distance formula. Therefore enumerate product(d_i+1)<=Delta+1 and max r_i<=D, maximizing the same factor-bound product.

The DP keeps the maximum bound at each exact factor count and exact degree/diameter resource state, appending every allowed(d,r) factor. Cartesian factor count is at most D because every r>=1. Strong factor count is at most floor(log2(Delta+1)) because every d_i+1>=2. These bounds make the enumeration finite and complete for the stated formulas. Keeping only the largest bound in a state is safe because future transitions depend only on those resources and multiply by positive factor bounds.

## All27 results

|Delta|D|Saved baseline|Cartesian optimistic upper|Strong optimistic upper|Result|
|---:|---:|---:|---:|---:|---|
|4|3|41|20|4|both excluded|
|4|4|104|44|4|both excluded|
|4|5|364|92|4|both excluded|
|5|3|72|34|14|both excluded|
|5|4|252|106|18|both excluded|
|5|5|650|322|22|both excluded|
|6|3|120|52|14|both excluded|
|6|4|441|212|18|both excluded|
|6|5|1518|852|22|both excluded|
|7|3|170|78|44|both excluded|
|7|4|684|374|92|both excluded|
|7|5|2810|1874|188|both excluded|
|8|3|253|111|49|both excluded|
|8|4|1100|604|92|both excluded|
|8|5|5334|3628|188|both excluded|
|9|3|585|150|106|both excluded|
|9|4|1768|914|322|both excluded|
|9|5|9020|6402|970|both excluded|
|10|3|650|200|106|both excluded|
|10|4|2485|1371|322|both excluded|
|10|5|33397|10532|970|both excluded|
|11|3|715|260|212|both excluded|
|11|4|3444|1974|852|both excluded|
|11|5|37628|16402|3412|both excluded|
|12|3|810|328|212|both excluded|
|12|4|5832|2733|852|both excluded|
|12|5|42342|24603|3412|both excluded|

## Consequence and boundaries

Numerical surviving cases: 0.
Every optimistic upper bound is already no larger than its saved public construction baseline. Consequently neither plain Cartesian nor plain strong products of two or more nontrivial connected factors can improve any of these27 saved bounds. No factor generation or product graph search is warranted for this unchanged method. Since a lower bound remains valid if a public table later increases, the exclusion against the saved constructions remains valid.

This does not exclude arbitrary graphs, modified products with deleted/added/rewired edges, tensor/direct or lexicographic products, or lifts with coordinate-dependent connections. Arbitrary factors inside the two specified outer product operations are covered, whether or not those factors themselves have further structure. No claim of a new general degree/diameter bound or original theorem is made.

## Cost and files

One worker; measured DP/input CPU 0.015492400 seconds, below10 seconds. Report serialization is outside that core measurement. RESULTS.json records all27 cells, complete maximizing factor parameter lists and DP counts. screen.py is the reproduction command source. No actual graph was generated.
