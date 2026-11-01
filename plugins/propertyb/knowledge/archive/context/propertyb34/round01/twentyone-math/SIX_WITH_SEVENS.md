# Twenty-one vertices: unique degree six with seven-degree points

2026-10-13. **Complete paper candidate**, conditional only on the existing locked-permutation probability and bad-link quota lemmas. H is simple, pair-covering, five-uniform, with 21 vertices and 34 edges. Its unique minimum-degree point x has degree six, and at least one vertex has degree seven. We prove Property B. Lean implementation remains outstanding.

Let λ denote codegree, τ common-three multiplicity, and r the number of seven-degree points. The degree sum is 170. A degree-six point has total codegree excess four; a degree-seven point has excess eight. The exact profiles below use those identities and do not impose arbitrary extra structure on H.

## 1. Two seven-degree locks

For two seven-degree points y,z, pairs of codegree at least five already have strict double bounds. Otherwise the complete (6,7,7) three-lock domain has 120 profiles, 118 strict. Its only residues, in pair order (xy,xz,yz), are

- A: $(1,1,2)$ and τ(x,y,z)=1;
- B: $(2,2,1)$ and τ(x,y,z)=0.

If r≥3, all x-to-seven codegrees are therefore the same, either one or two. In case A every seven-degree point lies in the same unique edge through its pair with x. Select three of them; the common-four trace is one, and the only additional three-seven trace has multiplicity zero or one. In case B, select any three; every triple containing x and two sevens vanishes, and the three-seven trace is again zero or one. All four (6,7,7,7) profiles have strict bounds. The largest is 23393/24310.

It remains to treat r=2 or r=1.

## 2. Exactly two seven-degree points

Let y,z be these points. The other eighteen vertices are at least eight-degree. The baseline degree sum is $6+2\cdot7+18\cdot8=164$, so the degree-eight set L has at least twelve points.

### Residue B

The pairs xy,xz have codegree two and yz has codegree one. At most two points of L can be nonunit neighbors of x, because the two sevens consume two of x's four excess incidences. Choose u∈L unit to x. If either λ(y,u) or λ(z,u) is at least three, the relevant (6,7,8) triple is strict (or a codegree-at-least-five double is strict). Hence both may be assumed in {1,2}.

Now (x,y,z,u) has degrees (6,7,7,8), pair vector $(2,2,1,1,b,c)$, b,c∈{1,2}, and τ(x,y,z)=0. The complete four-lock domain has twenty profiles; all are strict, with maximal bound 641/663.

### Residue A

There is a unique edge e containing x,y,z. Set

$$U=\{u\in L:\lambda(x,u)=1,\ u\notin e\}.$$

At most four L points are nonunit to x and e contains at most two L points, so |U|≥6. For every u∈U, triples xyu and xzu vanish. The same (6,7,8) argument bounds λ(y,u),λ(z,u) by two. The four-lock domain is strict unless both are one. Thus either a coloring is obtained or every U point is unit to y and z.

There are exactly two edges containing y,z: e and another edge f. Since f contains at most three U points, the set S=U\f has size at least three. Choose distinct u,v∈S. Their codegree is at most two, since otherwise (x,u,v) is a strict (6,8,8) profile.

For locks (x,y,z,u,v), the degree tuple is (6,7,7,8,8); pair vector is $(1,1,1,1,2,1,1,1,1,b)$ with b∈{1,2}; the exact xyz trace is one; and every other trace containing two among x,y,z and an additional lock vanishes. There are eleven possible profiles. All have strict five-lock witnesses after avoided-lock deductions. The largest bound is 11369/11440 (another previously failing profile has 2131/2145). This completes r=2.

## 3. Exactly one seven-degree point

Let y be that point. The other nineteen vertices are at least eight-degree. The baseline is $6+7+19\cdot8=165$, hence |L|≥14. The complete (6,7,8) triple table has 122 profiles after the degree-six excess filter. Its seventeen residues force, for every z∈L,

$$a=\lambda(x,y)\in\{1,2\},\qquad \lambda(x,z),\lambda(y,z)\in\{1,2\}.$$

