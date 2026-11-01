import Aris4Math.ThirtyFour.LockRelabel
import Aris4Math.ThirtyFour.TwentyThreeFourLowCatalog
import Aris4Math.ThirtyFour.TwentyThreeFourLowStrict
import Aris4Math.ThirtyFour.TwentyThreeFourLowJoint3
import Aris4Math.ThirtyFour.TwentyThreeFourLowJoint19
import Aris4Math.ThirtyFour.TwentyThreeFourLowJoint20
import Aris4Math.ThirtyFour.TwentyThreeFourLowJoint21

namespace Aris4Math.ThirtyFour.TwentyThreeFourLowClassified
open Aris4Math.ThirtyThree.MultiLockRecovery (count)
open Aris4Math.ThirtyThree.TwentyThreeFourLowCatalog (permutation)
set_option maxRecDepth 100000
set_option maxHeartbeats 0
def sourceCounts : Fin 50 → Finset (Fin 4) → ℕ := ![(fun T => if T=∅ then 16 else if T={0} then 3 else if T={1} then 3 else if T={0,1} then 1 else if T={2} then 3 else if T={0,2} then 1 else if T={1,2} then 1 else if T={3} then 3 else if T={0,3} then 1 else if T={1,3} then 1 else if T={2,3} then 1 else 0),(fun T => if T=∅ then 15 else if T={0} then 3 else if T={1} then 4 else if T={0,1} then 1 else if T={2} then 4 else if T={0,2} then 1 else if T={3} then 4 else if T={0,3} then 1 else if T={1,2,3} then 1 else 0),(fun T => if T=∅ then 13 else if T={0} then 5 else if T={1} then 5 else if T={2} then 5 else if T={3} then 5 else if T={0,1,2,3} then 1 else 0),(fun T => if T=∅ then 17 else if T={0} then 2 else if T={1} then 2 else if T={0,1} then 2 else if T={2} then 3 else if T={0,2} then 1 else if T={1,2} then 1 else if T={3} then 3 else if T={0,3} then 1 else if T={1,3} then 1 else if T={2,3} then 1 else 0),(fun T => if T=∅ then 16 else if T={0} then 3 else if T={1} then 3 else if T={0,1} then 1 else if T={2} then 3 else if T={0,2} then 1 else if T={1,2} then 1 else if T={3} then 4 else if T={0,3} then 1 else if T={1,2,3} then 1 else 0),(fun T => if T=∅ then 15 else if T={0} then 4 else if T={1} then 4 else if T={0,1} then 1 else if T={2} then 4 else if T={3} then 4 else if T={0,2,3} then 1 else if T={1,2,3} then 1 else 0),(fun T => if T=∅ then 16 else if T={0} then 2 else if T={1} then 3 else if T={0,1} then 2 else if T={2} then 4 else if T={0,2} then 1 else if T={3} then 4 else if T={0,3} then 1 else if T={1,2,3} then 1 else 0),(fun T => if T=∅ then 14 else if T={0} then 4 else if T={1} then 4 else if T={0,1} then 1 else if T={2} then 5 else if T={3} then 5 else if T={0,1,2,3} then 1 else 0),(fun T => if T=∅ then 18 else if T={0} then 1 else if T={1} then 1 else if T={0,1} then 3 else if T={2} then 3 else if T={0,2} then 1 else if T={1,2} then 1 else if T={3} then 3 else if T={0,3} then 1 else if T={1,3} then 1 else if T={2,3} then 1 else 0),(fun T => if T=∅ then 17 else if T={0} then 2 else if T={1} then 2 else if T={0,1} then 2 else if T={2} then 3 else if T={0,2} then 1 else if T={1,2} then 1 else if T={3} then 4 else if T={0,1,3} then 1 else if T={2,3} then 1 else 0),(fun T => if T=∅ then 16 else if T={0} then 3 else if T={1} then 3 else if T={0,1} then 1 else if T={2} then 4 else if T={0,1,2} then 1 else if T={3} then 4 else if T={0,1,3} then 1 else if T={2,3} then 1 else 0),(fun T => if T=∅ then 17 else if T={0} then 1 else if T={1} then 2 else if T={0,1} then 3 else if T={2} then 4 else if T={0,2} then 1 else if T={3} then 4 else if T={0,3} then 1 else if T={1,2,3} then 1 else 0),(fun T => if T=∅ then 15 else if T={0} then 3 else if T={1} then 3 else if T={0,1} then 2 else if T={2} then 5 else if T={3} then 5 else if T={0,1,2,3} then 1 else 0),(fun T => if T=∅ then 18 else if T={0} then 1 else if T={1} then 2 else if T={0,1} then 2 else if T={2} then 2 else if T={0,2} then 2 else if T={1,2} then 1 else if T={3} then 3 else if T={0,3} then 1 else if T={1,3} then 1 else if T={2,3} then 1 else 0),(fun T => if T=∅ then 17 else if T={0} then 2 else if T={1} then 3 else if T={0,1} then 1 else if T={2} then 3 else if T={0,2} then 1 else if T={1,2} then 1 else if T={3} then 3 else if T={0,3} then 1 else if T={1,3} then 1 else if T={0,2,3} then 1 else 0),(fun T => if T=∅ then 17 else if T={0} then 2 else if T={1} then 2 else if T={0,1} then 2 else if T={2} then 3 else if T={0,2} then 1 else if T={1,2} then 1 else if T={3} then 4 else if T={0,3} then 1 else if T={1,2,3} then 1 else 0),(fun T => if T=∅ then 16 else if T={0} then 3 else if T={1} then 3 else if T={0,1} then 1 else if T={2} then 4 else if T={0,2} then 1 else if T={3} then 4 else if T={0,1,3} then 1 else if T={1,2,3} then 1 else 0),(fun T => if T=∅ then 17 else if T={0} then 1 else if T={1} then 3 else if T={0,1} then 2 else if T={2} then 3 else if T={0,2} then 2 else if T={3} then 4 else if T={0,3} then 1 else if T={1,2,3} then 1 else 0),(fun T => if T=∅ then 15 else if T={0} then 3 else if T={1} then 4 else if T={0,1} then 1 else if T={2} then 4 else if T={0,2} then 1 else if T={3} then 5 else if T={0,1,2,3} then 1 else 0),(fun T => if T=∅ then 19 else if T={0} then 1 else if T={1} then 1 else if T={0,1} then 2 else if T={2} then 1 else if T={0,2} then 2 else if T={1,2} then 2 else if T={3} then 3 else if T={0,3} then 1 else if T={1,3} then 1 else if T={2,3} then 1 else 0),(fun T => if T=∅ then 18 else if T={0} then 2 else if T={1} then 2 else if T={0,1} then 1 else if T={2} then 2 else if T={0,2} then 1 else if T={1,2} then 1 else if T={0,1,2} then 1 else if T={3} then 3 else if T={0,3} then 1 else if T={1,3} then 1 else if T={2,3} then 1 else 0),(fun T => if T=∅ then 17 else if T={0} then 3 else if T={1} then 3 else if T={0,1} then 1 else if T={2} then 3 else if T={0,2} then 1 else if T={3} then 3 else if T={0,3} then 1 else if T={1,2,3} then 2 else 0),(fun T => if T=∅ then 18 else if T={0} then 1 else if T={1} then 2 else if T={0,1} then 2 else if T={2} then 2 else if T={0,2} then 2 else if T={1,2} then 1 else if T={3} then 4 else if T={0,3} then 1 else if T={1,2,3} then 1 else 0),(fun T => if T=∅ then 17 else if T={0} then 2 else if T={1} then 3 else if T={0,1} then 1 else if T={2} then 3 else if T={0,2} then 1 else if T={0,1,2} then 1 else if T={3} then 4 else if T={0,3} then 1 else if T={1,2,3} then 1 else 0),(fun T => if T=∅ then 16 else if T={0} then 3 else if T={1} then 3 else if T={0,1} then 1 else if T={2} then 3 else if T={0,2} then 1 else if T={1,2} then 1 else if T={3} then 5 else if T={0,1,2,3} then 1 else 0),(fun T => if T=∅ then 15 else if T={0} then 4 else if T={1} then 4 else if T={2} then 4 else if T={0,1,2} then 1 else if T={3} then 5 else if T={0,1,2,3} then 1 else 0),(fun T => if T=∅ then 18 else if T={0} then 2 else if T={1} then 2 else if T={0,1} then 1 else if T={2} then 2 else if T={0,2} then 1 else if T={1,2} then 2 else if T={3} then 2 else if T={0,3} then 2 else if T={1,3} then 1 else if T={2,3} then 1 else 0),(fun T => if T=∅ then 17 else if T={0} then 2 else if T={1} then 3 else if T={0,1} then 1 else if T={2} then 3 else if T={0,2} then 1 else if T={1,2} then 1 else if T={3} then 3 else if T={0,3} then 2 else if T={1,2,3} then 1 else 0),(fun T => if T=∅ then 16 else if T={0} then 3 else if T={1} then 3 else if T={0,1} then 2 else if T={2} then 4 else if T={3} then 4 else if T={0,2,3} then 1 else if T={1,2,3} then 1 else 0),(fun T => if T=∅ then 15 else if T={0} then 4 else if T={1} then 4 else if T={0,1} then 1 else if T={2} then 4 else if T={3} then 4 else if T={2,3} then 1 else if T={0,1,2,3} then 1 else 0),(fun T => if T=∅ then 19 else if T={0} then 1 else if T={1} then 1 else if T={0,1} then 2 else if T={2} then 2 else if T={0,2} then 1 else if T={1,2} then 2 else if T={3} then 2 else if T={0,3} then 2 else if T={1,3} then 1 else if T={2,3} then 1 else 0),(fun T => if T=∅ then 18 else if T={0} then 2 else if T={1} then 2 else if T={0,1} then 1 else if T={2} then 2 else if T={0,2} then 1 else if T={1,2} then 2 else if T={3} then 3 else if T={0,3} then 1 else if T={1,3} then 1 else if T={0,2,3} then 1 else 0),(fun T => if T=∅ then 17 else if T={0} then 3 else if T={1} then 3 else if T={0,1} then 1 else if T={2} then 3 else if T={0,2} then 1 else if T={3} then 3 else if T={1,3} then 1 else if T={0,2,3} then 1 else if T={1,2,3} then 1 else 0),(fun T => if T=∅ then 18 else if T={0} then 1 else if T={1} then 2 else if T={0,1} then 2 else if T={2} then 3 else if T={0,2} then 1 else if T={1,2} then 1 else if T={3} then 3 else if T={0,3} then 2 else if T={1,2,3} then 1 else 0),(fun T => if T=∅ then 17 else if T={0} then 2 else if T={1} then 3 else if T={0,1} then 1 else if T={2} then 3 else if T={0,2} then 2 else if T={3} then 4 else if T={0,1,3} then 1 else if T={1,2,3} then 1 else 0),(fun T => if T=∅ then 16 else if T={0} then 3 else if T={1} then 3 else if T={0,1} then 1 else if T={2} then 4 else if T={0,2} then 1 else if T={3} then 4 else if T={1,3} then 1 else if T={0,1,2,3} then 1 else 0),(fun T => if T=∅ then 19 else if T={0} then 1 else if T={1} then 1 else if T={0,1} then 3 else if T={2} then 2 else if T={0,2} then 1 else if T={1,2} then 1 else if T={3} then 2 else if T={0,3} then 1 else if T={1,3} then 1 else if T={2,3} then 2 else 0),(fun T => if T=∅ then 18 else if T={0} then 2 else if T={1} then 2 else if T={0,1} then 1 else if T={2} then 2 else if T={0,2} then 1 else if T={1,2} then 2 else if T={3} then 3 else if T={0,3} then 2 else if T={1,2,3} then 1 else 0),(fun T => if T=∅ then 18 else if T={0} then 1 else if T={1} then 2 else if T={0,1} then 3 else if T={2} then 3 else if T={0,2} then 1 else if T={3} then 3 else if T={0,3} then 1 else if T={2,3} then 1 else if T={1,2,3} then 1 else 0),(fun T => if T=∅ then 17 else if T={0} then 2 else if T={1} then 2 else if T={0,1} then 3 else if T={2} then 4 else if T={3} then 4 else if T={0,2,3} then 1 else if T={1,2,3} then 1 else 0),(fun T => if T=∅ then 17 else if T={0} then 3 else if T={1} then 3 else if T={0,1} then 1 else if T={2} then 3 else if T={0,1,2} then 1 else if T={3} then 3 else if T={0,1,3} then 1 else if T={2,3} then 2 else 0),(fun T => if T=∅ then 16 else if T={0} then 3 else if T={1} then 3 else if T={0,1} then 2 else if T={2} then 4 else if T={3} then 4 else if T={2,3} then 1 else if T={0,1,2,3} then 1 else 0),(fun T => if T=∅ then 20 else if T={0} then 1 else if T={1} then 1 else if T={0,1} then 1 else if T={2} then 1 else if T={0,2} then 1 else if T={1,2} then 3 else if T={3} then 1 else if T={0,3} then 3 else if T={1,3} then 1 else if T={2,3} then 1 else 0),(fun T => if T=∅ then 19 else if T={0} then 1 else if T={1} then 2 else if T={0,1} then 1 else if T={2} then 2 else if T={0,2} then 1 else if T={1,2} then 2 else if T={3} then 2 else if T={0,3} then 3 else if T={1,2,3} then 1 else 0),(fun T => if T=∅ then 18 else if T={0} then 2 else if T={1} then 2 else if T={0,1} then 3 else if T={2} then 3 else if T={3} then 3 else if T={2,3} then 1 else if T={0,2,3} then 1 else if T={1,2,3} then 1 else 0),(fun T => if T=∅ then 17 else if T={0} then 3 else if T={1} then 3 else if T={0,1} then 2 else if T={2} then 3 else if T={3} then 3 else if T={2,3} then 2 else if T={0,1,2,3} then 1 else 0),(fun T => if T=∅ then 20 else if T={0} then 1 else if T={1} then 1 else if T={0,1} then 1 else if T={2} then 1 else if T={0,2} then 2 else if T={1,2} then 2 else if T={3} then 1 else if T={0,3} then 2 else if T={1,3} then 2 else if T={2,3} then 1 else 0),(fun T => if T=∅ then 19 else if T={0} then 1 else if T={1} then 2 else if T={0,1} then 1 else if T={2} then 2 else if T={0,2} then 2 else if T={1,2} then 1 else if T={3} then 2 else if T={0,3} then 2 else if T={1,3} then 1 else if T={1,2,3} then 1 else 0),(fun T => if T=∅ then 18 else if T={0} then 2 else if T={1} then 2 else if T={0,1} then 2 else if T={2} then 3 else if T={0,2} then 1 else if T={3} then 3 else if T={1,3} then 1 else if T={0,2,3} then 1 else if T={1,2,3} then 1 else 0),(fun T => if T=∅ then 17 else if T={0} then 3 else if T={1} then 3 else if T={0,1} then 1 else if T={2} then 3 else if T={0,2} then 1 else if T={3} then 3 else if T={1,3} then 1 else if T={2,3} then 1 else if T={0,1,2,3} then 1 else 0)]
def oldToSource : Fin 50 → Fin 50 × Fin 24 := ![(0,0),(2,0),(1,0),(3,16),(7,16),(4,3),(5,0),(6,16),(8,16),(12,16),(9,16),(10,16),(11,16),(13,21),(18,21),(14,18),(15,11),(16,10),(17,21),(19,9),(24,9),(20,9),(25,9),(21,0),(22,9),(23,9),(26,0),(29,4),(27,0),(28,8),(30,16),(35,17),(31,13),(32,1),(33,16),(34,17),(36,8),(41,8),(37,0),(38,8),(39,8),(40,8),(42,0),(45,4),(43,0),(44,8),(46,0),(49,3),(47,0),(48,3)]
theorem old_binding : ∀ k T,
    TwentyThreeFourLowCatalog.counts k (T.image (permutation (oldToSource k).2)) =
      sourceCounts (oldToSource k).1 T := by decide +kernel
