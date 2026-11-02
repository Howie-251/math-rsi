# The 1+5 two-fiber mechanism and a candidate-preserving C6×A4 reduction

Date: 2026-10-26. Mathematical derivation by the source subagent; independent review and Lean are not yet performed. The finite output is an exact exhaustive exploratory computation with its scope below, not a formal certificate or general nonexistence theorem.

## 1. Exact short-walk condition

Let `a,b` be involutions in a group `G`, and let `T` contain five distinct elements. Internal edges in fibers 0 and 1 multiply on the right by `a` and `b`; cross edges multiply by `T` in direction 0→1. Let `C=TT^-1`, `C1=T^-1T`.

All vertices in the starting fiber reachable in at most three steps have group labels

```
W00 = C ∪ aC ∪ Ca ∪ T b T^-1,
W11 = C1 ∪ bC1 ∪ C1 b ∪ T^-1 a T.
```

The identity is already in `C,C1`, and `a,b` are already in `aC,bC1`, so zero- and one-step walks are included. Any length≤3 same-fiber walk has either zero or two cross edges; the three placements of the internal edge give precisely the final three terms.

The opposite-fiber labels from root 0 are

`W01=T ∪ aT ∪ Tb ∪ aTb ∪ TT^-1T`.

The reverse set is `W10=W01^-1`, by reversing walks. Thus diameter≤3 is equivalent to `W00=W11=W01=G`. This is an equality of group-element sets, not just path counts or an abelian quotient test.

## 2. The naive C_m×A4 extension is impossible for m≥6

Suppose `G=C_m×A4` and both involutions have central coordinate zero, so `a,b∈{0}×V4`. Project `A4→A4/V4=C3`; write the cross voltages as `s_i=(z_i,p_i)` for five indices.

Fix a nonzero central displacement `r∈C_m`. Every same-fiber walk of length≤3 that reaches this displacement uses exactly two cross edges, hence comes from an ordered pair `(i,j)`, `i≠j`, with `z_i-z_j=r`. The possible outputs of this pair in `W00` are

`x, ax, xa, s_i b s_j^-1`, where `x=s_i s_j^-1`.

All four have the same `C3` quotient `p_iV4-p_jV4`. If that quotient is zero, `x∈C_m×V4`, hence `ax=xa`; the pair gives at most three of the four elements in that quotient fiber. At least two ordered pairs are needed for this `C3` class. Each of the other two `C3` classes also needs at least one pair. Therefore each nonzero `r` requires at least four ordered pairs. Only `5×4=20` are available, so `4(m−1)≤20`.

For `m≥7` this is impossible. For `m=6`, equality forces every one of the 20 off-diagonal ordered pairs to have nonzero central displacement, so the five `z_i` are distinct. Then for central displacement zero only pairs `i=j` are available. Their outputs and the zero-cross walks all have `A4` component in `V4`, missing every 3-cycle. Hence `m=6` is also impossible.

This proof applies only to the 1+5 degree allocation with both internal involutions in the `A4` factor. It does not exclude other groups, other degree allocations, or a half-turn in an even cyclic factor.

## 3. C6×A4: central involutions can also be eliminated

Every nonidentity involution has the form `(alpha,v)` with `alpha∈{0,3}`, `v∈V4`, and not both identity. If `a=(3,e)` is central, then `aC=Ca` and

`|W00| ≤ |C|+|aC|+|TbT^-1| ≤21+21+23=65<72`.

Here `|C|≤1+5×4=21`; in `TbT^-1` the 20 off-diagonal ordered pairs give at most20 elements, while the five diagonal terms are conjugates of `b`. Any involution in `C6×A4` has at most three conjugates (a central one has only one), so that term has size≤23. If `b` is central, apply the same argument to `W11`.

Consequently both V4 components must be nonzero. Their cyclic components give cases `(alpha,beta)=(0,0),(0,3),(3,0),(3,3)`. The first is excluded by §2; exchanging the two base vertices sends `(3,0)` to `(0,3)` and replaces `T` by `T^-1`, so it suffices to consider `(0,3),(3,3)`.

## 4. Exact normalizations and finite input scope

Choose any cross voltage `s0∈T`. Relabel type-1 coordinates by `h_new=h_old s0^-1`, leaving type0 unchanged. Then

