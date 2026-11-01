# Twenty-one vertices with exactly two degree-seven points

2026-10-13. Complete paper candidate; not yet Lean. H is simple, pair-covering and five-uniform, has 21 vertices and 34 edges, and has minimum degree seven attained exactly at x,y. All other points have degree at least eight. The goal of this note is Property B for this branch.

## 1. Codegree patterns and a unit-set lemma

The degree-eight set L has at least fifteen points: the baseline degree total is $2\cdot7+19\cdot8=166$, leaving four extra degrees. The strict double and (7,7,8) triple tables from `AT_LEAST_THREE_SEVENS.md` imply, unless a coloring is already obtained,

$$a=\lambda(x,y)\in\{1,2\},\qquad \lambda(x,u),\lambda(y,u)\in\{1,2\}\ (u\in L).$$

Partition L into A,B,C,D according to the pair pattern (1,1),(1,2),(2,1),(2,2), respectively. Degree-seven codegree excess is eight. Removing the contribution of xy at both endpoints gives

$$|B|+|C|+2|D|\leq16-2(a-1)=18-2a,$$

and therefore

$$2|A|+|B|+|C|\geq2|L|-(18-2a)\geq12+2a.\tag{1}$$

We use the following local lemma at either seven-degree center z. If U consists of at least three eight-degree points unit to z, a (7,8,8) strict witness handles any U-pair of codegree≥3. The complete (7,8,8,8) table has 62 profiles; after exact avoided-lock deductions, its nine residues all have the three U-pair codegrees (2,2,2) and zero common-four multiplicity. Thus, unless a strict witness gives a coloring, every U-pair has codegree two and every z-edge contains at most two U points.

For our x and y, their sets of unit neighbors in L each have size at least $15-[8-(a-1)]=6+a$, so the lemma applies to A∪B and A∪C. All pairs within either of these sets have codegree two.

## 2. Three points of the same pattern

Select any three points from A, or any three from B (C is symmetric). Their mutual codegrees are two. The five locks x,y and those three points have degrees (7,7,8,8,8). The pair vector is

$$(a,1,1,1,b,b,b,2,2,2),$$

with b=1 for A and b=2 for B. Every four-point trace containing a unit center and all three eight-degree points is zero by Section 1. The complete local classification has 565 profiles, of which 465 are strict single-layout cases and 34 more have strict mixed-layout certificates.

The retained residues have three consequences:

1. If a=2 and b=2, there are no residues. Thus |B|,|C|≤2 when a=2.
2. If a=1 and b=2, every selected triple from B has exactly one point lying in the unique xy-edge e. If B contained four points Q, summing $|e\cap T|=1$ over the four triples T⊂Q would give $4=3|e\cap Q|$, impossible. Thus |B|,|C|≤3 when a=1.
3. If a=1 and b=1, the only residue has an exact edge trace consisting of the three A points once, and every other trace of size at least three zero.

By (1), these bounds imply |A|≥4 for a=1 and |A|≥6 for a=2.

## 3. The case a=1

Choose four distinct points of A. Section 2(3), applied to every three of them, gives common-three multiplicity one for every A triple. Every trace containing x or y and at least two A points is zero, as is every xyA trace. The common-four multiplicity of the four A points is zero or one. These data specify exactly two possible six-lock profiles. Both have strict bounds,

$$696/715<1,\qquad13994/15015<1.$$

This proves a=1.

## 4. The case a=2: turn local residues into two matchings

Now |A|≥6. Apply the five-lock residue constraints to every three A points. In particular all xyAA common-four multiplicities vanish. Let I be the set of A points lying in one of the two xy-edges. Each xy-edge contains at most one A point, so |I|≤2.

Each A point is unit to both x and y, and Section 1 says every x-edge and y-edge contains at most two A points. Thus the pairs of A points sharing an x-edge form a matching Mx; the pairs sharing a y-edge form a matching My. Points of I are isolated in both matchings because their unique x-edge and y-edge coincide and contain no other A point.

Choose any four A points. Add the fourth to a retained five-lock profile by splitting exact traces, with prescribed new codegrees (1,1,2,2,2); retain only extensions whose every three-A projection is a retained five-lock residue. There are 99 representatives up to the two equal-degree seven labels and the four eight labels, including the two a=1 profiles above. Seventy-six are strict single-layout cases, sixteen additional cases have strict mixed-layout witnesses using the first layout set, and three more are strict when all 720 six-lock orders are included. Exactly four a=2 residual representatives remain.

For a selected four-point A set Q, their relevant matching data are:

| Residue index in `TWO_SEVEN_FOUR_EIGHT.json` | I points in Q | Mx edges in Q | My edges in Q | Relation of the two edges |
|---:|---:|---:|---:|---|
|24|0|1|1|Distinct, sharing one endpoint|
|28|1|0|0|No edges|
|43|0|1|1|Disjoint|
|72|1|1|1|Distinct, sharing one endpoint|

The full exact higher traces remain in the saved representatives. Only the listed consequences are needed for the contradiction.

Let N=A\I. If |N|≥5, choose five points Q⊂N. Every four-point subset has exactly one Mx edge by the table. Summing over the five four-point subsets counts each edge of Mx[Q] exactly three times, giving $5=3|Mx[Q]|$, impossible. Hence |N|≤4. Since |A|≥6 and |I|≤2, equality must hold throughout: |A|=6, |I|=2, |N|=4.

The four-point set N has a unique Mx edge e and a unique My edge f, and e≠f. Choose a point t∈f\e and set R=N\{t}; then R has three points, contains e and does not contain f. For any i∈I, the four-set R∪{i} has exactly one I point, one Mx edge and no My edge. This is neither allowed I-count-one row of the table. The contradiction completes a=2.

## 5. Exact evidence and remaining formal work

The 565-profile table is `TWO_SEVEN_THREE_EIGHT.json`; its 66 retained labels (22 orbits with fixed x,y orientation) are `TWO_SEVEN_THREE_EIGHT_RESIDUES.json`. The 99 six-lock representatives are `TWO_SEVEN_FOUR_EIGHT.json`. The initial seven six-lock residues were refined by all 720 orders in `TWO_SEVEN_FOUR_EIGHT_REMAINING_JOINT.json`, leaving exactly the four table indices above.

`TWO_SEVENS_WITNESSES_VERIFIED.json` independently checks all 594 retained strict single-layout rows, including the unit-set lemma. The three `_STRICT_JOINT_VERIFIED.json` files record exact independent mixed-layout checks for the 34+16+3 additional witnesses. The checks recompute A/B/C and pair weights from labelled injections and verify actual degrees, total edge count, all bad-slot capacities, avoided quotas, rational coefficients and final bounds. The log is `verify_two_sevens.log`.

The finite classifications require formal coverage and actual-profile transport in Lean. Cross-model review should target the pattern deficit inequality, the constant-one-on-e triple condition, the completeness of the four retained six-lock residues and their conversion to matchings. This note closes only r=2; the unique-seven and minimum-degree-eight branches remain separate.
