# Brown57 nine-deletion assembly: fresh proof audit

**Verdict: PASS, same-family / provisional.** The paper argument and the completed finite checks establish the claimed modification bound for the supplied Brown57 graph. No open mathematical or search-completeness gap was found. One cosmetic sentence in a dependency was reported, corrected by the parent/author, and re-read during this audit.

For every finite simple undirected graph $G$ on the 57 supplied Brown labels and one new vertex $x$, maximum degree at most 8 and diameter at most 2 imply at least **10 deleted Brown edges**, and exactly as many added old–old edges. This is a restriction relative to that fixed graph. It is not nonexistence of arbitrary order-58 graphs.

Audit date: 2026-10-11T09:21:10Z. Reviewer task: `/root/proof_review_brown9_complete`. Requested route: `gpt-6-astra`, reasoning `ultra`; actual backend model/effort attestation is unavailable. This is a fresh same-family review with explicit finite computations, not formal verification or cross-family acceptance.

## What was read and what was used

The complete new `BROWN_NINE_DELETE_OBSTRUCTION.md` and `BROWN_R9_SEVEN_III_OBSTRUCTION.md` were read, together with the full six-III, eight-III-plus-EE, eight-deletion, earlier extension, and Brown57 construction proofs. All five load-bearing finite source files were read: the three C++ searches and the two Python family/basic-fact checkers. The actual `brown57.edges` and referenced finite JSON data were inspected and independently reconstructed.

The original order-58 root counts and the earlier $r\le8$ proofs were checked directly. Previous reviewer verdicts quoted inside the papers were not treated as proof. The larger exploratory EE profile is unnecessary and was not relied upon. No known-order63–65 work, SAT, added-edge completion, Lean, or wiki work was performed.

The reviewer wrote only this audit's Markdown/JSON files. The parent/author made the single wording correction recorded below. No hash, checksum, manifest, TeX, PDF, or HTML was produced.

## Mathematical closure

The concrete graph independently matches the displayed $\mathbb F_7$ orthogonality construction. It has 224 edges, class sizes $(8,21,28)$, edge-type counts $(II,CE,IE,EE)=(42,56,84,42)$, and exactly 14 III plus 42 IEE triangles. All degree, incidence, and unique-triangle premises used in the proof were checked directly against the edge list.

The order-58 hypothesis forces 8-regularity: a vertex of degree at most 7 reaches at most $1+7+7\cdot7=57$ vertices within two steps. The 232 candidate edges leave 224 old–old edges after the eight edges incident to $x$, giving exact deletion/addition balance. At a root $v$, its $t(v)$ triangles consume $2t(v)$ of the 56 second-step incidences, so $58\le65-2t(v)$ and $t(v)\le3$. Consequently every old internal vertex must lose one of its four old triangles.

The resource argument is valid for arbitrary repair edges. If $d_v$ is deletion degree, $k_v=d_v+1_C(v)$, and $S=N_G(x)$, then $|S|=8$, every selected vertex has positive deficit, and the exact number of available new old–old incidences at $S$ is
$$
\sigma(S)=\sum_{s\in S}(k_s-1).
$$
Every target outside the retained closed neighborhood needs a new edge from $S$. Such an incidence reaches at most one additional target. An added edge within $S$, or overlapping coverage, can only waste this resource. The $C$- and $I$-coverage bounds therefore do not presume a matching or any other unsupported form of the added-edge graph.

The earlier proof excludes $r\le7$, and each of the five $r=8$ cases was checked again from its actual argument. For $r=9$, $a+b\le9$ and $3a+b\ge21$ give $6\le a\le9$. Every $a=8$ deletion set has eight base III edges and one extra of the four actual old edge types. Every $a=9$ set is all II. There is no missing deletion-type case.

The new assembly's algebra was checked explicitly:

