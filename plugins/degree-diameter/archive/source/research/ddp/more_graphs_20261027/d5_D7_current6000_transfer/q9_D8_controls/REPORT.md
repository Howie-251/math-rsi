# Two fixed GF9 controls for the two-base source — complete, no D8 graph

Both actual graphs have n=19440, m=48600, are simple connected 5-regular, and have **exact global diameter9**. The target was (5,8), saved baseline18810. Neither of the two fixed module embeddings achieved D8, refuting the frozen prediction.

The source has two voltage-base vertices. Its group is (GF9²×C5) semidirect H24, with H24 represented by beta^u alpha^v (u mod3, v mod8). GF9 is encoded a+3b for a+b*t over F3, t²=−1. The fixed beta is [[0,2],[1,2]], K=[[1,2],[0,2]], and alpha is scalar4*K or scalar8*K. All source phases and C5 voltages remain fixed, with the C5 action alpha→2. The source cross-link vector (1,4) over F5 is lifted as (1,−1)=(1,2) over GF9; the other normal relation (0,2)=2(0,1) is preserved. run.py contains all literal voltages and the new inverse formula.

These were two newly constructed graphs, not inherited results. Each graph was checked by complete BFS from vertex0 and vertex9720, one representative of each free left-deck orbit. The deck action preserves all right-voltage edges, so these two representative eccentricities establish the exact global diameter. Scalar4 has root R8 missing63/83; scalar8 has71/77. These four counts are representative-root targets, not unordered bad pairs. No old source D7 BFS was repeated.

The recorded total process CPU is0.131661777 seconds. Both controls completed, zero untried/unknown and zero new lower bounds. This closes the fixed two-control experiment only. The subsequent free_B experiment changes the cross-link normal vector and is recorded separately as a related finite variant; no new field, phases or unrelated template is proposed here.
