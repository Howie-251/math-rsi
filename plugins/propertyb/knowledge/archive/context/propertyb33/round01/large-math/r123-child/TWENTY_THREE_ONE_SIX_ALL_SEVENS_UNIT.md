# Derivation Package: one degree-six vertex with unit codegree to all degree-seven vertices

## Target

Prove Property B for a simple pair-covering 5-uniform hypergraph H with 23 vertices, 33 edges, exactly one degree-six vertex x, and λ(x,y)=1 for every degree-seven vertex y. Together with `../TWENTY_THREE_LOW_WITH_SEVEN_BAD.md`, this covers the r=1 branch.

## Status

COHERENT AS STATED: complete conditional mathematical candidate. Exact witnesses and an independent labelled-injection audit are supplied. This branch has not yet been connected in Lean or reviewed across model families.

## Invariant Object

The position sum Σ_k min(A_k,B_k,C_k−D_k) in the established permutation criterion. All losses D_k come from real bad link pairs; both orientations are included. A strict sum below one implies a Property-B coloring.

## Assumptions

- H is finite, simple, 5-uniform, pair-covering, with 23 vertices and 33 edges.
- Exactly one vertex x has degree six, and all its codegrees with degree-seven vertices are one.
- Existing double-lock certificates exclude any two degree-seven vertices with codegree at least four. Their codegree-4/5/6/7 bounds are 282379/293930, 131581/146965, 34907/41990, 1738/2261.

## Notation

L is the degree-seven vertex set; t=|L|. The bad graph on L joins pairs of nonunit codegree. For a fixed lock set S, n_B counts actual edges whose exact trace on S is B.

## Derivation Strategy

First exclude codegree-three pairs in L using five locks. The remaining bad graph has maximum degree six. Partition it into four parts each inducing maximum degree at most one, then select five vertices in a largest part. These five seven-degree vertices and x form six locks whose only nonunit pairs are a matching of zero, one, or two codegree-two pairs. All complete local trace inputs have strict exact certificates.

## Derivation Map

1. Total degree forces t≥17.
2. Degree-seven codegree excess is six.
3. A codegree-three pair extends to a previously checked mixed five-lock matching pattern and is excluded.
4. Four-part defective coloring selects five highs with induced bad graph a matching.
5. Complete pair-budget recursion covers actual six-lock traces.
6. Exact permutation and link-subfamily certificates give a strict bound for every input.

## Main Derivation

### 1. Degree count and high-codegree exclusion

With t vertices of degree seven and the remaining 22−t vertices of degree at least eight,

165 ≥ 6+7t+8(22−t)=182−t,

so t≥17. For every y∈L,

Σ_{z≠y}(λ(y,z)−1)=4·7−22=6.

Thus y has at most six bad neighbors. The already certified two-lock branch excludes λ(y,z)≥4 for y,z∈L.

Suppose λ(y,z)=3 for two members of L. Each has at most four other bad neighbors, because their mutual pair consumes two units of its excess. Among L\{y,z}, at least t−2−8≥7 vertices are unit-codegree neighbors of both. Choose any two distinct such vertices u,v. Their mutual codegree is 1, 2, or 3. The five locks x,y,z,u,v have degrees (6,7,7,7,7); all pairs touching x are unit, and their only possible nonunit pairs are yz of codegree three and uv of codegree 1, 2, or 3.

`MIXED_MATCHING_FIVE.json` completely covers these three pair patterns. They have 24,31,20 representatives respectively, all 75 already strict using total/pure link quotas. Hence this case is excluded. We may now assume all pairs within L have codegree one or two.

### 2. Five-high selection by a four-part partition

Let G be the graph on L whose edges are codegree-two pairs. Its maximum degree is at most six. Among all partitions of L into four labelled parts, choose one minimizing the number of edges with both endpoints in the same part.

If a vertex had at least two neighbors in its own part, then among the other three parts some part would contain at most one of its neighbors: otherwise its total degree would be at least 2+2+2+2=8, contradicting the degree bound six. Moving it to that part strictly decreases the objective. Therefore every part induces maximum degree at most one.

