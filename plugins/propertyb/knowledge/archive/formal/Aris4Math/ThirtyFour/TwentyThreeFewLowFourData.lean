import Aris4Math.ThirtyFour.TwentyThreeFewLowBase
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

namespace OneLow
open TwentyThreeFewLowBase (Case oneLow)
abbrev NewCase := Fin 73
abbrev Perm := Fin 6

def μ : NewCase → Finset (Fin 4) → ℕ

  | 0, T => if T=∅ then 12 else if T={0} then 4 else if T={1} then 5 else if T={0,1} then 1 else if T={2} then 5 else if T={3} then 5 else if T={0,2,3} then 1 else if T={1,2,3} then 1 else 0

  | 1, T => if T=∅ then 13 else if T={0} then 4 else if T={1} then 4 else if T={2} then 4 else if T={1,2} then 1 else if T={0,1,2} then 1 else if T={3} then 5 else if T={0,3} then 1 else if T={1,2,3} then 1 else 0

  | 2, T => if T=∅ then 12 else if T={0} then 4 else if T={1} then 4 else if T={0,1} then 1 else if T={2} then 5 else if T={1,2} then 1 else if T={3} then 5 else if T={1,3} then 1 else if T={0,2,3} then 1 else 0

  | 3, T => if T=∅ then 13 else if T={0} then 4 else if T={1} then 4 else if T={0,1} then 1 else if T={2} then 4 else if T={1,2} then 1 else if T={3} then 5 else if T={0,2,3} then 1 else if T={1,2,3} then 1 else 0

  | 4, T => if T=∅ then 13 else if T={0} then 4 else if T={1} then 3 else if T={0,1} then 1 else if T={2} then 4 else if T={1,2} then 2 else if T={3} then 5 else if T={1,3} then 1 else if T={0,2,3} then 1 else 0

  | 5, T => if T=∅ then 14 else if T={0} then 4 else if T={1} then 3 else if T={0,1} then 1 else if T={2} then 3 else if T={1,2} then 2 else if T={3} then 5 else if T={0,2,3} then 1 else if T={1,2,3} then 1 else 0

  | 6, T => if T=∅ then 14 else if T={0} then 4 else if T={1} then 2 else if T={0,1} then 1 else if T={2} then 3 else if T={1,2} then 3 else if T={3} then 5 else if T={1,3} then 1 else if T={0,2,3} then 1 else 0

  | 7, T => if T=∅ then 13 else if T={0} then 4 else if T={1} then 4 else if T={0,1} then 1 else if T={2} then 4 else if T={1,2} then 1 else if T={3} then 4 else if T={1,3} then 1 else if T={2,3} then 1 else if T={0,2,3} then 1 else 0

  | 8, T => if T=∅ then 14 else if T={0} then 4 else if T={1} then 3 else if T={2} then 4 else if T={0,2} then 1 else if T={1,2} then 1 else if T={3} then 4 else if T={1,3} then 1 else if T={0,1,3} then 1 else if T={1,2,3} then 1 else 0

  | 9, T => if T=∅ then 14 else if T={0} then 4 else if T={1} then 3 else if T={2} then 3 else if T={1,2} then 2 else if T={0,1,2} then 1 else if T={3} then 4 else if T={0,3} then 1 else if T={1,3} then 1 else if T={2,3} then 1 else 0

  | 10, T => if T=∅ then 14 else if T={0} then 4 else if T={1} then 3 else if T={0,1} then 1 else if T={2} then 3 else if T={1,2} then 2 else if T={3} then 4 else if T={1,3} then 1 else if T={2,3} then 1 else if T={0,2,3} then 1 else 0

  | 11, T => if T=∅ then 15 else if T={0} then 4 else if T={1} then 2 else if T={2} then 3 else if T={0,2} then 1 else if T={1,2} then 2 else if T={3} then 4 else if T={1,3} then 1 else if T={0,1,3} then 1 else if T={1,2,3} then 1 else 0

  | 12, T => if T=∅ then 15 else if T={0} then 4 else if T={1} then 2 else if T={0,1} then 1 else if T={2} then 2 else if T={1,2} then 3 else if T={3} then 4 else if T={1,3} then 1 else if T={2,3} then 1 else if T={0,2,3} then 1 else 0

  | 13, T => if T=∅ then 15 else if T={0} then 4 else if T={1} then 2 else if T={2} then 3 else if T={0,2} then 1 else if T={1,2} then 2 else if T={3} then 3 else if T={1,3} then 2 else if T={0,1,3} then 1 else if T={2,3} then 1 else 0

  | 14, T => if T=∅ then 16 else if T={0} then 4 else if T={1} then 1 else if T={2} then 2 else if T={0,2} then 1 else if T={1,2} then 3 else if T={3} then 3 else if T={1,3} then 2 else if T={0,1,3} then 1 else if T={2,3} then 1 else 0

  | 15, T => if T=∅ then 12 else if T={0} then 3 else if T={1} then 5 else if T={0,1} then 1 else if T={2} then 5 else if T={0,2} then 1 else if T={3} then 5 else if T={0,3} then 1 else if T={1,2,3} then 1 else 0

  | 16, T => if T=∅ then 13 else if T={0} then 3 else if T={1} then 4 else if T={0,1} then 1 else if T={2} then 4 else if T={0,2} then 1 else if T={1,2} then 1 else if T={3} then 5 else if T={0,3} then 1 else if T={1,2,3} then 1 else 0

  | 17, T => if T=∅ then 14 else if T={0} then 3 else if T={1} then 3 else if T={0,1} then 1 else if T={2} then 3 else if T={0,2} then 1 else if T={1,2} then 2 else if T={3} then 5 else if T={0,3} then 1 else if T={1,2,3} then 1 else 0

  | 18, T => if T=∅ then 13 else if T={0} then 3 else if T={1} then 4 else if T={0,1} then 1 else if T={2} then 4 else if T={0,2} then 1 else if T={1,2} then 1 else if T={3} then 4 else if T={0,3} then 1 else if T={1,3} then 1 else if T={2,3} then 1 else 0

  | 19, T => if T=∅ then 14 else if T={0} then 3 else if T={1} then 3 else if T={0,1} then 1 else if T={2} then 4 else if T={0,2} then 1 else if T={1,2} then 1 else if T={3} then 4 else if T={0,3} then 1 else if T={1,3} then 1 else if T={1,2,3} then 1 else 0

  | 20, T => if T=∅ then 14 else if T={0} then 3 else if T={1} then 3 else if T={0,1} then 1 else if T={2} then 3 else if T={0,2} then 1 else if T={1,2} then 2 else if T={3} then 4 else if T={0,3} then 1 else if T={1,3} then 1 else if T={2,3} then 1 else 0

  | 21, T => if T=∅ then 15 else if T={0} then 3 else if T={1} then 2 else if T={0,1} then 1 else if T={2} then 3 else if T={0,2} then 1 else if T={1,2} then 2 else if T={3} then 4 else if T={0,3} then 1 else if T={1,3} then 1 else if T={1,2,3} then 1 else 0

  | 22, T => if T=∅ then 15 else if T={0} then 3 else if T={1} then 2 else if T={0,1} then 1 else if T={2} then 2 else if T={0,2} then 1 else if T={1,2} then 3 else if T={3} then 4 else if T={0,3} then 1 else if T={1,3} then 1 else if T={2,3} then 1 else 0

  | 23, T => if T=∅ then 15 else if T={0} then 3 else if T={1} then 2 else if T={0,1} then 1 else if T={2} then 3 else if T={0,2} then 1 else if T={1,2} then 2 else if T={3} then 3 else if T={0,3} then 1 else if T={1,3} then 2 else if T={2,3} then 1 else 0

  | 24, T => if T=∅ then 16 else if T={0} then 3 else if T={1} then 1 else if T={0,1} then 1 else if T={2} then 3 else if T={0,2} then 1 else if T={1,2} then 2 else if T={3} then 3 else if T={0,3} then 1 else if T={1,3} then 2 else if T={1,2,3} then 1 else 0

  | 25, T => if T=∅ then 16 else if T={0} then 3 else if T={1} then 1 else if T={0,1} then 1 else if T={2} then 2 else if T={0,2} then 1 else if T={1,2} then 3 else if T={3} then 3 else if T={0,3} then 1 else if T={1,3} then 2 else if T={2,3} then 1 else 0

  | 26, T => if T=∅ then 17 else if T={0} then 3 else if T={1} then 2 else if T={0,1} then 1 else if T={2} then 2 else if T={0,2} then 1 else if T={1,2} then 1 else if T={0,3} then 1 else if T={1,3} then 3 else if T={2,3} then 3 else 0

  | 27, T => if T=∅ then 10 else if T={0} then 5 else if T={1} then 6 else if T={2} then 6 else if T={3} then 6 else if T={0,1,2,3} then 1 else 0

  | 28, T => if T=∅ then 11 else if T={0} then 5 else if T={1} then 5 else if T={2} then 5 else if T={1,2} then 1 else if T={3} then 6 else if T={0,1,2,3} then 1 else 0

  | 29, T => if T=∅ then 12 else if T={0} then 5 else if T={1} then 4 else if T={2} then 4 else if T={1,2} then 2 else if T={3} then 6 else if T={0,1,2,3} then 1 else 0

  | 30, T => if T=∅ then 12 else if T={0} then 5 else if T={1} then 4 else if T={2} then 5 else if T={1,2} then 1 else if T={3} then 5 else if T={1,3} then 1 else if T={0,1,2,3} then 1 else 0

  | 31, T => if T=∅ then 13 else if T={0} then 5 else if T={1} then 3 else if T={2} then 4 else if T={1,2} then 2 else if T={3} then 5 else if T={1,3} then 1 else if T={0,1,2,3} then 1 else 0

  | 32, T => if T=∅ then 14 else if T={0} then 5 else if T={1} then 2 else if T={2} then 4 else if T={1,2} then 2 else if T={3} then 4 else if T={1,3} then 2 else if T={0,1,2,3} then 1 else 0

  | 33, T => if T=∅ then 14 else if T={0} then 4 else if T={1} then 2 else if T={0,1} then 1 else if T={2} then 4 else if T={1,2} then 2 else if T={3} then 4 else if T={1,3} then 2 else if T={0,2,3} then 1 else 0

  | 34, T => if T=∅ then 15 else if T={0} then 4 else if T={1} then 1 else if T={0,1} then 1 else if T={2} then 3 else if T={1,2} then 3 else if T={3} then 4 else if T={1,3} then 2 else if T={0,2,3} then 1 else 0

  | 35, T => if T=∅ then 16 else if T={0} then 4 else if T={1} then 3 else if T={2} then 3 else if T={0,1,2} then 1 else if T={0,3} then 1 else if T={1,3} then 3 else if T={2,3} then 3 else 0

  | 36, T => if T=∅ then 14 else if T={0} then 4 else if T={1} then 4 else if T={0,1} then 1 else if T={2} then 4 else if T={3} then 4 else if T={0,2,3} then 1 else if T={1,2,3} then 2 else 0

  | 37, T => if T=∅ then 14 else if T={0} then 4 else if T={1} then 3 else if T={0,1} then 1 else if T={2} then 4 else if T={1,2} then 1 else if T={3} then 4 else if T={1,3} then 1 else if T={0,2,3} then 1 else if T={1,2,3} then 1 else 0

  | 38, T => if T=∅ then 15 else if T={0} then 4 else if T={1} then 3 else if T={0,1} then 1 else if T={2} then 3 else if T={1,2} then 1 else if T={3} then 4 else if T={0,2,3} then 1 else if T={1,2,3} then 2 else 0

  | 39, T => if T=∅ then 15 else if T={0} then 4 else if T={1} then 2 else if T={0,1} then 1 else if T={2} then 3 else if T={1,2} then 2 else if T={3} then 4 else if T={1,3} then 1 else if T={0,2,3} then 1 else if T={1,2,3} then 1 else 0

  | 40, T => if T=∅ then 15 else if T={0} then 4 else if T={1} then 3 else if T={0,1} then 1 else if T={2} then 3 else if T={1,2} then 1 else if T={3} then 3 else if T={1,3} then 1 else if T={2,3} then 1 else if T={0,2,3} then 1 else if T={1,2,3} then 1 else 0

  | 41, T => if T=∅ then 15 else if T={0} then 4 else if T={1} then 2 else if T={0,1} then 1 else if T={2} then 3 else if T={1,2} then 2 else if T={3} then 3 else if T={1,3} then 2 else if T={2,3} then 1 else if T={0,2,3} then 1 else 0

  | 42, T => if T=∅ then 16 else if T={0} then 4 else if T={1} then 2 else if T={0,1} then 1 else if T={2} then 2 else if T={1,2} then 2 else if T={3} then 3 else if T={1,3} then 1 else if T={2,3} then 1 else if T={0,2,3} then 1 else if T={1,2,3} then 1 else 0

  | 43, T => if T=∅ then 16 else if T={0} then 4 else if T={1} then 1 else if T={0,1} then 1 else if T={2} then 2 else if T={1,2} then 3 else if T={3} then 3 else if T={1,3} then 2 else if T={2,3} then 1 else if T={0,2,3} then 1 else 0

  | 44, T => if T=∅ then 16 else if T={0} then 4 else if T={1} then 2 else if T={0,1} then 1 else if T={2} then 2 else if T={1,2} then 2 else if T={3} then 2 else if T={1,3} then 2 else if T={2,3} then 2 else if T={0,2,3} then 1 else 0

  | 45, T => if T=∅ then 17 else if T={0} then 4 else if T={1} then 1 else if T={0,1} then 1 else if T={2} then 1 else if T={1,2} then 3 else if T={3} then 2 else if T={1,3} then 2 else if T={2,3} then 2 else if T={0,2,3} then 1 else 0

  | 46, T => if T=∅ then 14 else if T={0} then 3 else if T={1} then 4 else if T={0,1} then 1 else if T={2} then 4 else if T={0,2} then 1 else if T={3} then 4 else if T={0,3} then 1 else if T={1,2,3} then 2 else 0

  | 47, T => if T=∅ then 15 else if T={0} then 3 else if T={1} then 3 else if T={0,1} then 1 else if T={2} then 3 else if T={0,2} then 1 else if T={1,2} then 1 else if T={3} then 4 else if T={0,3} then 1 else if T={1,2,3} then 2 else 0

  | 48, T => if T=∅ then 15 else if T={0} then 3 else if T={1} then 3 else if T={0,1} then 1 else if T={2} then 3 else if T={0,2} then 1 else if T={1,2} then 1 else if T={3} then 3 else if T={0,3} then 1 else if T={1,3} then 1 else if T={2,3} then 1 else if T={1,2,3} then 1 else 0

  | 49, T => if T=∅ then 16 else if T={0} then 3 else if T={1} then 2 else if T={0,1} then 1 else if T={2} then 3 else if T={0,2} then 1 else if T={1,2} then 1 else if T={3} then 3 else if T={0,3} then 1 else if T={1,3} then 1 else if T={1,2,3} then 2 else 0

  | 50, T => if T=∅ then 16 else if T={0} then 3 else if T={1} then 2 else if T={0,1} then 1 else if T={2} then 2 else if T={0,2} then 1 else if T={1,2} then 2 else if T={3} then 3 else if T={0,3} then 1 else if T={1,3} then 1 else if T={2,3} then 1 else if T={1,2,3} then 1 else 0

  | 51, T => if T=∅ then 16 else if T={0} then 3 else if T={1} then 2 else if T={0,1} then 1 else if T={2} then 2 else if T={0,2} then 1 else if T={1,2} then 2 else if T={3} then 2 else if T={0,3} then 1 else if T={1,3} then 2 else if T={2,3} then 2 else 0

  | 52, T => if T=∅ then 17 else if T={0} then 3 else if T={1} then 1 else if T={0,1} then 1 else if T={2} then 2 else if T={0,2} then 1 else if T={1,2} then 2 else if T={3} then 2 else if T={0,3} then 1 else if T={1,3} then 2 else if T={2,3} then 1 else if T={1,2,3} then 1 else 0

  | 53, T => if T=∅ then 17 else if T={0} then 3 else if T={1} then 1 else if T={0,1} then 1 else if T={2} then 1 else if T={0,2} then 1 else if T={1,2} then 3 else if T={3} then 2 else if T={0,3} then 1 else if T={1,3} then 2 else if T={2,3} then 2 else 0

  | 54, T => if T=∅ then 18 else if T={0} then 3 else if T={1} then 1 else if T={0,1} then 1 else if T={2} then 1 else if T={0,2} then 1 else if T={1,2} then 2 else if T={0,3} then 1 else if T={1,3} then 3 else if T={2,3} then 3 else 0

  | 55, T => if T=∅ then 12 else if T={0} then 5 else if T={1} then 5 else if T={2} then 5 else if T={3} then 5 else if T={1,2,3} then 1 else if T={0,1,2,3} then 1 else 0

  | 56, T => if T=∅ then 13 else if T={0} then 5 else if T={1} then 4 else if T={2} then 4 else if T={1,2} then 1 else if T={3} then 5 else if T={1,2,3} then 1 else if T={0,1,2,3} then 1 else 0

  | 57, T => if T=∅ then 13 else if T={0} then 5 else if T={1} then 4 else if T={2} then 4 else if T={1,2} then 1 else if T={3} then 4 else if T={1,3} then 1 else if T={2,3} then 1 else if T={0,1,2,3} then 1 else 0

  | 58, T => if T=∅ then 14 else if T={0} then 5 else if T={1} then 3 else if T={2} then 4 else if T={1,2} then 1 else if T={3} then 4 else if T={1,3} then 1 else if T={1,2,3} then 1 else if T={0,1,2,3} then 1 else 0

  | 59, T => if T=∅ then 14 else if T={0} then 5 else if T={1} then 3 else if T={2} then 3 else if T={1,2} then 2 else if T={3} then 4 else if T={1,3} then 1 else if T={2,3} then 1 else if T={0,1,2,3} then 1 else 0

  | 60, T => if T=∅ then 15 else if T={0} then 5 else if T={1} then 2 else if T={2} then 3 else if T={1,2} then 2 else if T={3} then 3 else if T={1,3} then 2 else if T={2,3} then 1 else if T={0,1,2,3} then 1 else 0

  | 61, T => if T=∅ then 16 else if T={0} then 4 else if T={1} then 1 else if T={0,1} then 1 else if T={2} then 3 else if T={1,2} then 2 else if T={3} then 3 else if T={1,3} then 2 else if T={0,2,3} then 1 else if T={1,2,3} then 1 else 0

  | 62, T => if T=∅ then 17 else if T={0} then 4 else if T={1} then 2 else if T={2} then 2 else if T={1,2} then 1 else if T={0,1,2} then 1 else if T={0,3} then 1 else if T={1,3} then 3 else if T={2,3} then 3 else 0

  | 63, T => if T=∅ then 16 else if T={0} then 4 else if T={1} then 2 else if T={0,1} then 1 else if T={2} then 3 else if T={1,2} then 1 else if T={3} then 3 else if T={1,3} then 1 else if T={0,2,3} then 1 else if T={1,2,3} then 2 else 0

  | 64, T => if T=∅ then 17 else if T={0} then 4 else if T={1} then 1 else if T={0,1} then 1 else if T={2} then 2 else if T={1,2} then 2 else if T={3} then 2 else if T={1,3} then 2 else if T={2,3} then 1 else if T={0,2,3} then 1 else if T={1,2,3} then 1 else 0

  | 65, T => if T=∅ then 18 else if T={0} then 4 else if T={1} then 1 else if T={2} then 1 else if T={1,2} then 2 else if T={0,1,2} then 1 else if T={0,3} then 1 else if T={1,3} then 3 else if T={2,3} then 3 else 0

  | 66, T => if T=∅ then 16 else if T={0} then 3 else if T={1} then 3 else if T={0,1} then 1 else if T={2} then 3 else if T={0,2} then 1 else if T={3} then 3 else if T={0,3} then 1 else if T={1,2,3} then 3 else 0

  | 67, T => if T=∅ then 17 else if T={0} then 3 else if T={1} then 2 else if T={0,1} then 1 else if T={2} then 2 else if T={0,2} then 1 else if T={1,2} then 1 else if T={3} then 2 else if T={0,3} then 1 else if T={1,3} then 1 else if T={2,3} then 1 else if T={1,2,3} then 2 else 0

  | 68, T => if T=∅ then 18 else if T={0} then 3 else if T={1} then 1 else if T={0,1} then 1 else if T={2} then 1 else if T={0,2} then 1 else if T={1,2} then 2 else if T={3} then 1 else if T={0,3} then 1 else if T={1,3} then 2 else if T={2,3} then 2 else if T={1,2,3} then 1 else 0

  | 69, T => if T=∅ then 19 else if T={0} then 3 else if T={0,1} then 1 else if T={0,2} then 1 else if T={1,2} then 3 else if T={0,3} then 1 else if T={1,3} then 3 else if T={2,3} then 3 else 0

  | 70, T => if T=∅ then 14 else if T={0} then 5 else if T={1} then 4 else if T={2} then 4 else if T={3} then 4 else if T={1,2,3} then 2 else if T={0,1,2,3} then 1 else 0

  | 71, T => if T=∅ then 15 else if T={0} then 5 else if T={1} then 3 else if T={2} then 3 else if T={1,2} then 1 else if T={3} then 3 else if T={1,3} then 1 else if T={2,3} then 1 else if T={1,2,3} then 1 else if T={0,1,2,3} then 1 else 0

  | 72, T => if T=∅ then 16 else if T={0} then 5 else if T={1} then 2 else if T={2} then 2 else if T={1,2} then 2 else if T={3} then 2 else if T={1,3} then 2 else if T={2,3} then 2 else if T={0,1,2,3} then 1 else 0

  | _, _ => 0

