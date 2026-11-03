import DegreeDiameter.Portfolio.FullNeighborhoodClones
import Mathlib.Data.ZMod.Basic
import Mathlib.Data.Fin.VecNotation
import Mathlib.Logic.Equiv.Fin.Basic
import Mathlib.Tactic.FinCases
import Mathlib.Tactic.Abel
import Mathlib.Tactic.Ring
namespace DegreeDiameter.Portfolio.F3Graph15552
set_option maxRecDepth 20000
set_option maxHeartbeats 40000000
abbrev F := ZMod 3
abbrev Vec := Fin 4 → F
abbrev Mat := Fin 4 → Fin 4 → F
def basisVec (j : Fin 4) : Vec := fun i => if i=j then 1 else 0
def act (A : Mat) (x : Vec) : Vec := fun i =>
  A i 0*x 0+A i 1*x 1+A i 2*x 2+A i 3*x 3
def controllerData : Array (Array Nat) := #[#[0, 11, 59, 79, 180], #[14, 4, 120, 45, 182], #[67, 36, 155, 125, 132], #[42, 170, 166, 21, 86], #[80, 82, 62, 1, 109], #[5, 80, 16, 28, 153], #[12, 78, 35, 47, 173], #[33, 102, 168, 78, 187], #[8, 48, 123, 26, 171], #[37, 17, 135, 127, 97], #[23, 149, 143, 99, 54], #[46, 49, 64, 0, 161], #[6, 46, 58, 102, 134], #[13, 81, 145, 80, 181], #[1, 29, 89, 101, 151], #[113, 84, 24, 52, 166], #[89, 119, 180, 186, 5], #[17, 148, 138, 9, 102], #[20, 147, 83, 62, 99], #[66, 126, 154, 147, 131], #[18, 93, 104, 169, 70], #[99, 3, 95, 75, 155], #[77, 99, 164, 130, 85], #[10, 133, 179, 132, 113], #[74, 70, 57, 133, 15], #[100, 131, 118, 72, 55], #[47, 8, 169, 49, 108], #[29, 50, 63, 31, 158], #[45, 5, 93, 50, 84], #[27, 30, 126, 14, 138], #[82, 45, 124, 29, 152], #[31, 27, 61, 81, 103], #[32, 79, 121, 48, 172], #[7, 47, 122, 46, 190], #[112, 52, 73, 139, 143], #[59, 88, 182, 178, 6], #[93, 129, 110, 2, 81], #[9, 128, 51, 64, 72], #[148, 91, 189, 128, 130], #[95, 65, 175, 146, 69], #[72, 44, 67, 74, 135], #[43, 72, 163, 170, 53], #[3, 98, 165, 97, 112], #[41, 69, 144, 98, 87], #[76, 130, 116, 40, 115], #[28, 1, 146, 30, 177], #[11, 33, 147, 12, 159], #[26, 6, 65, 33, 52], #[78, 32, 91, 8, 110], #[49, 26, 90, 11, 188], #[50, 28, 167, 27, 191], #[51, 190, 132, 182, 37], #[185, 15, 47, 34, 126], #[86, 185, 41, 159, 142], #[85, 161, 10, 138, 144], #[114, 109, 25, 161, 57], #[162, 139, 77, 111, 118], #[144, 122, 55, 61, 24], #[123, 144, 151, 163, 12], #[35, 117, 103, 166, 0], #[167, 118, 187, 117, 82], #[120, 57, 171, 164, 31], #[62, 18, 111, 68, 4], #[128, 96, 108, 95, 27], #[91, 37, 139, 96, 11], #[65, 94, 109, 39, 47], #[19, 125, 156, 93, 98], #[2, 92, 105, 126, 40], #[129, 62, 184, 92, 170], #[132, 100, 39, 43, 105], #[97, 76, 20, 24, 107], #[98, 77, 94, 76, 154], #[40, 25, 37, 41, 104], #[75, 97, 88, 150, 34], #[24, 40, 186, 149, 141], #[73, 21, 178, 131, 114], #[44, 71, 142, 70, 162], #[22, 132, 119, 71, 56], #[48, 7, 92, 6, 176], #[102, 0, 125, 32, 160], #[4, 13, 128, 5, 185], #[101, 31, 36, 13, 139], #[30, 101, 60, 4, 183], #[105, 191, 97, 171, 18], #[176, 87, 28, 15, 91], #[54, 176, 22, 185, 117], #[53, 138, 3, 110, 119], #[140, 111, 43, 84, 116], #[119, 167, 115, 35, 73], #[16, 179, 173, 143, 14], #[168, 116, 181, 179, 49], #[64, 95, 84, 38, 48], #[92, 68, 177, 67, 78], #[36, 66, 161, 20, 28], #[96, 127, 157, 65, 71], #[39, 63, 107, 91, 21], #[94, 64, 174, 63, 149], #[70, 42, 9, 73, 83], #[71, 43, 66, 42, 189], #[21, 10, 18, 22, 175], #[25, 150, 117, 69, 140], #[81, 14, 127, 82, 137], #[79, 12, 17, 7, 111], #[173, 184, 31, 175, 59], #[104, 173, 72, 152, 20], #[83, 181, 69, 180, 67], #[157, 171, 131, 181, 148], #[107, 187, 70, 151, 95], #[138, 162, 26, 140, 63], #[160, 115, 4, 55, 65], #[137, 86, 48, 115, 36], #[158, 56, 102, 87, 62], #[34, 160, 42, 177, 164], #[15, 137, 23, 160, 163], #[55, 158, 75, 176, 179], #[141, 110, 44, 109, 88], #[166, 120, 87, 90, 44], #[142, 60, 85, 59, 100], #[143, 123, 56, 60, 25], #[88, 168, 86, 16, 77], #[61, 142, 134, 116, 1], #[122, 143, 191, 142, 32], #[121, 186, 183, 57, 33], #[58, 165, 153, 118, 8], #[145, 166, 190, 165, 30], #[169, 2, 158, 66, 79], #[126, 67, 52, 19, 29], #[127, 9, 176, 94, 101], #[63, 38, 160, 37, 80], #[68, 169, 136, 36, 150], #[131, 22, 38, 44, 136], #[130, 75, 19, 25, 106], #[69, 23, 2, 77, 51], #[150, 24, 148, 23, 184], #[153, 174, 12, 155, 120], #[175, 153, 40, 188, 9], #[136, 151, 130, 190, 129], #[110, 140, 101, 113, 147], #[108, 54, 29, 86, 17], #[159, 34, 81, 56, 64], #[87, 108, 100, 137, 186], #[115, 159, 74, 158, 165], #[117, 121, 53, 120, 76], #[118, 89, 34, 121, 10], #[57, 145, 54, 58, 43], #[124, 178, 172, 144, 13], #[146, 39, 159, 148, 45], #[147, 19, 137, 18, 46], #[38, 146, 106, 17, 133], #[170, 74, 96, 10, 156], #[133, 73, 129, 100, 174], #[180, 107, 14, 136, 58], #[172, 104, 30, 174, 168], #[134, 154, 5, 135, 123], #[184, 172, 71, 153, 19], #[155, 134, 21, 183, 2], #[156, 182, 149, 187, 66], #[106, 180, 170, 191, 94], #[111, 141, 27, 114, 125], #[139, 53, 46, 141, 146], #[109, 113, 79, 112, 128], #[177, 55, 11, 54, 93], #[56, 177, 76, 108, 178], #[164, 58, 113, 167, 41], #[163, 61, 112, 168, 22], #[179, 124, 141, 123, 42], #[116, 59, 15, 124, 3], #[60, 163, 188, 88, 50], #[90, 164, 152, 119, 7], #[125, 20, 185, 129, 26], #[149, 41, 68, 3, 157], #[182, 83, 8, 106, 61], #[152, 175, 32, 154, 145], #[103, 189, 6, 104, 89], #[174, 152, 150, 134, 96], #[135, 103, 99, 172, 39], #[84, 114, 78, 85, 127], #[161, 112, 45, 162, 92], #[186, 35, 162, 145, 75], #[165, 90, 114, 89, 23], #[151, 105, 0, 157, 16], #[187, 106, 13, 105, 90], #[171, 51, 1, 156, 35], #[188, 155, 82, 189, 122], #[154, 188, 133, 103, 68], #[52, 85, 80, 53, 169], #[178, 16, 140, 122, 74], #[181, 156, 7, 107, 60], #[183, 135, 49, 184, 167], #[189, 183, 98, 173, 38], #[191, 136, 33, 51, 124], #[190, 157, 50, 83, 121]]
def matrixData : Array (Array Nat) := #[#[0, 0, 0, 0, 1, 0, 2, 1, 2, 0, 1, 0, 0, 1, 1, 0], #[0, 0, 0, 0, 0, 2, 0, 1, 2, 1, 2, 1, 0, 2, 2, 2], #[2, 1, 1, 2, 0, 0, 0, 0, 1, 1, 1, 1, 0, 1, 2, 1], #[0, 0, 0, 0, 2, 1, 1, 2, 1, 0, 1, 1, 0, 2, 1, 2], #[0, 0, 0, 0, 2, 1, 0, 2, 0, 2, 2, 1, 1, 0, 2, 0]]
def directionData : Array (Array Nat) := #[#[1, 2, 1, 0], #[1, 2, 2, 0], #[0, 1, 0, 1], #[1, 1, 1, 1], #[1, 2, 1, 2]]
def constantData : Array (Array Nat) := #[#[0, 0, 0, 0], #[0, 0, 0, 0], #[0, 0, 0, 0], #[0, 0, 0, 0], #[0, 0, 0, 0]]