Since t≥17, one part contains at least five vertices. Choose five of them. Their induced G is a matching of size zero, one, or two. Along with x, this gives six locks of degrees (7,7,7,7,7,6), pair codegree two on zero, one, or two disjoint pairs among the five high locks, and pair codegree one everywhere else.

### 3. Complete actual six-lock trace domain

Use high-lock bits 0,...,4 and low-lock bit 5. Up to relabeling the possible nonunit pairs are 01 and 23. For each matching size j=0,1,2, the target pair budget is two on the first j of these pairs and one on every other pair.

All actual edge traces have size at most five; the six-element mask 63 is forbidden. The following finite recursion is complete for multi-traces of size at least two:

- Choose the first pair with positive remaining budget.
- Choose one block B of size 2,...,5 that contains that pair and does not exceed any pair budget inside B.
- Subtract one from each pair budget inside B and recurse.

To see completeness, start from any actual remaining multi-trace family. Some actual trace B contains the selected positive-budget pair; choosing it is one legal branch. Removing that occurrence strictly decreases the total pair budget, so induction applies. Sorting traces and discarding duplicate recursion outputs loses no actual multiset.

The recursion yields respectively 352,467,611 labelled multi-trace families. For every family, the singleton and empty counts are forced by

n_i=d_i−Σ_{B∋i,|B|≥2}n_B,

n_∅=33−Σ_{B≠∅}n_B.

Retain nonnegative counts. Here the 1,430 labelled inputs give 17,84,142 representatives, totaling 243. A formalization can directly use all labelled inputs and avoid an orbit-classification theorem.

### 4. Exact bounds and real link losses

At each seven-degree center, the whole-link bad-pair quota is two; at x it is one. A pure-singleton link subfamily lives on the 17 free vertices, so its quota is max(0,ceil((4n_i−17)/3)). The nested total/pure inventory allocates these jointly; it does not add overlapping quotas.

242 of the 243 six-lock representatives have strict bounds from these quotas. The unique remaining representative, group 212, initially has value 12156/12155 at positions (9,11,12,14,10,13). Use all avoided-lock subfamily quotas instead. For a center i and avoided lock subset R, let F_R contain its incident edges avoiding R. Its link union lies in 22−|R| vertices, hence

q_R=max(0,ceil((4|F_R|−(22−|R|))/3)).

For nonnegative multipliers α_R, the exact loss lower bound is

Σ_R α_R q_R − Σ_j c_j max(0,Σ_{R: slot j avoids R}α_R−w_j),

where each unordered slot j has capacity c_j and both-orientation weight w_j. This follows directly by multiplying the actual quota inequalities and using the actual slot-count upper bounds. The saved multipliers are checked as exact rationals; no numerical LP optimum is assumed.

At the same positions, group 212 improves to 2385/2431<1. Every six-lock input is now strict, completing the stated branch.

## Remarks and Interpretation

The proof uses finite local trace classification and exact arithmetic, not whole-hypergraph enumeration. The four-part graph argument is a short general selection theorem; no catalogue of graphs on 17 vertices is needed.

## Boundaries and Non-Claims

- This branch assumes x is unit-codegree to all degree-seven vertices. The complementary branch is handled in the parent directory's low-with-seven-bad candidate.
- The finite numerical witnesses require the selection and actual-trace completeness arguments above; representative checks alone do not prove the branch.
- The branch is a full paper-level candidate, not a completed Lean theorem.

## Open Risks

Lean must connect the actual five-/six-lock selection, pair-budget domain recursion, link-subfamily quotas, and exact strict witnesses. No remaining mathematical gap is identified in this stated conditional branch.

## Evidence

- `MIXED_MATCHING_FIVE.json`: use only the 75 representatives whose pair-codegree tuple contains 3.
- `ONE_LOW_FIVE_HIGH.json`: 243 six-lock representatives, 242 baseline strict.
- `ONE_LOW_FIVE_HIGH_REFINEMENT.json`: exact rational dual for group 212, strict value 2385/2431.
- `ONE_LOW_ALL_UNIT_INDEPENDENT.json`: independent A/B/C replay of all selected five- and six-lock winners plus exact replay of the stored dual without calling LP.
- Scripts: `mixed_matching_five.py`, `one_low_five_high.py`, `audit_one_low_all_unit.py` in `computations/propertyb33/round01/r123-child/`.