def entries : Case → List (Finset (Fin 3) × ℕ)

  | 0 => [({0},4),({1},5),({0,1},1),({2},5),({0,2},1),({1,2},1)]

  | 1 => [({0},5),({1},6),({2},6),({0,1,2},1)]

  | 2 => [({0},4),({1},4),({0,1},1),({2},4),({0,2},1),({1,2},2)]

  | 3 => [({0},5),({1},5),({2},5),({1,2},1),({0,1,2},1)]

  | 4 => [({0},4),({1},3),({0,1},1),({2},3),({0,2},1),({1,2},3)]

  | 5 => [({0},5),({1},4),({2},4),({1,2},2),({0,1,2},1)]

def cap : Option (Fin 3) → ℕ
  | none => 7
  | some i => ![1,3,3] i

def permFn : Perm → Fin 4 → Fin 4 := ![![0,1,2,3],![0,1,3,2],![0,2,1,3],![0,2,3,1],![0,3,1,2],![0,3,2,1]]

theorem permFn_injective : ∀ p, Function.Injective (permFn p) := by decide +kernel
noncomputable def perm (p : Perm) : Equiv.Perm (Fin 4) :=
  Equiv.ofBijective (permFn p) ⟨permFn_injective p,Finite.surjective_of_injective (permFn_injective p)⟩
