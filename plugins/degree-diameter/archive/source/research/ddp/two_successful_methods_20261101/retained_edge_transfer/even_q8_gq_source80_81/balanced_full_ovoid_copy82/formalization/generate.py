import csv,json,time
from pathlib import Path
T=time.process_time();D=Path(__file__).resolve().parent
R=next(p for p in D.parents if(p/'formal/DegreeDiameter/Portfolio').is_dir());Q=R/'formal/DegreeDiameter/Portfolio'
S=D.parent;source=S.parent;G=source.parent/'even_q8_gq_geometry_pilot'
prefix='EvenQ8BalancedFullOvoidCopy82';NS='DegreeDiameter.Portfolio.'+prefix
parameters=json.loads((S/'PARAMETERS.json').read_text());O=parameters['ovoid_point_ids']
data=list(map(int,(source/'balanced/TABLES_INPUT.txt').read_text().split()))
np,nl,a,b,j=data[:5];at=10;lp=[data[at+k*a:at+(k+1)*a]for k in range(nl)]
owner=[65]*np
for i,p in enumerate(O):owner[p]=i
with(G/'OVOID65_LINE_INTERSECTIONS.csv').open()as f:
    rows=list(csv.DictReader(f));lineowners=[owner[int(row['ovoid_point'])]for row in rows]
assert len(lineowners)==585 and len(O)==65
def tree(v):
    n=1
    while n<len(v):n*=2
    v=list(v)+[0]*(n-len(v))
    def emit(x):return '(.leaf '+str(x[0])+')'if len(x)==1 else'(.node '+emit(x[::2])+' '+emit(x[1::2])+')'
    return emit(v)
