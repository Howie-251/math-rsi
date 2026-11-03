# Three new neighborhoods cover B0; the fixed43-set pool still has maximum40

The route prediction is **SUPPORTED**: all three new sets, indices0,8,17 of the fixed-peripheral core-swap rule, independently R4-cover original B0 in its entirety. Core omissions0 and peripheral omissions0 for each. This coverage was actually computed, not inferred from the rejected full-automorphism extension.

| New index | R3 size | R4 size | Core missing | Peripheral missing |
|---|---:|---:|---:|---:|
| 0 | 11647 | 51417 | 0 | 0 |
| 8 | 11040 | 51417 | 0 | 0 |
| 17 | 11062 | 51417 | 0 | 0 |

The same three distance arrays give each new set's distance to all40 original sets and to the other new sets. Every required set-distance is at most3. Original40 R4 coverage and780 old-old pair conditions were inherited, not rerun. Thus route incompatibility is not the obstruction in this fixed pool.

## Complete improving-subset check

Allow each of the40 original sets and3 new sets at most once. Every family with more than40 members must contain a nonempty new subset A and drop an old subset D of size at most|A|−1. The enumeration tested totals in descending order:

| Desired added vertices | All choices tested | Failure reason |
|---|---:|---|
| 43 | 1 | B0 port capacity |
| 42 | 43 | B0 port capacity in all43 |
| 41 | 903 | B0 port capacity in all903 |

All947 improving choices violate at least one old-port inequality `usage(v)≤13−degree_B0(v)`. None failed the route compatibility test. The unchanged original40 is already feasible, so the exact optimum of this fixed0/1 pool is **40**. No solver or complete new graph was used or produced.

The combinatorial scope is exhaustive: at total41 the choices are3 one-new/no-drop,120 two-new/one-drop, and780 three-new/two-drop; total42 has3 two-new/no-drop and40 three-new/one-drop; total43 has the single all-three/no-drop family. Smaller families cannot improve40. This does not exclude other neighborhoods, repeated new sets outside the specified0/1 model, modified guards, or other constructions.

## Subsequent saved-degree check closes arbitrary multiplicities of this43-set pool

The three new sets each contain a B0 port of spare capacity1:

| New index | One explicit witness | B0 degree | B0 spare |
|---|---:|---:|---:|
| 0 | 7030 | 12 | 1 |
| 8 | 12230 | 12 | 1 |
| 17 | 14782 | 12 | 1 |

All additional minimum-spare witnesses are saved in `MULTIPLICITY_LIFT_CHECK.json`. These are capacity witnesses; they need not be exclusive to one set. For nonnegative integer multiplicities, the port inequality at such a vertex implies the corresponding k_i≤1 regardless of which other sets use that port. The old40 individual bounds k_i≤1 were already proved. Therefore **all43 integer variables are necessarily0/1**, and the completed0/1 maximum40 is also the exact maximum for arbitrary nonnegative multiplicities of this same43-set pool. The earlier untested-multiplicity limitation above is thus resolved by this follow-up, without a new packing run.

This check read only the saved original-B0 `degree13.u8.bin`, its51417/324451 metadata, and the three saved sets. No source edge read, BFS, solver, or packing enumeration was repeated. Other neighborhoods, changed guards, and other graph operations remain outside the exclusion.

## Artifacts and cost

`CANDIDATE_COVERAGE.json` stores the three exact sets, complete omission lists (empty), R3/R4 counts, and all old/new set distances. Distances are capped at5, meaning greater than4; every relevant compatibility distance here is≤3. `R3.u64.bin` and `R4.u64.bin` have three rows in order0,8,17, each804 little-endian uint64 words with bit v representing original label v. `RESULT.json` and `TERMINAL.json` record all combination counts and the final maximum40. `PREDICTION.md` predates calculation.

One read of original51417/324451 B0, exactly3 new multi-source radius4 computations, CPU0.372726496 seconds, within5CPU. No original40 ball recomputation, sourceD5 all-root BFS, SAT/MIP, new guard, extra candidate, or new graph. Dominated candidate37 was not subjected to a ball computation. The bounded task is complete and this exact pool stops.
