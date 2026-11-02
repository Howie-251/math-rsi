import DegreeDiameter.Portfolio.EvenQ8SourceDefinitions
import DegreeDiameter.Portfolio.EvenQ8BalancedFullOvoidCopy82Definitions
import DegreeDiameter.Portfolio.DiagonalFillReallocationDefinitions
namespace DegreeDiameter.Portfolio.Q8DiagonalFill
set_option maxRecDepth 30000
set_option maxHeartbeats 100000000
namespace Source
abbrev Point := EvenQ8Source.Balanced.Point
abbrev Line := EvenQ8Source.Balanced.Line
abbrev Old := EvenQ8Source.Balanced.Old
abbrev Helper := EvenQ8Source.Balanced.Helper
abbrev Vertex := EvenQ8Source.Balanced.Vertex
abbrev oldEquiv := EvenQ8Source.Balanced.oldEquiv
abbrev Inc := EvenQ8Source.Balanced.Inc
abbrev linePoint := EvenQ8Source.Balanced.linePoint
abbrev spread := EvenQ8Source.Balanced.spread
abbrev spreadOwner := EvenQ8Source.Balanced.spreadOwner
abbrev graph := EvenQ8Source.Balanced.graph
abbrev label := EvenQ8Source.Balanced.label
abbrev ovoid := EvenQ8BalancedFullOvoidCopy82.ovoid
end Source
#eval IO.eprintln "Q8_defs_after_source"
abbrev CloneIndex := Fin 65 × Fin 65
abbrev Vertex := DiagonalFillReallocation.Vertex Source.Old Source.Helper CloneIndex
abbrev raw := DiagonalFillReallocation.rawGraph Source.oldEquiv Source.Inc
def center (c : CloneIndex) : Source.Old := Source.oldEquiv.symm (Source.ovoid c.1,Source.spread c.2)
abbrev graph : SimpleGraph Vertex := DiagonalFillReallocation.graph raw Source.graph center
instance : DecidableRel graph.Adj := inferInstanceAs
  (DecidableRel (DiagonalFillReallocation.graph raw Source.graph center).Adj)
#eval IO.eprintln "Q8_defs_after_graph_instance"
def cloneLabel : CloneIndex ≃ Fin 4225 := finProdFinEquiv
def unitLabel : Unit ≃ Fin 1 where
  toFun _ := 0
  invFun _ := ()
  left_inv := by intro u;cases u;rfl
  right_inv := by intro i;apply Fin.ext;have := i.isLt;change 0=i.val;omega
#eval IO.eprintln "Q8_defs_after_unit"
def baseLabel : (Source.Vertex ⊕ CloneIndex) ≃ Fin 346515 :=
  (Equiv.sumCongr Source.label cloneLabel).trans finSumFinEquiv
def label : Vertex ≃ Fin 346516 := (Equiv.sumCongr baseLabel unitLabel).trans finSumFinEquiv
#eval IO.eprintln "Q8_defs_after_label"
theorem label_old (v : Source.Vertex) :
    (label (.inl (.inl v))).val = (Source.label v).val := rfl
theorem label_copy (i k : Fin 65) :
    (label (.inl (.inr (i,k)))).val = 342290+65*i.val+k.val := by
  change 342290+(k.val+65*i.val)=_
  omega
theorem label_hub : (label (.inr ())).val = 346515 := rfl
theorem center_label (i k : Fin 65) :
    (center (i,k)).val = (Source.spread k).val+585*(Source.ovoid i).val := rfl
#eval IO.eprintln "Q8_defs_after_label_lemmas"
theorem card_vertex : Fintype.card Vertex = 346516 := by
  change Fintype.card ((EvenQ8Source.Balanced.Vertex ⊕ CloneIndex) ⊕ Unit) = 346516
  rw [Fintype.card_sum,Fintype.card_sum,EvenQ8Source.Balanced.card_vertex,Fintype.card_prod]
  simp only [Fintype.card_fin,Fintype.card_unit]
#eval IO.eprintln "Q8_defs_after_card"
def coverPayload : Nat := 137147716697251108827210981241877343275329346323410719684311414468393137194199579091833526921296490122575754363995300756095766513048116549903225281205468281057506107683997272514012585161337941835462023755699039454161973594570734933368677020771669677044958958231841212110220614694534470520963495957739800129636870254461271722518925853278360627387004699223010207354026852326254310738152839417058229029375750229263344758661639035406204511858723049611159500240627791845542928790419550898574745776068826975326899543602806673918455346921029043478823548210074540501669616289255723131138400495730252185759541853177025602958567719721700086327775315326176940642621091668844765387441360577495907671064637006157197840
def coverSlot (p : Source.Point) : Fin 9 :=
  ⟨(coverPayload / 16^p.val) % 16 % 9,Nat.mod_lt _ (by decide)⟩
#eval IO.eprintln "Q8_defs_after_cover_payload"
def FinalClaim : Prop := Fintype.card Vertex = 346516 ∧
  (∀v,graph.degree v≤82) ∧ DiameterAtMost graph 3 ∧ ¬DiameterAtMost graph 2
#check (label : Vertex ≃ Fin 346516)
#print graph
end DegreeDiameter.Portfolio.Q8DiagonalFill
