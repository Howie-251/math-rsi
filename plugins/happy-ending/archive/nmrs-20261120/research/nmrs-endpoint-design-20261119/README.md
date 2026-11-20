<!-- Publication excerpt: mathematical content retained; local paths/control-plane metadata redacted, links relocated. Original SHA256 in INVENTORY.json. Historical snapshots are superseded by HANDOFF.md. -->
# Endpoint request weight certificates

These are scoped mathematical research artifacts. The scientific executions ran
on the authoritative Linux server with
`<private-python-runtime>` and SciPy 1.15.3. The floating point
optimizer discovers weights; each certificate floors all nonnegative weights to
denominator 1,000,000. The standalone integer checker reconstructs every legal
face profile and checks the constraints without SciPy. This is not independent
external review or an optimality certificate for signotope capacity.

The complete mathematical interface, assumptions and infinite-family transfer
are in [the research proof](../NMRS_WINDOW_INTEGER_LIFT_20261119.md), sections 8.1–8.5.

## Reproduce exact checks

Run from this directory on Linux:

```bash
<private-python-runtime> verify.py a5-v44.json a3-v22.json a4-v15.json a6-v24.json normalized-a5-v44.json
<private-python-runtime> check_small.py
<private-python-runtime> verify_union.py union-a5-v44.json
<private-python-runtime> check_union_small.py
```

The checker creates `.verified.json` reports. Each report binds the certificate
bytes by SHA256 and gives the full profile count, objective integer numerator,
maximum red/private costs and any constraint violations. The row certificates
use `a E <= v-a+1`, `P <= v`; the normalized profile uses `E <= 1`, `P <= a`.
The small check independently enumerates actual request sets and faces for
three domains and compares their coverage counts to the endpoint formulas.
The union checker verifies all 123,410 legal four-endpoint profiles and all
861 repeated-red/private face profiles for the a=5, v=44 joint certificate.
Its small checker constructs actual request unions and verifies the unique
double payment directly. The joint certificate yields H >= 15493 and the
population bound 2,103,267. Its finite red cost must be transferred using the
mixture in the research proof, section 9.2; it is not a uniform per-face bound.

## Rediscover candidates

```bash
<private-python-runtime> solve.py --case 5 44 --case 3 22 --case 4 15 --case 6 24
<private-python-runtime> solve.py --case 5 44 --profile normalized
<private-python-runtime> solve_union.py
```

Rediscovery may choose different optima and overwrite candidate certificates;
recheck the resulting exact certificate. The recorded population bound consumes
only the retained exact certificate, not a floating objective or solver status.
The union discovery uses cutting planes; exact replay still checks every
legal profile, including constraints not added by the floating discovery.

`solve.json` and `solve-normalized.json` retain the actual remote commands,
successful exit codes and complete discovery/check output. The `preflight.json`
[Operational connection details omitted from this publication excerpt.]
authorized network call in `preflight-network.json`. No retry of an external
mathematical review occurred. Upload/fetch receipts preserve control-plane
outcomes; credentials are not stored in this directory.
