from pathlib import Path
ROOT=Path(__file__).resolve().parents[4]
s=''.join('import Aris4Math.ThirtyFour.TwentyOneSixQuad'+ds+'\n' for ds in ['6688','6777','6778','6788','6888'])
s+='''import Aris4Math.ThirtyThree.TwentyTwoQuadAssembly
namespace Aris4Math.ThirtyFour.TwentyOneSixQuadCoverage
open Aris4Math.ThirtyThree.QuadProfiles
open Aris4Math.ThirtyThree.TwentyTwoQuadAssembly (highPairSum high_inventory high_le_two)
set_option maxRecDepth 100000
set_option maxHeartbeats 0
'''
patterns={
'6688':dict(co='![a,1,1,1,1,b]',ass='h 0+h 4=0 ∧ h 1+h 4=0',res='co 5=2 ∧ (co 0=1 → ∀j,h j=0)'),
'6777':dict(co='![a,a,a,3-a,3-a,3-a]',ass='(a=1 → h 4=1) ∧ (a=2 → h 0+h 4=0 ∧ h 1+h 4=0 ∧ h 2+h 4=0)',res='False'),
'6778':dict(co='![a,a,1,3-a,b,c]',ass='(a=1 → h 0+h 4=1 ∧ h 1+h 4=0 ∧ h 2+h 4=0) ∧ (a=2 → h 0+h 4=0)',res='co 0=1 ∧ co 4=1 ∧ co 5=1'),
'6788':dict(co='![a,1,1,b,c,2]',ass='True',res='(co 0=2 ∧ co 3=1 ∧ co 4=1 ∧ h 0+h 4=0 ∧ h 1+h 4=0) ∨ (co 0=1 ∧ co 3=co 4 ∧ h 4=0)'),
'6888':dict(co='![1,1,1,a,b,c]',ass='True',res='h 4=0 ∧ ((co 3=2 ∧ co 4=2 ∧ co 5=2) ∨ (co 3+co 4+co 5=4 ∧ ∀j,h j=0))')}
for ds,d in patterns.items():
 name='TwentyOneSixQuad'+ds
 s+=f'''
def co{ds} (a b c : ℕ) : Fin 6 → ℕ := {d['co']}
def Assumptions{ds} (a : ℕ) (h : Fin 5 → ℕ) : Prop := {d['ass']}
instance (a : ℕ) (h : Fin 5→ℕ) : Decidable (Assumptions{ds} a h) := by unfold Assumptions{ds};infer_instance
def Residue{ds} (co : Fin 6→ℕ) (h : Fin 5→ℕ) : Prop := {d['res']}
instance (co : Fin 6→ℕ) (h : Fin 5→ℕ) : Decidable (Residue{ds} co h) := by unfold Residue{ds};infer_instance

theorem coverage{ds} : ∀ a b c : Fin 2, ∀ h : Fin 5→Fin 3,
    Assumptions{ds} (a.val+1) (fun j=>(h j).val) →
    (∀j,highPairSum (fun z=>(h z).val) j≤co{ds} (a.val+1) (b.val+1) (c.val+1) j) →
    Residue{ds} (co{ds} (a.val+1) (b.val+1) (c.val+1)) (fun j=>(h j).val) ∨
    ∃i : {name}Data.Case,
      (∀j,co{ds} (a.val+1) (b.val+1) (c.val+1) j={name}Data.co i j) ∧
      (∀j,(h j).val={name}Data.high i j) := by decide +kernel

theorem actual{ds} (H : Simple5Hypergraph (Fin 21)) (size : H.edges.card=34)
    (noB : ¬PropertyB H) (f : Fin 4↪Fin 21) (a b c : Fin 2)
    (hd : ∀j,H.degree (f j)={name}Data.degree j)
    (hc : ∀j,H.codegree (f (first j)) (f (second j))=co{ds} (a.val+1) (b.val+1) (c.val+1) j)
    (ass : Assumptions{ds} (a.val+1) (fun j=>count H f (highLabels j))) :
    Residue{ds} (co{ds} (a.val+1) (b.val+1) (c.val+1)) (fun j=>count H f (highLabels j)) := by
  have pairBound (j) : H.codegree (f (first j)) (f (second j))≤2 := by
    rw [hc]
    have bounds : ∀a b c : Fin 2,∀j,co{ds} (a.val+1) (b.val+1) (c.val+1) j≤2 := by decide
    exact bounds a b c j
  have bound := high_le_two H f pairBound
  let h : Fin 5→Fin 3 := fun j=>⟨count H f (highLabels j),by have := bound j;omega⟩
  have inv (j) : highPairSum (fun k=>(h k).val) j≤co{ds} (a.val+1) (b.val+1) (c.val+1) j := by
    rw [←hc]; exact high_inventory H f j
  rcases coverage{ds} a b c h ass inv with residue | ⟨i,coeq,heq⟩
  · exact residue
  · exact False.elim (noB ({name}.propertyB_of_data H size f i hd
      (fun j=>(hc j).trans (coeq j)) heq))
'''
s+='''
theorem equality_coverage : ∀a b : Fin 2, ∀h : Fin 2,
    h.val≤a.val → h.val≤b.val →
    ∃i : TwentyOneSixQuad6888Data.Case,
      (∀j,(![1,1,2,2,a.val+1,b.val+1] : Fin 6→ℕ) j=TwentyOneSixQuad6888Data.co i j) ∧
      (∀j,(![0,0,0,h.val,1] : Fin 5→ℕ) j=TwentyOneSixQuad6888Data.high i j) := by decide +kernel
end Aris4Math.ThirtyFour.TwentyOneSixQuadCoverage
'''
(ROOT/'formal/Aris4Math/ThirtyFour/TwentyOneSixQuadCoverage.lean').write_text(s)
