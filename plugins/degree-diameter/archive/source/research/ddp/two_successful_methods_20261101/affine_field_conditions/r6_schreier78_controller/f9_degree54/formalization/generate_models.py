import json,re,time
from pathlib import Path
R=Path('/inspire/hdd/global_user/mahaitong-240108120090/ar4math');D=Path(__file__).resolve().parent;P=D.parent;Q=R/'formal/DegreeDiameter/Portfolio';N='F9Graph56862';t=time.process_time()
d=json.loads((P/'PARAMETERS.json').read_text());s=(Q/(N+'RouteData.lean')).read_text()
def arr(name):return json.loads(re.search(r'^def '+name+r' .*? := (.+)$',s,re.M).group(1).replace('#',''))
def array(x):return '#['+', '.join(array(y) if isinstance(y,list) else str(y) for y in x)+']'
wp=arr('wordData');ii=arr('nbInverseIndex');ct=d['controller'];ci=d['dart_chart_index'];shape={}
for a in range(78):
 for b in range(78):
  if b in ct[a]:continue
  w=wp[a][b];p=w%6;q=w//6%6;r=w//36%6;mid=ct[a][p];z=(d['inverse_ports'][p],ci[mid][q],ci[ct[mid][q]][r])
  assert ii[a][b]!=0
  if ii[a][b] in shape:assert shape[ii[a][b]]==z
  shape[ii[a][b]]=z
assert set(shape)==set(range(1,170)) and len(set(shape.values()))==169
table=[list(shape[k]) for k in range(1,170)]
text=f'''import DegreeDiameter.Portfolio.{N}RouteData
import Mathlib.Data.Fintype.EquivFin
namespace DegreeDiameter.Portfolio.{N}
set_option maxRecDepth 30000
set_option maxHeartbeats 100000000
def modelData : Array (Array Nat) := {array(table)}
def modelIndex (a b : Fin 78) : Fin 169 :=
  ⟨(((nbInverseIndex.getD a.val #[]).getD b.val 0)-1)%169,Nat.mod_lt _ (by decide)⟩
def modelFirst (k : Fin 169) : Fin 6 :=
  ⟨(modelData.getD k.val #[]).getD 0 0 %6,Nat.mod_lt _ (by decide)⟩
def modelSecond (k : Fin 169) : Fin 8 :=
  ⟨(modelData.getD k.val #[]).getD 1 0 %8,Nat.mod_lt _ (by decide)⟩
def modelThird (k : Fin 169) : Fin 8 :=
  ⟨(modelData.getD k.val #[]).getD 2 0 %8,Nat.mod_lt _ (by decide)⟩
def modelInverse (k : Fin 169) : Mat := fun i j =>
  F.ofCode ((nbInversePool.getD (k.val+1) #[]).getD (i.val*3+j.val) 0)
def modelNoise (k : Fin 169) (n : Vec) : Vec :=
  act (matrixPool (modelThird k))
    (act (matrixPool (modelSecond k)) (n 0 • direction (modelFirst k)) +
      n 1 • direction (chartTarget (modelSecond k))) +
    n 2 • direction (chartTarget (modelThird k))
def PairCheck (a b : Fin 78) : Prop :=
  let w := controllerWord a b
  let p := wordP0 w; let q := wordP1 w; let r := wordP2 w
  let k := modelIndex a b
  routeController a p q r = b ∧
  (nbInverseIndex.getD a.val #[]).getD b.val 0 = k.val+1 ∧
  inversePort p = modelFirst k ∧
  chart (controller a p) q = modelSecond k ∧
  chart (controller (controller a p) q) r = modelThird k
instance (a b : Fin 78) : Decidable (PairCheck a b) := by unfold PairCheck; infer_instance
end DegreeDiameter.Portfolio.{N}
'''
(Q/(N+'Models.lean')).write_text(text)
for b in range(13):
 text=f'''import Mathlib.Logic.Equiv.Fin.Basic
import DegreeDiameter.Portfolio.{N}Models
namespace DegreeDiameter.Portfolio.{N}
set_option maxRecDepth 30000
set_option maxHeartbeats 100000000
theorem model_basis_chunk_{b} : ∀ (j : Fin 13) (i : Fin 3),
    let k := (finProdFinEquiv (m:=13) (n:=13)) (({b} : Fin 13),j)
    modelNoise k (act (modelInverse k) (basisVec i)) = basisVec i := by decide +kernel
#print axioms model_basis_chunk_{b}
end DegreeDiameter.Portfolio.{N}
'''
 (Q/(N+f'ModelChunk{b:02d}.lean')).write_text(text)
for b in range(6):
 text=f'''import Mathlib.Logic.Equiv.Fin.Basic
import DegreeDiameter.Portfolio.{N}Models
namespace DegreeDiameter.Portfolio.{N}
set_option maxRecDepth 30000
set_option maxHeartbeats 100000000
theorem pair_check_chunk_{b} : ∀ (j : Fin 13) (b : Fin 78),
    let a := (finProdFinEquiv (m:=6) (n:=13)) (({b} : Fin 6),j)
    (¬∃ p, controller a p = b) → PairCheck a b := by decide +kernel
#print axioms pair_check_chunk_{b}
end DegreeDiameter.Portfolio.{N}
'''
 (Q/(N+f'PairChunk{b}.lean')).write_text(text)
(D/'MODEL_PREPARATION_RESULT.json').write_text(json.dumps(dict(CPU_seconds=time.process_time()-t,actual_selected_NB_route_types=169,nondefault_inverse_indices=list(range(1,170)),types_per_inverse_index=1,finite_model_basis_checks=507,pair_alignment_checks=5616,old_raw_nb_row00_retained=True),indent=2)+'\n')
print('Generated169noise types,13model chunks,6pair alignment chunks;CPU',time.process_time()-t)
