# Quartic census scope for small diameter

A complete Cayley census does exist: Evans–Potočnik, [A census of Cayley graphs](https://arxiv.org/abs/2512.05406), abstract and Section6, gives all connected simple4-valent Cayley graphs through order1025 (11,361,600 nonisomorphic graphs). The [authors’ census site](https://graphsym.net/) independently states that coverage and offers sparse6 files by order; the full archive is about24GB. No census archive was downloaded.

The degree4 Moore bounds are53 for D3 and161 for D4. Thus every possible quartic Cayley graph relevant to either question is inside that complete collection. This is an implication of the census coverage, not a diameter exclusion: the paper does not tabulate diameters, and this bounded read obtained no verified maximum order at D≤3 or D≤4. In particular, **neither “Cayley>41 at D3 impossible” nor “Cayley>104 at D4 impossible” is established here**. No40/98 or other guessed maximum is adopted.

For the larger vertex-transitive class, no complete census covering every quartic VT graph through161 was confirmed. The same author site separately supplies all quartic arc-transitive graphs through640 and graphs admitting a half-arc-transitive action through1000. These are restricted classes and cannot exclude arbitrary VT or Cayley graphs, which need not be edge-transitive.

This scout generated no graph, parsed no census graph, and called no BFS or solver. It does not block the already frozen108-group experiment. It does identify an existing complete Cayley data source that should be queried for a verified diameter summary before future broad group enumeration. LITERATURE_SCOPE.json records the exact read scope and unconfirmed extrema; no new method row is created.
