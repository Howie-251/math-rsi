# Primary-source venue evidence

Accessed 2026-10-22. These are scope statements and publication precedents, not rankings or acceptance predictions. No submission has been initiated. Official publisher/conference/journal pages only; the author-university repository below supplies a second primary bibliographic record.

## Work being assessed

The completed general result is for every integer k≥12 and every finite simple k-uniform hypergraph: edge count at most B_RS(k)+Δ(k) implies Property B, where Δ(k)=floor(sqrt(B_RS(k))/(8(1+ln k))). B_RS is the project's explicitly defined maximum integer RS-integral budget. The result gives a growing additive gain, without changing the leading asymptotic order. The general theorem has end-to-end Lean verification. This status comes from the project record, not the external pages below. Stronger small-k candidates must retain their individual paper/computation/formalization statuses: in particular m(5)≥35 and k=12 lock-point 4661 are not thereby promoted to complete Lean results; fully formalized m(5)≥34 remains distinct.

## Journals

| Venue | Official scope, paraphrased | Fit implication (our inference) |
|---|---|---|
| Electronic Journal of Combinatorics | Substantial discrete-mathematics research, including combinatorics, graph theory and combinatorial algorithms; correctness and substantiality are explicit criteria. | Direct topic fit for a self-contained new hypergraph bound. Lean supports correctness; mathematical content must supply substantiality. |
| Discrete Mathematics | Significant discrete-mathematics research; explicitly includes hypergraphs, extremal set theory and discrete probability; Contributions and Notes. Primarily experimental articles fall outside scope. | Direct fit for the analytic theorem, with computations as support. |
| Combinatorics, Probability and Computing | Combinatorics, probability and theoretical computer science; explicitly extremal set theory, probabilistic methods and random structures. | Strong subject fit if the central contribution is the refined probabilistic/structural argument. |
| Random Structures & Algorithms | Discrete random structures and applications in combinatorics/CS; emphasis on probabilistic methods, hypergraphs and algorithms. | Strong method/topic fit; improvement magnitude and reusable idea remain editorial questions. |
| Journal of Combinatorial Theory, Series A | Original combinatorial research, particularly finite/discrete structures and extremal combinatorics, among other areas. | In scope; scope alone establishes no evidence of the level of novelty editors would require. |

Exact sources:

- EJC: https://www.combinatorics.org/ojs/index.php/eljc/about/index
- DM (publisher description): https://shop.elsevier.com/journals/discrete-mathematics/0012-365X — Description, paragraphs 1–4. Direct ScienceDirect aims/scope returned HTTP 403; no unofficial mirror used.
- CPC: https://www.cambridge.org/core/journals/combinatorics-probability-and-computing/information/about-this-journal
- RSA: https://onlinelibrary.wiley.com/page/journal/10982418/homepage/productinformation.html
- JCTA (publisher description): https://shop.elsevier.com/journals/journal-of-combinatorial-theory-series-a/0097-3165

## Formalization conferences

- **ITP:** https://itp-conference-2026.github.io/ explicitly includes mathematical formalizations and interactive-prover applications. The series scope is also at https://itp-conference.github.io/ . A mathematical formalization can itself fit; a new proof-assistant algorithm is not stated as mandatory. Assessment should explain the mathematical and formalization significance rather than rely on the statement that Lean compiled.
- **CPP:** https://popl26.sigplan.org/home/CPP-2026 , Call for Papers → Topics of Interest explicitly includes certified mathematical libraries/theorems. Its review criteria ask for formalization design decisions, related techniques, library comparisons and lessons for future formalizations. Thus a formalization-focused paper should expose reusable proof engineering or library contributions; this is an inference from those explicit criteria, not an absolute requirement for a new formal method. These 2026 calls establish topic fit, not a currently open submission opportunity.

## Closely related publication precedents

- Aglave, Amarnath, Shannigrahi and Singh, *Improved bounds for uniform hypergraphs without property B*, Australasian Journal of Combinatorics 76(1) (2020), 73–86. Official journal contents: https://ajc.maths.uq.edu.au/index.php?page=get_volumes&volume=76 . This establishes an actual specialist-journal home for finite Property B bounds, not an equivalence of contribution strength.
- Cherkashin and Kozik, *A note on random greedy coloring of uniform hypergraphs*, RSA 47(3) (2015), 407–413, DOI https://doi.org/10.1002/rsa.20556 . Author-university primary record: https://ruj.uj.edu.pl/entities/publication/5ccaba16-350e-4844-af4b-ff5f7ad5a398 . The author abstract at https://arxiv.org/abs/1310.1368 describes a simpler proof of the RS asymptotic bound, extension to r-coloring, and edge-degree results. This is evidence of methodological value mattering independently of improving the binary leading order; its additional results prevent treating it as a like-for-like acceptance benchmark.

## Sources added for the targeted follow-up

- European Journal of Combinatorics (different from Electronic Journal of Combinatorics): https://shop.elsevier.com/journals/european-journal-of-combinatorics/0195-6698 . Its stated emphasis is pure combinatorial theory, mathematical structures, and connections with other areas; it accepts full-length work on important topics. This supports subject fit, not an official ranking relative to the Electronic journal.
- SIAM Journal on Discrete Mathematics: https://epubs.siam.org/journal/sidma/editorial-policy . The official policy explicitly includes extremal discrete structures and probabilistic methods, and asks for significant contributions. Therefore a claim that Property B has the wrong readership here is unsupported; an assessment of insufficient mathematical strength must be argued separately.
- JCTA's publisher description above explicitly sets a high significance standard and an even higher standard for very long papers. It does not impose an exclusive requirement to improve a leading asymptotic term.
- SODA: https://www.siam.org/conferences-events/siam-conferences/soda27/submissions/ and https://www.siam.org/conferences-events/siam-conferences/soda27/ . Selection emphasizes insights into efficient algorithms; related combinatorics is in scope. Our current theorem does not itself establish a new running-time, derandomization or algorithmic consequence. Treat this as a fit judgment, not a ban on pure combinatorial papers. The 2027 submission deadline shown has passed; no deadline recommendation is being made.
- CPP's above CFP discusses mathematical formalization design, alternative representations, library comparisons and lessons. These are grounds to explain the existing development; a new tactic or a second unrelated theorem is not a universal entry condition.
- Existing related formalization: Edmonds and Paulson, Hypergraph Colourings (2023), Isabelle Archive of Formal Proofs: https://isa-afp.org/entries/Hypergraph_Colourings.html . Do not claim the first Property B formalization. This publication-positioning task has not performed a complete formalization novelty audit.

