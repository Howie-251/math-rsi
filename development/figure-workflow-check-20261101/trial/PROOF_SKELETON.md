# Proof skeleton

Scope: every finite V, every E subset of the four-element subsets of V, with |E|<=7, has a Bool coloring taking both values on every edge.

Source extraction: all original source units in SOURCE_UNITS.json were read by executor; no extraction fanout for this 23-line input. Coverage receipt proves reading scope only.

## Symbols and hypotheses

V: arbitrary finite set. E: finite set of four-element subsets of V (simple hypergraph). m=|E|: natural number <=7. Omega={0,1}^V: nonempty finite set, uniform probability. B_e: subset of Omega whose members are constant on e. Simplicity is stated but the union argument needs only a finite indexed list. No cardinality bound on V, regularity, disjointness, or balance assumption is introduced.

## Source-ordered obligations

SU-002:OB-001: original quantified theorem above.
SU-003:OB-001: finite uniform product sample space exists, including V empty (one coloring).
SU-003:OB-002: four distinct vertices give P(B_e)=2/16=1/8.
SU-003:OB-003-original: independence of vertex colors implies mutual independence of B_e (candidate claim; requires review).
SU-003:OB-004-original: product of good-event probabilities equals (7/8)^m (depends on OB-003-original).
SU-003:OB-005: positive probability on finite coloring space supplies desired coloring.

Fix obligations when union bound replaces the product:
SU-003:OB-003-fixed: for each coloring, 1_{union B_e} <= sum_e 1_{B_e}; averaging over the finite Omega gives P(union B_e)<=m/8, with no independence hypothesis.
SU-003:OB-004-fixed: m<=7 implies 1-m/8>=1/8>0, so complement is nonempty.

## DAG and application ledger

Original: finite product space -> edge probability -> claimed event independence -> product -> positive probability -> theorem.
Repaired: finite product space -> edge probability; finite indicator inequality + edge probability + m<=7 -> union bound -> positive complement -> theorem.
Both graphs are source-directed and acyclic; original event-independence node is not accepted merely because acyclic.

Finite probability and indicator averaging are allowed foundations. All sets/functions are finite; no limiting exchange, integrability assumption, asymptotic constant, or uniformity issue occurs. Empty E yields empty union probability 0 and every coloring is admissible. If V has fewer than four elements, E is empty. No WLOG reduction, induction, classification or imported research theorem is used.
