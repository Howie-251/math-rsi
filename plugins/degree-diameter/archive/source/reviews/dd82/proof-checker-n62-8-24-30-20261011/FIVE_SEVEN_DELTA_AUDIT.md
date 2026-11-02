# Delta audit: four-point components and the five/seven-component candidates

**PASS — the uniform lemma and both stated applications are justified.** No mathematical issue requiring a source edit was found. This is an authorship-independent, same-family/provisional **delta** review of `proofs/dd82/n62/FIVE_SEVEN_COMPONENT_QUOTIENT_EXCLUSIONS.md`. It uses the existing reviewer task `/root/proof_review_n62_8_24_30`, not a newly isolated review context. Requested invocation metadata remains `gpt-6-astra`, reasoning `ultra`; backend identity is not independently attested.

The reviewed conclusion is precisely: in an actual legal order-62 graph, any four-vertex positive-repeat-support component containing an original edge is D0_EDGE_BOUT and has a distinct six-vertex unit-prism repeat component whose induced original graph is independent. Consequently neither complete component pattern `(4,8,10,20,20)` with internal degrees `(1,2,0,2,1)` nor `(4,4,4,10,10,10,20)` with internal degrees `(1,1,1,0,0,0,2)` can occur.

Enumeration completeness, universal connectedness of B, arbitrary order-62 exclusion, and the value N(8,2) are outside this delta review. No solver, enumeration, formalization, other proof audit, or source edit was performed. Output is limited to this Markdown file and its JSON counterpart.

## Inputs and dependency scope

The complete target was read, including the lemma at lines 5–9, source hypotheses at 31–65, proof at 80–120, and the two matrices and applications at 124–162.

New dependency checking focused on `GLOBAL_DOUBLE_TRIANGLE_QUOTIENT.md`, Section 2, and `D1_MATCH_HARD_BRANCH_REDUCTION.md`, Section 1. The D0 source rows in `D0_DOUBLE_COMPONENTS_AND_D1_OUTLET.md`, Sections 1–2, were also checked directly. The actual identities, triangle-pairing consequence, D2/BIN exclusions, and arbitrary-double-root classification had already been read and checked in this review task. Their mathematical contents, not prior audit verdicts or claims of external review, supply the dependencies.

The following finite dependency chain has no circularity:

```text
actual identities + triangle pairing → four-point component is triangle-free
original internal edge + row sum three → a double repeat in that component
double-root coverage + D2/BIN exclusions → D0 or D1
raw D1 Section 1 rows → six distinct vertices in its heavy component
component order four → D0
D0 closure + existence of an original edge → D0_EDGE_BOUT
D0 companion construction → distinct closed independent six-point prism
each proposed complete size list has no six → contradiction.
```

The D1 six-vertex deduction precedes the harder reroot and minimum-size results, so it does not rely on them. The D0 companion is established for the selected D0 component; no pairing or parity assertion about all D1 heavy edges is used.

## Obligation ledger

