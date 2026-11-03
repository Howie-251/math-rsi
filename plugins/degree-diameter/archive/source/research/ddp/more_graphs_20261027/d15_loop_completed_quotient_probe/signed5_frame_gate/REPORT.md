The frozen signed5-frame prediction failed at the first controller, so the test stopped before any signed-arc or binary-graph construction.

At controller0, the outgoing target order is0,11,59,79,180. All five B matrices have rank3 and their one-dimensional kernels agree projectively with the corresponding reverse arc output directions. Their normalized input-kernel representatives are:

```text
u0=(1,2,1,0)
u1=(1,1,1,1)
u2=(1,2,1,2)
u3=(1,2,2,0)
u4=(0,1,0,1)
```

The first four-subset tested, indices0,1,2,3, has rank4. The next subset0,1,2,4 has rank3. In particular the literal representatives already show u2=u1+u4 overF3, so these three lines are collinear. The five kernel lines therefore are not a projective5-frame. A simultaneous invertible coordinate change cannot change this dependency; no basis search was attempted.

One worker used0.003352509 CPU seconds, checking five kernels and two four-subsets. It completed zero controller frames and zero signed-arc checks, and generated no signed recipe, target graph, BFS or solver model. This rejects only the prescribed signed5-frame prerequisite for the proposed3072/degree10/D4 migration. It does not exclude general binary relations or general3072-point graphs.

Evidence: PREDICTION.json, run.py and RESULT.json. The latter contains the first complete literal counterexample. No other source, field, frame or coordinate system was tried.