def vector (c : Case) (values : List ℕ) := BoundedAllocations.decode (entries c) values
def code (c : Case) (values : List ℕ) : ℕ := c.val+6*(values.foldl (fun a x => 8*a+x) 0)

theorem perm_preserves_roles : ∀ p i, ((perm p) i).val<1 ↔ i.val<1 := by decide +kernel

def lookup : List (ℕ × (NewCase × Perm)) := [

(54,(0,0)),
(438,(1,3)),
(3078,(0,2)),
(3456,(2,2)),
(3462,(3,3)),
(3840,(4,3)),
(3846,(5,3)),
(4224,(6,3)),
(24624,(2,0)),
(24630,(3,1)),
(25008,(7,0)),
(25014,(8,4)),
(25392,(9,3)),
(27654,(1,1)),
(28032,(7,2)),
(28038,(8,5)),
(28416,(10,3)),
(28422,(11,5)),
(28800,(12,3)),
(49200,(4,1)),
(49206,(5,1)),
(49584,(10,1)),
(49590,(11,4)),
(49968,(13,4)),
(52608,(9,1)),
(52992,(13,5)),
(53376,(14,5)),
(73776,(6,1)),
(74160,(12,1)),
(74544,(14,4)),
(196614,(15,0)),
(196998,(16,3)),
(197382,(17,3)),
(221190,(16,1)),
(221568,(18,0)),
(221574,(19,4)),
(221952,(20,3)),
(221958,(21,5)),
(222336,(22,3)),
(245766,(17,1)),
(246144,(20,1)),
(246150,(21,4)),
(246528,(23,4)),
(246534,(24,4)),
(246912,(25,5)),
(270720,(22,1)),
(271104,(25,4)),
(271488,(26,0)),
(7,(27,0)),
(55,(28,3)),
(103,(29,3)),
(391,(28,1)),
(439,(30,4)),
(487,(31,5)),
(775,(29,1)),
(823,(31,4)),
(871,(32,4)),
(3505,(2,4)),
(3553,(4,5)),
(3601,(6,5)),
(3889,(4,4)),
(3937,(33,4)),
(3985,(34,5)),
(4273,(6,4)),
(4321,(34,4)),
(4369,(35,0)),
(56,(3,0)),
(62,(36,0)),
(440,(8,2)),
(3080,(3,2)),
(3086,(36,2)),
(3458,(4,2)),
(3464,(37,2)),
(3470,(38,3)),
(3842,(33,2)),
(3848,(39,3)),
(4226,(34,3)),
(24626,(4,0)),
(24632,(37,0)),
(24638,(38,1)),
(25010,(10,0)),
(25016,(40,0)),
(25394,(13,2)),
(27656,(8,0)),
(28034,(10,2)),
(28040,(40,2)),
(28418,(41,2)),
(28424,(42,3)),
(28802,(43,3)),
(49202,(33,0)),
(49208,(39,1)),
(49586,(41,0)),
(49592,(42,1)),
(49970,(44,0)),
(52610,(13,0)),
(52994,(44,2)),
(53378,(45,3)),
(73778,(34,1)),
(74162,(43,1)),
(74546,(45,1)),
(196616,(16,0)),
(196622,(46,0)),
(197000,(19,2)),
(197006,(47,3)),
(197384,(21,3)),
(221192,(19,0)),
(221198,(47,1)),
(221570,(20,0)),
(221576,(48,0)),
(221582,(49,4)),
(221954,(23,2)),
(221960,(50,3)),
(222338,(25,3)),
(245768,(21,1)),
(246146,(23,0)),
(246152,(50,1)),
(246530,(51,0)),
(246536,(52,4)),
(246914,(53,3)),
(270722,(25,1)),
(271106,(53,1)),
(271490,(54,0)),
(9,(28,0)),
(57,(55,0)),
(393,(30,2)),
(441,(56,3)),
(777,(31,3)),
(3081,(30,0)),
(3129,(56,1)),
(3465,(57,0)),
(3513,(58,4)),
(3849,(59,3)),
(6153,(31,1)),
(6537,(59,1)),
(6921,(60,4)),
(24627,(0,4)),
(25011,(3,5)),
(25395,(5,5)),
(27699,(3,4)),
(28035,(7,4)),
(28083,(37,4)),
(28419,(10,5)),
(28467,(39,5)),
(28803,(12,5)),
(30771,(5,4)),
(31107,(10,4)),
(31155,(39,4)),
(31491,(41,4)),
(31539,(61,4)),
(31875,(43,5)),
(34179,(12,4)),
(34563,(43,4)),
(34947,(62,0)),
(58,(5,0)),
(64,(38,0)),
(442,(11,2)),
(3082,(5,2)),
(3088,(38,2)),
(3460,(6,2)),
(3466,(39,2)),
(3472,(63,2)),
(3844,(34,2)),
(3850,(61,2)),
(4228,(35,1)),
(24628,(6,0)),
(24634,(39,0)),
(24640,(63,0)),
(25012,(12,0)),
(25018,(42,0)),
(25396,(14,2)),
(27658,(11,0)),
(28036,(12,2)),
(28042,(42,2)),
(28420,(43,2)),
(28426,(64,2)),
(28804,(62,1)),
(49204,(34,0)),
(49210,(61,0)),
(49588,(43,0)),
(49594,(64,0)),
(49972,(45,0)),
(52612,(14,0)),
(52996,(45,2)),
(53380,(65,1)),
(73780,(35,3)),
(74164,(62,3)),
(74548,(65,3)),
(196618,(17,0)),
(196624,(47,0)),
(196630,(66,0)),
(197002,(21,2)),
(197008,(49,2)),
(197386,(24,2)),
(221194,(21,0)),
(221200,(49,0)),
(221572,(22,0)),
(221578,(50,0)),
(221584,(67,0)),
(221956,(25,2)),
(221962,(52,2)),
(222340,(26,1)),
(245770,(24,0)),
(246148,(25,0)),
(246154,(52,0)),
(246532,(53,0)),
(246538,(68,0)),
(246916,(54,1)),
(270724,(26,3)),
(271108,(54,3)),
(271492,(69,0)),
(11,(29,0)),
(59,(56,0)),
(107,(70,0)),
(395,(31,2)),
(443,(58,2)),
(779,(32,2)),
(3083,(31,0)),
(3131,(58,0)),
(3467,(59,0)),
(3515,(71,0)),
(3851,(60,2)),
(6155,(32,0)),
(6539,(60,0)),
(6923,(72,0)),
(24629,(1,0)),
(24677,(36,4)),
(25013,(8,3)),
(25061,(38,5)),
(25397,(11,3)),
(27701,(8,1)),
(27749,(38,4)),
(28037,(9,0)),
(28085,(40,4)),
(28133,(63,4)),
(28421,(13,3)),
(28469,(42,5)),
(28805,(14,3)),
(30773,(11,1)),
(31109,(13,1)),
(31157,(42,4)),
(31493,(44,4)),
(31541,(64,4)),
(31877,(45,5)),
(34181,(14,1)),
(34565,(45,4)),
(34949,(65,0))]

