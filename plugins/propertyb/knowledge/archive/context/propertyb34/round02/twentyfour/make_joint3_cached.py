from pathlib import Path
import json
from fractions import Fraction as Q
root=Path(__file__).resolve().parents[4]; out=root/'formal/Aris4Math/ThirtyFour'; here=Path(__file__).resolve().parent
old=(out/'TwentyThreeFiveLowStrictJoint3Numeric.lean').read_text()
prefix=old[:old.index('theorem strict :')].replace('import Aris4Math.ThirtyFour.TwentyThreeFiveLowStrictJoint3Data','import Aris4Math.ThirtyFour.TwentyThreeFiveLowStrictJoint3Data\nimport Aris4Math.ThirtyFour.CachedRows').replace('TwentyThreeFiveLowStrictJoint3Numeric','TwentyThreeFiveLowStrictJoint3CachedNumeric')
prefix+='''
def cachedFree (l : Layout) : ℚ :=
  ∑ k ∈ Finset.univ.filter (fun k : Fin 23 => ¬ ∃ j, positions l j = k),
    min (CachedRows.cachedA (p l) (k.val+1) true)
      (min (CachedRows.cachedA (p l) (k.val+1) false) (CachedRows.cachedC (p l) (k.val+1)))
def cachedCenterA (l : Layout) (j : Fin 5) : ℚ :=
  min (CachedRows.cachedA (p l) ((positions l j).val+1) true)
    (CachedRows.cachedA (p l) ((positions l j).val+1) false)
def cachedCenterC (l : Layout) (j : Fin 5) : ℚ :=
  CachedRows.cachedC (p l) ((positions l j).val+1)

theorem free_eq (l : Layout) : free (positions l) (p l) = cachedFree l := by
  unfold free cachedFree
  apply Finset.sum_congr rfl
  intro k hk
  obtain ⟨ha,hb,hc⟩ := CachedRows.rows_eq (p l) 34 (k.val+1)
    (data_valid.2.1 l) (data_valid.2.2.1 l)
  rw [ha,hb,hc]
theorem a_eq (l : Layout) (j : Fin 5) : a positions p l j = cachedCenterA l j := by
  unfold a cachedCenterA
  obtain ⟨ha,hb,hc⟩ := CachedRows.rows_eq (p l) 34 ((positions l j).val+1)
    (data_valid.2.1 l) (data_valid.2.2.1 l)
  rw [ha,hb]
theorem c_eq (l : Layout) (j : Fin 5) : c positions p l j = cachedCenterC l j := by
  exact (CachedRows.rows_eq (p l) 34 ((positions l j).val+1)
    (data_valid.2.1 l) (data_valid.2.2.1 l)).2.2
'''
end='end Aris4Math.ThirtyFour.TwentyThreeFiveLowStrictJoint3CachedNumeric\n'
(here/'Joint3CachedAPIProbe.lean').write_text(prefix+end)
x=json.loads((here/'JOINT3_SOURCE.json').read_text());scale=x['scale']
def rat(q):
 q=Q(q);return f'({q.numerator}/{q.denominator}:ℚ)'
for l in [0,13]:
 z=x['layouts'][l]
 exp=rat(Q(z['free'],scale))
 for label,expr in [('cached',f'cachedFree {l}'),('old',f'free (positions {l}) (p {l})')]:
  code=f'example : {expr} = {exp} := by\n  simp only [cachedFree,p_eq_computed]\n  decide +kernel\n'
  (here/f'Joint3Free{l}{label}Probe.lean').write_text(prefix+code+end)
 # First five exact center rows.
 code=''
 for j in range(5):
  code+=f'example : cachedCenterA {l} {j} = {rat(Q(z["centers"][j]["a"],scale))} ∧ cachedCenterC {l} {j} = {rat(Q(z["centers"][j]["c"],scale))} := by\n  simp only [cachedCenterA,cachedCenterC,p_eq_computed]\n  decide +kernel\n'
 (here/f'Joint3Centers{l}Probe.lean').write_text(prefix+code+end)
# One center exact penalty, all20 mixed weights, unchanged semantics.
pen=sum((Q(p)*s['capacity'] for p,s in zip(x['penalties'],x['slots']) if s['center']==0),Q())
code=f'example : penalty support μ beta (weights positions p) 0 (R 0) (delta 0) = {rat(pen)} := by\n  simp only [LocalProfiles.weights_eq,p_eq_computed]\n  decide +kernel\n'
(here/'Joint3Penalty0Probe.lean').write_text(prefix+code+end)
strict=old[old.index('theorem strict :'):old.index('end Aris4Math.')]
cs=strict.replace('theorem strict :','theorem cached_strict :').replace('free (positions l) (p l)','cachedFree l').replace('a positions p l j','cachedCenterA l j').replace('c positions p l j','cachedCenterC l j').replace('[LocalProfiles.weights_eq,p_eq_computed]','[cachedFree,cachedCenterA,cachedCenterC,LocalProfiles.weights_eq,p_eq_computed]')
orig=strict[:strict.index(' := by')]+''' := by
  simpa only [free_eq,a_eq,c_eq] using cached_strict
'''
(out/'TwentyThreeFiveLowStrictJoint3CachedNumeric.lean').write_text(prefix+cs+orig+end+'#print axioms Aris4Math.ThirtyFour.TwentyThreeFiveLowStrictJoint3CachedNumeric.strict\n')
print('created cached Numeric and bounded probes; original Numeric untouched')
