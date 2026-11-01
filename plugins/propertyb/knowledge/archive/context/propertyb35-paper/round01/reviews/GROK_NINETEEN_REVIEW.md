# Grok：19点δ8/δ9静态审阅原回应

实际 grok-4.7-build / xhigh；end_turn。未执行计数程序或Lean。

Both conditional branches are correct. They establish Property B only for a pair-covering simple 5-uniform hypergraph on 19 vertices with exactly 35 edges and minimum degree 8 or 9. They do not prove \(m(5)\ge 36\).

The original statement quantifies over every finite vertex set and every set of at most 35 distinct 5-edges, with no pair-covering, order, or degree hypothesis. `REDUCTION.md` derives those restrictions from a minimum counterexample and then invokes these branches. The branch arguments use the reduced hypotheses and do not feed back into that reduction. The conditional-permutation bound is taken as given; the inventories below were checked directly.

**Degree 8.** For \(d(x)=8\), the codegree row sums to 32. Pair covering makes every non-unit codegree at least 2, so \(32\ge |W|+2(18-|W|)\) and \(|W|\ge 4\). A unit neighbor of degree \(b\) has \(11\le b\le 28\): the upper end is \(35-8-b+1\ge 0\), and all 18 values are double-lock inputs. Every surviving unit neighbor therefore has degree 8, 9, or 10.

The six pair rows are complete. For two degree-8 neighbors the possible codegrees are 1 through 8; the double locks remove 3 through 8 and the triple locks remove codegree 1 at both triple multiplicities 0 and 1. The other rows likewise leave no omitted integer: the survivors are codegree 2 when a neighbor has degree 8, and codegree 3 otherwise. Thus \((8,10)\) and \((10,10)\) cannot occur. The only sorted four-neighbor degree lists are \(8888\), \(8889\), \(8899\), \(8999\), \(9999\), and \(999(10)\).

Each chosen neighbor lies in exactly one edge through \(x\), so the nonempty traces on those neighbors form a partition \(\Pi\). There are \(B_3=5\) and \(B_4=15\) partitions. Exact \(x\)-free multiplicities invert the stated inclusion, with total 27. Nonnegative inversion gives 66 three-neighbor inventories. The pilot leaves 11 non-strict; the separate three-neighbor lock of degrees \((8,8,8)\), codegrees \((2,2,2)\), and triple multiplicity 1 removes the singleton partition at multiplicity 1. The other 10 are exactly the labeled table: \(1+3+1+1+1+2+1\). Every other nonnegative inventory is one of the 55 strict four-vertex locks.

Projecting a four-neighbor partition onto all four triples, and keeping one common \(\Pi\) and one common quadruple multiplicity, leaves 33 nonnegative inventories: 10, 4, 2, 2, 12, and 3 in the degree order above. The raw \(9999\) singleton list has 17 candidates; five give a negative singleton multiplicity, namely the all-zero pattern and the four patterns with only one triple multiplicity equal to 1. The remaining 12 are \(11\) with quadruple multiplicity 0 and one with all four triple multiplicities and the quadruple multiplicity equal to 1. All 33 saved four-neighbor profiles are marked strict. No block of size 3 or 4 survives projection.

**Degree 9.** The degree sum is \(5\cdot 35=175=19\cdot 9+4\). The only excess partitions are \((10,10,10,10)\), \((11,10,10)\), \((12,10)\), \((11,11)\), and \((13)\). The 84 certificate profiles are exactly the stated rules: all codegrees at least 4 up to the smaller degree, the four low codegree-1 pairs, both small codegrees of two degree-11 vertices, six triple types for each third degree 10 and 13, and the seven rows of the degree-\((9,11,11)\) table.

A degree-10 vertex forces the first three partitions. A unit pair in the degree-9 set meets that vertex in codegrees 2 or 3, with triple multiplicity at most 1, which is rule 3. Otherwise every codegree from a degree-9 vertex equals 2. The degree-10 row then sums to 40, while it is at most \(2(19-h)+3(h-1)=35+h\le 39\).

For a single degree-13 vertex the same split applies. Rule 3 covers a unit pair. Otherwise that vertex has codegree 2 with all 18 other vertices, so its row sums to 36, not \(4\cdot 13=52\).

For two degree-11 vertices their mutual codegree must be 3. Mixed codegrees \((2,3)\) are strict for every feasible triple multiplicity. The equal case \(22\) must have triple multiplicity 0, and \(33\) must have multiplicity at least 2. With \(q\) vertices of type \(33\), the degree-11 row gives \(34+q=41\), hence \(q=7\). The three common edges contribute \(3\cdot 3=9\) to the sum of those multiplicities, while the lower bound is \(2\cdot 7=14\).

The boundaries that look like escapes are already strict inputs or numerically impossible: high-high codegree 4, excess \((12,11)\), a degree-14 vertex, and triple multiplicity 1 on a type-\(33\) vertex. Under pair covering the minimum degree is at least \(\lceil 18/4\rceil=5\), so degrees below 5 are not additional cases of this reduced problem.
