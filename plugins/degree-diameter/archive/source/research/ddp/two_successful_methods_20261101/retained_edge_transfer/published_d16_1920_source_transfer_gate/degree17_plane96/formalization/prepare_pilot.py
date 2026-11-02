from pathlib import Path
import json,time
started=time.process_time();D=Path(__file__).resolve().parent
ROOT=next(p for p in D.parents if(p/'formal/DegreeDiameter/Portfolio').is_dir());OUT=ROOT/'formal/DegreeDiameter/Portfolio'
P=json.loads((ROOT/'research/ddp/breadth_20261027_wave4/mizuno_d3_source/construction.json').read_text())
C,T,L,iv=P['controller'],P['matrices'],P['outgoing_return_directions'],[1,0,3,2]
def flat(x):return sum((flat(y)if isinstance(y,list)else[y]for y in x),[])
def arr(x):return '#['+', '.join(map(str,flat(x)))+']'
def rows(x):return '#['+', '.join(arr(y)for y in x)+']'
def intern(data):
    pool=[];lookup={};indices=[]
    for row in data:
        ii=[]
        for v in row:
            key=tuple(flat(v))
            if key not in lookup:lookup[key]=len(pool);pool.append(list(key))
            ii.append(lookup[key])
        indices.append(ii)
    return pool,indices
def write(name,text):
    path=ROOT/'formal'/f'{name}.lean'if name.endswith('PilotAudit')else OUT/f'{name}.lean'
    assert not path.exists(),f'New pilot module already exists: {name}'
    path.write_text(text)
def adapt(text):
    text=text.replace('namespace DegreeDiameter.Portfolio.F4Graph3840','namespace DegreeDiameter.Portfolio.F4Graph1920\nopen F4Graph3840')
    text=text.replace('end DegreeDiameter.Portfolio.F4Graph3840','end DegreeDiameter.Portfolio.F4Graph1920')
    return text.replace('Fin 3840','Fin 1920').replace('Fin 60','Fin 30').replace('Fin 5','Fin 4').replace('% 60','% 30')
matrix_pool,matrix_index=intern(T)
old=(OUT/'F4Graph3840.lean').read_text();body=old[old.index('def controller ('):]
body=body.replace('def inversePort : Fin 5 → Fin 5 := ![1,0,3,2,4]','def inversePort : Fin 5 → Fin 5 := ![1,0,3,2]')
body=body.replace('F.ofCode ((matrixData.getD a.val #[]).getD (p.val * 9 + i.val * 3 + j.val) 0)',
    'F.ofCode ((matrixPool.getD ((matrixIndex.getD a.val #[]).getD p.val 0) #[]).getD (i.val*3+j.val) 0)')
