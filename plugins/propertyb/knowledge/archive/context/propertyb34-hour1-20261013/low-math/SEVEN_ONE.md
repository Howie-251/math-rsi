# T34 on 20 vertices: a unique degree-seven point

2026-10-13 first-hour sprint. A complete paper candidate for the final minimum-degree-seven subbranch. Six residual four-lock types force an elementary incidence contradiction.

## Target, assumptions, and invariant object

H is simple, pair-covering and 5-uniform, with 20 vertices and 34 edges. Its unique degree-seven point is x; every other vertex has degree at least eight. Let L be the degree-eight points. Since `7+19*8=159` and total degree is 170, at most eleven of the other nineteen points exceed degree eight. Therefore `|L|≥8`.

We use the existing conditional greedy-coloring failure bound `sum_k min(A_k,B_k,C_k-D_k)`. A strict bound supplies Property B. The argument below assumes no selected witness has supplied this yet and derives a contradiction from the residual profiles.

## Notation and derivation map

λ denotes pair codegree, τ a three-point common-edge multiplicity. Exact trace counts are the multiplicities of edge intersections with the chosen lock set. Distinguish them from τ: a common-edge multiplicity also includes any larger exact trace containing the three points.

1. Strict double/triple witnesses restrict all codegrees among x and L to one or two.
2. A complete four-lock trace calculation, with known three-lock alternatives and exact avoided-lock duals, leaves six types up to permutations of the three eight-degree labels.
3. Partition L by codegree with x. The six types exclude every possible partition of at least eight points.

## Main derivation

### Step 1: restrict the codegrees

Every pair of degrees (7,8) or (8,8) with codegree at least four has a strict double-lock witness. Thus, if no such witness has completed the proof, these codegrees are at most three.

If some z∈L has λ(x,z)=3, choose any other w∈L. The (7,8,8) triple has all pair codegrees at most three and one of the two x-codegrees equal to three. Every such triple profile has a strict witness. Hence λ(x,z)∈{1,2} for all z∈L.

If some pair z,w∈L has λ(z,w)=3, their (7,8,8) triple with x also has a strict witness for both x-codegrees in {1,2}. Thus every pair codegree among x and L lies in {1,2}.

### Step 2: the complete local residual list

Choose any three distinct points a,b,c of L and lock x,a,b,c. There are six pair codegrees in {1,2}. For each choice, let q be the exact four-point trace multiplicity, and let t_123,t_124,t_134,t_234 be exact three-point traces. The complete nonnegative domain is recovered by

`0≤q≤min(pair codegrees)`,

`l_ij = λ_ij-q-sum_(T contains ij) t_T ≥0`,

`l_i = d_i-sum_(S contains i, |S|≥2) l_S ≥0`,

`l_empty = 34-sum_(S nonempty) l_S ≥0`,

with degrees (7,8,8,8). Enumerating these integer trace parameters gives 674 labelled profiles. This is a local count identity/inequality domain, not enumeration of H.

Each profile is handled by a strict triple witness, a strict four-lock witness, or one of the six following types, up to permutation of a,b,c. All residuals have `λ(a,b)=λ(a,c)=λ(b,c)=2`, no common four-point edge, and the table lists the **common-edge** multiplicities τ:

|Type|λ(x,a),λ(x,b),λ(x,c)|τ(x,a,b),τ(x,a,c),τ(x,b,c),τ(a,b,c)|
|---|---|---|
|AAA|(1,1,1)|(0,0,0,0)|
|ABB|(2,2,1)|(0,0,0,0)|
|BBB-0|(2,2,2)|(0,0,0,0)|
|BBB-L|(2,2,2)|(0,0,0,1)|
|BBB-x1|(2,2,2)|(0,0,1,0)|
|BBB-x2|(2,2,2)|(0,0,2,0)|

In the ABB row the two B points are a,b and the A point is c; its label only records one A and two B points. In particular **no residual has exactly two A points and one B point**.

### Step 3: eliminate all six globally

Partition `L=A⊔B`, where λ(x,a)=1 for a∈A and λ(x,b)=2 for b∈B. Since the same local alternatives apply to any triple of L, every triple must fit one residual above unless a coloring witness has already been found.

If `|A|≥2` and B is nonempty, choose two points of A and one of B. There is no such residual, a contradiction.

If `|A|=1` and B is nonempty, then `|B|≥7`. For every two distinct b,c∈B, the triple consisting of the unique A point and b,c has the ABB residual. Thus no edge containing x can contain two B points, and no edge containing x can contain both the A point and any B point. Each B point lies in exactly two x-incident edges, while the A point lies in one. These are all distinct edges, requiring `2|B|+1≤7`, impossible.

If B is empty, then `|A|≥8`. For any pair of A points choose a third; the AAA residual says that no x-incident edge contains the pair. Every A point lies in an x-incident edge, so seven such edges can cover at most seven A points, a contradiction.

Finally if A is empty, then `|B|≥8`. An x-incident edge cannot contain three B points: for those three points all three common-edge multiplicities involving x would be positive, whereas each BBB residual allows at most one of them to be positive. Hence each of the seven x-incident edges contains at most two B points. Counting incidences gives `2|B|≤14`, again impossible.

These cases exhaust L=A⊔B. Therefore one of the strict local probability witnesses must apply, and H has Property B.

## Verification and evidence

`verify_seven_one.py` independently recomputes the chosen exact bounds and checks every A/B/C row by labelled injections. Every avoided-lock certificate is additionally checked from its actual type-pair capacities, two-direction weights, subfamily quotas, nonnegative rational multipliers, and capacity penalties; floating LP outputs are not treated as proof.

`SEVEN_ONE_VERIFIED.json` maps every one of the 674 labelled profiles to its strict witness or canonical residual, and records exactly six residual orbits. The three extra strict four-lock orbits discovered by repositioning have bounds `142/143`, `6377/6435`, and `259/260`; their raw records are in `ONE7_POSITION_REFINEMENT.json`. Older nine-orbit residual data are retained as an intermediate diagnostic, superseded by this six-orbit coverage.

## Status and boundaries

COHERENT AS STATED as a complete paper candidate for the unique-seven branch. Combined with `SEVEN_TWO.md` and `SEVEN_MANY.md`, it supplies all minimum-degree-seven cases on 20 vertices. The degree-eight branch remains open, and none of these new branches is yet a Lean theorem. The substantive review obligations are the finite local-domain coverage, the strict witnesses and deductions, and the universally quantified residual-to-incidence contradiction above.
