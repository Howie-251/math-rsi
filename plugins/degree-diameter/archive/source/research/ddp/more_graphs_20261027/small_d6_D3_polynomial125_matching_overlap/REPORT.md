# F5³ source plus an arbitrary matching: exact overlap exclusion

The fixed q=5 polynomial source plus **any one simple complement matching**, including a partial matching, cannot have diameter three. The origin reaches at most 120 of the 125 vertices after augmentation; at least five targets remain outside radius three.

The parent first froze the conditional prediction max_x |B2(x) minus B3(p)|<=24. Its first q5 endpoint test evaluated the exact formal three-walk image at p and the closed two-step endpoint sets at all 125 possible x. The 120 eligible complement partners exclude precisely p and its four old neighbours. The actual complete result is **max marginal 20**, attained by 24 partners, so the prediction is supported more strongly than required. The saved symbolic CPU was **0.001438583 seconds**. These are exact endpoint evaluations, not graph BFS or matching trials.

The old origin ball has |B3(p)|=55 and |B2(p)|=21. When p is matched to x, delete x from the last-matching endpoint class because it is retained in B2(x). For every matched old neighbour u of p, delete the centre M(u) from its middle-matching closed ball because that centre remains in the last class. With k<=4 such neighbours, the full union has size at most 55+20+20+5k+5<=120. If p is unmatched, the first and two-matching classes vanish, leaving at most 55+21+5k<=96. `ANALYSIS_PROOF.md` makes this deduplication explicit, so it also covers partial matchings and does not double-subtract endpoints.

There was no source adjacency or augmented graph generation, BFS, matching assignment, or solver call. The missing-target lower bound five is not an ordinary unordered bad-pair count. Actual graph order and global diameter stay null. The scout's read-only formula/scope check and the independent paper review both found the endpoint and path-class interfaces valid; neither repeated the numerical endpoint test.

This is the small boundary case of the same polynomial-source matching mechanism, selected because the generic q>=7 bound is not strict at q=5. It is not a separate independent construction method. It excludes only the fixed q5 source plus one matching, not arbitrary 125-vertex degree-six graphs, multiple matchings or rewiring. In particular, adding an absolute C5 uses two new ports at each absolute and is outside this closed single-matching scope.

Saved target baseline: (6,3), lower bound 120, from the parent PREDICTION. Stop matching optimization for this family. `wiki_rows.json` contains the raw row and evidence links; no global Wiki synchronization was performed here.
