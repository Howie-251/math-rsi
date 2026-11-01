namespace ExampleProof

def Target : Prop := ∀ n : Nat, n ≤ n + 1

theorem available_interface (certificate : Target) : Target := certificate

end ExampleProof
#print ExampleProof.Target
#check @ExampleProof.available_interface
#print axioms ExampleProof.available_interface
