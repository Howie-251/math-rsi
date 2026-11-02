# Four-base topology: complete symbolic capacity and a deferred m33 gate

This batch completes the single fixed topology in `PRED.md`. It does not produce a controller or run a numerical voltage assignment. Its output is a complete symbolic endpoint table, exact structural conditions, and a candidate-checking interface for a later separately chosen experiment.

## Symbolic result

The variable order is

```
(a0,a1,a2,a3,sigma01,sigma23,tau02,tau13,rho03,rho12,e), e=m/3.
```

Every one of the4*7³=1372 three-port words was followed using the literal base maps. The first ten voltage coefficients remain integers; only the coefficient of e is reduced modulo3, using3e=0. The complete words and coefficient vectors are in `ALL_WORD_FORMS.tsv`. `DISTINCT_FORMS.tsv` keeps every distinct endpoint form and a first word witnessing it. Equal formal vectors certainly evaluate equally for every admissible modulus; unequal vectors can still collide after evaluation.

The actual distinct counts, with source and target bases ordered0,1,2,3, are

| source / target | 0 | 1 | 2 | 3 |
| --- | ---: | ---: | ---: | ---: |
| 0 | 69 | 62 | 56 | 66 |
| 1 | 62 | 61 | 62 | 67 |
| 2 | 56 | 62 | 69 | 66 |
| 3 | 66 | 67 | 66 | 51 |

Therefore exact-three-walk coverage requires **m<=51**, with3|m. This is a symbolic capacity bound for the fixed topology. It does not assert existence at any modulus. It leaves the first competitive modulus33 open: controller order132 and the conditional full F11³ lift order175692 exceed the located public degree77 guarantee169750.

The former three-base m50 obstruction cannot be copied here. That topology had a50-form bottleneck at a required modulus50, forcing a perfect tiling. Here the smallest class has51 forms, and at m33 coverage allows collisions. Root00 is no longer the minimum class: its capacity is69; the minimum is source3 to target3.

## Literal inverse and triangles

For A, the dart i to i+1 uses voltage a_i, and its reverse uses-a_i. For S,T,R, each unordered base pair has one voltage v from smaller to larger base and-v on the reverse dart. These are involutions with exchanged bases. For B on bases0,1,2, the zero-voltage three-cycle reverses literally. At base3, B and B^-1 use+e and-e. The28 source-base/port reverse equations were checked symbolically, with reverse ports[1,0,3,2,4,5,6].

Every vertex belongs to a B triangle. At bases0,1,2 the triangle is ((0,g),(1,g),(2,g)); at base3 it is ((3,g),(3,g+e),(3,g+2e)). Since m is positive and divisible by3, e has exact order3, so these vertices are distinct. The four symbolic B³ identities were checked in the same run.

These facts bind the topology to the already tested F11 local interface: A± are special ports0,1, B± ordinary ports2,3, and the three matching ports4,5,6 use orientation plus the actual inverse chart. The old local rank/pencil computation need not be repeated for each controller; actual three-walk coverage still needs verification.

## Exact simplicity conditions

For positive3|m, all seven neighbors are distinct and loop-free exactly when the following residue conditions hold:

```
0, a0, sigma01 are pairwise distinct;
0, a1, rho12 are pairwise distinct;
tau02 != 0;
a2 != sigma23;
a3 != -rho03.
```

There is no separate restriction on tau13. All its edges exchange bases1 and3 and share no other port's target base at those vertices. A's darts exchange bases, so A alone cannot make a loop. The only same-base neighbors are B± at base3, and e,-e are distinct and nonzero automatically.

For example, from base0 the target-base1 shifts are{a0,0,sigma01}, target-base2 shifts are{0,tau02}, and target-base3 shifts are{-a3,rho03}. From base1, target-base2 shifts are{a1,0,rho12}; its target-base0 comparison repeats the first condition. From base2, target-base3 shifts are{a2,sigma23}; its other comparisons repeat earlier conditions. Base3 gives only those reversed comparisons and the automatic B± distinction. This proves necessity and sufficiency without numerical assignments.

## A safe gauge reduction

The coordinate change g_i'=g_i+c_i preserves all zero B voltages exactly when c0=c1=c2. An overall common translation has no effect; the one remaining relative translation of base3 can normalize a2=0. Take c0=c1=c2=0,c3=-a2. The transformed coefficients are

```
a2'=0, a3'=a3+a2,
sigma23'=sigma23-a2, tau13'=tau13-a2, rho03'=rho03-a2,
```

with the other five free voltages unchanged. Thus the ten free voltages have nine effective coordinates in this fixed zero-B-voltage presentation. This is an exact graph isomorphism, not a symmetry assumption or an executed search. It preserves simplicity, triangles and three-walk coverage.

## Checkable necessary gate for m33

Set e=11. Given a numerical candidate, first check the exact simplicity conditions. Evaluate each saved coefficient vector modulo33 and require all33 residues in every one of the16 ordered base-pair classes. Deck translations then imply coverage of all controller pairs. `check_m33_candidate.py` implements this finite candidate check but has not been run on any parameter assignment.

Before the full33-bit masks, projection onto modulus3 or11 gives necessary coverage masks. In these projections e=2 modulo3 and e=0 modulo11. Every class must cover all residues of each quotient. These projection gates are weaker than full33 coverage, and neither capacity nor either projection alone certifies a controller. In particular the earlier m50 uniform-multiplicity test does not apply: 51 and the other class sizes exceed33, and their residue multiplicities need not be uniform. No residue assignment domain has been enumerated in this batch.

The complete symbolic experiment used0.011546033CPU seconds, one worker, within the5-second budget. `RESULT.json` and `TERMINAL.json` record complete symbolic enumeration and no active process. There were no parameter tests, controller searches, graphs, BFS, Lean, solvers, further A permutations, lower-modulus ladders or external reviews. Root decides any subsequent actual bounded experiment.