abbrev Residue := Fin 8
def residualSource : Residue → Fin 50 := ![0,1,2,4,5,26,27,29]
def residualCounts (r : Residue) : Finset (Fin 4) → ℕ := sourceCounts (residualSource r)
def pureSource : TwentyThreeFourLowStrictData.Case → Fin 50 := ![6,7,8,9,10,11,12,13,14,15,16,17,18,22,23,24,25,28,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49]
theorem pure_binding : ∀ i T, sourceCounts (pureSource i) T =
    TwentyThreeFourLowStrictData.μ i T := by decide +kernel
theorem joint_binding3 : ∀ T, sourceCounts 3 T =
    TwentyThreeFourLowJoint3Data.μ T := by decide +kernel
theorem joint_binding19 : ∀ T, sourceCounts 19 T =
    TwentyThreeFourLowJoint19Data.μ T := by decide +kernel
theorem joint_binding20 : ∀ T, sourceCounts 20 T =
    TwentyThreeFourLowJoint20Data.μ T := by decide +kernel
theorem joint_binding21 : ∀ T, sourceCounts 21 T =
    TwentyThreeFourLowJoint21Data.μ T := by decide +kernel

/-- All 50 actual types are split into 42 strict types and precisely eight residues. -/
theorem residual_of_noB (H : Simple5Hypergraph (Fin 23)) (f : Fin 4 ↪ Fin 23)
    (q : Fin 50) (notB : ¬ PropertyB H)
    (actual : ∀ T, count H f T=sourceCounts q T) :
    ∃ r : Residue, ∀ T, count H f T=residualCounts r T := by
  fin_cases q
  · exact ⟨0, actual⟩
  · exact ⟨1, actual⟩
  · exact ⟨2, actual⟩
  · exact (notB (TwentyThreeFourLowJoint3.propertyB_of_counts H f
      (fun T => (actual T).trans (joint_binding3 T)))).elim
  · exact ⟨3, actual⟩
  · exact ⟨4, actual⟩
  · exact (notB (TwentyThreeFourLowStrict.propertyB_of_counts H f 0
      (fun T => (actual T).trans (pure_binding 0 T)))).elim
  · exact (notB (TwentyThreeFourLowStrict.propertyB_of_counts H f 1
      (fun T => (actual T).trans (pure_binding 1 T)))).elim
  · exact (notB (TwentyThreeFourLowStrict.propertyB_of_counts H f 2
      (fun T => (actual T).trans (pure_binding 2 T)))).elim
  · exact (notB (TwentyThreeFourLowStrict.propertyB_of_counts H f 3
      (fun T => (actual T).trans (pure_binding 3 T)))).elim
  · exact (notB (TwentyThreeFourLowStrict.propertyB_of_counts H f 4
      (fun T => (actual T).trans (pure_binding 4 T)))).elim
  · exact (notB (TwentyThreeFourLowStrict.propertyB_of_counts H f 5
      (fun T => (actual T).trans (pure_binding 5 T)))).elim
  · exact (notB (TwentyThreeFourLowStrict.propertyB_of_counts H f 6
      (fun T => (actual T).trans (pure_binding 6 T)))).elim
  · exact (notB (TwentyThreeFourLowStrict.propertyB_of_counts H f 7
      (fun T => (actual T).trans (pure_binding 7 T)))).elim
  · exact (notB (TwentyThreeFourLowStrict.propertyB_of_counts H f 8
      (fun T => (actual T).trans (pure_binding 8 T)))).elim
  · exact (notB (TwentyThreeFourLowStrict.propertyB_of_counts H f 9
      (fun T => (actual T).trans (pure_binding 9 T)))).elim
  · exact (notB (TwentyThreeFourLowStrict.propertyB_of_counts H f 10
      (fun T => (actual T).trans (pure_binding 10 T)))).elim
  · exact (notB (TwentyThreeFourLowStrict.propertyB_of_counts H f 11
      (fun T => (actual T).trans (pure_binding 11 T)))).elim
  · exact (notB (TwentyThreeFourLowStrict.propertyB_of_counts H f 12
      (fun T => (actual T).trans (pure_binding 12 T)))).elim
  · exact (notB (TwentyThreeFourLowJoint19.propertyB_of_counts H f
      (fun T => (actual T).trans (joint_binding19 T)))).elim
  · exact (notB (TwentyThreeFourLowJoint20.propertyB_of_counts H f
      (fun T => (actual T).trans (joint_binding20 T)))).elim
  · exact (notB (TwentyThreeFourLowJoint21.propertyB_of_counts H f
      (fun T => (actual T).trans (joint_binding21 T)))).elim
  · exact (notB (TwentyThreeFourLowStrict.propertyB_of_counts H f 13
      (fun T => (actual T).trans (pure_binding 13 T)))).elim
  · exact (notB (TwentyThreeFourLowStrict.propertyB_of_counts H f 14
      (fun T => (actual T).trans (pure_binding 14 T)))).elim
  · exact (notB (TwentyThreeFourLowStrict.propertyB_of_counts H f 15
      (fun T => (actual T).trans (pure_binding 15 T)))).elim
  · exact (notB (TwentyThreeFourLowStrict.propertyB_of_counts H f 16
      (fun T => (actual T).trans (pure_binding 16 T)))).elim
  · exact ⟨5, actual⟩
  · exact ⟨6, actual⟩
  · exact (notB (TwentyThreeFourLowStrict.propertyB_of_counts H f 17
      (fun T => (actual T).trans (pure_binding 17 T)))).elim
  · exact ⟨7, actual⟩
  · exact (notB (TwentyThreeFourLowStrict.propertyB_of_counts H f 18
      (fun T => (actual T).trans (pure_binding 18 T)))).elim
  · exact (notB (TwentyThreeFourLowStrict.propertyB_of_counts H f 19
      (fun T => (actual T).trans (pure_binding 19 T)))).elim
  · exact (notB (TwentyThreeFourLowStrict.propertyB_of_counts H f 20
      (fun T => (actual T).trans (pure_binding 20 T)))).elim
  · exact (notB (TwentyThreeFourLowStrict.propertyB_of_counts H f 21
      (fun T => (actual T).trans (pure_binding 21 T)))).elim
  · exact (notB (TwentyThreeFourLowStrict.propertyB_of_counts H f 22
      (fun T => (actual T).trans (pure_binding 22 T)))).elim
  · exact (notB (TwentyThreeFourLowStrict.propertyB_of_counts H f 23
      (fun T => (actual T).trans (pure_binding 23 T)))).elim
  · exact (notB (TwentyThreeFourLowStrict.propertyB_of_counts H f 24
      (fun T => (actual T).trans (pure_binding 24 T)))).elim
  · exact (notB (TwentyThreeFourLowStrict.propertyB_of_counts H f 25
      (fun T => (actual T).trans (pure_binding 25 T)))).elim
  · exact (notB (TwentyThreeFourLowStrict.propertyB_of_counts H f 26
      (fun T => (actual T).trans (pure_binding 26 T)))).elim
  · exact (notB (TwentyThreeFourLowStrict.propertyB_of_counts H f 27
      (fun T => (actual T).trans (pure_binding 27 T)))).elim
  · exact (notB (TwentyThreeFourLowStrict.propertyB_of_counts H f 28
      (fun T => (actual T).trans (pure_binding 28 T)))).elim
  · exact (notB (TwentyThreeFourLowStrict.propertyB_of_counts H f 29
      (fun T => (actual T).trans (pure_binding 29 T)))).elim
  · exact (notB (TwentyThreeFourLowStrict.propertyB_of_counts H f 30
      (fun T => (actual T).trans (pure_binding 30 T)))).elim
  · exact (notB (TwentyThreeFourLowStrict.propertyB_of_counts H f 31
      (fun T => (actual T).trans (pure_binding 31 T)))).elim
  · exact (notB (TwentyThreeFourLowStrict.propertyB_of_counts H f 32
      (fun T => (actual T).trans (pure_binding 32 T)))).elim
  · exact (notB (TwentyThreeFourLowStrict.propertyB_of_counts H f 33
      (fun T => (actual T).trans (pure_binding 33 T)))).elim
  · exact (notB (TwentyThreeFourLowStrict.propertyB_of_counts H f 34
      (fun T => (actual T).trans (pure_binding 34 T)))).elim
  · exact (notB (TwentyThreeFourLowStrict.propertyB_of_counts H f 35
      (fun T => (actual T).trans (pure_binding 35 T)))).elim
  · exact (notB (TwentyThreeFourLowStrict.propertyB_of_counts H f 36
      (fun T => (actual T).trans (pure_binding 36 T)))).elim
  · exact (notB (TwentyThreeFourLowStrict.propertyB_of_counts H f 37
      (fun T => (actual T).trans (pure_binding 37 T)))).elim

