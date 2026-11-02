import json
from pathlib import Path
ROOT=Path('/inspire/hdd/global_user/mahaitong-240108120090/ar4math');D=Path(__file__).resolve().parent;P=json.loads((D.parent/'PARAMETERS.json').read_text());OUT=ROOT/'formal/DegreeDiameter/Portfolio'
def flat(v):return sum((flat(x) if isinstance(x,list) else [x] for x in v),[])
def arr(v):return '#['+', '.join(map(str,flat(v)))+']'
def rows(v):return '#['+', '.join(arr(x) for x in v)+']'
def cube(v):return '#['+', '.join(rows(x) for x in v)+']'
s='''import DegreeDiameter.Portfolio.F4Graph3840Field

namespace DegreeDiameter.Portfolio.F4Graph3840
set_option maxRecDepth 10000
set_option maxHeartbeats 20000000

'''
s+='def controllerData : Array (Array Nat) := '+rows(P['controller'])+'\n'
s+='def matrixData : Array (Array Nat) := '+rows(P['dart_matrices'])+'\n'
s+='def directionData : Array (Array Nat) := '+rows(P['directions'])+'\n'
s+='''
def controller (a : Fin 60) (p : Fin 5) : Fin 60 :=
  ⟨(controllerData.getD a.val #[]).getD p.val 0 % 60, Nat.mod_lt _ (by decide)⟩
def inversePort : Fin 5 → Fin 5 := ![1,0,3,2,4]
def matrix (a : Fin 60) (p : Fin 5) : Mat := fun i j =>
  F.ofCode ((matrixData.getD a.val #[]).getD (p.val * 9 + i.val * 3 + j.val) 0)
def direction (p : Fin 5) : Vec := fun i =>
  F.ofCode ((directionData.getD p.val #[]).getD i.val 0)

def encodeVec (x : Vec) : Fin 64 :=
  ⟨F.code (x 0) + 4 * F.code (x 1) + 16 * F.code (x 2), by
    have h0 := F.code_lt (x 0); have h1 := F.code_lt (x 1); have h2 := F.code_lt (x 2)
    omega⟩
def decodeVec (x : Fin 64) : Vec := fun i => F.ofCode (x.val / 4 ^ i.val % 4)

theorem decodeVec_encodeVec (x : Vec) : decodeVec (encodeVec x) = x := by
  have h0 := F.code_lt (x 0); have h1 := F.code_lt (x 1); have h2 := F.code_lt (x 2)
  funext i
  fin_cases i
  all_goals simp only [decodeVec, encodeVec, Fin.val_zero, Fin.val_one, Fin.val_two,
    pow_zero, pow_one, show 4 ^ 2 = 16 from rfl, Nat.div_one]
  · rw [show (F.code (x 0) + 4 * F.code (x 1) + 16 * F.code (x 2)) % 4 = F.code (x 0) by omega]
    exact F.ofCode_code _
  · rw [show (F.code (x 0) + 4 * F.code (x 1) + 16 * F.code (x 2)) / 4 % 4 = F.code (x 1) by omega]
    exact F.ofCode_code _
  · rw [show (F.code (x 0) + 4 * F.code (x 1) + 16 * F.code (x 2)) / 16 % 4 = F.code (x 2) by omega]
    exact F.ofCode_code _

theorem encodeVec_decodeVec (x : Fin 64) : encodeVec (decodeVec x) = x := by revert x; decide

def stepVec (a : Fin 60) (p : Fin 5) (t : F) (x : Vec) : Vec :=
  act (matrix a p) x + t • direction (inversePort p)
def fiberStep (a : Fin 60) (p : Fin 5) (t : F) (x : Fin 64) : Fin 64 :=
  encodeVec (stepVec a p t (decodeVec x))
def controllerOf (u : Fin 3840) : Fin 60 := ⟨u.val / 64, by omega⟩
def fiberOf (u : Fin 3840) : Fin 64 := ⟨u.val % 64, Nat.mod_lt _ (by decide)⟩
def liftAt (a : Fin 60) (x : Fin 64) : Fin 3840 :=
  ⟨64 * a.val + x.val, by have ha := a.isLt; have hx := x.isLt; omega⟩
def forward (u : Fin 3840) (p : Fin 5) (t : F) : Fin 3840 :=
  liftAt (controller (controllerOf u) p) (fiberStep (controllerOf u) p t (fiberOf u))

/-- Symmetrization of the exact generated edge relation, with loops excluded. -/
def graph : SimpleGraph (Fin 3840) where
  Adj u v := u ≠ v ∧ ((∃ p t, forward u p t = v) ∨ (∃ p t, forward v p t = u))
  symm := by intro u v h; exact ⟨Ne.symm h.1, h.2.elim Or.inr Or.inl⟩
  loopless := by intro u h; exact h.1 rfl

instance : DecidableRel graph.Adj := by
  intro u v
  change Decidable (u ≠ v ∧ ((∃ p t, forward u p t = v) ∨ (∃ p t, forward v p t = u)))
  infer_instance

theorem controller_reverse : ∀ (a : Fin 60) (p : Fin 5),
  controller (controller a p) (inversePort p) = a := by decide
theorem controller_no_loops : ∀ (a : Fin 60) (p : Fin 5), controller a p ≠ a := by decide
theorem inversePort_involution : ∀ p, inversePort (inversePort p) = p := by decide

theorem controllerOf_liftAt (a : Fin 60) (x : Fin 64) : controllerOf (liftAt a x) = a := by
  apply Fin.ext
  change (64*a.val+x.val)/64=a.val
  have hx:=x.isLt
  omega

theorem fiberOf_liftAt (a : Fin 60) (x : Fin 64) : fiberOf (liftAt a x) = x := by
  apply Fin.ext
  change (64*a.val+x.val)%64=x.val
  have hx:=x.isLt
  omega

theorem liftAt_parts (u : Fin 3840) : liftAt (controllerOf u) (fiberOf u) = u := by
  apply Fin.ext
  change 64*(u.val/64)+u.val%64=u.val
  omega

theorem forward_liftAt (a : Fin 60) (x : Fin 64) (p : Fin 5) (t : F) :
  forward (liftAt a x) p t = liftAt (controller a p) (fiberStep a p t x) := by
  simp only [forward, controllerOf_liftAt, fiberOf_liftAt]

theorem forward_ne_self (u : Fin 3840) (p : Fin 5) (t : F) : forward u p t ≠ u := by
  intro h
  have hc := congrArg controllerOf h
  simp only [forward, controllerOf_liftAt] at hc
  exact controller_no_loops (controllerOf u) p hc

theorem forward_adj (u : Fin 3840) (p : Fin 5) (t : F) : graph.Adj u (forward u p t) :=
  ⟨Ne.symm (forward_ne_self u p t), Or.inl ⟨p,t,rfl⟩⟩

#print axioms forward_adj
end DegreeDiameter.Portfolio.F4Graph3840
'''
(OUT/'F4Graph3840.lean').write_text(s)
# Certificate transport is exact finite GF4 arithmetic, not graph search.
C=P['controller'];T=P['dart_matrices'];L=P['directions'];iv=P['inverse_ports'];R=json.loads((D.parent/'ROUTE_CERTIFICATE.json').read_text())
def mul(a,b):
 c=0
 while b:
  if b&1:c^=a
  b>>=1;a<<=1
  if a&4:a^=7
 return c
