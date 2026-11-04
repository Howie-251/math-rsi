# Proof Package: core 4, two-hole-face cut

Date: 2026-11-01. ARIS proof-writer. No global status or previously audited files are changed.

## Claim

Let $F$ be any complete-graph matching on $V(Q_5)$ with holes $\{0,1,2,7,11,31\}$. If no edge of $F$ crosses coordinate $2$, there is a simple cycle on $V(Q_5)\setminus\{1,2\}$ containing $F$, all of whose other edges are short hypercube edges.

The universal core 4 claim, allowing original crossings, is **NOT CURRENTLY JUSTIFIED** here. Neither full T15 nor eight-hole P6 is claimed.

## Status

**PROVABLE AFTER WEAKENING / EXTRA ASSUMPTION**: the displayed zero-crossing claim follows from the explicit finite checks below and the imported perfect-matching extension theorem. Positive residual witnesses have been checked by a separate Python implementation. The separate C++ coverage checker has also completed successfully: all $135135$ A matchings and $10395$ B matchings give exactly $155931$ required residuals, all saved, with zero missing. Fresh-context audit remains necessary before global integration.

## Assumptions and notation

A short edge joins two binary labels differing in one bit; original required edges may have arbitrary lengths. Cut coordinate $2$, and define
$$b(x)=(x\mathbin{\&}3)+2(x\mathbin{\&}12),\qquad a(x)=b(x)+4.$$
Thus $A$ is the one-face and $B$ the zero-face, both labeled by $0,\ldots,15$. Their local holes are $\{3,15\}$ and $\{0,1,2,7\}$ respectively. Both omitted vertices $1,2$ lie in $B$. Under the zero-crossing hypothesis the internal matchings $F_A,F_B$ have seven and six edges.

## Proof strategy and dependency map

1. The perfect-matching extension theorem used elsewhere in the project: every perfect matching of the complete graph on $V(Q_4)$ extends to a Hamiltonian cycle using only short additional edges. This is the Fink import in `Q4_CORE_AND_A4_SPLIT.md`; it applies to arbitrary required edges.
2. Two short bridges at local labels $3,15$ work for $5760$ of the $10395$ possible $F_B$, uniformly in $F_A$.
3. Four-bridge forest spectra cover every remaining input except $155931$ explicit pairs.
4. Each remaining pair has a directly verified $30$-cycle certificate.

## Proof

### Step 1. The two-bridge transfer

Add the artificial edge $3_A15_A$ to $F_A$. This is a perfect matching, so the imported theorem gives a Hamiltonian cycle on all $16$ A vertices. Delete the artificial edge to get a spanning $3_A$--$15_A$ path preserving $F_A$.

If there is a spanning $3_B$--$15_B$ path on $B\setminus\{1_B,2_B\}$ preserving $F_B$ and using only short new edges, join these disjoint paths by the two short bridges at $3,15$. This yields the required $30$-cycle.

This B-path test is exact and extremely small. The set of new short edges must have degree two at $0,7$, degree zero at $3,15$, and degree one at the other ten supported vertices. There are exactly two such short-edge sets. Either produces a B spanning path precisely when its union with $F_B$ is simple and acyclic. Exhaustion of all $10395=11!!$ B matchings gives $5760$ successes.

An equivalent compressed table has omitted vertices $\{1,2,3,15\}$, retained free vertices $0,7$, and a required matching on the remaining ten vertices. All $945=9!!$ inputs have been classified: $576$ positive, $369$ negative. After suppressing $3,15$ in B, the zero-crossing B cases split as $5760$ positive, $3690$ negative, and $945$ with the required edge $3_B15_B$ closing an inaccessible component. The separate checker exhausts the two possible degree completions, checks every positive cycle, and regenerates all $945$ matching inputs; this classification uses no bounded-search negative claims.

### Step 2. The four-bridge transfer

Take any distinct $u,v\in V(Q_4)\setminus\{1,2,3,15\}$ of opposite parity. There are exactly $36$ unordered choices. The bridge labels are $E=\{3,15,u,v\}$; either or both retained free B vertices $0,7$ may belong to $E$.

On A, enumerate every short perfect matching $N_A$ on $V(Q_4)\setminus\{u,v\}$. Retain it if $F_A\cup N_A$ is simple and acyclic. The resulting graph has degree one exactly at $E$ and degree two everywhere else, hence consists of exactly two paths covering A. It induces a pairing $p_A$ of the four bridge labels.

On $B'=V(Q_4)\setminus\{1,2\}$, enumerate every short graph $N_B$ with
$$\deg_{N_B}(x)=2-\deg_{F_B}(x)-\mathbf1_{x\in E}.$$
These degrees depend only on the hole and bridge sets, not on the individual matching edges. Retain $N_B$ when $F_B\cup N_B$ is simple and acyclic. It then consists of exactly two paths covering $B'$, inducing a pairing $p_B$ of $E$.

Whenever $p_A\ne p_B$, add the four short bridges. The resulting graph is a single cycle: contraction of each path gives the union of two distinct perfect pairings on four labels, which is one alternating four-cycle. Expansion restores all $16+14=30$ vertices. Every required edge survives, and every other edge is short.

This proves the existential order used by the spectra: an A pattern and a B pattern may be chosen separately, and only their induced endpoint pairings must differ. No particular A path is assumed to work for all B matchings.

