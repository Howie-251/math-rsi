from pathlib import Path
p=Path(__file__).with_name('generate_low_promotions.py');s=p.read_text()
backup=p.with_name('generate_low_promotions_explicit_rows.py')
if not backup.exists():backup.write_text(s)
s=s.replace('records=[];stats=[];catalogues=[]','records=[];stats=[];catalogues=[];metadata=[]')
s=s.replace('  feasible=survive=0','  feasible=survive=0;catmeta=[]')
s=s.replace('''   if any(co[i][j]<1 for i in range(n+1)for j in range(n+1)if i!=j):continue
   if any(sum(co[i][j]-1 for j in range(n+1)if i!=j)>2 for i in range(n+1)):continue''','''   badpair=next(((i,j)for i in range(n+1)for j in range(n+1)if i!=j and co[i][j]<1),None)
   if badpair is not None:
    catmeta.append(('zeroPair',badpair));continue
   badcenter=next((i for i in range(n+1)if sum(co[i][j]-1 for j in range(n+1)if i!=j)>2),None)
   if badcenter is not None:
    catmeta.append(('excess',badcenter));continue''')
s=s.replace('   records.append((code,(bad or 0,q,perm)))','''   records.append((code,(bad or 0,q,perm)))
   catmeta.append(('projection',(bad,dict(out)))if bad is not None else('matched',(q,perm)))''')
s=s.replace('  stats.append(dict(source=c','  metadata.append(catmeta)\n  stats.append(dict(source=c')
s=s.replace('import Aris4Math.ThirtyFour.TwentyThreeLowPromotionBase\nnamespace','import Aris4Math.ThirtyFour.TwentyThreeLowPromotionBase\nimport Aris4Math.ThirtyFour.TwentyThreeSparseTrace\nnamespace',1)
a=s.index(' witness_lookup=dict(records)');b=s.index(" s+=f'abbrev Witness",a)
s=s[:a]+''' rowlists=[]
 for c,(cat,mds)in enumerate(zip(catalogues,metadata)):
  rs=[]
  for vs,(kind,meta)in zip(cat,mds):
   if kind=='zeroPair':reason=f'.zeroPair {meta[0]} {meta[1]}'
   elif kind=='excess':reason=f'.excess {meta}'
   elif kind=='projection':
    x,out=meta;traces='['+','.join(f'({fs(t,n+1)},{m})'for t,m in sorted(out.items())if m)+']'
    reason=f'.projection {x} {traces}'
   else:reason=f'.matched {meta[0]} {dense[meta[1]]}'
   rs.append('(['+','.join(map(str,vs))+'], '+reason+')')
  rowlists.append('[\\n'+',\\n'.join(rs)+'\\n]')
'''+s[b:]
pos=s.index('def catalogue (c : OldCase)')
base='''inductive Reason where
  | zeroPair (i j : Fin {n+1})
  | excess (i : Fin {n+1})
  | projection (x : Fin {n+1}) (traces : TwentyThreeSparseTrace.TraceList {n+1})
  | matched (q : NewCase) (p : NewPerm)

'''
# Split the f-string around a n-dependent definition block.
s=s[:pos]+base+s[pos:]
# Additional declarations come after replacements have introduced expected/OldResidual.
pos=s.index(" write_changed(OUT/f'{prefix}Data.lean',s)")
addition=''' if n==4:
  fastcondition='∃ r : OldCase, ∀ k : Fin 5, ∀ p : Fin 2, TwentyThreeSparseTrace.moment xs k p=expected r k p'
  bridge=\'''  obtain ⟨r,h⟩ := h
  refine ⟨r,?_⟩
  intro k p
  rw [TwentyThreeSparseTrace.moment_eq]
  exact h k p
\'''
 else:
  fastcondition='∃ r : OldCase, ∀ k : Fin 6, TwentyThreeSparseTrace.moment xs k 0=expected r k'
  bridge=\'''  obtain ⟨r,h⟩ := h
  refine ⟨r,?_⟩
  intro k
  rw [TwentyThreeSparseTrace.moment_zero_eq_cardMass]
  exact h k
\'''
 decl=f\'''def SparseResidual (xs : TwentyThreeSparseTrace.TraceList {n}) : Prop := {fastcondition}
noncomputable instance (xs : TwentyThreeSparseTrace.TraceList {n}) : Decidable (SparseResidual xs) := by
  unfold SparseResidual
  infer_instance

theorem sparseResidual_of_old (xs : TwentyThreeSparseTrace.TraceList {n})
    (h : OldResidual (TwentyThreeSparseTrace.counts xs)) : SparseResidual xs := by
{bridge}
def rowValid (c : OldCase) (values : List ℕ) : Reason → Prop
  | .zeroPair i j => i≠j ∧ TwentyThreeLowPromotionBase.co (newCounts c values) i j=0
  | .excess i => 2 < ∑ j ∈ Finset.univ.erase i,
      (TwentyThreeLowPromotionBase.co (newCounts c values) i j-1)
  | .projection x traces =>
      (∀ T, newCounts c values T=TwentyThreeSparseTrace.counts traces T) ∧
      ¬ SparseResidual (TwentyThreeSparseTrace.projected (deletion x) traces)
  | .matched q p => ∀ T,
      newCounts c values (T.map (newPerm p).toEmbedding)=μ q T
noncomputable instance (c : OldCase) (values : List ℕ) (reason : Reason) :
    Decidable (rowValid c values reason) := by
  cases reason <;> unfold rowValid <;> infer_instance

theorem rowValid_covered (c : OldCase) (values : List ℕ) (reason : Reason)
    (valid : rowValid c values reason) : covered c values := by
  cases reason with
  | zeroPair i j =>
    refine ⟨(0,0,0),?_⟩
    intro feasible _ T
    have pos := feasible.1 i j valid.1
    rw [valid.2] at pos
    omega
  | excess i =>
    refine ⟨(0,0,0),?_⟩
    intro feasible _ T
    have bound := feasible.2 i
    exact (Nat.not_lt_of_ge bound valid).elim
  | projection x traces =>
    refine ⟨(x,0,0),?_⟩
    intro _ old T
    have same : projected x (newCounts c values)=
        TwentyThreeSparseTrace.counts (TwentyThreeSparseTrace.projected (deletion x) traces) := by
      funext U
      rw [TwentyThreeSparseTrace.projected_counts]
      unfold projected
      simp_rw [valid.1]
    have old' : OldResidual (TwentyThreeSparseTrace.counts
        (TwentyThreeSparseTrace.projected (deletion x) traces)) := by
      rwa [← same]
    exact (valid.2 (sparseResidual_of_old _ old')).elim
  | matched q p =>
    exact ⟨(0,q,p),fun _ _ T => valid T⟩

\'''
 end=f'end Aris4Math.ThirtyFour.{prefix}\\n'
 s=s.removesuffix(end)+decl+end
'''
s=s[:pos]+addition+s[pos:]
s=s.replace('def rows{c} : List (List ℕ × Witness)', 'def rows{c} : List (List ℕ × Reason)')
s=s.replace('decide (rowCovered {c} row.1 row.2)','decide (rowValid {c} row.1 row.2)')
s=s.replace('  exact ⟨row.2,of_decide_eq_true (List.all_eq_true.mp row_coverage{c} row member)⟩','  exact rowValid_covered {c} row.1 row.2 (of_decide_eq_true (List.all_eq_true.mp row_coverage{c} row member))')
p.write_text(s)
