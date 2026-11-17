# Linux execution unavailable before SSH authentication

The fixed-spec implementation is ready in `probe.py`, `verify.py`, and
`transport.ps1`. It has not been executed or tested on Linux. No CNF, schema
receipt, model, proof, solver receipt, or checker receipt exists locally.
This is neither SAT nor UNSAT evidence and grants no mathematical conclusion.

The first unprivileged SSH attempt was denied by the local execution sandbox.
An approved escalated launch attempt then lost its stdin pipe because SSH
closed. Escalated read-only status requests returned exit 255 and
`Connection closed by 10.60.133.166 port 22`. A verbose read-only request
established the precise phase: TCP connected, the client sent its SSH version,
then `kex_exchange_identification` reported closure before any remote version,
key exchange, authentication request, or remote command execution. The raw
verbose evidence is `ssh-diagnostic-output.txt`. A later status check repeated
the same closure (`status-receipt.json`). No solver invocation was possible
through those failed connections.

The source fixes introduced during this control-plane work are limited to
robust SSH pipe-failure receipts, a 615-second hard process kill, separated
DRAT checker arguments `-t 600`, and additional physical SAT reporting of
which marked vertices lack finite blue-five incoming/outgoing witnesses.
They add no mathematical rule or alternate formula.

Resume by establishing the existing SSH route and reading status first:

```powershell
& reports/n7-blue-through-seventeen-20261113/transport.ps1 -Mode status
```

Only if the directory is confirmed absent, launch the create-only prepared
directory. If it exists, inspect its actual status and artifacts rather than
reissuing launch. The worker creates an exclusive `solver-invocation.json`
before the one authorized external Kissat invocation. The fixed solver command
is:

```text
/data/ktqiu_hdd/math_agent/AE_kissat2025_MAB/build/kissat --no-binary --time=600 formula.cnf proof.drat
```

External hard limit is 615 seconds. A raw UNSAT result is accepted only after
the actual successful command below, also with a 615-second external limit:

```text
/data/ktqiu_hdd/math_agent/cadical-sc2025/build/drat-trim formula.cnf proof.drat -t 600
```

The independent schema rebuild precedes the sole solve. SAT verification
checks the complete assignment, then independently computes all finite
constraints and canonical virtual-red-five/M0 closures from triple colors.
No intermediate marked point is required to have finite blue-five anchors.
