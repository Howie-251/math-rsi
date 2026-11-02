# Two-helper budget test after the exact single-point obstruction

The prior integer witness puts 13,876,887 of its total 14,775,252 weight on the 108 original free vertices. Thus the hard part of the source is mostly reaching other free vertices, rather than the whole source indiscriminately.

A direct pin has weighted closed-R2 contribution at most999999. In a two-adjacent-helper construction the other helper gives access through closedR1, whose maximum weighted contribution is997321. The proposed inequality W>12*C2+12*C1 is false. This refutes the budget obstruction prediction; it is only a necessary capacity pass and does not produce or validate a graph.

All972 old vertices belong to the closed neighborhood of the108free vertices. Their induced degrees are36 vertices of degree2 and72 of degree1; later actual component analysis refutes the guess that these are36P3.

This changed the next construction rule from one-root R2 cover to simultaneous R2/R1 cover for two adjacent helpers, with each old free pin assigned to at most one helper. That finite joint MIP was run once and returned UNKNOWN without an incumbent. It remains open; no extension of that run was automatically authorized.

This test evaluated existing integer weights and old adjacency only, 0.004636CPU, with no graph or solver run. Prediction and exact values are in PREDICTION.json and RESULT.json.
