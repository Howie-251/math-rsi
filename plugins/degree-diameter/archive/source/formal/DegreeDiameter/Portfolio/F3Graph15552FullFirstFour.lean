import DegreeDiameter.Portfolio.F3Graph15552Row0Data
namespace DegreeDiameter.Portfolio.F3Graph15552.FullFirstFour
set_option maxRecDepth 20000
set_option maxHeartbeats 40000000
def group (g : Fin 4) : Row0Coset.G := ⟨g.val,by have h:=g.isLt;omega⟩
def slot (k : Fin 27) : Row0Coset.K := ⟨k.val,by have h:=k.isLt;omega⟩
theorem column_certificate : ∀k j,routeVec (Row0Coset.word (slot k)) 0 (basisVec j)=
    routeVec (Row0Coset.reference (Row0Coset.slotGroup (slot k))) 0 (basisVec j)+
      routeVec (Row0Coset.word (slot k)) (Row0Coset.column (slot k) j) 0 := by decide +kernel
theorem cover_certificate : ∀g z,
    routeVec (Row0Coset.word (Row0Coset.choice (group g) z)) (Row0Coset.alpha (group g) z) 0=
      decodeVec z := by decide +kernel
theorem choice_group_certificate : ∀g z,
    Row0Coset.slotGroup (Row0Coset.choice (group g) z)=group g := by decide +kernel
theorem choice_slot_range : ∀g z,(Row0Coset.choice (group g) z).val<27 := by decide +kernel
theorem controller_certificate : ∀k,routeController 0 (Row0Coset.word (slot k))=
    Row0Coset.target (Row0Coset.slotGroup (slot k)) := by decide +kernel
#print axioms column_certificate
#print axioms cover_certificate
#print axioms controller_certificate
end DegreeDiameter.Portfolio.F3Graph15552.FullFirstFour
