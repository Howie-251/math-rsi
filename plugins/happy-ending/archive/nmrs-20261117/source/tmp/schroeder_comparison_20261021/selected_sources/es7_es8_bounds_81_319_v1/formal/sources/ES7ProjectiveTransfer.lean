import ES7PartitionComplete

namespace ES7ProjectiveTransfer
open ES8Geometry ES8BalancedGeometry ES8Projective ES8CoordinateMaps ES8ActualRanks
open ES7Geometry ES7Subset

/-- Pull an actual seven-point convex set back along a hull-preserving injection. -/
theorem heptagon_pullback (f : Point→Point) (S : Set Point)
    (inj : Set.InjOn f S) (hull : MapsHull f S)
    (oct : HasConvexHeptagon (f '' S)) : HasConvexHeptagon S := by
  classical
  obtain ⟨A,card,inside,convex⟩ := oct
  have witnesses (q : ↥A) : ∃ p, p∈S ∧ f p=q.val := inside q.property
  choose g gin geq using witnesses
  let B := Finset.univ.image g
  have gi : Function.Injective g := by
    intro q r eq
    apply Subtype.ext
    rw [←geq q,←geq r,eq]
  have Bin : (↑B : Set Point)⊆S := by
    intro p hp; obtain ⟨q,_,rfl⟩ := Finset.mem_image.mp hp
    exact gin q
  have image : f '' (↑B : Set Point)=↑A := by
    ext q
    constructor
    · rintro ⟨p,hp,rfl⟩
      obtain ⟨r,_,rfl⟩ := Finset.mem_image.mp hp
      rw [geq r]; exact r.property
    · intro hq
      exact ⟨g ⟨q,hq⟩,Finset.mem_image.mpr ⟨⟨q,hq⟩,by simp,rfl⟩,geq ⟨q,hq⟩⟩
  refine ⟨B,?_,Bin,?_⟩
  · simp [B,Finset.card_image_of_injective _ gi,card]
  · apply convex_pullback f (↑B) (inj.mono Bin)
    · intro T hT p hp h; exact hull T (hT.trans Bin) p (Bin hp) h
    · rw [image]; exact convex

/-- Numerical asymmetric obligation, left explicit throughout the transfer. -/
def AsymmetricBound (K : Nat) : Prop := ∀ {n} (c : Configuration n),
  (¬(colorConfig c.cup true).HasNCap 6 (Finset.range n)) →
  (¬HasConvexHeptagon (Set.range c.point)) → n≤K

/-- Radial order is exactly the abscissa order in the projective chart. -/
theorem radial_identity (a b : Point) (ha : a.1≠0) (hb : b.1≠0) :
    orient (0,0) a b=a.1*b.1*((project b).1-(project a).1) := by
  unfold project orient; dsimp; field_simp; ring