/-- From any actual four low vertices, obtain a residue after a genuine
permutation of those same vertices. No external local-table premise remains. -/
theorem actual_residual (H : Simple5Hypergraph (Fin 23)) (cover : H.PairCovering)
    (edges : H.edges.card=34) (f : Fin 4 ↪ Fin 23)
    (degrees : ∀ i, H.degree (f i)=6) (notB : ¬ PropertyB H) :
    ∃ r : Residue, ∃ σ : Equiv.Perm (Fin 4),
      ∀ T, count H (σ.toEmbedding.trans f) T=residualCounts r T := by
  obtain ⟨k, σ, actual⟩ := TwentyThreeFourLowCatalog.actual_representative_perm H cover edges f degrees
  change ∀ T, count H (σ.toEmbedding.trans f) T = TwentyThreeFourLowCatalog.counts k T at actual
  let τ := permutation (oldToSource k).2
  have mapped : ∀ T, count H ((τ.trans σ).toEmbedding.trans f) T =
      sourceCounts (oldToSource k).1 T := by
    intro T
    change count H (τ.toEmbedding.trans (σ.toEmbedding.trans f)) T = _
    rw [LockRelabel.count_comp_perm, actual]
    simpa only [Finset.map_eq_image] using old_binding k T
  obtain ⟨r, hr⟩ := residual_of_noB H ((τ.trans σ).toEmbedding.trans f)
    (oldToSource k).1 notB mapped
  exact ⟨r, τ.trans σ, hr⟩

end Aris4Math.ThirtyFour.TwentyThreeFourLowClassified
#print axioms Aris4Math.ThirtyFour.TwentyThreeFourLowClassified.actual_residual
