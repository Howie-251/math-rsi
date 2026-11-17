# Direct native boundary-trace LP for 988

2026-11-16. Linux scientific execution only. This directory is exclusively
owned by the `global_lift` worker; no production encoding, sealed job or other
worker's artifacts are modified. Integer certificates here are same-session
candidate evidence; no independent review is requested or claimed.

**Current result:** the final generic native jobs and separately implemented
selected-row/standalone checkers actually succeeded on Linux. Their exact
certificates give 236 holes/`988<=688` and 124 holes/actual `D9<=458`, hence
`ES(9)<=1148` through the existing interfaces. All selected rows are native
traces; no numerical slice imports or public cycles are used. Self-contained
compact certificates replay without an optimizer or large matrix.
See [RESULTS.md](RESULTS.md) for exact arithmetic, hashes and raw receipts.
The earlier 233-hole/691 certificate remains a preserved successful baseline.

The precise caller is every ordered rank-three signotope configuration with no
blue or red path of eight vertices and no same-end weak nine-gon. Its states
are the 924 ideals of the 6 by 6 box, represented equivalently by six-subsets
of `[12]`. For decreasing heights lambda, the subset is the increasing list
`lambda[5]+1,...,lambda[0]+6`. Each actual state can occur at most once. The
variable h_W is its missing-state indicator, hence is in {0,1}.

The desired improvement to the current bound 706 requires at least 219 holes.
An LP relaxation is used for discovery; its floating optimum is not a theorem.

At the exact old threshold 218, the ordinary 252 mother rows already have a
useful common equality: their total demand is 1008, internal holes serve six
rows and private holes one. The two disjoint outer private slices each need
30 holes, so `6H >= 1008+5*60 = 1308`. Equality forces exactly 30 holes in
each private slice and exactly four holes in every ordinary mother row.
This is a statement about the same hole set, available for subsequent
critical-layer analysis even if the continuous LP does not improve 218.

For an explicit paper continuation, let the ten inner coordinates be I, let
B and R be the four-subset marks of blue and red internal holes, and let P
be the multiset union of the two 30-element private five-subset families.
Write x=|B|, y=|R|, so x+y=158. For each i and pair ij, the exact ordinary-row
equations give, with degrees denoted by subscripts,

`504 = x + 5 B_i + 5 y - 5 R_i + P_i`,

`224 = B_i+B_j+4 B_ij + 4(y-R_i-R_j+R_ij) + P_ij`.

Thus every P_i is congruent to 4x-1 modulo 5, and every P_ij is congruent to
`-B_i-B_j` modulo 4. For a triple ijk the corresponding exact identity is

`84 = B_ij+B_ik+B_jk+3 B_ijk
      +3(y-R_i-R_j-R_k+R_ij+R_ik+R_jk-R_ijk) + P_ijk`.

These constraints cover the actual two private families jointly and do not
assume either family is an arbitrary independent optimal 5 by 5 example.
They are not claimed to exclude the 218-hole layer.

## Admissible rows and exact quantifiers

For each a by b box, choose decreasing `q_1,...,q_(a-1)` in `[1,b]` and
`p_i` in `{q_i,q_i+1}` with p decreasing and `p_i <= q_(i-1)`, where q_0=b.
Take S=(p_1-1,...,p_(a-1)-1,0), E=(b,q_1,...,q_(a-1)). The difference E-S has
every column and every height nonempty, and any cell in an earlier column is
at least as high as any cell in a later column. Conversely, any two ideals
with these properties have these parameters: the lower and upper endpoints
of adjacent column intervals overlap by zero or one level, giving precisely
q_i <= p_i <= q_i+1.

The column chain and the height chain from S to E have disjoint interiors and
jointly a+b states. By [EIGHT-MOVE section 2](../EIGHT-MOVE.md), **every occupied
subset** of this trace has a common-end blue/red path pair with total vertex
count equal to its population plus two. Missing endpoints are permitted.
Thus at most eight states are occupied in this weak-nine caller: two-vertex
degeneracies are excluded by the actual forbidden eight-point monochromatic
paths. Each trace therefore needs a+b-8 holes.

All traces are generated in the 6 by 6 mother (RHS 4), in each one-coordinate
containing 5 by 6 and avoiding 6 by 5 slice (RHS 3), and in every ordered pair
of distinct coordinates (contain i, avoid j), which is a 5 by 5 slice (RHS 2).
The inverse slice map is explicitly `w -> rank_compression_inverse(w) union
{i}`. It fixes the same containing coordinate and the same avoiding coordinate
for all states in that row. Coordinate erasure is the existing ordered
threshold-chart compression; its actual inherited color labels and forbidden
paths are preserved. It is not arbitrary relabeling of the state poset.

Every such 252-state 5 by 5 slice also needs 30 holes by the existing actual
`N_sig(9,7,7)<=222` import. This is a universally quantified slice constraint,
not a 30-hole assumption about a pure 4 by 4 private layer. The two outer
private 5 by 5 slices of this 6 by 6 mother are among these ordered pairs.

Further universally valid integer imports, identified after freezing the first
run but **not present in the v1 source**, are: every single-containing or
single-avoiding 462-state slice needs 82 holes by PROOF section 9.3; every
double-containing or double-avoiding 210-state slice needs 25 holes by
TRANSFER-NEXT's 185 bound and genuine transposition. These are potential
next-stage constraints, not falsely attributed to the v1 matrix. The separately
frozen `direct_lp_v2.py` adds exactly these 24+132 rows, and its run has a fresh
output directory. The independent verifier supports both profiles.

The optional public cycle extension is disabled in the first native run.
Its input will require the separately validated cyclic order, support and the
signotope packet bridge in [EIGHT-CYCLE-TRANSFER](../EIGHT-CYCLE-TRANSFER.md).
Published weights and branch trees are never reused as weak-nine evidence.

## Certificate arithmetic and implementation boundary

The generator minimizes sum h under all stated row constraints and 0<=h<=1.
It rounds nonnegative dual row weights at several integer scales Lambda.
For integer row weights w, let D=sum w*d, l_W=sum_(rows containing W) w, and
P=sum_W max(0,l_W-Lambda). Since h_W<=1,

`D <= sum l_W h_W <= Lambda * sum h_W + P`.

Consequently `sum h >= ceil((D-P)/Lambda)`. No floating inequality is consumed
by this conclusion. `certificate.json` stores every nonzero row weight and
all 924 integer loads. `verify_cert.py` independently regenerates **each used
row** from its q/p or slice metadata, checks actual monotonic difference cells
and chain-state identities, and recomputes all integer loads and the bound.
Only an actual successful Linux receipt counts as an execution.

Sources `direct_lp.py` and `verify_cert.py` are local Windows authored files;
all construction, solving and replay run on the authoritative Linux server.
`transport.ps1` reads existing connection fields and fixed askpass/known_hosts,
redacts connection details and never places credentials in outputs. A failed
transport receipt is retained as such. `remote-start.sh` is a frozen launcher
with the generator embedded as wrapped base64 and a bounded 600-second job;
the parent may deliver its bytes through its already connected SSH channel.

## Actual execution state

The first parent-delivered v1 Linux launch ended with `run-native.exit=1`:
`/opt/anaconda3/envs/forktqiu3/bin/python3.12` raised
`ModuleNotFoundError: No module named 'scipy'` before matrix construction or LP.
This is a real failed execution, not an LP result. The parent and seven worker
then located existing SciPy in the same host's Python3.10 environment and
successfully executed the frozen v2 source. The success and its independent
integer replay are documented separately in RESULTS.md. No scientific
execution has occurred on Windows.