| ID | Verification |
|---|---|
| D01 | **Actual binding** (5–9,31–36,63–65). C is an actual connected support component of the actual symmetric nonnegative integer row-sum-three B. Thus its rows have no support outside C. Quotient internal degrees count original neighbors at every vertex, by equitability. |
| D02 | **Local triangle-freeness** (82–89). Triangle pairing produces a closed connected support component of exactly six vertices through any original triangle vertex. The component containing such a vertex is unique, so it cannot also be the stipulated four-point C. This proves triangle-freeness only for vertices of C; triangles elsewhere are permitted. |
| D03 | **Original edge forces a double repeat** (93–105). If u,v∈C are adjacent, local triangle-freeness gives c(u,v)=0, hence Buv=0. For C={u,v,x,y}, the full row sum is therefore Bux+Buy=3. Under the cited B≤2 bound, integrality forces the unordered values {1,2}. No positive support can escape C. |
| D04 | **Double-root coverage applies to this edge** (109). Choosing an endpoint of this particular double edge as root gives exactly one exceptional parent triple and one exceptional parent pair, with all other outside parent sets singleton. The intersection classification and already checked D2/BIN exclusions leave D0_MATCH, D0_EDGE_BOUT, or D1_MATCH. This is coverage for an arbitrary double edge, not merely existence of some D1 root somewhere in the graph. |
| D05 | **D1 really has six distinct vertices** (46–56,110–111). In the D1 source, 0,w,a are distinct, and the calculation at (1,w) gives Baw=0; at (0,a) it gives B[X,a]=0. Thus w's remaining repeat r and a's two units are ordinary points. For every ordinary y, Bwy+Bay+Σx∈C1 Bxy=1_{C2∪C3∪C4}(y). Nonnegativity makes each Bay≤1, so a's remaining two units occur at distinct p,q. At y=r, Bwr=1 forces Bar=0, so r differs from p and q. All three ordinary points differ from 0,w,a. |
| D06 | **All six D1 vertices lie in the heavy component** (50–54,110–111). The positive repeat edges 0w,0a,wr,ap,aq connect all six vertices to 0. This concerns one actual component, not a union of the heavy and generated-triangle components. Therefore its order is at least six and it cannot be C. |
| D07 | **D0 identity and branch selection** (112–119). The D0 theorem forces complete rows on {0,w,a,b} forming the connected alternating 2,1,2,1 cycle, so these four vertices constitute the entire support component and it equals C. D0_MATCH induces no original edges. The given original edge rules it out, leaving D0_EDGE_BOUT, which induces exactly the matching edges 0b and wa and hence has rCC=1. |
| D08 | **Companion has six distinct vertices** (57–61,114–116). The D0 source constructs S={1,2,3} in the root neighborhood and three distinct ordinary outside vertices c1,c2,c3, with B(i,ci)=1. Distinctness follows from Σx∈X B(x,ci)=1 in BOUT; a coincidence would contribute two units. The ci are distinct from a because a~ci, and from w by its complete repeat row; they are outside X and distinct from 0. Consequently S and {ci} are disjoint and both avoid {0,w,a,b}. |
| D09 | **Companion is exactly a closed connected unit prism, independent in G** (57–61,115–119). In S the repeat entries are all one by the D0 parent data. All ci neighbor both a and b, and Bab=2 with a,b nonadjacent. The triangle-free heavy endpoint a makes {ci} independent in G. Every pair of ci has B≥1 from their common neighbors a,b; each ci also has B(ci,i)=1. These three required units exhaust every ci row, forcing the unit triangle and no additional repeat edges. The S rows are likewise exhausted by their unit triangle and matching edges to ci. The resulting two triangles and matching form a connected closed six-vertex component. In BOUT each ci has unique root parent b∉S, so no original edge crosses between the two triples. Each triple is independent in G, hence the whole companion is independent. |
| D10 | **Five-component application** (124–140). The listed sizes sum to 62. The first actual quotient cell has order four and r11=1, so it contains an original edge. The lemma forces a distinct support component of order six. None of the complete five listed sizes is six. Only this diagonal entry and the complete size list are needed; the off-diagonal matrix entries and enumeration coverage are not assumptions of the deduction. |
| D11 | **Seven-component application** (144–162). These listed sizes also sum to 62. Each of the first three actual quotient cells has order four and internal degree one. Applying the lemma to any single such component forces a size-six support component, absent from the complete displayed size list. No assertion of three different companions is needed. |
| D12 | **Scope and statement match** (19–27,164–179). The argument proves the uniform four-point lemma and excludes the two exact size/internal-degree patterns, hence the displayed matrices. It neither assumes nor proves that those patterns exhaust five/seven-component quotients, and does not infer B connected or exclude an arbitrary legal graph. |

All twelve obligations are discharged. There are no open fatal, critical, major, or minor issues. Every sum is finite; no asymptotic, probabilistic, limiting, analytic-interchange, or hidden-uniformity condition occurs.

## Counterexample pass

1. **A triangle in C or elsewhere.** A triangle through a vertex of C forces its component to have order six, contradicting the hypothesis. A triangle outside C creates no contradiction with the proof and is not silently prohibited.
2. **Repeat weights 3 and 0 instead of 2 and 1.** The cited global bound excludes this. More locally, a weight-three entry exhausts both endpoint rows and makes a closed two-vertex component, which cannot occur inside the connected four-point C. Thus the needed local bound follows without the global triple-repeat enumeration.
3. **Identify D1 ordinary endpoints to fit four vertices.** Setting p=q would require Bay=2 at one ordinary y and violate the displayed right-hand side bound 1. Setting r=p or r=q would give Bwy+Bay≥2 and the same contradiction. They cannot coincide with 0,w,a by their ordinary status. The component cannot be compressed this way.
4. **Attach six D1 vertices to different components.** The five explicit positive repeat edges connect all six to 0, so splitting them would contradict the definition of a support component.
5. **Let the D0 companion overlap the original four points, or collapse two ci.** Root-neighborhood versus ordinary-point locations exclude overlap with S; complete repeat rows and the original edges a~ci exclude the heavy/light points; the D0 commutation row sum excludes coincident ci. Thus six distinct points are actually present.
6. **Allow extra repeat edges from the companion or original edges between its triples.** Every companion row already uses three units, excluding repeat exits. In BOUT the unique original root parent of every ci is b outside S, excluding original cross-edges; triangle-freeness at a excludes edges within the ci triple.
7. **Hide an extra size-six component outside either candidate list.** The applications explicitly assume complete component lists whose sizes sum to all 62 vertices. There are no remaining vertices for such a component. If the lists were only partial, the conclusion would not follow; that weaker hypothesis is not asserted.

No counterexample was found under the theorem's hypotheses. The pass rests on the displayed derivations and hypothesis checks, not on unsuccessful searches.

## State and limitations

Verdict **PASS**, `reason_code: all_proofs_complete`, `review_independence: same-family`, `acceptance_status: provisional`, `review_scope: delta`. Three claims were checked: one uniform lemma and two applications. No source fix was required. The referenced global triple-repeat result can be avoided for the local row bound by the elementary observation above, but no target edit is needed for correctness.

This audit does not review quotient enumeration, combine this result with the three-component exclusions, certify a theorem that B is connected, establish a Lean result, or close the order-62/N(8,2) problem.
