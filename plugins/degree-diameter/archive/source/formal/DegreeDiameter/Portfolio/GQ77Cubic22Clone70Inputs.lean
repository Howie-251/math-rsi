import DegreeDiameter.Portfolio.GQ77Cubic22Clone70Definitions
import DegreeDiameter.Portfolio.GQ77Cubic22Clone65Inputs
namespace DegreeDiameter.Portfolio.GQ77Cubic22Clone70
set_option maxRecDepth 20000
set_option maxHeartbeats 20000000
/-- The copy coordinate distinguishes all adjacent clones, since at most one base center
is adjacent to any original source vertex. No center independence or injectivity is assumed. -/
theorem load_le_six (w : Source.Vertex) : FullNeighborhoodClones.load OppositeGQ77Spread.graph center w ≤ 6 := by
  have hbase : ∀ x y : {b : Fin 1100 // OppositeGQ77Spread.graph.Adj w (GQ77Cubic22Clone65.center b)}, x = y :=
    Fintype.card_le_one_iff.mp (GQ77Cubic22Clone65.load_le_one w)
  let copyIndex : {k : CloneIndex // OppositeGQ77Spread.graph.Adj w (center k)} → Fin 6 :=
    fun k => (clonePair k.val).1
  have hinj : Function.Injective copyIndex := by
    intro x y hcopy
    have hbaseval : (clonePair x.val).2 = (clonePair y.val).2 :=
      congrArg Subtype.val (hbase ⟨(clonePair x.val).2,x.property⟩ ⟨(clonePair y.val).2,y.property⟩)
    apply Subtype.ext
    apply clonePair.injective
    exact Prod.ext hcopy hbaseval
  have hcard := Fintype.card_le_of_injective copyIndex hinj
  simpa only [Fintype.card_fin] using hcard
#print axioms load_le_six
end DegreeDiameter.Portfolio.GQ77Cubic22Clone70
