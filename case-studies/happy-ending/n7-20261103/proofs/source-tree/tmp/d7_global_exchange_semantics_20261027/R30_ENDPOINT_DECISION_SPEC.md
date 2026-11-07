# One bounded complete E5/E6 decision, 2026-10-27

Main-session mathematical specification. This is a fresh runtime in a new
isolation directory, not a restart of any existing run. Requested executor:
native gpt-6.1-sol/high, authoritative Linux only. No model fallback.

## Exact model and full-class reduction

For V={0,...,29}, assign every triple a color. Require all ordered rank3
packets, no B5, no weak7 (hence no R7), and no actual point in both internal
EndR5(V) and SrcB4(V). These are the full D7 conditions.

Define exact E_i iff there exists an actual R6 ending at i. Branch 5 requires
exactly five E_i; branch 6 requires exactly six E_i. Every endpoint is an
internal right root: E_i implies red(i,j,k) for all i<j<k.

Proof of redundancy: for R6 ending at i with penultimate u, any blue(i,j,k)
would make (u,i,j) red and yield R7, or make it blue and yield a B4 at u,
which also ends the R5 prefix. Both violate D7.

Every actual R30 D7 is in exactly one branch. All E form a red set, so
|E|<=6. Scoped b25 implies every R6-free subset has at most25 points;
therefore tau>=5. E is a transversal, so |E|>=5. The old R7 transversal
proof also gives tau<=5, alpha=25, but these values need not be encoded.
No four-deletion constraints, favorable core type, endpoint positions,
private-path template, artificial fan, or H–R embedding is imposed.

The E5 core is V\E; the E6 core is V\(E\{second actual endpoint}). All
multi-endpoint paths and packets remain in the full base model.

## Changed expression and value

The old complete R30 run had no exact endpoint population branch and no
explicit root-identity channel. The fresh formula exposes exact positive
R6 ending identities, the two exhaustive populations, and all corresponding
root colors. This adds strong propagation from the full-class R7 proof.
It does not claim a proven runtime improvement.

Use an unchanged full D7 base snapshot at actual N30. Positive endpoint
identities must use a new exact forward path recurrence, with joins iff
predecessor AND actual color and reach iff OR of every join. E_i is iff OR
of the exact R6 reaches ending at i. Use an audited exact count encoding.
Do not count the old one-way existence flags. For every actual D7 coloring
the canonical reach/count values give an extension; every satisfying
assignment projects to the specified full coloring.

## Budget and stopping

Exactly one controlled external default AE Kissat invocation per branch:
CPU<=180s, wall<=180s, address space<=4GiB, owned process group.
Total new solver invocations<=2; no retry, extension, diversification,
template relaxation, smaller/larger order, or sealed-runtime restart.

Run bounded Linux deterministic encoder controls first, then retain
source, CNF, solver command, full streams, termination status and hashes.
SAT must receive complete assignment/clause and independent color-only
semantic checks, all actual R6 endpoints, all forbidden shapes, and the
actual E5/E6 core with recomputed states and explicit index map.

For raw UNSAT retain finalized proof and report before any proof check.
No new proof checker installation or checker invocation is authorized by
this document. A later separately stated bounded check may use an existing
checker. A SAT proof stream is never called an UNSAT certificate.

If Linux/native execution or required transport approval is unavailable,
record NOT_RUN/blocked stage accurately, do not fall back, and return.

## Interpretation

Full SAT plus semantic checks refutes independent D<=29, and provides an
actual R30 input for subsequent canonical H–R embedding research.
It does not refute R30=>H<=48.

Only bound, proof-checked UNSAT for BOTH exhaustive branches gives D<=29,
then Q<=79 using current C<=50. One branch UNSAT excludes only its branch.
Raw UNSAT, timeout, error or unavailable execution has no upper-bound
credit. New results remain unreviewed/unaccepted; no Claude review.
