import DegreeDiameter.Portfolio.GQ77Published33CloneFamilyDefinitions
namespace DegreeDiameter.Portfolio.GQ77Published33CloneFamily
set_option maxRecDepth 20000
set_option maxHeartbeats 20000000
/-- Literal20-line block:160 incidence positions; no native computation oracle. -/
theorem line_index_chunk_10 : ∀ (j : Fin 20) (k : Fin 8),
    let l := (finProdFinEquiv (m:=20) (n:=20)) ((10 : Fin 20),j)
    ovoidOwner (OppositeGQ77Spread.linePoint l k) = none ∨
      ovoidOwner (OppositeGQ77Spread.linePoint l k) = some (lineOvoidIndex l) := by decide
#print axioms line_index_chunk_10
end DegreeDiameter.Portfolio.GQ77Published33CloneFamily
