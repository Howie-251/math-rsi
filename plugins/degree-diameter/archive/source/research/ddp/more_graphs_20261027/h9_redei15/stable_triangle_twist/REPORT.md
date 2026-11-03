The explicit triangle twist is a new Frobenius-stable realization of the same projective blocking 15-set. The frozen prediction was supported by one 91-point field calculation and a PGL3(F3) orbit calculation.

Use F9 encoding a+3b=a+b*u with u²=−1 and μ4={1,2,3,6}. Start with B+++={e0,e1,e2} plus e_i+t e_j for i<j and t∈μ4, and apply R with rows (1,0,0),(0,1,1),(0,3,6). Its determinant is 3, so R is invertible.

The resulting 15-set is Frobenius-stable with five fixed points and five conjugate pairs, hence ten fully unsplit pins. It is minimal blocking for all 91 lines. The line intersection histogram is 60 tangents, 12 two-secants, 16 three-secants, and three six-secants. Exactly one of the three six-secant triangle vertices is Frobenius-fixed; the old seed has all three fixed.

The complete PGL3(F3) orbit has 702 distinct masks and stabilizer order 8. Its exact mask intersection with the existing 702-set orbit is empty. `orbit.json` preserves the old pool orbit schema and coefficient-point indexing, so the producer can reuse the existing plane embedding interface. B+++ itself was checked only as a control: nine fixed points and three conjugate pairs, giving twelve unsplit pins; no orbit or source pool was generated for it.

Actual CPU was 0.022166238 seconds. This task generated no source pool, R4 balls, graph, or solver model. The result establishes a new candidate orbit; source degree and complete coverage remain the producer's separate task. No new graph or lower bound is claimed.

Evidence: `PREDICTION.json`, `run.py`, `RESULT.json`, `orbit.json`; old comparison inputs `../pool/orbit.json` and `../SHAPE.json`. The independent paper argument is saved separately as `ANALYSIS_TWIST.md/json` when ready.
