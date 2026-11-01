import Aris4Math.ThirtyFour.TwentyOneSixQuad6688
import Aris4Math.ThirtyFour.TwentyOneSixQuad6777
import Aris4Math.ThirtyFour.TwentyOneSixQuad6778
import Aris4Math.ThirtyFour.TwentyOneSixQuad6788
import Aris4Math.ThirtyFour.TwentyOneSixQuad6888
import Aris4Math.ThirtyThree.TwentyTwoQuadAssembly
namespace Aris4Math.ThirtyFour.TwentyOneSixQuadCoverage
open Aris4Math.ThirtyThree.QuadProfiles
open Aris4Math.ThirtyThree.TwentyTwoQuadAssembly (highPairSum high_inventory high_le_two)
set_option maxRecDepth 100000
set_option maxHeartbeats 0

def co6688 (a b c : ℕ) : Fin 6 → ℕ := ![a,1,1,1,1,b]
def Assumptions6688 (a : ℕ) (h : Fin 5 → ℕ) : Prop := h 0+h 4=0 ∧ h 1+h 4=0
instance (a : ℕ) (h : Fin 5→ℕ) : Decidable (Assumptions6688 a h) := by unfold Assumptions6688;infer_instance
def Residue6688 (co : Fin 6→ℕ) (h : Fin 5→ℕ) : Prop := co 5=2 ∧ (co 0=1 → ∀j,h j=0)
instance (co : Fin 6→ℕ) (h : Fin 5→ℕ) : Decidable (Residue6688 co h) := by unfold Residue6688;infer_instance

theorem coverage6688 : ∀ a b c : Fin 2, ∀ h : Fin 5→Fin 3,
    Assumptions6688 (a.val+1) (fun j=>(h j).val) →
    (∀j,highPairSum (fun z=>(h z).val) j≤co6688 (a.val+1) (b.val+1) (c.val+1) j) →
    Residue6688 (co6688 (a.val+1) (b.val+1) (c.val+1)) (fun j=>(h j).val) ∨
    ∃i : TwentyOneSixQuad6688Data.Case,
      (∀j,co6688 (a.val+1) (b.val+1) (c.val+1) j=TwentyOneSixQuad6688Data.co i j) ∧
      (∀j,(h j).val=TwentyOneSixQuad6688Data.high i j) := by decide +kernel

theorem actual6688 (H : Simple5Hypergraph (Fin 21)) (size : H.edges.card=34)
    (noB : ¬PropertyB H) (f : Fin 4↪Fin 21) (a b c : Fin 2)
    (hd : ∀j,H.degree (f j)=TwentyOneSixQuad6688Data.degree j)
    (hc : ∀j,H.codegree (f (first j)) (f (second j))=co6688 (a.val+1) (b.val+1) (c.val+1) j)
    (ass : Assumptions6688 (a.val+1) (fun j=>count H f (highLabels j))) :
    Residue6688 (co6688 (a.val+1) (b.val+1) (c.val+1)) (fun j=>count H f (highLabels j)) := by
  have pairBound (j) : H.codegree (f (first j)) (f (second j))≤2 := by
    rw [hc]
    have bounds : ∀a b c : Fin 2,∀j,co6688 (a.val+1) (b.val+1) (c.val+1) j≤2 := by decide
    exact bounds a b c j
  have bound := high_le_two H f pairBound
  let h : Fin 5→Fin 3 := fun j=>⟨count H f (highLabels j),by have := bound j;omega⟩
  have inv (j) : highPairSum (fun k=>(h k).val) j≤co6688 (a.val+1) (b.val+1) (c.val+1) j := by
    rw [←hc]; exact high_inventory H f j
  rcases coverage6688 a b c h ass inv with residue | ⟨i,coeq,heq⟩
  · exact residue
  · exact False.elim (noB (TwentyOneSixQuad6688.propertyB_of_data H size f i hd
      (fun j=>(hc j).trans (coeq j)) heq))

