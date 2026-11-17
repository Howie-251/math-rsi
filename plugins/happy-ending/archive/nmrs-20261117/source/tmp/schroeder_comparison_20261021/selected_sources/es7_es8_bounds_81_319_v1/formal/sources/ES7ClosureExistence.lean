import ES7ClosureConstruction
namespace ES7ClosureExistence
open ES7ClosureFrame ES7ClosureConstruction ES7BalancedEndpoints ES7BalancedPopulations ES8BalancedGeometry

theorem exists_frame (c : Configuration 50)
    (noSix : NoSix c.cup (Finset.range 50))
    (noH : ¬ES7Geometry.HasConvexHeptagon (Set.range c.point)) :
    ∃d : Configuration 50,∃states : Nat→Finset ES7ActualState.Label,Nonempty (Model d states) := by
  obtain ⟨d,dSix,dH,normal⟩ := ES7BalancedSelection.exists_normalized c noSix noH
  obtain ⟨last,a,b,f,g,lastIn,lastMax,la,ab,bf,fg,chain⟩ := ES7BalancedSelection.exists_terminal d dSix dH
  let tail : Fin 4→Fin 50 := ![a,b,f,g]
  have mono : StrictMono tail := by
    apply Fin.strictMono_iff_lt_succ.mpr
    intro i
    fin_cases i <;> simpa [tail] using (by assumption)
  exact ⟨d,selectedStates d tail,⟨frame d dSix dH normal tail mono last lastIn lastMax la chain⟩⟩
end ES7ClosureExistence
