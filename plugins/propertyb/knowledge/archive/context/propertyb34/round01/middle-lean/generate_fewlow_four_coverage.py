"""Complete sparse promotion coverage, bound to actual old/new inventories."""
from pathlib import Path
from itertools import product,permutations
import json
P=Path(__file__).resolve().parents[1]/'middle-math'
OUT=Path(__file__).resolve().parents[4]/'formal/Aris4Math/ThirtyFour'
def fs(t,n):return '∅' if t==0 else '{'+','.join(str(i)for i in range(n)if t>>i&1)+'}'
def mat(rows):return '!['+','.join('!['+','.join(map(str,r))+']'for r in rows)+']'
def perm_counts(ns,p):return {sum(1<<p[i]for i in range(4)if t>>i&1):m for t,m in ns.items() if m}
def code(c,vals):
 r=0
 for x in vals:r=8*r+x
 return c+6*r
parts=['''import Aris4Math.ThirtyFour.TwentyThreeFewLowBase
import Aris4Math.ThirtyFour.PromotionReconstruction
import Aris4Math.ThirtyFour.LockRelabel
namespace Aris4Math.ThirtyFour.TwentyThreeFewLowFourCoverage
open scoped BigOperators
open Aris4Math.ThirtyThree.MultiLockRecovery
open Aris4Math.ThirtyFour.LockExtension
open Aris4Math.ThirtyFour.PromotionCatalog
open Aris4Math.ThirtyFour.PromotionReconstruction
set_option maxHeartbeats 0
set_option maxRecDepth 100000
set_option synthInstance.maxSize 1000
''']
replay=[]
for l,h,name,base in [(1,2,'OneLow','oneLow'),(2,1,'TwoLow','twoLow')]:
 old=json.loads((P/f'FEW_LOW23_{l}_{h}.json').read_text())['results']
 new=json.loads((P/f'FEW_LOW23_{l}_{h+1}.json').read_text())['results']
 perms=[p for p in permutations(range(4)) if all((i<l)==(p[i]<l)for i in range(4))]
 lookup={}
 for row in new:
  ns={int(k):v for k,v in row['counts'].items()}
  # Equality desired: newActual(sigma(T))=representative(T).
  for pi,perm in enumerate(perms):
   target=perm_counts(ns,perm)
   key=tuple(sorted(target.items()))
   lookup.setdefault(key,(row['group'],pi))
 s=[f'namespace {name}\nopen TwentyThreeFewLowBase (Case {base})\nabbrev NewCase := Fin {len(new)}\nabbrev Perm := Fin {len(perms)}\n']
 s.append('def μ : NewCase → Finset (Fin 4) → ℕ\n')
 for r in new:s.append('  | '+str(r['group'])+', T => '+' else '.join('if T='+fs(int(t),4)+' then '+str(m)for t,m in r['counts'].items())+' else 0\n')
 s.append('  | _, _ => 0\n')
 s.append('def entries : Case → List (Finset (Fin 3) × ℕ)\n')
 entries=[]
 for c,r in enumerate(old):
  es=[(int(t),m)for t,m in r['counts'].items()if int(t)];entries.append(es)
  s.append(f'  | {c} => ['+','.join('('+fs(t,3)+','+str(m)+')'for t,m in es)+']\n')
 caps=[1]*l+[3]*h
 s.append('def cap : Option (Fin 3) → ℕ\n  | none => 7\n  | some i => !['+','.join(map(str,caps))+'] i\n')
 s.append('def permFn : Perm → Fin 4 → Fin 4 := '+mat(perms)+'\n')
 s.append('''theorem permFn_injective : ∀ p, Function.Injective (permFn p) := by decide +kernel
noncomputable def perm (p : Perm) : Equiv.Perm (Fin 4) :=
  Equiv.ofBijective (permFn p) ⟨permFn_injective p,Finite.surjective_of_injective (permFn_injective p)⟩
def vector (c : Case) (values : List ℕ) := BoundedAllocations.decode (entries c) values
def code (c : Case) (values : List ℕ) : ℕ := c.val+6*(values.foldl (fun a x => 8*a+x) 0)
''')
 s.append(f'theorem perm_preserves_roles : ∀ p i, ((perm p) i).val<{l} ↔ i.val<{l} := by decide +kernel\n')
 s.append('def lookup : List (ℕ × (NewCase × Perm)) := [\n')
 records=[]
 total=accepted=0;observed=set()
 for c,(r,es) in enumerate(zip(old,entries)):
  oldns={int(t):m for t,m in r['counts'].items()}
  for vals in product(*(range(m+1)for t,m in es)):
   sums=[sum(k for (t,_),k in zip(es,vals)if t>>i&1)for i in range(3)]
   if sum(vals)>7 or any(a>b for a,b in zip(sums,caps)):continue
   total+=1
   if min(sums)<1:continue
   ns=dict(oldns)
   for (t,_),k in zip(es,vals):ns[t]-=k;ns[t|8]=k
   q=7-sum(vals);ns[0]-=q;ns[8]=q
   key=tuple(sorted((t,m)for t,m in ns.items()if m));chosen=lookup[key]
   representative={int(t):m for t,m in new[chosen[0]]['counts'].items()}
   assert all(ns.get(sum(1<<perms[chosen[1]][i] for i in range(4) if t>>i&1),0)==representative.get(t,0) for t in range(16))
   observed.add(chosen[0])
   records.append(f'({code(c,vals)},({chosen[0]},{chosen[1]}))');accepted+=1
 s.append(',\n'.join(records)+']\n')
 s.append('def choose (key : ℕ) : NewCase × Perm := ((lookup.find? (fun r => r.1 == key)).map Prod.snd).getD (0,0)\n')
 s.append(f'''def newCounts (c : Case) (values : List ℕ) := extend ({base} c) (vector c values) 7
+def positive (c : Case) (values : List ℕ) : Prop :=
+  ∀ i : Fin 3, 1≤∑ T : Finset (Fin 3), if i∈T then vector c values T else 0
+instance (c : Case) (values : List ℕ) : Decidable (positive c values) := inferInstanceAs (Decidable (∀ i : Fin 3, 1≤∑ T : Finset (Fin 3), if i∈T then vector c values T else 0))
+def covered (c : Case) (values : List ℕ) : Prop :=
+  positive c values → ∀ T, newCounts c values
+    (T.map (perm (choose (code c values)).2).toEmbedding)=μ (choose (code c values)).1 T
+noncomputable instance (c : Case) (values : List ℕ) : Decidable (covered c values) := inferInstanceAs (Decidable (positive c values → ∀ T, newCounts c values (T.map (perm (choose (code c values)).2).toEmbedding)=μ (choose (code c values)).1 T))
+def catalogue (c : Case) := BoundedAllocations.enumerate cost (entries c) cap
+'''.replace('\n+','\n'))
 for c in range(6):s.append(f'theorem coverage{c} : (catalogue {c}).all (fun values => decide (covered {c} values))=true := by decide +kernel\n')
 s.append('''theorem coverage (c : Case) (values : List ℕ) (member : values∈catalogue c) : covered c values := by
  have all : (catalogue c).all (fun values => decide (covered c values))=true := by
    fin_cases c
''')
 for c in range(6):s.append(f'    · exact coverage{c}\n')
 s.append('  exact of_decide_eq_true (List.all_eq_true.mp all values member)\n')
 s.append(f'''theorem entries_distinct : ∀ c, ((entries c).map Prod.fst).Nodup := by decide +kernel
+theorem entries_values : ∀ c, ∀ e∈entries c, e.2={base} c e.1 := by decide +kernel
+theorem entries_support : ∀ c, ∀ T : Finset (Fin 3),
+  T≠∅ → T∉(entries c).map Prod.fst → {base} c T=0 := by decide +kernel
+'''.replace('\n+','\n'))
 # entries_values unbounded pair quantification cannot decide; use list.all instead in generated source
 s[-1]=s[-1].replace(f'theorem entries_values : ∀ c, ∀ e∈entries c, e.2={base} c e.1 := by decide +kernel',f'''theorem entries_values (c : Case) (e : Finset (Fin 3) × ℕ) (mem : e∈entries c) : e.2={base} c e.1 := by
  have h : ∀ c, (entries c).all (fun e => decide (e.2={base} c e.1))=true := by decide +kernel
  exact of_decide_eq_true (List.all_eq_true.mp (h c) e mem)''')
 s.append(f'''attribute [local irreducible] covered

/-- Match an abstract promotion vector before inserting the actual H counts. -/
theorem actual_of_covered (H : Simple5Hypergraph (Fin 23)) (f : Fin 4 ↪ Fin 23)
    (c : Case) (values : List ℕ) (matched : covered c values)
    (pos : positive c values) (actual : ∀ T, count H f T=newCounts c values T) :
    ∃ q : NewCase, ∃ σ : Equiv.Perm (Fin 4),
      (∀ i, (σ i).val<{l} ↔ i.val<{l}) ∧
      ∀ T, count H (σ.toEmbedding.trans f) T=μ q T := by
  unfold covered at matched
  let chosen := choose (code c values)
  refine ⟨chosen.1,perm chosen.2,perm_preserves_roles chosen.2,?_⟩
  intro T
  rw [LockRelabel.count_comp_perm,actual]
  exact matched pos T

theorem actual (H : Simple5Hypergraph (Fin 23)) (cover : H.PairCovering)
+    (f : Fin 4 ↪ Fin 23) (c : Case)
+    (old : ∀ T, count H (restrict f) T={base} c T)
+    (degree : H.degree (f 3)=7)
+    (pairs : ∀ i : Fin 3, H.codegree (f i.castSucc) (f 3)≤cap (some i)) :
+    ∃ q : NewCase, ∃ σ : Equiv.Perm (Fin 4),
+      (∀ i, (σ i).val<{l} ↔ i.val<{l}) ∧
+      ∀ T, count H (σ.toEmbedding.trans f) T=μ q T := by
+  let values := (entries c).map (fun e => promotion H f e.1)
+  have capacity (j : Option (Fin 3)) : actualCap H f j≤cap j := by
+    cases j with
+    | none => simpa [actualCap,cap] using degree.le
+    | some i => exact pairs i
+  have member : values∈catalogue c := by
+    apply actual_mem_of_old H f (entries c) cap (entries_distinct c) ?_ capacity
+    intro e he
+    rw [old,entries_values c e he]
+  have prom (T : Finset (Fin 3)) (ne : T≠∅) : vector c values T=promotion H f T := by
+    apply decode_nonempty H f (entries c) ?_ T ne
+    intro S nonempty absent
+    have bound := promotion_le_old H f S
+    rw [old,entries_support c S nonempty absent] at bound
+    omega
+  have pos : positive c values := by
+    intro i
+    have eq : (∑ T : Finset (Fin 3), if i∈T then vector c values T else 0) =
+        ∑ T : Finset (Fin 3), if i∈T then promotion H f T else 0 := by
+      apply Finset.sum_congr rfl
+      intro T _
+      by_cases hi : i∈T
+      · rw [if_pos hi,if_pos hi,prom T (by intro empty; simpa [empty] using hi)]
+      · simp [hi]
+    rw [eq,sum_promotion_codegree]
+    exact H.one_le_codegree cover (f.injective.ne (Fin.castSucc_ne_last i))
+  have eq (T : Finset (Fin 4)) : count H f T=newCounts c values T :=
+    extend_actual H f ({base} c) (vector c values) 7 old prom degree T
+  have matched : covered c values := by exact coverage c values member
+  exact actual_of_covered H f c values matched pos eq
+end {name}
+'''.replace('\n+','\n'))
 assert len(observed)==len(new)
 replay.append(dict(family=name,capacity_allocations=total,positive_pair_allocations=accepted,orbits=len(new),permutation_direction_checked=True))
 parts.extend(s);print(name,total,accepted,len(new))
