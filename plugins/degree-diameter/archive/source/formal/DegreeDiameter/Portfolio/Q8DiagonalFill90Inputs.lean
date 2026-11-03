import DegreeDiameter.Portfolio.Q8DiagonalFill90Definitions
import DegreeDiameter.Portfolio.Q8DiagonalFill83Inputs
namespace DegreeDiameter.Portfolio.Q8DiagonalFill90
theorem load_le (v : Source.Vertex) : FullNeighborhoodClones.load Source.graph center v≤8 := by
  unfold FullNeighborhoodClones.load
  let copyIndex : {x : CopyIndex // Source.graph.Adj v (center x)} → Fin 8 := fun x => x.val.1
  have hinj : Function.Injective copyIndex := by
    intro x y h
    apply Subtype.ext
    have hb : x.val.1=y.val.1 := h
    have hr : x.val.2=y.val.2 :=
      Q8DiagonalFill83.adjacent_roles_unique v x.val.2 y.val.2 x.property y.property
    exact Prod.ext hb hr
  simpa only [Fintype.card_fin] using Fintype.card_le_of_injective copyIndex hinj
#print axioms load_le
end DegreeDiameter.Portfolio.Q8DiagonalFill90
