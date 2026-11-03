import DegreeDiameter.Portfolio.Q8DiagonalFill83Definitions
namespace DegreeDiameter.Portfolio.Q8DiagonalFill86
namespace Source
abbrev Vertex := Q8DiagonalFill83.Source.Vertex
abbrev graph := Q8DiagonalFill83.Source.graph
abbrev label := Q8DiagonalFill83.Source.label
end Source
abbrev Role := Q8DiagonalFill83.Role
abbrev CopyIndex := Fin 4 × Role
abbrev Vertex := Source.Vertex ⊕ CopyIndex
def center (x : CopyIndex) : Source.Vertex := Q8DiagonalFill83.center x.2
abbrev graph : SimpleGraph Vertex := FullNeighborhoodClones.graph Source.graph center
instance : DecidableRel graph.Adj := inferInstanceAs
  (DecidableRel (FullNeighborhoodClones.graph Source.graph center).Adj)
def copyLabel : CopyIndex ≃ Fin 16904 :=
  (Equiv.prodCongr (Equiv.refl (Fin 4)) Q8DiagonalFill83.roleLabel).trans finProdFinEquiv
def label : Vertex ≃ Fin 363420 :=
  (Equiv.sumCongr Source.label copyLabel).trans finSumFinEquiv
theorem source_center_label (x : CopyIndex) :
    (Source.label (center x)).val = 342290+(Q8DiagonalFill83.roleLabel x.2).val :=
  Q8DiagonalFill83.source_center_label x.2
theorem label_old (v : Source.Vertex) : (label (.inl v)).val = (Source.label v).val := rfl
theorem copy_label (b : Fin 4) (h : Role) :
    (copyLabel (b,h)).val = 4226*b.val+(Q8DiagonalFill83.roleLabel h).val := by
  change (Q8DiagonalFill83.roleLabel h).val+4226*b.val=_
  omega
theorem label_new (b : Fin 4) (h : Role) :
    (label (.inr (b,h))).val = 346516+4226*b.val+(Q8DiagonalFill83.roleLabel h).val := by
  change 346516+((Q8DiagonalFill83.roleLabel h).val+4226*b.val)=_
  omega
theorem label_copy (b : Fin 4) (i j : Fin 65) :
    (label (.inr (b,.inl (i,j)))).val = 346516+4226*b.val+65*i.val+j.val := by
  change 346516+((j.val+65*i.val)+4226*b.val)=_
  omega
theorem label_hub (b : Fin 4) :
    (label (.inr (b,.inr ()))).val = 346516+4226*b.val+4225 := by
  change 346516+(4225+4226*b.val)=_
  omega
theorem card_vertex : Fintype.card Vertex=363420 := by
  simpa only [Fintype.card_fin] using Fintype.card_congr label
def FinalClaim : Prop := Fintype.card Vertex=363420 ∧
  (∀v,graph.degree v≤86) ∧ DiameterAtMost graph 3 ∧ ¬DiameterAtMost graph 2
#check (label : Vertex ≃ Fin 363420)
#print graph
end DegreeDiameter.Portfolio.Q8DiagonalFill86
