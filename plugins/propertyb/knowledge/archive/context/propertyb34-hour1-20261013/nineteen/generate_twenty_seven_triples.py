from pathlib import Path
from fractions import Fraction
from itertools import product,permutations
import sys,json
ROOT=Path(__file__).resolve().parents[3]
sys.path.insert(0,str(ROOT/'computations'))
from multilock import Profile,rows,total_bound,pair_weight,link_certificate,json_value
D=[]
for high in (False,True):
 for a,b,c in product((1,2,3),repeat=3):
  if not high and (min(a,b,c)<2 or max(a,b,c)!=3):continue
  if high and (a!=2 or (b==c and b<3)):continue
  for t in range(min(a,b,c)+1):
   deg=[7,7,8 if high else 7]
   counts={0:34+a+b+c-sum(deg)-t,1:deg[0]+t-a-b,2:deg[1]+t-a-c,4:deg[2]+t-b-c,3:a-t,5:b-t,6:c-t,7:t}
   best=None
   for start in range(7,13):
    for pos in permutations(range(start,start+3)):
     p0=Profile(20,5,pos,counts);ls=[];pureflags=[]
     for j in range(3):
      qt=link_certificate(p0,j,(4*deg[j]-19+2)//3)['deduction'];qp=max(0,(4*counts[1<<j]+2-17)//3)
      pl=qp*2*pair_weight(20,5,pos,1<<j,1<<j,pos[j]);ls.append(max(qt,pl));pureflags.append(pl>qt)
     bound=total_bound(rows(p0,deductions=dict(zip(pos,ls))))
     if best is None or bound<best['bound']:best=dict(a=a,b=b,c=c,t=t,high=high,pos=pos,counts=counts,loss=ls,pure=pureflags,bound=bound)
   assert best['bound']<1,(high,a,b,c,t,best)
   D.append(best)
print('labelled',len(D),'max',max(d['bound'] for d in D))
Path(__file__).with_name('TWENTY_SEVEN_TRIPLE_DATA.json').write_text(json.dumps(json_value(D),indent=2)+'\n')
vec=lambda a:'!['+','.join(map(str,a))+']'
rat=lambda r:f'({r.numerator}/{r.denominator})'
type_list=lambda p,c:'['+','.join('⟨['+','.join(map(str,sorted(p[j] for j in range(3) if mask>>j&1)))+f'],{c[mask]}⟩' for mask in (0,1,2,4,3,5,6,7) if c[mask])+']'
s='''import Aris4Math.ThirtyThree.TripleProfiles
import Aris4Math.ThirtyThree.RefinedDeletion
import Aris4Math.ThirtyThree.TwentyOnePairAssembly

/-! Seventeen labelled three-lock degree-eight cases; actual multiplicities and
actual total/pure bad-pair quotas are supplied by general proved interfaces. -/
namespace Aris4Math.ThirtyFour.TwentySevenTriples
set_option maxRecDepth 100000
open scoped BigOperators
open Aris4Math.TypeCounting Aris4Math.LinkDeletion Aris4Math.LinkWeightCertificates
open Aris4Math.ThirtyThree.TripleProfiles Aris4Math.ThirtyThree.TwentyOneDeletion
namespace RD
export Aris4Math.ThirtyThree.RefinedDeletion (avoidedPositions avoidedCount penaltySum realized_refined_deduction)
end RD

abbrev Case := Fin 39
structure Data where
  a : ℕ
  b : ℕ
  c : ℕ
  t : ℕ
  high : Bool
  deriving DecidableEq
'''
s+='def data : Case → Data := '+vec([f'⟨{d["a"]},{d["b"]},{d["c"]},{d["t"]},{str(d["high"]).lower()}⟩' for d in D])+'\n'
s+='def positionFn : Case → Fin 3 → Fin 20 := '+vec([vec([x-1 for x in d['pos']]) for d in D])+'\n'
s+='''theorem positionFn_injective : ∀ i, Function.Injective (positionFn i) := by decide
def positions (i : Case) : Fin 3 ↪ Fin 20 := ⟨positionFn i,positionFn_injective i⟩
def degree (i : Case) (j : Fin 3) : ℕ := if (data i).high && decide (j=2) then 8 else 7
def μ (i : Case) : Finset (Fin 3) → ℕ := recovered 34 (degree i 0) (degree i 1) (degree i 2) (data i).a (data i).b (data i).c (data i).t

def p (i : Case) : Numeric.Profile :=
  pruneZero ⟨20,executableType (positions i) Finset.univ,
    labels.map (fun T => ⟨executableType (positions i) T, μ i T⟩),none,
    List.ofFn (fun j => (positions i j).val+1)⟩

theorem p_eq (i : Case) : p i =
    profile (positions i) (μ i) (List.ofFn fun j => (positions i j).val+1) := by
  simp only [p,executableType_eq,profile,rawProfile]
'''
s+='def computed : Case → Numeric.Profile := '+vec([f'⟨20,[{",".join(map(str,sorted(d["pos"])))}],{type_list(d["pos"],d["counts"])},none,[{",".join(map(str,d["pos"]))}]⟩' for d in D])+'\n'
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
def pureQ (i : Case) (j : Fin 3) : ℕ := (4*μ i {j}+2-17)/3
def pureWeight (i : Case) (j : Fin 3) : ℚ :=
  2 * Numeric.pairWeight (p i) ⟨[(positions i j).val+1],0⟩
    ⟨[(positions i j).val+1],0⟩ ((positions i j).val+1)

set_option maxRecDepth 100000 in
set_option maxHeartbeats 0 in
theorem certificates : ∀ i : Case,
    Numeric.validProfile (p i) 34 ∧
    (∑ k : Fin 20, min (Numeric.boundA (p i) (k.val+1))
      (min (Numeric.boundB (p i) (k.val+1)) (Numeric.boundC (p i) (k.val+1)-loss i (k.val+1)))) < 1 ∧
    ∀ j : Fin 3, let k := (positions i j).val+1
      if usePure i j then
        0 ≤ pureWeight i j ∧
        (∀ z : Fin 1, pureQ i j ≤
          (4*RD.avoidedCount (p i) k (RD.avoidedPositions (positions i) (R j z))+2-
            (20-1-(R j z).card))/3) ∧
        loss i k ≤ (∑ _z : Fin 1, (pureQ i j : ℚ)*pureWeight i j) -
          RD.penaltySum (p i) k (fun z => RD.avoidedPositions (positions i) (R j z))
            (fun _z => pureWeight i j)
      else
        0 ≤ threshold (p i) k ∧
        loss i k ≤ (((4*degree i j-19+2)/3 : ℕ) : ℚ)*threshold (p i) k - penaltySum (p i) k (threshold (p i) k) := by
  intro i
  fin_cases i <;> simp only [loss,pureWeight,p_eq_computed] <;>
    unfold Numeric.validProfile <;> decide +kernel

theorem realizes34 (H : Simple5Hypergraph (Fin 20)) (vertices : Fin 3 ↪ Fin 20)
    (i : Case) (hμ : ∀ T, count H vertices T = μ i T)
    (valid : Numeric.validProfile (p i) 34) :
    RealizesProfile H vertices (positions i) (p i) 34 := by
  rw [p_eq] at valid ⊢
  refine ⟨rfl,valid,?_,table_pruneZero _ _ _ (raw_table H vertices (positions i) (μ i) hμ _)⟩
  simp [profile,pruneZero,rawProfile,canonicalType]

theorem propertyB_of_data (H : Simple5Hypergraph (Fin 20)) (cover : H.PairCovering)
    (edges34 : H.edges.card = 34) (vertices : Fin 3 ↪ Fin 20) (i : Case)
    (hd : ∀ j, H.degree (vertices j) = degree i j)
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
      apply realized_threshold_deduction H cover vertices (positions i) (p i) real j _ ((4*degree i j-19+2)/3) _ _ rfl
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

def Matches (a b c t : ℕ) (high : Bool) (i : Case) : Prop :=
  a=(data i).a ∧ b=(data i).b ∧ c=(data i).c ∧ t=(data i).t ∧ (data i).high=high
instance (a b c t : ℕ) (high : Bool) (i : Case) : Decidable (Matches a b c t high i) := by
  unfold Matches; infer_instance

theorem coverage_seven : ∀ a b c t : Fin 4,
    2 ≤ a.val → 2 ≤ b.val → 2 ≤ c.val →
    (a.val=3 ∨ b.val=3 ∨ c.val=3) →
    t.val ≤ a.val → t.val ≤ b.val → t.val ≤ c.val →
    ∃ i, Matches a.val b.val c.val t.val false i := by decide +kernel

theorem coverage_mixed : ∀ b c t : Fin 4,
    1 ≤ b.val → 1 ≤ c.val → (b.val≠c.val ∨ b.val=3) →
    t.val ≤ 2 → t.val ≤ b.val → t.val ≤ c.val →
    ∃ i, Matches 2 b.val c.val t.val true i := by decide +kernel

theorem propertyB_of_three_sevens (H : Simple5Hypergraph (Fin 20)) (cover : H.PairCovering)
    (edges34 : H.edges.card = 34) (x y z : Fin 20)
    (xy : x ≠ y) (xz : x ≠ z) (yz : y ≠ z)
    (dx : H.degree x = 7) (dy : H.degree y = 7) (dz : H.degree z = 7)
    (la : 2 ≤ H.codegree x y) (lb : 2 ≤ H.codegree x z) (lc : 2 ≤ H.codegree y z)
    (ca : H.codegree x y ≤ 3) (cb : H.codegree x z ≤ 3) (cc : H.codegree y z ≤ 3)
    (someThree : H.codegree x y=3 ∨ H.codegree x z=3 ∨ H.codegree y z=3) : PropertyB H := by
  obtain ⟨ta,tb,tc⟩ := ThirtyThree.TwentyOnePairAssembly.tripleCodegree_le_pairs H x y z
  obtain ⟨i,ha,hb,hc,ht,kind⟩ := coverage_seven ⟨H.codegree x y,by omega⟩
    ⟨H.codegree x z,by omega⟩ ⟨H.codegree y z,by omega⟩
    ⟨tripleCodegree H x y z,by omega⟩ la lb lc someThree ta tb tc
  apply propertyB_of_data H cover edges34 (threeVertices x y z xy xz yz) i
  · intro j; fin_cases j
    · simpa [degree,kind,threeVertices] using dx
    · simpa [degree,kind,threeVertices] using dy
    · simpa [degree,kind,threeVertices] using dz
  · exact ha
  · exact hb
  · exact hc
  · exact ht

theorem propertyB_of_mixed (H : Simple5Hypergraph (Fin 20)) (cover : H.PairCovering)
    (edges34 : H.edges.card = 34) (x y z : Fin 20)
    (xy : x ≠ y) (xz : x ≠ z) (yz : y ≠ z)
    (dx : H.degree x = 7) (dy : H.degree y = 7) (dz : H.degree z = 8)
    (ca : H.codegree x y = 2) (cb : H.codegree x z ≤ 3) (cc : H.codegree y z ≤ 3)
    (good : H.codegree x z ≠ H.codegree y z ∨ H.codegree x z=3) : PropertyB H := by
  have lb := H.one_le_codegree cover xz
  have lc := H.one_le_codegree cover yz
  obtain ⟨ta,tb,tc⟩ := ThirtyThree.TwentyOnePairAssembly.tripleCodegree_le_pairs H x y z
  obtain ⟨i,ha,hb,hc,ht,kind⟩ := coverage_mixed
    ⟨H.codegree x z,by omega⟩ ⟨H.codegree y z,by omega⟩
    ⟨tripleCodegree H x y z,by omega⟩ lb lc good (by simpa only [ca] using ta) tb tc
  apply propertyB_of_data H cover edges34 (threeVertices x y z xy xz yz) i
  · intro j; fin_cases j
    · simpa [degree,kind,threeVertices] using dx
    · simpa [degree,kind,threeVertices] using dy
    · simpa [degree,kind,threeVertices] using dz
  · exact ca.trans ha
  · exact hb
  · exact hc
  · exact ht

end Aris4Math.ThirtyFour.TwentySevenTriples
#print axioms Aris4Math.ThirtyFour.TwentySevenTriples.propertyB_of_three_sevens
'''
(ROOT/'formal/Aris4Math/ThirtyFour/TwentySevenTriples.lean').write_text(s)
