# One GF4-chart transfer to the known76 controller fails

The prediction was frozen before generation: reuse the four exact global URSA16384 affineF4 line relations on the already known four-base C19 controller. Both controllers have alpha=(0123), beta=(0132) on their four base cells, with inverse type pairs0↔3 and1↔2. The chosen fixed76 controller has va=(0,12,4,0), vb=(17,0,0,1). Its lift would have19456 vertices at degree16, beyond the current public16384.

The prediction explicitly included a possible failure mechanism: four GF3 hyperplanes can form a full pencil, whereas F4 needs five. Since all four recovered constants are0, source-zero route images are linear subspaces. A target without a full-rank route and with at most four hyperplanes can have at most208 of256 reachable fiber states. No assertion that the old GF3 certificate carries over was made.

The single literal graph was generated from the actual F4 line relations, without assuming their canonical matrices invertible. It is simple, connected,16-regular, with19456 vertices and155648 edges. Native adjacency was checked for reverse consistency. The first root0 has eccentricity5 and963 targets outside its four-ball. One shortest-path witness is

    0 -> 4864 -> 127 -> 14601 -> 5020 -> 4.

Thus dist(0,4)=5. Missing target counts by controller label are0:39,2:36,17:36,30:192,32:192,39:36,42:192,47:192,61:48. Complete missing fiber-ID lists are retained in RESULT.json. The963 count refers only to one root's target vertices; it is not an unordered graph bad-pair count. The full graph's exact diameter remains unknown, with established lower bound5.

The test stopped after this first root. Had it passed, actual C19 deck translations would reduce complete verification to1024 roots (four base cells times256 fiber coordinates). That continuation was not run. No failed graph edge file was exported; input.txt and test.cpp reconstruct exactly this candidate.

Native generation/checking/BFS used0.006902 CPU seconds; compilation plus execution used1.50833013 CPU seconds. The original URSA16384 source was not rechecked by BFS, and no other controller, chart, phase modulus, or voltage was tried. A complementary agent is classifying the nine failed controller slots using its already cached341 actual word images, including inverse backtracks; this adds no candidate or BFS. Until that explanatory result is attached, the graph counterexample is already terminal.


## Cached-route explanation, with no extra graph test

The complementary `../route_capacity/C19_SLOT_ANALYSIS.json` assigns all341 words of length at most four, including inverse backtracks, to this exact controller. Its reachable fiber sets match the native first-root BFS point for point at all nine failed controller slots, totaling963 missing targets. No reduced-only negative shortcut is used.

- Controller30 has only word0022, controller32 only3311, controller42 only2002, and controller47 only2322. Each unique route has rank3 and reaches64 of256 fiber points. Keeping these controller endpoints and the linear relation parts, changing any affine offsets can only translate that64-point image. It cannot repair the192 missing values. This is a fixed-controller/linear-part obstruction, not merely failure of the offset-zero instance.
- Controller61 has reduced-two word20 and eleven actual routes in total. Its four distinct rank3 hyperplanes have common16-point intersection. Their union is exactly16+4·(64−16)=208; all lower-rank route images are already contained there. GF4 needs the fifth pencil member. Thus the predicted GF3-versus-GF4 pencil issue occurs literally.
- Controllers2,17,39 each cover220 points and miss36. Controller0 covers217 and misses39 across35 routes.

The source controller has b of order4, and the actual words1111 and2222 (b⁴,B⁴) have rank4, so they fill the entire source's own fiber. The transferred C19 controller instead has total b-cycle voltage17+0+0+1=18, which is nonzero modulo19. Those full-rank words no longer close. This explains an entire lost whole-fiber resource rather than a change in a local bad-pair score.

A separate agent's subsequently authorized b⁴-preserving controller family is reported separately; this report does not count those candidates as graph generation by this producer. No second graph was tested here.
