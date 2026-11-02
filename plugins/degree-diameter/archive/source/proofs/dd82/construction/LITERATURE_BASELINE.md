# Literature and construction baseline, checked 2026-10-11

ARIS skills used: project `research-lit` and `proof-writer`. Local `papers/` and `literature/` contained no PDFs at the start of this task. The ARIS `arxiv_fetch.py` search for degree/diameter and defect completed successfully; general web retrieval and full original documents supplied the useful sources. Optional reference-manager sources were not configured/requested. No Gemini CLI was introduced.

| Source | Publication | Checked contribution | Evidence and remaining scope |
|---|---|---|---|
| J. Širáň, J. Šiagiová, M. Ždímalová, *Large graphs of diameter two and given degree* | IWONT 2010 proceedings, UPC 2011, 347–359 | Orthogonality construction, pp. 350–351 | Full PDF downloaded, relevant complete argument read; independent local construction and proof supplied |
| F. Comellas, largest-known graph table | Maintained UPC data, accessed 2026-10-11 | Degree $8$, diameter $2$: order $57$ and complete adjacency list | The downloaded list is independently shown isomorphic to our graph; a record table is not a nonexistence proof |
| A. J. Hoffman, R. R. Singleton, *On Moore graphs with diameters 2 and 3* | IBM J. Res. Dev. 4 (1960), 497–504, DOI 10.1147/RD.45.0497 | Moore equality has degree $2,3,7$, or possibly $57$; excludes $n=65$ at degree $8$ | Original scan located at Cornell; source fetch did not yield readable local full text in this task; final formal chain still requires proof |
| P. Erdős, S. Fajtlowicz, A. J. Hoffman, *Maximum degree in graphs of diameter 2* | Networks 10 (1980), 87–90, DOI 10.1002/net.3230100109 | Its theorem on p. 88 excludes degree $8$, order $64$ | Complete four-page original downloaded and read, including eigenvalue argument pp. 88–90 |
| M. Miller, M. H. Nguyen, G. Pineda-Villavicencio, *On the nonexistence of graphs of diameter 2 and defect 2* | J. Combin. Math. Combin. Comput. 71 (2009), 5–20 | Theorem 4 also excludes degree $8$, order $63$ | Publisher PDF downloaded; p. 12 directly inspected as image; proof depends on structural Theorem 2 attributed to another preprint |

Canonical links:
- Construction: https://upcommons.upc.edu/server/api/core/bitstreams/03389833-adb7-4b2c-b5e8-50f8fd5743fa/content
- Record table: https://web.mat.upc.edu/francesc.comellas/delta-d/desc_g/desc_g2.html
- Raw record graph: https://web.mat.upc.edu/francesc.comellas/delta-d/desc_g/adjacencies/adjD2/G8_2.adj
- Hoffman–Singleton original scan: https://people.orie.cornell.edu/dpw/orie6334/HoffmanS60.pdf
- Erdős–Fajtlowicz–Hoffman original: https://www.renyi.hu/~p_erdos/1980-14.pdf
- Miller et al. publisher record: https://combinatorialpress.com/jcmcc-articles/volume-071/on-the-nonexistence-of-graphs-of-diameter-2-and-defect-2/
- Miller et al. published scan: https://combinatorialpress.com/article/jcmcc/Volume%20071/vol-071-paper%201.pdf
- Miller et al. searchable author version: https://guillermo.com.au/pdfs/BothDegrees.pdf

## Baseline assessment
The concrete lower bound $57$ has now been made fully local and independently executable. The public record source still lists that order. The classical literature baseline is $57\le N(8,2)\le62$, subject to incorporating the upper-bound proofs in the final chain. This search found no larger degree-$8$, diameter-$2$ construction; that search outcome is not a proof that no newer result exists. None of the local historical solver-level claims is upgraded to a public extremal theorem here.

The original papers are more useful than abstracts because they identify exactly which structural theorems or spectral arguments the final Lean chain needs. The order-$64$ proof is self-contained in the retrieved paper. The order-$63$ publication has an inherited structural theorem whose referenced full proof has not yet been obtained. This is a documentation/formalization dependency, not grounds to claim that the published nonexistence result is false.

## An actual textual issue, and a usable alternate route for degree 8
Direct visual inspection of the **published** 2009 scan, printed p. 12 (PDF page 8), confirms the clause:

> “since (d − 2) is not divisible by 3 when d is even”

The corresponding image is `miller_published_pdf_page_8.png`. This arithmetic assertion is false for $d=8$. It occurs in Lemma 2's proof, which feeds Theorem 3. The searchable author version has the same text. Therefore that particular argument cannot be transcribed unchanged. This observation neither disproves Lemma 2 nor disproves Theorem 3.

For our parameter, the same page's **Theorem 4** offers another route, through the required number of 5-cycles:
$$N_5=\frac{(d-2)(d^4+2d^2-2d-25)}{10}.$$
At $d=8$, this equals $12549/5$, which is not an integer. Its proof uses the three vertex classes from structural Theorem 2 rather than Lemma 2. The specialized local 5-cycle counts in its derivation are $189,199,200$, with class sizes $3,18,42$, yielding $(3\cdot189+18\cdot199+42\cdot200)/5=12549/5$.

The remaining inherited source is M. H. Nguyen and M. Miller, *Structural properties of graphs of diameter 2 with defect 2*, cited as a preprint in reference [10]. Its full proof was not retrieved in this bounded task. For a fully checked order-$63$ proof, obtain/reprove its needed classification or use an independently verified alternative. The published Theorem 4 is an accurate literature exclusion, but the above arithmetic alone does not discharge that structural premise.

## Construction direction advanced in this task
A direct Brown57-to-58 extension preserving all old edges is impossible. More strongly, `BROWN_EXTENSION_OBSTRUCTION.md` proves that **at least eight old edges must be deleted and eight old–old edges added**. The tight seven-triangle cover has two patterns; all $4374$ choices of one deleted edge in each triangle fail the new vertex's two-step coverage, with a uniform proof explaining the failure. This advances a specific construction route; it does not shrink the original set of admissible graphs.


## Follow-up: structural publication located
The cited preprint is now identified as Nguyen–Miller, AKCE 7(1) (2010), 29–43. The original theorem and proof text were read through a public mirror; the needed statement is Theorem 6(i), pp. 41–42. See `N63_STRUCTURAL_SOURCE_CHAIN.md` for the exact dependency map, remaining diagram/proof obligations, and a degree-at-most-eight replacement for one older spectral exclusion. The earlier statement that its full proof was not retrieved describes the initial bounded pass; the chain is now more precisely located but is still not independently closed.
