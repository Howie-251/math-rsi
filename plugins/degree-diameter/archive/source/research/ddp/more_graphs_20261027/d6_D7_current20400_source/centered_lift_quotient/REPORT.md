# Every larger modulus fails for this fixed centered voltage recipe

The actual recovered source has48 base vertices with six explicitly reversed ports, using abelian deck coordinates F5²×C17. The source scout bound all source edges to that recipe; this agent reused its fixed basis and section. No graph or automorphism recovery was repeated.

Replacing each c17 coordinate by its centered integer in[−8,8] and then reducing modulo m≥18 defines an undirected simple degree6 lift, as proved in MODEL_NOTES.md. The retained deck translations give48 source representatives. The old complement action need not survive; connectedness of a changed graph is not assumed.

## Complete route data

At each representative, every named nonbacktracking word of length0 through7 was enumerated. Inverse ports were taken from the actual per-dart reverse map, not guessed global symbol pairs. There are117187 words per root,5624976 total. Forgetting the scalar coordinate gives1200 projected states. Their raw route count minimum is66, so the frozen prediction that raw capacity permits18 and19 is supported.

In the same traversal, the scalar endpoint is the ordinary integer sum of centered port values, in[−56,56]. For every one of57600(root,projectedtarget) slots, the complete set X was persisted. These integer supports are independent of the new modulus. Immediate inverse backtracking deletes without changing a voltage endpoint, so X modulo m is the exact length-at-most-seven reachable scalar set, rather than just a sufficient screen.

The initial exact tests already rejected m18 and19. Root0 misses37 and68 targets respectively; sums over all48 representative-root target lists are2004 and3720. These are representative counts, not ordinary unordered graph bad pairs. No actual graph or BFS was generated to obtain them.

## Derived cap and exhaustive larger-parameter decision

The smallest integer support has K=23. One literal witness is rootbase0 to targetbase37,a4,b1, with scalar endpoint set

    {−17,−11,−10,−8,−7,−6,−5,−4,−3,−2,−1,0,1,2,3,4,5,7,8,9,10,11,16}.

No modulus above23 can cover its entire cyclic fiber, since reduction cannot increase cardinality. Thus all larger-than-source orders reduce to the finite range18≤m≤23, rather than an open-ended modulus search.

The admissible-modulus list is empty. The m18/19 negatives were inherited from the first exact calculation. First root0 failures for the remaining cases are:

- m20: targetbase0,a1,b0, scalar12 missing;
- m21: targetbase0,a1,b1, scalar11 missing;
- m22: targetbase0,a0,b0, scalar11 missing;
- m23: targetbase0,a1,b0, scalar15 missing.

Each failure has its entire supporting X in RESULT.json. Larger moduli are excluded by the23-element witness. Therefore every m>17 fails diameter≤7 for **this fixed recovered basis, section, F5² voltages and centered integer choice**. No conclusion is made about different gauges, other integer representatives, changed base/voltages or arbitrary graphs at(6,7).

## Artifacts and actual cost

The full supports are endpoint_scalar_masks.u128le.bin:57600 little-endian128-bit masks, root-major; projected index is25·base+a+5b, and bit(c+56) records c. SUPPORTS.json gives the cap witness and layout. supports.cpp computes the supports; decide.py reproduces the finite residue decision. RESIDUE_DECISION.json is the saved decision.

The initial quotient/scalar pass cost0.070223 native CPU seconds,1.299940586 including compilation. The authorized support persistence and complete cap-bounded decision cost0.052561 native support CPU seconds,1.198228144 including compilation and residue checks. No new graph, BFS, sourceD7 recheck, parameter gauge change, or further modulus was performed. Exact global diameters and ordinary bad-pair totals remain unspecified. The family is closed in the stated scope and the task is terminal.
