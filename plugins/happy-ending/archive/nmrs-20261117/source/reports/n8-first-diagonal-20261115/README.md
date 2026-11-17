# Finite strip-row verifier: prepared, not executed

This isolated directory belongs to the 2026-11-15 N7/N8 synthesis. It does not
contain a SAT encoding, CNF, solver invocation, or proof-checker certificate.

`verify_strips.py` uses only the Python standard library. It generates strip
coordinates, both chains, every intermediate ideal, and all ordered triples
of each chain. For each triple it checks every possible terminal label from
the two state differences through coordinate extrema. It checks shared
endpoints, no shared internal state, disjoint state-row families, catalog
counts, ordinary/exceptional counts, and the nominal triangular-cell arithmetic.

Prepared cases are 3x3, 3x4, 3x5, 4x4, 3x6, 3x7, 4x6, 5x7, and 6x6.
A successful run would verify only these finite state rows and arithmetic.
It would not independently prove the universal lifting to ordered colorings,
check all parameter values, certify SAT/UNSAT, or grant mathematical acceptance.

## Actual execution status

One authorized, read-only SSH probe was attempted using the existing project
credential source and pinned `known_hosts`. The [raw receipt](probe-receipt.json)
has exit code 255 and reports that no ED25519 host key is known for the current
endpoint, so strict host-key checking rejected the connection. The probe did
not request scientific-script execution. No source was uploaded, no remote
directory was created, and the verifier was not executed on Linux or Windows.
No host-key checks were weakened, no key was enrolled, and no login retry occurred.

A separately authorized, one-time public `ssh-keyscan -T 5 -t ed25519`
attempt then tried to compare the endpoint with the already deployed old
authoritative pin, without using a password or printing a key. It returned
exit code 1 and zero keys; see [the metadata receipt](pin-comparison.json).
Therefore no comparison could be established; this is not evidence of a
different host key. Work stopped without any HostKeyAlias login or further
connection attempt. `compare-pin.ps1` preserves that comparison procedure.

The verifier source has received a textual self-check only. Its syntax, runtime and
finite checks remain untested until an authorized Linux run succeeds.

## Reproduction

After the existing trusted SSH route is restored, first inspect remote status:

```powershell
& reports/n8-first-diagonal-20261115/transport.ps1 -Mode probe
```

Only when the remote directory is confirmed absent may the prepared create-only
transport be used; it refuses to overwrite an existing directory:

```powershell
& reports/n8-first-diagonal-20261115/transport.ps1 -Mode run
```

The authoritative Linux command is:

```bash
/opt/anaconda3/envs/forktqiu3/bin/python3.12 -B \
  /data/ktqiu_hdd/math_agent/reports/n8-first-diagonal-20261115/verify_strips.py
```

The verifier prints a JSON receipt with its source hash, generated chains,
case counts, and `status: PASS` only after every finite check succeeds. The
transport bounds execution at 45 seconds and preserves stdout/stderr on Linux
and a transport receipt locally. No PASS receipt exists at this handoff.
