# Six mathematical research threads

[English entry](../README.md) · [中文入口](../README.zh-CN.md) · [Bilingual visual tour](../docs/HOMEPAGE.md) · [Domain routing](../docs/DOMAIN_ROUTING.md)

This page indexes all six research threads, summarizing what has been established and linking to each case's proofs, verification checks and runnable tools. Local HTML readers can be opened directly in a browser after cloning.

## Property B

**Hypergraph two-coloring:** concrete lower bounds for $m(5),\ldots,m(12)$ reach $35,67,131,267,543,1112,2275,4664$, and a uniform theorem gives a stronger explicit lower bound with an exponentially growing additive gain over the Radhakrishnan–Srinivasan baseline for every $k\ge12$.

The uniform $k\ge12$ theorem and $m(5)\ge33,34$ have end-to-end Lean proofs; $m(5)\ge35$ has a complete written proof with Lean formalization still in progress. The bounds for $k=6,\ldots,12$ rest on parameter-specific computer-assisted proofs; for $k=12$, an independent check covers the full parameter and trace domain and verifies 20 exact probability values.

[Case and per-parameter status](property-b/README.md) · [Offline reader](property-b/index.html) · [General theorem](property-b/readers/PROPERTY_B_GENERAL_BOUND.html) · [Lean reader](property-b/readers/PROPERTY_B_GENERAL_LEAN.html) · [Domain skill](../plugins/propertyb/skills/mathrsi-propertyb/SKILL.md)

## Error-correcting codes

**Four exact binary-code distances:** $d_2(43,10)=16$, $d_2(44,10)=17$, $d_2(44,11)=16$ and $d_2(42,16)=12$. The first three combine a complete 172-parent exclusion with matching constructions; $d_2(42,16)=12$ follows from a published 2020 theorem. The remaining case narrows to $16\le d_2(45,11)\le17$.

**Historical context.** Verhoeff's *Updating a table of bounds on the minimum distance of binary linear codes* (1985), [Appendix I, block (1,0), PDF p.45](https://pure.tue.nl/ws/portalfiles/portal/2264214/253220.pdf#page=45), listed $(43,10)$ at 16–17, $(44,10)$ at **16–18**, $(44,11)$ at 16–17 and $(45,11)$ at 16–18. Our exclusion settles the first three at 16, 17 and 16 and narrows $(45,11)$ to 16–17; see also CodeTables (checked 2026-11-12) for [43/10](https://www.codetables.de/BKLC/BKLC.php?q=2&n=43&k=10), [44/10](https://www.codetables.de/BKLC/BKLC.php?q=2&n=44&k=10), [44/11](https://www.codetables.de/BKLC/BKLC.php?q=2&n=44&k=11) and [45/11](https://www.codetables.de/BKLC/BKLC.php?q=2&n=45&k=11).

Lean reductions state their explicit literature, classification and computation premises, while reusable checkers cover concrete generator matrices and parent-code pair rejections. The plugin also includes a branch-organization walkthrough on the open $[72,36,\ge16]$ problem.

[Plugin and methods](../plugins/ecc/README.md) · [Actual checks and import boundaries](../plugins/ecc/evidence/IMPLEMENTATION.md) · [Node organization example](../plugins/ecc/skills/mathrsi-ecc/examples/node-research.md)

## Degree–Diameter

Our constructions reach **(10,4)=2,567**, **(11,5)=37,632**, **(12,5)=42,433** and **(16,4)=16,416** vertices. The 2026-11-16 diameter-five follow-up improves our (11,5) and (12,5) constructions by +1 and +31 (+1 and +81 above the Comellas table checked 2026-11-16).

Constructed on the 2026-11-11 v4-maintenance workflow with local degree–diameter updates (whose methods later informed v5 main maintenance), both D5 graphs regenerate deterministically: D12 preserves the 42,402-vertex source subgraph and runs breadth-first search from all 31 new vertices, while D11 takes core–core distances from the H9 theorem under its stated $\sigma/\pi$ identification and runs breadth-first search from all 161 peripheral and new vertices. End-to-end Lean proofs and independent refereeing for these D5 graphs remain open.

