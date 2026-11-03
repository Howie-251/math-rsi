import DegreeDiameter.Portfolio.FullNeighborhoodClones
import DegreeDiameter.Portfolio.F4Graph3840Exact
import Mathlib.Logic.Equiv.Fin.Basic
namespace DegreeDiameter.Portfolio.F4PlaneBlockClones
open F4Graph3840
set_option maxRecDepth 20000
set_option maxHeartbeats 20000000

def planeCode : Fin 16 → Fin 64 := ![0, 5, 10, 15, 18, 23, 24, 29, 35, 38, 41, 44, 49, 52, 59, 62]
def layers21 : Fin 9 → Fin 60 := ![18, 20, 22, 29, 31, 43, 45, 54, 56]
def layers22 : Fin 22 → Fin 60 := ![1, 4, 11, 14, 22, 23, 24, 25, 32, 33, 34, 35, 40, 46, 47, 48, 49, 50, 56, 57, 58, 59]

def form (x : Vec) : F := x 0 + x 1 + F.w * x 2

def blockIndex {K : Nat} (j : Fin (K*16)) : Fin K := ⟨j.val/16, by have hj:=j.isLt; omega⟩
def planeIndex {K : Nat} (j : Fin (K*16)) : Fin 16 := ⟨j.val%16,Nat.mod_lt _ (by decide)⟩
def center {K : Nat} (layers : Fin K → Fin 60) (j : Fin (K*16)) : Fin 3840 :=
  liftAt (layers (blockIndex j)) (planeCode (planeIndex j))
abbrev V21 := Fin 3840 ⊕ Fin (9*16)
abbrev V22 := Fin 3840 ⊕ Fin (22*16)
def graph21 : SimpleGraph V21 := FullNeighborhoodClones.graph F4Graph3840.graph (center layers21)
def graph22 : SimpleGraph V22 := FullNeighborhoodClones.graph F4Graph3840.graph (center layers22)
def label21 : V21 ≃ Fin 3984 := finSumFinEquiv
def label22 : V22 ≃ Fin 4192 := finSumFinEquiv

theorem card21 : Fintype.card V21 = 3984 := by decide
theorem card22 : Fintype.card V22 = 4192 := by decide
end DegreeDiameter.Portfolio.F4PlaneBlockClones