theorem root_cap_heptagon (p : Fin 6→Point) (positive : ∀ i, 0<(p i).1)
    (ordered : StrictMono (fun i=>(project (p i)).1))
    (caps : ∀ i j k : Fin 6, i<j → j<k → orient (project (p i)) (project (p j)) (project (p k))<0)
    (S : Set Point) (root : (0,0)∈S) (inside : ∀ i, p i∈S) : HasConvexHeptagon S := by
  let q : Nat→Point := fun i=>if h : 0 < i ∧ i < 7 then p ⟨i-1,by omega⟩ else (0,0)
  apply heptagon_of_cyclic q
  · intro i j k ij jk kn
    have jpos : 0 < j := by omega
    have kpos : 0 < k := by omega
    have jn : j<7 := by omega
    have kj : (⟨j-1,by omega⟩ : Fin 6)<⟨k-1,by omega⟩ := by change j-1<k-1; omega
    by_cases iz : i=0
    · subst i
      simp only [q,show ¬(0<0 ∧ 0<7) by omega, dite_false]
      simp only [show 0 < j ∧ j < 7 from ⟨jpos,jn⟩,show 0 < k ∧ k < 7 from ⟨kpos,kn⟩,and_self,dite_true]
      rw [radial_identity _ _ (ne_of_gt (positive _)) (ne_of_gt (positive _))]
      exact mul_pos (mul_pos (positive _) (positive _)) (sub_pos.mpr (ordered kj))
    · have ipos : 0 < i := by omega
      have inn : i < 7 := by omega
      simp only [q,show 0 < i ∧ i < 7 from ⟨ipos,inn⟩,show 0 < j ∧ j < 7 from ⟨jpos,jn⟩,show 0 < k ∧ k < 7 from ⟨kpos,kn⟩,and_self,dite_true]
      have neg := caps ⟨i-1,by omega⟩ ⟨j-1,by omega⟩ ⟨k-1,by omega⟩ (by change i-1<j-1; omega) kj
      rw [project_orient _ _ _ (ne_of_gt (positive _)) (ne_of_gt (positive _)) (ne_of_gt (positive _))] at neg
      have den := mul_pos (mul_pos (positive ⟨i-1,by omega⟩) (positive ⟨j-1,by omega⟩)) (positive ⟨k-1,by omega⟩)
      have := (div_lt_iff₀ den).mp neg
      linarith
  · intro i hi
    by_cases iz : 0 < i
    · simpa only [q,show 0 < i ∧ i < 7 from ⟨iz,hi⟩,and_self,dite_true] using inside ⟨i-1,by omega⟩
    · simpa [q,iz] using root

/-- The projective-deletion theorem in a positive-x chart. The root is retained
in the ambient set, and every possible six-cap yields a heptagon with it. -/
theorem chart_bound (bound : AsymmetricBound K) {m} (p : Fin m→Point) (positive : ∀ i, 0<(p i).1)
    (radial : ∀ i j, i≠j → orient (0,0) (p i) (p j)≠0)
    (gp : ∀ i j k, i≠j → j≠k → i≠k → orient (p i) (p j) (p k)≠0)
    (S : Set Point) (root : (0,0)∈S) (inside : ∀ i, p i∈S)
    (noOct : ¬HasConvexHeptagon S) : m≤K := by
  have xi : Function.Injective (fun i=>(project (p i)).1) := by
    intro i j eq
    change (project (p i)).1=(project (p j)).1 at eq
    by_contra ne
    apply radial i j ne
    rw [radial_identity _ _ (ne_of_gt (positive _)) (ne_of_gt (positive _)),eq]
    ring
  have pg : ∀ i j k, i≠j → j≠k → i≠k →
      orient (project (p i)) (project (p j)) (project (p k))≠0 := by
    intro i j k ij jk ik
    rw [project_orient _ _ _ (ne_of_gt (positive _)) (ne_of_gt (positive _)) (ne_of_gt (positive _))]
    exact div_ne_zero (neg_ne_zero.mpr (gp i j k ij jk ik))
      (ne_of_gt (mul_pos (mul_pos (positive i) (positive j)) (positive k)))
  have reorder : ∃ c : Configuration m, ∃ e : Fin m≃Fin m,
      ∀ i, c.point i=project (p (e i)) := by
    have h := ordered_configuration (fun i=>project (p i)) xi pg
    have card : Fintype.card (Fin m)=m := Fintype.card_fin m
    rw [card] at h
    exact h
  obtain ⟨c,e,points⟩ := reorder
  have range_eq : Set.range c.point=project '' Set.range p := by
    ext v
    constructor
    · rintro ⟨i,rfl⟩; exact ⟨p (e i),⟨e i,rfl⟩,(points i).symm⟩
    · rintro ⟨v,⟨i,rfl⟩,rfl⟩; exact ⟨e.symm i,by simp [points]⟩
  have noOctC : ¬HasConvexHeptagon (Set.range c.point) := by
    intro h
    rw [range_eq] at h
    have posSet : Set.range p⊆{x : Point | 0<x.1} := by rintro x ⟨i,rfl⟩; exact positive i
    have hull : MapsHull project (Set.range p) := by
      intro T hT x hx hin; exact project_mapsHull T (hT.trans posSet) x (posSet hx) hin
    have old := heptagon_pullback project (Set.range p) (project_injective.mono posSet) hull h
    exact noOct (ES7Subset.heptagon_mono _ S (by rintro x ⟨i,rfl⟩; exact inside i) old)
  have noCapC : ¬(colorConfig c.cup true).HasNCap 6 (Finset.range m) := by
    rintro ⟨xs,⟨cap,len⟩,xsIn⟩
    let index : Fin 6→Fin m := fun i=>⟨xs.get ⟨i.val,by omega⟩,
      Finset.mem_range.mp (xsIn _ (xs.get_mem _))⟩
    have indexOrder : StrictMono index := by
      intro i j hij
      exact cap.1.pairwise.rel_get_of_lt hij
    have at_point (i : Fin 6) : ES8BaekGeometry.pointAt c (xs.get ⟨i.val,by omega⟩)=project (p (e (index i))) := by
      rw [ES8BaekGeometry.pointAt_eq c _ (index i).isLt]
      exact points (index i)
    apply noOct
    apply root_cap_heptagon (fun i=>p (e (index i))) (fun i=>positive _) ?_ ?_ S root (fun i=>inside _)
    · intro i j ij
      have h := c.xOrder (indexOrder ij)
      simpa only [points] using h
    · intro i j k ij jk
      have h := ES8BaekGeometry.cap_list_all c xs xsIn cap
        _ (xs.get_mem ⟨i.val,by omega⟩) _ (xs.get_mem ⟨j.val,by omega⟩) _ (xs.get_mem ⟨k.val,by omega⟩)
        (indexOrder ij) (indexOrder jk)
      simpa only [at_point] using h
  exact bound c noCapC noOctC