On the Comellas table checked 2026-11-16, (10,4) is 2,612 and (16,4) is 16,848, above our earlier constructions of 2,567 and 16,416. The 163-graph catalogue (across 44 parameter pairs, including intermediate orders and 49 completed concrete-graph Lean proofs) is the earlier snapshot from the (10,4) stage.

[Latest case and scope](degree-diameter/README.md) · [中文](degree-diameter/README.zh-CN.md) · [Bilingual latest reader](../development/homepage-redesign-20261105/site/dd-latest.html) · [Historical illustrated case](degree-diameter/index.html) · [Earlier v2 execution provenance](degree-diameter/evidence/execution_version.md) · [Plugin](../plugins/degree-diameter/README.md)

## Erdős Problem 86

**Finite and asymptotic $C_4$-free hypercube bounds:**
- **$Q_7$ ($n = 7$):** **`304`** — **304-edge construction verified; 304 upper bound as reported in the source package, not re-verified in this pass** (two explicit 304-edge $C_4$-free subgraphs checked in-repo; 21 raw `.cnf`/`.drup` traces were omitted in the upstream 2026-10-31 compilation).
- **$Q_8$ ($n = 8$):** **`682 ≤ ex(Q₈, C₄) ≤ 683`** — four 682-edge constructions verified in-repo; Theorem B rules out 684 edges via a same-subgraph 3-measure pullback over 83 active cuts and 25 imported $Q_6$ DRAT certificates (checked computationally and reviewed in the same model family; independent refereeing is pending, and $\mathrm{ex}(Q_8, C_4) \le 682$ remains open).
- **$Q_\infty$ (asymptotic):** **T3** $\le 681653995482306581 / 1152921504606846976 \le 0.5912405943$ and **T4** $\le 9701859764505653085708308080340303 / 16409326186106551516455239680000000 \le 0.5912405942$ ($m=1024$ degree potential via a 5-line hypergeometric tower), both proved and rechecked in 128-bit C++20, improving the v3 $Q_4$ bound ($< 0.59155154$) and the `0.60318` reference. Exploratory `0.5907` is an approximate fit (residual $\approx 3.9\times 10^{-4}$), an earlier `0.5899` claim was refuted and withdrawn, and $\pi_\square(C_4) = 1/2$ remains open.

[Per-setting case study & verification table](erdos-86/README.md) · [Bilingual public reader](../development/homepage-redesign-20261105/site/erdos-86-latest.html) · [Plugin and source map](../plugins/hypercube-extremal/README.md) · [Domain skill](../plugins/hypercube-extremal/skills/mathrsi-hypercube-extremal/SKILL.md)

## Ruskey–Savage Q6

**Every matching in $Q_6$ extends to a Hamilton cycle.** Combined with published results, this also extends every matching in $Q_n$ that uses at most six coordinate directions. The stronger stored $P_6$ statement covers a Hamilton path from every free root to every opposite-parity target.

The checked A10 replay rebuilds 1,024 forests, all 1,048,576 connectivity bits and rank 1,024, while the larger $P_6$ certificate streams are listed in inventory manifests rather than replayed here. The proof was reviewed in the same model family; independent refereeing is pending, there is no Lean formalization, and the general dimension-$n$ conjecture remains open.

[Plugin and mathematics](../plugins/hypercube-hamilton/README.md) · [Finite replay and whole-proof boundary](../plugins/hypercube-hamilton/evidence/IMPLEMENTATION.md) · [Domain skill](../plugins/hypercube-hamilton/skills/mathrsi-hypercube-hamilton/SKILL.md)

### Q7: dense matchings and complete E16 closure

**Every matching with at least 56 edges (at most 16 holes) in the 128-vertex $Q_7$ extends to a Hamilton cycle containing all prescribed edges.** Complete E16 closes adjacent-hole augmentation and all five 16-hole parity classes $\mu \in \{0,1,2,3,4\}$ by a computational argument reviewed in the same model family and depending on the listed baseline imports (independent refereeing pending, no Lean). Matchings with at most 55 edges (even hole layers 18–38), full $Q_7$, free-root paths $P_7$ and seven-direction lifting remain open.

