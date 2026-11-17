# Literature assessment for the ES7–ES8 manuscript

Michael Schroeder · 18 September 2026

## Scope and conclusion

This review concerns ordinary convex polygons in finite real planar sets with no three collinear. It separates forcing thresholds ES(n), avoiding maxima, empty polygons, arbitrary ordered triple colorings, and restricted geometric classes. The manuscript's numerical claims are ES(7) ≤ 81 and ES(8) ≤ 319. Their evidence is the accompanying formal development, not this literature review.

Primary arXiv texts, author/institutional copies, and publisher records were searched and inspected through 18 September 2026. Searches combined the problem name with “heptagon”, “octagon”, “upper bound”, “2025”, “2026”, “81”, “319”, and the names of the principal authors; references were followed backward from the recent papers. Searching only ES(7)/ES(8) returned many unrelated results, so those searches were supplemented by names and full titles. The review also revisits the project's 15 September machinery assessment. Full-text theorem inspection is distinguished below from abstract/metadata inspection. No search establishes exhaustive priority, and external computational artifacts were not all replayed.

**Comparison supported by an explicit finite theorem:** Nassajian Mojarrad–Vlachos gives 113 and 408. The new endpoints reduce these by 32 and 89. A 2026 historical table lists 92 and 324 under an asymptotic Norin–Yuditsky expression. The cited paper does not furnish that finite derivation. Our endpoints are also smaller than those entries, by 11 and 5. We found no smaller proved unrestricted upper bounds in the sources reviewed, but do not claim that an exhaustive priority determination has been completed.

## 1. Foundations and explicit finite bounds

