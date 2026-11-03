# Frozen obligations: internal double paths at order 61

Date: 2026-10-13. Reviewer: `/root/internal_path_proof_check`.
This is the bounded obligation inventory for the two declared inputs,
before the final audit verdict. It does not add an exclusion claim.

## Declared inputs and quantified scope

- `proofs/dd82/n61/INTERNAL_DOUBLE_PATH_LOCAL.md`, complete, lines 1–190.
- `proofs/dd82/n61/INTERNAL_DOUBLE_PATH_FOLLOWUP.md`, complete, lines 1–114.

For every simple undirected 8-regular graph `G` on 61 vertices with
diameter at most two, put `B=A^2+A-7I-J` for its actual adjacency `A`.
With the explicitly inherited defect conclusions below, every ordered
triple of consecutive vertices `u,v,w` of the double-defect forest has
the stated local necessary structure. For every double-defect path
`v_0,...,v_m`, `m>=2`, its actual principal adjacency block is symmetric
Toeplitz, and its selected distinct positive offsets obey the stated
rectangle restriction. Every complete double-defect component has at
most 52 vertices. These are universally quantified necessary conditions,
not sufficient constructions and not an order61 exclusion.

## Inherited assumptions and their exact sources

I1. `A` is a single symmetric binary 61-by-61 matrix, with zero diagonal
and row sum eight, and diameter at most two. This is the input hypothesis.
The extension from maximum degree at most eight is supplied by the
regularity statement in `CONNECTED_TRIPLE_EXCLUSION.md`; it is inherited.

I2. `B` is symmetric, nonnegative integral, zero-diagonal, row sum four,
has entries in `{0,1,2}`, and has connected positive support. Source:
`proofs/dd82/n61/CONNECTED_TRIPLE_EXCLUSION.md`, including its explicitly
reviewed finite-enumeration and checked-CNF dependencies. Those computations
and underlying proofs are not repeated in this audit.

I3. `D=(V(G),{xy:B_xy=2})` is a path forest. Source:
`proofs/dd82/n61/DOUBLE_DEFECT_CYCLE_OBSTRUCTION.md`. Its accepted status
is evidenced by the earlier local adjacent-double audit and Gemini round1,
then carried into the completed handoff. Only source/import/status
alignment is checked here; the cycle proof is not independently reproved.

Usage: I1 gives actual common-neighbor identities and commutation; I2
gives nonnegative saturated rows and row budgets; I3 excludes `beta=2`
and supplies component language. Connected support is a transitive
dependency of I3, not an additional fresh step in either target proof.

## Typed symbols

| Symbol | Type and scope |
|---|---|
| `A,B,J,I` | Real/integer matrices of size 61; `A` binary, `B` nonnegative integral; `J` all ones, `I` identity |
| `mu(x,y)` | Nonnegative integer common-neighbor count for distinct original vertices |
| `u,v,w` | Three distinct consecutive vertices of `D` |
| `T=N_A(v)` | Eight-element vertex set, proved independent |
| `U,W` | Three-element subsets of `T` |
| `epsilon,beta` | `A_uw in {0,1}` and `B_uw in {0,1}` after the forest premise |
| `r,h` | Local intersection sizes `|U intersect W|` and `|P intersect Q|` |
| `Z,Z_t` | The 50 remaining vertices and their eight disjoint parent classes |
| `P,Q` | Attachment sets `N_A(u) intersect Z`, `N_A(w) intersect Z` in the local note |
| `k_t,e(z)` | Integers in `{0,1,2}` counting endpoint incidences |
| `rho_t,sigma_t` | Nonnegative defect entries `B_ut,B_wt`, only in `epsilon=1` |
| `d_S(z)` | Number of original `A` neighbors of `z` in the named set `S` |
| `v_i,a_ij,E_ij` | Distinct ordered path vertices; binary adjacency entries; integer shift differences |
| `a_d,p,q,m,k` | Toeplitz coefficient; positive integer offsets; number of path edges; `k=m+1` |
| `r` in followup §3 | Integer half-length parameter, distinct local scope from intersection size `r` |
| `P` in followup §3 | The whole path, distinct local scope from the local attachment set `P` |

The scoped reuse of `r` and `P` is unambiguous. No probabilistic, limiting,
asymptotic or uniformity assertion appears.

## Dependency DAG

`I1 + I2 -> L01 -> L02 -> L03 -> L04`

`L01 + L02 + I3 -> L05 -> L06 -> L07`

`L03 + L07 -> L08 -> L09 -> {L10,L11}`

`L03 + L05 + L09 -> L12 -> L13`

`L02 + I3 -> L14; L01 + I2 + L14 -> L15 -> L16`

`I2 + L07 + I3 -> F01`

