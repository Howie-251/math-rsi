import ES7BalancedExtensions
import ES7PathSemantics

namespace ES7OrderedPaths
open ES8ActualRanks ES8ResidualRanks ES8BalancedGeometry ES7BalancedEndpoints

/-- Suffix shortening retains the exact ending pair. -/
theorem ending_truncate {cup color u v len} (p : EndingPath cup color u v len)
    (m : Nat) (lo : 2≤m) (hi : m≤len) : EndingPath cup color u v m := by
  induction p generalizing m with
  | pair huv =>
    have he : m=2 := by omega
    subst m
    exact .pair huv
  | @step t u v len path huv same ih =>
    by_cases h : m=2
    · subst m; exact .pair huv
    · have small := ih (m-1) (by omega) (by omega)
      have he : m-1+1=m := by omega
      simpa only [he] using EndingPath.step small huv same

theorem starting_of_cup {n cup color u v} (xs : List Nat)
    (chain : (colorConfig cup color).Cup (u::v::xs))
    (inside : (u::v::xs).In (Finset.range n)) :
    StartingPath n cup color u v (xs.length+2) := by
  induction xs generalizing u v with
  | nil =>
    exact .pair (Config.Cup.pair.mp chain) (Finset.mem_range.mp (inside v (by simp)))
  | cons w xs ih =>
    obtain ⟨uv,same,tail⟩ := Config.Cup.cons3.mp chain
    have tailin : (v::w::xs).In (Finset.range n) := fun a ha => inside a (List.mem_cons_of_mem u ha)
    have step := StartingPath.step (ih tail tailin) uv same
    simpa only [List.length_cons,Nat.add_assoc,Nat.add_comm,Nat.add_left_comm] using step

/-- Join two actual chains sharing their exact pair. Chronology makes all
remaining vertices distinct; no disjointness hypothesis is imposed. -/
theorem join_pair {n cup color u v r} (future : StartingPath n cup color u v r)
    {l} (past : EndingPath cup color u v l) :
    ∃ a b, b<n ∧ EndingPath cup color a b (l+r-2) := by
  induction future generalizing l with
  | @pair u v uv vn => exact ⟨u,v,vn,by simpa using past⟩
  | @step u v w len future uv same ih =>
    have vw := (path_bounds future).2.2.1
    obtain ⟨a,b,bn,joined⟩ := ih (EndingPath.step past vw same)
    refine ⟨a,b,bn,?_⟩
    convert joined using 1 <;> omega

theorem ending_forbidden {n cup color u v k}
    (noChain : ¬(colorConfig cup color).HasNCup k (Finset.range n))
    (vn : v<n) (p : EndingPath cup color u v k) : False := by
  obtain ⟨xs,len,chain,bounded⟩ := ES8ActualRanks.list_witness p
  exact noChain ⟨xs++[u,v],⟨chain,len⟩,fun a ha => Finset.mem_range.mpr (by have := bounded a ha; omega)⟩

theorem starting_forbidden {n cup color u v k}
    (noChain : ¬(colorConfig cup color).HasNCup k (Finset.range n))
    (p : StartingPath n cup color u v k) : False := by
  obtain ⟨xs,len,chain,inside⟩ := ES8ResidualRanks.list_witness p
  exact noChain ⟨u::v::xs,⟨chain,len⟩,inside⟩

theorem pair_budget {n cup color u v l r}
    (noSix : NoSix cup (Finset.range n)) (total : l+r=8)
    (past : EndingPath cup color u v l)
    (future : StartingPath n cup color u v r) : False := by
  obtain ⟨a,b,bn,path⟩ := join_pair future past
  have len : l+r-2=6 := by omega
  rw [len] at path
  exact ending_forbidden (noSix color) bn path

theorem triple_budget {n cup color u v w l r}
    (noSix : NoSix cup (Finset.range n)) (total : l+r=7)
    (past : EndingPath cup color u v l)
    (future : StartingPath n cup color v w r) (same : cup u v w=color) : False := by
  have vw := (path_bounds future).2.2.1
  exact pair_budget noSix (by omega) (EndingPath.step past vw same) future

theorem selected_path_rank {cup color s u v k}
    (p : ES7PathSemantics.Path cup color s u v k) : EndingPath cup color u v k := by
  obtain ⟨xs,first,len,chain⟩ := p
  have result := ES8SlopePartition.ending_of_cup cup color xs u v chain
  have eq : xs.length+2=k := by simpa using len
  simpa only [eq] using result

/-- Both possible weak-heptagon path lengths are covered with their common
actual endpoints, including overlapping interior witnesses. -/
theorem weak_heptagon {n} (c : Configuration n) {s v a b}
    (vn : v<n) (ha : 2≤a) (hb : 2≤b) (total : a+b=9)
    (cup : ES7PathSemantics.Endpoint c.cup true s v a)
    (cap : ES7PathSemantics.Endpoint c.cup false s v b) :
    ES7Geometry.HasConvexHeptagon (Set.range c.point) := by
  obtain ⟨u,xs,xfirst,xlen,xchain⟩ := cup
  obtain ⟨t,ys,yfirst,ylen,ychain⟩ := cap
  apply ES7Geometry.hasNGon_heptagon c
  refine ⟨ys++[t,v],xs++[u,v],⟨?_,by omega⟩,
    ES7PathSemantics.path_inside c.cup false ychain vn,
    ES7PathSemantics.path_inside c.cup true xchain vn⟩
  refine ⟨by omega,(false_cup_iff_cap _ _).mp ychain,by omega,xchain,?_,?_⟩
  · exact yfirst.trans xfirst.symm
  · simp

end ES7OrderedPaths
