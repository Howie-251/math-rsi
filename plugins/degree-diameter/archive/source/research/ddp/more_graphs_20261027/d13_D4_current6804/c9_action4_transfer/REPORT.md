# The single connected C9/action4 transfer fails D4 at its first root

2026-10-27. Frozen prediction: the unchanged current6804 fiber chart on C9 semidirect_4 C12, retaining a=(1,1), b=(0,4), z=(0,6), would give a (13,4) graph on8748 vertices. The prediction is refuted.

## Candidate and legitimate connectivity

The exact multiplication used was (i,j)(k,l)=(i+4^j k mod9,j+l mod12). Since4 has order3 modulo9, z=y^6 is a central involution. Moreover a^4 b^-1=(4,0), which generates the entire additive C9, while a has phase1. These generators therefore span all108 controller vertices. The characteristic-two parity obstruction from the previous C8 transfer does not apply. No prime-field assumption was made for C9.

All fiber matrices, line directions and c=(0,0,1,0) were copied unchanged from the current6804 recipe. The vertex label is81(i+9j)+x0+3x1+9x2+27x3. All five label relations were generated and their undirected union was formed. The actual graph is simple, connected,13-regular, with8748 vertices and56862 edges.

## Route certificate and decisive actual test

The current chart differs from the earlier degree12 Mizuno chart, so its I/R2/full-rank facts were checked rather than inherited automatically. Inverse-consistent matrix representatives were matched to the actual inverse line relations. Among108 reduced four-line words,88 have full-rank image. Ten of the twelve reduced-two-word cancellation packets cover all81 fiber values, while the empty cancellation packet alone does not. The previously computed32 central-insertion packets were reused.

Together these sufficient certificates cover85 of108 controller vertices. Certificate failure alone was not treated as graph failure. A fresh BFS was then run from root0 in the generated graph. It reaches every vertex but has eccentricity5, with918 target vertices outside its four-ball. One exact witness is

    0 -> 8257 -> 5296 -> 2406 -> 1833 -> 730.

The target730 has controller coordinate(0,1) and fiber coordinate(1,0,0,0). Its computed shortest distance from0 is exactly5. The918 figure counts targets from one root; it is not an unordered graph bad-pair total.

The test stopped immediately after that first root. Therefore the whole graph's exact diameter was not determined: the established conclusion is D≥5, not an all-source D=5 claim. Had the first root passed, left controller multiplication L_h(g,x)=(hg,x) would have reduced full verification to81 identity-fiber roots, since it preserves every right-generator transition and fixed fiber relation. That continuation was not needed.

The full one-shot computation, including certificate preparation, generation, degree checking and first-root BFS, used0.104727329 CPU seconds. No compilation was needed. No original6804 BFS, further action/module candidate, chart adjustment or score optimization was run. Because the candidate failed, no final edge file was exported. `run.py` reconstructs the literal fixed graph, `CONTROLLER_CERTIFICATE.json` lists the precise certificate gaps, and `RESULT.json` retains the first-root metrics and shortest-path witness. This closes only the specified C9/action4 transfer with unchanged source generators and chart. No wider C9-family exclusion is asserted; no work remains in this scope.