def choose (key : ℕ) : NewCase × Perm := ((lookup.find? (fun r => r.1 == key)).map Prod.snd).getD (0,0)

def newCounts (c : Case) (values : List ℕ) := extend (oneLow c) (vector c values) 7
def positive (c : Case) (values : List ℕ) : Prop :=
  ∀ i : Fin 3, 1≤∑ T : Finset (Fin 3), if i∈T then vector c values T else 0
instance (c : Case) (values : List ℕ) : Decidable (positive c values) := inferInstanceAs (Decidable (∀ i : Fin 3, 1≤∑ T : Finset (Fin 3), if i∈T then vector c values T else 0))
def covered (c : Case) (values : List ℕ) : Prop :=
  positive c values → ∀ T, newCounts c values
    (T.map (perm (choose (code c values)).2).toEmbedding)=μ (choose (code c values)).1 T
noncomputable instance (c : Case) (values : List ℕ) : Decidable (covered c values) := inferInstanceAs (Decidable (positive c values → ∀ T, newCounts c values (T.map (perm (choose (code c values)).2).toEmbedding)=μ (choose (code c values)).1 T))
def catalogue (c : Case) := BoundedAllocations.enumerate cost (entries c) cap

end OneLow

namespace TwoLow
open TwentyThreeFewLowBase (Case twoLow)
abbrev NewCase := Fin 48
abbrev Perm := Fin 4

