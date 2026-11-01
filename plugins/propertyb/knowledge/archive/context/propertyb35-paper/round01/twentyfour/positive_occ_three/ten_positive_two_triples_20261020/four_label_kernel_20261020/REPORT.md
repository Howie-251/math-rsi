# Complete four-label shared-kernel profile and exact repair certificates

**Result:** the complete stated four-label relaxation has5573 labelled graph inputs in18 fixed sorted-capacity cells, giving1333 capacity-preserving graph orbits. **All1333 have strict rational shared-capacity certificates; none remains fractional-only.** A second standard-library verifier checks674721 complete typed-target inequalities, maximum exact bound10/11. The full LP run used10.877339 CPU seconds; exact certificate replay1.753976 seconds; separate complete-domain replay0.099511 seconds. No integer solver, negative-layout enumeration or original-H realization was used.

This establishes the parameterized four-positive lemma below by explicit exact certificates and complete local classification. Its surrounding actual-input connection is given here; independent parent acceptance and designated cross-family review remain separate. It is not a proof of the whole ten-positive gate or of m(5)≥36.

## 1. Parameterized local lemma

Fix n∈{0,1,2}. There are four indexed positive sets Ai. Their sizes ci obey:

- n0: c=(4,4,4,4), positive union size≤16;
- n1: each ci∈{3,4}, Σci≥13, positive union size≤15;
- n2: each ci∈{2,3,4}, Σci≥10, positive union size≤14.

Every point has positive frequency g≤2 in these four sets. Negative indices have five separate types and satisfy shared budgets and point capacities as follows.

|Type|Target size|T budget cost|B budget cost|Kernel budget cost|
|---|---:|---:|---:|---:|
|Tpair|2|1|0|1|
|Ttriple|3|1|0|0|
|Bpair|2|0|1|2|
|Btriple|3|0|1|1|
|B4|4|0|1|0|

The three budgets are T≤2−n, B≤18, K≤8−2n. Each point's total negative occurrence is at most7−g. Any finite ground containing the four positive sets is allowed; targets outside their union are automatically avoided by a repair inside the union. Under these conditions, a set S meeting all four positives and containing no negative target exists. Indices and repeated residual targets may be retained; no simplicity of negative families is needed for the supplied certificates.

## 2. Full representation and domain coverage

Represent each positive double point by an edge joining its two positive labels. Parallel edges are distinct actual points. Single-occurrence points are private to their label. Thus a six-entry vector of nonnegative loopless multigraph multiplicities on labels0..3, with degree di≤ci, reconstructs the four positives by adding ci−di private points to label i. If E is the graph's total multiplicity, the union size is

U=Σci−E≤16−n.

No other point type occurs when the positive maximum is two. Conversely every such graph/vector constructs a valid four-positive system, up to actual point relabeling.

Sort the four capacities first. This loses no actual input: any four-label system can be relabeled to sorted capacities. Once sorted, use **only permutations preserving each capacity** when taking graph orbits. Thus the group is a subgroup of S4, not an independent relabeling of different types or sets.

There is one capacity tuple for n0; four for n1 (3334,3344,3444,4444); and thirteen for n2 (the sorted four-tuples from2,3,4 except2222 and2223). This gives18 capacity cells. `PROFILE.py` assigns the six edge multiplicities recursively, never exceeding endpoint capacity, then checks U. Every legal vector determines a unique sequence of six choices. It takes the minimum image under the exact capacity stabilizer and checks that every stored orbit size equals the size of its transported labelled vector set.

|n|Sorted-capacity cells|Labelled vectors within those cells|Orbits|
|---:|---:|---:|---:|
|0|1|641|61|
|1|4|1725|358|
|2|13|3207|914|
|Total|18|5573|1333|

The labelled count is for the stated fixed sorted-capacity cells, not all ordered capacity assignments. `VERIFY_DOMAIN.py` independently enumerates the Cartesian product of all six edge multiplicity ranges, filters only degrees/U, and compares each cell's **entire labelled vector set** against the disjoint transported representative orbits. All18 sets agree exactly. This check does not import the recursive generator.

## 3. Candidate and negative domains

For each representative reconstruct its actual point sets and list **all** subsets of their union of sizes1,2,3,4 that meet all four positives. A size-one transversal cannot occur with maximum positive frequency two, but its inclusion is checked rather than assumed by the implementation. This is not restricted to the three-/four-point candidates used in the previous six-label proof.

For the LP discovery, include every typed target that is contained in some candidate. Each type has its own nonnegative variable; equality of a Tpair target with a Bpair target does not identify their different budget costs. Logical merging of identical targets within one type permits upper bounds one during discovery. Removing such repetitions leaves the repair condition unchanged and decreases resource use. The exact accepted certificates below all have zero upper-bound multipliers, so their final proof in fact works directly with indexed repetitions.

Negative targets involving a point outside the positive union cannot be contained in any chosen S and are safe; ignored inactive indices can only make the resource relaxation larger. Targets of size two or three are checked by containment in S, not equality with S. Any represented point/positive-label permutation transports the candidates, all five target types and all capacities together.

## 4. Exact weak-dual certificate and proof

For candidate weights λS≥0 with ΣλS=1, write W(F)=ΣS⊇F λS. Save nonnegative rational budget prices α,β,κ and nonnegative point prices hv. Every typed target F must obey