def co6777 (a b c : ℕ) : Fin 6 → ℕ := ![a,a,a,3-a,3-a,3-a]
def Assumptions6777 (a : ℕ) (h : Fin 5 → ℕ) : Prop := (a=1 → h 4=1) ∧ (a=2 → h 0+h 4=0 ∧ h 1+h 4=0 ∧ h 2+h 4=0)
instance (a : ℕ) (h : Fin 5→ℕ) : Decidable (Assumptions6777 a h) := by unfold Assumptions6777;infer_instance
def Residue6777 (co : Fin 6→ℕ) (h : Fin 5→ℕ) : Prop := False
instance (co : Fin 6→ℕ) (h : Fin 5→ℕ) : Decidable (Residue6777 co h) := by unfold Residue6777;infer_instance

theorem coverage6777 : ∀ a b c : Fin 2, ∀ h : Fin 5→Fin 3,
    Assumptions6777 (a.val+1) (fun j=>(h j).val) →
    (∀j,highPairSum (fun z=>(h z).val) j≤co6777 (a.val+1) (b.val+1) (c.val+1) j) →
    Residue6777 (co6777 (a.val+1) (b.val+1) (c.val+1)) (fun j=>(h j).val) ∨
    ∃i : TwentyOneSixQuad6777Data.Case,
      (∀j,co6777 (a.val+1) (b.val+1) (c.val+1) j=TwentyOneSixQuad6777Data.co i j) ∧
      (∀j,(h j).val=TwentyOneSixQuad6777Data.high i j) := by decide +kernel

theorem actual6777 (H : Simple5Hypergraph (Fin 21)) (size : H.edges.card=34)
    (noB : ¬PropertyB H) (f : Fin 4↪Fin 21) (a b c : Fin 2)
    (hd : ∀j,H.degree (f j)=TwentyOneSixQuad6777Data.degree j)
    (hc : ∀j,H.codegree (f (first j)) (f (second j))=co6777 (a.val+1) (b.val+1) (c.val+1) j)
    (ass : Assumptions6777 (a.val+1) (fun j=>count H f (highLabels j))) :
    Residue6777 (co6777 (a.val+1) (b.val+1) (c.val+1)) (fun j=>count H f (highLabels j)) := by
  have pairBound (j) : H.codegree (f (first j)) (f (second j))≤2 := by
    rw [hc]
    have bounds : ∀a b c : Fin 2,∀j,co6777 (a.val+1) (b.val+1) (c.val+1) j≤2 := by decide
    exact bounds a b c j
  have bound := high_le_two H f pairBound
  let h : Fin 5→Fin 3 := fun j=>⟨count H f (highLabels j),by have := bound j;omega⟩
  have inv (j) : highPairSum (fun k=>(h k).val) j≤co6777 (a.val+1) (b.val+1) (c.val+1) j := by
    rw [←hc]; exact high_inventory H f j
  rcases coverage6777 a b c h ass inv with residue | ⟨i,coeq,heq⟩
  · exact residue
  · exact False.elim (noB (TwentyOneSixQuad6777.propertyB_of_data H size f i hd
      (fun j=>(hc j).trans (coeq j)) heq))

def co6778 (a b c : ℕ) : Fin 6 → ℕ := ![a,a,1,3-a,b,c]
def Assumptions6778 (a : ℕ) (h : Fin 5 → ℕ) : Prop := (a=1 → h 0+h 4=1 ∧ h 1+h 4=0 ∧ h 2+h 4=0) ∧ (a=2 → h 0+h 4=0)
instance (a : ℕ) (h : Fin 5→ℕ) : Decidable (Assumptions6778 a h) := by unfold Assumptions6778;infer_instance
def Residue6778 (co : Fin 6→ℕ) (h : Fin 5→ℕ) : Prop := co 0=1 ∧ co 4=1 ∧ co 5=1
instance (co : Fin 6→ℕ) (h : Fin 5→ℕ) : Decidable (Residue6778 co h) := by unfold Residue6778;infer_instance

theorem coverage6778 : ∀ a b c : Fin 2, ∀ h : Fin 5→Fin 3,
    Assumptions6778 (a.val+1) (fun j=>(h j).val) →
    (∀j,highPairSum (fun z=>(h z).val) j≤co6778 (a.val+1) (b.val+1) (c.val+1) j) →
    Residue6778 (co6778 (a.val+1) (b.val+1) (c.val+1)) (fun j=>(h j).val) ∨
    ∃i : TwentyOneSixQuad6778Data.Case,
      (∀j,co6778 (a.val+1) (b.val+1) (c.val+1) j=TwentyOneSixQuad6778Data.co i j) ∧
      (∀j,(h j).val=TwentyOneSixQuad6778Data.high i j) := by decide +kernel

