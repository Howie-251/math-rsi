import ES7ClosureBaseRules
import ES7ClosureAmbientRules
import ES7ClosureCoreRules
import ES7ClosureLowRules
import ES7ClosureCounting
import ES7ClosureTerminal
import ES7ClosurePacket
import ES7PrefixSchema
namespace ES7ClosureRules
open ES7ClosureFrame ES7ClosureMeaning ES7ClauseLogic ES8BalancedGeometry
inductive Schema where
  | base (r : ES7ClosureBaseRules.Schema)
  | ambient (r : ES7ClosureAmbientRules.Schema)
  | core (r : ES7ClosureCoreRules.Schema)
  | low (r : ES7ClosureLowRules.Schema)
  | counting (r : ES7ClosureCounting.Schema)
  | terminal (r : ES7ClosureTerminal.Schema)
  | packet (a b c d i j k : Nat) (v : Bool)
  | prefixRule (r : ES7PrefixSchema.Schema)
  deriving DecidableEq, Repr
def clause : Schema→List (Atom Variable)
  | .base r => ES7ClosureBaseRules.clause r
  | .ambient r => ES7ClosureAmbientRules.clause r
  | .core r => ES7ClosureCoreRules.clause r
  | .low r => ES7ClosureLowRules.clause r
  | .counting r => ES7ClosureCounting.clause r
  | .terminal r => ES7ClosureTerminal.clause r
  | .packet a b c d i j k v => ES7ClosurePacket.clause a b c d i j k v
  | .prefixRule r => ES7PrefixSchema.clause r
def Valid : Schema→Prop
  | .base r => ES7ClosureBaseRules.Valid r
  | .ambient r => ES7ClosureAmbientRules.Valid r
  | .core r => ES7ClosureCoreRules.Valid r
  | .low r => ES7ClosureLowRules.Valid r
  | .counting r => ES7ClosureCounting.Valid r
  | .terminal r => ES7ClosureTerminal.Valid r
  | .packet a b c d i j k _ => ES7ClosureBaseRules.boundedDistinct 39 [a,b,c,d] ∧ i < j ∧ j < k ∧ k < 4
  | .prefixRule r => ES7PrefixSchema.Valid r
instance (r) : Decidable (Valid r) := by cases r <;> unfold Valid <;> infer_instance
theorem sound (m : Model c realStates) (r : Schema) (valid : Valid r) : Satisfied (meaning m) (clause r) := by
  cases r with
  | base r => exact ES7ClosureBaseRules.sound m r valid
  | ambient r => exact ES7ClosureAmbientRules.sound m r valid
  | core r => exact ES7ClosureCoreRules.sound m r valid
  | low r => exact ES7ClosureLowRules.sound m r valid
  | counting r => exact ES7ClosureCounting.sound m r valid
  | terminal r => exact ES7ClosureTerminal.sound m r valid
  | packet a b c d i j k v => exact ES7ClosurePacket.sound m a b c d i j k v valid.1 valid.2.1 valid.2.2.1 valid.2.2.2
  | prefixRule r => exact ES7PrefixSchema.sound m r valid
end ES7ClosureRules
