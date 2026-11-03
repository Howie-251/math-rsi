import csv,json,os,time
from pathlib import Path

T=time.process_time();D=Path(__file__).resolve().parent
R=next(p for p in D.parents if (p/'formal/DegreeDiameter/Portfolio').is_dir())
Q=R/'formal/DegreeDiameter/Portfolio';S=D.parent;G=S.parent/'even_q8_gq_geometry_pilot'
NS='DegreeDiameter.Portfolio.EvenQ8SourceFull';OLD='DegreeDiameter.Portfolio.EvenQ8Source'

def save(path,data):
    temp=path.with_suffix(path.suffix+'.tmp');temp.write_text(json.dumps(data,indent=2)+'\n');os.replace(temp,path)
def pack(v,base=1024):return sum(x*base**i for i,x in enumerate(v))
def tree(v):
    n=1
    while n<len(v):n*=2
    v=list(v)+[0]*(n-len(v))
    def emit(w):
        if len(w)==1:return '(.leaf '+str(w[0])+')'
        return '(.node '+emit(w[::2])+' '+emit(w[1::2])+')'
    return emit(v)
def write(mod,body,audit=False):
    path=R/'formal'/('' if audit else 'DegreeDiameter/Portfolio')/(mod+'.lean')
    if path.exists():raise RuntimeError('Refuse overwrite: '+str(path))
    path.write_text(body)
def header(imports,case=None):
    out=''.join('import '+x+'\n' for x in imports)+f'namespace {NS}\n'
    out+='set_option maxRecDepth 30000\nset_option maxHeartbeats 100000000\n'
    if case:out+=f'namespace {case}\nopen {OLD}.{case}\nopen {OLD}\n'
    return out
def end(case=None):return ('end '+case+'\n' if case else '')+'end '+NS+'\n'

