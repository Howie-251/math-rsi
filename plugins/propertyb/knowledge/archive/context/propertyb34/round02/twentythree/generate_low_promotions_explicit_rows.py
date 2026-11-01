"""Complete 4→5 and 5→6 low-lock promotion catalogues, with one rejection
projection per excluded vector. No whole-hypergraph enumeration occurs."""
from pathlib import Path
from itertools import permutations
from fractions import Fraction as F
import json
ROOT=Path(__file__).resolve().parents[4];HERE=Path(__file__).resolve().parent
SRC=ROOT/'context/propertyb34/round01/middle-math';OUT=ROOT/'formal/Aris4Math/ThirtyFour'
vec=lambda xs:'!['+','.join(map(str,xs))+']'
def fs(t,n):return '{'+','.join(str(i)for i in range(n)if t>>i&1)+'}' if t else '∅'
def funmu(ns,n):return '(fun T => '+''.join(f'if T={fs(t,n)} then {k} else 'for t,k in sorted(ns.items()))+'0)'
def image(t,p):return sum(1<<p[i]for i in range(len(p))if t>>i&1)
def project(ns,keep):
 ans={}
 for t,k in ns.items():
  u=sum(1<<i for i,j in enumerate(keep)if t>>j&1);ans[u]=ans.get(u,0)+k
 return {t:k for t,k in ans.items()if k}
def keyof(ns):return tuple(sorted((t,k)for t,k in ns.items()if k))
def card_spectrum(ns,n):return tuple(sum(k for t,k in ns.items()if t.bit_count()==j)for j in range(n+1))
def card_moments(ns,n):return tuple(sum(k**p for t,k in ns.items()if t.bit_count()==j)for j in range(n+1)for p in [1,2])
def write_changed(path,text):
 if not path.exists()or path.read_text()!=text:path.write_text(text)
def orbit_lookup(rows,n):
 ans={}
 for j,ns in enumerate(rows):
  for k,p in enumerate(permutations(range(n))):
   ans.setdefault(keyof({image(t,p):m for t,m in ns.items()}),(j,k))
 return ans