- **All II:** the selected III union covers $I$. Base spare count is at most $3a-21$; each of the $9-a$ extra deletions adds at most two. Thus $\sigma\le a-3\le6$. Since $e=0$, $C$ needs at least $j$ incidences, giving $j\le6$. With $D=\sum_{S\cap I}d_i$ and $\sigma=D-j$, internal coverage is at most $5j-D+\sigma-j=3j\le18$.
- **Eight III plus CE:** the III union covers all 21 internal vertices; its spare count is at most three, and the CE deletion gives at most one additional spare, at its $C$ endpoint. Hence $\sigma\le4$, $e\le1$, and retained $C$-coverage is at most $e$, so $j\le4$. Substituting $\sigma=D-j+\varepsilon_C$ gives internal coverage at most $3j+3e+\varepsilon_C\le16$.
- **Eight III plus IE:** a full-cover union gives at most three base spares plus one extra. A 20-cover union gives at most four base spares, and the extra's internal endpoint must be the missing vertex, initially of deletion degree zero; the extra therefore adds no spare. In both cases $\sigma\le4$, $e\le1$, and $j\le e+\sigma\le5$. The external endpoint retains two internal neighbors. The displayed substitution gives at most $3j+3e+\varepsilon\le19$ when $j\ge e$; if $j<e$, $(j,e,\varepsilon)=(0,1,0)$ gives two.
- **Eight III plus EE, full cover:** in all 14 families the three repeated internal vertices form a selected central triangle. Its single base deletion can hit only two, so $\sigma\le2$. With $e\le2$ and $j\le e+\sigma$, internal coverage is at most 20.
- **Eight III plus EE, 20-cover:** all 42 families and both allowed EE edges satisfy the six claimed incidence properties of the six-point set $Z$. The missing internal point has no deletion deficit and cannot lie in $S$. If $e\le1$, internal coverage is at most 19. If $e=2$, only $k=j-\sigma\le2$ selected internal points of deletion degree one can cover $Z$ through old edges or membership. For $k=0,1,2$, old coverage is at most $0,3,5$, and remaining new incidence budget is at most $2-k$. The resulting $2,4,5$ all fall below $|Z|=6$. In the exceptional pair $a,b$ of cross-edge endpoints, both retained closed neighborhoods contain $a,b$, so their union is at most four, not six.

The six-III and both seven-III cases are closed by their valid necessary-condition reductions and the completed finite searches below. These branches together exhaust every $r=9$ case.

## Finite family obligations

An independent Python reconstruction was run on one pinned CPU with a 55-second CPU limit and 60-second wall timeout; it completed in approximately 1.47 seconds. Its full command, source text, and output are in [RAW_FINITE_CHECK.json](RAW_FINITE_CHECK.json).

| Obligation | Independently obtained result |
|---|---:|
| Six III triangles with union 18 | 14 families |
| Seven III triangles with union 19 | 42 families |
| Seven III triangles with union 20 | 0 families |
| Seven III triangles with union 21 | 2 families |
| Eight III triangles with union 21 | 14 families |
| Eight III triangles with union 20 | 42 families |
| EE alternatives for those 42 families | 84 |
| Cover-19 known-deletion cases | 630 |
| Cover-21 known-deletion cases | 145,040 |

All complete recorded family data in `brown_r9_eight_iii_facts.json` matched independent reconstruction. The reconstruction also verifies the missing-triple fact for a6; the central triangle, six disjoint residual triangles, and disjoint unknown blocks for a7/19; all allowed extra-edge choices, affected base triangles, disjointness, and spare bounds for a7/21.

The cover-21 unordered extra-type case counts are $1554,4704,19152,3528,3080,28224,4704,57204,21168,1722$, in the paper's order. These agree both with the independent enumeration and with the C++ output after merging reversed type labels. The C++ program prints labels in edge-list order, so e.g. `CE+II` and `II+CE` are correctly combined; this is not a discrepancy.

## Search completeness and implementation

For a6 the nine deletion blocks are pairwise disjoint, so every deficit is one. No repair edge can touch $S$. It is therefore sound to relax retained-graph domination to domination in the original graph. The search's allowed set and block constraints contain every possible $S$.

For a7/19, the central deletion is the only possible source of repeated endpoints. Fixing each noncentral base triangle met by that deletion fixes all positive spare weights; the remaining disjoint blocks contribute only zero or one deletion degree. Ignoring their unfixed deletions can only increase coverage. The 15 cases per family are exactly the central edge joining both repeated vertices with $3^2$ base choices, plus the two central edges meeting only one repeated vertex with three choices each. The checker permits at most two vertices per unknown block and, for the five-point blocks, requires an adjacent pair. Its spare count is exact for each selected set.

For a7/21, every actual deletion set admits the extras-first representation in the proof. The two extras are distinct edges in the 203-edge pool, and fixing the affected base deletions excludes those extras. Duplicated representations are harmless. Every unaffected base triangle is disjoint from the known deletion endpoints; its selected vertices contribute zero spare weight.

The $h(S)$ correction is exact. With zero selected vertices in an unaffected triangle, its deletion changes no coverage from $S$. With two selected vertices, their connecting edge can be deleted without making either endpoint uncovered. With one selected vertex $v$, exactly one of its two incident edges must be deleted. The opposite endpoint loses coverage iff $v$ was its only neighbor in $S$; it is outside $S$, so membership does not rescue it. No known deletion touches that endpoint, and no other unknown block touches it. Both unsafe partners force one new uncovered vertex; a safe partner avoids that loss. These forced losses lie in distinct blocks and were initially covered, proving the exact formula $u_K(S)+h(S)$.

