import ES7JointCodec
namespace ES7JointCatalog
open ES7ActualState

def shapes : List (List Nat) := [[0, 0, 0, 0], [1, 0, 0, 0], [1, 1, 0, 0], [1, 1, 1, 0], [2, 0, 0, 0], [2, 1, 0, 0], [2, 1, 1, 0], [2, 2, 0, 0], [2, 2, 1, 0], [2, 2, 2, 0], [3, 0, 0, 0], [3, 1, 0, 0], [3, 1, 1, 0], [3, 2, 0, 0], [3, 2, 1, 0], [3, 2, 2, 0], [3, 3, 0, 0], [3, 3, 1, 0], [3, 3, 2, 0], [3, 3, 3, 0], [4, 1, 1, 1], [4, 2, 1, 1], [4, 2, 2, 1], [4, 2, 2, 2], [4, 3, 1, 1], [4, 3, 2, 1], [4, 3, 2, 2], [4, 3, 3, 1], [4, 3, 3, 2], [4, 3, 3, 3], [4, 4, 1, 1], [4, 4, 2, 1], [4, 4, 2, 2], [4, 4, 3, 1], [4, 4, 3, 2], [4, 4, 3, 3], [4, 4, 4, 1], [4, 4, 4, 2], [4, 4, 4, 3], [4, 4, 4, 4]]
def cells (hs : List Nat) : Finset Label :=
  (Finset.range 4).biUnion (fun i => (Finset.range (hs[i]?.getD 0)).image (fun j => (i+1,j+1)))
def states (i : Nat) : Finset Label := cells (shapes[i]?.getD [])
end ES7JointCatalog