Tpair: W(F)≤α+κ+ΣFh;
Ttriple: W(F)≤α+ΣFh;
Bpair: W(F)≤β+2κ+ΣFh;
Btriple: W(F)≤β+κ+ΣFh;
B4: W(F)≤β+ΣFh.

The strict objective bound is

(2−n)α+18β+(8−2n)κ+Σv(7−gv)hv<1.             (1)

Apply the appropriate inequality to every actual negative index and sum. Shared T/B/kernel budgets and the point capacities make the total weight of blocked candidates at most(1), hence strictly less than the candidate weight one. At least one positive-weight S is unblocked. This proves the local lemma from the finite certificates, without an inference from a floating solver status.

`JOINT_LP.py` used the existing SciPy/HiGHS in `/tmp/tbs-s01-dev-venv/bin/python`; nothing was installed. It first profiled two minimum-sum n2 disjoint-capacity cases2224 and2233, both strict, then completed all1333 representatives under an80-CPU-second bound. Each floating dual was rationalized, candidate weights normalized exactly, and any positive target violation repaired by adding a common exact amount to both the T and B prices (every source type has one of these costs). Acceptance occurs only after exact inequalities and a strict exact objective are verified. Full discovery and original exact certificates are preserved in `ALL_LP.json`.

`VERIFY_CERTIFICATES.py` is a second implementation using only Python's standard library and Fraction. It independently reconstructs each graph's four sets and all1..4 transversals, checks the complete1333-key equality with the profile, every point capacity and source cost, all listed candidate weights and their exact sum, and the rational objective. It checks **all union subsets** of the five appropriate target types, including inactive targets, not only the discovery columns. All674721 inequalities pass; all upper multipliers are checked and their sum is zero. The maximum exact bound is10/11, reached in n2 at capacities2224 with a single graph edge12. Results are in `VERIFICATION.json`.

## 5. Connection from an actual ten-positive double-three-kernel input

In the original ten-positive gate, assume maximum original positive occurrence three and choose three-points x,y with disjoint three-label supports. Fix x,y red, leaving four original positive four-sets. Their total negative kernel incidence is at most eight.

First logically merge identical original negative triples. This preserves repair and only reduces all original counts and occurrences. Let n be the number of remaining original triples containing both x,y; their n distinct third points form Z, which is fixed blue. All negative indices containing Z are now satisfied and removed whole. For the four unhit positives set Ai=original Ai minus Z. Since each Z point belonged to at most three original positives, at most3n incidences are removed from these four sets. Thus ci≥4−n, Σci≥16−3n and the number of unfixed ground points is at most18−2−n=16−n. These are precisely the three capacity/union conditions above. They are safe relaxations and do not assume every listed capacity pattern is actually realizable by a Z support pattern.

If the current four positives still have a three-point, the separate [high-three-kernel proof](../FOUR_REMAINING_HIGH_THREE_REPAIR.md) handles n0/1/2, including kernel reselection when n2. Otherwise their maximum occurrence is two and they enter the graph domain just proved.

The original remaining negative triples cannot contain both kernels: all such indices contain their blue third point in Z and were removed. A triple with one/no kernel becomes Tpair/Ttriple. An original negative four-set with two/one/no kernels becomes Bpair/Btriple/B4. Their original source counts imply T≤2−n and B≤18, and the n removed two-kernel triples have already used2n kernel incidences, leaving K≤8−2n. Every unfixed point's current positive frequency is no greater than its original frequency, so its negative occurrence is safely at most7−current frequency. Original positives already hit by x/y are not being used to assert a falsely stronger negative capacity.

Apply the local repair to obtain S in the current positive union. The red set is {x,y}∪S, with Z and all other ground points blue. Original x/y positive sets are hit by the kernels; other positives are hit through their shortened Ai. Every original negative removed on Z contains a blue point; every other negative is avoided exactly when its residual target is not contained in S. Hence this returns a repair of the original signed input.

Together with the separate high-three proof, the result covers the **double-three-center branch** of the ten-positive problem. It does not cover maximum-three systems with no disjoint positive three-star supports, nor assert any actual P6 input has such a kernel unless independently proved.

## Reproduction and evidence boundary

```sh
python3 -B context/propertyb35-paper/round01/twentyfour/positive_occ_three/ten_positive_two_triples_20261020/four_label_kernel_20261020/PROFILE.py
/tmp/tbs-s01-dev-venv/bin/python context/propertyb35-paper/round01/twentyfour/positive_occ_three/ten_positive_two_triples_20261020/four_label_kernel_20261020/JOINT_LP.py --all --cpu-limit 80
python3 -B context/propertyb35-paper/round01/twentyfour/positive_occ_three/ten_positive_two_triples_20261020/four_label_kernel_20261020/VERIFY_DOMAIN.py
python3 -B context/propertyb35-paper/round01/twentyfour/positive_occ_three/ten_positive_two_triples_20261020/four_label_kernel_20261020/VERIFY_CERTIFICATES.py
```

All requested local domain cells and certificates are complete, with no CPU-truncated prefix or fractional-only remainder. The two pure-standard-library checks are separate implementations, not cross-family review. Original census/canonical/navigation files were not changed. Final theorem acceptance and any further branch assembly remain with the parent.