def controller (a : Fin 192) (p : Fin 5) : Fin 192 :=
  ⟨(controllerData.getD a.val #[]).getD p.val 0 %192,Nat.mod_lt _ (by decide)⟩
def matrix (p : Fin 5) : Mat := fun i j =>
  ((matrixData.getD p.val #[]).getD (4*i.val+j.val) 0 : F)
def direction (p : Fin 5) : Vec := fun i => ((directionData.getD p.val #[]).getD i.val 0 : F)
def constant (p : Fin 5) : Vec := fun i => ((constantData.getD p.val #[]).getD i.val 0 : F)
theorem constant_zero : ∀p,constant p=0 := by decide +kernel
def inverseType : Fin 5 → Fin 5 := ![0,3,4,1,2]
theorem controller_reverse_type : ∀a p,controller (controller a p) (inverseType p)=a := by decide +kernel
def encodeVec (x : Vec) : Fin 81 :=
  ⟨(x 0).val+3*(x 1).val+9*(x 2).val+27*(x 3).val,by
    have h0:=ZMod.val_lt (x 0);have h1:=ZMod.val_lt (x 1)
    have h2:=ZMod.val_lt (x 2);have h3:=ZMod.val_lt (x 3)
    omega⟩
def decodeVec (x : Fin 81) : Vec := fun i => (x.val/3^i.val%3 : Nat)
theorem decodeVec_encodeVec (x : Vec) : decodeVec (encodeVec x)=x := by
  have h0:=ZMod.val_lt (x 0);have h1:=ZMod.val_lt (x 1)
  have h2:=ZMod.val_lt (x 2);have h3:=ZMod.val_lt (x 3)
  funext i
  fin_cases i
  · change ((((x 0).val+3*(x 1).val+9*(x 2).val+27*(x 3).val)/1%3 : Nat) : F)=x 0
    rw [show ((x 0).val+3*(x 1).val+9*(x 2).val+27*(x 3).val)/1%3=(x 0).val by omega]
    exact ZMod.natCast_zmod_val _
  · change ((((x 0).val+3*(x 1).val+9*(x 2).val+27*(x 3).val)/3%3 : Nat) : F)=x 1
    rw [show ((x 0).val+3*(x 1).val+9*(x 2).val+27*(x 3).val)/3%3=(x 1).val by omega]
    exact ZMod.natCast_zmod_val _
  · change ((((x 0).val+3*(x 1).val+9*(x 2).val+27*(x 3).val)/9%3 : Nat) : F)=x 2
    rw [show ((x 0).val+3*(x 1).val+9*(x 2).val+27*(x 3).val)/9%3=(x 2).val by omega]
    exact ZMod.natCast_zmod_val _
  · change ((((x 0).val+3*(x 1).val+9*(x 2).val+27*(x 3).val)/27%3 : Nat) : F)=x 3
    rw [show ((x 0).val+3*(x 1).val+9*(x 2).val+27*(x 3).val)/27%3=(x 3).val by omega]
    exact ZMod.natCast_zmod_val _
theorem encodeVec_decodeVec : ∀x,encodeVec (decodeVec x)=x := by decide +kernel
def controllerOf (u : Fin 15552) : Fin 192 := ⟨u.val/81,by have h:=u.isLt;omega⟩
def fiberOf (u : Fin 15552) : Fin 81 := ⟨u.val%81,Nat.mod_lt _ (by decide)⟩
def liftAt (a : Fin 192) (x : Fin 81) : Fin 15552 :=
  ⟨81*a.val+x.val,by have ha:=a.isLt;have hx:=x.isLt;omega⟩
theorem controllerOf_liftAt (a : Fin 192) (x : Fin 81) : controllerOf (liftAt a x)=a := by
  apply Fin.ext
  change (81*a.val+x.val)/81=a.val
  have hx:=x.isLt;omega
theorem fiberOf_liftAt (a : Fin 192) (x : Fin 81) : fiberOf (liftAt a x)=x := by
  apply Fin.ext
  change (81*a.val+x.val)%81=x.val
  have hx:=x.isLt;omega
theorem liftAt_parts (u : Fin 15552) : liftAt (controllerOf u) (fiberOf u)=u := by
  apply Fin.ext
  change 81*(u.val/81)+u.val%81=u.val
  omega
def stepVec (p : Fin 5) (t : F) (x : Vec) : Vec := act (matrix p) x+constant p+t • direction p
def forward (u : Fin 15552) (p : Fin 5) (t : F) : Fin 15552 :=
  liftAt (controller (controllerOf u) p) (encodeVec (stepVec p t (decodeVec (fiberOf u))))
def graph : SimpleGraph (Fin 15552) where
  Adj u v := u≠v ∧ ((∃p t,forward u p t=v) ∨ (∃p t,forward v p t=u))
  symm := by intro u v h;exact ⟨Ne.symm h.1,h.2.elim Or.inr Or.inl⟩
  loopless := by intro u h;exact h.1 rfl
instance : DecidableRel graph.Adj := by
  intro u v
  change Decidable (u≠v ∧ ((∃p t,forward u p t=v) ∨ (∃p t,forward v p t=u)))
  infer_instance
theorem forward_adj_of_ne (u : Fin 15552) (p : Fin 5) (t : F) (h : u≠forward u p t) :
    graph.Adj u (forward u p t) := ⟨h,Or.inl ⟨p,t,rfl⟩⟩
theorem forward_liftAt (a : Fin 192) (x : Vec) (p : Fin 5) (t : F) :
    forward (liftAt a (encodeVec x)) p t=liftAt (controller a p) (encodeVec (stepVec p t x)) := by
  simp only [forward,controllerOf_liftAt,fiberOf_liftAt,decodeVec_encodeVec]
def source_label : Fin 15552 ≃ Fin 15552 := Equiv.refl _
def SourceFinalClaim : Prop := Fintype.card (Fin 15552)=15552 ∧
  (∀v,graph.degree v≤15) ∧ DiameterAtMost graph 4 ∧ ¬DiameterAtMost graph 3
namespace Clone16389
abbrev Vertex := Fin 15552 ⊕ Fin 837
def layerData : Array Nat := #[16, 35, 52, 58, 59, 61, 72, 89, 91, 92, 93, 108, 109, 111, 120, 123, 127, 138, 146, 147, 150, 158, 160, 172, 181, 183, 185, 187, 188, 190, 191]
def layer (i : Fin 31) : Fin 192 := ⟨layerData.getD i.val 0 %192,Nat.mod_lt _ (by decide)⟩
def planeVec (a b c : Fin 3) : Vec := ![(a.val:F),0,(b.val:F),(c.val:F)]
def center (j : Fin 837) : Fin 15552 :=
  liftAt (layer ⟨j.val/27,by have h:=j.isLt;omega⟩)
    (encodeVec (planeVec ⟨j.val%3,Nat.mod_lt _ (by decide)⟩
      ⟨j.val/3%3,Nat.mod_lt _ (by decide)⟩ ⟨j.val/9%3,Nat.mod_lt _ (by decide)⟩))
abbrev graph := FullNeighborhoodClones.graph F3Graph15552.graph center
instance : DecidableRel graph.Adj := inferInstanceAs
  (DecidableRel (FullNeighborhoodClones.graph F3Graph15552.graph center).Adj)
def label : Vertex ≃ Fin 16389 := finSumFinEquiv
theorem label_new (j : Fin 837) : (label (.inr j)).val=15552+j.val := rfl
theorem label_old (v : Fin 15552) : (label (.inl v)).val=v.val := rfl
def FinalClaim : Prop := Fintype.card Vertex=16389 ∧ (∀v,graph.degree v≤16) ∧
  DiameterAtMost graph 4 ∧ ¬DiameterAtMost graph 3
#check (label : Vertex ≃ Fin 16389)
end Clone16389
#print axioms forward_adj_of_ne
end DegreeDiameter.Portfolio.F3Graph15552