def μ : NewCase → Finset (Fin 4) → ℕ

  | 0, T => if T=∅ then 13 else if T={0} then 4 else if T={1} then 4 else if T={0,1} then 1 else if T={2} then 5 else if T={3} then 5 else if T={0,2,3} then 1 else if T={1,2,3} then 1 else 0

  | 1, T => if T=∅ then 14 else if T={0} then 4 else if T={1} then 4 else if T={0,1} then 1 else if T={2} then 4 else if T={3} then 4 else if T={2,3} then 1 else if T={0,2,3} then 1 else if T={1,2,3} then 1 else 0

  | 2, T => if T=∅ then 13 else if T={0} then 4 else if T={1} then 4 else if T={2} then 4 else if T={0,2} then 1 else if T={1,2} then 1 else if T={3} then 5 else if T={0,1,3} then 1 else if T={2,3} then 1 else 0

  | 3, T => if T=∅ then 14 else if T={0} then 4 else if T={1} then 4 else if T={2} then 3 else if T={0,2} then 1 else if T={1,2} then 1 else if T={3} then 4 else if T={0,1,3} then 1 else if T={2,3} then 2 else 0

  | 4, T => if T=∅ then 15 else if T={0} then 4 else if T={1} then 4 else if T={2} then 2 else if T={0,2} then 1 else if T={1,2} then 1 else if T={3} then 3 else if T={0,1,3} then 1 else if T={2,3} then 3 else 0

  | 5, T => if T=∅ then 13 else if T={0} then 3 else if T={1} then 4 else if T={0,1} then 1 else if T={2} then 5 else if T={0,2} then 1 else if T={3} then 5 else if T={0,3} then 1 else if T={1,2,3} then 1 else 0

  | 6, T => if T=∅ then 14 else if T={0} then 3 else if T={1} then 4 else if T={0,1} then 1 else if T={2} then 4 else if T={0,2} then 1 else if T={3} then 4 else if T={0,3} then 1 else if T={2,3} then 1 else if T={1,2,3} then 1 else 0

  | 7, T => if T=∅ then 15 else if T={0} then 3 else if T={1} then 4 else if T={0,1} then 1 else if T={2} then 3 else if T={0,2} then 1 else if T={3} then 3 else if T={0,3} then 1 else if T={2,3} then 2 else if T={1,2,3} then 1 else 0

  | 8, T => if T=∅ then 14 else if T={0} then 3 else if T={1} then 3 else if T={0,1} then 1 else if T={2} then 4 else if T={0,2} then 1 else if T={1,2} then 1 else if T={3} then 4 else if T={0,3} then 1 else if T={1,3} then 1 else if T={2,3} then 1 else 0

  | 9, T => if T=∅ then 15 else if T={0} then 3 else if T={1} then 3 else if T={0,1} then 1 else if T={2} then 3 else if T={0,2} then 1 else if T={1,2} then 1 else if T={3} then 3 else if T={0,3} then 1 else if T={1,3} then 1 else if T={2,3} then 2 else 0

  | 10, T => if T=∅ then 16 else if T={0} then 3 else if T={1} then 3 else if T={0,1} then 1 else if T={2} then 2 else if T={0,2} then 1 else if T={1,2} then 1 else if T={3} then 2 else if T={0,3} then 1 else if T={1,3} then 1 else if T={2,3} then 3 else 0

  | 11, T => if T=∅ then 11 else if T={0} then 5 else if T={1} then 5 else if T={2} then 6 else if T={3} then 6 else if T={0,1,2,3} then 1 else 0

  | 12, T => if T=∅ then 12 else if T={0} then 5 else if T={1} then 5 else if T={2} then 5 else if T={3} then 5 else if T={2,3} then 1 else if T={0,1,2,3} then 1 else 0

  | 13, T => if T=∅ then 13 else if T={0} then 5 else if T={1} then 5 else if T={2} then 4 else if T={3} then 4 else if T={2,3} then 2 else if T={0,1,2,3} then 1 else 0

  | 14, T => if T=∅ then 14 else if T={0} then 3 else if T={1} then 3 else if T={0,1} then 2 else if T={2} then 5 else if T={3} then 5 else if T={0,2,3} then 1 else if T={1,2,3} then 1 else 0

  | 15, T => if T=∅ then 15 else if T={0} then 3 else if T={1} then 3 else if T={0,1} then 2 else if T={2} then 4 else if T={3} then 4 else if T={2,3} then 1 else if T={0,2,3} then 1 else if T={1,2,3} then 1 else 0

  | 16, T => if T=∅ then 14 else if T={0} then 3 else if T={1} then 3 else if T={0,1} then 1 else if T={2} then 4 else if T={0,2} then 1 else if T={1,2} then 1 else if T={3} then 5 else if T={0,1,3} then 1 else if T={2,3} then 1 else 0

  | 17, T => if T=∅ then 15 else if T={0} then 3 else if T={1} then 3 else if T={0,1} then 1 else if T={2} then 3 else if T={0,2} then 1 else if T={1,2} then 1 else if T={3} then 4 else if T={0,1,3} then 1 else if T={2,3} then 2 else 0

  | 18, T => if T=∅ then 16 else if T={0} then 3 else if T={1} then 3 else if T={0,1} then 1 else if T={2} then 2 else if T={0,2} then 1 else if T={1,2} then 1 else if T={3} then 3 else if T={0,1,3} then 1 else if T={2,3} then 3 else 0

  | 19, T => if T=∅ then 14 else if T={0} then 2 else if T={1} then 3 else if T={0,1} then 2 else if T={2} then 5 else if T={0,2} then 1 else if T={3} then 5 else if T={0,3} then 1 else if T={1,2,3} then 1 else 0

  | 20, T => if T=∅ then 15 else if T={0} then 2 else if T={1} then 3 else if T={0,1} then 2 else if T={2} then 4 else if T={0,2} then 1 else if T={3} then 4 else if T={0,3} then 1 else if T={2,3} then 1 else if T={1,2,3} then 1 else 0

  | 21, T => if T=∅ then 16 else if T={0} then 2 else if T={1} then 3 else if T={0,1} then 2 else if T={2} then 3 else if T={0,2} then 1 else if T={3} then 3 else if T={0,3} then 1 else if T={2,3} then 2 else if T={1,2,3} then 1 else 0

  | 22, T => if T=∅ then 15 else if T={0} then 2 else if T={1} then 2 else if T={0,1} then 2 else if T={2} then 4 else if T={0,2} then 1 else if T={1,2} then 1 else if T={3} then 4 else if T={0,3} then 1 else if T={1,3} then 1 else if T={2,3} then 1 else 0

  | 23, T => if T=∅ then 16 else if T={0} then 2 else if T={1} then 2 else if T={0,1} then 2 else if T={2} then 3 else if T={0,2} then 1 else if T={1,2} then 1 else if T={3} then 3 else if T={0,3} then 1 else if T={1,3} then 1 else if T={2,3} then 2 else 0

  | 24, T => if T=∅ then 17 else if T={0} then 2 else if T={1} then 2 else if T={0,1} then 2 else if T={2} then 2 else if T={0,2} then 1 else if T={1,2} then 1 else if T={3} then 2 else if T={0,3} then 1 else if T={1,3} then 1 else if T={2,3} then 3 else 0

  | 25, T => if T=∅ then 12 else if T={0} then 4 else if T={1} then 4 else if T={0,1} then 1 else if T={2} then 6 else if T={3} then 6 else if T={0,1,2,3} then 1 else 0

  | 26, T => if T=∅ then 13 else if T={0} then 4 else if T={1} then 4 else if T={0,1} then 1 else if T={2} then 5 else if T={3} then 5 else if T={2,3} then 1 else if T={0,1,2,3} then 1 else 0

  | 27, T => if T=∅ then 14 else if T={0} then 4 else if T={1} then 4 else if T={0,1} then 1 else if T={2} then 4 else if T={3} then 4 else if T={2,3} then 2 else if T={0,1,2,3} then 1 else 0

  | 28, T => if T=∅ then 13 else if T={0} then 4 else if T={1} then 4 else if T={2} then 5 else if T={0,1,2} then 1 else if T={3} then 5 else if T={0,1,3} then 1 else if T={2,3} then 1 else 0

  | 29, T => if T=∅ then 14 else if T={0} then 4 else if T={1} then 4 else if T={2} then 4 else if T={0,1,2} then 1 else if T={3} then 4 else if T={0,1,3} then 1 else if T={2,3} then 2 else 0

  | 30, T => if T=∅ then 15 else if T={0} then 4 else if T={1} then 4 else if T={2} then 3 else if T={0,1,2} then 1 else if T={3} then 3 else if T={0,1,3} then 1 else if T={2,3} then 3 else 0

  | 31, T => if T=∅ then 15 else if T={0} then 2 else if T={1} then 2 else if T={0,1} then 3 else if T={2} then 5 else if T={3} then 5 else if T={0,2,3} then 1 else if T={1,2,3} then 1 else 0

  | 32, T => if T=∅ then 16 else if T={0} then 2 else if T={1} then 2 else if T={0,1} then 3 else if T={2} then 4 else if T={3} then 4 else if T={2,3} then 1 else if T={0,2,3} then 1 else if T={1,2,3} then 1 else 0

  | 33, T => if T=∅ then 15 else if T={0} then 2 else if T={1} then 2 else if T={0,1} then 2 else if T={2} then 4 else if T={0,2} then 1 else if T={1,2} then 1 else if T={3} then 5 else if T={0,1,3} then 1 else if T={2,3} then 1 else 0

  | 34, T => if T=∅ then 16 else if T={0} then 2 else if T={1} then 2 else if T={0,1} then 2 else if T={2} then 3 else if T={0,2} then 1 else if T={1,2} then 1 else if T={3} then 4 else if T={0,1,3} then 1 else if T={2,3} then 2 else 0

  | 35, T => if T=∅ then 17 else if T={0} then 2 else if T={1} then 2 else if T={0,1} then 2 else if T={2} then 2 else if T={0,2} then 1 else if T={1,2} then 1 else if T={3} then 3 else if T={0,1,3} then 1 else if T={2,3} then 3 else 0

  | 36, T => if T=∅ then 15 else if T={0} then 1 else if T={1} then 2 else if T={0,1} then 3 else if T={2} then 5 else if T={0,2} then 1 else if T={3} then 5 else if T={0,3} then 1 else if T={1,2,3} then 1 else 0

  | 37, T => if T=∅ then 16 else if T={0} then 1 else if T={1} then 2 else if T={0,1} then 3 else if T={2} then 4 else if T={0,2} then 1 else if T={3} then 4 else if T={0,3} then 1 else if T={2,3} then 1 else if T={1,2,3} then 1 else 0

  | 38, T => if T=∅ then 17 else if T={0} then 1 else if T={1} then 2 else if T={0,1} then 3 else if T={2} then 3 else if T={0,2} then 1 else if T={3} then 3 else if T={0,3} then 1 else if T={2,3} then 2 else if T={1,2,3} then 1 else 0

  | 39, T => if T=∅ then 16 else if T={0} then 1 else if T={1} then 1 else if T={0,1} then 3 else if T={2} then 4 else if T={0,2} then 1 else if T={1,2} then 1 else if T={3} then 4 else if T={0,3} then 1 else if T={1,3} then 1 else if T={2,3} then 1 else 0

  | 40, T => if T=∅ then 17 else if T={0} then 1 else if T={1} then 1 else if T={0,1} then 3 else if T={2} then 3 else if T={0,2} then 1 else if T={1,2} then 1 else if T={3} then 3 else if T={0,3} then 1 else if T={1,3} then 1 else if T={2,3} then 2 else 0

  | 41, T => if T=∅ then 18 else if T={0} then 1 else if T={1} then 1 else if T={0,1} then 3 else if T={2} then 2 else if T={0,2} then 1 else if T={1,2} then 1 else if T={3} then 2 else if T={0,3} then 1 else if T={1,3} then 1 else if T={2,3} then 3 else 0

  | 42, T => if T=∅ then 13 else if T={0} then 3 else if T={1} then 3 else if T={0,1} then 2 else if T={2} then 6 else if T={3} then 6 else if T={0,1,2,3} then 1 else 0

  | 43, T => if T=∅ then 14 else if T={0} then 3 else if T={1} then 3 else if T={0,1} then 2 else if T={2} then 5 else if T={3} then 5 else if T={2,3} then 1 else if T={0,1,2,3} then 1 else 0

  | 44, T => if T=∅ then 15 else if T={0} then 3 else if T={1} then 3 else if T={0,1} then 2 else if T={2} then 4 else if T={3} then 4 else if T={2,3} then 2 else if T={0,1,2,3} then 1 else 0

  | 45, T => if T=∅ then 14 else if T={0} then 3 else if T={1} then 3 else if T={0,1} then 1 else if T={2} then 5 else if T={0,1,2} then 1 else if T={3} then 5 else if T={0,1,3} then 1 else if T={2,3} then 1 else 0

  | 46, T => if T=∅ then 15 else if T={0} then 3 else if T={1} then 3 else if T={0,1} then 1 else if T={2} then 4 else if T={0,1,2} then 1 else if T={3} then 4 else if T={0,1,3} then 1 else if T={2,3} then 2 else 0

  | 47, T => if T=∅ then 16 else if T={0} then 3 else if T={1} then 3 else if T={0,1} then 1 else if T={2} then 3 else if T={0,1,2} then 1 else if T={3} then 3 else if T={0,1,3} then 1 else if T={2,3} then 3 else 0

  | _, _ => 0