Pair codegrees ≥5 were already excluded by strict doubles, while codegrees three and four are in the strict triple table.

Let U be the unit neighbors of x in L. At most $4-(a-1)$ L points are nonunit to x, so |U|≥10 if a=1 and |U|≥11 if a=2. Apply `SIX_UNIT_SET_LEMMA.md`: unless a coloring is already obtained, all U-pairs have codegree two and every x-edge contains at most two U points.

For each u,v∈U, the full (6,7,8,8) four-lock table uses pair vector $(a,1,1,b,c,2)$, b,c∈{1,2}. Its residuals have the following exact implications:

- If a=2, b=c=1 and τ(x,y,u)=τ(x,y,v)=0.
- If a=1, b=c, and the common-four multiplicity of x,y,u,v is zero.

These implications follow from the saved complete 134-profile table; profiles with U-pair codegree one were included too, although the unit-set lemma has already excluded them here.

If a=2, the two xy-edges contain no U point. Only four x-edges remain, each containing at most two U points, contradicting |U|≥11.

Suppose a=1. The equality b=c for every pair forces λ(y,u) constant on U. That value cannot be two, since |U|≥10 would exceed y's total codegree excess eight. Therefore all U points are unit to y. Let e be the unique xy-edge. Its intersection with U has size at most one, by the zero common-four condition. Thus S=U\e has size at least nine, and τ(x,y,u)=0 for every u∈S.

The other five x-edges cover S, so one contains two distinct points u,v∈S. Choose a third point w∈S. The five locks (x,y,u,v,w) have degrees (6,7,8,8,8), pair vector

$$(1,1,1,1,1,1,1,2,2,2),$$

no trace containing x,y and an additional lock, and τ(x,u,v)=1. Exactly fourteen profiles remain. Nine have strict single-layout witnesses. The other five have strict rational certificates using one common actual bad-pair count vector across all layouts; their largest bound is

$$169595751971/171600000000<1.$$

Therefore the failure upper bound is less than one and a valid coloring exists. This finishes r=1 and the entire claimed branch.

## 4. Numerical and logical evidence

`SIX_WITH_SEVENS_WITNESSES.json` contains 404 strict single-layout witnesses. `verify_exact.py` independently replays all A/B/C rows by labelled injections and checks complete unordered-slot capacities, avoided-lock quota duals, 34-edge totals and selected degrees. All 404 passed; maximum bound 24301/24310.

The five final shared-vector certificates are in `ONE_SEVEN_FIVE_DUAL_JOINT.json`; `verify_joint.py` directly replays their saved layouts using independent A/B/C and independent injection weights, checks nonnegative rational layout mass summing to one, coefficients 0≤β≤γ, actual avoided quotas, all capacities and repaired dual penalties. `ONE_SEVEN_FIVE_DUAL_JOINT_VERIFIED.json` records all five passing checks. Candidate generation uses a floating-point LP only to propose coefficients; the final bound and checks are exact rationals. Layout base positions must be sorted before a label permutation is applied; the local implementation does so.

For the common actual bad-pair vector z, each layout ℓ gives an upper bound $F_\ell+\sum_i\min(a_{\ell i},c_{\ell i}-w_{\ell i}\cdot z)$. The conditional random spaces and failure probabilities may differ between layouts. If a rational weighted average of these upper bounds is less than one, some layout with positive weight has its own upper bound less than one; that layout therefore supplies a valid coloring. The common object is H and its actual bad-pair vector z, not a single layout-independent failure probability. Pointwise convex combinations upper-bound each minimum, and shared avoided-lock quotas lower-bound weighted bad-pair loss; explicit capacity penalties correct any dual excess. The certificate therefore does not interchange a layout-dependent worst-case count vector with averaging. The abstract mixed-layout inequality is the same one documented by the parent in `middle-math/MULTI_BAD_LAYOUT_PROPOSAL.md`.

This is complete paper coverage for unique-six/with-seven inputs, not a Lean verification or the full 21-vertex theorem. The general minimum-degree-six result combines this note with `MULTIPLE_SIX.md` and `UNIQUE_SIX_NO_SEVEN.md`. Minimum degree seven and eight remain separate obligations.
