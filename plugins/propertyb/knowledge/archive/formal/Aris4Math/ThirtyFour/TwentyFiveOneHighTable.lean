import Aris4Math.ThirtyFour.TwentyFiveColoredRows
namespace Aris4Math.ThirtyFour.TwentyFiveOneHighTable
open Aris4Math.K6Classification TwentyFiveUnitCounts TwentyFiveColoredActual
open TwentyFiveColoredRows
variable {m t : ℕ}

def sources (base : Fin m → Finset (Finset (Fin 9))) :=
  (List.ofFn base).flatMap fun big => List.ofFn fun h : Fin 9 => (big,Finset.univ.erase h)

theorem low_eq (low : Finset (Fin 9)) (card : low.card=8) :
    ∃ h : Fin 9, low=Finset.univ.erase h := by
  have one : lowᶜ.card=1 := by rw [Finset.card_compl,Fintype.card_fin,card]
  obtain ⟨h,same⟩ := Finset.card_eq_one.mp one
  refine ⟨h,?_⟩
  have eq := congrArg (fun s : Finset (Fin 9) => sᶜ) same
  simpa only [compl_compl,Finset.compl_singleton] using eq

theorem table (base : Fin m → Finset (Finset (Fin 9)))
    (target : Fin t → Finset (Finset (Fin 9)))
    (rows : List (Row 9 t)) (complete : rows.map source=sources base)
    (checked : rows.all (fun r => decide (Check 8 target r))=true)
    (c : Fin m) (low : Finset (Fin 9)) (card : low.card=8)
    (feasible : Feasible 34 (colors low) (pairCompletion (base c))) :
    ∃ d : Fin t, ∃ τ : Equiv.Perm (Fin 9),
      (∀ i,standard 8 (τ i)=colors low i) ∧
      (base c).image (fun T => T.map τ.toEmbedding)=target d := by
  obtain ⟨h,rfl⟩ := low_eq low card
  have mem : (base c,Finset.univ.erase h)∈rows.map source := by
    rw [complete]
    exact List.mem_flatMap.mpr ⟨base c,List.mem_ofFn.mpr ⟨c,rfl⟩,
      List.mem_ofFn.mpr ⟨h,rfl⟩⟩
  obtain ⟨r,member,same⟩ := List.mem_map.mp mem
  have bigEq : r.listed.toFinset=base c := congrArg Prod.fst same
  have lowEq : r.low=Finset.univ.erase h := congrArg Prod.snd same
  have valid := of_decide_eq_true (List.all_eq_true.mp checked r member)
  have rf : Feasible 34 (colors r.low) (pairCompletion r.listed.toFinset) := by
    simpa only [bigEq,lowEq] using feasible
  obtain ⟨τ,moves,family⟩ := sound 8 target r valid rf
  refine ⟨r.witness.target,τ,?_,?_⟩
  · simpa only [lowEq] using moves
  · simpa only [bigEq] using family

end Aris4Math.ThirtyFour.TwentyFiveOneHighTable
