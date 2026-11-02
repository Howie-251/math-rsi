import DegreeDiameter.Portfolio.OppositeGQ77SpreadDefinitions
import DegreeDiameter.Portfolio.OvoidSpreadCloneCapacity
namespace DegreeDiameter.Portfolio.GQ77Published33CloneFamily
namespace Source
abbrev Vertex := OppositeGQ77Spread.Vertex
end Source
set_option maxRecDepth 20000
set_option maxHeartbeats 20000000
abbrev BaseIndex := Fin 1650
abbrev CloneIndex (k : Nat) := Fin k × BaseIndex
abbrev Vertex (k : Nat) := Source.Vertex ⊕ CloneIndex k
/-- An explicit reproduction of the published size33, in the immutable source's point order. -/
def ovoid : Fin 33 → OppositeGQ77Spread.Point := ![20, 32, 40, 42, 43, 44, 52, 57, 85, 119, 122, 133, 147, 165, 179, 199, 230, 248, 251, 260, 265, 279, 295, 312, 315, 322, 323, 326, 337, 347, 364, 378, 394]
def baseLabel : (Fin 33 × Fin 50) ≃ BaseIndex := finProdFinEquiv
def basePair : BaseIndex ≃ (Fin 33 × Fin 50) := baseLabel.symm
def baseCenter (b : BaseIndex) : Source.Vertex :=
  OvoidSpreadCloneCapacity.center OppositeGQ77Spread.oldEquiv ovoid OppositeGQ77Spread.spread (basePair b)
/-- All copies retain their owner and its full neighborhood in the original160050 source. -/
def center (k : Nat) (j : CloneIndex k) : Source.Vertex := baseCenter j.2
def graph (k : Nat) : SimpleGraph (Vertex k) :=
  FullNeighborhoodClones.graph OppositeGQ77Spread.graph (center k)
instance (k : Nat) : DecidableRel (graph k).Adj := inferInstanceAs
  (DecidableRel (FullNeighborhoodClones.graph OppositeGQ77Spread.graph (center k)).Adj)
def cloneLabel (k : Nat) : CloneIndex k ≃ Fin (1650*k) :=
  (finProdFinEquiv (m:=k) (n:=1650)).trans (finCongr (Nat.mul_comm k 1650))
def label (k : Nat) : Vertex k ≃ Fin (160050+1650*k) :=
  (Equiv.sumCongr OppositeGQ77Spread.label (cloneLabel k)).trans finSumFinEquiv
theorem base_label (i : Fin 33) (j : Fin 50) :
    (baseLabel (i,j)).val = j.val+50*i.val := rfl
theorem clone_label (k : Nat) (copy : Fin k) (base : BaseIndex) :
    (cloneLabel k (copy,base)).val = base.val+1650*copy.val := rfl
theorem center_source_label (b : BaseIndex) :
    (OppositeGQ77Spread.label (baseCenter b)).val =
      (OppositeGQ77Spread.spread (basePair b).2).val+400*(ovoid (basePair b).1).val := rfl
theorem label_old (k : Nat) (v : Source.Vertex) :
    (label k (.inl v)).val = (OppositeGQ77Spread.label v).val := rfl
theorem label_new (k : Nat) (copy : Fin k) (base : BaseIndex) :
    (label k (.inr (copy,base))).val = 160050+1650*copy.val+base.val := by
  change 160050+(base.val+1650*copy.val) = _
  omega
theorem label_new_coordinates (k : Nat) (copy : Fin k) (i : Fin 33) (j : Fin 50) :
    (label k (.inr (copy,baseLabel (i,j)))).val =
      160050+1650*copy.val+50*i.val+j.val := by
  change 160050+((j.val+50*i.val)+1650*copy.val) = _
  omega
theorem card_vertex (k : Nat) : Fintype.card (Vertex k) = 160050+1650*k := by
  simp only [Vertex,CloneIndex,Fintype.card_sum,Fintype.card_prod,Fintype.card_fin]
  omega