def entries : Case → List (Finset (Fin 3) × ℕ)

  | 0 => [({0},4),({1},4),({0,1},1),({2},5),({0,2},1),({1,2},1)]

  | 1 => [({0},5),({1},5),({2},6),({0,1,2},1)]

  | 2 => [({0},3),({1},3),({0,1},2),({2},5),({0,2},1),({1,2},1)]

  | 3 => [({0},4),({1},4),({0,1},1),({2},6),({0,1,2},1)]

  | 4 => [({0},2),({1},2),({0,1},3),({2},5),({0,2},1),({1,2},1)]

  | 5 => [({0},3),({1},3),({0,1},2),({2},6),({0,1,2},1)]

def cap : Option (Fin 3) → ℕ
  | none => 7
  | some i => ![1,1,3] i

def permFn : Perm → Fin 4 → Fin 4 := ![![0,1,2,3],![0,1,3,2],![1,0,2,3],![1,0,3,2]]

theorem permFn_injective : ∀ p, Function.Injective (permFn p) := by decide +kernel
noncomputable def perm (p : Perm) : Equiv.Perm (Fin 4) :=
  Equiv.ofBijective (permFn p) ⟨permFn_injective p,Finite.surjective_of_injective (permFn_injective p)⟩
def vector (c : Case) (values : List ℕ) := BoundedAllocations.decode (entries c) values
def code (c : Case) (values : List ℕ) : ℕ := c.val+6*(values.foldl (fun a x => 8*a+x) 0)