common=header(['DegreeDiameter.Portfolio.EvenQ8SourcePilot'])
leaves=[];assemblies=[];scopes=[]
for case,C,csvname in [('derived','Derived','DERIVED_ALL_NONINCIDENT_PROJECTIONS.csv'),('balanced','Balanced','ORIGINAL_ALL_NONINCIDENT_PROJECTIONS.csv')]:
    values=list(map(int,(S/case/'TABLES_INPUT.txt').read_text().split()))
    np,nl,a,b,j,oldn,oldm,n,m,delta=values[:10];at=10
    lp=[values[at+i*a:at+(i+1)*a]for i in range(nl)];at+=nl*a
    pl=[values[at+i*b:at+(i+1)*b]for i in range(np)];at+=np*b
    spread=values[at:at+j];at+=j;owner=values[at:at+np];assert at+np==len(values)
    inv=[{p:i for i,p in enumerate(row)}for row in lp]
    covers=[pack([pl[p].index(l)for p in row],16)for l,row in enumerate(lp)]
    common+=f'''namespace {C}
open {OLD}.{C}
open {OLD}
def coverRows : NatTable := {tree(covers)}
def coverSlot (l : Line) (i : Fin {a}) : Fin {b} :=
  ⟨(coverRows.get l.val / 16^i.val) % 16 % {b}, Nat.mod_lt _ (by decide)⟩
end {C}
'''
    rows=[{}for _ in range(np-1)]
    with (G/csvname).open()as f:
        rd=csv.reader(f);next(rd)
        for row in rd:
            p,l,q,middle=map(int,row)
            if p<np-1:rows[p][l]=(q,middle)
    modules=[]
    for p in range(np-1):
        words=[]
        for l in range(nl):
            q,middle=(p,l)if p in inv[l]else rows[p][l]
            words.append(inv[l][q]+16*middle+16384*inv[middle][p]+262144*inv[middle][q])
        mod=f'EvenQ8SourceFull{C}Row{p:03d}';modules.append(mod);leaves.append(mod)
        body=header(['DegreeDiameter.Portfolio.EvenQ8SourceDefinitions'],C)+f'''namespace Row{p:03d}
def witnessRow : NatTable := {tree(words)}
def qSlot (l : Line) : Fin {a} := ⟨witnessRow.get l.val % 16 % {a}, Nat.mod_lt _ (by decide)⟩
def connector (l : Line) : Line := ⟨(witnessRow.get l.val / 16) % 1024 % {nl}, Nat.mod_lt _ (by decide)⟩
def pSlot (l : Line) : Fin {a} := ⟨(witnessRow.get l.val / 16384) % 16 % {a}, Nat.mod_lt _ (by decide)⟩
def qConnectorSlot (l : Line) : Fin {a} := ⟨(witnessRow.get l.val / 262144) % 16 % {a}, Nat.mod_lt _ (by decide)⟩
theorem certificate : ∀ l : Line,
    linePoint (connector l) (pSlot l) = ({p} : Point) ∧
    linePoint (connector l) (qConnectorSlot l) = linePoint l (qSlot l) := by decide
theorem projection : ∀ l : Line,
    ∃ q m, Inc q l ∧ Inc ({p} : Point) m ∧ Inc q m := by
  intro l
  refine ⟨linePoint l (qSlot l),connector l,⟨qSlot l,rfl⟩,?_,?_⟩
  · exact ⟨pSlot l,(certificate l).1⟩
  · exact ⟨qConnectorSlot l,(certificate l).2⟩
#print axioms projection
end Row{p:03d}
'''+end(C)
        write(mod,body)
    hline=f'EvenQ8SourceFull{C}Hline';howner=f'EvenQ8SourceFull{C}Howner'
    leaves.extend([hline,howner])
    body=header(['DegreeDiameter.Portfolio.EvenQ8SourceFullData'],C)+f'''def restrictedLine (l : Fin {nl-1}) : Line := ⟨l.val,by omega⟩
theorem hline_certificate : ∀ (l : Fin {nl-1}) (i : Fin {a}),
    pointLine (linePoint (restrictedLine l) i) (coverSlot (restrictedLine l) i) = restrictedLine l := by decide
theorem hline : ∀ p l, Inc p l → ∃ i, pointLine p i = l := by
  intro p l h
  by_cases hl : l.val < {nl-1}
  · let small : Fin {nl-1} := ⟨l.val,hl⟩
    have he : restrictedLine small = l := Fin.ext rfl
    obtain ⟨i,hi⟩ := h
    refine ⟨coverSlot l i,?_⟩
    rw [←hi]
    have hc := hline_certificate small i
    rw [he] at hc
    exact hc
  · have he : l = lastLine := by
      apply Fin.ext
      change l.val = {nl-1}
      have := l.isLt
      omega
    subst l
    exact representative_hline p h
#print axioms hline
'''+end(C)
    write(hline,body)
    body=header(['DegreeDiameter.Portfolio.EvenQ8SourceFullData'],C)+f'''def restrictedHelper (j : Fin {j-1}) : Helper := ⟨j.val,by omega⟩
theorem howner_certificate : ∀ (j : Fin {j-1}) (i : Fin {a}),
    spreadOwner (linePoint (spread (restrictedHelper j)) i) = restrictedHelper j := by decide
theorem howner : ∀ p j, Inc p (spread j) → j = spreadOwner p := by
  intro p j h
  by_cases hj : j.val < {j-1}
  · let small : Fin {j-1} := ⟨j.val,hj⟩
    have he : restrictedHelper small = j := Fin.ext rfl
    obtain ⟨i,hi⟩ := h
    rw [←hi]
    have hc := howner_certificate small i
    rw [he] at hc
    exact hc.symm
  · have he : j = lastSpread := by
      apply Fin.ext
      change j.val = {j-1}
      have := j.isLt
      omega
    subst j
    exact representative_howner p h
#print axioms howner
'''+end(C)
    write(howner,body)
    inp=f'EvenQ8SourceFull{C}Inputs';assemblies.append(inp)
    imports=['DegreeDiameter.Portfolio.'+x for x in modules+[hline,howner]]
    body=header(imports,C)+'''theorem project : ∀ p l, ∃ q m, Inc q l ∧ Inc p m ∧ Inc q m := by
  intro p l
'''
    expression='Fin.elim0 p'
    for p in reversed(range(np)):
        proof=f'Row{p:03d}.projection l' if p<np-1 else 'complete_last_projection_row l'
        expression=f'Fin.cases ({proof}) (fun p => {expression}) p'
    body+='  exact '+expression+'\n#print axioms project\n'+end(C)
    write(inp,body)
    scopes.append(dict(case=case,np=np,nl=nl,a=a,b=b,J=j,n=n,m=m,delta=delta,new_projection_rows=np-1,new_projection_pairs=(np-1)*nl,reused_projection_point=np-1,new_hline_positions=(nl-1)*a,new_howner_positions=(j-1)*a))
