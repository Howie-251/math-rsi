# Six mathematical research threads

[English entry](../README.md) · [中文入口](../README.zh-CN.md) · [Bilingual visual tour](../docs/HOMEPAGE.md) · [Domain routing](../docs/DOMAIN_ROUTING.md)

This is the shared index for all six results. Existing case pages and plugin records own the detailed proofs, current evidence scopes and reproduction commands. HTML readers work locally after cloning; GitHub shows their source.

## Property B

**Hypergraph two-coloring:** individual reported lower bounds for $m(5),\ldots,m(12)$ are $35,67,131,267,543,1112,2275,4664$. A uniform theorem improves the specified exact RS budget for every $k\ge12$.

The uniform theorem and earlier $m(5)\ge33,34$ have end-to-end Lean proofs. The bound 35 has a complete written candidate with unfinished Lean. The other individual bounds retain parameter-specific paper/computational evidence; the k=12 independent checks cover the whole parameter/trace domain plus 20 exact probability checks, rather than a second full probability implementation.

[Case and per-parameter status](property-b/README.md) · [Offline reader](property-b/index.html) · [General theorem](property-b/readers/PROPERTY_B_GENERAL_BOUND.html) · [Lean reader](property-b/readers/PROPERTY_B_GENERAL_LEAN.html) · [Domain skill](../plugins/propertyb/skills/mathrsi-propertyb/SKILL.md)

## Error-correcting codes

**Four exact binary-code distances:** $d_2(43,10)=16$, $d_2(44,10)=17$, $d_2(44,11)=16$ and $d_2(42,16)=12$. The first three follow from the old 172-parent exclusion and constructions; 42/16 applies a published 2020 theorem. The remaining range is $16\le d_2(45,11)\le17$.

**Historical source.** Verhoeff's *Updating a table of bounds on the minimum distance of binary linear codes* (1985), [Appendix I, block (1,0), PDF p.45](https://pure.tue.nl/ws/portalfiles/portal/2264214/253220.pdf#page=45), records $(43,10)$ at 16–17, $(44,10)$ at **16–18**, $(44,11)$ at 16–17 and $(45,11)$ at 16–18. The main proof closes the first three at 16, 17 and 16; the last narrows to 16–17. For public-table comparisons checked on 2026-11-12, see CodeTables [43/10](https://www.codetables.de/BKLC/BKLC.php?q=2&n=43&k=10), [44/10](https://www.codetables.de/BKLC/BKLC.php?q=2&n=44&k=10), [44/11](https://www.codetables.de/BKLC/BKLC.php?q=2&n=44&k=11) and [45/11](https://www.codetables.de/BKLC/BKLC.php?q=2&n=45&k=11). The fourth exact value, $d_2(42,16)=12$, remains the separate 2020-literature corollary.

Lean reductions retain explicit literature, classification and computation premises. Actual-matrix checking, one-parent replay and the whole-domain exclusion have different scopes. The recent $[72,36,\ge16]$ A/B/C node example teaches research organization; it is not an additional solved parameter.

[Plugin and methods](../plugins/ecc/README.md) · [Actual checks and import boundaries](../plugins/ecc/evidence/IMPLEMENTATION.md) · [Node organization example](../plugins/ecc/skills/mathrsi-ecc/examples/node-research.md)

## Degree–Diameter

Our constructions retain four highlighted settings: **(10,4)=2,567**, **(11,5)=37,632**, **(12,5)=42,433** and **(16,4)=16,416** vertices. The latest D5 follow-up improves only the (11,5) and (12,5) rows, by +1/+31 over previous local constructions and +1/+81 over the Comellas entries checked 2026-11-16. The four values are our constructions, not a claim of current global records.

The D5 follow-up ran with local 2026-11-11 main/v4-maintenance plus DD feedback updates and feeds **v5 main maintenance**. Both D5 finals regenerate exactly. D12 retains the source and checks all 31 new roots; D11 uses the H9 theorem plus literal core binding and checks all 161 peripheral/new roots. Concrete end-to-end Lean instances and required source final-review obligations remain open.

Earlier (10,4)=2,567 and (16,4)=16,416 remain dated historical highlights; the current table checked 2026-11-16 lists 2,612 and 16,848. The earlier catalogue's 163 graphs / 44 parameter pairs / 49 concrete Lean instances are historical counts, not updated totals or additional certifications for the new endpoints.

[Latest case and scope](degree-diameter/README.md) · [中文](degree-diameter/README.zh-CN.md) · [Bilingual latest reader](../development/homepage-redesign-20261105/site/dd-latest.html) · [Historical illustrated case](degree-diameter/index.html) · [Earlier v2 execution provenance](degree-diameter/evidence/execution_version.md) · [Plugin](../plugins/degree-diameter/README.md)

## Erdős Problem 86

