import ES7OrderedData
import ES7LRAT

namespace ES7PrimitiveAssignment
open ES8ActualRanks ES8BalancedGeometry ES7LiteralMeaning ES7SourceClauses

/-- The source's positive DIMACS identifier k+1 uses Std.Sat variable k. -/
noncomputable def geometricAssignment (d : Decoder) (c : Configuration 26) (k : Nat) : Bool :=
  match (d[k+1]?).join with
  | some v => assignment c v
  | none => false

def signedClause (ls : List Int) : Std.Sat.CNF.Clause Nat :=
  ls.map (fun l=>(l.natAbs-1,decide (0<l)))
def formula (cls : List (List Int)) : Std.Sat.CNF Nat := ⟨(cls.map signedClause).toArray⟩

theorem original_to_eval (d : Decoder) (c : Configuration 26) (ls : List Int)
    (sat : OriginalSatisfied d c ls) : (signedClause ls).eval (geometricAssignment d c)=true := by
  classical
  obtain ⟨l,hl,v,hv,h⟩ := sat
  have nonzero : l≠0 := by rcases h with h|h <;> omega
  have abspos : 0<l.natAbs := Int.natAbs_pos.mpr nonzero
  have index : l.natAbs-1+1=l.natAbs := by omega
  apply List.any_eq_true.mpr
  refine ⟨(l.natAbs-1,decide (0<l)),List.mem_map.mpr ⟨l,hl,rfl⟩,?_⟩
  change (geometricAssignment d c (l.natAbs-1)==decide (0<l))=true
  simp only [geometricAssignment,index,hv]
  rcases h with ⟨pos,h⟩|⟨neg,h⟩
  · simp [pos,(assignment_spec c v).mpr h]
  · have eq : assignment c v=false := by
      cases he : assignment c v
      · rfl
      · exact (h ((assignment_spec c v).mp he)).elim
    simp [show ¬0<l by omega,eq]

theorem formula_satisfied (d : Decoder) (c : Configuration 26) (cls : List (List Int))
    (sat : ∀ cl∈cls,OriginalSatisfied d c cl) :
    (formula cls).eval (geometricAssignment d c)=true := by
  unfold formula Std.Sat.CNF.eval
  simp only [List.all_toArray]
  apply List.all_eq_true.mpr
  intro cl member
  obtain ⟨ls,hls,rfl⟩ := List.mem_map.mp member
  exact original_to_eval d c ls (sat ls hls)

/-- Both source families are satisfied by the SAME assignment. No independent
choice of pair ranks, colors, orders, or witness owners is allowed. -/
theorem all_primitive_clauses_satisfied (c : Configuration 26)
    (noCap : ¬(colorConfig c.cup true).HasNCap 5 (Finset.range 26))
    (noCup : ¬(colorConfig c.cup true).HasNCup 6 (Finset.range 26))
    (noGon : ¬ES7Geometry.HasConvexHeptagon (Set.range c.point)) :
    ∃ d ex ord,
      ES7VariableCodec.decoder ES7ExactData.names ES7ExactData.tableSize=some d ∧
      ES7VariableCodec.records ES7ExactData.rows=some ex ∧
      ES7OrderedCodec.records ES7OrderedData.rows=some ord ∧
      (formula ((ex.map ES7SourceClauses.Record.clause)++(ord.map ES7OrderedCodec.Record.clause))).eval
        (geometricAssignment d c)=true := by
  obtain ⟨d,ex,hd,he,hx⟩ := ES7ExactData.all_exact_clauses_necessary
  obtain ⟨d',ord,hd',ho,hy⟩ := ES7OrderedData.all_ordered_clauses_necessary
  have equal : d'=d := Option.some.inj (hd'.symm.trans hd)
  subst d'
  refine ⟨d,ex,ord,hd,he,ho,formula_satisfied d c _ ?_⟩
  intro cl member
  rcases List.mem_append.mp member with left|right
  · obtain ⟨r,hr,rfl⟩ := List.mem_map.mp left
    exact hx r hr c noCap noCup
  · obtain ⟨r,hr,rfl⟩ := List.mem_map.mp right
    exact hy r hr c noCap noCup noGon

#print axioms original_to_eval
#print axioms all_primitive_clauses_satisfied
end ES7PrimitiveAssignment