body=body.replace('end DegreeDiameter.Portfolio.F4Graph3840','')
body=adapt(body)
definitions='''import DegreeDiameter.Portfolio.F4Graph3840Field
import DegreeDiameter.Portfolio.FullNeighborhoodClones
import Mathlib.Logic.Equiv.Fin.Basic
namespace DegreeDiameter.Portfolio.F4Graph1920
open F4Graph3840
set_option maxRecDepth 20000
set_option maxHeartbeats 40000000
'''
definitions+='def controllerData : Array (Array Nat) := '+rows(C)+'\n'
definitions+='def matrixPool : Array (Array Nat) := '+rows(matrix_pool)+'\n'
definitions+='def matrixIndex : Array (Array Nat) := '+rows(matrix_index)+'\n'
definitions+='def directionData : Array (Array Nat) := '+rows(L)+'\n'+body
definitions+='''
def SourceFinalClaim : Prop := Fintype.card (Fin 1920)=1920 ∧
  (∀v,graph.degree v≤16) ∧ DiameterAtMost graph 3 ∧ ¬DiameterAtMost graph 2
namespace Clone2016
abbrev Vertex := Fin 1920 ⊕ Fin 96
def layer : Fin 6 → Fin 30 := ![0,3,5,7,9,16]
def planeVec (a b : Fin 4) : Vec := ![F.ofCode a.val,F.ofCode b.val,F.ofCode a.val+F.ofCode b.val]
def center (j : Fin 96) : Fin 1920 :=
  liftAt (layer ⟨j.val/16,by have h:=j.isLt;omega⟩)
    (encodeVec (planeVec ⟨j.val/4%4,Nat.mod_lt _ (by decide)⟩ ⟨j.val%4,Nat.mod_lt _ (by decide)⟩))
abbrev graph := FullNeighborhoodClones.graph F4Graph1920.graph center
instance : DecidableRel graph.Adj := inferInstanceAs
  (DecidableRel (FullNeighborhoodClones.graph F4Graph1920.graph center).Adj)
def label : Vertex ≃ Fin 2016 := finSumFinEquiv
theorem label_new (j : Fin 96) : (label (.inr j)).val=1920+j.val := rfl
def FinalClaim : Prop := Fintype.card Vertex=2016 ∧
  (∀v,graph.degree v≤17) ∧ DiameterAtMost graph 3 ∧ ¬DiameterAtMost graph 2
#check (label : Vertex ≃ Fin 2016)
end Clone2016
end DegreeDiameter.Portfolio.F4Graph1920
'''
write('F4Graph1920Definitions',definitions)
matrix=adapt((OUT/'F4Graph3840MatrixCertificate.lean').read_text()).replace('import DegreeDiameter.Portfolio.F4Graph3840\n','import DegreeDiameter.Portfolio.F4Graph1920Definitions\n')
write('F4Graph1920MatrixCertificate',matrix)
routes=adapt((OUT/'F4Graph3840Routes.lean').read_text()).replace('import DegreeDiameter.Portfolio.F4Graph3840MatrixCertificate','import DegreeDiameter.Portfolio.F4Graph1920MatrixCertificate')
routes=routes.replace('degree_le_twenty','degree_le_sixteen').replace('≤ 20','≤ 16').replace('_ = 20','_ = 16')
write('F4Graph1920Routes',routes)
linear=adapt((OUT/'F4Graph3840Linear.lean').read_text()).replace('import DegreeDiameter.Portfolio.F4Graph3840Routes','import DegreeDiameter.Portfolio.F4Graph1920Routes')
write('F4Graph1920Linear',linear)

# New row0 witness transport only. No old rank/field law verifier or graph is run.
def mul(a,b):
    c=0
    while b:
        if b&1:c^=a
        b>>=1;a<<=1
        if a&4:a^=7
    return c
def mv(M,x):return [mul(row[0],x[0])^mul(row[1],x[1])^mul(row[2],x[2])for row in M]
def step(a,p,t,x):return [y^mul(t,l)for y,l in zip(mv(T[a][p],x),L[iv[p]])]
def route(a,ps,noises):
    x=[0,0,0]
    for p,t in zip(ps,noises):x=step(a,p,t,x);a=C[a][p]
    return x
def inverse(M):
    A=[row[:]+[int(i==j)for j in range(3)]for i,row in enumerate(M)]
    for j in range(3):
        k=next(i for i in range(j,3)if A[i][j]);A[j],A[k]=A[k],A[j]
        s=next(t for t in range(1,4)if mul(t,A[j][j])==1);A[j]=[mul(s,t)for t in A[j]]
        for i in range(3):
            if i!=j:
                c=A[i][j];A[i]=[x^mul(c,y)for x,y in zip(A[i],A[j])]
    return[row[3:]for row in A]
words=[0]*30;inverses=[[0]*9 for _ in range(30)];nb=0
for rec in P['pair_certificate']:
    if rec['u']!=0 or rec['kind']!='full_rank':continue
    b=rec['v'];ps=rec['word'];words[b]=ps[0]+4*ps[1]+16*ps[2]
    cols=[route(0,ps,[int(i==j)for i in range(3)])for j in range(3)]
    inverses[b]=flat(inverse([list(row)for row in zip(*cols)]));nb+=1
