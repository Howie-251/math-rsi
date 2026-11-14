# Independent audit: seven marked T63 rank inputs

Verdict: **PASS**, same-family / provisional. Reviewer `/root/t26_first_rank_review`, GPT-6.1-sol high, explicitly selected by the user through the parent. This follows the invoked ARIS proof-checker workflow, with the requested model route overriding its default. The new independent verifier neither imports nor executes the producer generator or checker. It writes only new reviewer artifacts and leaves frozen T26 files, all producer files and main state untouched.

## Exact quantified scope

For every one of the seven (H,U) rows in Q5_T63_RANK_PROOF.md, and every perfect matching F of the complete graph on K=Q5\H, there is a simple cycle with vertex set exactly Q5\U containing F, and every edge outside F is short. The statement includes every common cube-automorphic image of (H,U), including parity reversal. It places no bipartite, short-edge or parity condition on F. It asserts these seven marked inputs only, with the specified omissions; it does not establish unrestricted T63.

| index | H | U |
|---:|---|---|
|0|0,3,5,10,20,30|0,3,5|
|1|0,3,5,10,12,23|0,3,23|
|2|0,3,5,10,29,30|0,29,30|
|3|0,3,5,10,29,30|0,3,5|
|4|0,3,5,6,24,27|0,5,6|
|5|0,3,5,6,9,27|0,5,6|
|6|0,3,5,10,12,23|0,10,12|

## Obligation ledger