theorem actual6778 (H : Simple5Hypergraph (Fin 21)) (size : H.edges.card=34)
    (noB : ¬PropertyB H) (f : Fin 4↪Fin 21) (a b c : Fin 2)
    (hd : ∀j,H.degree (f j)=TwentyOneSixQuad6778Data.degree j)
    (hc : ∀j,H.codegree (f (first j)) (f (second j))=co6778 (a.val+1) (b.val+1) (c.val+1) j)
    (ass : Assumptions6778 (a.val+1) (fun j=>count H f (highLabels j))) :
    Residue6778 (co6778 (a.val+1) (b.val+1) (c.val+1)) (fun j=>count H f (highLabels j)) := by
  have pairBound (j) : H.codegree (f (first j)) (f (second j))≤2 := by
    rw [hc]
    have bounds : ∀a b c : Fin 2,∀j,co6778 (a.val+1) (b.val+1) (c.val+1) j≤2 := by decide
    exact bounds a b c j
  have bound := high_le_two H f pairBound
  let h : Fin 5→Fin 3 := fun j=>⟨count H f (highLabels j),by have := bound j;omega⟩
  have inv (j) : highPairSum (fun k=>(h k).val) j≤co6778 (a.val+1) (b.val+1) (c.val+1) j := by
    rw [←hc]; exact high_inventory H f j
  rcases coverage6778 a b c h ass inv with residue | ⟨i,coeq,heq⟩
  · exact residue
  · exact False.elim (noB (TwentyOneSixQuad6778.propertyB_of_data H size f i hd
      (fun j=>(hc j).trans (coeq j)) heq))

def co6788 (a b c : ℕ) : Fin 6 → ℕ := ![a,1,1,b,c,2]
def Assumptions6788 (a : ℕ) (h : Fin 5 → ℕ) : Prop := True
instance (a : ℕ) (h : Fin 5→ℕ) : Decidable (Assumptions6788 a h) := by unfold Assumptions6788;infer_instance
def Residue6788 (co : Fin 6→ℕ) (h : Fin 5→ℕ) : Prop := (co 0=2 ∧ co 3=1 ∧ co 4=1 ∧ h 0+h 4=0 ∧ h 1+h 4=0) ∨ (co 0=1 ∧ co 3=co 4 ∧ h 4=0)
instance (co : Fin 6→ℕ) (h : Fin 5→ℕ) : Decidable (Residue6788 co h) := by unfold Residue6788;infer_instance

theorem coverage6788 : ∀ a b c : Fin 2, ∀ h : Fin 5→Fin 3,
    Assumptions6788 (a.val+1) (fun j=>(h j).val) →
    (∀j,highPairSum (fun z=>(h z).val) j≤co6788 (a.val+1) (b.val+1) (c.val+1) j) →
    Residue6788 (co6788 (a.val+1) (b.val+1) (c.val+1)) (fun j=>(h j).val) ∨
    ∃i : TwentyOneSixQuad6788Data.Case,
      (∀j,co6788 (a.val+1) (b.val+1) (c.val+1) j=TwentyOneSixQuad6788Data.co i j) ∧
      (∀j,(h j).val=TwentyOneSixQuad6788Data.high i j) := by decide +kernel

theorem actual6788 (H : Simple5Hypergraph (Fin 21)) (size : H.edges.card=34)
    (noB : ¬PropertyB H) (f : Fin 4↪Fin 21) (a b c : Fin 2)
    (hd : ∀j,H.degree (f j)=TwentyOneSixQuad6788Data.degree j)
    (hc : ∀j,H.codegree (f (first j)) (f (second j))=co6788 (a.val+1) (b.val+1) (c.val+1) j)
    (ass : Assumptions6788 (a.val+1) (fun j=>count H f (highLabels j))) :
    Residue6788 (co6788 (a.val+1) (b.val+1) (c.val+1)) (fun j=>count H f (highLabels j)) := by
  have pairBound (j) : H.codegree (f (first j)) (f (second j))≤2 := by
    rw [hc]
    have bounds : ∀a b c : Fin 2,∀j,co6788 (a.val+1) (b.val+1) (c.val+1) j≤2 := by decide
    exact bounds a b c j
  have bound := high_le_two H f pairBound
  let h : Fin 5→Fin 3 := fun j=>⟨count H f (highLabels j),by have := bound j;omega⟩
  have inv (j) : highPairSum (fun k=>(h k).val) j≤co6788 (a.val+1) (b.val+1) (c.val+1) j := by
    rw [←hc]; exact high_inventory H f j
  rcases coverage6788 a b c h ass inv with residue | ⟨i,coeq,heq⟩
  · exact residue
  · exact False.elim (noB (TwentyOneSixQuad6788.propertyB_of_data H size f i hd
      (fun j=>(hc j).trans (coeq j)) heq))

