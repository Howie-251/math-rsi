# Unified higher-hole transfer: independent proof review

2026-11-01. ARIS proof-checker. Fresh reviewer task
`/root/higher_hole_transfer_audit`; user-requested `gpt-6.1-sol`, reasoning
`high`, overrides the skill's default model. Assurance: **same-family / provisional**.

**PASS relative to the explicit established local imports.** Sections 1--3
prove a conditional transfer for every original short matching realizing the
stated independent-hole geometry. All eleven unconditional cut rows in
Section 4 have the stated local inputs: eight for ten holes and three for
twelve holes, including both free and covered targets. The four marked-T15
rows remain conditional on their actual marked projected geometry.

This review does **not** prove any complete 10,12,14,16,18-hole layer or
full P6, nor unrestricted Q5 T15. The parent's new geometry enumeration is
outside this audit. Production proofs and the main ledger were not edited.

## Input and imported scope

The theorem-bearing input is `HIGHER_HOLE_UNIFIED_TRANSFER.md`, SHA256
`75f481593ecff17f888102e687c0c669f8dd96cdd5ce953434fb93de644df0ed`.
The JSON sidecar fixes this hash separately from imported dependency hashes.

The local balanced endpoint lemma is Section 1 of
`EIGHT_HOLE_CONDITIONAL_REDUCTION_DRAFT.md`. Its A6 assumption is discharged
by `A6_CLOSURE_REVIEW.json`; the exact K6 consequence is also recorded in
`A6_AND_EIGHT_FREE_CLOSED.md`. The balanced 0,2,4,6-hole cycle theorems and
the 0+2,1+3,2+4 omit-one theorems apply to **arbitrary K(Q5) matching edges**.
The precise T44_5 statement and its PASS review likewise allow long and
same-parity edges and **any prescribed pair** of four same-parity holes.
Thus arbitrary artificial pairs and compressed edges are within scope.
Global and local face parities may reverse together under face coordinates;
the inputs have both parity orientations by cube translation.

The established five-direction endpoint theorem is an explicit external
import for c=0. No proof of any higher-hole P6 statement is used. The complete
eight-hole package is accepted as a fixed preceding input, without rerunning
its large certificates. Six selected import reports are PASS, and seventeen
recorded hashes of the relevant source files were independently compared
with their current bytes; all agree. Earlier draft warnings are historical,
not replacements for the later accepted import statements.

## Quantifiers and dependency order

For every k, original short M, free even u, opposite-parity target v, and
coordinate cut with v in A, assume Z union W independent. If c=0, use the
five-direction import. If c>0, assume either branch's explicit numerical and
selection conditions and the exact B cycle input for every arbitrary
matching on the complement of its marked hole set. Then a Hamilton u--v
extension of M exists with only short new edges.

The dependency graph is local endpoint imports -> A path -> tagged transfer
matching -> simultaneous suppression -> specified B import -> expansion.
The table instantiates the final import with established cycle theorems.
There is no reverse dependency on this transfer or on higher-hole P6.
Independent-hole preprocessing for a whole layer would additionally need
the complete predecessor layer. In particular this is available from eight
to ten holes, but cannot be silently used from unproved ten to twelve holes.
The draft correctly keeps independence a hypothesis throughout.

## Proof-obligation ledger

