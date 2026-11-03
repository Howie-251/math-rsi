import DegreeDiameter.Portfolio.F3Graph15552Linear
namespace DegreeDiameter.Portfolio.F3Graph15552
set_option maxRecDepth 20000
set_option maxHeartbeats 40000000

def routeController : Fin 192 → List (Fin 5) → Fin 192
  | a,[] => a
  | a,p::ps => routeController (controller a p) ps
def routeForward : List (Fin 5) → Vec → Fin 15552 → Fin 15552
  | [],_,u => u
  | p::ps,q,u => routeForward ps (noiseShift q) (forward u p (q 0))
theorem routeForward_parts (ps : List (Fin 5)) (q x : Vec) (a : Fin 192) :
    routeForward ps q (liftAt a (encodeVec x))=
      liftAt (routeController a ps) (encodeVec (routeVec ps q x)) := by
  induction ps generalizing q x a with
  | nil => rfl
  | cons p ps ih =>
      simp only [routeForward,routeController,routeVec,forward_liftAt]
      exact ih _ _ _

/-- Holding is a nil walk; it is never asserted to be a source edge. -/
theorem holding_or_edge_walk {u v : Fin 15552} (h : u=v ∨ graph.Adj u v) :
    ∃w : graph.Walk u v,w.length≤1 := by
  rcases h with h|h
  · subst v
    exact ⟨SimpleGraph.Walk.nil,by change 0≤1;omega⟩
  · exact ⟨SimpleGraph.Walk.cons h SimpleGraph.Walk.nil,by change 1≤1;omega⟩
theorem completed_step_walk (u : Fin 15552) (p : Fin 5) (t : F) :
    ∃w : graph.Walk u (forward u p t),w.length≤1 := by
  apply holding_or_edge_walk
  by_cases h : u=forward u p t
  · exact Or.inl h
  · exact Or.inr (forward_adj_of_ne u p t h)
theorem bounded_walk_of_route (ps : List (Fin 5)) (q : Vec) (u : Fin 15552) :
    ∃w : graph.Walk u (routeForward ps q u),w.length≤ps.length := by
  induction ps generalizing q u with
  | nil => exact ⟨SimpleGraph.Walk.nil,by change 0≤0;omega⟩
  | cons p ps ih =>
      obtain ⟨first,hfirst⟩ := completed_step_walk u p (q 0)
      obtain ⟨tail,htail⟩ := ih (noiseShift q) (forward u p (q 0))
      refine ⟨first.append tail,?_⟩
      simp only [SimpleGraph.Walk.length_append,List.length_cons]
      omega
theorem walk_of_vector_endpoint (a b : Fin 192) (ps : List (Fin 5))
    (q x y : Vec) (hc : routeController a ps=b) (hv : routeVec ps q x=y)
    (hlen : ps.length≤4) :
    ∃w : graph.Walk (liftAt a (encodeVec x)) (liftAt b (encodeVec y)),w.length≤4 := by
  obtain ⟨w,hw⟩ := bounded_walk_of_route ps q (liftAt a (encodeVec x))
  have hb : ∃w : graph.Walk (liftAt a (encodeVec x))
      (routeForward ps q (liftAt a (encodeVec x))),w.length≤4 := ⟨w,hw.trans hlen⟩
  have heq := routeForward_parts ps q x a
  rw [hc,hv] at heq
  exact heq ▸ hb
theorem encoded_walk_to_finite (a b : Fin 192)
    (h : ∀x y : Vec,∃w : graph.Walk (liftAt a (encodeVec x)) (liftAt b (encodeVec y)),w.length≤4)
    (x y : Fin 81) : ∃w : graph.Walk (liftAt a x) (liftAt b y),w.length≤4 := by
  have hv := h (decodeVec x) (decodeVec y)
  have hx : liftAt a (encodeVec (decodeVec x))=liftAt a x :=
    congrArg (liftAt a) (encodeVec_decodeVec x)
  have hy : liftAt b (encodeVec (decodeVec y))=liftAt b y :=
    congrArg (liftAt b) (encodeVec_decodeVec y)
  have hv' : ∃w : graph.Walk (liftAt a x) (liftAt b (encodeVec (decodeVec y))),w.length≤4 := hx ▸ hv
  exact hy ▸ hv'

theorem coset_walk_bound {K : Type*} (a b : Fin 192) (reference : List (Fin 5))
    (word : K → List (Fin 5)) (column : K → Fin 4 → Vec)
    (choice : Fin 81 → K) (alpha : Fin 81 → Vec)
    (hcol : ∀k j,routeVec (word k) 0 (basisVec j)=
      routeVec reference 0 (basisVec j)+routeVec (word k) (column k j) 0)
    (hcover : ∀z,routeVec (word (choice z)) (alpha z) 0=decodeVec z)
    (hcontroller : ∀k,routeController a (word k)=b)
    (hlength : ∀k,(word k).length≤4) (x y : Fin 81) :
    ∃w : graph.Walk (liftAt a x) (liftAt b y),w.length≤4 := by
  apply encoded_walk_to_finite a b _ x y
  intro vx vy
  obtain ⟨k,q,hq⟩ := coset_solution reference word column choice alpha hcol hcover vx vy
  exact walk_of_vector_endpoint a b (word k) q vx vy (hcontroller k) hq (hlength k)
theorem inverse_walk_bound (a b : Fin 192) (word : List (Fin 5))
    (inverseBasis : Fin 4 → Vec)
    (hbasis : ∀j,routeVec word (inverseBasis j) 0=basisVec j)
    (hcontroller : routeController a word=b) (hlength : word.length≤4) (x y : Fin 81) :
    ∃w : graph.Walk (liftAt a x) (liftAt b y),w.length≤4 := by
  apply encoded_walk_to_finite a b _ x y
  intro vx vy
  obtain ⟨q,hq⟩ := inverse_basis_solution word inverseBasis hbasis vx vy
  exact walk_of_vector_endpoint a b word q vx vy hcontroller hq hlength
#print axioms bounded_walk_of_route
#print axioms coset_walk_bound
#print axioms inverse_walk_bound
end DegreeDiameter.Portfolio.F3Graph15552