def ovoidOwnerBlocks : Fin 20 → Fin 20 → Option (Fin 33) := ![![none, none, none, none, none, none, none, none, none, none, none, none, none, none, none, none, none, none, none, none], ![some 0, none, none, none, none, none, none, none, none, none, none, none, some 1, none, none, none, none, none, none, none], ![some 2, none, some 3, some 4, some 5, none, none, none, none, none, none, none, some 6, none, none, none, none, some 7, none, none], ![none, none, none, none, none, none, none, none, none, none, none, none, none, none, none, none, none, none, none, none], ![none, none, none, none, none, some 8, none, none, none, none, none, none, none, none, none, none, none, none, none, none], ![none, none, none, none, none, none, none, none, none, none, none, none, none, none, none, none, none, none, none, some 9], ![none, none, some 10, none, none, none, none, none, none, none, none, none, none, some 11, none, none, none, none, none, none], ![none, none, none, none, none, none, none, some 12, none, none, none, none, none, none, none, none, none, none, none, none], ![none, none, none, none, none, some 13, none, none, none, none, none, none, none, none, none, none, none, none, none, some 14], ![none, none, none, none, none, none, none, none, none, none, none, none, none, none, none, none, none, none, none, some 15], ![none, none, none, none, none, none, none, none, none, none, none, none, none, none, none, none, none, none, none, none], ![none, none, none, none, none, none, none, none, none, none, some 16, none, none, none, none, none, none, none, none, none], ![none, none, none, none, none, none, none, none, some 17, none, none, some 18, none, none, none, none, none, none, none, none], ![some 19, none, none, none, none, some 20, none, none, none, none, none, none, none, none, none, none, none, none, none, some 21], ![none, none, none, none, none, none, none, none, none, none, none, none, none, none, none, some 22, none, none, none, none], ![none, none, none, none, none, none, none, none, none, none, none, none, some 23, none, none, some 24, none, none, none, none], ![none, none, some 25, some 26, none, none, some 27, none, none, none, none, none, none, none, none, none, none, some 28, none, none], ![none, none, none, none, none, none, none, some 29, none, none, none, none, none, none, none, none, none, none, none, none], ![none, none, none, none, some 30, none, none, none, none, none, none, none, none, none, none, none, none, none, some 31, none], ![none, none, none, none, none, none, none, none, none, none, none, none, none, none, some 32, none, none, none, none, none]]
def ovoidOwner (p : OppositeGQ77Spread.Point) : Option (Fin 33) :=
  OppositeGQ77Spread.lookup400 ovoidOwnerBlocks p
/-- Index0 on the136 unoccupied lines; the finite certificate uses an implication. -/
def lineOvoidIndexBlocks : Fin 20 → Fin 20 → Fin 33 := ![![0, 7, 0, 0, 0, 8, 0, 0, 4, 5, 6, 1, 2, 0, 3, 14, 0, 13, 15, 0], ![0, 0, 11, 0, 0, 12, 9, 10, 0, 0, 18, 0, 16, 0, 17, 0, 21, 20, 0, 19], ![22, 0, 0, 0, 30, 0, 0, 0, 31, 32, 24, 25, 29, 26, 23, 28, 27, 7, 19, 0], ![26, 8, 28, 22, 7, 30, 0, 31, 8, 0, 15, 7, 23, 10, 27, 8, 0, 29, 7, 20], ![0, 21, 8, 0, 17, 7, 24, 25, 16, 8, 0, 18, 7, 13, 0, 14, 8, 0, 0, 7], ![9, 0, 11, 8, 12, 32, 16, 0, 0, 18, 20, 0, 21, 9, 29, 11, 23, 12, 27, 0], ![0, 0, 0, 0, 15, 0, 0, 0, 0, 0, 24, 25, 0, 0, 32, 10, 22, 0, 19, 0], ![0, 0, 0, 0, 0, 0, 0, 0, 28, 14, 30, 17, 31, 26, 13, 27, 0, 0, 29, 13], ![23, 14, 19, 0, 0, 0, 0, 22, 0, 17, 32, 0, 0, 0, 24, 25, 18, 11, 15, 12], ![16, 0, 9, 20, 0, 21, 30, 0, 31, 0, 26, 0, 28, 0, 0, 0, 0, 10, 0, 0], ![0, 0, 0, 0, 0, 0, 32, 0, 0, 0, 0, 24, 25, 13, 20, 14, 21, 10, 0, 0], ![0, 0, 30, 0, 31, 1, 1, 1, 1, 1, 1, 1, 15, 0, 26, 0, 28, 0, 0, 11], ![22, 12, 19, 17, 9, 0, 23, 16, 27, 0, 18, 29, 0, 31, 12, 24, 25, 9, 30, 11], ![0, 17, 0, 0, 0, 0, 0, 13, 18, 14, 0, 22, 16, 19, 0, 0, 0, 0, 26, 10], ![28, 2, 2, 2, 2, 2, 2, 2, 29, 21, 23, 32, 27, 15, 20, 3, 3, 3, 3, 3], ![3, 3, 4, 4, 4, 4, 4, 4, 4, 5, 5, 5, 5, 5, 5, 5, 12, 28, 20, 9], ![21, 11, 26, 14, 0, 0, 0, 32, 13, 0, 0, 0, 29, 0, 23, 17, 27, 0, 31, 16], ![0, 10, 18, 30, 22, 0, 19, 15, 24, 25, 0, 0, 15, 17, 10, 0, 0, 0, 0, 26], ![18, 28, 0, 32, 16, 6, 6, 6, 6, 6, 6, 6, 30, 27, 31, 22, 29, 19, 23, 0], ![0, 9, 13, 11, 14, 12, 25, 0, 0, 0, 0, 0, 24, 21, 0, 0, 0, 0, 20, 0]]
def lineOvoidIndex (l : OppositeGQ77Spread.Line) : Fin 33 :=
  OppositeGQ77Spread.lookup400 lineOvoidIndexBlocks l
def FinalClaim (k : Nat) : Prop := Fintype.card (Vertex k) = 160050+1650*k ∧
  (∀ v, (graph k).degree v ≤ 64+k) ∧ DiameterAtMost (graph k) 3 ∧ ¬DiameterAtMost (graph k) 2
#print ovoid
#print center
#print graph
#print label
#print FinalClaim
end DegreeDiameter.Portfolio.GQ77Published33CloneFamily