This research ran on **MathRSI v3 (with local adaptations)** and hardest-branch split probes, with its methods feeding `v5` and `v6`.

[Q7 results, methods and evidence scope](ruskey-savage-q7/README.md) · [Bilingual public reader](../development/homepage-redesign-20261105/site/q7.html) · [v6 changes](../docs/V6_CHANGES.md)

## Happy Ending

**Ordered rank-3 signotope capacities $N(m,r,s)$ and planar forcing corollaries ($m = 7, 8, 9$ & general $m$):**
- **$m = 7$ (heptagons):** Working manuscripts tighten $N(7,5,7)\le 39$ (owner intervals) and $N(7,6,6)\le 49$ (strict balanced capacity $2b-1$), and give $N(7,6,7)\le 75, N(7,7,7)\le 76 \implies$ working planar corollary **$\mathrm{ES}(7)\le 77$** (vs. Schroeder 2026 v1 planar $\le 81$), built on the accepted restricted capacity $N(7,5,6)=25$ (with a checked 25-point E21 abstract witness and DRAT-verified $\le 4$ common lock blocks).
- **$m = 8$ (octagons):** Replayed shared-label CNF+DRAT certificate (`milestone9`, 115 rows) proves **$N(8,6,6)\le 61$** (9-hole hitting vector proves exact matrix minimum 9, not a 61-point signotope). Replaying Schroeder's 15-file omission trees (`193` / `124`) together with our signotope cyclic-sign packet bridge gives working signotope bounds $C_8\le 193, D_8\le 124 \implies N(8,8,8)\le 318$ (planar $\mathrm{ES}(8)\le 319$ is Schroeder's published preprint bound; autonomous fallback without public trees gives $N(8,8,8)\le 322, \mathrm{ES}(8)\le 323$).
- **$m = 9$ (nonagons) & general $m$:** Replayed native boundary-trace integer dual certificates (`check_native_trace_cert.py`, $\Lambda=10^6$, zero float) establish **$N(9,8,8)\le 688$** ($\ge 236$ holes) and junction-restricted **$D_9\le 458$** ($\ge 124$ holes, matching the `47,635`-row depth-$\le 3$ LP ceiling). Assembled via R7 and R20, these give working bounds **$N(9,8,9)\le 1146, N(9,9,9)\le 1147 \implies \mathrm{ES}(9)\le 1148$** (vs. Mojarrad–Vlachos 2016 printed **$1508$** and combined planar reference **$1501^*$**). General-$m$ slice double counting gives $2b-1$ balanced capacity and quadratic/cubic deficits. Independent mathematical review of the structural, transfer, and R7/R20 assembly manuscripts is pending, and there is no Lean formalization.

[Case summary & verification table](happy-ending/README.md) · [Bilingual public reader](../development/homepage-redesign-20261105/site/happy-ending-latest.html) · [Earlier `m = 7` reader](happy-ending/n7-20261103/START_HERE.html) · [Plugin & runnable checkers](../plugins/happy-ending/README.md)

## Research lineage and workflow feedback

Property B was researched with standalone ARIS tools and distilled into MathRSI v1. ECC continued using methods inherited through v1/v2 and deepened its formal reductions, matrix checks and portable certificates. Earlier Degree–Diameter work informed v2, which was then used to construct the 2,567-vertex $(10,4)$ graph. Erdős 86 ($Q_4$), $Q_6$ and earlier Happy Ending work informed v3; the later Happy Ending `m = 7` manuscripts and DD local-edit methods informed v4. Dense-matching $Q_7$ work ($\ge 57$ edges) on v3 fed v5, while subsequent $C_4$-free $Q_7/Q_8/Q_\infty$ coevolution, complete $Q_7$ E16 ($\ge 56$ edges), and the `m = 7, 8, 9` $N(m,r,s)$ runs (Trellis + ARIS + v3) fed v6 and its `main` maintenance.

[Version and maintenance records](../development/README.md) document each release's changes and verification checks. New studies run in their own [task workspace](../docs/WORKSPACE.md).
