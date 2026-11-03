# Public comparison: verified extension, not a record

Checked 2026-11-01 against the original Delorme paper and the October 2026
primary paper. No graph generation or distance computation was used here.

Delorme, *Grands Graphes de Degré et Diamètre Donnés*, European Journal of
Combinatorics 6 (1985), 291–302,
[original PDF](https://web.mat.upc.edu/francesc.comellas/old-files/delta-d/papers/81981341.pdf),
§2, p.292, states the polarity construction for **odd powers of two**:

\[
q=2^{2m+1},\quad \Delta=q+1,\quad D=3,\quad n=(q+1)(q^2+1).
\]

Thus q=32 is admissible, giving n=33825 and maximum degree33. Already
N(35,3)≥N(33,3)≥33825>20580.

The same original paper §8(c), p.299 removes diagonal loops and identifies
q²+1 absolute vertices of degreeq, pairwise at distance3. Every other vertex
has exactly one absolute neighbor. Its §7 replication rule therefore permits
two new false twins of every absolute vertex, yielding

\[
n=(33+2)(32^2+1)=35875,\quad\Delta=35,\quad D=3.
\]

The hypotheses and formulas are independently restated in
[Isham–Lakhotia–Monroe–Petrini, arXiv:2608.27253v2](https://arxiv.org/html/2608.27253v2):
§7.1 gives the admissible q; Propositions7.4–7.8 give degree, order and exact
diameter; §2.3 explains loop removal; §7.7 states replication. These are
single-factor polarity graphs; Corollary7.11 about products is not needed.

**Disposition:** the actual20580-vertex35-regularD3 graph is a verified new
instance of our affine extension rule, but it is not a degree–diameter record.
35875 is a proved known lower bound, not a claim of the latest global optimum.
The earlier13272 PolarStar value was only one family's instance and must not
be used as the best-known comparison. No Lean or controller66 continuation is
justified by record improvement at degree35.
