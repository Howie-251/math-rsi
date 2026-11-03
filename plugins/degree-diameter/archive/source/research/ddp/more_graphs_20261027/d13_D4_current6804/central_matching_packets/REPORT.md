# Central plain-edge packets work; the unchanged module-eight transfer cannot connect

2026-10-27. Status: complete mechanism profile and structural transfer obstruction. No graph or action sweep was generated.

## Inherited mechanism and quantitative prediction

The primary author search README already states the central plain-letter insertion tiling principle, in lines25–29 of the locally saved `../../d12_D4_current6156/route_capacity_analysis/author_README.md`. This is inherited source knowledge. The new frozen quantitative prediction was that at least one current-chart three-line-word packet realizes that principle.

Let λ=t1t2t3 be one of the 36 reduced words in a,A,b,B. Insert z at position j, for j=0,1,2,3. Since z is central in the controller, every insertion ends at λz. Write γ(x)=−x+c and Mλ=M3M2M1. The four fiber images are

    −Mλ x + c_j + Hλ,
    c_j = M3 ... M_(j+1) c,
    Hλ = span(M3 M2 d1, M3 d2, d3).

The z insertion changes signs of some free line controls, which leaves their span unchanged. Therefore the common linear source term is −Mλ x. This argument uses the commutation of the scalar linear part −I with the chart matrices. The complete affine map γ need not commute with them: Mc and c can differ, and those differences supply the useful residues.

For every one of the 36 packets, Hλ has dimension three. With its normalized normal n, coverage is complete exactly when the four residues n·c_j contain all three elements of F3. This happens for **32 of36 packets**. Only baB, bAb, bAB, BaB have two residue classes and cover54 points. These union sizes hold for every source coordinate by the common linear term; an 81-source brute-force repetition is unnecessary.

For example, λ=aaa has normal (0,1,2,1) and residues (0,1,2,2), so its four insertions tile all81 points. The central edge thus supplies a genuine whole-fiber route certificate at λz using three line moves and one plain move. This describes a resource present in the mixed degree13 source. It is not a proof that no degree12 construction on84 controller vertices can exist; its chart and route conditions differ from the fixed degree12 source.

## Phase-only capacity has room

All781 words of length at most four over a,A,b,B,z were included, with phase steps (1,−1,4,−4,6). Summing individual route-image cardinalities in each phase gives the safe upper bounds

    [1557,1311,1839,1350,1365,1731,1280,1731,1365,1350,1839,1311].

These sums can count the same endpoint repeatedly. They are upper bounds, not coverage claims or a full-rank assumption. The minimum1280 exceeds8·81=648, so this coarse phase count does not rule out a size-eight translation module.

## A stronger uniform obstruction to the specified transfer

Keep exactly a=(1,1), b=(0,4), z=(0,6), but replace the translation module C7 by C8. For any valid action r in the units modulo8, multiplication is

    (i,j)(k,l) = (i + r^j k mod8, j+l mod12).

Every unit r is odd. Hence χ(i,j)=i−j modulo2 is a group homomorphism: χ(gh)=χ(g)+χ(h). All three fixed generators have χ=0, as do their inverses. Their generated component therefore lies in the proper index-two subgroup i≡j modulo2, containing only48 of the96 controller vertices. At every phase, all four opposite-parity translation values are unreachable, together with their full81-point fibers. No choice of fiber chart can cure absent controller routes.

In particular this applies to the proposed r=3,5,7 actions; their twelfth powers are1 and sixth powers1, so they do define an action and central z, but the unchanged generator coordinates still cannot connect the graph. The module-eight literal transfer is thus excluded before selecting or generating one7776-vertex graph. No r sweep, source BFS, or candidate BFS was run. This exclusion depends on the retained integer generator coordinates; it does not exclude different generators or odd translation modules.

The profile used0.034883321 CPU seconds. Full36-packet normals/residues, common matrices, image sizes, and phase data are in `RESULT.json`; the frozen prediction is supported. `profile.py` is the complete one-shot computation. The requested scope has ended, with no follow-up action or search pending.