**Erdős–Szekeres (1935).** *A combinatorial problem in geometry*, Compositio Mathematica 2, 463–470. The original upper bound and cup–cap theorem supply the starting framework. The monotone subsequence theorem in the same paper is a different result and must not be confused with the convex-polygon conjecture. Primary scan and bibliographic record inspected: [Numdam](https://numdam.org/item/CM_1935__2__463_0/).

**Erdős–Szekeres (1960–1961).** *On some extremum problems in elementary geometry*, Ann. Univ. Sci. Budapest. Eötvös Sect. Math. 3–4, 53–62. The classical construction gives 2^(n−2) points avoiding a convex n-gon, hence the lower forcing thresholds 33 and 65. These lower bounds are cited, not newly formalized by this package. Primary [Rényi scan](https://renyi.hu/~p_erdos/1960-09.pdf) inspected. Catalogues vary between 1960 and 1961; the manuscript retains the volume's 1960–1961 convention.

**Tóth–Valtr (1998, 2005).** *Note on the Erdős–Szekeres theorem*, DCG 19, 457–459, gives binomial(2n−5,n−2)+2; the 2005 chapter improves the additive constant to +1. The projective reduction is the ingredient actually used here. A restricted avoiding maximum Q converts to an unrestricted threshold Q+2: deleting a root accounts for one point, and passing from a maximum to a forcing threshold accounts for the other. [1998 publisher](https://doi.org/10.1007/PL00009363); [2005 primary chapter](https://library.slmath.org/books/Book52/files/30toth.pdf), pp. 557–568. A 2025 online reissue date is not a new result.

**Nassajian Mojarrad–Vlachos (2016).** *An improved upper bound for the Erdős–Szekeres conjecture*, DCG 56, 165–180. Theorem 1.1 gives, for n≥6,

ES(n) ≤ binomial(2n−5,n−2) − binomial(2n−8,n−3) + 2.

Substitution gives 126−15+2=113 and 462−56+2=408. Theorem 4.3 states the projective transfer using a restricted forcing threshold. This is the manuscript's verified explicit finite comparator. [arXiv v2](https://arxiv.org/pdf/1510.06255); [publisher DOI](https://doi.org/10.1007/s00454-016-9791-5). Full statement and transfer inspected.

**Norin–Yuditsky (2016).** *Erdős–Szekeres without induction*, DCG 55, 963–971. Theorem 1.1 is a limsup bound with factor 7/8. Claim 3.3 identifies the exceptional coincidence between the second cap point and the terminal cup point; our partition discharges it using membership in disjoint parts. Claim 3.4 bounds a deletion set by |P|/(n−2); the subsequent argument neglects it only asymptotically. This paper is an important structural source, but does not justify substituting n=7 or 8 into an asymptotic expression while omitting finite terms. [Primary full text](https://arxiv.org/pdf/1509.03332).

## 2. What asymptotic and restricted results provide

**Suk (2017).** *On the Erdős–Szekeres convex polygon problem*, JAMS 30, 1047–1053, proves 2^(n+O(n^(2/3) log n)). This changes the asymptotic scale of the problem. The displayed big-O expression alone is not an explicit small-n competitor. [Primary paper](https://arxiv.org/pdf/1604.08657), main theorem inspected.

**Holmsen–Nassajian Mojarrad–Pach–Tardos (2020).** *Two extensions of the Erdős–Szekeres problem*, JEMS 22, 3981–3995. Theorem 1.3 improves the error term to O(sqrt(n log n)) and applies to pseudo-configurations; ordinary planar sets are included. Its extensions to convex bodies concern still other categories. The manuscript recognizes this stronger asymptotic result without asserting unsupported finite constants. [Primary v3](https://arxiv.org/pdf/1710.11415), Theorems 1.1–1.3 and Remark 1.4 inspected.

**Moshkovitz–Shapira (2014).** *Ramsey theory, integer partitions and a new proof of the Erdős–Szekeres theorem*, Advances in Mathematics 262, 1107–1129. Monotone-path ranks, partitions, and iterated down-sets have established precedent. The present paper does not claim to originate that encoding. Its contribution lies in the particular geometric restrictions and certified exclusions added to it. [arXiv](https://arxiv.org/abs/1206.4001); [author text](https://www.math.tau.ac.il/~asafico/erdos-szekeres.pdf). Abstract and established encoding attribution checked; the higher-uniformity theory is not used as a premise.

**Baek (2025; arXiv v2, 2022).** *On the Erdős–Tuza–Valtr conjecture*, EJC 124, 104085. Theorem 1.6 forces a four-cap or convex n-gon from binomial(n−1,2)+2 points. At n=8 this gives capacity 22; at n=7 capacity 16. Theorem 2.7 supplies the combinatorial form, while Section 3 explains slope labels and restriction. This is an actual input, with Baek's own formalization ported and attributed. The stronger many-laced-cup conjecture is not assumed. [Full text](https://arxiv.org/html/2206.04260v2); [code](https://github.com/jcpaik/erdos-tuza-valtr). The retained port is pinned to commit a5ad53efefb36f8654b9227ce4dba2bf04a7ec3f.

**Baek–Balko (SoCG 2025; JCTA 222, 2026, 106195).** *The Erdős–Szekeres conjecture revisited* proves the conjectured threshold for split polygons and treats decomposable sets. The analogous unrestricted-coloring conjecture can fail. A split polygon allows unmatched left endpoints; decomposability is not automatic for arbitrary planar sets. These results sharpen the need for shared endpoint and geometric compatibility, but do not settle ES(7) or ES(8). [Conference full text](https://drops.dagstuhl.de/storage/00lipics/lipics-vol332-socg2025/LIPIcs.SoCG.2025.13/LIPIcs.SoCG.2025.13.pdf); [2026 publisher record](https://www.sciencedirect.com/science/article/pii/S0097316526000385). Conference text and journal abstract/metadata inspected; the full journal text was not accessible through the browsing tool.

## 3. Computational and formal precedents

**Szekeres–Peters (2006).** *Computer solution to the 17-point Erdős–Szekeres problem*, ANZIAM Journal 48, 151–164, establishes ES(6)=17. It is the relevant computational predecessor for ordinary convex polygons. [Primary journal archive](https://archive.austms.org.au/Publ/Jamsb/V48P2/2409.html); DOI 10.1017/S144618110000300X. Abstract and primary paper inspected for scope; the original exhaustive computation was not rerun.

**Balko–Valtr (2017).** *A SAT attack on the Erdős–Szekeres conjecture*, EJC 66, 13–23, uses SAT to refute an ordered-hypergraph strengthening. Such an abstract counterexample is not automatically a real planar counterexample. This reinforces the category distinction maintained by our final statements. [Institutional publication record](https://cris.bgu.ac.il/en/publications/a-sat-attack-on-the-erd%C5%91sszekeres-conjecture-2/), DOI 10.1016/j.ejc.2017.06.010. Abstract/metadata inspected; no external certificate replay claimed.

**Marić (2019; online 2017).** *Fast formal proof of the Erdős–Szekeres conjecture for convex polygons with at most 6 points*, JAR 62, 301–329. The paper uses Isabelle/HOL and SAT, providing direct precedent for formal geometric encoding and computational exclusion. [Publisher abstract and metadata](https://doi.org/10.1007/s10817-017-9423-7) inspected. We do not claim to be the first formalization of an Erdős–Szekeres result.

**Subercaseaux–Nawrocki–Gallicchio–Codel–Carneiro–Heule (2024).** *Formal verification of the empty hexagon number*, ITP 2024, LIPIcs 309, 35:1–35:19. The Lean development connects planar geometry to propositional encodings and verifies the empty-hexagon result. It concerns empty polygons; our polygons may contain other ambient points. [Conference paper](https://doi.org/10.4230/LIPIcs.ITP.2024.35); [arXiv](https://arxiv.org/abs/2403.17370). Its conceptual separation of source semantics and refutation is cited; no code from that project is represented as our original work.

**Dumitru (December 2025 v1).** *Notes on the 33-point Erdős–Szekeres problem* reports anchored-family UNSAT results and substantial runtime variation. Section 5.2 says the anchoring restrictions are not an exhaustive splitting strategy. Accordingly, these cases do not imply ES(7)=33 or discharge our complete case cover. [Full text](https://arxiv.org/html/2512.24061v1). No later revision was present in the inspected arXiv record.

**Damásdi–Dong–Scheucher–Zeng (2026).** *Saturation results around the Erdős–Szekeres problem*, EJC 131, 104236, constructs n-gon-saturated sets of size (7/8)2^(n−2) for n≥7. Thus a 28-point set may resist every one-point extension while larger heptagon-free sets exist. This is a useful warning for discovery, not an upper-bound input. [Full v3](https://arxiv.org/html/2312.01223v3); [publisher record](https://www.sciencedirect.com/science/article/abs/pii/S0195669825001258).

**Koshelev–Koshka (April 2026 v1).** *Combinatorial geometry of Erdős–Szekeres type problems: SAT/ASP modeling and linear subreduction* concerns several colored/empty-polygon variants. Section 5.2's fixed-abscissa linearization is valuable for finding realizations but may lose realizable order types. An unsuccessful fixed-grid search is not a global exclusion. Table 1's finite 92/324 entries remain attribution questions, not adopted dependencies. [Full text](https://arxiv.org/html/2604.20120v1), table and modeling discussion inspected. The archive does not redistribute this preprint or claim to have checked its external computations.

## 4. Novelty boundary and decisions for this manuscript

The project does not claim new cup–cap theory, the projective reduction, the down-set encoding, Baek's four-cap theorem, the general idea of a SAT-assisted proof, or formalization of computational geometry. It claims the concrete restrictions and fully connected exclusions proving the two new endpoints, with exact source-level evidence.

The heptagon contribution is the combination of the restricted-25 exclusion, the residual five-point transversal, and a complete balanced-fifty exclusion. The octagon contribution is the particular hereditary state capacities, threshold block maps, two-sided residual state restriction, and two complete weighted omission trees. Formalization supplies full planar statements, verifies shared actual witnesses, and replaces a historical mixed-family proof dependency by direct cyclic certification.

The main paper includes only machinery used in the proofs or needed to situate them. Earlier investigations of Hall matching, common chronology, final polynomials, finite rooted moments, tableaux, and pseudo-Boolean optimization remain research directions. They are not silently promoted to premises or new numerical results. The inherited 15 September review is preserved separately as `BACKGROUND_MACHINERY_2026_09_15.md`, explicitly dated; not every linked auxiliary paper was re-read in this release pass.

A future referee review should examine mathematical novelty and the statement-to-encoding correspondence in addition to replaying certificates. The public version should retain the native-evaluation trust disclosure. Nothing in this assessment establishes external peer review, resolves the disputed table attribution, or constitutes an arXiv/Zenodo publication.


## Verification of feedback

The sharp ETV (7,5,6) interpretation, fitted finite table formula and its 5/8 limiting ratio, and publisher metadata for Baek–Balko and Damásdi et al. were checked in revision 1.1. The arXiv abstract for 2512.24061 lists Bogdan Dumitru, consistent with the citation. The upper bound is the existing project certificate; the exact 25-point example independently verifies the lower bound. No broader signotope theorem or exhaustive priority claim is adopted.

## Original attribution and precise scope

The manuscript now cites **P. Erdős, Z. Tuza and P. Valtr, Ramsey-remainder, European Journal of Combinatorics 17(6) (1996), 519–532**, [original DOI](https://doi.org/10.1006/eujc.1996.0045). The [publisher record](https://www.sciencedirect.com/science/article/pii/S0195669896900451) and [Valtr's publication list](https://kam.mff.cuni.cz/~valtr/publications-sdiplomkami.html) establish its bibliographic identity. The original full proof was not newly inspected in this revision; the accessible Baek and Baek–Balko papers supply the explicit attribution and restricted sum.

The [Baek–Balko conference text](https://drops.dagstuhl.de/storage/00lipics/lipics-vol332-socg2025/LIPIcs.SoCG.2025.13/LIPIcs.SoCG.2025.13.pdf), §2.1, states the known ETV ranges n≥a+b−3 or a=4 or b=4. Its §4 discusses the Erdős–Szekeres construction and ETV refinement; the proof of its split-polygon lower-bound Lemma 12 is explicitly omitted. The paper therefore attributes the original lower construction to Erdős–Szekeres and ETV, retaining the journal version of Baek–Balko as the main bibliographic entry. The publisher's [journal record](https://www.sciencedirect.com/science/article/pii/S0097316526000385) confirms JCTA 222 (2026), 106195; its full text was not accessible in this run. Section-specific claims in the audit are based on the accessible conference version.

Baek–Balko §3 distinguishes arbitrary ordered colorings from signotopes and records the latter's connection to Goodman–Pollack. Our complete theorem's extension to that category has not been audited. The conditional table follows the ETV sum directly: C7=30 and C8=62, while D7≤26 and D8≤57 use only inclusion in M_n(n−2,n). The checked 26-point residual lower example now makes D7=26 conditional on ETV; no equality is asserted for D8.

The general residual baseline in the revision is derived in the manuscript for n≥6; its sum with the balanced cup–cap count is identically the published Mojarrad–Vlachos formula. It is presented as an alternative derivation, not a stronger general numerical theorem. The paper's former long discussion of the disputed 92/324 table is reduced to a footnote, with the comparison calculations retained here and in the exact checker.

## Targeted feedback verification — 19 September 2026

The [Baek–Balko conference text](https://drops.dagstuhl.de/storage/00lipics/lipics-vol332-socg2025/LIPIcs.SoCG.2025.13/LIPIcs.SoCG.2025.13.pdf), §2.3, distinguishes weak polygons from strong polygons by allowing the two monotone paths to share interior vertices. It attributes C_strong(7)>33 to Balko–Valtr and proves C_weak(7)>33 in Theorem 7. The [Balko–Valtr author project page](https://kam.mff.cuni.cz/~balko/ES_SAT/) also identifies the 33-vertex abstract counterexample. These statements concern arbitrary ordered triple colorings, not planar counterexamples or the signotope conjecture.

The classical restricted lower constructions give C7≥30, C8≥62, and M8(6,6)≥50. The last class has no six-cup and hence no residual junction, giving D8≥50. The weaker D7≥M7(5,5)=20 observation is correct, but the project's exact planar residual control gives D7≥26. Its coordinates and a complete independent check are now included in the release. Thus the unconditional floors of the separately optimized additive method are 58 and 114. ETV would make the heptagon value exactly 58 and put the octagon value in [114,121]. The interval's upper endpoint is conditional; these are not intervals or new lower bounds for ES(7) and ES(8).

The original Ramsey-remainder proof has not been newly replayed or formalized here. The lower constructions are cited separately from the new project upper-bound proofs; the residual 26-point claim additionally has a complete exact coordinate check. The 19 September pass is a targeted source check, not a claim that the entire earlier literature search was repeated.
