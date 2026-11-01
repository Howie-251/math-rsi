# T34: formal six-lock selection at 23 vertices

2026-10-13. Three modules compile; the independent raw-edge selection caller
and eight transitive-axiom queries pass. This proves the selection and
extension interfaces, not the entire 23-point coloring theorem.

- `WeightedSubsetSelection.lean`: minimum six-subset existence, exact swap
  balance, `(r−7)d+E≤30`, internal degree≤3, E≤12, degree3⇒E≤8, and equality
  saturation r=14 / selected vertices use their full weight inside L.
- `WeightedSubsetExtension.lean`: one actual y outside S has internal weight
  ≤4 when E≥4, and ≤3 when E≥6, together with all swap inequalities for the
  same y.
- `TwentyThreeSevenSelection.lean`: actual H23 with 34 edges and minimum
  degree seven supplies ≥14 seven-degree points and the required weighted
  degree six; `actual_minimum_six` applies the generic selection. When E=12,
  `equality_degree_eight_lock` supplies an actual degree-eight point outside
  S with codegree one to every selected vertex.

The last bridge does not need the stronger global two-K7 theorem. The even
energy argument also avoids averaging over all six-subsets. Full derivation
and why the unchanged 209-entry equality table still applies are in
`LEAN_SELECTION_SIMPLIFICATION.md`.

The unique official builder ran the actual targets. Generic subset build:
`../twentyone-lean/build-queue-WeightedSubsetSelection-r5.log` (905 jobs).
Actual H selection: `../twentyone-lean/build-twenty-three-r7.log`
(910 jobs). Extension build succeeded in the same serial queue. Independent
`SelectionAudit.lean` ran with exit0, saved as `selection-audit.log`; all eight
queries contain only propext, Classical.choice, Quot.sound. The audit starts
one caller from a raw Finset of five-element edges and proves actual lock
selection. It does not claim a raw-H coloring conclusion yet.

Still required: strong-codegree actual branch, full local trace classification
and promotion/projection coverage, retained strict probability callers, and
all original-H case assembly. Final T34 Main and final C review remain open.