def generate(n):
 oldfile='FOUR_LOW_23.json' if n==4 else f'EXTEND_LOW_23_{n}.json'
 oldrows=json.loads((SRC/oldfile).read_text())['results']
 old=[{int(t):k for t,k in r['counts'].items()if k}for r in oldrows
      if min(F(r['bound']),F(r.get('joint',r)['bound']))>=1]
 rows=json.loads((SRC/f'EXTEND_LOW_23_{n+1}.json').read_text())['results']
 new=[{int(t):k for t,k in r['counts'].items()if k}for r in rows]
 oldlook=orbit_lookup(old,n);newlook=orbit_lookup(new,n+1)
 old_spectra={card_spectrum(ns,n)for ns in old}
 old_moments={card_moments(ns,n)for ns in old}
 oldperms=list(permutations(range(n)));newperms=list(permutations(range(n+1)))
 oldname='TwentyThreeFourLowClassified' if n==4 else 'TwentyThreeFiveLowClassified'
 prefix='TwentyThreeFiveLowPromotion' if n==4 else 'TwentyThreeSixLowPromotion'
 entries=[[(t,k)for t,k in sorted(ns.items())if t]for ns in old]
 records=[];stats=[];catalogues=[]
 for c,(ns,es)in enumerate(zip(old,entries)):
  cat=[]
  def rec(i,used,lams,total,vs):
   if i==len(es):cat.append(vs);return
   t,k=es[i]
   cap=min(k,6-used,*[3-lams[j]for j in range(n)if t>>j&1],(n+2-total)//t.bit_count())
   for v in range(cap+1):rec(i+1,used+v,[a+v if t>>j&1 else a for j,a in enumerate(lams)],total+v*t.bit_count(),vs+[v])
  rec(0,0,[0]*n,0,[])
  catalogues.append(cat)
  feasible=survive=0
  for vs in cat:
   out=dict(ns)
   for(t,k),v in zip(es,vs):out[t]-=v;out[t|(1<<n)]=v
   p0=6-sum(vs);out[0]-=p0;out[1<<n]=p0
   assert min(out.values())>=0
   co=[[sum(k for t,k in out.items()if t>>i&1 and t>>j&1)for j in range(n+1)]for i in range(n+1)]
   if any(co[i][j]<1 for i in range(n+1)for j in range(n+1)if i!=j):continue
   if any(sum(co[i][j]-1 for j in range(n+1)if i!=j)>2 for i in range(n+1)):continue
   feasible+=1
   if n==5:
    bad=next((x for x in range(n+1)if card_spectrum(project(out,[i for i in range(n+1)if i!=x]),n)not in old_spectra),None)
   else:
    bad=next((x for x in range(n+1)if card_moments(project(out,[i for i in range(n+1)if i!=x]),n)not in old_moments),None)
   q,perm=(0,0)if bad is not None else newlook[keyof(out)]
   if bad is None:
    survive+=1
    assert all(out.get(image(t,newperms[perm]),0)==new[q].get(t,0)for t in range(1<<(n+1)))
   code=c+len(old)*sum(v*7**i for i,v in enumerate(reversed(vs)))
   records.append((code,(bad or 0,q,perm)))
  stats.append(dict(source=c,capacity=len(cat),feasible=feasible,surviving=survive))
 used=sorted({0}|{perm for _,(_,_,perm)in records})
 dense={perm:i for i,perm in enumerate(used)}
 newperms=[newperms[perm]for perm in used]
 records=[(key,(x,q,dense[perm]))for key,(x,q,perm)in records]
 s=f'''import Aris4Math.ThirtyFour.{oldname}
import Aris4Math.ThirtyFour.TwentyThreeLowPromotionBase
namespace Aris4Math.ThirtyFour.{prefix}
open scoped BigOperators
open Aris4Math.ThirtyThree.MultiLockRecovery
open LockProjection LockExtension PromotionReconstruction
set_option maxHeartbeats 0
set_option maxRecDepth 100000
set_option synthInstance.maxSize 2000
abbrev OldCase := {oldname}.Residue
abbrev NewCase := Fin {len(new)}
abbrev OldPerm := Fin {len(oldperms)}
abbrev NewPerm := Fin {len(newperms)}
def oldCounts := {oldname}.residualCounts
'''
 s+=f'def μ : NewCase → Finset (Fin {n+1}) → ℕ := '+vec(funmu(ns,n+1)for ns in new)+'\n'
 s+=f'def entries : OldCase → List (Finset (Fin {n}) × ℕ) := '+vec('['+','.join(f'({fs(t,n)},{k})'for t,k in es)+']'for es in entries)+'\n'
 for name,ps,k in [('oldPerm',oldperms,n),('newPerm',newperms,n+1)]:
  typ='OldPerm'if name=='oldPerm'else'NewPerm'
  s+=f'def {name}Fn : {typ} → Fin {k} → Fin {k} := '+vec(vec(p)for p in ps)+'\n'
  s+=f'''theorem {name}Fn_injective : ∀ p, Function.Injective ({name}Fn p) := by decide +kernel
noncomputable def {name} (p : {typ}) : Equiv.Perm (Fin {k}) :=
  Equiv.ofBijective ({name}Fn p) ⟨{name}Fn_injective p,Finite.surjective_of_injective ({name}Fn_injective p)⟩
'''
 args=' '.join('x'+str(i)for i in range(n));vals=vec('x'+str(i)for i in range(n))
 s+=f'''theorem oldPerm_covers_vector : ∀ {args} : Fin {n},
    Function.Injective ({vals} : Fin {n} → Fin {n}) →
    ∃ p : OldPerm, ∀ i, oldPerm p i = {vals} i := by decide +kernel

theorem oldPerm_covers (σ : Equiv.Perm (Fin {n})) : ∃ p : OldPerm, oldPerm p=σ := by
  have same : {vec('σ '+str(i)for i in range(n))}=σ := by
    funext i
    fin_cases i <;> rfl
  have h := oldPerm_covers_vector {' '.join('(σ '+str(i)+')'for i in range(n))}
  rw [same] at h
  obtain ⟨p,hp⟩ := h σ.injective
  exact ⟨p,Equiv.ext hp⟩

def OldResidual (c : Finset (Fin {n}) → ℕ) : Prop :=
  ∃ r : OldCase, ∃ p : OldPerm, ∀ T, c (T.map (oldPerm p).toEmbedding)=oldCounts r T
noncomputable instance (c : Finset (Fin {n}) → ℕ) : Decidable (OldResidual c) := by
  unfold OldResidual
  infer_instance

def deletion (x : Fin {n+1}) : Fin {n} ↪ Fin {n+1} := x.succAboveEmb

def projected (x : Fin {n+1}) (c : Finset (Fin {n+1}) → ℕ) (T : Finset (Fin {n})) :=
  ∑ U : Finset (Fin {n+1}), if project (deletion x) U=T then c U else 0

def vector (c : OldCase) (values : List ℕ) := BoundedAllocations.decode (entries c) values

def newCounts (c : OldCase) (values : List ℕ) := extend (oldCounts c) (vector c values) 6

def code (c : OldCase) (values : List ℕ) : ℕ := c.val+{len(old)}*(values.foldl (fun a x => 7*a+x) 0)
'''
 witness_lookup=dict(records)
 rowlists=[]
 for c,cat in enumerate(catalogues):
  rs=[]
  for vs in cat:
   key=c+len(old)*sum(v*7**i for i,v in enumerate(reversed(vs)))
   x,q,p=witness_lookup.get(key,(0,0,0))
   rs.append('(['+','.join(map(str,vs))+f'],({x},{q},{p}))')
  rowlists.append('[\n'+',\n'.join(rs)+'\n]')
 s+=f'abbrev Witness := Fin {n+1} × NewCase × NewPerm\n'

 s+=f'''def rowCovered (c : OldCase) (values : List ℕ) (w : Witness) : Prop :=
  TwentyThreeLowPromotionBase.Feasible (newCounts c values) →
  OldResidual (projected w.1 (newCounts c values)) →
  ∀ T, newCounts c values (T.map (newPerm w.2.2).toEmbedding)=μ w.2.1 T
noncomputable instance (c : OldCase) (values : List ℕ) (w : Witness) : Decidable (rowCovered c values w) := by
  unfold rowCovered
  infer_instance

def covered (c : OldCase) (values : List ℕ) : Prop := ∃ w : Witness, rowCovered c values w

def catalogue (c : OldCase) := BoundedAllocations.enumerate
  TwentyThreeLowPromotionBase.incidenceCost (entries c) TwentyThreeLowPromotionBase.incidenceCap
end Aris4Math.ThirtyFour.{prefix}
'''
 s=s.replace(f'import Aris4Math.ThirtyFour.{oldname}',f'import Aris4Math.ThirtyFour.{oldname}\nimport Aris4Math.ThirtyFour.TwentyThreeTraceShape')
 a=s.index('def oldPermFn');b=s.index('def newPermFn',a);s=s[:a]+s[b:]
 a=s.index('theorem oldPerm_covers_vector');b=s.index('def OldResidual',a);s=s[:a]+s[b:]
 s=s.replace(f'abbrev OldPerm := Fin {len(oldperms)}\n','')
 if n==5:
  expected=vec(vec(card_spectrum(ns,n))for ns in old)
  declarations=f'''def expected : OldCase → Fin 6 → ℕ := {expected}
theorem expected_correct : ∀ r (k : Fin 6),
    TwentyThreeTraceShape.cardMass (oldCounts r) k=expected r k := by decide +kernel

'''
  condition='∃ r : OldCase, ∀ k : Fin 6, TwentyThreeTraceShape.cardMass c k=expected r k'
 else:
  expected=vec(vec(vec(sum(m**p for t,m in ns.items()if t.bit_count()==k)for p in [1,2])for k in range(n+1))for ns in old)
  declarations=f'''def expected : OldCase → Fin 5 → Fin 2 → ℕ := {expected}
theorem expected_correct : ∀ r (k : Fin 5) (p : Fin 2),
    TwentyThreeTraceShape.cardMoment (oldCounts r) k (p.val+1)=expected r k p := by decide +kernel

'''
  condition='∃ r : OldCase, ∀ k : Fin 5, ∀ p : Fin 2, TwentyThreeTraceShape.cardMoment c k (p.val+1)=expected r k p'
 s=s.replace('def OldResidual',declarations+'def OldResidual')
 s=s.replace('∃ r : OldCase, ∃ p : OldPerm, ∀ T, c (T.map (oldPerm p).toEmbedding)=oldCounts r T',condition)
 write_changed(OUT/f'{prefix}Data.lean',s)
 for c in range(len(old)):
  part=f'''import Aris4Math.ThirtyFour.{prefix}Data
namespace Aris4Math.ThirtyFour.{prefix}
set_option maxHeartbeats 0
set_option maxRecDepth 100000
set_option synthInstance.maxSize 2000
def rows{c} : List (List ℕ × Witness) := {rowlists[c]}
theorem catalogue_eq{c} : catalogue {c}=rows{c}.map Prod.fst := by decide +kernel

theorem row_coverage{c} : rows{c}.all (fun row => decide (rowCovered {c} row.1 row.2))=true := by decide +kernel

theorem coverage{c} (values : List ℕ) (mem : values∈catalogue {c}) : covered {c} values := by
  rw [catalogue_eq{c}] at mem
  obtain ⟨row,member,same⟩ := List.mem_map.mp mem
  subst values
  exact ⟨row.2,of_decide_eq_true (List.all_eq_true.mp row_coverage{c} row member)⟩
end Aris4Math.ThirtyFour.{prefix}
'''
  write_changed(OUT/f'{prefix}Coverage{c}.lean',part)
 num=''.join(f'import Aris4Math.ThirtyFour.{prefix}Coverage{c}\n'for c in range(len(old)))
 num+=f'''namespace Aris4Math.ThirtyFour.{prefix}
set_option maxHeartbeats 0
set_option maxRecDepth 100000
set_option synthInstance.maxSize 2000
'''
 num+='''theorem coverage (c : OldCase) (values : List ℕ) (mem : values∈catalogue c) : covered c values := by
  fin_cases c
'''+''.join(f'  · exact coverage{c} values mem\n'for c in range(len(old)))+f'end Aris4Math.ThirtyFour.{prefix}\n'
 write_changed(OUT/f'{prefix}Numeric.lean',num)
 return dict(old_locks=n,new_locks=n+1,projection_gate='size spectrum only'if n==5 else 'first and second cardinality moments',stored_new_permutations=len(newperms),sources=stats,lookup_records=len(records),status='generated, kernel checks pending')
summary=[generate(4),generate(5)]
(HERE/'LOW_PROMOTION_EXPORT.json').write_text(json.dumps(summary,indent=2)+'\n')
print(json.dumps(summary,indent=2))

def generate_actual(n):
 oldname='TwentyThreeFourLowClassified'if n==4 else'TwentyThreeFiveLowClassified'
 prefix='TwentyThreeFiveLowPromotion'if n==4 else'TwentyThreeSixLowPromotion'
 s=f'''import Aris4Math.ThirtyFour.{prefix}Numeric
namespace Aris4Math.ThirtyFour.{prefix}
open scoped BigOperators
open Aris4Math.ThirtyThree.MultiLockRecovery
open LockExtension PromotionCatalog PromotionReconstruction
set_option maxRecDepth 100000
set_option maxHeartbeats 0
set_option synthInstance.maxSize 2000

theorem entries_distinct : ∀ c, ((entries c).map Prod.fst).Nodup := by decide +kernel

theorem entries_values (c : OldCase) (e : Finset (Fin {n}) × ℕ) (mem : e∈entries c) :
    e.2=oldCounts c e.1 := by
  have h : ∀ c, (entries c).all (fun e => decide (e.2=oldCounts c e.1))=true := by decide +kernel
  exact of_decide_eq_true (List.all_eq_true.mp (h c) e mem)

theorem entries_support : ∀ c, ∀ T : Finset (Fin {n}),
    T≠∅ → T∉(entries c).map Prod.fst → oldCounts c T=0 := by decide +kernel

theorem old_actual (H : Simple5Hypergraph (Fin 23)) (cover : H.PairCovering)
    (edges : H.edges.card=34) (g : Fin {n} ↪ Fin 23)
    (degrees : ∀ i, H.degree (g i)=6) (notB : ¬ PropertyB H) :
    OldResidual (count H g) := by
  obtain ⟨r, σ, actual⟩ := {oldname}.actual_residual H cover edges g degrees notB
  obtain ⟨p, hp⟩ := oldPerm_covers σ
  refine ⟨r,p,?_⟩
  intro T
  rw [hp,← LockRelabel.count_comp_perm]
  exact actual T

attribute [local irreducible] covered

theorem actual_of_covered (H : Simple5Hypergraph (Fin 23)) (cover : H.PairCovering)
    (edges : H.edges.card=34) (f : Fin {n+1} ↪ Fin 23)
    (degrees : ∀ i, H.degree (f i)=6) (notB : ¬ PropertyB H)
    (c : OldCase) (values : List ℕ) (matched : covered c values)
    (actual : ∀ T, count H f T=newCounts c values T) :
    ∃ q : NewCase, ∃ σ : Equiv.Perm (Fin {n+1}),
      ∀ T, count H (σ.toEmbedding.trans f) T=μ q T := by
  have feasible := TwentyThreeLowPromotionBase.feasible_actual H cover f degrees
    (newCounts c values) actual
  unfold covered at matched
  obtain ⟨choice,matched⟩ := matched
  have projection : ∀ T, projected choice.1 (newCounts c values) T =
      count H ((deletion choice.1).trans f) T := by
    intro T
    rw [LockProjection.count_comp]
    simp only [projected,actual]
  have old := old_actual H cover edges ((deletion choice.1).trans f)
    (fun i => degrees ((deletion choice.1) i)) notB
  have residual : OldResidual (projected choice.1 (newCounts c values)) := by
    simpa only [show projected choice.1 (newCounts c values)=
      count H ((deletion choice.1).trans f) from funext projection] using old
  unfold rowCovered at matched
  refine ⟨choice.2.1,newPerm choice.2.2,?_⟩
  intro T
  rw [LockRelabel.count_comp_perm,actual]
  exact matched feasible residual T

/-- Complete actual extension from one canonical old inventory. Every
rejected projection is classified on the same original H. -/
theorem actual_extension (H : Simple5Hypergraph (Fin 23)) (cover : H.PairCovering)
    (edges : H.edges.card=34) (f : Fin {n+1} ↪ Fin 23)
    (degrees : ∀ i, H.degree (f i)=6) (notB : ¬ PropertyB H)
    (c : OldCase) (old : ∀ T, count H (restrict f) T=oldCounts c T) :
    ∃ q : NewCase, ∃ σ : Equiv.Perm (Fin {n+1}),
      ∀ T, count H (σ.toEmbedding.trans f) T=μ q T := by
  let values := (entries c).map (fun e => promotion H f e.1)
  have member : values∈catalogue c := by
    apply TwentyThreeLowPromotionBase.actual_mem H cover f degrees (entries c) (entries_distinct c)
    intro e he
    rw [old,entries_values c e he]
  have prom (T : Finset (Fin {n})) (ne : T≠∅) : vector c values T=promotion H f T := by
    apply decode_nonempty H f (entries c) ?_ T ne
    intro S nonempty absent
    have bound := promotion_le_old H f S
    rw [old,entries_support c S nonempty absent] at bound
    omega
  have actual (T : Finset (Fin {n+1})) : count H f T=newCounts c values T :=
    extend_actual H f (oldCounts c) (vector c values) 6 old prom (degrees _) T
  exact actual_of_covered H cover edges f degrees notB c values (coverage c values member) actual

/-- Every original low-lock choice is covered: first normalize its old
subset, then lift that same permutation while fixing the newly added point. -/
theorem actual (H : Simple5Hypergraph (Fin 23)) (cover : H.PairCovering)
    (edges : H.edges.card=34) (f : Fin {n+1} ↪ Fin 23)
    (degrees : ∀ i, H.degree (f i)=6) (notB : ¬ PropertyB H) :
    ∃ q : NewCase, ∃ σ : Equiv.Perm (Fin {n+1}),
      ∀ T, count H (σ.toEmbedding.trans f) T=μ q T := by
  obtain ⟨c,σ,hc⟩ := {oldname}.actual_residual H cover edges (restrict f)
    (fun i => degrees i.castSucc) notB
  let lift := LockLiftRelabel.lift σ
  let g := lift.toEmbedding.trans f
  have old : ∀ T, count H (restrict g) T=oldCounts c T := by
    intro T
    rw [show restrict g=σ.toEmbedding.trans (restrict f) from
      LockLiftRelabel.restrict_lift_trans σ f]
    exact hc T
  obtain ⟨q,τ,ht⟩ := actual_extension H cover edges g (fun i => degrees (lift i)) notB c old
  exact ⟨q,τ.trans lift,ht⟩

end Aris4Math.ThirtyFour.{prefix}
#print axioms Aris4Math.ThirtyFour.{prefix}.actual
'''
 a=s.index('  obtain ⟨p, hp⟩ := oldPerm_covers σ')
 b=s.index('\nattribute [local irreducible]',a)
 replacement=('''  refine ⟨r,?_⟩
  intro k
  exact (TwentyThreeTraceShape.cardMass_of_relabelled_counts H g σ (oldCounts r) actual k).trans
    (expected_correct r k)
'''if n==5 else'''  refine ⟨r,?_⟩
  intro k p
  exact (TwentyThreeTraceShape.cardMoment_of_relabelled_counts H g σ (oldCounts r) actual k (p.val+1)).trans
    (expected_correct r k p)
''')
 s=s[:a]+replacement+s[b:]
 write_changed(OUT/f'{prefix}.lean',s)
for n in [4,5]:generate_actual(n)