common+=end();write('EvenQ8SourceFullData',common)
exact=header(['DegreeDiameter.Portfolio.'+x for x in assemblies])
for scope in scopes:
    C=scope['case'].capitalize();delta=scope['delta'];n=scope['n'];target=f'graph{delta}'
    exact+=f'''abbrev {target} : SimpleGraph {OLD}.{C}.Vertex := {OLD}.{C}.graph
namespace D{delta}_{n}
abbrev Vertex := {OLD}.{C}.Vertex
def label : Vertex ≃ Fin {n} := {OLD}.{C}.label
def FinalClaim : Prop :=
  Fintype.card Vertex = {n} ∧
  (∀ u, {target}.degree u ≤ {delta}) ∧
  DiameterAtMost {target} 3 ∧ ¬ DiameterAtMost {target} 2
theorem final_claim : FinalClaim := by
  simpa only [FinalClaim,{target},Fintype.card_fin] using
    (OppositeIncidenceSpread.order_degree_and_exact_D3
      {OLD}.{C}.oldEquiv {OLD}.{C}.linePoint {OLD}.{C}.pointLine
      {OLD}.{C}.spread {OLD}.{C}.spreadOwner (by decide)
      {C}.hline {C}.howner {C}.project (by decide))
theorem label_old (v : {OLD}.{C}.Old) : (label (.inl v)).val = v.val := rfl
theorem label_new (j : {OLD}.{C}.Helper) : (label (.inr j)).val = {n-scope['J']}+j.val := rfl
#check final_claim
#print axioms final_claim
end D{delta}_{n}
theorem d{delta}_{n} : D{delta}_{n}.FinalClaim := D{delta}_{n}.final_claim
'''
exact+=end();write('EvenQ8SourceFullExact',exact)
audit='import DegreeDiameter.Portfolio.EvenQ8SourceFullExact\nopen '+NS+'\n'
for scope in scopes:
    delta=scope['delta'];n=scope['n'];name=f'D{delta}_{n}'
    audit+=f'#check (graph{delta} : SimpleGraph {name}.Vertex)\n#check ({name}.label : {name}.Vertex ≃ Fin {n})\n#print {name}.FinalClaim\n#check {name}.final_claim\n#print {name}.final_claim\n#print axioms {name}.final_claim\n#print axioms {name}.label_old\n#print axioms {name}.label_new\n#check d{delta}_{n}\n#print d{delta}_{n}\n#print axioms d{delta}_{n}\n'
write('EvenQ8SourceFullAudit',audit,True)
plan=dict(common=['EvenQ8SourceFullData'],leaves=leaves,assembly=assemblies+['EvenQ8SourceFullExact','EvenQ8SourceFullAudit'],module_count=1+len(leaves)+len(assemblies)+2,scopes=scopes,reused_modules=['EvenQ8SourceDefinitions','EvenQ8SourcePilot'])
save(D/'MODULE_PLAN.json',plan)
save(D/'PREPARATION_RESULT.json',dict(status='GENERATED_NOT_COMPILED',CPU_seconds=time.process_time()-T,**plan))
print(json.dumps(dict(status='GENERATED',modules=plan['module_count'],CPU_seconds=time.process_time()-T)),flush=True)