A successful final set has a complete DFS path. Maintain that all selected points lie in this fixed successful set, all of its unselected points remain available, and each ignored target is truly uncovered by it in the known-deletion graph. For a target it covers, follow the branch selecting its first available dominator. Earlier excluded dominators are not in the final set; local block exclusions likewise remove none of its remaining points. For a target it does not cover, follow the ignore branch. Its final number of uncovered vertices is at most its spare count, at most the global $M$, so the ignore budget cannot block this path.

The sum of the largest individual gains over the remaining selection slots, plus the remaining ignore budget, is an upper bound on the number of outstanding targets the path can handle. It overcounts overlapping coverage and ignores block conflicts, both in the optimistic direction. The availability-count prune is also necessary. If there are no outstanding unignored targets, the code still chooses further available vertices until exactly eight have been selected. A branch that ignores a target later covered may be redundant; it cannot remove the consistent path just described.

At depth eight the predicates count actual uncovered vertices and actual spare weight; a7/21 additionally counts $h(S)$. Each recursive step either increases depth or adds a previously unignored target, so the finite search terminates. The a7/21 diagnostic stop after ten survivors was not triggered: the final line has `passes=0 complete=1`.

The concrete C++ input contract was checked: 57 valid labels, sorted edge pairs, 224 unique edges, and 14 uniquely enumerated III triangles. All shifts use labels below 57 in unsigned 64-bit masks; count-trailing-zero calls are guarded by nonzero masks; gain-array indexing follows the candidate-count test. Compilers were invoked without `NDEBUG`, so assertions remained active. No missing-input or arbitrary-input parser robustness is needed for this fixed-input proof.

## Fresh compilation and bounded reruns

Each source was freshly compiled with `g++ -O3 -std=c++17` to a temporary executable. Each compile and each run used one pinned CPU, a 55-second CPU limit, and a 60-second wall timeout. Every process exited zero; the temporary executables were removed afterwards. Full commands, limits, exit codes, stdout, and stderr are in [RAW_CPP_CHECKS.json](RAW_CPP_CHECKS.json).

| Check | Families | Known cases | Nodes | Survivors | Run wall time |
|---|---:|---:|---:|---:|---:|
| a6 domination | 14 | — | 1,189 | 0 | 0.006 s |
| a7, union 19 | 42 | 630 | 107,074 | 0 | 0.149 s |
| a7, union 21 | 2 | 145,040 | 5,805,357 | 0 | 8.056 s |

The a6 and a7/19 per-family node arrays exactly match the retained JSON. The a7/21 aggregate totals and all normalized extra-type counts also match. No a6 dominating leaf reaches its later deletion-compatibility filter, so that unused filter is not load-bearing.

## Issue and correction

**MINOR-01 — cosmetic overstatement, fixed.** The initially read a6 proof, line 27, said every Brown edge belongs to one triangle. The 56 CE edges are counterexamples to that universal wording. The particular edge $mm'$ in its argument is II and does lie in a triangle; the already stated at-most-one-triangle premise suffices for the contradiction.

The reviewer reported the defect immediately. The parent/author changed the phrase to **“every Brown edge belongs to at most one triangle.”** The reviewer then re-read the updated line and confirmed that correction. This was the only revision during the audit; no mathematical argument or finite input changed, and no rerun was needed.

There were no fatal, critical, or major issues, no theorem counterexamples, and no open issues at completion.

## Obligation and counterexample accounting

The 28 discharged obligations, dependency graph, assumptions, and typed symbols are recorded in [PROOF_SKELETON.md](PROOF_SKELETON.md) and [PROOF_AUDIT.json](PROOF_AUDIT.json). The JSON records eight concrete counterexample/edge-case passes, including concentrated deletion degrees, boundary $j<e$, the absent 20-cover family, the DFS ignore branch, the residual $h(S)$ calculation, and both cross-edge endpoints in the $Z$-bound.

All arguments concern finite sets and integer counts. There are no asymptotic constants, probability-mode transitions, limit exchanges, or analytic hypotheses to discharge. No WLOG symmetry quotient is used in the searches: all listed triangle families and all stated known-deletion cases are enumerated.

The resulting theorem is the fixed-Brown edit-distance lower bound of ten. Its proof has ordinary computer-assisted assurance from reviewed finite code and successful executions; its semantic audit status remains same-family/provisional.