theorem perm_preserves_roles : ∀ p i, ((perm p) i).val<2 ↔ i.val<2 := by decide +kernel

def lookup : List (ℕ × (NewCase × Perm)) := [

(54,(0,0)),
(438,(1,0)),
(3456,(2,0)),
(3840,(3,0)),
(4224,(4,0)),
(24624,(5,2)),
(25008,(6,2)),
(25392,(7,2)),
(196614,(5,0)),
(196998,(6,0)),
(197382,(7,0)),
(221568,(8,0)),
(221952,(9,0)),
(222336,(10,0)),
(7,(11,0)),
(55,(12,0)),
(103,(13,0)),
(3505,(2,1)),
(3553,(3,1)),
(3601,(4,1)),
(56,(14,0)),
(440,(15,0)),
(3458,(16,0)),
(3842,(17,0)),
(4226,(18,0)),
(24626,(19,2)),
(25010,(20,2)),
(25394,(21,2)),
(196616,(19,0)),
(197000,(20,0)),
(197384,(21,0)),
(221570,(22,0)),
(221954,(23,0)),
(222338,(24,0)),
(9,(25,0)),
(57,(26,0)),
(105,(27,0)),
(435,(28,0)),
(483,(29,0)),
(531,(30,0)),
(27699,(16,1)),
(27747,(17,1)),
(27795,(18,1)),
(58,(31,0)),
(442,(32,0)),
(3460,(33,0)),
(3844,(34,0)),
(4228,(35,0)),
(24628,(36,2)),
(25012,(37,2)),
(25396,(38,2)),
(196618,(36,0)),
(197002,(37,0)),
(197386,(38,0)),
(221572,(39,0)),
(221956,(40,0)),
(222340,(41,0)),
(11,(42,0)),
(59,(43,0)),
(107,(44,0)),
(437,(45,0)),
(485,(46,0)),
(533,(47,0)),
(27701,(33,1)),
(27749,(34,1)),
(27797,(35,1))]

