import DegreeDiameter.Portfolio.F3Graph15552Clone16416Definitions
import DegreeDiameter.Portfolio.F3Graph15552FullCloneInputs
namespace DegreeDiameter.Portfolio.F3Graph15552.Clone16416
set_option maxRecDepth 20000
set_option maxHeartbeats 40000000
open Clone16389 (recover recover_plane)
def ownerIndex (n : Nat) : Fin 32 × Fin 5 :=
  if n < 96 then
    if n < 48 then
      if n < 24 then
        if n < 12 then
          if n < 6 then
            if n < 3 then
              if n < 1 then
                (0, 0)
              else
                if n < 2 then
                  (8, 0)
                else
                  (17, 0)
            else
              if n < 4 then
                (20, 2)
              else
                if n < 5 then
                  (1, 1)
                else
                  (4, 0)
          else
            if n < 9 then
              if n < 7 then
                (7, 0)
              else
                if n < 8 then
                  (29, 2)
                else
                  (6, 0)
            else
              if n < 10 then
                (0, 0)
              else
                if n < 11 then
                  (0, 0)
                else
                  (0, 1)
        else
          if n < 18 then
            if n < 15 then
              if n < 13 then
                (5, 0)
              else
                if n < 14 then
                  (0, 0)
                else
                  (1, 0)
            else
              if n < 16 then
                (24, 0)
              else
                if n < 17 then
                  (4, 2)
                else
                  (26, 3)
          else
            if n < 21 then
              if n < 19 then
                (10, 0)
              else
                if n < 20 then
                  (0, 0)
                else
                  (9, 0)
            else
              if n < 22 then
                (3, 3)
              else
                if n < 23 then
                  (19, 2)
                else
                  (24, 2)
      else
        if n < 36 then
          if n < 30 then
            if n < 27 then
              if n < 25 then
                (0, 0)
              else
                if n < 26 then
                  (16, 2)
                else
                  (6, 3)
            else
              if n < 28 then
                (12, 1)
              else
                if n < 29 then
                  (4, 3)
                else
                  (8, 1)
          else
            if n < 33 then
              if n < 31 then
                (0, 0)
              else
                if n < 32 then
                  (12, 0)
                else
                  (28, 2)
            else
              if n < 34 then
                (31, 2)
              else
                if n < 35 then
                  (18, 4)
                else
                  (5, 2)
        else
          if n < 42 then
            if n < 39 then
              if n < 37 then
                (2, 1)
              else
                if n < 38 then
                  (0, 0)
                else
                  (26, 0)
            else
              if n < 40 then
                (0, 0)
              else
                if n < 41 then
                  (17, 4)
                else
                  (15, 0)
          else
            if n < 45 then
              if n < 43 then
                (3, 0)
              else
                if n < 44 then
                  (21, 2)
                else
                  (0, 0)
            else
              if n < 46 then
                (1, 3)
              else
                if n < 47 then
                  (7, 1)
                else
                  (5, 3)
    else
      if n < 72 then
        if n < 60 then
          if n < 54 then
            if n < 51 then
              if n < 49 then
                (6, 1)
              else
                if n < 50 then
                  (30, 2)
                else
                  (0, 0)
            else
              if n < 52 then
                (31, 3)
              else
                if n < 53 then
                  (13, 1)
                else
                  (20, 0)
          else
            if n < 57 then
              if n < 55 then
                (19, 0)
              else
                if n < 56 then
                  (11, 4)
                else
                  (27, 0)
            else
              if n < 58 then
                (16, 4)
              else
                if n < 59 then
                  (7, 2)
                else
                  (0, 2)
        else
          if n < 66 then
            if n < 63 then
              if n < 61 then
                (29, 4)
              else
                if n < 62 then
                  (12, 2)
                else
                  (9, 3)
            else
              if n < 64 then
                (23, 3)
              else
                if n < 65 then
                  (23, 1)
                else
                  (22, 3)
          else
            if n < 69 then
              if n < 67 then
                (0, 0)
              else
                if n < 68 then
                  (2, 0)
                else
                  (0, 0)
            else
              if n < 70 then
                (15, 1)
              else
                if n < 71 then
                  (10, 4)
                else
                  (22, 4)
      else
        if n < 84 then
          if n < 78 then
            if n < 75 then
              if n < 73 then
                (11, 3)
              else
                if n < 74 then
                  (13, 2)
                else
                  (25, 2)
            else
              if n < 76 then
                (18, 0)
              else
                if n < 77 then
                  (27, 2)
                else
                  (0, 0)
          else
            if n < 81 then
              if n < 79 then
                (5, 1)
              else
                if n < 80 then
                  (0, 3)
                else
                  (4, 1)
            else
              if n < 82 then
                (12, 3)
              else
                if n < 83 then
                  (0, 0)
                else
                  (9, 2)
        else
          if n < 90 then
            if n < 87 then
              if n < 85 then
                (21, 3)
              else
                if n < 86 then
                  (0, 0)
                else
                  (3, 4)
            else
              if n < 88 then
                (15, 4)
              else
                if n < 89 then
                  (18, 2)
                else
                  (8, 2)
          else
            if n < 93 then
              if n < 91 then
                (0, 0)
              else
                if n < 92 then
                  (14, 1)
                else
                  (17, 1)
            else
              if n < 94 then
                (10, 1)
              else
                if n < 95 then
                  (23, 0)
                else
                  (0, 0)
  else
    if n < 144 then
      if n < 120 then
        if n < 108 then
          if n < 102 then
            if n < 99 then
              if n < 97 then
                (22, 0)
              else
                if n < 98 then
                  (18, 1)
                else
                  (15, 3)
            else
              if n < 100 then
                (9, 4)
              else
                if n < 101 then
                  (11, 0)
                else
                  (8, 3)
          else
            if n < 105 then
              if n < 103 then
                (7, 3)
              else
                if n < 104 then
                  (12, 4)
                else
                  (10, 2)
            else
              if n < 106 then
                (17, 2)
              else
                if n < 107 then
                  (26, 2)
                else
                  (29, 3)
        else
          if n < 114 then
            if n < 111 then
              if n < 109 then
                (27, 3)
              else
                if n < 110 then
                  (16, 1)
                else
                  (20, 3)
            else
              if n < 112 then
                (21, 1)
              else
                if n < 113 then
                  (13, 0)
                else
                  (0, 0)
          else
            if n < 117 then
              if n < 115 then
                (16, 0)
              else
                if n < 116 then
                  (25, 0)
                else
                  (21, 4)
            else
              if n < 118 then
                (19, 4)
              else
                if n < 119 then
                  (11, 2)
                else
                  (20, 4)
      else
        if n < 132 then
          if n < 126 then
            if n < 123 then
              if n < 121 then
                (1, 2)
              else
                if n < 122 then
                  (0, 0)
                else
                  (0, 0)
            else
              if n < 124 then
                (6, 2)
              else
                if n < 125 then
                  (31, 4)
                else
                  (2, 3)
          else
            if n < 129 then
              if n < 127 then
                (17, 3)
              else
                if n < 128 then
                  (22, 1)
                else
                  (14, 3)
            else
              if n < 130 then
                (0, 0)
              else
                if n < 131 then
                  (14, 4)
                else
                  (11, 1)
        else
          if n < 138 then
            if n < 135 then
              if n < 133 then
                (2, 4)
              else
                if n < 134 then
                  (26, 4)
                else
                  (7, 4)
            else
              if n < 136 then
                (30, 1)
              else
                if n < 137 then
                  (31, 1)
                else
                  (24, 1)
          else
            if n < 141 then
              if n < 139 then
                (20, 1)
              else
                if n < 140 then
                  (13, 3)
                else
                  (21, 0)
            else
              if n < 142 then
                (0, 0)
              else
                if n < 143 then
                  (0, 0)
                else
                  (13, 4)
    else
      if n < 168 then
        if n < 156 then
          if n < 150 then
            if n < 147 then
              if n < 145 then
                (15, 2)
              else
                if n < 146 then
                  (28, 4)
                else
                  (26, 1)
            else
              if n < 148 then
                (9, 1)
              else
                if n < 149 then
                  (14, 0)
                else
                  (23, 4)
          else
            if n < 153 then
              if n < 151 then
                (18, 3)
              else
                if n < 152 then
                  (8, 4)
                else
                  (28, 0)
            else
              if n < 154 then
                (4, 4)
              else
                if n < 155 then
                  (28, 3)
                else
                  (2, 2)
        else
          if n < 162 then
            if n < 159 then
              if n < 157 then
                (29, 1)
              else
                if n < 158 then
                  (22, 2)
                else
                  (25, 3)
            else
              if n < 160 then
                (25, 1)
              else
                if n < 161 then
                  (24, 3)
                else
                  (16, 3)
          else
            if n < 165 then
              if n < 163 then
                (0, 0)
              else
                if n < 164 then
                  (24, 4)
                else
                  (0, 0)
            else
              if n < 166 then
                (25, 4)
              else
                if n < 167 then
                  (3, 2)
                else
                  (30, 4)
      else
        if n < 180 then
          if n < 174 then
            if n < 171 then
              if n < 169 then
                (0, 0)
              else
                if n < 170 then
                  (10, 3)
                else
                  (3, 1)
            else
              if n < 172 then
                (6, 4)
              else
                if n < 173 then
                  (0, 0)
                else
                  (5, 4)
          else
            if n < 177 then
              if n < 175 then
                (23, 2)
              else
                if n < 176 then
                  (28, 1)
                else
                  (19, 1)
            else
              if n < 178 then
                (27, 1)
              else
                if n < 179 then
                  (27, 4)
                else
                  (0, 0)
        else
          if n < 186 then
            if n < 183 then
              if n < 181 then
                (0, 4)
              else
                if n < 182 then
                  (29, 0)
                else
                  (1, 4)
            else
              if n < 184 then
                (30, 0)
              else
                if n < 185 then
                  (30, 3)
                else
                  (19, 3)
          else
            if n < 189 then
              if n < 187 then
                (0, 0)
              else
                if n < 188 then
                  (0, 0)
                else
                  (0, 0)
            else
              if n < 190 then
                (14, 2)
              else
                if n < 191 then
                  (0, 0)
                else
                  (31, 0)
