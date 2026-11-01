from pathlib import Path
from fractions import Fraction
from itertools import product,permutations
import sys,json
ROOT=Path(__file__).resolve().parents[3]
sys.path.insert(0,str(ROOT/'computations'))
from multilock import Profile,rows,total_bound,pair_weight,link_certificate,json_value
D=[]
for a,b,c in product((1,2),repeat=3):
 for t in range(min(a,b,c)+1):
  counts={0:10+a+b+c-t,1:8+t-a-b,2:8+t-a-c,4:8+t-b-c,3:a-t,5:b-t,6:c-t,7:t}
  best=None
  for start in range(7,12):
   for pos in permutations(range(start,start+3)):
    p=Profile(19,5,pos,counts);ls=[];pureflags=[]
    for j in range(3):
     qt=link_certificate(p,j,5)['deduction'];qp=max(0,(4*counts[1<<j]+2-16)//3)
     pl=qp*2*pair_weight(19,5,pos,1<<j,1<<j,pos[j]);ls.append(max(qt,pl));pureflags.append(pl>qt)
    bound=total_bound(rows(p,deductions=dict(zip(pos,ls))))
    if best is None or bound<best['bound']:best=dict(a=a,b=b,c=c,t=t,pos=pos,counts=counts,loss=ls,pure=pureflags,bound=bound)
  assert best['bound']<1
  D.append(best)
print('labelled',len(D),'max',max(d['bound'] for d in D))
Path(__file__).with_name('TRIPLE_DATA.json').write_text(json.dumps(json_value(D),indent=2)+'\n')
vec=lambda a:'!['+','.join(map(str,a))+']'
rat=lambda r:f'({r.numerator}/{r.denominator})'
type_list=lambda p,c:'['+','.join('⟨['+','.join(map(str,sorted(p[j] for j in range(3) if mask>>j&1)))+f'],{c[mask]}⟩' for mask in (0,1,2,4,3,5,6,7) if c[mask])+']'
s='''import Aris4Math.ThirtyThree.TripleProfiles
import Aris4Math.ThirtyThree.RefinedDeletion
import Aris4Math.ThirtyThree.TwentyOnePairAssembly

/-! Seventeen labelled three-lock degree-eight cases; actual multiplicities and
actual total/pure bad-pair quotas are supplied by general proved interfaces. -/
namespace Aris4Math.ThirtyFour.NineteenTriples
open scoped BigOperators
open Aris4Math.TypeCounting Aris4Math.LinkDeletion Aris4Math.LinkWeightCertificates
open Aris4Math.ThirtyThree.TripleProfiles Aris4Math.ThirtyThree.TwentyOneDeletion
namespace RD
export Aris4Math.ThirtyThree.RefinedDeletion (avoidedPositions avoidedCount penaltySum realized_refined_deduction)
end RD

abbrev Case := Fin 17
structure Data where
  a : ℕ
  b : ℕ
  c : ℕ
  t : ℕ
  deriving DecidableEq
'''
s+='def data : Case → Data := '+vec([f'⟨{d["a"]},{d["b"]},{d["c"]},{d["t"]}⟩' for d in D])+'\n'
s+='def positionFn : Case → Fin 3 → Fin 19 := '+vec([vec([x-1 for x in d['pos']]) for d in D])+'\n'
s+='''theorem positionFn_injective : ∀ i, Function.Injective (positionFn i) := by decide
def positions (i : Case) : Fin 3 ↪ Fin 19 := ⟨positionFn i,positionFn_injective i⟩
def μ (i : Case) : Finset (Fin 3) → ℕ := recovered 34 8 8 8 (data i).a (data i).b (data i).c (data i).t

def p (i : Case) : Numeric.Profile :=
  pruneZero ⟨19,executableType (positions i) Finset.univ,
    labels.map (fun T => ⟨executableType (positions i) T, μ i T⟩),none,
    List.ofFn (fun j => (positions i j).val+1)⟩

theorem p_eq (i : Case) : p i =
    profile (positions i) (μ i) (List.ofFn fun j => (positions i j).val+1) := by
  simp only [p,executableType_eq,profile,rawProfile]
'''
s+='def computed : Case → Numeric.Profile := '+vec([f'⟨19,[{",".join(map(str,sorted(d["pos"])))}],{type_list(d["pos"],d["counts"])},none,[{",".join(map(str,d["pos"]))}]⟩' for d in D])+'\n'
s+='''theorem p_eq_computed (i : Case) : p i = computed i := by
  fin_cases i <;> rfl
'''
s+='def losses : Case → Fin 3 → ℚ := '+vec([vec([rat(x) for x in d['loss']]) for d in D])+'\n'
s+='def usePure : Case → Fin 3 → Bool := '+vec([vec([str(x).lower() for x in d['pure']]) for d in D])+'\n'
s+='''def loss (i : Case) (k : ℕ) : ℚ :=
  if k=(positions i 0).val+1 then losses i 0 else
  if k=(positions i 1).val+1 then losses i 1 else
  if k=(positions i 2).val+1 then losses i 2 else 0

def R (j : Fin 3) (_ : Fin 1) : Finset (Fin 3) := Finset.univ.erase j
def pureQ (i : Case) (j : Fin 3) : ℕ := (4*μ i {j}+2-16)/3
def pureWeight (i : Case) (j : Fin 3) : ℚ :=
  2 * Numeric.pairWeight (p i) ⟨[(positions i j).val+1],0⟩
    ⟨[(positions i j).val+1],0⟩ ((positions i j).val+1)

set_option maxRecDepth 100000 in
set_option maxHeartbeats 0 in
theorem certificates : ∀ i : Case,
    Numeric.validProfile (p i) 34 ∧
    (∑ k : Fin 19, min (Numeric.boundA (p i) (k.val+1))
      (min (Numeric.boundB (p i) (k.val+1)) (Numeric.boundC (p i) (k.val+1)-loss i (k.val+1)))) < 1 ∧
    ∀ j : Fin 3, let k := (positions i j).val+1
      if usePure i j then
        0 ≤ pureWeight i j ∧
        (∀ z : Fin 1, pureQ i j ≤
          (4*RD.avoidedCount (p i) k (RD.avoidedPositions (positions i) (R j z))+2-
            (19-1-(R j z).card))/3) ∧
        loss i k ≤ (∑ _z : Fin 1, (pureQ i j : ℚ)*pureWeight i j) -
          RD.penaltySum (p i) k (fun z => RD.avoidedPositions (positions i) (R j z))
            (fun _z => pureWeight i j)
      else
        0 ≤ threshold (p i) k ∧
        loss i k ≤ (5 : ℚ)*threshold (p i) k - penaltySum (p i) k (threshold (p i) k) := by
  simp only [loss,pureWeight,p_eq_computed]
  unfold Numeric.validProfile
  decide +kernel

theorem realizes34 (H : Simple5Hypergraph (Fin 19)) (vertices : Fin 3 ↪ Fin 19)
    (i : Case) (hμ : ∀ T, count H vertices T = μ i T)
    (valid : Numeric.validProfile (p i) 34) :
    RealizesProfile H vertices (positions i) (p i) 34 := by
  rw [p_eq] at valid ⊢
  refine ⟨rfl,valid,?_,table_pruneZero _ _ _ (raw_table H vertices (positions i) (μ i) hμ _)⟩
  simp [profile,pruneZero,rawProfile,canonicalType]

theorem propertyB_of_data (H : Simple5Hypergraph (Fin 19)) (cover : H.PairCovering)
    (edges34 : H.edges.card = 34) (vertices : Fin 3 ↪ Fin 19) (i : Case)
    (hd : ∀ j, H.degree (vertices j) = 8)
    (ha : H.codegree (vertices 0) (vertices 1) = (data i).a)
    (hb : H.codegree (vertices 0) (vertices 2) = (data i).b)
    (hc : H.codegree (vertices 1) (vertices 2) = (data i).c)
    (ht : tripleCodegree H (vertices 0) (vertices 1) (vertices 2) = (data i).t) : PropertyB H := by
  obtain ⟨valid,strict,bounds⟩ := certificates i
  have hm : ∀ T, count H vertices T = μ i T := by
    intro T
    rw [actual_recovered,triple_count_eq,edges34,hd 0,hd 1,hd 2,ha,hb,hc,ht]
    rfl
  have real := realizes34 H vertices i hm valid
  apply ThirtyThree.CustomDeletion.propertyB_of_custom_deletion H vertices (positions i) (p i) real rfl (loss i)
  · intro j _
    have hb := bounds j
    dsimp only at hb
    by_cases hp : usePure i j = true
    · rw [if_pos hp] at hb
      obtain ⟨nonneg,quota,bound⟩ := hb
      exact RD.realized_refined_deduction H vertices (positions i) (p i) real j
        (R j) (fun _ : Fin 1 => pureWeight i j) (fun _ => pureQ i j) _
        (fun _ => nonneg) (fun _ => by simp [R]) quota bound
    · rw [if_neg hp] at hb
      apply realized_threshold_deduction H cover vertices (positions i) (p i) real j _ 5 _ _ rfl
      · rw [hd]
      · exact hb.1
      · exact hb.2
  · intro k hk
    have absent : ∀ j : Fin 3, k ≠ (positions i j).val+1 := by
      intro j he
      apply hk
      simp only [p,pruneZero]
      exact List.mem_ofFn.mpr ⟨j,he.symm⟩
    simp [loss,absent 0,absent 1,absent 2]
  · exact strict

def Matches (a b c t : ℕ) (i : Case) : Prop :=
  a=(data i).a ∧ b=(data i).b ∧ c=(data i).c ∧ t=(data i).t
instance (a b c t : ℕ) (i : Case) : Decidable (Matches a b c t i) := by
  unfold Matches; infer_instance

theorem coverage : ∀ a b c t : Fin 3,
    1 ≤ a.val → 1 ≤ b.val → 1 ≤ c.val →
    t.val ≤ a.val → t.val ≤ b.val → t.val ≤ c.val →
    ∃ i, Matches a.val b.val c.val t.val i := by decide +kernel

theorem propertyB_of_three_eights (H : Simple5Hypergraph (Fin 19)) (cover : H.PairCovering)
    (edges34 : H.edges.card = 34) (x y z : Fin 19)
    (xy : x ≠ y) (xz : x ≠ z) (yz : y ≠ z)
    (dx : H.degree x = 8) (dy : H.degree y = 8) (dz : H.degree z = 8)
    (ca : H.codegree x y ≤ 2) (cb : H.codegree x z ≤ 2) (cc : H.codegree y z ≤ 2) : PropertyB H := by
  have la := H.one_le_codegree cover xy
  have lb := H.one_le_codegree cover xz
  have lc := H.one_le_codegree cover yz
  obtain ⟨ta,tb,tc⟩ := ThirtyThree.TwentyOnePairAssembly.tripleCodegree_le_pairs H x y z
  obtain ⟨i,ha,hb,hc,ht⟩ := coverage ⟨H.codegree x y,by omega⟩
    ⟨H.codegree x z,by omega⟩ ⟨H.codegree y z,by omega⟩
    ⟨tripleCodegree H x y z,by omega⟩ la lb lc ta tb tc
  apply propertyB_of_data H cover edges34 (threeVertices x y z xy xz yz) i
  · intro j; fin_cases j
    · exact dx
    · exact dy
    · exact dz
  · exact ha
  · exact hb
  · exact hc
  · exact ht

end Aris4Math.ThirtyFour.NineteenTriples
#print axioms Aris4Math.ThirtyFour.NineteenTriples.propertyB_of_three_eights
'''
(ROOT/'formal/Aris4Math/ThirtyFour/NineteenTriples.lean').write_text(s)