1. **Forest support, degrees and pairings: discharged.** An independently parameterized C++ verifier checks every one of the seven certificates, each containing 4096 graphs of sixteen distinct short edges. Vertices in U have degree zero, the 26 vertices of K have degree one, and the three included holes have degree two. DSU rejects every cycle, and deriving endpoints by component connectivity reproduces every supplied pairing. Every supplied column matching uses each K vertex exactly once. Forbidden holes, duplicate vertices, duplicate edges, incorrect degrees, long forest edges, cycles and incorrect endpoint pairings all trigger rejection.
2. **All matrix bits and full rank: discharged.** The verifier contracts each supplied endpoint matching into thirteen components, then computes DSU connectivity after adding each column matching. It recomputes all 16,777,216 bits per certificate and requires exact byte equality with the saved matrix. Increasing-column Gaussian elimination over GF(2), using 64-bit row arrays, independently computes rank 4096 in each case. It does not rely on the producer's highest-pivot arrays or reported ranks. Those arrays remain hash-bound artifacts; independently recomputed rank suffices. Totals are 28,672 forests, 28,672 columns and **117,440,512 checked connectivity bits**. All frozen manifest hashes match. The complete checker run exits zero.
3. **Primary rank bound: discharged by source alignment.** The [primary accepted manuscript](https://pure.tue.nl/ws/portalfiles/portal/99596886/1211.1506.pdf), inspected during this independent audit series, defines H_t on all perfect matchings of the complete graph (abstract, PDF page 1). Theorem 3.4 and Corollary 3.5 (PDF page 9) give rank_GF(2)(H_t)=2^(t/2-1) for every even t>=2. Substituting t=26 gives the required upper bound 4096. No bipartite restriction is introduced by this substitution; the earlier t=22 or t=24 certificates are not used to infer the generic formula.
4. **Universal matching quantifier: discharged analytically.** A rank-4096 restriction proves that the selected complete rows are independent; the generic upper bound makes them span the entire row space. Given any F={(a_i,b_i):i=1,...,13}, the cyclic linking matching {(b_i,a_(i+1))} forms one alternating cycle with F, so F's column is nonzero. If all selected rows vanished there, their entire span would vanish, contradiction. The supplied 4096 columns witness rank; they do not restrict the quantified original F.
5. **Cycle expansion: discharged analytically.** Each forest consists of thirteen paths whose disjoint interiors are precisely H\U. A connecting endpoint pairing therefore expands to one connected degree-two graph on the 29 specified vertices. A shared F/pair edge would form an isolated labelled two-edge component on the endpoint level and is incompatible with connectivity on 26 endpoints. In particular a one-edge forest path cannot duplicate F. The expanded cycle is simple, retains every edge of F and has only short introduced edges.

The counterexample/rejection pass explicitly tests the relevant obstruction types: malformed support, multiple components, cycles, shared pair edges, dependent rank, unmarked instead of marked orbit matching, illegal root-mirror bridge sources, and finite-column versus universal matching quantifier confusion. No mathematical counterexample or open gap was found in the declared scope.

## Actual three-bridge transfer

The application starts only from the **4096 accepted residual inputs** in Q5_T26_RANK_BATCH_REVIEW_remaining_v{1,7,31}.bin, bound by the existing PASS review's evidence hashes. Normalize the root u=0, and let Z be the four other even holes and W the five odd holes. The target v is covered, opposite in parity to root, and Z union W is independent. For c=0 the accepted five-direction theorem applies. For c>0 the accepted uniform transfer is replayed as follows.

- Row (a,b)=(4,2): s=a+1-b=3. Enumerate every three-element S subset of Z intersect A. Mirrors Y are three distinct odd vertices, internally covered because independence excludes W and a free source excludes a crossing mate; they differ from root by parity. If root belongs to A use r=u and complete X_A union S. Otherwise choose r in S and complete X_A union (S\{r}). Both leave balanced (2,2) A holes, within the accepted four-hole endpoint input. B has no surviving even hole, and its odd holes are exactly (W intersect B) union Y, with precisely Y omitted.
- Row (a,b)=(1,5): t=b-a-1=3. Enumerate every three-element S subset of W intersect A excluding the possible source whose mirror is root. Since v is covered it is not a free source. Five candidates minus at most one exclusion leave at least four, so legal triples exist. Mirrors Y are three distinct internally covered even vertices, different from root and original nonroot holes. If root is in A take r=u; otherwise take an even crossing port, guaranteed by even-minus-odd port count b-a=4. The completion leaves balanced (2,2) A holes. B has no odd hole, and its even holes are exactly (Z intersect B) union Y, omitting precisely Y.

In each case delete the artificial completion matching, attach original crossing edges and the three actual short bridges. The tagged terminal closure is a forest by the accepted transfer proof. Conflicts occur only at Y; their distinct original pendant mates have opposite parity and are internally covered, hence lie outside transferred endpoints. Simultaneous suppression therefore produces paths rather than cycles and yields an **arbitrary complete-graph matching** L with precisely the displayed B holes. Every selected local theorem allows every possible such L, even when compression makes long or same-parity required edges. A common automorphism must map H and Y together; mapping only the unmarked hole set would be insufficient. Expand the resulting local cycle through conflict paths and A paths, then delete the tag. The original root and covered target are preserved, every original matching edge survives, and every surviving introduced edge is short. The argument is uniform over **all** original short matchings realizing the eligible hole/target geometry, not one sampled matching.

## Exact independent coverage

The new Python application checker generates all translations and coordinate permutations of the seven entire marked pairs (H,U), obtaining 14400 distinct marked images. It enumerates every one of the six outer cuts and every legal source triple on every accepted input, computes its actual B projection, and tests marked membership against this independently generated lookup. It validates each producer witness's cut, row, source triple, actual holes, omissions and orbit index. An independent witness with a common cube automorphism is saved for every newly covered input.

| Target | Accepted input | Newly covered | Still OPEN |
|---:|---:|---:|---:|
|1|910|330|580|
|7|1476|693|783|
|31|1710|720|990|
|Total|4096|1743|2353|

Counts are taken as exact unions, despite overlaps between the seven local inputs. The independent residual files preserve original record order, equal exactly the input set minus independently covered records, and have exact byte equality with the frozen producer residuals.

| Independent residual | SHA256 |
|---|---|
|Q5_T63_RANK_REVIEW_remaining_v1.bin|36ebe44e84f00ecd1d7657fa89ab7bf9b1ace89ad7ffd6ed3391e616d3e06002|
|Q5_T63_RANK_REVIEW_remaining_v7.bin|9990ce743b27f13efdd045e1d1e9e22c408f8fe9481ef20510ef631507e3ae06|
|Q5_T63_RANK_REVIEW_remaining_v31.bin|9876a0b36084267a1034f6911676d754ab3f032363a5367e1d8915517f16ebe0|

The dependency DAG is primary rank theorem + independent finite certificates -> seven exact local universal theorems; these + accepted uniform transfer/A endpoint + accepted exact 4096 domain -> the new 1743 uniform geometry reductions. It is acyclic and uses no desired higher-layer claim as a premise.

No fatal, critical or major issue remains in this scope. Full unrestricted T63, full ten-hole covered/free results, higher Q6 layers and full P6 remain **OPEN**. The 2353 residual records are obligations, not counterexamples. Other new T15/T17 routes must be combined by exact sets to avoid repeated decrements.

Evidence: Q5_T63_RANK_REVIEW_check.cpp/.exe/.py/.json, Q5_T63_RANK_REVIEW_certificates.log, Q5_T63_RANK_REVIEW_witnesses.json and the three independent residual files. Main state and producer files remain unchanged.