def owner (a : Fin 192) : Fin 32 × Fin 5 := ownerIndex a.val
/-- Only the new 32×5 positive table, including self-controller targets. -/
theorem owner_forward : ∀(i : Fin 32)(p : Fin 5),
    owner (controller (layer i) p)=(i,p) := by decide +kernel
def cloneBlock (j : Fin 864) : Fin 32 :=
  ⟨j.val/27,by have h := j.isLt;omega⟩
def cloneA (j : Fin 864) : Fin 3 := ⟨j.val%3,Nat.mod_lt _ (by decide)⟩
def cloneB (j : Fin 864) : Fin 3 := ⟨j.val/3%3,Nat.mod_lt _ (by decide)⟩
def cloneC (j : Fin 864) : Fin 3 := ⟨j.val/9%3,Nat.mod_lt _ (by decide)⟩

theorem center_eq_parts (j : Fin 864) : center j =
    liftAt (layer (cloneBlock j))
      (encodeVec (planeVec (cloneA j) (cloneB j) (cloneC j))) := rfl

/-- The clone index has weights (1,3,9), while the old fiber encoding has
weights (1,9,27) on plane coordinates (0,2,3). -/
def makeIndex (i : Fin 32) (a b c : F) : Fin 864 :=
  ⟨27*i.val+a.val+3*b.val+9*c.val,by
    have hi := i.isLt
    have ha := ZMod.val_lt a
    have hb := ZMod.val_lt b
    have hc := ZMod.val_lt c
    omega⟩

