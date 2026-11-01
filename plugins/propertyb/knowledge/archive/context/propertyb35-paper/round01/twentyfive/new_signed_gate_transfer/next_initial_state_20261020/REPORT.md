# A fixed initial-state obstruction to simultaneous low-point repair

The investigation stopped at the root agent's direction to prioritize the strengthened eight-positive gate. No new initial-state normalization or unconditional three-low theorem was obtained.

Use the frozen actual core15 realization in `../../MIXED_THREE_SIX_UNIT8_REALIZATION.json`, with lows $K=\{0,1,2\}$ and common edge $G=\{0,1,2,3,4\}$. Initially color precisely

$$B=\{5,6,7,10,13,15,19,20\}$$

blue and all other points red. Direct inspection verifies that $H-G$ is proper. This is a fixed actual coloring, not a proposed new optimizing rule. No claim is made that every possible initial coloring has the following obstruction.

The all-blue positive block through low0 is

$$A_0=\{5,10,15,20\},$$

and that through low1 is

$$A_1=\{7,13,19,20\}.$$

Low2 has no all-blue positive block. The zero-low edge family has singleton-blue points

$$F_0=\{5,10,13,19,20\}.$$

When both lows0 and1 are flipped blue, any repair that only turns original blue points red must hit both $A_0,A_1$ and avoid $F_0$. It therefore must turn both15 and7 red. But the actual zero-low edge

$$\{3,7,11,15,24\}$$

has initial blue part exactly $\{7,15\}$. It would become entirely red. Flipping low2 as well does not change this edge, so the same obstruction persists. Thus flipping several low centers can remove their private-star blockers while leaving a common zero-low singleton/pair obstruction. It does not automatically produce a repair.

This example is colorable: flipping low2 alone, with no exterior change, already repairs $H$. The witness refutes only the assertion that adding the other two low flips automatically resolves an initial private-star blockage. It is not a counterexample to Property B, existence of a suitable initial coloring, or a general three-low theorem.

[CHECK.py](CHECK.py) verifies the fixed source and saves actual singleton witness edges. It also checks all seven nonempty low-flip subsets and all256 exterior recoloring subsets for each, with exact output [CHECK.json](CHECK.json): `PASS`. No initial-state minimization is used by this verification.

For a general fixed proper $H-G$ coloring and a selected subset $S\subseteq K$ of lows flipped blue, the exact common interface keeps all zero-low blue parts as negative constraints. Each flipped low contributes its all-blue four-blocks as positives; each unflipped low contributes its nonempty blue star parts as negatives. All the low centers share the **same** negative zero-low family and exterior repair set. Any proposed simultaneous repair must control that common family, including its singleton and pair constraints. The three unit partitions alone do not remove it.

The prior report's degree observation also persists: with all three lows blue, an active point $x\in V-G$ has signed occurrence

$$a_x+d_{H_0}(x)=a_x+d_H(x)-3,$$

before inactive negatives are removed. For seven-degree points this is at most seven, but a high point needs an explicit compensation or exclusion. Neither the common-zero-low obstruction nor the high-point cap has been resolved uniformly here.