/-- Every ordered configuration avoiding heptagons has at most K+1 points. -/
theorem ordered_bound (bound : AsymmetricBound K) {m} (c : Configuration (m+1))
    (noOct : ¬HasConvexHeptagon (Set.range c.point)) : m+1≤K+1 := by
  let r := c.point 0
  let p : Fin m→Point := fun i=>shift r (c.point i.succ)
  have positive (i : Fin m) : 0<(p i).1 := by
    change 0<(c.point i.succ).1-(c.point 0).1
    exact sub_pos.mpr (c.xOrder (by change 0 < i.val+1; omega))
  have radial (i j : Fin m) (ij : i≠j) : orient (0,0) (p i) (p j)≠0 := by
    have gp := generalPosition_any c 0 i.succ j.succ (by intro h; have := congrArg Fin.val h; simp at this) ((by simpa using ij)) (by intro h; have := congrArg Fin.val h; simp at this)
    have eq := shift_orient r r (c.point i.succ) (c.point j.succ)
    have rz : shift r r=(0,0) := by ext <;> simp [shift]
    rw [rz] at eq
    exact eq ▸ gp
  have gp (i j k : Fin m) (ij : i≠j) (jk : j≠k) (ik : i≠k) : orient (p i) (p j) (p k)≠0 := by
    rw [show orient (p i) (p j) (p k)=orient (c.point i.succ) (c.point j.succ) (c.point k.succ) from shift_orient _ _ _ _]
    exact generalPosition_any c _ _ _ ((by simpa using ij)) ((by simpa using jk)) ((by simpa using ik))
  have noShift : ¬HasConvexHeptagon (shift r '' Set.range c.point) := by
    intro h
    exact noOct (heptagon_pullback _ _ (shift_injective r).injOn (shift_mapsHull r _) h)
  have bound := chart_bound bound p positive radial gp (shift r '' Set.range c.point)
    ⟨r,⟨0,rfl⟩,by ext <;> simp [shift]⟩ (fun i=>⟨c.point i.succ,⟨i.succ,rfl⟩,rfl⟩) noShift
  omega


#print axioms root_cap_heptagon
#print axioms chart_bound
#print axioms ordered_bound
end ES7ProjectiveTransfer