**Finite and asymptotic $C_4$-free hypercube bounds:**
- **$Q_7$ ($n = 7$):** **`304`** — **304-edge construction verified; 304 upper bound as reported in the source package, not re-verified in this pass** (two explicit 304-edge $C_4$-free constructions verified in-repo; 21 raw `.cnf`/`.drup` traces were already omitted in the upstream 2026-10-31 compilation).
- **$Q_8$ ($n = 8$):** **`682 ≤ ex(Q₈, C₄) ≤ 683`** — four explicit 682-edge seeds verified in-repo; Theorem B rules out 684 edges via a same-subgraph 3-measure pullback over 83 active inequalities and 25 $Q_6$ subcube imports (`PASS · same-family · provisional`; $\mathrm{ex}(Q_8, C_4) \le 682$ remains open).
- **$Q_\infty$ (asymptotic):** unconditional **T3** $\le 681653995482306581 / 1152921504606846976 \le 0.5912405943$ and **T4** $\le 9701859764505653085708308080340303 / 16409326186106551516455239680000000 \le 0.5912405942$ ($m=1024$ generalized degree potential via a 5-line hypergeometric tower), improving the `v3` $Q_4$ certificate ($< 0.59155154$) and the `0.60318` reference; `0.5907` and retracted `0.5899` are non-theorems, and $\pi_\square(C_4) = 1/2$ remains open.

[Per-setting case study & verification table](erdos-86/README.md) · [Bilingual public reader](../development/homepage-redesign-20261105/site/erdos-86-latest.html) · [Plugin and source map](../plugins/hypercube-extremal/README.md) · [Domain skill](../plugins/hypercube-extremal/skills/mathrsi-hypercube-extremal/SKILL.md)

## Ruskey–Savage Q6

**Every matching in $Q_6$ extends to a Hamilton cycle.** With explicit imported results, this also yields extension for matchings using at most six directions in any dimension. The stronger stored P6 statement concerns a Hamilton path from every free root to every opposite-parity target.

The whole-proof audit remains **same-family/provisional**, with no Lean. The bounded A10 replay reconstructs 1,024 forests, all 1,048,576 connectivity bits and rank 1,024. It does not replay all large P6 certificate streams; inventories identify omitted material. The general conjecture remains open.

[Plugin and mathematics](../plugins/hypercube-hamilton/README.md) · [Finite replay and whole-proof boundary](../plugins/hypercube-hamilton/evidence/IMPLEMENTATION.md) · [Domain skill](../plugins/hypercube-hamilton/skills/mathrsi-hypercube-hamilton/SKILL.md)

### Q7: dense matchings and complete E16 closure

**Every matching with at least 56 edges (at most 16 holes) in the 128-vertex Q7 extends to a Hamilton cycle containing all prescribed edges.** Complete E16 closes adjacent-hole augmentation plus all five independent 16-hole parity-gap classes $\mu \in \{0,1,2,3,4\}$ (`PASS · same-family · provisional · sound-modulo-imports`). Even hole layers 18–38 ($\le 55$ edges), full Q7, free-root paths $P_7$ and seven-direction lifting remain open.

The research ran with **MathRSI v3 (local adaptation)** plus hardest-remainder E16 gating; its methods feed `v5` and `v6`.

[Q7 results, methods and evidence scope](ruskey-savage-q7/README.md) · [Bilingual public reader](../development/homepage-redesign-20261105/site/q7.html) · [v6 changes](../docs/V6_CHANGES.md)

## Happy Ending

**Working manuscripts; independent review pending.** Received structural manuscripts claim $N(7,6,7)\le75$ and $N(7,7,7)\le76$, hence the geometric threshold $\mathrm{ES}(7)\le77$, improving the prior 76/77/78 chain. The stronger 74-point statement holds only for specified subclasses.

These manuscripts remain **same-session / unreviewed / unaccepted**, without completed Lean. Restricted capacity b25 has its own historical SAT acceptance. The separately checked abstract lower25 witness and 10/11-point strategy counterexamples do not verify the upper-bound chain or geometric realizability.

[Case and manuscripts](happy-ending/README.md) · [Reading guide and exact scope](happy-ending/n7-20261103/proofs/READING_GUIDE.md) · [Plugin](../plugins/happy-ending/README.md) · [v4 actual use](../development/evolution/v4-20261108/HAPPY_ENDING.md)

## Research provenance and workflow feedback

Property B was researched with ARIS and distilled into MathRSI. ECC continued using methods inherited through v1/v2 and deepened its formal reductions, matrix connections and portable evidence. Earlier DD work informed v2; the later 2,567 graph actually used that version. Erdős 86, Q6 and older Happy Ending evidence informed v3; the later Happy Ending manuscripts and DD methods informed v4. Q7 dense-matching research used v3 with local adaptations and fed v5, while subsequent $C_4$-free $Q_7/Q_8/Q_\infty$ coevolution and complete $Q_7$ E16 closure feed v6. Incorporation retains those histories; it does not attribute every result to a run of the receiving release.

[Version and maintenance records](../development/README.md) preserve the actual changes and bounded uses. No equal-budget speedup or long-task success-rate claim is established by these presentation pages. New research uses its own [task workspace](../docs/WORKSPACE.md); archived Goals stay historical.
