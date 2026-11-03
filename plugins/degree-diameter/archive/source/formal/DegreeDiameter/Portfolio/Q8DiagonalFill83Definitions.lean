import DegreeDiameter.Portfolio.Q8DiagonalFillDefinitions
import DegreeDiameter.Portfolio.FullNeighborhoodClones
namespace DegreeDiameter.Portfolio.Q8DiagonalFill83
namespace Source
abbrev Vertex := Q8DiagonalFill.Vertex
abbrev Old := Q8DiagonalFill.Source.Old
abbrev graph := Q8DiagonalFill.graph
abbrev label := Q8DiagonalFill.label
end Source
abbrev CloneIndex := Q8DiagonalFill.CloneIndex
abbrev Role := CloneIndex ⊕ Unit
abbrev Vertex := Source.Vertex ⊕ Role
def center : Role → Source.Vertex
  | .inl c => .inl (.inr c)
  | .inr u => .inr u
abbrev graph : SimpleGraph Vertex := FullNeighborhoodClones.graph Source.graph center
instance : DecidableRel graph.Adj := inferInstanceAs
  (DecidableRel (FullNeighborhoodClones.graph Source.graph center).Adj)
def roleLabel : Role ≃ Fin 4226 :=
  (Equiv.sumCongr Q8DiagonalFill.cloneLabel Q8DiagonalFill.unitLabel).trans finSumFinEquiv
def label : Vertex ≃ Fin 350742 :=
  (Equiv.sumCongr Source.label roleLabel).trans finSumFinEquiv
theorem source_center_label (r : Role) : (Source.label (center r)).val = 342290+(roleLabel r).val := by
  cases r with
  | inl c => rfl
  | inr u => cases u;rfl
theorem label_old (v : Source.Vertex) : (label (.inl v)).val = (Source.label v).val := rfl
theorem label_new (r : Role) : (label (.inr r)).val = 346516+(roleLabel r).val := rfl
theorem label_copy (i j : Fin 65) : (label (.inr (.inl (i,j)))).val = 346516+65*i.val+j.val := by
  change 346516+(j.val+65*i.val)=_
  omega
theorem label_hub : (label (.inr (.inr ()))).val = 350741 := rfl
theorem card_vertex : Fintype.card Vertex=350742 := by
  change Fintype.card (Q8DiagonalFill.Vertex ⊕ (Q8DiagonalFill.CloneIndex ⊕ Unit))=350742
  rw [Fintype.card_sum,Q8DiagonalFill.card_vertex,Fintype.card_sum,Fintype.card_prod]
  simp only [Fintype.card_fin,Fintype.card_unit]
def FinalClaim : Prop := Fintype.card Vertex=350742 ∧
  (∀v,graph.degree v≤83) ∧ DiameterAtMost graph 3 ∧ ¬DiameterAtMost graph 2
#check (label : Vertex ≃ Fin 350742)
#print graph
end DegreeDiameter.Portfolio.Q8DiagonalFill83