adj=[]
for p in range(4):
    out=[None]*64
    for side in range(2):
        for q in range(4):
            ps=[q,iv[q],p]if side==0 else[p,q,iv[q]]
            for n in range(64):
                v=route(0,ps,[n%4,n//4%4,n//16]);d=v[0]+4*v[1]+16*v[2]
                if out[d]is None:out[d]=n+64*q+256*side
    assert all(v is not None for v in out);adj.append(out)
assert nb==26
pool,idx=intern([inverses]);idx=idx[0]
data='''import DegreeDiameter.Portfolio.F4Graph1920Linear
namespace DegreeDiameter.Portfolio.F4Graph1920.Row0
open F4Graph3840
'''
data+='def wordData : Array Nat := '+arr(words)+'\n'
data+='def inversePool : Array (Array Nat) := '+rows(pool)+'\n'
data+='def inverseIndex : Array Nat := '+arr(idx)+'\n'
data+='def adjacentData : Array (Array Nat) := '+rows(adj)+'\n'
data+='''
def controllerWord (b : Fin 30) : Fin 64 := ⟨wordData.getD b.val 0 % 64,Nat.mod_lt _ (by decide)⟩
def wordP0 (w : Fin 64) : Fin 4 := ⟨w.val%4,Nat.mod_lt _ (by decide)⟩
def wordP1 (w : Fin 64) : Fin 4 := ⟨w.val/4%4,Nat.mod_lt _ (by decide)⟩
def wordP2 (w : Fin 64) : Fin 4 := ⟨w.val/16%4,Nat.mod_lt _ (by decide)⟩
def nbInverse (b : Fin 30) : Mat := fun i j =>
  F.ofCode ((inversePool.getD (inverseIndex.getD b.val 0) #[]).getD (i.val*3+j.val) 0)
def nbNoise (b : Fin 30) (d : Vec) : Vec := act (nbInverse b) d
def adjacentDecoder (p : Fin 4) (d : Fin 64) : Nat := (adjacentData.getD p.val #[]).getD d.val 0
def adjBefore (p : Fin 4) (d : Fin 64) : Prop := adjacentDecoder p d < 256
instance (p : Fin 4) (d : Fin 64) : Decidable (adjBefore p d) := inferInstanceAs (Decidable (_ < _))
def adjQ (p : Fin 4) (d : Fin 64) : Fin 4 := ⟨adjacentDecoder p d/64%4,Nat.mod_lt _ (by decide)⟩
def adjNoise (p : Fin 4) (d : Fin 64) : Vec := decodeVec ⟨adjacentDecoder p d%64,Nat.mod_lt _ (by decide)⟩
def adjP0 (p : Fin 4) (d : Fin 64) : Fin 4 := if adjBefore p d then adjQ p d else p
def adjP1 (p : Fin 4) (d : Fin 64) : Fin 4 := if adjBefore p d then inversePort (adjQ p d) else adjQ p d
def adjP2 (p : Fin 4) (d : Fin 64) : Fin 4 := if adjBefore p d then p else inversePort (adjQ p d)
end DegreeDiameter.Portfolio.F4Graph1920.Row0
'''
write('F4Graph1920Row0Data',data)
certificate='''import DegreeDiameter.Portfolio.F4Graph1920Row0Data
namespace DegreeDiameter.Portfolio.F4Graph1920.Row0
open F4Graph3840
set_option maxRecDepth 30000
set_option maxHeartbeats 100000000
theorem controller_row : ∀(b : Fin 30),(¬∃p,controller 0 p=b) →
    routeController 0 (wordP0 (controllerWord b)) (wordP1 (controllerWord b)) (wordP2 (controllerWord b))=b := by decide +kernel
theorem nb_basis_row : ∀(b : Fin 30)(j : Fin 3),(¬∃p,controller 0 p=b) →
    routeVec 0 (wordP0 (controllerWord b)) (wordP1 (controllerWord b)) (wordP2 (controllerWord b))
      (nbNoise b (basisVec j)) 0=basisVec j := by
  simp only [routeVec,stepVec]
  decide +kernel
theorem adjacent_row : ∀(p : Fin 4)(d : Fin 64),
    routeVec 0 (adjP0 p d) (adjP1 p d) (adjP2 p d) (adjNoise p d) 0=decodeVec d := by
  simp only [routeVec,stepVec]
  decide +kernel
#print axioms nb_basis_row
#print axioms adjacent_row
end DegreeDiameter.Portfolio.F4Graph1920.Row0
'''
write('F4Graph1920Row0Certificate',certificate)
walks='''import DegreeDiameter.Portfolio.F4Graph1920Row0Certificate
namespace DegreeDiameter.Portfolio.F4Graph1920.Row0
open F4Graph3840
theorem noise_decode (b : Fin 30)(h : ¬∃p,controller 0 p=b)(d : Vec) :
    routeVec 0 (wordP0 (controllerWord b)) (wordP1 (controllerWord b)) (wordP2 (controllerWord b)) (nbNoise b d) 0=d := by
  have heq := additive_ext
    (fun d => routeVec 0 (wordP0 (controllerWord b)) (wordP1 (controllerWord b)) (wordP2 (controllerWord b)) (nbNoise b d) 0) id
    (by intro x y;dsimp only;unfold nbNoise;rw [act_add,route_noise_add]) (by intros;rfl)
    (by intro t x;dsimp only;unfold nbNoise;rw [act_smul,route_noise_smul]) (by intros;rfl)
    (fun j => nb_basis_row b j h)
  exact congrFun heq d
theorem adjacent_controller (p : Fin 4)(d : Fin 64) :
    routeController 0 (adjP0 p d) (adjP1 p d) (adjP2 p d)=controller 0 p := by
  unfold adjP0 adjP1 adjP2
  split_ifs <;> simp only [routeController,controller_reverse]
theorem adjacent_center (p : Fin 4)(d : Fin 64)(x : Vec) :
    routeVec 0 (adjP0 p d) (adjP1 p d) (adjP2 p d) 0 x=stepVec 0 p 0 x := by
  unfold adjP0 adjP1 adjP2
  split_ifs
  · exact route_before_center 0 p (adjQ p d) x
  · exact route_after_center 0 p (adjQ p d) x
theorem row0_full_walk_bound (x : Fin 64)(v : Fin 1920) :
    ∃w : graph.Walk (liftAt 0 x) v,w.length≤3 := by
  by_cases h : ∃p,controller 0 p=controllerOf v
  · obtain ⟨p,hp⟩ := h
    let d := encodeVec (decodeVec (fiberOf v)-stepVec 0 p 0 (decodeVec x))
    apply bounded_walk_of_route (liftAt 0 x) v (adjP0 p d) (adjP1 p d) (adjP2 p d) (adjNoise p d)
    · simpa only [controllerOf_liftAt] using (adjacent_controller p d).trans hp
    · simp only [controllerOf_liftAt,fiberOf_liftAt]
      rw [route_affine,adjacent_row,adjacent_center]
      simp only [d,decodeVec_encodeVec]
      abel
  · let b := controllerOf v
    let w := controllerWord b
    let center := routeVec 0 (wordP0 w) (wordP1 w) (wordP2 w) 0 (decodeVec x)
    let d := decodeVec (fiberOf v)-center
    apply bounded_walk_of_route (liftAt 0 x) v (wordP0 w) (wordP1 w) (wordP2 w) (nbNoise b d)
    · simpa only [controllerOf_liftAt] using controller_row b h
    · simp only [controllerOf_liftAt,fiberOf_liftAt]
      rw [route_affine,noise_decode b h]
      change center+(decodeVec (fiberOf v)-center)=decodeVec (fiberOf v)
      abel
#print axioms row0_full_walk_bound
end DegreeDiameter.Portfolio.F4Graph1920.Row0
'''
write('F4Graph1920Row0Walks',walks)
audit='''import DegreeDiameter.Portfolio.F4Graph1920Row0Walks
open DegreeDiameter.Portfolio.F4Graph1920
#check (graph : SimpleGraph (Fin 1920))
#check (Clone2016.label : Clone2016.Vertex ≃ Fin 2016)
#print SourceFinalClaim
#print Clone2016.FinalClaim
#check Row0.row0_full_walk_bound
#print Row0.row0_full_walk_bound
#print axioms Row0.row0_full_walk_bound
#print axioms degree_le_sixteen
#print axioms bounded_walk_of_route
#print axioms inverse_basis
'''
write('F4Graph1920PilotAudit',audit)
mods=['F4Graph1920Definitions','F4Graph1920MatrixCertificate','F4Graph1920Routes','F4Graph1920Linear','F4Graph1920Row0Data','F4Graph1920Row0Certificate','F4Graph1920Row0Walks','F4Graph1920PilotAudit']
receipt=dict(status='LITERAL_NEW_SOURCE_PILOT_MODULES_WRITTEN_NOT_COMPILED',CPU_seconds=time.process_time()-started,
    modules=mods,new_matrix_pool_size=len(matrix_pool),new_row0_NB_words=26,new_row0_adjacent_darts=4,new_row0_residual_decoders=256,
    coefficient_generation='Only new row0 inverse-noise/decoder witnesses; not old rank/verifier execution',
    source_recipe='research/ddp/breadth_20261027_wave4/mizuno_d3_source/construction.json',old_modules_modified_or_recompiled=False,
    source_BFS_solver_or_old_field_rank_checks=0,whole_pilot_CPU_budget_seconds=120,per_module_CPU_limit_seconds=60)
(D/'PREPARATION_RESULT.json').write_text(json.dumps(receipt,indent=2)+'\n')
print(json.dumps(receipt))
