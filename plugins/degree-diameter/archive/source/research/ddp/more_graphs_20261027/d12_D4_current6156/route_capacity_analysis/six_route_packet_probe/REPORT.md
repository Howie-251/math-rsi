# Specified inverse-three-word augmentation fails

The frozen prediction added only aab and its inverse BAA to the already tested packet AABa, Abaa, Babb, BBAb. The prediction was that all six images would cover F3^4 for every source. It is refuted.

For va=(0,10,9,0), vb=(z,0,0,1) modulo 20, the four original routes have voltage ±(y+1)=10, while aab and BAA have voltage ±x=10. Every route ends at base 0, phase 10, independently of z. Their controller alignment is therefore valid.

The two added rank-three hyperplanes have normalized normals (0,0,1,1) and (1,2,2,0), in coordinate order x0,x1,x2,x3. Alongside the original four normals, all six remain distinct but do not cover the fiber. Each individual image has 27 points. Exact six-route union sizes over all 81 source coordinates are:

- 77 reached, 4 missing: 9 source coordinates;
- 75 reached, 6 missing: 18 source coordinates;
- 73 reached, 8 missing: 54 source coordinates.

In particular, source (0,0,0,0) misses fiber IDs 9,18,33,57. ID 9 is target (0,0,1,0); each of the six normalized normals evaluates nonzero there. The complete 81-source results, affine constants, controller forms, and normals are saved in RESULT.json.

The computation used 0.011304509 CPU seconds. No voltage assignments, graph generation, BFS, or alternate packet tests were performed. The optional 20-value z follow-up was conditional on a complete six-route certificate and was not started. Failure here excludes this six-route packet as a sufficient certificate; it does not show that other routes cannot cover its missing targets in a full graph. The fixed packet line is now stopped.
