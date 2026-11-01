from pathlib import Path
ROOT=Path(__file__).resolve().parents[4]
s='''import Aris4Math.ThirtyFour.TwentyOneSixLocalTriples
namespace Aris4Math.ThirtyFour.TwentyOneSixStructure
open Aris4Math.ThirtyThree.TripleProfiles
open TwentyOneSixLocalTriples TwentyOneSixIncidence
set_option maxHeartbeats 0

theorem codegree_le_four (H : Simple5Hypergraph (Fin 21)) (size : H.edges.card=34)
    (noB : ¬PropertyB H) (x y : Fin 21) (xy : x≠y)
    (dx6 : 6≤H.degree x) (dx7 : H.degree x≤7) (dxy : H.degree x≤H.degree y) (dy8 : H.degree y≤8) :
    H.codegree x y≤4 := by
  by_contra hn
  exact noB (TwentyOneSixPairs.propertyB_of_high H size x y xy dx6 dx7 dxy dy8 (by omega))
'''
result={
'666':'PropertyB H',
'667':'PropertyB H',
'668':'''(H.codegree x y=1 ∧ H.codegree x z=1 ∧ H.codegree y z=1 ∧ tripleCodegree H x y z=0) ∨
    (H.codegree x y=2 ∧ ((H.codegree x z=1 ∧ H.codegree y z=1 ∧ tripleCodegree H x y z=0) ∨
      (H.codegree x z=1 ∧ H.codegree y z=2 ∧ tripleCodegree H x y z=1) ∨
      (H.codegree x z=2 ∧ H.codegree y z=1 ∧ tripleCodegree H x y z=1)))''',
'677':'''(H.codegree x y=1 ∧ H.codegree x z=1 ∧ H.codegree y z=2 ∧ tripleCodegree H x y z=1) ∨
    (H.codegree x y=2 ∧ H.codegree x z=2 ∧ H.codegree y z=1 ∧ tripleCodegree H x y z=0)''',
'678':'''H.codegree x y≤2 ∧ H.codegree x z≤2 ∧ H.codegree y z≤2'''}
for ds,target in result.items():
 name=('propertyB_of_' if ds in ['666','667'] else 'residual_')+ds
 s+=f'''
theorem {name} (H : Simple5Hypergraph (Fin 21)) (cover : H.PairCovering) (size : H.edges.card=34)
'''
 if ds not in ['666','667']:s+='    (noB : ¬PropertyB H)\n'
 s+=f'''    (x y z : Fin 21) (xy : x≠y) (xz : x≠z) (yz : y≠z)
    (dx : H.degree x=6) (dy : H.degree y={ds[1]}) (dz : H.degree z={ds[2]}) :
    {target} := by
'''
 if ds in ['666','667']:s+='  by_contra noB\n'
 s+='''  have a4 := codegree_le_four H size noB x y xy (by omega) (by omega) (by omega) (by omega)
  have b4 := codegree_le_four H size noB x z xz (by omega) (by omega) (by omega) (by omega)
  have c4 := codegree_le_four H size noB y z yz (by omega) (by omega) (by omega) (by omega)
  have a1 := H.one_le_codegree cover xy
  have b1 := H.one_le_codegree cover xz
  have c1 := H.one_le_codegree cover yz
  obtain ⟨ta,tb,tc⟩ := ThirtyThree.TwentyOnePairAssembly.tripleCodegree_le_pairs H x y z
  have ab := pair_excess H cover x y z xy xz yz dx
  obtain ⟨ixa,iya,iza⟩ := inventories H x y z xy xz yz
  rw [dx] at ixa
  rw [dy] at iya
  rw [dz] at iza
'''
 if ds[1]=='6':s+='''  have ac := pair_excess H cover y x z xy.symm yz xz dy
  rw [H.codegree_comm y x] at ac
'''
 if ds=='666':s+='''  have bc := pair_excess H cover z x y xz.symm yz.symm xy dz
  rw [H.codegree_comm z x,H.codegree_comm z y] at bc
'''
 args='ab '+('ac ' if ds[1]=='6' else 'iya ')+('bc' if ds=='666' else 'iza')
 s+=f'''  have cov := coverage{ds} ⟨H.codegree x y,by omega⟩ ⟨H.codegree x z,by omega⟩
    ⟨H.codegree y z,by omega⟩ ⟨tripleCodegree H x y z,by omega⟩ a1 b1 c1 ta tb tc {args}
'''
 if ds in ['666','667']:s+=f'  exact noB (apply{ds} H size x y z xy xz yz dx dy dz cov)\n'
 elif ds in ['668','677']:s+=f'''  rcases cov with left | right | strict
  · exact Or.inl left
  · exact Or.inr right
  · exact False.elim (noB (apply{ds} H size x y z xy xz yz dx dy dz strict))
'''
 else:s+=f'''  rcases cov with residual | strict
  · exact residual
  · exact False.elim (noB (apply{ds} H size x y z xy xz yz dx dy dz strict))
'''
s+='''
theorem unit_eight_pair (H : Simple5Hypergraph (Fin 21)) (cover : H.PairCovering) (size : H.edges.card=34)
    (noB : ¬PropertyB H) (x y z : Fin 21) (xy : x≠y) (xz : x≠z) (yz : y≠z)
    (dx : H.degree x=6) (dy : H.degree y=8) (dz : H.degree z=8)
    (unitY : H.codegree x y=1) (unitZ : H.codegree x z=1) : H.codegree y z≤2 := by
  have upper := ThirtyThree.TwentyOnePairAssembly.codegree_le_degree H y z
  rw [dy] at upper
  obtain ⟨ta,tb,tc⟩ := ThirtyThree.TwentyOnePairAssembly.tripleCodegree_le_pairs H x y z
  rw [unitY] at ta
  have inv := TwentyOneFiveStructure.pair_inventory H x y z xy xz yz
  rw [unitY,dy] at inv
  by_contra hn
  apply noB
  apply apply688 H size x y z xy xz yz dx dy dz
  rw [unitY,unitZ]
  exact coverage688 ⟨H.codegree y z,by omega⟩ ⟨tripleCodegree H x y z,by omega⟩ (by omega) inv

theorem two_six_others_eight (H : Simple5Hypergraph (Fin 21)) (cover : H.PairCovering)
    (size : H.edges.card=34) (minimum : ∀v,6≤H.degree v) (noB : ¬PropertyB H)
    (x y : Fin 21) (xy : x≠y) (dx : H.degree x=6) (dy : H.degree y=6) :
    ∀z,z≠x→z≠y→8≤H.degree z := by
  intro z zx zy
  have low := minimum z
  by_contra hn
  have cases : H.degree z=6 ∨ H.degree z=7 := by omega
  rcases cases with dz | dz
  · exact noB (propertyB_of_666 H cover size x y z xy zx.symm zy.symm dx dy dz)
  · exact noB (propertyB_of_667 H cover size x y z xy zx.symm zy.symm dx dy dz)
end Aris4Math.ThirtyFour.TwentyOneSixStructure
#print axioms Aris4Math.ThirtyFour.TwentyOneSixStructure.propertyB_of_666
#print axioms Aris4Math.ThirtyFour.TwentyOneSixStructure.two_six_others_eight
'''
(ROOT/'formal/Aris4Math/ThirtyFour/TwentyOneSixStructure.lean').write_text(s)
