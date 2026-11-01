# Independent exact audit of the 77 shared-capacity residuals

**Result:** all76 rational certificates pass a second standard-library-only verifier. The unique remaining graph has the short integer repair below. Thus this particular complete77-residual six-label domain is covered, conditional on its previously proved actual-input reduction and complete census. This report does not claim the entire nine-positive gate or the global m(5) target is proved.

Review independence: same-family; acceptance status: provisional. `VERIFY.py` does not import SciPy, the LP discovery code or either census generator. It uses exact `fractions.Fraction` arithmetic and does not rerun an LP.

## Complete binding and rational certificates

The verifier reads `../CENSUS_SUMMARY.json` and selects exactly its raw-bound-nongated records not resolved by the two-isolated-label argument. This gives77 distinct graph vectors. The complete graph-key set is exactly the set of77 rows in `../joint_cover_lp/ALL77.json`, with no missing or duplicate key. The source census's already established417328-labelled/981-orbit completeness is not rerun here.

For every row, the verifier independently reconstructs the six positive four-sets from the15 graph multiplicities: each graph edge instance gives one shared point, followed by private points restoring each label to size four. It checks exact equality with the stored positive sets. It then enumerates all three- and four-point transversals from the reconstructed point set, independently recovering C3,C4, union size, positive frequencies and the stored budgets `(3,4,20,7−frequency(v))`. It independently recovers the complete active negative-target count rather than trusting that count as a certificate premise.

For each rational certificate it verifies that every listed positive candidate really hits all six positives, has size three or four, has nonnegative rational weight, occurs only once, and that the total weight is exactly one. The three shared budget multipliers and all point multipliers are parsed as nonnegative exact rationals. Upper-bound multipliers, if present, are parsed by `(type,negative_set,weight)`, checked nonnegative, and included in both their own target inequality and the objective. In the supplied76 certificates all these upper-multiplier lists are empty, so their exact contribution is zero.

For each graph, **all** subsets of its U are checked, not just discovery-listed active negative variables: every pair for N2, every triple separately for T3 and Bx3, and every four-set for N4. In total the76 certificates pass **283968 target inequalities**. With candidate weight W(F)=ΣS⊇F λS and budget prices(a,b,c), their costs are respectively

N2: a+b+c+ΣFh+γN2,F;
T3: a+c+ΣFh+γT3,F;
Bx3: b+c+ΣFh+γBx3,F;
N4: c+ΣFh+γN4,F.

The exact objective is recomputed as3a+4b+20c+Σv(7−frequency(v))hv+Σγ, checked equal to the stored rational bound and strictly below one. Its maximum over76 inputs is **10/11**. Neither a floating solver status, the recorded floating objective, a stored PASS flag nor a positive stored margin is used to establish these inequalities.

The general justification, including nonempty upper multipliers, is in [the shared-capacity weak dual](../../shared_capacity_dual_20261020/LEMMA.md), now with its explicit target-upper-bound extension. Same-type identical negative targets may first be logically merged; cross-type residual equality is allowed. This preserves the repair requirement and only decreases every resource count. In the actual76 certificates γ=0, the weak-dual proof even applies directly with arbitrary indexed target repetitions, without any uniqueness premise.

Targets involving U-exterior points cannot block these candidates, all of which lie in U. Pairs/triples are tested by containment, not equality with a candidate. The two triple origins have separate shared-budget costs. Point capacities use the safe frequency in the six remaining positives; any appearances in the three positives already hit by x only strengthen the actual capacity. These observations ensure the finite inequalities cover every actual negative family represented by the fixed-x reduction.

## The unique noncertified graph: integer proof

The sole row without a strict rational certificate has

J=15+2·23+2·24+2·34,

degrees(0,1,4,4,4,1), E7, C3=M3=0 and C4=48. Its15-entry vector is independently checked to be

(0,0,0,0,0,0,0,0,1,2,2,0,2,0,0).

Write z for the actual shared point on graph edge15. Every four-point transversal of the six remaining positives is exactly

S={z,a,i,j},  a∈A,

where A is the four-point private positive set at isolated label0, and ij is one of12 edges of the complete tripartite graph K2,2,2 on the six shared points belonging to the doubled triangle23/24/34. Thus there are4·12=48 distinct candidates. The remaining private points at labels1 and5 occur in no such candidate.

Use only active negative indices. For each type N2,T3,Bx3, let subscripts0/1 mean that its residual target contains/avoids z, giving counts u0/u1,s0/s1,v0/v1. Let q count active N4 indices. Every active N4 equals a four-point candidate and hence contains z. Since z has at least two original positive appearances,

q≤5−u0−s0−v0.

A containing-z pair blocks at most16 candidates and an avoiding-z pair at most4. A containing-z triple blocks at most4 and an avoiding-z triple at most1; this applies to both triple origins. Each active N4 blocks exactly one. Hence the union of blocked candidates is at most

16u0+4u1+4s0+s1+4v0+v1+q.                  (1)

The shared budgets give

u0+u1+s0+s1≤3,  u0+u1+v0+v1≤4.

Substituting the q bound into(1), then using the two displayed budgets, bounds(1) by26+9u0−2u1. If u0≤2 this is at most44<48, so a candidate remains. `VERIFY.py` also independently enumerates these small integer count parameters; the exact maxima for u0=0,1,2 are24,33,44. The more conservative45 bound in preliminary discussion was therefore safe as well.

It remains u0=3. First merge identical active N2 targets; if fewer than three survive, the preceding u0≤2 argument applies to the equivalent deduplicated family. Hence assume the three targets are distinct `{z,w}`. All three original negative triples are used, so u1=s0=s1=0. Each w lies in A or the six core vertices, since inactive targets were excluded.

Let ℓ of the three distinct target points be core vertices; the other3−ℓ are distinct A points. Exclude all three target points from the candidates. The number remaining is at least

|A\targets|·|core edges avoiding targets|
≥(1+ℓ)·(12,8,4,2)ℓ,

for ℓ=0,1,2,3 respectively. The core bounds follow directly by deleting ℓ vertices from K2,2,2; the four minima are independently checked by the small six-vertex subset count. The resulting candidate lower bounds are12,16,12,8, so at least eight remain. No original negative triple blocks any of these survivors.

Only Bx3 and N4 remain. The x budget gives v0+v1≤1, while the z capacity gives q≤2−v0. Thus these remaining indices block at most

4v0+v1+q≤4v0+v1+2−v0≤5<8.

The finer bound is **five**, as in the discovery proof: a Bx3 target avoiding z blocks at most one, not four. Treating both cases uniformly by four gives the weaker six, which is also strict but unnecessary. There is no discrepancy affecting the proof. All these bounds retain indexed counts; optional same-type N2 deduplication only decreases the resources. Consequently this exceptional graph also repairs.

## Evidence and limits

`RESULT.json` records every certified graph key, all target inequality counts, exact objective and margin, the exceptional graph and its small integer checks. Reproduction:

```sh
python3 -B context/propertyb35-paper/round01/twentyfour/positive_occ_three/nine_positive_joint_negative_budget_20261020/six_label_pilot/joint_cover_independent_20261020/VERIFY.py
```

The full second run used about0.85 CPU seconds. It changed no source census or LP data. The noncertified row's fractional covering witness is not needed or asserted to be an integer obstruction; the short combinatorial proof resolves that row. The surrounding nine-positive proof still must cover its other fixed-point/occurrence branches and connect any actual H caller separately. No cross-family review or new Lean check is asserted here.
