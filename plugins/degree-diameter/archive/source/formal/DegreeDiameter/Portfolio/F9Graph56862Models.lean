import DegreeDiameter.Portfolio.F9Graph56862RouteData
import Mathlib.Data.Fintype.EquivFin
namespace DegreeDiameter.Portfolio.F9Graph56862
set_option maxRecDepth 30000
set_option maxHeartbeats 100000000
def modelData : Array (Array Nat) := #[#[1, 0, 0], #[1, 0, 2], #[1, 0, 3], #[1, 0, 4], #[1, 0, 6], #[1, 2, 0], #[1, 2, 1], #[1, 2, 2], #[1, 2, 5], #[1, 2, 6], #[1, 3, 0], #[1, 3, 1], #[1, 3, 3], #[1, 3, 4], #[1, 3, 7], #[1, 4, 0], #[1, 4, 1], #[1, 4, 2], #[1, 4, 3], #[1, 4, 6], #[1, 6, 0], #[1, 6, 1], #[1, 6, 2], #[1, 6, 3], #[1, 6, 4], #[0, 1, 1], #[0, 1, 3], #[0, 1, 4], #[0, 1, 6], #[0, 2, 2], #[0, 2, 5], #[0, 2, 7], #[0, 3, 1], #[0, 3, 3], #[0, 3, 7], #[0, 4, 0], #[0, 4, 1], #[0, 4, 2], #[0, 4, 3], #[0, 4, 6], #[0, 6, 0], #[0, 6, 2], #[0, 6, 3], #[0, 6, 4], #[3, 0, 0], #[3, 0, 4], #[3, 0, 7], #[3, 1, 2], #[3, 1, 7], #[3, 2, 0], #[3, 2, 2], #[3, 2, 7], #[3, 5, 2], #[3, 5, 6], #[3, 6, 3], #[2, 0, 0], #[2, 0, 2], #[2, 0, 3], #[2, 1, 2], #[2, 1, 5], #[2, 1, 7], #[2, 3, 5], #[2, 3, 6], #[4, 0, 2], #[4, 0, 7], #[4, 1, 3], #[4, 1, 5], #[4, 1, 7], #[4, 2, 2], #[4, 2, 4], #[4, 3, 4], #[5, 3, 3], #[1, 6, 5], #[0, 2, 6], #[0, 6, 5], #[1, 4, 7], #[2, 1, 6], #[3, 0, 5], #[4, 2, 5], #[0, 4, 7], #[1, 2, 7], #[1, 3, 5], #[4, 1, 4], #[3, 7, 3], #[2, 3, 7], #[1, 0, 5], #[1, 0, 7], #[1, 2, 4], #[1, 3, 6], #[1, 7, 0], #[1, 7, 1], #[1, 7, 2], #[1, 7, 3], #[1, 7, 4], #[0, 2, 0], #[0, 2, 1], #[0, 2, 4], #[0, 7, 2], #[0, 7, 3], #[0, 7, 4], #[3, 0, 2], #[3, 0, 3], #[3, 1, 5], #[3, 2, 4], #[3, 2, 6], #[3, 4, 2], #[3, 7, 1], #[3, 7, 4], #[2, 1, 3], #[2, 1, 4], #[2, 3, 0], #[2, 3, 1], #[2, 3, 4], #[2, 4, 0], #[2, 4, 1], #[2, 4, 2], #[2, 4, 3], #[2, 4, 6], #[2, 6, 2], #[4, 0, 0], #[4, 0, 6], #[4, 2, 0], #[4, 2, 1], #[4, 2, 7], #[4, 3, 0], #[4, 3, 1], #[0, 5, 2], #[0, 5, 7], #[4, 2, 6], #[3, 1, 6], #[1, 5, 2], #[1, 5, 7], #[2, 4, 7], #[0, 1, 7], #[1, 5, 0], #[1, 5, 1], #[1, 5, 3], #[1, 5, 6], #[1, 7, 5], #[0, 1, 2], #[0, 3, 0], #[0, 3, 4], #[0, 5, 3], #[0, 5, 6], #[0, 7, 5], #[3, 1, 3], #[3, 2, 1], #[3, 2, 5], #[3, 4, 0], #[3, 4, 1], #[3, 4, 3], #[3, 4, 6], #[3, 6, 0], #[3, 6, 1], #[3, 6, 4], #[2, 0, 4], #[2, 5, 2], #[2, 5, 3], #[2, 6, 5], #[4, 7, 1], #[4, 7, 3], #[5, 0, 3], #[5, 1, 1], #[5, 1, 4], #[3, 6, 5], #[2, 0, 5], #[3, 4, 7], #[0, 1, 5], #[2, 7, 5]]
def modelIndex (a b : Fin 78) : Fin 169 :=
  ⟨(((nbInverseIndex.getD a.val #[]).getD b.val 0)-1)%169,Nat.mod_lt _ (by decide)⟩
def modelFirst (k : Fin 169) : Fin 6 :=
  ⟨(modelData.getD k.val #[]).getD 0 0 %6,Nat.mod_lt _ (by decide)⟩
def modelSecond (k : Fin 169) : Fin 8 :=
  ⟨(modelData.getD k.val #[]).getD 1 0 %8,Nat.mod_lt _ (by decide)⟩
def modelThird (k : Fin 169) : Fin 8 :=
  ⟨(modelData.getD k.val #[]).getD 2 0 %8,Nat.mod_lt _ (by decide)⟩
def modelInverse (k : Fin 169) : Mat := fun i j =>
  F.ofCode ((nbInversePool.getD (k.val+1) #[]).getD (i.val*3+j.val) 0)
def modelNoise (k : Fin 169) (n : Vec) : Vec :=
  act (matrixPool (modelThird k))
    (act (matrixPool (modelSecond k)) (n 0 • direction (modelFirst k)) +
      n 1 • direction (chartTarget (modelSecond k))) +
    n 2 • direction (chartTarget (modelThird k))
def PairCheck (a b : Fin 78) : Prop :=
  let w := controllerWord a b
  let p := wordP0 w; let q := wordP1 w; let r := wordP2 w
  let k := modelIndex a b
  routeController a p q r = b ∧
  (nbInverseIndex.getD a.val #[]).getD b.val 0 = k.val+1 ∧
  inversePort p = modelFirst k ∧
  chart (controller a p) q = modelSecond k ∧
  chart (controller (controller a p) q) r = modelThird k
instance (a b : Fin 78) : Decidable (PairCheck a b) := by unfold PairCheck; infer_instance
end DegreeDiameter.Portfolio.F9Graph56862
