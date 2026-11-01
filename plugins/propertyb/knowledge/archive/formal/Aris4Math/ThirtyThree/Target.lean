import Aris4Math

/-!
# The next Property B target

This proposition uses the unchanged hypergraph and coloring definitions from
the original project. It is a target declaration, not a proof of the target.
-/

namespace Aris4Math

universe u

/-- Every finite simple five-uniform hypergraph with at most 33 edges has
Property B. There is no vertex-count or pair-covering hypothesis. -/
def Target33 : Prop :=
  ∀ (V : Type u) [Fintype V] (H : Simple5Hypergraph V),
    H.edges.card ≤ 33 → PropertyB H

end Aris4Math
