import itertools,json,time
from pathlib import Path
R=Path('/inspire/hdd/global_user/mahaitong-240108120090/ar4math');D=Path(__file__).resolve().parent;P=D.parent;S=P.parent
t=time.process_time();Q=R/'formal/DegreeDiameter/Portfolio';ns='F9Graph56862'
cp=json.loads((S/'PARAMETERS.json').read_text());xp=json.loads((S.parent/'r6_f9_projective_halves/cross_port_extension/PARAMETERS.json').read_text())
ct=cp['controller'];rev=cp['inverse_ports'];assert rev==[1,0,3,2,4,5] and len(ct)==78
charts={x['chart_id']:x['matrix'] for x in xp['charts']}
ids=['cross_0_1_forward','cross_0_1_reverse','cross_2_3_forward','cross_2_3_reverse','self_4_plus','self_4_minus','self_5_plus','self_5_minus']
pool=[charts[x] for x in ids];mi=[[p if p<4 else 2*p-4+(a>ct[a][p]) for p in range(6)] for a in range(78)]
def add(a,b):return (a%3+b%3)%3+3*((a//3+b//3)%3)
def neg(a):return (-a%3)%3+3*((-(a//3))%3)
def mul(a,b):return (a%3*(b%3)-a//3*(b//3))%3+3*((a%3*(b//3)+a//3*(b%3))%3)
def vec(xs):return '!['+', '.join(map(str,xs))+']'
def arr(xs):return '#['+', '.join(arr(x) if isinstance(x,list) else str(x) for x in xs)+']'
def fv(n):return f'F.c{n}'
decl='''import DegreeDiameter.Portfolio.SingleExtension
import Mathlib.Data.Fin.VecNotation
import Mathlib.Algebra.Ring.Basic
import Mathlib.Tactic.FinCases
import Mathlib.Tactic.Abel
import Mathlib.Tactic.Ring
import Mathlib.Tactic.DeriveFintype
namespace DegreeDiameter.Portfolio.F9Graph56862
set_option maxRecDepth 20000
set_option maxHeartbeats 40000000
/-- code a+3b denotes a+bw, with w²=-1 over F3. -/
inductive F where
  | c0 | c1 | c2 | c3 | c4 | c5 | c6 | c7 | c8
  deriving DecidableEq, Fintype
namespace F
instance : Zero F := ⟨c0⟩
instance : One F := ⟨c1⟩
def add : F → F → F
'''
decl+=''.join(f'  | c{a},c{b} => c{add(a,b)}\n' for a in range(9) for b in range(9))
decl+='def mul : F → F → F\n'+''.join(f'  | c{a},c{b} => c{mul(a,b)}\n' for a in range(9) for b in range(9))
decl+='def neg : F → F\n'+''.join(f'  | c{a} => c{neg(a)}\n' for a in range(9))
decl+='''instance : Add F := ⟨add⟩
instance : Mul F := ⟨mul⟩
instance : Neg F := ⟨neg⟩
instance : CommRing F where
  add_assoc := by decide +kernel
  zero_add := by decide +kernel
  add_zero := by decide +kernel
  add_comm := by decide +kernel
  neg_add_cancel := by decide +kernel
  nsmul := nsmulRec
  zsmul := zsmulRec
  mul_assoc := by decide +kernel
  one_mul := by decide +kernel
  mul_one := by decide +kernel
  mul_comm := by decide +kernel
  left_distrib := by decide +kernel
  right_distrib := by decide +kernel
  zero_mul := by decide +kernel
  mul_zero := by decide +kernel
def ofCode (n : Nat) : F := match n % 9 with
'''
decl+=''.join(f'  | {a} => c{a}\n' for a in range(8))+'  | _ => c8\n'
decl+='def code : F → Nat\n'+''.join(f'  | c{a} => {a}\n' for a in range(9))
decl+='''theorem code_lt (a : F) : code a < 9 := by cases a <;> decide
theorem ofCode_code (a : F) : ofCode (code a) = a := by cases a <;> rfl
theorem code_ofCode (a : Fin 9) : code (ofCode a.val) = a.val := by revert a; decide +kernel
end F
'''
tail=(Q/'F4Graph3840Field.lean').read_text().split('abbrev Vec :=',1)[1]
decl+='abbrev Vec :='+tail.replace('F4Graph3840',ns)
(Q/(ns+'Field.lean')).write_text(decl)
old=(Q/'F4Graph3840.lean').read_text();start=old.index('def encodeVec');end=old.index('/-- Symmetrization')
body=old[start:];body=body.replace('Fin 60','Fin 78').replace('Fin 5','Fin 6').replace('Fin 64','Fin 729').replace('Fin 3840','Fin 56862').replace('3840','56862').replace('F4Graph3840',ns)
body=body.replace('16','81').replace('64','729').replace('4 *','9 *').replace('4 ^','9 ^').replace('% 4','% 9').replace('/ 4','/ 9').replace('= 4','= 9').replace('pow_one','pow_one')
# The first coordinate modulus and bounds in numeric omega statements also use q=9.
body=body.replace(') % 4',') % 9').replace('show 4','show 9').replace('F4Graph56862',ns)
matrixvec=vec([vec([vec([fv(x) for x in row]) for row in mat]) for mat in pool])
head=f'''import DegreeDiameter.Portfolio.{ns}Field
namespace DegreeDiameter.Portfolio.{ns}
set_option maxRecDepth 20000
set_option maxHeartbeats 40000000
def controllerData : Array (Array Nat) := {arr(ct)}
def chartData : Array (Array Nat) := {arr(mi)}
def controller (a : Fin 78) (p : Fin 6) : Fin 78 :=
  ⟨(controllerData.getD a.val #[]).getD p.val 0 % 78, Nat.mod_lt _ (by decide)⟩
def inversePort : Fin 6 → Fin 6 := ![1,0,3,2,4,5]
def matrixPool : Fin 8 → Mat := {matrixvec}
def chart (a : Fin 78) (p : Fin 6) : Fin 8 :=
  ⟨(chartData.getD a.val #[]).getD p.val 0 % 8, Nat.mod_lt _ (by decide)⟩
def matrix (a : Fin 78) (p : Fin 6) : Mat := matrixPool (chart a p)
def direction : Fin 6 → Vec := {vec([vec([fv(x) for x in row]) for row in xp['port_vectors']])}
'''
(Q/(ns+'.lean')).write_text(head+body)
# Matrix inverse/direction checks are small468dart checks, using only8actual charts.
mat=(Q/'F4Graph3840MatrixCertificate.lean').read_text().replace('F4Graph3840',ns).replace('Fin 60','Fin 78').replace('Fin 5','Fin 6').replace('by decide','by decide +kernel')
(Q/(ns+'MatrixCertificate.lean')).write_text(mat)
routes=(Q/'F4Graph3840Routes.lean').read_text().replace('F4Graph3840',ns).replace('Fin 60','Fin 78').replace('Fin 5','Fin 6').replace('Fin 64','Fin 729').replace('Fin 3840','Fin 56862').replace('3840','56862')
a=routes.index('theorem vec_add_self');b=routes.index('theorem stepVec_zero');routes=routes[:a]+routes[b:]
routes=routes.replace(') t (stepVec a p t x)',') (-t) (stepVec a p t x)').replace(') t (fiberStep a p t x)',') (-t) (fiberStep a p t x)')
routes=routes.replace('(inversePort p) t = u','(inversePort p) (-t) = u').replace('rw [add_assoc, vec_add_self, add_zero]','simp only [neg_smul]\n  abel')
routes=routes.replace('⟨inversePort p,t,?_⟩','⟨inversePort p,-t,?_⟩').replace('degree_le_twenty','degree_le_fifty_four').replace('≤ 20','≤ 54').replace('_ = 20','_ = 54')
(Q/(ns+'Routes.lean')).write_text(routes)
linear=(Q/'F4Graph3840Linear.lean').read_text().replace('F4Graph3840',ns).replace('Fin 60','Fin 78').replace('Fin 5','Fin 6')
linear=linear.replace('theorem route_before_center', '''theorem stepVec_reverse_zero (a : Fin 78) (p : Fin 6) (x : Vec) :
  stepVec (controller a p) (inversePort p) 0 (stepVec a p 0 x) = x := by
  simpa only [neg_zero] using stepVec_reverse a p 0 x

theorem route_before_center''').replace('controller_reverse,stepVec_reverse]','controller_reverse,stepVec_reverse_zero]').replace('Pi.zero_apply,stepVec_reverse]','Pi.zero_apply,stepVec_reverse_zero]')
(Q/(ns+'Linear.lean')).write_text(linear)
(D/'PREPARATION_RESULT.json').write_text(json.dumps(dict(status='GENERATED_NEW_FIXED_FIELD_GRAPH_LINEAR_PILOT_SOURCES',CPU_seconds=time.process_time()-t,chart_ids=ids,controller_order=78,old_sources_changed=False),indent=2)+'\n')
print('Generated new F9 Field/Graph/Matrix/Routes/Linear sources; no old source changed.')
