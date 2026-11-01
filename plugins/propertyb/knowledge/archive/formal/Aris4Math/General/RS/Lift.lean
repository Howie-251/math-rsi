import Aris4Math.General.RS.Definitions
import Mathlib.Data.Finset.Image
import Mathlib.Data.Fintype.Card

/-! Relabel finite hypergraphs along actual vertex equivalences and transfer
results on `Fin n` back to arbitrary finite vertex types. -/
namespace Aris4Math.General.RS

universe u v

/-- The same edge family under a bijective change of vertex labels. -/
def relabel {V : Type u} {W : Type v} (f : V ≃ W) (E : Finset (Finset V)) :
    Finset (Finset W) := E.map f.finsetCongr.toEmbedding

@[simp] theorem relabel_card {V : Type u} {W : Type v}
    (f : V ≃ W) (E : Finset (Finset V)) : (relabel f E).card = E.card := by
  exact Finset.card_map _

@[simp] theorem edge_relabel_card {V : Type u} {W : Type v}
    (f : V ≃ W) (e : Finset V) : (f.finsetCongr e).card = e.card := by
  exact Finset.card_map _

@[simp] theorem mem_relabel {V : Type u} {W : Type v}
    (f : V ≃ W) (E : Finset (Finset V)) (e : Finset V) :
    f.finsetCongr e ∈ relabel f E ↔ e ∈ E := by
  simp only [relabel, Finset.mem_map_equiv, Equiv.symm_apply_apply]

@[simp] theorem uniform_relabel_iff {V : Type u} {W : Type v}
    (f : V ≃ W) (E : Finset (Finset V)) (k : ℕ) :
    Uniform (relabel f E) k ↔ Uniform E k := by
  constructor
  · intro h e he
    simpa using h _ ((mem_relabel f E e).mpr he)
  · intro h e he
    obtain ⟨d, hd, rfl⟩ := Finset.mem_map.mp he
    simpa using h d hd

@[simp] theorem edge_relabel_inter {V : Type u} {W : Type v}
    [DecidableEq V] [DecidableEq W] (f : V ≃ W) (e g : Finset V) :
    f.finsetCongr e ∩ f.finsetCongr g = f.finsetCongr (e ∩ g) := by
  exact (Finset.map_inter e g).symm

@[simp] theorem edge_relabel_inter_card {V : Type u} {W : Type v}
    [DecidableEq V] [DecidableEq W] (f : V ≃ W) (e g : Finset V) :
    (f.finsetCongr e ∩ f.finsetCongr g).card = (e ∩ g).card := by
  rw [edge_relabel_inter, edge_relabel_card]

/-- Relabeling preserves the actual directed single-intersection pair set. -/
theorem singlePairs_relabel {V : Type u} {W : Type v}
    (f : V ≃ W) (E : Finset (Finset V)) :
    singlePairs (relabel f E) = (singlePairs E).map
      (Equiv.prodCongr f.finsetCongr f.finsetCongr).toEmbedding := by
  classical
  ext p
  obtain ⟨⟨e, g⟩, rfl⟩ := (Equiv.prodCongr f.finsetCongr f.finsetCongr).surjective p
  rw [Finset.mem_map_equiv, Equiv.symm_apply_apply]
  change (f.finsetCongr e, f.finsetCongr g) ∈ singlePairs (relabel f E) ↔
    (e, g) ∈ singlePairs E
  have heq : f.finsetCongr e = f.finsetCongr g ↔ e = g :=
    (f.finsetCongr).injective.eq_iff
  simp only [singlePairs, Finset.mem_filter, Finset.mem_product,
    mem_relabel, edge_relabel_inter_card, ne_eq, heq]

@[simp] theorem gamma_relabel {V : Type u} {W : Type v}
    (f : V ≃ W) (E : Finset (Finset V)) : gamma (relabel f E) = gamma E := by
  rw [gamma, singlePairs_relabel, Finset.card_map]
  rfl

/-- Pull a given coloring back along the actual vertex equivalence. -/
theorem bichromatic_relabel_iff {V : Type u} {W : Type v}
    (f : V ≃ W) (E : Finset (Finset V)) (c : W → Bool) :
    Bichromatic (relabel f E) c ↔ Bichromatic E (c ∘ f) := by
  constructor
  · intro h e he
    obtain ⟨ht, hf⟩ := h _ ((mem_relabel f E e).mpr he)
    constructor
    · obtain ⟨y, hy, hc⟩ := ht
      obtain ⟨x, hx, hxy⟩ := Finset.mem_map.mp hy
      exact ⟨x, hx, by simpa only [Function.comp_apply, ← hxy] using hc⟩
    · obtain ⟨y, hy, hc⟩ := hf
      obtain ⟨x, hx, hxy⟩ := Finset.mem_map.mp hy
      exact ⟨x, hx, by simpa only [Function.comp_apply, ← hxy] using hc⟩
  · intro h e he
    obtain ⟨d, hd, rfl⟩ := Finset.mem_map.mp he
    obtain ⟨⟨x, hx, hxc⟩, ⟨y, hy, hyc⟩⟩ := h d hd
    exact ⟨⟨f x, Finset.mem_map.mpr ⟨x, hx, rfl⟩, hxc⟩,
      ⟨f y, Finset.mem_map.mpr ⟨y, hy, rfl⟩, hyc⟩⟩

@[simp] theorem propertyB_relabel_iff {V : Type u} {W : Type v}
    (f : V ≃ W) (E : Finset (Finset V)) :
    PropertyB (relabel f E) ↔ PropertyB E := by
  constructor
  · rintro ⟨c, hc⟩
    exact ⟨c ∘ f, (bichromatic_relabel_iff f E c).mp hc⟩
  · rintro ⟨c, hc⟩
    refine ⟨c ∘ f.symm, (bichromatic_relabel_iff f E (c ∘ f.symm)).mpr ?_⟩
    simpa [Function.comp_def] using hc

/-- Transfer any criterion depending on the actual edge count and the actual
single-intersection pair count from `Fin n` to arbitrary finite vertices. -/
theorem propertyB_of_fin_criterion (k : ℕ) (C : ℕ → ℕ → Prop)
    (hfin : ∀ (n : ℕ) (F : Finset (Finset (Fin n))),
      Uniform F k → C F.card (gamma F) → PropertyB F)
    {V : Type u} [Finite V] (E : Finset (Finset V))
    (hU : Uniform E k) (hC : C E.card (gamma E)) : PropertyB E := by
  classical
  letI := Fintype.ofFinite V
  let f : V ≃ Fin (Fintype.card V) := Fintype.equivFin V
  apply (propertyB_relabel_iff f E).mp
  exact hfin _ (relabel f E) ((uniform_relabel_iff f E k).mpr hU) (by simpa using hC)

/-- The precise bare finite-vertex pilot target follows from its `Fin n` caller. -/
theorem pilotTarget_of_fin
    (hfin : ∀ (n : ℕ) (F : Finset (Finset (Fin n))),
      Uniform F 17 → F.card ≤ 2 ^ 17 → PropertyB F) : PilotTarget.{u} := by
  intro V _ E hU hcard
  exact propertyB_of_fin_criterion 17 (fun m _ => m ≤ 2 ^ 17)
    (by intro n F hF hM; exact hfin n F hF hM) E hU hcard

end Aris4Math.General.RS

#print axioms Aris4Math.General.RS.gamma_relabel
#print axioms Aris4Math.General.RS.propertyB_relabel_iff
#print axioms Aris4Math.General.RS.propertyB_of_fin_criterion
#print axioms Aris4Math.General.RS.pilotTarget_of_fin