def co6888 (a b c : ℕ) : Fin 6 → ℕ := ![1,1,1,a,b,c]
def Assumptions6888 (a : ℕ) (h : Fin 5 → ℕ) : Prop := True
instance (a : ℕ) (h : Fin 5→ℕ) : Decidable (Assumptions6888 a h) := by unfold Assumptions6888;infer_instance
def Residue6888 (co : Fin 6→ℕ) (h : Fin 5→ℕ) : Prop := h 4=0 ∧ ((co 3=2 ∧ co 4=2 ∧ co 5=2) ∨ (co 3+co 4+co 5=4 ∧ ∀j,h j=0))
instance (co : Fin 6→ℕ) (h : Fin 5→ℕ) : Decidable (Residue6888 co h) := by unfold Residue6888;infer_instance

theorem coverage6888 : ∀ a b c : Fin 2, ∀ h : Fin 5→Fin 3,
    Assumptions6888 (a.val+1) (fun j=>(h j).val) →
    (∀j,highPairSum (fun z=>(h z).val) j≤co6888 (a.val+1) (b.val+1) (c.val+1) j) →
    Residue6888 (co6888 (a.val+1) (b.val+1) (c.val+1)) (fun j=>(h j).val) ∨
    ∃i : TwentyOneSixQuad6888Data.Case,
      (∀j,co6888 (a.val+1) (b.val+1) (c.val+1) j=TwentyOneSixQuad6888Data.co i j) ∧
      (∀j,(h j).val=TwentyOneSixQuad6888Data.high i j) := by decide +kernel

theorem actual6888 (H : Simple5Hypergraph (Fin 21)) (size : H.edges.card=34)
    (noB : ¬PropertyB H) (f : Fin 4↪Fin 21) (a b c : Fin 2)
    (hd : ∀j,H.degree (f j)=TwentyOneSixQuad6888Data.degree j)
    (hc : ∀j,H.codegree (f (first j)) (f (second j))=co6888 (a.val+1) (b.val+1) (c.val+1) j)
    (ass : Assumptions6888 (a.val+1) (fun j=>count H f (highLabels j))) :
    Residue6888 (co6888 (a.val+1) (b.val+1) (c.val+1)) (fun j=>count H f (highLabels j)) := by
  have pairBound (j) : H.codegree (f (first j)) (f (second j))≤2 := by
    rw [hc]
    have bounds : ∀a b c : Fin 2,∀j,co6888 (a.val+1) (b.val+1) (c.val+1) j≤2 := by decide
    exact bounds a b c j
  have bound := high_le_two H f pairBound
  let h : Fin 5→Fin 3 := fun j=>⟨count H f (highLabels j),by have := bound j;omega⟩
  have inv (j) : highPairSum (fun k=>(h k).val) j≤co6888 (a.val+1) (b.val+1) (c.val+1) j := by
    rw [←hc]; exact high_inventory H f j
  rcases coverage6888 a b c h ass inv with residue | ⟨i,coeq,heq⟩
  · exact residue
  · exact False.elim (noB (TwentyOneSixQuad6888.propertyB_of_data H size f i hd
      (fun j=>(hc j).trans (coeq j)) heq))

theorem equality_coverage : ∀a b : Fin 2, ∀h : Fin 2,
    h.val≤a.val → h.val≤b.val →
    ∃i : TwentyOneSixQuad6888Data.Case,
      (∀j,(![1,1,2,2,a.val+1,b.val+1] : Fin 6→ℕ) j=TwentyOneSixQuad6888Data.co i j) ∧
      (∀j,(![0,0,0,h.val,1] : Fin 5→ℕ) j=TwentyOneSixQuad6888Data.high i j) := by decide +kernel
end Aris4Math.ThirtyFour.TwentyOneSixQuadCoverage
