# Order61: exactly three actual defect components are impossible

Let G be any finite simple graph with61 vertices, maximum degree at most8 and diameter at most2. Then its actual weighted defect B=A²+A−7I−J cannot have exactly three positive-support components. This is a structural restriction on arbitrary61-point targets, not their complete exclusion.

To prove the claim, first use [the unconditional quotient reduction and complete c3 classification](../../proofs/dd82/n61/GENERAL_THREE_DEFECT_COMPONENT_QUOTIENTS.md). Regularity follows from the radius-two counting bound. AB=BA makes the actual defect components equitable, giving a nonnegative integral quotient with row8, detailed balance, and Q²+Q−11I=1nᵀ. For c=3 the exact complete45³ row-sum domain leaves only the simultaneous permutation classes (6,25,30) and (12,21,28).

[The first case](../../proofs/dd82/n61/THREE_COMPONENT_6_25_30_EXCLUSION.md) forces a five-sheet cover of C6, hence R=C30; the five exact resonance calculations force25 distinct binary rows to come from only five possible words.

[The second case](../../proofs/dd82/n61/THREE_COMPONENT_12_21_28_EXCLUSION.md) has a complete calculation-free proof. Actual block equations force four-periodicity. A Rayleigh bound excludes cycles of length at least12; weighted commutation on any C8 counts the same edges as20 and16; sevenC4 would force21vertices to cover all35 Kneser labels. Every possible R case is excluded.

Both classified quotients are therefore impossible, proving the stated theorem. Full proofs and exact finite dependencies are at the linked sources; no argument is replaced by reviewer agreement. Fresh local review and actual Gemini receipts are linked in audit.md. Connected defect and component counts5,7,...,17 remain open, as do arbitrary58–61 constructions or exclusions. The project interval remains57≤N(8,2)≤61 and Lean verification remains unfinished.