parts.append('end Aris4Math.ThirtyFour.TwentyThreeFewLowFourCoverage\n#print axioms Aris4Math.ThirtyFour.TwentyThreeFewLowFourCoverage.OneLow.actual\n#print axioms Aris4Math.ThirtyFour.TwentyThreeFewLowFourCoverage.TwoLow.actual\n')
full='\n'.join(parts)
head=full[:full.index('namespace OneLow')]
openhead=head[head.index('namespace Aris4Math.'):]
dat=[];num=[];act=[]
for name in ['OneLow','TwoLow']:
 body=full.split('namespace '+name+'\n',1)[1].split('end '+name+'\n',1)[0]
 idx=body.index('theorem coverage0'); end=body.index('theorem entries_distinct')
 dat.append('namespace '+name+'\n'+body[:idx]+'end '+name+'\n')
 num.append('namespace '+name+'\nopen TwentyThreeFewLowBase (Case)\n'+body[idx:end]+'end '+name+'\n')
 act.append('namespace '+name+'\nopen TwentyThreeFewLowBase (Case '+('oneLow' if name=='OneLow' else 'twoLow')+')\n'+body[end:]+'end '+name+'\n')
tail='end Aris4Math.ThirtyFour.TwentyThreeFewLowFourCoverage\n'
(OUT/'TwentyThreeFewLowFourData.lean').write_text(head+'\n'.join(dat)+tail)
(OUT/'TwentyThreeFewLowFourNumeric.lean').write_text('import Aris4Math.ThirtyFour.TwentyThreeFewLowFourData\n'+openhead+'\n'.join(num)+tail)
(OUT/'TwentyThreeFewLowFourCoverage.lean').write_text('import Aris4Math.ThirtyFour.TwentyThreeFewLowFourNumeric\n'+openhead+'\n'.join(act)+tail+'#print axioms Aris4Math.ThirtyFour.TwentyThreeFewLowFourCoverage.OneLow.actual\n#print axioms Aris4Math.ThirtyFour.TwentyThreeFewLowFourCoverage.TwoLow.actual\n')

(Path(__file__).parent/'FOUR_PROMOTION_COVERAGE_REPLAY.json').write_text(json.dumps(dict(scope='Local four-lock promotion classification only; not the complete 23-point branch',status='python_exact_reconstruction_checked_lean_pending',families=replay),indent=2)+'\n')
