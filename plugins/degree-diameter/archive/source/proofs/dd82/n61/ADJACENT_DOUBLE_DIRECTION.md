# Order61 adjacent double defects: a new actual-graph obligation

Run: dd82-v3-adjacent-doubles61-20261013. This is distinct from the completed
triple-defect and connected-component mechanisms, not a reset of either.
The parent goal remains actual graphs or full exclusions at58–61.

## Inherited facts and target

Every arbitrary order61 maximum-degree8 diameter2 graph is8-regular and
has actual B=A²+A−7I−J connected, nonnegative integral, zero-diagonal,
row sum4, and entries0,1,2. CONNECTED_TRIPLE_EXCLUSION.md is the accepted
source with explicit finite-enumeration and checked-CNF imports. Do not
repeat its computation or certificate check.

The new target is whether an actual A edge uv can have B_uv=2, equivalently
whether an original edge can belong to two triangles. A complete exclusion
would give lambda(u,v)≤1 on every original edge, a general order61 result;
a SAT result must give a full original target graph. Nonadjacent double
defects and the whole order61 problem are not thereby excluded. No
triangle-free assumption or equitability of row types is made.

## Concrete new reduction being finished

For an adjacent double pair uv, its two common neighbors s,t and the
row-four budgets force Bu=2v+s+t and Bv=2u+s+t. The pair st is not an
A edge. B_st=2 would close a proper four-vertex defect component, so
B_st=1, Bs=u+v+t+p and Bt=u+v+s+q. The new draft
ADJACENT_DOUBLE_REPEAT_LOCAL.md derives the positions p in T and q in S
and the entire original61 partition

```text
{u,v,s,t}, U5, V5, S6, T6, Z35.
N(u)={v,s,t}+U; N(v)={u,s,t}+V;
N(s)={u,v}+S; N(t)={u,v}+T.
```

Here S,T are the external neighborhoods of s,t, not the pair{s,t}.
U,V,S,T are independent; U–V and U/V–S/T have no A edges. Each Z point
has exactly one neighbor in U,V,S,T and four Z neighbors. U/V points
have seven Z neighbors; ordinary S/T points have six, q/p have five.
The S/T interface has seven edges, with degree2 precisely at q and p,
and all other degrees1. These are actual-A necessities under local
proof review, not assumptions to be imposed without a proof.

The cross-defect C=B[U,V] is a5×5 nonnegative integer matrix with row
and column sums2. Every Z point belongs to a unique(U,V) cell, and
its cell sizes are H=C+J. Thus all25 cells are nonempty and their sizes
sum35. This permits a complete, small original-graph representation.

## Seven C types without choosing an artificial symmetry

View C as the incidence matrix of a2-regular bipartite multigraph on
five U and five V labels. Its components are even cycles, including
a pair of parallel edges as a cycle of length2. Alternating colors
split the edges into two perfect matchings. Independently relabeling
U and V puts one matching at I, so C=I+P_sigma. Permuting the components
and cycle labels makes sigma a canonical permutation whose cycle
lengths partition5. The seven partitions are

`5;4+1;3+2;3+1+1;2+2+1;2+1+1+1;1+1+1+1+1`.

This classification covers all C under independent row/column labels.
It is legitimate here because A[U,V] is empty and no U/V identity
matching is fixed. It must not be confused with the preceding triple
model, where an actual U/V matching forbade independent permutations.

For each C, label the35 Z points by their actual(U,V) cells of sizes
C_ij+1. A single model can retain all seven C types with case selectors,
and seven separately covered inputs are another option. Do not also
force q's Z-neighbor transversal to be an identity matching: that would
reuse the same V label freedom. Leave S/T maps and internal Z edges
free except for proved necessary conditions. SAT decoding retains all
original61 vertices and every real degree/path condition.

## Auxiliary double-support fact

DOUBLE_DEFECT_CYCLE_OBSTRUCTION.md gives a short independent pure proof
that D={B_uv=2} is a path forest. A D-cycle would saturate its vertex
rows and, by connectedness, force B=2A(C61). The odd-cycle commutant
with constant diagonal forces actual A circulant, whose two-step ball
with degree8 has at most41 vertices. This supports the remaining domain
but is not an unproved assumption or an automatic type-equitability
statement. Its local/external proof reviews are pending at preparation.

## Direction decision and concrete execution boundary

The adjacent-double case is selected because it already determines all
61 vertex layers and a complete seven-type interface, allowing actual
graph completion rather than another unbounded local case chain. It
does not inherit an excluded core or fixed quotient from old58–60
construction searches, and it introduces no automorphism restriction.

Next: review the actual new local/cycle proofs and seven-type coverage;
prepare a full original61 CNF, retaining all seven cases and all1830
real path pairs; run one bounded profile with the existing solver and
independent model/certificate checks. Use the result in the same Gemini
thread to decide any mathematically substantive revision. UNKNOWN is
not an exclusion or authorization for an unchanged cold restart.
At most four substantive reviews, preserving full raw memory. No new
CLI, old Lean, frozen n62/63–65 work, hashes or paper scoring.
