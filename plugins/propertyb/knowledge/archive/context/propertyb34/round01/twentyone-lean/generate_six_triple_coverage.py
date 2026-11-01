from pathlib import Path
ROOT=Path(__file__).resolve().parents[4]
out=''.join('import Aris4Math.ThirtyFour.TwentyOneSixTriple'+ds+'\n' for ds in ['666','667','668','677','678','688'])
out+='''import Aris4Math.ThirtyFour.TwentyOneSixPairs
import Aris4Math.ThirtyFour.TwentyOneSixIncidence
namespace Aris4Math.ThirtyFour.TwentyOneSixLocalTriples
open Aris4Math.ThirtyThree.TripleProfiles
set_option maxHeartbeats 0
set_option maxRecDepth 100000
'''
for ds in ['666','667','668','677','678','688']:
 name='TwentyOneSixTriple'+ds
 out+=f'''
def Suitable{ds} (a b c t : ℕ) : Prop := ∃ i : {name}Data.Case,
  a={name}Data.co i 0 ∧ b={name}Data.co i 1 ∧ c={name}Data.co i 2 ∧ t={name}Data.triple i
instance (a b c t : ℕ) : Decidable (Suitable{ds} a b c t) := by unfold Suitable{ds};infer_instance

theorem apply{ds} (H : Simple5Hypergraph (Fin 21)) (size : H.edges.card=34)
    (x y z : Fin 21) (xy : x≠y) (xz : x≠z) (yz : y≠z)
    (dx : H.degree x={ds[0]}) (dy : H.degree y={ds[1]}) (dz : H.degree z={ds[2]})
    (h : Suitable{ds} (H.codegree x y) (H.codegree x z) (H.codegree y z) (tripleCodegree H x y z)) :
    PropertyB H := by
  obtain ⟨i,ha,hb,hc,ht⟩ := h
  apply {name}.propertyB_of_data H size (threeVertices x y z xy xz yz) i
  · intro j; fin_cases j
    · exact dx
    · exact dy
    · exact dz
  · exact ha
  · exact hb
  · exact hc
  · exact ht
'''
reqs={
'666':'a.val+b.val≤6 → a.val+c.val≤6 → b.val+c.val≤6 → Suitable666 a.val b.val c.val t.val',
'667':'a.val+b.val≤6 → a.val+c.val≤6 → b.val+c.val≤7+t.val → Suitable667 a.val b.val c.val t.val',
'668':'a.val+b.val≤6 → a.val+c.val≤6 → b.val+c.val≤8+t.val →\n    (a.val=1 ∧ b.val=1 ∧ c.val=1 ∧ t.val=0) ∨\n    (a.val=2 ∧ ((b.val=1 ∧ c.val=1 ∧ t.val=0) ∨ (b.val=1 ∧ c.val=2 ∧ t.val=1) ∨ (b.val=2 ∧ c.val=1 ∧ t.val=1))) ∨\n    Suitable668 a.val b.val c.val t.val',
'677':'a.val+b.val≤6 → a.val+c.val≤7+t.val → b.val+c.val≤7+t.val →\n    (a.val=1 ∧ b.val=1 ∧ c.val=2 ∧ t.val=1) ∨\n    (a.val=2 ∧ b.val=2 ∧ c.val=1 ∧ t.val=0) ∨ Suitable677 a.val b.val c.val t.val',
'678':'a.val+b.val≤6 → a.val+c.val≤7+t.val → b.val+c.val≤8+t.val →\n    (a.val≤2 ∧ b.val≤2 ∧ c.val≤2) ∨ Suitable678 a.val b.val c.val t.val'}
for ds,req in reqs.items():
 out+=f'''
theorem coverage{ds} : ∀ a b c t : Fin 5,
    1≤a.val → 1≤b.val → 1≤c.val → t.val≤a.val → t.val≤b.val → t.val≤c.val →
    {req} := by decide +kernel
'''
out+='''
theorem coverage688 : ∀ c : Fin 9, ∀ t : Fin 2,
    3≤c.val → 1+c.val≤8+t.val → Suitable688 1 1 c.val t.val := by decide +kernel
end Aris4Math.ThirtyFour.TwentyOneSixLocalTriples
'''
(ROOT/'formal/Aris4Math/ThirtyFour/TwentyOneSixLocalTriples.lean').write_text(out)
