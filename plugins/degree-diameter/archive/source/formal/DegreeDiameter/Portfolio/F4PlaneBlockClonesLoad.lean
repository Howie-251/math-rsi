import DegreeDiameter.Portfolio.F4PlaneBlockClonesPlane
import DegreeDiameter.Portfolio.F4PlaneBlockClonesCapacity
namespace DegreeDiameter.Portfolio.F4PlaneBlockClones
open F4Graph3840
set_option maxRecDepth 20000
set_option maxHeartbeats 20000000

/-- Each actual adjacent clone names an allowed control block. -/
def neighborBlock {K : Nat} (layers : Fin K → Fin 60) (v : Fin 3840) :
    {j : Fin (K*16) // F4Graph3840.graph.Adj v (center layers j)} → Allowed layers (controllerOf v) :=
  fun j => ⟨blockIndex j.val, by
    obtain ⟨p,t,hp⟩ := (adj_iff_forward _ _).mp j.property
    refine ⟨p,?_⟩
    have hc := congrArg controllerOf hp
    simpa only [forward,center,controllerOf_liftAt] using hc⟩

theorem neighborBlock_injective {K : Nat} (layers : Fin K → Fin 60) (v : Fin 3840) :
    Function.Injective (neighborBlock layers v) := by
  intro x y h
  have hb : blockIndex x.val = blockIndex y.val := congrArg Subtype.val h
  have hy : F4Graph3840.graph.Adj v
      (liftAt (layers (blockIndex y.val)) (planeCode (planeIndex y.val))) := y.property
  rw [← hb] at hy
  have hp := plane_neighbor_unique v (layers (blockIndex x.val)) (planeIndex x.val) (planeIndex y.val) x.property hy
  apply Subtype.ext
  apply Fin.ext
  have hbn := congrArg Fin.val hb
  have hpn := congrArg Fin.val hp
  change x.val.val/16=y.val.val/16 at hbn
  change x.val.val%16=y.val.val%16 at hpn
  omega

theorem load_le_capacity {K : Nat} (layers : Fin K → Fin 60) (k : Nat)
    (hcap : ∀ a, Fintype.card (Allowed layers a) ≤ k) (v : Fin 3840) :
    FullNeighborhoodClones.load F4Graph3840.graph (center layers) v ≤ k := by
  unfold FullNeighborhoodClones.load
  exact (Fintype.card_le_of_injective (neighborBlock layers v) (neighborBlock_injective layers v)).trans (hcap (controllerOf v))

theorem source_no_isolated (v : Fin 3840) : ∃ w, F4Graph3840.graph.Adj v w :=
  ⟨forward v 0 0,forward_adj v 0 0⟩

#print axioms load_le_capacity
end DegreeDiameter.Portfolio.F4PlaneBlockClones