def mv(M,x):return [mul(row[0],x[0])^mul(row[1],x[1])^mul(row[2],x[2]) for row in M]
def step(a,p,t,x):return [y^mul(t,l) for y,l in zip(mv(T[a][p],x),L[iv[p]])]
def rt(a,ps,n,x):
 for p,t in zip(ps,n):x=step(a,p,t,x);a=C[a][p]
 return x
def inverse(M):
 A=[row[:]+[int(i==j) for j in range(3)] for i,row in enumerate(M)]
 for j in range(3):
  k=next(i for i in range(j,3) if A[i][j]);A[j],A[k]=A[k],A[j]
  s=next(t for t in range(1,4) if mul(t,A[j][j])==1);A[j]=[mul(s,t) for t in A[j]]
  for i in range(3):
   if i!=j:
    c=A[i][j];A[i]=[x^mul(c,y) for x,y in zip(A[i],A[j])]
 return [row[3:] for row in A]
def vec(n):return [n%4,n//4%4,n//16]
def code(x):return x[0]+4*x[1]+16*x[2]
words=[[0]*60 for _ in range(60)]; inverses=[[[0]*9 for _ in range(60)] for _ in range(60)]
for item in R['rank3_pairs']:
 a,b=item['source'],item['target'];ps=item['word']['ports'];words[a][b]=ps[0]+5*ps[1]+25*ps[2]
 cols=[rt(a,ps,[int(i==j) for i in range(3)],[0,0,0]) for j in range(3)]
 inverses[a][b]=flat(inverse([list(row) for row in zip(*cols)]))
adj=[]
for a in range(60):
 row=[]
 for p in range(5):
  out=[None]*64
  for before in [True,False]:
   for q in range(5):
    ps=[q,iv[q],p] if before else [p,q,iv[q]]
    for n in range(64):
     d=code(rt(a,ps,vec(n),[0,0,0]));v=n+64*q+(0 if before else 320)
     if out[d] is None:out[d]=v
  assert all(v is not None for v in out)
  row.append(out)
 adj.append(row)
s='''import DegreeDiameter.Portfolio.F4Graph3840Routes
namespace DegreeDiameter.Portfolio.F4Graph3840
set_option maxRecDepth 30000
set_option maxHeartbeats 20000000
'''
s+='def wordData : Array (Array Nat) := '+rows(words)+'\n'
def intern(data):
 pool=[];lookup={};indices=[]
 for row in data:
  ir=[]
  for v in row:
   k=tuple(flat(v))
   if k not in lookup:lookup[k]=len(pool);pool.append(list(k))
   ir.append(lookup[k])
  indices.append(ir)
 return pool,indices
nbpool,nbindices=intern(inverses);adjpool,adjindices=intern(adj)
s+='def nbInversePool : Array (Array Nat) := '+rows(nbpool)+'\n'
s+='def nbInverseIndex : Array (Array Nat) := '+rows(nbindices)+'\n'
s+='def adjacentPool : Array (Array Nat) := '+rows(adjpool)+'\n'
s+='def adjacentIndex : Array (Array Nat) := '+rows(adjindices)+'\n'
s+='''
def controllerWord (a b : Fin 60) : Fin 125 :=
  ⟨(wordData.getD a.val #[]).getD b.val 0 % 125,Nat.mod_lt _ (by decide)⟩
def wordP0 (w : Fin 125) : Fin 5 := ⟨w.val%5,Nat.mod_lt _ (by decide)⟩
def wordP1 (w : Fin 125) : Fin 5 := ⟨w.val/5%5,Nat.mod_lt _ (by decide)⟩
def wordP2 (w : Fin 125) : Fin 5 := ⟨w.val/25%5,Nat.mod_lt _ (by decide)⟩
def nbInverse (a b : Fin 60) : Mat := fun i j =>
  F.ofCode ((nbInversePool.getD ((nbInverseIndex.getD a.val #[]).getD b.val 0) #[]).getD (i.val*3+j.val) 0)
def nbNoise (a b : Fin 60) (d : Vec) : Vec := act (nbInverse a b) d

def adjacentDecoder (a : Fin 60) (p : Fin 5) (d : Fin 64) : Nat :=
  (adjacentPool.getD ((adjacentIndex.getD a.val #[]).getD p.val 0) #[]).getD d.val 0
def adjBefore (a : Fin 60) (p : Fin 5) (d : Fin 64) : Prop := adjacentDecoder a p d < 320
instance (a : Fin 60) (p : Fin 5) (d : Fin 64) : Decidable (adjBefore a p d) := inferInstanceAs (Decidable (_ < _))
def adjQ (a : Fin 60) (p : Fin 5) (d : Fin 64) : Fin 5 :=
  ⟨adjacentDecoder a p d /64%5,Nat.mod_lt _ (by decide)⟩
def adjNoise (a : Fin 60) (p : Fin 5) (d : Fin 64) : Vec :=
  decodeVec ⟨adjacentDecoder a p d%64,Nat.mod_lt _ (by decide)⟩
def adjP0 (a : Fin 60) (p : Fin 5) (d : Fin 64) : Fin 5 := if adjBefore a p d then adjQ a p d else p
def adjP1 (a : Fin 60) (p : Fin 5) (d : Fin 64) : Fin 5 := if adjBefore a p d then inversePort (adjQ a p d) else adjQ a p d
def adjP2 (a : Fin 60) (p : Fin 5) (d : Fin 64) : Fin 5 := if adjBefore a p d then p else inversePort (adjQ a p d)
end DegreeDiameter.Portfolio.F4Graph3840
'''
(OUT/'F4Graph3840RouteData.lean').write_text(s)
(D/'CERTIFICATE_TRANSPORT.json').write_text(json.dumps(dict(status='LOCAL_GF4_CERTIFICATE_TRANSPORT_ONLY',rank_pairs=len(R['rank3_pairs']),adjacent_darts=len(R['adjacent_pencils']),adjacent_noise_targets=19200,graph_BFS=False,solver_called=False,unproved_Lean_obligations='Kernel discharge of basis and decoder checks'),indent=2)+'\n')
s='''import DegreeDiameter.Portfolio.F4Graph3840DecoderInterface
import DegreeDiameter.Portfolio.F4Graph3840RouteData
import DegreeDiameter.Portfolio.F4Graph3840Linear
import DegreeDiameter.Portfolio.F4Graph3840FastTables
namespace DegreeDiameter.Portfolio.F4Graph3840
set_option maxRecDepth 30000
set_option maxHeartbeats 100000000
'''
for a in range(60):
 s+=f'''\ntheorem controller_row_{a} : ∀ (b : Fin 60),
    (¬∃ p, controller {a} p = b) →
    routeController {a} (wordP0 (controllerWord {a} b)) (wordP1 (controllerWord {a} b)) (wordP2 (controllerWord {a} b)) = b := by decide +kernel

theorem nb_basis_row_{a} : ∀ (b : Fin 60) (j : Fin 3),
    (¬∃ p, controller {a} p = b) →
    routeVec {a} (wordP0 (controllerWord {a} b)) (wordP1 (controllerWord {a} b)) (wordP2 (controllerWord {a} b))
      (nbNoise {a} b (basisVec j)) 0 = basisVec j := by
  simp only [routeVec,stepVec,matrix_eq_fast]
  decide +kernel

theorem adjacent_row_{a} : ∀ (p : Fin 5) (d : Fin 64),
    routeVec {a} (adjP0 {a} p d) (adjP1 {a} p d) (adjP2 {a} p d) (adjNoise {a} p d) 0 = decodeVec d := by
  simp only [routeVec,stepVec,matrix_eq_fast]
  decide +kernel
'''
for name,args,typ in [
 ('controller_valid','(a b : Fin 60)','(¬∃ p, controller a p = b) → routeController a (wordP0 (controllerWord a b)) (wordP1 (controllerWord a b)) (wordP2 (controllerWord a b)) = b'),
 ('nb_basis_valid','(a b : Fin 60) (j : Fin 3)','(¬∃ p, controller a p = b) → routeVec a (wordP0 (controllerWord a b)) (wordP1 (controllerWord a b)) (wordP2 (controllerWord a b)) (nbNoise a b (basisVec j)) 0 = basisVec j'),
 ('adjacent_valid','(a : Fin 60) (p : Fin 5) (d : Fin 64)','routeVec a (adjP0 a p d) (adjP1 a p d) (adjP2 a p d) (adjNoise a p d) 0 = decodeVec d')]:
 s+=f'\ntheorem {name} {args} : {typ} := by\n  fin_cases a\n'
 for a in range(60):
  row=('controller_row_' if name=='controller_valid' else 'nb_basis_row_' if name=='nb_basis_valid' else 'adjacent_row_')+str(a)
  s+='  · exact '+row+(' b' if name=='controller_valid' else ' b j' if name=='nb_basis_valid' else ' p d')+'\n'
s+='''
theorem nb_noise_valid (a b : Fin 60) (h : ¬∃ p, controller a p = b) (d : Vec) :
  routeVec a (wordP0 (controllerWord a b)) (wordP1 (controllerWord a b)) (wordP2 (controllerWord a b)) (nbNoise a b d) 0 = d :=
  noise_decode_of_basis a b (fun j => nb_basis_valid a b j h) d

#print axioms nb_noise_valid
#print axioms adjacent_valid
end DegreeDiameter.Portfolio.F4Graph3840
'''
(OUT/'F4Graph3840Certificates.lean').write_text(s)

mpool,mindices=intern(T)
s='import DegreeDiameter.Portfolio.F4Graph3840Routes\nnamespace DegreeDiameter.Portfolio.F4Graph3840\nset_option maxRecDepth 30000\nset_option maxHeartbeats 20000000\n'
s+='def matrixPool : Array (Array Nat) := '+rows(mpool)+'\n'
s+='def matrixIndex : Array (Array Nat) := '+rows(mindices)+'\n'
s+='''
def fastMatrix (a : Fin 60) (p : Fin 5) : Mat := fun i j =>
  F.ofCode ((matrixPool.getD ((matrixIndex.getD a.val #[]).getD p.val 0) #[]).getD (i.val*3+j.val) 0)
/-- Kernel checked equality to every entry of the original300dart matrix table. -/
theorem matrix_eq_fast : ∀ (a : Fin 60) (p : Fin 5), matrix a p = fastMatrix a p := by decide +kernel
#print axioms matrix_eq_fast
end DegreeDiameter.Portfolio.F4Graph3840
'''
(OUT/'F4Graph3840FastTables.lean').write_text(s)

# Independent controller rows are separate modules for reusable kernel receipts.
full=(OUT/'F4Graph3840Certificates.lean').read_text()
header='import DegreeDiameter.Portfolio.F4Graph3840RouteData\nimport DegreeDiameter.Portfolio.F4Graph3840Linear\nimport DegreeDiameter.Portfolio.F4Graph3840FastTables\nnamespace DegreeDiameter.Portfolio.F4Graph3840\nset_option maxRecDepth 30000\nset_option maxHeartbeats 100000000\n'
for a in range(60):
 start=full.index(f'theorem controller_row_{a} :')
 end=full.index(f'theorem controller_row_{a+1} :') if a<59 else full.index('theorem controller_valid')
 target=OUT/f'F4Graph3840CertificateRow{a:02d}.lean'
 body=header+full[start:end]+'\nend DegreeDiameter.Portfolio.F4Graph3840\n'
 if not target.exists() or target.read_text()!=body:target.write_text(body)
start=full.index('theorem controller_valid')
body='import DegreeDiameter.Portfolio.F4Graph3840DecoderInterface\n'+''.join(f'import DegreeDiameter.Portfolio.F4Graph3840CertificateRow{a:02d}\n' for a in range(60))+'namespace DegreeDiameter.Portfolio.F4Graph3840\nset_option maxRecDepth 30000\nset_option maxHeartbeats 100000000\n'+full[start:]
(OUT/'F4Graph3840Certificates.lean').write_text(body)
