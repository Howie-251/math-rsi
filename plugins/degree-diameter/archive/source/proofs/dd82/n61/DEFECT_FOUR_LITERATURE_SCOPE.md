# Literature scope: degree 8, diameter 2, defect 4

Date: 2026-10-13. Target: simple undirected graphs with maximum degree 8,
diameter 2 and order 61. This is a bounded literature check for the connected
weighted-defect mechanism, not a new nonexistence proof.

**Result.** No theorem directly excluding this target, or excluding its connected
weighted defect matrix, was located in the sources checked below. This reports
the result of this search; it does not establish that no such theorem exists.
The applicable general repeat identities are already present in the project.

## Parameter translation

The ordinary degree/diameter Moore bound here is
\(M_{8,2}=1+8+8\cdot7=65\), so the defect is 4. Regularity follows directly:
a vertex of degree at most 7 could reach at most \(1+7+7\cdot7=57\) vertices.
Thus every target has adjacency matrix satisfying

\[
B=A^2+A-7I-J,\qquad B\ge0,\quad B_{uu}=0,\quad B\mathbf1=4\mathbf1,
\quad AB=BA.
\]

The last identity follows because \(AJ=JA=8J\). No assumption that \(B\) is
binary is justified. Connectedness of this weighted 4-regular matrix does not
make it a *cyclic defect* graph in the terminology below.

## Primary sources and exact boundaries

| Source and original location checked | Statement or hypothesis relevant to this search | Consequence for order 61 |
|---|---|---|
| M. Miller and G. Pineda-Villavicencio, *Complete catalogue of graphs of maximum degree 3 and defect at most 4*, Discrete Applied Mathematics 157 (2009), 2983–2996, [publisher abstract / DOI](https://doi.org/10.1016/j.dam.2009.04.021), first-page abstract. Also the earlier author manuscript [*On graphs of maximum degree 3 and defect 4*](https://guillermo.com.au/pdfs/GPVPaper3.pdf), PDF pp. 1–2 and §5, p. 8. | The catalogue fixes maximum degree **3**. Its new nonexistence range is defect 4 and diameter at least 5; it completes the cubic catalogue with defect at most 4. The earlier manuscript likewise explicitly fixes degree 3. | Neither the cubic hypothesis nor its parity arguments transfer to even degree 8. The final catalogue's abstract and the earlier manuscript were checked; they are distinct documents, not interchangeable full-text evidence. |
| R. Feria-Purón and G. Pineda-Villavicencio, *On bipartite graphs of defect at most 4*, Discrete Applied Mathematics 160 (2012), 140–154; [author arXiv PDF](https://arxiv.org/pdf/1010.5651), §3, PDF p. 4, and Theorems 5.2–5.4, PDF pp. 19–20. | Defect is measured from the **bipartite** Moore bound. Theorem 5.2 excludes bipartite defect-4 graphs for degree at least 3 and odd diameter at least 5; Theorem 5.4 addresses degree 3 and even diameter at least 6. Section 3 handles diameter 2 separately. | At diameter 2 the bipartite bound is \(2\Delta=16\), not 65. These are not statements about ordinary defect 4 at order 61. There is no hidden even-degree-8, diameter-2 case to import. |
| C. Delorme and G. Pineda-Villavicencio, *On graphs with cyclic defect or excess*, Electronic Journal of Combinatorics 17 (2010), R143; [author arXiv PDF](https://arxiv.org/pdf/1010.5841), §1, PDF pp. 2–5, especially the restriction on p. 3, equation (4) on p. 4 and Problems 1–2 on p. 5. | The paper explicitly restricts its subsequent study to defect/excess **2**. Cyclic defect means \(B=A(C_n)\). Its degree-parity and cyclotomic conclusions retain that premise; some results further require odd degree or diameter at least 3. | A connected weighted 4-regular \(B\) is outside this cyclic-defect domain. The general regularity observation and equation (4) do apply, but give the identities already displayed above. |
| M. H. Nguyen and M. Miller, *Structural properties of graphs of diameter 2 and defect 2*, AKCE International Journal of Graphs and Combinatorics 7 (2010), 29–43; [publisher text](https://www.tandfonline.com/doi/pdf/10.1080/09728600.2010.12088909), p. 31, Observations 2–3 and Theorem 1 (Neighbourhood Theorem). | Theorem 1 is stated for a regular \((d,k,\Delta)\)-graph with arbitrary positive defect: the multiset of neighbours of repeats equals the multiset of repeats of neighbours. The subsequent structural classification is explicitly defect 2. The theorem statement and page position were available in the publisher-indexed text; direct full-PDF retrieval failed. | The general statement applies at defect 4 and is exactly the multiset form of \(AB=BA\). The defect-2 repeat-type classification does not apply. No new exclusion follows from the checked statement. |

The word *excess* in the cyclic paper concerns the lower Moore bound for
minimum degree and odd girth, with order \(M+\epsilon\); see its §1, PDF p. 2.
Cage/excess theorems therefore require a different parameter translation and
cannot be used by changing the sign of the present defect. Likewise,
almost-Moore defect-1 results and defect-at-most-2 results do not assert
nonexistence at defect 4.

## Maximal-repeat lead and connectedness

Nguyen and Miller's [*Structural properties of graphs of diameter 2 with
maximal repeats*](https://doi.org/10.1016/j.disc.2006.09.057), Discrete
Mathematics 308 (2008), 2337–2341, was found through the bibliography. The
publisher abstract and metadata were accessible; the full theorem statements
were not retrieved. No unchecked theorem from that paper is used here.

There is an elementary boundary independent of that paper: if a defect-4
target has \(B_{uv}=4\), nonnegativity and row sum 4 imply that \(u,v\) form an
isolated two-vertex component of the support of \(B\). Hence the connected
61-vertex defect mechanism cannot contain a multiplicity-4 repeat. This says
nothing by itself about multiplicity 3, which remains a separate project
obligation.

## Search record and stopping point

Local records checked first were
[LITERATURE_BASELINE.md](../construction/LITERATURE_BASELINE.md),
[LITERATURE_DEFECT3_NOTE_20261011.md](../../../context/dd82/LITERATURE_DEFECT3_NOTE_20261011.md),
the relevant local `literature/dd82/` entries, and narrow literature references
in `N8/N8_LLM_SAT_REPORT_REVISED_20260930.md`. They did not supply a defect-4
closure. Miller–Širáň's 2013 survey, pp. 15–16 and its bibliography, was used
as a discovery guide, not as a substitute for the primary theorem hypotheses.

Web searches combined “defect four” / “defect 4” with diameter two, Moore,
even degree, nonexistence, and the target order; the project arXiv metadata
helper was also invoked successfully with a defect/Moore/diameter query.
No PDFs were saved locally; no graph computations, solver runs, or Gemini
calls were made.
The `research-lit` workflow was restricted under V3 to local and primary web
sources and this one requested note; no shared navigation or wiki was changed.

The usable literature input is therefore the existing general repeat-matrix
framework. The present search supplies no external theorem that closes
connected weighted defect 4 at \((8,2,61)\).
