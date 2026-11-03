# Ten combinatorial (10_3) configurations

Retrieved 2026-10-12. No configuration classification was rerun.

`10_3.inc` is extracted from Anton Betten's official
[Orbiter user's guide](https://www.math.colostate.edu/~betten/orbiter/users_guide.pdf),
Section 12.6, PDF/printed page 536. `orbiter_manual_page536.pdf` preserves
that page. The full PDF was downloaded and this page read with `pypdf`.
The web search engine's extracted table contained duplicated/incorrect
rows; the saved data come from the actual PDF instead.

The header `10 10 30` specifies ten points, ten blocks and thirty
incidences. Each of the next ten rows is one configuration. An integer
`10*p+b` means point `p` belongs to block `b`, using indices 0 through 9.
The footer starts `-1 10`; the following row gives the distribution of
automorphism group orders. Its circumflex is a PDF font character.
`10_3_orbiter.json` parses the ten incidence rows as explicit triple lists.

`10_3_grunbaum.json` independently transcribes the ten triple lists in
[Grunbaum's Table 2.2.7](https://faculty.washington.edu/moishe/branko/CfsPts%26LinesFinal%20pdf%20files/Chapter%202.pdf),
page 2.2.6, PDF page 18. Its numbering differs from Orbiter's.

`verify_catalog.py` compares the tables as Levi graphs with point/block
colors preserved, checks their axioms and within-table nonduplication,
and saves explicit isomorphisms in `verification.json`. This is a table
check; completeness is inherited from the primary classification cited in
[the local-equivalence proof](../../../../proofs/dd82/construction/D1_LOCAL_CONFIGURATION_CATALOG.md).

`local_interfaces.json` is the root agent's separate expansion of all
leave matchings for the Grunbaum representatives and their duals. It
records exact one-sided equations, not global graph solutions.
