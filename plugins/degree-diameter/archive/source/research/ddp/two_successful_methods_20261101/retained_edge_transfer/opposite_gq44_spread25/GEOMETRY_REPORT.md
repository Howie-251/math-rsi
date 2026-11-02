# Actual geometry preparation

The fixed GF4/GF16 construction passed. This report concerns incidence geometry only. No complete source graph or candidate graph has been generated.

GF4 code 2 is w with w^2=w+1; field multiplication is not integer multiplication modulo 4. GF16 element code u0+4*u1 means u0+u1*beta. The actual multiplication table satisfies beta^2=beta+w, its defining polynomial has no GF4 root, all finite field-law checks passed, and u+u^4 equals the GF4 element u1 for all 16 elements.

There are exactly 85 lexicographically sorted normalized projective vectors (u0,u1,v0,v1), normalized so the first nonzero coordinate equals 1. The checked alternating form is Trace(u*v'+v*u'); its radical is zero. The 85 distinct isotropic lines are sorted lexicographically as ascending five-point-ID tuples. Every point belongs to five lines, every line has five points, two points share at most one line, two lines share at most one point, and point collinearity agrees exactly with B=0. All 6800 nonincident point-line pairs have one collinear projection. PROJECTION_WITNESSES.json gives each projection and its unique joining line.

The fixed spread uses slope codes 0..15 followed by infinity. Its line IDs are

    21,26,31,36,57,54,67,64,77,82,71,76,49,46,43,40,0.

All 17 lines belong to the generated 85-line geometry; their five-point sets are disjoint and cover every point exactly once. PARAMETERS.json contains every point, line, generating pair, both incidence directions, ordered spread slope data, and the point's unique spread owner. This numbering is now frozen. The conditional graph labels are old 85*p+l and new 7225+j.

Actual preparation cost: 0.050489278 CPU seconds, one worker, zero solver calls and zero BFS calls. Source/candidate construction is held until root release. Prediction 7242 is not an actual graph result here. Independent acceptance, public comparison and final formalization are separate tasks.
