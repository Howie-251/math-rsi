namespace ExampleProof

def Target : Prop := ∀ n : Nat, n ≤ n + 1

theorem original_theorem : Target := by
  intro n
  exact Nat.le_succ n

end ExampleProof
#print ExampleProof.Target
#check @ExampleProof.original_theorem
#print axioms ExampleProof.original_theorem
