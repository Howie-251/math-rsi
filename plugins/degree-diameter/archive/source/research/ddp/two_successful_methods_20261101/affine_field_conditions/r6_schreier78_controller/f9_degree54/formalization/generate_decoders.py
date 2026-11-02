import itertools,json,time
from pathlib import Path
R=Path('/inspire/hdd/global_user/mahaitong-240108120090/ar4math');D=Path(__file__).resolve().parent;P=D.parent;Q=R/'formal/DegreeDiameter/Portfolio';ns='F9Graph56862'
t0=time.process_time();d=json.loads((P/'PARAMETERS.json').read_text());ct=d['controller'];mi=d['dart_chart_index'];mp=d['matrices'];ell=d['directions'];rp=d['inverse_ports']
def add(a,b):return (a%3+b%3)%3+3*((a//3+b//3)%3)
def neg(a):return (-a%3)%3+3*((-(a//3))%3)
def mul(a,b):return d['field']['multiplication'][a][b]
def av(x,y):return tuple(add(a,b) for a,b in zip(x,y))
def scale(t,x):return tuple(mul(t,a) for a in x)
def act(m,x):return tuple(add(add(mul(row[0],x[0]),mul(row[1],x[1])),mul(row[2],x[2])) for row in m)
def invert(m):
 a=[list(r)+[int(i==j) for j in range(3)] for i,r in enumerate(m)]
 for j in range(3):
  k=next((i for i in range(j,3) if a[i][j]),None)
  if k is None:return None
  a[k],a[j]=a[j],a[k];s=d['field']['inverses'][a[j][j]];a[j]=[mul(s,x) for x in a[j]]
  for i in range(3):
   if i!=j:
    f=neg(a[i][j]);a[i]=[add(x,mul(f,y)) for x,y in zip(a[i],a[j])]
 return [r[3:] for r in a]
def arr(xs):return '#['+', '.join(arr(x) if isinstance(x,list) else str(x) for x in xs)+']'
def vec(xs):return '!['+', '.join(map(str,xs))+']'
wp=[];invpool=[[[1,0,0],[0,1,0],[0,0,1]]];invmap={tuple(sum(invpool[0],[])):0};ii=[]
for a in range(78):
 words=[0]*78;invs=[0]*78;found=set()
 for p,q,r in itertools.product(range(6),repeat=3):
  b=ct[a][p];c=ct[b][q];end=ct[c][r]
  if end in found or end in ct[a]:continue
  mr=mp[mi[c][r]];mq=mp[mi[b][q]]
  cols=[act(mr,act(mq,ell[rp[p]])),act(mr,ell[rp[q]]),tuple(ell[rp[r]])]
  m=[[cols[j][i] for j in range(3)] for i in range(3)];inv=invert(m)
  if inv is None:continue
  found.add(end);words[end]=p+6*q+36*r;key=tuple(sum(inv,[]))
  if key not in invmap:invmap[key]=len(invpool);invpool.append(inv)
  invs[end]=invmap[key]
 assert set(range(78))-set(ct[a])<=found
 wp.append(words);ii.append(invs)
ad=[]
for c in range(8):
 out=[None]*729;target=d['chart_target_ports'][c];m=mp[c]
 for before,q,s,t in itertools.product(range(2),range(6),range(9),range(9)):
  noise=av(scale(s,act(m,ell[q]) if before==0 else ell[q]),scale(t,ell[target]));code=noise[0]+9*noise[1]+81*noise[2]
  if out[code] is None:out[code]=486*before+81*q+s+9*t
 assert all(x is not None for x in out);ad.append(out)
poolflat=[sum(m,[]) for m in invpool]
data=f'''import DegreeDiameter.Portfolio.{ns}Linear
namespace DegreeDiameter.Portfolio.{ns}
set_option maxRecDepth 30000
set_option maxHeartbeats 100000000
def wordData : Array (Array Nat) := {arr(wp)}
def nbInversePool : Array (Array Nat) := {arr(poolflat)}
def nbInverseIndex : Array (Array Nat) := {arr(ii)}
def controllerWord (a b : Fin 78) : Fin 216 :=
  ⟨(wordData.getD a.val #[]).getD b.val 0 % 216,Nat.mod_lt _ (by decide)⟩
def wordP0 (w : Fin 216) : Fin 6 := ⟨w.val%6,Nat.mod_lt _ (by decide)⟩
def wordP1 (w : Fin 216) : Fin 6 := ⟨w.val/6%6,Nat.mod_lt _ (by decide)⟩
def wordP2 (w : Fin 216) : Fin 6 := ⟨w.val/36%6,Nat.mod_lt _ (by decide)⟩
def nbInverse (a b : Fin 78) : Mat := fun i j =>
  F.ofCode ((nbInversePool.getD ((nbInverseIndex.getD a.val #[]).getD b.val 0) #[]).getD (i.val*3+j.val) 0)
def nbNoise (a b : Fin 78) (d : Vec) : Vec := act (nbInverse a b) d
def adjacentPool : Array (Array Nat) := {arr(ad)}
def adjacentDecoder (c : Fin 8) (d : Fin 729) : Nat :=
  (adjacentPool.getD c.val #[]).getD d.val 0
def chartTarget : Fin 8 → Fin 6 := ![1,0,3,2,4,4,5,5]
def chartBefore (c : Fin 8) (d : Fin 729) : Prop := adjacentDecoder c d < 486
instance (c : Fin 8) (d : Fin 729) : Decidable (chartBefore c d) := inferInstanceAs (Decidable (_ < _))
def chartQ (c : Fin 8) (d : Fin 729) : Fin 6 := ⟨adjacentDecoder c d /81%6,Nat.mod_lt _ (by decide)⟩
def chartS (c : Fin 8) (d : Fin 729) : F := F.ofCode (adjacentDecoder c d%9)
def chartT (c : Fin 8) (d : Fin 729) : F := F.ofCode (adjacentDecoder c d/9%9)
def planeNoise (c : Fin 8) (d : Fin 729) : Vec :=
  (if chartBefore c d then chartS c d • act (matrixPool c) (direction (chartQ c d))
    else chartS c d • direction (chartQ c d)) + chartT c d • direction (chartTarget c)
def adjBefore (a : Fin 78) (p : Fin 6) (d : Fin 729) : Prop := chartBefore (chart a p) d
instance (a : Fin 78) (p : Fin 6) (d : Fin 729) : Decidable (adjBefore a p d) := inferInstanceAs (Decidable (chartBefore _ _))
def adjQ (a : Fin 78) (p : Fin 6) (d : Fin 729) : Fin 6 := chartQ (chart a p) d
def adjNoise (a : Fin 78) (p : Fin 6) (d : Fin 729) : Vec :=
  if adjBefore a p d then ![0,chartS (chart a p) d,chartT (chart a p) d]
  else ![chartT (chart a p) d,0,chartS (chart a p) d]
def adjP0 (a : Fin 78) (p : Fin 6) (d : Fin 729) : Fin 6 := if adjBefore a p d then adjQ a p d else p
def adjP1 (a : Fin 78) (p : Fin 6) (d : Fin 729) : Fin 6 := if adjBefore a p d then inversePort (adjQ a p d) else adjQ a p d
def adjP2 (a : Fin 78) (p : Fin 6) (d : Fin 729) : Fin 6 := if adjBefore a p d then p else inversePort (adjQ a p d)
end DegreeDiameter.Portfolio.{ns}
'''
(Q/(ns+'RouteData.lean')).write_text(data)
for a in range(1):
 text=f'''import DegreeDiameter.Portfolio.{ns}RouteData
namespace DegreeDiameter.Portfolio.{ns}
set_option maxRecDepth 30000
set_option maxHeartbeats 100000000
theorem controller_row_{a} : ∀ (b : Fin 78),
    (¬∃ p, controller {a} p = b) →
    routeController {a} (wordP0 (controllerWord {a} b)) (wordP1 (controllerWord {a} b)) (wordP2 (controllerWord {a} b)) = b := by decide +kernel
theorem nb_basis_row_{a} : ∀ (b : Fin 78) (j : Fin 3),
    (¬∃ p, controller {a} p = b) →
    routeVec {a} (wordP0 (controllerWord {a} b)) (wordP1 (controllerWord {a} b)) (wordP2 (controllerWord {a} b))
      (nbNoise {a} b (basisVec j)) 0 = basisVec j := by decide +kernel
#print axioms nb_basis_row_{a}
end DegreeDiameter.Portfolio.{ns}
'''
 (Q/(ns+f'CertificateRow{a:02d}.lean')).write_text(text)
for c in range(8):
 text=f'''import DegreeDiameter.Portfolio.{ns}RouteData
namespace DegreeDiameter.Portfolio.{ns}
set_option maxRecDepth 30000
set_option maxHeartbeats 100000000
theorem adjacent_chart_{c} : ∀ d : Fin 729, planeNoise {c} d = decodeVec d := by decide +kernel
#print axioms adjacent_chart_{c}
end DegreeDiameter.Portfolio.{ns}
'''
 (Q/(ns+f'AdjacentChart{c}.lean')).write_text(text)
(D/'DECODER_PREPARATION_RESULT.json').write_text(json.dumps(dict(status='GENERATED_SELECTED_THREE_PORT_INVERSE_AND_EIGHT_CHART_PENCILS',CPU_seconds=time.process_time()-t0,controller_pairs=6084,nb_pairs=5616,nb_inverse_pool=len(invpool),adjacent_chart_points=8*729,root_BFS_runs=0),indent=2)+'\n')
print('Generated fixed decoder data and finite certificate rows/charts; inverse pool',len(invpool),'CPU',time.process_time()-t0)