| ID | Obligation and discharge | Result |
|---|---|---|
| U01 | Short internal M_A gives port imbalance p_E-p_O=b-a-delta and c congruent to a+b+delta modulo2. These identities hold before adding arbitrary D. | PASS |
| U02 | Even consumption s=a+1-b satisfies 0<=s<=a because b>=1. Z vertices are distinct free even vertices; S is disjoint from all ports and v. | PASS |
| U03 | For delta=1, pairing X_A union S is even and leaves exactly b even and b odd holes, including u. | PASS |
| U04 | For delta=0,s>=1, leave r in S unpaired. X_A union (S minus r) is even and leaves exactly b+b holes with r even/free. No port parity requirement is imposed here. | PASS |
| U05 | For delta=0,s=0, port imbalance is1, so an even port r exists. Pairing the remaining ports leaves b+b holes. | PASS |
| U06 | Odd consumption has b-t=a+1. A covered target excludes no hole and bar(u) excludes at most one. A free target excludes at most two holes; a>=1 suffices. The remaining a=0 case is only claimed under the explicit S-existence hypothesis. | PASS |
| U07 | In odd consumption delta=0, p_E-p_O=t+1>0 supplies an even port. In either root face D has even pairing-set size and the resulting holes are exactly (a+1,a+1). | PASS |
| U08 | M_A+D is a matching because all D endpoints were free for M_A; D may be any pairing, including long and same-parity edges. The root is even and free, the target odd and outside S. The balanced endpoint import applies with2,4,6 holes. | PASS |
| U09 | In both branches a bridge mirror is not an original nonroot hole by independence, not u by parity or explicit exclusion, and not a crossing port because its mirror is originally free. Thus it is internally M_B-covered. Mirrors are distinct. | PASS |
| U10 | Delete D from the simple A path, then attach crossings and bridges at distinct B vertices. Every cut D endpoint gets one attachment. If r is a port or S vertex, its attachment makes it internal; if r=u it remains terminal. The target remains terminal even if it was a crossing port isolated by deleting its D edge. | PASS |
| U11 | If u in A, c>0 and the even pairing set force D nonempty; deleting any such path edge separates u,v. Adding tag uv joins different components. If u in B, u was untouched and tag extends the v component to u, including D empty. Hence no cycle is created. | PASS |
| U12 | After tagging every component is a path with two distinct B endpoints, each of degree1. Compress to a matching T with endpoint set X_B union Y and additionally u iff u in B; exactly one component carries the tag. | PASS |
| U13 | Conflicts of T with M_B are exactly Y. Each original mate h_y is distinct and opposite in parity to Y, and is neither a port nor a free root. Therefore h_y is outside all T endpoints. | PASS |
| U14 | A T edge can join two members of Y. Its conflict component is h_y--y--y'--h_y', not a cycle. All other nontrivial conflicts are h_y--y--z. This exhaustive classification proves simultaneous suppression gives a matching, distinct endpoints and a uniquely retained tag. | PASS |
| U15 | Vertices formerly free in M_B are exactly H_B union X_B. T covers every X_B and the B root. Suppression uncovers exactly Y. Thus L holes are (H_B minus {u}) union Y, with u removed only in B, giving exactly the two displayed B count formulas. | PASS |
| U16 | Every specified omitted vertex Y is a hole of L. The B input is required for the actual marked holes, for every arbitrary complete-graph matching; it therefore applies to the constructed L. | PASS |
| U17 | Replacing the L edges on one simple B cycle by their disjoint recorded paths preserves one simple cycle and restores exactly Y and all A vertices. Every original M_A,M_B,crossing edge survives. The unique tag can then be deleted to give the prescribed u--v path. | PASS |
| U18 | No completion D edge survives. Compressed edges are expanded; apart from original M the surviving edges are local new short edges and chosen short bridges. Even if some compressed edge is geometrically short, expansion is determined by its recorded required-edge identity. | PASS |
| U19 | Independent computation verifies all eleven established table rows and four conditional T15 rows. Both root-face positions cancel from the final B counts. All odd-consumption established rows have a>=1. | PASS |
| U20 | No exhaustive higher-hole cut coverage is asserted. The marked T15 condition is an exact additional hypothesis; neither the count (1,5)/(5,1) nor a prior eight-hole core census alone discharges it for a new geometry. | PASS |

## Boundary and counterexample pass

The independent checker is `HIGHER_HOLE_UNIFIED_TRANSFER_REVIEW_check.py`;
its reproducible output is the adjacent `_check.json`.

* It verifies 9,718 feasible parity-population branch instances with
  1<=k<=32, each face having16 vertices per parity and original internal
  edges short. These include48 D-empty instances. The genuine boundary is
  delta=0,s=0,c=1; tagging still gives one transferable path. D-empty with
  u in A cannot occur under c>0.
* It exhaustively checks14,450 abstract path/deletion/attachment/conflict
  configurations on A paths of4 through10 vertices, allowing D to touch
  the target but never the free A root. This includes8,772 target-port
  cases,8,428 tag-incident conflicts and8,316 cases with two Y endpoints
  on one transferred edge. These counts overlap.
* Each configuration is independently compressed, conflicts suppressed,
  closed by a constructed cycle containing L, expanded and untagged.
  Connectedness, exact endpoints, degrees, restored A/Y vertices and all
  modeled original edges are checked. All pass. The abstract Y placements
  include patterns impossible under same parity, which only strengthens
  this finite topology check.
* Counterexample candidates considered analytically: D empty; v a crossing
  port; free v accidentally consumed; bar(u) selected as bridge mirror;
  Y--Y transferred edge; a tag inside a double conflict; duplicate h_y;
  a conflict cycle; unrestricted-T15 substitution. The first, second and
  Y--Y/tag boundaries are valid and covered; other candidates violate an
  explicit hypothesis or the matching/parity invariant. No counterexample
  was found.

The finite checks supplement the universal forest argument in U10--U18;
they are not exhaustive enumeration of Q6 matchings or higher-hole geometry.
There are no limit interchanges, probability assertions or asymptotic
uniformity obligations in this finite combinatorial proof.

## Decision and remaining obligations

All twenty listed obligations pass, with no open FATAL, CRITICAL, MAJOR or
MINOR issue in the submitted scope. No proof fix was required. The eight
ten-hole and three twelve-hole cut classes are valid for both covered and
free opposite-parity targets, relative to the imported local theorems.

Full10-hole coverage, full12-hole coverage,14--18-hole coverage, predecessor
preprocessing where still unavailable, exact marked-T15 membership for any
new use, and full P6 remain unproved by this document. These are limits of
the claimed result, not omitted obligations of its conditional transfer.
