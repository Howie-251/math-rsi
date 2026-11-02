import json,time
from pathlib import Path
T=time.process_time();D=Path(__file__).resolve().parent
R=next(p for p in D.parents if(p/'formal/DegreeDiameter/Portfolio').is_dir());Q=R/'formal/DegreeDiameter/Portfolio'
BASE=R/'research/ddp/two_successful_methods_20261101/retained_edge_transfer'
for tag,np,nl,a,j,oldn,nH,n,delta,oldns,ovns in[
 ('Q4',85,85,5,17,7225,7242,7532,25,'OppositeGQ44Spread','OvoidProduct26'),
 ('Q8',585,585,9,65,342225,342290,346516,81,'EvenQ8Source.Balanced','EvenQ8BalancedFullOvoidCopy82')]:
 prefix=tag+'DiagonalFill';ns='DegreeDiameter.Portfolio.'+prefix
 if tag=='Q4':
  data=json.loads((BASE/'opposite_gq44_spread25/PARAMETERS.json').read_text());lp=[r['points']for r in data['lines']];spread=data['spread_line_labels'];owner=data['point_spread_owner'];sourceimports=['OppositeGQ44SpreadExact','OvoidProduct26Inputs'];project='OppositeGQ44Spread.projection';sourceclaim='OppositeGQ44Spread.concrete_order_degree_and_exact_D3';helper='New'
 else:
  w=list(map(int,(BASE/'even_q8_gq_source80_81/balanced/TABLES_INPUT.txt').read_text().split()));at=10;lp=[w[at+x*a:at+(x+1)*a]for x in range(nl)];at+=nl*a+np*a;spread=w[at:at+j];owner=w[at+j:at+j+np];sourceimports=['EvenQ8SourceFullExact','EvenQ8BalancedFullOvoidCopy82Inputs'];project='EvenQ8SourceFull.Balanced.project';sourceclaim='EvenQ8SourceFull.D81_342290.final_claim';helper='Helper'
 slots=[lp[spread[owner[p]]].index(p)for p in range(np)];payload=sum(x*16**p for p,x in enumerate(slots))
 defs=''.join('import DegreeDiameter.Portfolio.'+x+'\n'for x in sourceimports+['DiagonalFillReallocationDefinitions'])+f'''namespace {ns}
set_option maxRecDepth 30000
set_option maxHeartbeats 100000000
namespace Source
abbrev Point := {oldns}.Point
abbrev Line := {oldns}.Line
abbrev Old := {oldns}.Old
abbrev Helper := {oldns}.{helper}
abbrev Vertex := {oldns}.Vertex
abbrev oldEquiv := {oldns}.oldEquiv
abbrev Inc := {oldns}.Inc
abbrev linePoint := {oldns}.linePoint
abbrev spread := {oldns}.spread
abbrev spreadOwner := {oldns}.spreadOwner
abbrev graph := {oldns}.graph
abbrev label := {oldns}.label
abbrev ovoid := {ovns}.ovoid
end Source
abbrev CloneIndex := Fin {j} × Fin {j}
abbrev Vertex := DiagonalFillReallocation.Vertex Source.Old Source.Helper CloneIndex
abbrev raw := DiagonalFillReallocation.rawGraph Source.oldEquiv Source.Inc
def center (c : CloneIndex) : Source.Old := Source.oldEquiv.symm (Source.ovoid c.1,Source.spread c.2)
def graph : SimpleGraph Vertex := DiagonalFillReallocation.graph raw Source.graph center
instance : DecidableRel graph.Adj := inferInstanceAs
  (DecidableRel (DiagonalFillReallocation.graph raw Source.graph center).Adj)
def cloneLabel : CloneIndex ≃ Fin {j*j} := finProdFinEquiv
def unitLabel : Unit ≃ Fin 1 where
  toFun _ := 0
  invFun _ := ()
  left_inv := by intro u;cases u;rfl
  right_inv := by intro i;apply Fin.ext;have := i.isLt;change 0=i.val;omega
def baseLabel : (Source.Vertex ⊕ CloneIndex) ≃ Fin {nH+j*j} :=
  (Equiv.sumCongr Source.label cloneLabel).trans finSumFinEquiv
def label : Vertex ≃ Fin {n} := (Equiv.sumCongr baseLabel unitLabel).trans finSumFinEquiv
theorem label_old (v : Source.Vertex) :
    (label (.inl (.inl v))).val = (Source.label v).val := rfl
theorem label_copy (i k : Fin {j}) :
    (label (.inl (.inr (i,k)))).val = {nH}+{j}*i.val+k.val := by
  change {nH}+(k.val+{j}*i.val)=_
  omega
theorem label_hub : (label (.inr ())).val = {n-1} := rfl
theorem center_label (i k : Fin {j}) :
    (center (i,k)).val = (Source.spread k).val+{nl}*(Source.ovoid i).val := rfl
theorem card_vertex : Fintype.card Vertex = {n} := by
  simp only [Vertex,DiagonalFillReallocation.Vertex,Fintype.card_sum,Fintype.card_prod,Fintype.card_fin,Fintype.card_unit]
def coverPayload : Nat := {payload}
def coverSlot (p : Source.Point) : Fin {a} :=
  ⟨(coverPayload / 16^p.val) % 16 % {a},Nat.mod_lt _ (by decide)⟩
def FinalClaim : Prop := Fintype.card Vertex = {n} ∧
  (∀v,graph.degree v≤{delta+1}) ∧ DiameterAtMost graph 3 ∧ ¬DiameterAtMost graph 2
#check (label : Vertex ≃ Fin {n})
#print graph
end {ns}
'''
 inputs=f'''import DegreeDiameter.Portfolio.{prefix}Definitions
import DegreeDiameter.Portfolio.DiagonalFillReallocationGeometry
namespace {ns}
set_option maxRecDepth 30000
set_option maxHeartbeats 100000000
theorem cover_certificate : ∀p,Source.linePoint (Source.spread (Source.spreadOwner p)) (coverSlot p)=p := by decide
theorem spread_cover (p : Source.Point) : Source.Inc p (Source.spread (Source.spreadOwner p)) :=
  ⟨coverSlot p,cover_certificate p⟩
theorem line_two_certificate : ∀l,Source.linePoint l 0 ≠ Source.linePoint l 1 := by decide
theorem line_two (l : Source.Line) : ∃a b,Source.Inc a l ∧ Source.Inc b l ∧ a≠b :=
  ⟨Source.linePoint l 0,Source.linePoint l 1,⟨0,rfl⟩,⟨1,rfl⟩,line_two_certificate l⟩
theorem compat (u v : Source.Old) : Source.graph.Adj (.inl u) (.inl v) ↔ raw.Adj u v := Iff.rfl
theorem raw_D3 : DiameterAtMost raw 3 :=
  DiagonalFillReallocation.raw_diameter_three Source.oldEquiv Source.Inc {project}
theorem raw_no_isolated (v : Source.Old) : ∃w,raw.Adj v w := by
  have ht : ∃t:Source.Old,v≠t := by
    by_cases h0 : v=0
    · refine ⟨1,?_⟩;rw [h0];decide
    · exact ⟨0,h0⟩
  obtain ⟨t,ht⟩ := ht
  obtain ⟨p,_⟩ := raw_D3 v t
  obtain ⟨w,hw,tail,heq⟩ := SimpleGraph.Walk.exists_eq_cons_of_ne ht p
  exact ⟨w,hw⟩
theorem load_le_one (v : Source.Old) : FullNeighborhoodClones.load raw center v≤1 := by
  unfold FullNeighborhoodClones.load
  apply Fintype.card_le_one_iff.mpr
  intro x y
  apply Subtype.ext
  exact OvoidSpreadCloneCapacity.adjacent_centers_unique Source.oldEquiv Source.Inc
    Source.ovoid Source.spread {ovns}.ovoid_unique {ovns}.spread_unique
    (.inl v) x.val y.val x.property y.property
theorem flag_route : ∀v,∃j w,Source.graph.Adj (.inr j) (.inl w) ∧ raw.Adj w v :=
  DiagonalFillReallocation.flag_neighbor Source.oldEquiv Source.Inc Source.spread
    Source.spreadOwner spread_cover line_two {project}
theorem filler_route : ∀j c,∃w,∃p:Source.graph.Walk (.inr j) (.inl w),
    p.length≤2 ∧ raw.Adj w (center c) :=
  DiagonalFillReallocation.filler_route Source.oldEquiv Source.Inc Source.spread
    Source.ovoid Source.spreadOwner spread_cover line_two {ovns}.spread_unique {project}
#print axioms load_le_one
#print axioms flag_route
#print axioms filler_route
end {ns}
'''
 exact=f'''import DegreeDiameter.Portfolio.{prefix}Inputs
import DegreeDiameter.Portfolio.DiagonalFillReallocationDegree
import DegreeDiameter.Portfolio.DiagonalFillReallocationLower
namespace {ns}
theorem degree_le : ∀v,graph.degree v≤{delta+1} :=
  DiagonalFillReallocation.degree_le raw Source.graph center {delta} compat
    {sourceclaim}.2.1 load_le_one (by decide)
theorem diameterAtMost_three : DiameterAtMost graph 3 :=
  DiagonalFillReallocation.diameter_three raw Source.graph center compat
    {sourceclaim}.2.2.1 raw_D3 raw_no_isolated filler_route flag_route
theorem not_diameterAtMost_two : ¬DiameterAtMost graph 2 :=
  DiagonalFillReallocation.not_diameterAtMost_two raw Source.graph center (0,0)
theorem d{delta+1}_{n} : Fintype.card Vertex={n} ∧
    (∀v,graph.degree v≤{delta+1}) ∧ DiameterAtMost graph 3 ∧ ¬DiameterAtMost graph 2 :=
  ⟨card_vertex,degree_le,diameterAtMost_three,not_diameterAtMost_two⟩
theorem final_claim : FinalClaim := d{delta+1}_{n}
#print axioms final_claim
end {ns}
'''
 audit=f'''import DegreeDiameter.Portfolio.{prefix}Exact
open {ns}
#check (graph : SimpleGraph Vertex)
#check (label : Vertex ≃ Fin {n})
#print FinalClaim
#check d{delta+1}_{n}
#print d{delta+1}_{n}
#print axioms d{delta+1}_{n}
#print final_claim
#print axioms final_claim
#print axioms label_old
#print axioms label_copy
#print axioms label_hub
'''
 if tag=='Q8':
  defs=defs.replace('import DegreeDiameter.Portfolio.EvenQ8SourceFullExact','import DegreeDiameter.Portfolio.EvenQ8SourceDefinitions').replace('import DegreeDiameter.Portfolio.EvenQ8BalancedFullOvoidCopy82Inputs','import DegreeDiameter.Portfolio.EvenQ8BalancedFullOvoidCopy82Definitions').replace('def graph : SimpleGraph Vertex','abbrev graph : SimpleGraph Vertex')
  defs=defs.replace('  simp only [Vertex,DiagonalFillReallocation.Vertex,Fintype.card_sum,Fintype.card_prod,Fintype.card_fin,Fintype.card_unit]',f'''  change Fintype.card ((EvenQ8Source.Balanced.Vertex ⊕ CloneIndex) ⊕ Unit) = {n}
  rw [Fintype.card_sum,Fintype.card_sum,EvenQ8Source.Balanced.card_vertex,Fintype.card_prod]
  simp only [Fintype.card_fin,Fintype.card_unit]''')
  inputs='import DegreeDiameter.Portfolio.EvenQ8SourceFullBalancedInputs\nimport DegreeDiameter.Portfolio.EvenQ8BalancedFullOvoidCopy82Inputs\n'+inputs
  exact='import DegreeDiameter.Portfolio.EvenQ8SourceFullExact\n'+exact
 for suffix,body in [('Definitions',defs),('Inputs',inputs),('Exact',exact),('Audit',audit)]:
  path=(R/'formal'if suffix=='Audit'else Q)/(prefix+suffix+'.lean');assert not path.exists();path.write_text(body)
 (D/(tag+'_BRIDGE_INPUT.json')).write_text(json.dumps(dict(points=np,lines=nl,cover_slots=slots,slot_order='old point ID',new_finite_conditions=2*np,old_geometry_projection_reruns=0),indent=2)+'\n')
(D/'PREPARATION_RESULT.json').write_text(json.dumps(dict(status='TWO_CASE_FOUR_MODULES_EACH_PREPARED',CPU_seconds=time.process_time()-T,source_graph_reads=0,old_field_or_geometry_or_projection_rechecks=0),indent=2)+'\n')
print(json.dumps(dict(status='PREPARED',CPU_seconds=time.process_time()-T)))