theorem makeIndex_reassemble (j : Fin 864) :
    makeIndex (cloneBlock j) ((planeVec (cloneA j) (cloneB j) (cloneC j)) 0)
      ((planeVec (cloneA j) (cloneB j) (cloneC j)) 2)
      ((planeVec (cloneA j) (cloneB j) (cloneC j)) 3) = j := by
  apply Fin.ext
  change 27*(cloneBlock j).val+((cloneA j).val:F).val+
    3*((cloneB j).val:F).val+9*((cloneC j).val:F).val = j.val
  rw [ZMod.val_natCast_of_lt (cloneA j).isLt,
    ZMod.val_natCast_of_lt (cloneB j).isLt,
    ZMod.val_natCast_of_lt (cloneC j).isLt]
  simp only [cloneBlock,cloneA,cloneB,cloneC]
  omega

def pinCoordinates (v : Fin 15552) : Vec :=
  recover (owner (controllerOf v)).2 (decodeVec (fiberOf v))

def pinOwner (v : Fin 15552) : Fin 864 :=
  makeIndex (owner (controllerOf v)).1
    ((pinCoordinates v) 0) ((pinCoordinates v) 2) ((pinCoordinates v) 3)

/-- Completed outputs recover their original center even when that output
is a removed virtual self.  Only actual adjacency is used for load below. -/
theorem pinOwner_forward (j : Fin 864) (p : Fin 5) (t : F) :
    pinOwner (forward (center j) p t) = j := by
  let i := cloneBlock j
  let a := cloneA j
  let b := cloneB j
  let c := cloneC j
  have hcenter : center j = liftAt (layer i) (encodeVec (planeVec a b c)) := rfl
  have hc : controllerOf (forward (center j) p t) = controller (layer i) p := by
    rw [hcenter,forward_liftAt,controllerOf_liftAt]
  have hf : decodeVec (fiberOf (forward (center j) p t)) =
      stepVec p t (planeVec a b c) := by
    rw [hcenter,forward_liftAt,fiberOf_liftAt,decodeVec_encodeVec]
  have ho : owner (controllerOf (forward (center j) p t)) = (i,p) := by
    rw [hc,owner_forward]
  have hcoordinates : pinCoordinates (forward (center j) p t) = planeVec a b c := by
    simp only [pinCoordinates,ho,hf]
    exact recover_plane p t a b c
  calc
    pinOwner (forward (center j) p t) =
        makeIndex i ((planeVec a b c) 0) ((planeVec a b c) 2) ((planeVec a b c) 3) := by
          simp only [pinOwner,ho,hcoordinates]
    _ = j := makeIndex_reassemble j

/-- The adjacency bridge handles both source-origin disjuncts before the
center-originating formula is used.  No independence of centers is assumed. -/
theorem common_pin_index_unique (v : Fin 15552) (i j : Fin 864)
    (hi : F3Graph15552.graph.Adj v (center i))
    (hj : F3Graph15552.graph.Adj v (center j)) : i = j := by
  obtain ⟨_,p,s,hp⟩ := (adj_iff_forward _ _).mp (F3Graph15552.graph.symm hi)
  obtain ⟨_,q,t,hq⟩ := (adj_iff_forward _ _).mp (F3Graph15552.graph.symm hj)
  have h := congrArg pinOwner (hp.trans hq.symm)
  simpa only [pinOwner_forward] using h

theorem load_le_one (v : Fin 15552) :
    FullNeighborhoodClones.load F3Graph15552.graph center v ≤ 1 := by
  apply Fintype.card_le_one_iff.mpr
  intro x y
  apply Subtype.ext
  exact common_pin_index_unique v x.val y.val x.property y.property

#print axioms pinOwner_forward
#print axioms load_le_one
end DegreeDiameter.Portfolio.F3Graph15552.Clone16416
