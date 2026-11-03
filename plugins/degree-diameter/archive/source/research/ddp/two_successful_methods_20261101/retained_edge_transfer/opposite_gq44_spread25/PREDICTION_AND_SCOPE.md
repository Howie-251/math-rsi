# PRED: fixed GF4 balanced GQ opposite graph and spread extension

Written before any new numerical geometry or graph execution, 2026-11-01 UTC.

This is one fixed new source/rule variant within mechanism A, retained-edge extension by complete current radius-2 pin coverage. It does not restart the completed 6160 construction or its source, and is not a field/spread search or independent new framework. The same Degree/Diameter Goal stays ACTIVE. New-source public comparison and final independent acceptance are separate root-owned tasks.

## Stage 1: geometry only, authorized now

Use GF4 = F2[w]/(w^2+w+1), codes 0,1,2=w,3=w+1, XOR addition. Use GF16 = GF4[beta]/(beta^2+beta+w), code u0+4*u1 for u0+u1*beta. The predicted relative trace is u1. The 4-vector coordinates are (u0,u1,v0,v1), interpreted as (u,v) in GF16^2. Normalize each nonzero GF4 vector by scaling its first nonzero coordinate to 1 and sort the 85 normalized vectors lexicographically. Set B((u,v),(u',v')) = Trace(u*v'+v*u'). Generate every isotropic projective line from independent projective point pairs with B=0, take its 5 normalized GF4-span points, deduplicate, and lexicographically order the resulting point-ID tuples.

Prediction to test, not a result: 85 points, 85 lines; 5 points per line and 5 lines per point; any two points on at most one line; all 6800 nonincident point-line pairs have exactly one collinear projection. The 16 GF16 slope subspaces {(u,a*u)} and infinity {(0,v)} should yield 17 of these lines and partition all 85 points. The basis, multiplication relation, trace, alternating/nondegenerate form, and normalization are actually checked. A discrepancy stops this instance and is reported.

Stage-1 resource cap: single Python worker, at most 30 CPU seconds, no solver, no BFS, no complete opposite source adjacency, no candidate graph. Save literal field tables, 85 points/85 lines, both incidence directions, the 17 spread IDs and generating slopes, and all projection witnesses. No install, native compile, hash, checksum, or artifact manifest.

## Stage 2: only after an explicit root go-ahead

Conditional prediction: old vertices (p,l) have label 85*p+l and adjacency for distinct vertices (p,l),(q,m) iff p lies on m and q lies on l. Predicted old source: 7225 vertices, 90100 edges, 425 incident flags of degree 24, 6800 nonflags of degree 25. Do not report these formula predictions as generated facts.

For the fixed spread in slope-code order 0..15 then infinity, attach new vertex 7225+j to all flags (p,l) with p on the jth spread line. Predicted 25 distinct pins per new vertex; the 17 pin sets partition the 425 degree-24 flags. Before each insertion, check all 25 pin degrees and the complete current radius-2 pin union over every current vertex, including earlier new vertices. Stop on the first failure without adjusting the rule. Predicted final graph: 7242 vertices, 90525 edges, all degrees 25, all old edges retained. Write the unique complete unordered edge table, check simplicity and reciprocity, and run one final ordinary root-0 connectivity BFS. No old-source or final candidate all-roots BFS by the producer. Root will arrange a fresh independent check.

Stage-2 budget, if released: one worker, at most 30 CPU seconds, one fixed source and one final candidate, zero solver calls, no search variants. The proof must bind the literal new incidence and spread tables and include all old-old, old-new and new-new routes, following the accepted 6160 mechanism. Construction, independent acceptance, concrete Lean, and public comparison remain separate states; neither old source nor candidate is a public record merely from the formula.
