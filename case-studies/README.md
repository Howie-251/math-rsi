# Six mathematical research threads

[English entry](../README.md) · [中文入口](../README.zh-CN.md) · [Bilingual visual tour](../docs/HOMEPAGE.md) · [Domain routing](../docs/DOMAIN_ROUTING.md)

This is the shared index for all six results. Existing case pages and plugin records own the detailed proofs, current evidence scopes and reproduction commands. HTML readers work locally after cloning; GitHub shows their source.

## Property B

**Hypergraph two-coloring:** individual reported lower bounds for $m(5),\ldots,m(12)$ are $35,67,131,267,543,1112,2275,4664$. A uniform theorem improves the specified exact RS budget for every $k\ge12$.

The uniform theorem and earlier $m(5)\ge33,34$ have end-to-end Lean proofs. The bound 35 has a complete written candidate with unfinished Lean. The other individual bounds retain parameter-specific paper/computational evidence; the k=12 independent checks cover the whole parameter/trace domain plus 20 exact probability checks, rather than a second full probability implementation.

[Case and per-parameter status](property-b/README.md) · [Offline reader](property-b/index.html) · [General theorem](property-b/readers/PROPERTY_B_GENERAL_BOUND.html) · [Lean reader](property-b/readers/PROPERTY_B_GENERAL_LEAN.html) · [Domain skill](../plugins/propertyb/skills/mathrsi-propertyb/SKILL.md)

## Error-correcting codes

**Four exact binary-code distances:** $d_2(43,10)=16$, $d_2(44,10)=17$, $d_2(44,11)=16$ and $d_2(42,16)=12$. The first three follow from the old 172-parent exclusion and constructions; 42/16 applies a published 2020 theorem. The remaining range is $16\le d_2(45,11)\le17$.

Lean reductions retain explicit literature, classification and computation premises. Actual-matrix checking, one-parent replay and the whole-domain exclusion have different scopes. The recent $[72,36,\ge16]$ A/B/C node example teaches research organization; it is not an additional solved parameter.

[Plugin and methods](../plugins/ecc/README.md) · [Actual checks and import boundaries](../plugins/ecc/evidence/IMPLEMENTATION.md) · [Node organization example](../plugins/ecc/skills/mathrsi-ecc/examples/node-research.md)

## Degree–Diameter

**A 2,567-vertex, 10-regular graph of exact diameter four** exceeds the Comellas 2,566 entry checked on 2026-11-05. Earlier dated table improvements cover $(11,5)$, $(12,5)$ and $(16,4)$; the combined catalogue has 163 graph instances, 44 parameter pairs and 49 concrete Lean instances, including intermediate graphs.

The new graph ran with **MathRSI v2 + DD + the PR #7 repair**. Independent all-roots BFS and `Fin 2567` Lean assembly/import receipts are preserved. External formal C review is incomplete, and the portable package does not contain the full rebuildable Lean project. The v4 edit replay reconstructs ten graphs and checks literal structure; it does not rerun BFS or Lean.

[Case study](degree-diameter/README.md) · [中文](degree-diameter/README.zh-CN.md) · [Illustrated reader](degree-diameter/index.html) · [Execution provenance](degree-diameter/evidence/execution_version.md) · [Reconstruction](degree-diameter/reproduce/README.md) · [Plugin](../plugins/degree-diameter/README.md)

## Erdős Problem 86

**Square-free hypercube density:** $\pi_Q(C_4)\le23662061277957791/40000000000000000\lt0.59155154$, improving the specified 0.60318 reference toward the conjectured $1/2$.

This is an asymptotic edge-density bound. Full exact local replay covers 13,150,453 legal $Q_4$ completions; analytic high-dimensional averaging supplies the global bridge. There is no Lean formalization or claim of SDP optimality. Shared completions, synchronized rooted flags and exact rational Gram certificates are the reusable methods.

[Plugin and source map](../plugins/hypercube-extremal/README.md) · [Full finite replay and scope](../plugins/hypercube-extremal/evidence/IMPLEMENTATION.md) · [Domain skill](../plugins/hypercube-extremal/skills/mathrsi-hypercube-extremal/SKILL.md)

## Ruskey–Savage Q6

**Every matching in $Q_6$ extends to a Hamilton cycle.** With explicit imported results, this also yields extension for matchings using at most six directions in any dimension. The stronger stored P6 statement concerns a Hamilton path from every free root to every opposite-parity target.

The whole-proof audit remains **same-family/provisional**, with no Lean. The bounded A10 replay reconstructs 1,024 forests, all 1,048,576 connectivity bits and rank 1,024. It does not replay all large P6 certificate streams; inventories identify omitted material. The general conjecture remains open.

[Plugin and mathematics](../plugins/hypercube-hamilton/README.md) · [Finite replay and whole-proof boundary](../plugins/hypercube-hamilton/evidence/IMPLEMENTATION.md) · [Domain skill](../plugins/hypercube-hamilton/skills/mathrsi-hypercube-hamilton/SKILL.md)

## Happy Ending

**Working manuscripts; independent review pending.** Received structural manuscripts claim $N(7,6,7)\le75$ and $N(7,7,7)\le76$, hence the geometric threshold $\mathrm{ES}(7)\le77$, improving the prior 76/77/78 chain. The stronger 74-point statement holds only for specified subclasses.

These manuscripts remain **same-session / unreviewed / unaccepted**, without completed Lean. Restricted capacity b25 has its own historical SAT acceptance. The separately checked abstract lower25 witness and 10/11-point strategy counterexamples do not verify the upper-bound chain or geometric realizability.

[Case and manuscripts](happy-ending/README.md) · [Reading guide and exact scope](happy-ending/n7-20261103/proofs/READING_GUIDE.md) · [Plugin](../plugins/happy-ending/README.md) · [v4 actual use](../development/evolution/v4-20261108/HAPPY_ENDING.md)

## Research provenance and workflow feedback

Property B was researched with ARIS and distilled into MathRSI. ECC continued using methods inherited through v1/v2 and deepened its formal reductions, matrix connections and portable evidence. Earlier DD work informed v2; the later 2,567 graph actually used that version. Erdős 86, Q6 and older Happy Ending evidence informed v3; the later Happy Ending manuscripts and DD methods informed v4. Incorporation retains those histories; it does not attribute every result to a run of the receiving release.

[Version and maintenance records](../development/README.md) preserve the actual changes and bounded uses. No equal-budget speedup or long-task success-rate claim is established by these presentation pages. New research uses its own [task workspace](../docs/WORKSPACE.md); archived Goals stay historical.