`L01 + L14 + L16 + I2 -> F02 -> {F03,F04}`

`F02 + F03 + F04 + I1 -> F05 -> {F06,F07} -> F08`

All arrows go from hypotheses or earlier arguments to later arguments;
there is no semantic or formal dependency cycle.

## Frozen micro-claim inventory

| ID | Context and goal | Rule and side conditions |
|---|---|---|
| L01 | I1 and actual definition of B imply `mu=1+B-A` for distinct pairs and `AB=BA` | Matrix entries and `AJ=JA=8J` |
| L02 | Saturated `v` row implies `A_uv=A_vw=0` and independent T | Each actual triangle supplies positive adjacent defect; two distinct common neighbors cannot fit into one permitted endpoint |
| L03 | L01–L02 imply `|U|=|W|=3`, `|Z|=50`, unique parent of each z | Pair `(v,z)` has `A=B=0`, hence exactly one common neighbor in T |
| L04 | L03 implies `B[T]=K_3[U]+K_3[W]` with zero diagonal | Partition all potential common neighbors; only v,u,w can meet two T vertices |
| L05 | Actual commutation at `(v,x)` gives local equation (5) for all x | The complete v defect row is `2e_u+2e_w` |
| L06 | `beta<=1`; `epsilon=1` implies `beta=0` and no common u,w neighbor | I3 excludes a double triangle; equation (5) spends remaining row budget at u,w |
| L07 | `r+h=1+beta-epsilon` gives exactly six necessary tuples | Full disjoint partition; nonnegative integer r,h; retain all beta-one cases |
| L08 | Parent class sizes are `7-k_t`, with multiplicities `r,6-2r,2+r` for sizes `5,6,7` | Degree eight at t; T independent; count `U intersect W`, symmetric difference and complement |
| L09 | `|P|=|Q|=5-epsilon`, overlap h | Exhaust original endpoint neighborhoods using U,W and possible uw edge |
| L10 | `epsilon=0` implies both transversal formulas (8) | Nonnegative zero defect sum; all actual common neighbors of u,t lie in `P intersect Z_t` |
| L11 | `epsilon=1` implies disjoint U,W and P,Q and formulas (9) | `mu(u,w)=0`; account for the extra common neighbor w exactly when `t in W`, symmetrically u |
| L12 | Every z has all three equations (10) | Degree partition; list actual common neighbors against x in T; use equation (5) |
| L13 | Nonexceptional z obeys equation (11); counts `40+h` or 42 | Nonnegative sum zero; inclusion–exclusion for P,Q |
| L14 | Every A-adjacent double edge is a two-vertex D component; every edge of a D path with m>=2 is an A nonedge | Apply L02 at an internal endpoint, retain isolated-edge case |
| L15 | Internal indices `1<=r,s<=m-1` satisfy recurrence (12) | Both full defect rows saturated, so no uncounted outside term in AB or BA |
| L16 | Recurrence implies all `E_ij=0`, hence symmetric Toeplitz | `r=i+1,s=j` lies inside valid bounds for `i<j`; reduce gap only for gap>=2; diagonal and gap-one bases vanish; symmetry covers lower triangle |
| F01 | `beta=1` confines the triple to a three-vertex component | Each endpoint has defect weight three already; a second double edge would require weight five |
| F02 | Nonconsecutive path vertices with at least one internal endpoint have `mu+A=1`; consecutive internal vertices have `mu=3` | Saturated internal defect row and L14 |
| F03 | Distinct selected offsets cannot satisfy `p+q<m` | Four distinct vertices `0,p,q,p+q` give two common neighbors for a zero-defect pair |
| F04 | If `p+q=m`, selected distinct offsets must differ by one | Opposite internal pair p,q has two endpoint common neighbors; distance>=2 contradicts F02 |
| F05 | Formula (3) counts the union of outside neighborhoods exactly | Each outside degree is `8-d_P`; finite inclusion–exclusion |
| F06 | For `m=2r`, centers `r,r-1` both have path degree at most two | Even m excludes the boundary exception; small offsets cannot coexist with r or r+1; both centers internal for k>=53 |
| F07 | For `m=2r+1`, centers `r,r+1` either both have degree<=2, or degree three with two known path common neighbors | The only selected small/large pair allowed is r,r+1; both endpoints are then common neighbors |
| F08 | `k>=53` is impossible, hence all components have size<=52 | F05–F07 force at least nine outside vertices; order61 leaves at most eight |

Counterexample-first review must test full overlap `r=3`, all beta-one
types, the epsilon-one extra common neighbor, exceptional vertices in
parent classes, the smallest Toeplitz path, both recurrence boundaries,
equal versus distinct offsets, the odd boundary pair, and the first
forbidden sizes 53 and 54. The audit records their dispositions.
