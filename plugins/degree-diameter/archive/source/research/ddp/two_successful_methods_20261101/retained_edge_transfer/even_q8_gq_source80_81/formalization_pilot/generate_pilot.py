import csv,json
from pathlib import Path
from time import process_time

start=process_time();D=Path(__file__).resolve().parent
R=next(p for p in D.parents if (p/'formal/DegreeDiameter/Portfolio').is_dir())
Q=R/'formal/DegreeDiameter/Portfolio';source=D.parent;geometry=source.parent/'even_q8_gq_geometry_pilot'
prefix='EvenQ8Source';ns='DegreeDiameter.Portfolio.'+prefix

def pack(row,base=1024):return sum(v*base**i for i,v in enumerate(row))
def tree(values):
    n=1
    while n<len(values):n*=2
    values=list(values)+[0]*(n-len(values))
    def emit(v):
        if len(v)==1:return '(.leaf '+str(v[0])+')'
        return '(.node '+emit(v[::2])+' '+emit(v[1::2])+')'
    return emit(values)

defs=f'''import DegreeDiameter.Portfolio.OppositeIncidenceSpreadFamily
namespace {ns}
set_option maxRecDepth 30000
set_option maxHeartbeats 50000000
inductive NatTable where
  | leaf : Nat → NatTable
  | node : NatTable → NatTable → NatTable
def NatTable.get : NatTable → Nat → Nat
  | .leaf v, _ => v
  | .node even odd, i => if i % 2 = 0 then NatTable.get even (i/2) else NatTable.get odd (i/2)
'''
pilot=f'''import DegreeDiameter.Portfolio.{prefix}Definitions
namespace {ns}
set_option maxRecDepth 30000
set_option maxHeartbeats 100000000
'''
scopes=[]
for case,namespace,csvname in [('derived','Derived','DERIVED_ALL_NONINCIDENT_PROJECTIONS.csv'),('balanced','Balanced','ORIGINAL_ALL_NONINCIDENT_PROJECTIONS.csv')]:
    words=list(map(int,(source/case/'TABLES_INPUT.txt').read_text().split()));np,nl,a,b,j,oldn,oldm,n,m,delta=words[:10];at=10
    lp=[words[at+i*a:at+(i+1)*a]for i in range(nl)];at+=nl*a
    pl=[words[at+i*b:at+(i+1)*b]for i in range(np)];at+=np*b
    spread=words[at:at+j];at+=j;owner=words[at:at+np];assert at+np==len(words)
    last=np-1;projection={}
    with(geometry/csvname).open()as f:
        reader=csv.reader(f);next(reader)
        for row in reader:
            if int(row[0])==last:projection[int(row[1])]=(int(row[2]),int(row[3]))
    row_words=[]
    for l in range(nl):
        if last in lp[l]:q,middle=last,l
        else:q,middle=projection[l]
        i=lp[l].index(q);ip=lp[middle].index(last);iq=lp[middle].index(q)
        row_words.append(i+16*middle+16384*ip+262144*iq)
    line_inverse=[pl[p].index(nl-1)for p in lp[-1]]
    for rows,limit in [(lp,np),(pl,nl)]:
        for row in rows:
            payload=pack(row);assert all((payload//1024**i)%1024==v and 0<=v<limit for i,v in enumerate(row))
    defs+=f'''namespace {namespace}
abbrev Point := Fin {np}
abbrev Line := Fin {nl}
abbrev Old := Fin {oldn}
abbrev Helper := Fin {j}
abbrev Vertex := Old ⊕ Helper
def oldEquiv : Old ≃ Point × Line := (finProdFinEquiv (m:={np}) (n:={nl})).symm
def label : Vertex ≃ Fin {n} := finSumFinEquiv
def lineRows : NatTable := {tree([pack(r)for r in lp])}
def pointRows : NatTable := {tree([pack(r)for r in pl])}
def spreadRows : NatTable := {tree(spread)}
def ownerRows : NatTable := {tree(owner)}
def linePoint (l : Line) (i : Fin {a}) : Point :=
  ⟨((lineRows.get l.val / 1024^i.val) % 1024) % {np}, Nat.mod_lt _ (by decide)⟩
def pointLine (p : Point) (i : Fin {b}) : Line :=
  ⟨((pointRows.get p.val / 1024^i.val) % 1024) % {nl}, Nat.mod_lt _ (by decide)⟩
def spread (j : Helper) : Line := ⟨spreadRows.get j.val % {nl}, Nat.mod_lt _ (by decide)⟩
def spreadOwner (p : Point) : Helper := ⟨ownerRows.get p.val % {j}, Nat.mod_lt _ (by decide)⟩
abbrev Inc := OppositeIncidenceSpread.Inc linePoint
def graph : SimpleGraph Vertex := OppositeIncidenceSpread.graph oldEquiv linePoint spread
instance : DecidableRel graph.Adj := inferInstanceAs
  (DecidableRel (OppositeIncidenceSpread.graph oldEquiv linePoint spread).Adj)
theorem old_label_coordinates (p : Point) (l : Line) :
    (oldEquiv.symm (p,l)).val = l.val+{nl}*p.val := rfl
theorem label_old (v : Old) : (label (.inl v)).val = v.val := rfl
theorem label_new (h : Helper) : (label (.inr h)).val = {oldn}+h.val := rfl
theorem card_vertex : Fintype.card Vertex = {n} := by
  simp only [Fintype.card_sum,Fintype.card_fin]
def lastPoint : Point := {last}
def lastLine : Line := {nl-1}
def lastSpread : Helper := {j-1}
def projectionRow : NatTable := {tree(row_words)}
def qSlot (l : Line) : Fin {a} := ⟨projectionRow.get l.val % 16 % {a}, Nat.mod_lt _ (by decide)⟩
def connector (l : Line) : Line := ⟨(projectionRow.get l.val / 16) % 1024 % {nl}, Nat.mod_lt _ (by decide)⟩
def pSlot (l : Line) : Fin {a} := ⟨(projectionRow.get l.val / 16384) % 16 % {a}, Nat.mod_lt _ (by decide)⟩
def qConnectorSlot (l : Line) : Fin {a} := ⟨(projectionRow.get l.val / 262144) % 16 % {a}, Nat.mod_lt _ (by decide)⟩
def lastLineInverseSlot (i : Fin {a}) : Fin {b} :=
  ⟨({pack(line_inverse,16)} / 16^i.val) % 16 % {b}, Nat.mod_lt _ (by decide)⟩
#check (label : Vertex ≃ Fin {n})
#print graph
end {namespace}
'''
    pilot+=f'''namespace {namespace}
/-- All {nl} point/line pairs at actual point {last},with two checked equalities
and the first incidence given by qSlot itself. -/
theorem complete_last_projection_row_certificate : ∀ l : Line,
    linePoint (connector l) (pSlot l) = lastPoint ∧
    linePoint (connector l) (qConnectorSlot l) = linePoint l (qSlot l) := by decide
theorem complete_last_projection_row : ∀ l : Line,
    ∃ q m, Inc q l ∧ Inc lastPoint m ∧ Inc q m := by
  intro l
  refine ⟨linePoint l (qSlot l),connector l,⟨qSlot l,rfl⟩,?_,?_⟩
  · exact ⟨pSlot l,(complete_last_projection_row_certificate l).1⟩
  · exact ⟨qConnectorSlot l,(complete_last_projection_row_certificate l).2⟩
theorem representative_hline_certificate : ∀ i : Fin {a},
    pointLine (linePoint lastLine i) (lastLineInverseSlot i) = lastLine := by decide
theorem representative_hline : ∀ p, Inc p lastLine → ∃ i, pointLine p i = lastLine := by
  intro p h
  obtain ⟨i,hi⟩ := h
  refine ⟨lastLineInverseSlot i,?_⟩
  rw [←hi]
  exact representative_hline_certificate i
theorem representative_howner_certificate : ∀ i : Fin {a},
    spreadOwner (linePoint (spread lastSpread) i) = lastSpread := by decide
theorem representative_howner : ∀ p, Inc p (spread lastSpread) → lastSpread = spreadOwner p := by
  intro p h
  obtain ⟨i,hi⟩ := h
  rw [←hi]
  exact (representative_howner_certificate i).symm
#check complete_last_projection_row
#print axioms complete_last_projection_row
#print axioms representative_hline
#print axioms representative_howner
end {namespace}
'''
    scopes.append({'case':case,'point':last,'line_range':[0,nl-1],'pairs':nl,'nonincident_CSV_witnesses':len(projection),'hline_line':nl-1,'hline_slots':a,'howner_spread':j-1,'howner_slots':a,'packed_table_representation':'balanced parity tree,1024-base Nat rows'})
defs+='end '+ns+'\n';pilot+='end '+ns+'\n'
(Q/(prefix+'Definitions.lean')).write_text(defs);(Q/(prefix+'Pilot.lean')).write_text(pilot)
compiler=(source.parent/'opposite_gq77_spread64/published_partial_ovoid33/multiplicity73_79_family/formalization/compile.py').read_text()
compiler=compiler.replace("mod in {'GQ77Published33CloneFamilyUpperExact','GQ77Published33CloneFamilyUpperAudit'}","mod in {'EvenQ8SourceDefinitions','EvenQ8SourcePilot'}")
compiler=compiler.replace('GQ77Published33CloneFamilyUpper',prefix).replace('spent+budget<=300','spent+budget<=90')
(D/'compile.py').write_text(compiler)
(D/'PREPARATION_RESULT.json').write_text(json.dumps({'status':'TWO_MODULES_PREPARED_NO_SOURCE_TARGET_CLAIM','CPU_seconds':process_time()-start,'row_scopes':scopes,'total_projection_pairs':1225,'new_old_graph_or_field_checks':0,'source_files_modified':False},indent=2)+'\n')
(D/'STAGE_STATE.json').write_text(json.dumps({'status':'PREPARED_NOT_YET_COMPILED','row_scopes':scopes,'running':False,'active_modules':[],'concrete_source_Lean_complete':False},indent=2)+'\n')
print(json.dumps({'status':'TWO_MODULES_PREPARED','CPU_seconds':process_time()-start,'row_scopes':scopes}))