def choose (key : ℕ) : NewCase × Perm := ((lookup.find? (fun r => r.1 == key)).map Prod.snd).getD (0,0)

def newCounts (c : Case) (values : List ℕ) := extend (twoLow c) (vector c values) 7
def positive (c : Case) (values : List ℕ) : Prop :=
  ∀ i : Fin 3, 1≤∑ T : Finset (Fin 3), if i∈T then vector c values T else 0
instance (c : Case) (values : List ℕ) : Decidable (positive c values) := inferInstanceAs (Decidable (∀ i : Fin 3, 1≤∑ T : Finset (Fin 3), if i∈T then vector c values T else 0))
def covered (c : Case) (values : List ℕ) : Prop :=
  positive c values → ∀ T, newCounts c values
    (T.map (perm (choose (code c values)).2).toEmbedding)=μ (choose (code c values)).1 T
noncomputable instance (c : Case) (values : List ℕ) : Decidable (covered c values) := inferInstanceAs (Decidable (positive c values → ∀ T, newCounts c values (T.map (perm (choose (code c values)).2).toEmbedding)=μ (choose (code c values)).1 T))
def catalogue (c : Case) := BoundedAllocations.enumerate cost (entries c) cap

end TwoLow
end Aris4Math.ThirtyFour.TwentyThreeFewLowFourCoverage