`T_new=T s0^-1`, `b_new=s0 b s0^-1`, `a_new=a`.

This makes one cross voltage the identity and preserves both cyclic involution coordinates and the fact that their V4 components are nonzero. Then simultaneously conjugate all group labels by a suitable order-three element of `A4`. Its conjugation cyclically permutes the three nonzero elements of `V4`, so the V4 component of `a` can be fixed to one chosen value. The identity cross voltage stays the identity. `b` still ranges over all three nonzero V4 elements; it is not held to the original source's value.

Project to `Q=C6×C3`. The five cross voltages project to a **multiset** containing `0`; projected repeats are allowed. Remove one chosen occurrence of0 and enumerate the remaining four projected values in nondedecreasing order from the18 elements. A quotient fiber has four lifts, so multiplicity>4 is disallowed. This gives 5984 normalized projected multisets for each cyclic pair. Relabeling the five cross edges has no mathematical effect, so sorting loses no candidates. If zero occurs several times, one of its actual lifts is the normalized identity; the other lifts are independently enumerated below.

## 5. Necessary capacity filter

For an enumerated projected multiset let

`c(q)=#{(i,j): q_i-q_j=q}`,

including the five diagonal pairs at `q=0`. Put `A=(alpha,0)`, `B=(beta,0)` in `Q`. We upper-bound, for each `q`, the number of distinct outputs of the four terms of `W00` in that quotient fiber (which must contain all four V4 values).

- `C` contributes at most `c(q)-4[ q=0 ]`: five diagonal products are all identity.
- If the C3 component of `q` is zero, `aC=Ca` at this quotient, since `a` commutes with every element of `C6×V4`; their union contributes at most `c(q-A)-4[ q=A ]`.
- If the C3 component is nonzero, use the valid looser bound `2c(q-A)` for those two terms.
- `TbT^-1` contributes at most `c(q-B)-2[ q=B ]`: the five diagonal conjugates of `b` have at most three possible values.
- When `A=B`, at quotient `q=A` the diagonal contribution `a` and the diagonal conjugates of `b` together lie among the same three nonzero V4 values. The separate bounds counted at most1+3, so subtract one more.

Call the resulting upper bound `U(q;A,B)`. Necessity is `U(q;A,B)≥4` for all18 quotients. For `W11`, the projected difference counts for `T^-1T` are `c(-q)=c(q)` after exchanging ordered pair indices; hence the second necessary condition is `U(q;B,A)≥4`. There is no claim that these conditions suffice.

`central_halfturn_profile.py` implements exactly these formulas. It leaves zero multisets for `(0,0)` and30 for each of `(0,3),(3,3)`. The zero result is consistent with, but unnecessary for, the paper proof §2. All surviving input multisets are in `central_halfturn_profile.json`.

## 6. Exact completion of surviving lifts

Represent `A4=V4⋊C3` by `(v,t)`, with `v∈{0,1,2,3}` under bitwise XOR and the C3 generator rotating `1→2→3→1`. The implementation uses `(r,t,v)` and multiplication

`(r,t,v)(s,u,w)=(r+s mod6,t+u mod3,v XOR R^t(w))`.

For each surviving quotient multiset, set the first cross lift to identity and independently try all `4^4=256` V4 components of its other four cross voltages. Reject actual repeated voltages. Fix `a=(alpha,0,1)` by §4 and enumerate `b=(beta,0,vb)` for `vb=1,2,3`. Compute `W00,W11` exactly using the full multiplication table; if both are full, compute `W01` too.

This covers `30×256×3=23040` assignments in each cyclic case, 46080 total. `complete_c6_a4.py` completed in approximately one second on one CPU, with no full solution. The best sum `|W00|+|W11|` was138/144, with69 elements covered in each fiber, in both cases. Exact best examples and counts are in `c6_a4_complete_result.json`.

Interpretation: subject to independent checking of this candidate-preserving reduction and the finite implementation, the full **C6×A4, 1+5 bi-Cayley family** is excluded at order144. It does not exclude the root's other 64/66/68/70/72-order groups, the2+4 degree allocation, or arbitrary144-vertex degree-six graphs. It gives a concrete reason to stop unchanged1+5 C6×A4 annealing; formal certification is not needed merely to pause a search family.
