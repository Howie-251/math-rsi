import DegreeDiameter.Portfolio.OppositeGQ44SpreadExact
import DegreeDiameter.Portfolio.OvoidProduct26Inputs
import DegreeDiameter.Portfolio.DiagonalFillReallocationDefinitions
namespace DegreeDiameter.Portfolio.Q4DiagonalFill
set_option maxRecDepth 30000
set_option maxHeartbeats 100000000
namespace Source
abbrev Point := OppositeGQ44Spread.Point
abbrev Line := OppositeGQ44Spread.Line
abbrev Old := OppositeGQ44Spread.Old
abbrev Helper := OppositeGQ44Spread.New
abbrev Vertex := OppositeGQ44Spread.Vertex
abbrev oldEquiv := OppositeGQ44Spread.oldEquiv
abbrev Inc := OppositeGQ44Spread.Inc
abbrev linePoint := OppositeGQ44Spread.linePoint
abbrev spread := OppositeGQ44Spread.spread
abbrev spreadOwner := OppositeGQ44Spread.spreadOwner
abbrev graph := OppositeGQ44Spread.graph
abbrev label := OppositeGQ44Spread.label
abbrev ovoid := OvoidProduct26.ovoid
end Source
abbrev CloneIndex := Fin 17 × Fin 17
abbrev Vertex := DiagonalFillReallocation.Vertex Source.Old Source.Helper CloneIndex
abbrev raw := DiagonalFillReallocation.rawGraph Source.oldEquiv Source.Inc
def center (c : CloneIndex) : Source.Old := Source.oldEquiv.symm (Source.ovoid c.1,Source.spread c.2)
def graph : SimpleGraph Vertex := DiagonalFillReallocation.graph raw Source.graph center
instance : DecidableRel graph.Adj := inferInstanceAs
  (DecidableRel (DiagonalFillReallocation.graph raw Source.graph center).Adj)
def cloneLabel : CloneIndex ≃ Fin 289 := finProdFinEquiv
def unitLabel : Unit ≃ Fin 1 where
  toFun _ := 0
  invFun _ := ()
  left_inv := by intro u;cases u;rfl
  right_inv := by intro i;apply Fin.ext;have := i.isLt;change 0=i.val;omega
def baseLabel : (Source.Vertex ⊕ CloneIndex) ≃ Fin 7531 :=
  (Equiv.sumCongr Source.label cloneLabel).trans finSumFinEquiv
def label : Vertex ≃ Fin 7532 := (Equiv.sumCongr baseLabel unitLabel).trans finSumFinEquiv
theorem label_old (v : Source.Vertex) :
    (label (.inl (.inl v))).val = (Source.label v).val := rfl
theorem label_copy (i k : Fin 17) :
    (label (.inl (.inr (i,k)))).val = 7242+17*i.val+k.val := by
  change 7242+(k.val+17*i.val)=_
  omega
theorem label_hub : (label (.inr ())).val = 7531 := rfl
theorem center_label (i k : Fin 17) :
    (center (i,k)).val = (Source.spread k).val+85*(Source.ovoid i).val := rfl
theorem card_vertex : Fintype.card Vertex = 7532 := by
  simp only [Vertex,DiagonalFillReallocation.Vertex,Fintype.card_sum,Fintype.card_prod,Fintype.card_fin,Fintype.card_unit]
def coverPayload : Nat := 597265264580747789473890154433977936369835573435522892251055285850733524843479376543121195197121442320
def coverSlot (p : Source.Point) : Fin 5 :=
  ⟨(coverPayload / 16^p.val) % 16 % 5,Nat.mod_lt _ (by decide)⟩
def FinalClaim : Prop := Fintype.card Vertex = 7532 ∧
  (∀v,graph.degree v≤26) ∧ DiameterAtMost graph 3 ∧ ¬DiameterAtMost graph 2
#check (label : Vertex ≃ Fin 7532)
#print graph
end DegreeDiameter.Portfolio.Q4DiagonalFill
