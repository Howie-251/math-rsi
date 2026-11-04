# Proof Package: core 0 with two original crossings

Date: 2026-11-01. ARIS proof-writer. Does not modify the previously
delivered zero-crossing proof or certificates.

## Claim and status

The target is the core 0 T15 statement for every arbitrary complete-graph
matching with holes $\{0,1,2,7,11,13\}$, omitted vertices $1,2$, and
exactly two original edges crossing coordinate zero.

Status: **PROVABLE AS STATED** relative to the imported checked Q4
classification. The exceptional full-input certificates and independent
verification have finished with PASS, as has the independently implemented
component check of the finite reduction. Fresh-context audit is pending.
Full core 0, T15, eight-hole P6 and P6 are not asserted.

## Assumptions and notation

Use local A labels $a\mapsto2a+1$ and B labels $b\mapsto2b$. The holes
are $\{0,3,5,6\}$ in A and $\{0,1\}$ in B. Let the two A crossing
ports be $p_A<q_A$ and the B ports $p_B<q_B$. There are two possible
crossing bijections. The internal matchings have five A edges and six
B edges. Original required edges may be arbitrary complete-graph edges.

For a choice $s<t$ from $\{3,5,6\}$, let $u$ be the remaining retained
A hole. Consider the three abstract pairings of four endpoint labels:
$$
R_0=(p q)(s t),\qquad R_1=(p s)(q t),\qquad R_2=(p t)(q s).
$$
The three families are indexed by $u=3,5,6$ in this order. A nine-bit
signature records these three pairing options for each family.

## Strategy and dependency map

1. Import the complete checked Q4 three-avoid negative classification
   for omitted $1,s,t$; outside the negative set a positive 13-cycle exists.
2. Enumerate all possible A short path forests, retain their abstract
   four-port pairings, and compute all possible B suppressions.
3. Compare the finite signature types including both crossing bijections.
4. Directly certify every remaining full Q5 input.

## Proof of the finite reduction

### Step 1. Complete A spectra

Fix the internal A matching. The short new edges of a desired A path
forest must have degree two at $u$ and degree one at all other vertices
of $A\setminus\{0_A\}$. Exactly 116 such short-edge sets occur per $u$:
choose two distinct short neighbors of $u$, and match all twelve remaining
vertices by short edges. This enumerates all choices because the new
degrees specify precisely those two edges and that perfect matching.

Discard a set if it repeats an original A edge or creates a cycle when
joined to the original internal matching. Every surviving union is a
forest of two paths with endpoint set $\{p_A,q_A,s_A,t_A\}$ and exact
support $A\setminus\{0_A\}$. Record its abstract pairing $R_i$.

All $\binom{12}{2}9!!=62370$ internal A matchings are enumerated. They
have 16 distinct signatures. An available signature bit is a positive
path-forest assertion; completeness also holds because all short degree
completions are included.

### Step 2. Complete B compatibility signatures

There are $\binom{14}{2}11!!=945945$ internal B matchings with two marked
uncovered ports. For each and each $(u,i)$, replace the A forest by its
abstract pairing, map $p_A,q_A$ to the sorted B ports, attach the bridges
at $s,t$, and include the six original internal B edges.

If a cycle component occurs, mark that bit unavailable. Otherwise suppress
the degree-two vertices $s_B,t_B$ and the two artificial A endpoint labels.
This produces a six-edge matching $L$ on
$B\setminus\{0_B,1_B,s_B,t_B\}$. Mark the bit available exactly when
$L$ is outside the complete Q4 negative table for omitted $1,s,t$.
This procedure also handles B ports equal to $s$ or $t$; no disjointness
assumption is imposed on those labels.

An A bit available also in B expands a Q4 13-cycle through both A paths
to a simple 30-cycle with precisely the required support. The original
matching edges survive, and all added edges are short. Reversing the
crossing bijection exchanges bits $R_1,R_2$ in each of the three families
and fixes $R_0$.

### Step 3. Exact type comparison

`t15_core0_c2_types.cpp` generates the complete A and B input lists and
their signatures. `verify_t15_core0_c2_types.cpp` independently recomputes
every signature by disjoint-set components, whereas the producer uses
explicit path walks. The verifier checks every input matching, uniqueness
of its encoded edges, the exact universe cardinalities, and every
signature. It then checks every A/B signature pair in both crossing
orientations.

The result is that every nonzero B signature intersects every A signature
in both crossing orientations. Exactly 24 B inputs have zero signature.
Thus the only remaining full inputs are
$$
24\cdot62370\cdot2=2993760.
$$

The two-port triple-choice claim for a fixed $s,t$ is therefore false in
general, and even the three $s,t$ choices together have these 24 B
exceptions. The explicit list is `t15_core0_c2_exceptional_B.txt`.
They are failures of this sufficient transfer, not T15 counterexamples.
The six A inputs whose best single-family spectrum has size two do not
create an additional exception: their full nine-bit signatures intersect
every nonzero B signature as well.

The independently checked report is
`t15_core0_c2_types_verification.json` with status PASS, 62370 A inputs,
945945 B inputs, 24 exceptional B inputs and 2993760 residual full inputs.
This checker does not rely on any negative global Q5 search.

## Step 4. Complete exceptional-family positive certificates

`t15_core0_c2_residual.cpp` exhausts every residual full input: sorted
A ports, every perfect pairing of the other ten A covered vertices,
the 24 exceptional B inputs, and both crossing bijections. It searches
for a short-edge-connected oriented ordering of required-edge blocks and
four retained free vertices. A successful 56-byte record contains the
26 required-edge endpoint bytes followed by 30 cycle vertices.

All $2993760$ residual full inputs have positive witnesses, with no
exhausted or node-limited input. The final binary contains exactly
$167650560$ bytes and its SHA-256 is
`7465c6b5e7b23dd01724ebe396393ca17d1b9361c53d3aed071fe955de948c4d`.
The computation was partitioned by the sorted A port pair; the first
27 of the 66 port pairs and three subsequent 13-pair partitions were
concatenated in enumeration order. Partitioning does not affect the
independent verification or the mathematical claim.

`verify_t15_core0_c2_residual.cpp` independently regenerates all those
original inputs and checks the exact required-edge prefix, 30 distinct
vertices, exact support, all 13 required edges, shortness of all other
edges including the closing edge, exact record count and no trailing
data. All $2993760$ records pass. The report is
`t15_core0_c2_residual_verification.json`; the combined report with the
exact imported-negative-list comparison is
`t15_core0_c2_verification.json`.

Steps 1--4 exhaust every internal A matching, internal B matching and
both original crossing bijections. The target c2 claim therefore follows.
The theorem retains arbitrary original complete-graph edges and has not
been narrowed to short original edges.

## Open risks

- The Q4 negative classification is an imported already-checked input.
- Fresh-context audit of this proof and both new verifiers remains pending.
- Crossings $c\ge4$ are not covered by this package.
- No global eight-hole remaining count is changed here.