defs=f'''import DegreeDiameter.Portfolio.EvenQ8SourceDefinitions
import DegreeDiameter.Portfolio.OvoidSpreadCloneCapacity
namespace {NS}
set_option maxRecDepth 30000
set_option maxHeartbeats 100000000
namespace Source
abbrev Point := EvenQ8Source.Balanced.Point
abbrev Line := EvenQ8Source.Balanced.Line
abbrev Old := EvenQ8Source.Balanced.Old
abbrev Helper := EvenQ8Source.Balanced.Helper
abbrev Vertex := EvenQ8Source.Balanced.Vertex
abbrev oldEquiv := EvenQ8Source.Balanced.oldEquiv
abbrev label := EvenQ8Source.Balanced.label
abbrev linePoint := EvenQ8Source.Balanced.linePoint
abbrev spread := EvenQ8Source.Balanced.spread
abbrev Inc := EvenQ8Source.Balanced.Inc
abbrev graph := EvenQ8Source.Balanced.graph
end Source
open EvenQ8Source
abbrev CloneIndex := Fin 4225
abbrev Vertex := Source.Vertex ⊕ CloneIndex
def pair : CloneIndex ≃ Fin 65 × Fin 65 := (finProdFinEquiv (m:=65) (n:=65)).symm
def ovoidRows : NatTable := {tree(O)}
def ovoid (i : Fin 65) : Source.Point := ⟨ovoidRows.get i.val % 585,Nat.mod_lt _ (by decide)⟩
def ovoidOwnerRows : NatTable := {tree(owner)}
/-- Value65 denotes a point outside the selected65-point ovoid. -/
def ovoidOwner (p : Source.Point) : Nat := ovoidOwnerRows.get p.val
def lineOvoidRows : NatTable := {tree(lineowners)}
def lineOvoidIndex (l : Source.Line) : Fin 65 := ⟨lineOvoidRows.get l.val % 65,Nat.mod_lt _ (by decide)⟩
def center (j : CloneIndex) : Source.Vertex :=
  OvoidSpreadCloneCapacity.center Source.oldEquiv ovoid Source.spread (pair j)
def graph : SimpleGraph Vertex := FullNeighborhoodClones.graph Source.graph center
instance : DecidableRel graph.Adj := inferInstanceAs
  (DecidableRel (FullNeighborhoodClones.graph Source.graph center).Adj)
def label : Vertex ≃ Fin 346515 :=
  (Equiv.sumCongr Source.label (Equiv.refl CloneIndex)).trans finSumFinEquiv
theorem clone_index_coordinates (i j : Fin 65) : (pair.symm (i,j)).val = j.val+65*i.val := rfl
theorem center_label_coordinates (i j : Fin 65) :
    (Source.label (center (pair.symm (i,j)))).val = 585*(ovoid i).val+(Source.spread j).val := by
  simp only [center,OvoidSpreadCloneCapacity.center,Equiv.apply_symm_apply]
  change (Source.spread j).val+585*(ovoid i).val = _
  omega
theorem label_old (v : Source.Vertex) : (label (.inl v)).val = (Source.label v).val := rfl
theorem label_new (j : CloneIndex) : (label (.inr j)).val = 342290+j.val := rfl
theorem label_new_coordinates (i j : Fin 65) :
    (label (.inr (pair.symm (i,j)))).val = 342290+65*i.val+j.val := by
  change 342290+(j.val+65*i.val) = _
  omega
theorem card_vertex : Fintype.card Vertex = 346515 := by
  simp only [Vertex,Source.Vertex,EvenQ8Source.Balanced.Vertex,Fintype.card_sum,Fintype.card_fin]
def FinalClaim : Prop := Fintype.card Vertex = 346515 ∧
  (∀ v,graph.degree v ≤ 82) ∧ DiameterAtMost graph 3 ∧ ¬DiameterAtMost graph 2
#check (label : Vertex ≃ Fin 346515)
#print graph
end {NS}
'''
inputs=f'''import DegreeDiameter.Portfolio.{prefix}Definitions
import DegreeDiameter.Portfolio.EvenQ8SourceFullBalancedHowner
namespace {NS}
set_option maxRecDepth 30000
set_option maxHeartbeats 100000000
theorem owner_of_ovoid : ∀ i,ovoidOwner (ovoid i) = i.val := by decide
theorem line_index_certificate : ∀ l k,
    ovoidOwner (Source.linePoint l k) = 65 ∨
      ovoidOwner (Source.linePoint l k) = (lineOvoidIndex l).val := by decide
theorem ovoid_index_of_incidence (l : Source.Line) (i : Fin 65)
    (h : Source.Inc (ovoid i) l) : i = lineOvoidIndex l := by
  obtain ⟨k,hk⟩ := h
  have hi : ovoidOwner (Source.linePoint l k) = i.val :=
    (congrArg ovoidOwner hk).trans (owner_of_ovoid i)
  rcases line_index_certificate l k with hnone | hsome
  · have := i.isLt
    omega
  · apply Fin.ext
    exact hi.symm.trans hsome
theorem ovoid_unique : ∀ l i i', Source.Inc (ovoid i) l → Source.Inc (ovoid i') l → i = i' := by
  intro l i i' hi hi'
  exact (ovoid_index_of_incidence l i hi).trans (ovoid_index_of_incidence l i' hi').symm
theorem spread_unique : ∀ p j j',Source.Inc p (Source.spread j) →
    Source.Inc p (Source.spread j') → j = j' := by
  intro p j j' hj hj'
  exact (EvenQ8SourceFull.Balanced.howner p j hj).trans
    (EvenQ8SourceFull.Balanced.howner p j' hj').symm
theorem load_le_one (w : Source.Vertex) : FullNeighborhoodClones.load Source.graph center w ≤ 1 := by
  unfold FullNeighborhoodClones.load
  apply Fintype.card_le_one_iff.mpr
  intro x y
  apply Subtype.ext
  apply pair.injective
  exact OvoidSpreadCloneCapacity.adjacent_centers_unique Source.oldEquiv Source.Inc
    ovoid Source.spread ovoid_unique spread_unique
    w (pair x.val) (pair y.val) x.property y.property
#print axioms ovoid_unique
#print axioms load_le_one
end {NS}
'''
exact=f'''import DegreeDiameter.Portfolio.{prefix}Inputs
import DegreeDiameter.Portfolio.EvenQ8SourceFullExact
namespace {NS}
theorem source_no_isolated (v : Source.Vertex) : ∃ w,Source.graph.Adj v w := by
  have ht : ∃ t : Source.Vertex,v ≠ t := by
    by_cases h0 : v = .inl (0 : Source.Old)
    · refine ⟨.inl (1 : Source.Old),?_⟩
      rw [h0]
      decide
    · exact ⟨.inl (0 : Source.Old),h0⟩
  obtain ⟨t,ht⟩ := ht
  obtain ⟨p,_⟩ := EvenQ8SourceFull.D81_342290.final_claim.2.2.1 v t
  obtain ⟨w,hw,tail,heq⟩ := SimpleGraph.Walk.exists_eq_cons_of_ne ht p
  exact ⟨w,hw⟩
theorem degree_le : ∀ v,graph.degree v ≤ 82 :=
  FullNeighborhoodClones.degree_le Source.graph center 81 1
    EvenQ8SourceFull.D81_342290.final_claim.2.1 load_le_one
theorem diameterAtMost_three : DiameterAtMost graph 3 :=
  FullNeighborhoodClones.diameterAtMost Source.graph center 3 (by decide)
    EvenQ8SourceFull.D81_342290.final_claim.2.2.1 source_no_isolated
theorem not_diameterAtMost_two : ¬DiameterAtMost graph 2 :=
  FullNeighborhoodClones.not_diameterAtMost Source.graph center 2
    EvenQ8SourceFull.D81_342290.final_claim.2.2.2
theorem d82_346515 : Fintype.card Vertex = 346515 ∧
    (∀ v,graph.degree v ≤ 82) ∧ DiameterAtMost graph 3 ∧ ¬DiameterAtMost graph 2 :=
  ⟨card_vertex,degree_le,diameterAtMost_three,not_diameterAtMost_two⟩
theorem final_claim : FinalClaim := d82_346515
theorem old_walk_bound_iff (u v : Source.Vertex) (n : Nat) :
    (∃p:graph.Walk (.inl u) (.inl v),p.length ≤ n) ↔
      ∃p:Source.graph.Walk u v,p.length ≤ n :=
  FullNeighborhoodClones.old_walk_bound_iff Source.graph center u v n
#check d82_346515
#print axioms final_claim
end {NS}
'''
audit=f'''import DegreeDiameter.Portfolio.{prefix}Exact
open {NS}
#check (graph : SimpleGraph Vertex)
#check (label : Vertex ≃ Fin 346515)
#print FinalClaim
#check d82_346515
#print d82_346515
#print axioms d82_346515
#check final_claim
#print final_claim
#print axioms final_claim
#print axioms load_le_one
#print axioms old_walk_bound_iff
#print axioms label_new_coordinates
'''
for suffix,text in [('Definitions',defs),('Inputs',inputs),('Exact',exact),('Audit',audit)]:
    path=(R/'formal'if suffix=='Audit'else Q)/(prefix+suffix+'.lean')
    assert not path.exists(),path;path.write_text(text)
result=dict(status='FOUR_MODULES_PREPARED_COMPILATION_GATED',CPU_seconds=time.process_time()-T,modules=[prefix+x for x in['Definitions','Inputs','Exact','Audit']],finite_line_slots=585*9,ovoid_index_checks=65,source_exact_required='EvenQ8SourceFullExact',fresh_receipt_required=True,actual_compiles=0)
(D/'PREPARATION_RESULT.json').write_text(json.dumps(result,indent=2)+'\n')
(D/'STAGE_STATE.json').write_text(json.dumps(dict(status=result['status'],running=False,active_modules=[],kernel_target_complete=False),indent=2)+'\n');print(json.dumps(result))