### Step 3. Complete zero-crossing enumeration

The producer `t15_core4_fourbridge_c0.cpp` enumerates all $135135=13!!$ A matchings and all $10395=11!!$ B matchings. For each bridge choice it stores the three possible A endpoint pairings and, on B, the A pairings compatible with at least one B pairing. Together these form $108$ bits. One further bit records the two-bridge construction. The A two-bridge bit is always available by Step 1.

Two signatures have a common bit exactly when one of Steps 1--2 supplies a cycle. The B matchings have $5306$ distinct signatures. Grouping by these signatures preserves every original B matching, so it exhausts all $1404728325$ original A--B pairs without selecting representatives alone.

Precisely $155931$ pairs have disjoint signatures. They involve $10401$ A matchings. Of those, the $10395$ A matchings containing local edge $0_A7_A$ each have the same $15$ residual B matchings; six additional A matchings have one residual B each. These descriptive counts were independently recovered from the saved residual inputs; their structural form is not needed by the transfer.

The separately implemented checker `verify_t15_core4_c0_coverage.cpp` uses path walking and explicit degree checks instead of the producer union-find. It enumerates both full matching families, rebuilds their signatures using independently generated degree patterns, and checks that every uncovered pair occurs in the saved residual list. Duplicate residual inputs are rejected. Equality of the rebuilt residual count and saved-list size also checks that no saved pair lies outside that exact residual set. `t15_core4_c0_patterns.py` generates complete degree patterns by selecting all remaining neighbors at the first vertex of positive residual degree.

### Step 4. Positive certificates for every residual input

`t15_core4_c0_residual.cpp` reads the $155931$ residual matchings and searches oriented orders of their required-edge blocks and the four retained free singleton vertices $0,7,11,31$. All $155931$ inputs have positive witnesses; there are zero exhausted or node-limited inputs. Total nodes: $5489075$; maximum for one input: $1095$. These search counts are diagnostic only.

`verify_t15_core4_c0_residual.py` checks each saved record against its exact input and verifies thirty distinct vertices, exact support $V(Q_5)\setminus\{1,2\}$, inclusion of all thirteen required edges, and shortness of every other edge, including the closing edge. It checks input and witness file lengths and input holes as well. Every record passes.

Each witness record consists of $26$ required-edge endpoint bytes followed by $30$ cycle vertex bytes. The input-file SHA-256 is `ab94b1cbb9d6bd538da0569e72390e8d199d1832ca5273d71ac9577b3b1ea8f8`; the witness-file SHA-256 is `8d56e5820a8de2732c49a47ddabbd096d06c9699ef2f3f25193a67a032f50b2f`.

Steps 1--4 prove the zero-crossing claim, subject to the explicit imported theorem and recorded finite checks.

## Arbitrary-crossing sufficient reduction and remaining finite kernel

Let $C$ be the original crossing matching, with A port set $X_A$, B port set $X_B$, and unrestricted partner bijection. The crossing count $c$ is even and satisfies $0\le c\le12$.

There are exactly $272$ short perfect matchings $N$ of $Q_4$. For each one disjoint from $F_A$, form
$$H=F_A\cup N\cup C\cup F_B\cup\{3_A3_B,15_A15_B\}.$$
If $H$ has no cycle component, suppress its paths through A and through B vertices $3,15$. All A vertices and those two B vertices have degree two; the ten B vertices outside $\{0,1,2,3,7,15\}$ have degree one; retained free B vertices $0,7$ have degree zero. Thus compression gives a five-edge matching $L$ with holes $\{0,1,2,3,7,15\}$.

If this $L$ belongs to the $576$ positive entries of the twelve-cycle table, expand its five required edges through their corresponding paths. The result is the desired $30$-cycle. This proof applies to every port location and crossing bijection whenever the stated two conditions hold.

The list of $272$ N candidates is complete for this two-bridge architecture: subtracting required-edge, crossing, and bridge incidences from the desired degree two at every A vertex leaves degree one everywhere on A. Therefore every possible short completion in this architecture is a short perfect matching. `t15_core4_A_short_perfect.py` enumerates all $272$ without pruning.

The exact remaining universal obligation is to show that every positive-crossing input has some one of these $272$ candidates with no closed component and positive compressed table entry, or to supply a different construction. The zero-crossing negatives show that this particular architecture alone cannot be universal. The four-bridge method above is proved only for zero original crossings.

There are $2390479$ possible A internal partial matchings relevant to $c\le12$. By crossing count $c=0,2,4,6,8,10,12$, the counts are respectively $135135,945945,945945,315315,45045,3003,91$, from $\binom{14}{c}(13-c)!!$. An enumeration of those A partials alone would not cover B internal matchings, B port positions, or crossing bijections. None of those quantifiers is discharged by this package.

## Open risks and reproducibility

- Imported perfect-matching extension theorem must retain its arbitrary complete-graph matching scope.
- This is a zero-crossing local closure, not full core 4, core 24, T15, or eight-hole closure.
- Independent checker reports are saved under `t15_core4_*_verification.json`; fresh-context semantic audit is still required.
- Run the Python Q4 producer and checker, the independent pattern generator, the C++ coverage checker, and the residual Python checker from the workspace root. All C++ files compile with `g++ -O3 -std=c++17`.
