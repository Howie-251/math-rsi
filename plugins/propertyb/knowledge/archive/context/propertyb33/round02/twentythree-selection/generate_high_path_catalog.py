"""Generate the finite P3 catalog coverage proof from the fixed pair equations."""
from pathlib import Path
from itertools import combinations
ROOT=Path(__file__).resolve().parents[4]
large=[b for b in range(32) if b.bit_count()>=3]
pairs=list(combinations(range(5),2))
def fs(t):return '{'+','.join(str(i) for i in range(5) if t>>i&1)+'}'
vec='!['+','.join(fs(t) for t in large)+']'
lines=['import Aris4Math.ThirtyThree.TwentyThreeHighPathData','',
 '/-! Complete local Boolean-trace classification for P3 and P3+K2. -/',
 'namespace Aris4Math.ThirtyThree.TwentyThreeHighPathCatalog',
 'open scoped BigOperators','open TwentyThreeHighPathData (extra catalog counts)',
 'def largeTypes : Fin 16 → Finset (Fin 5) := '+vec,
 'theorem largeTypes_injective : Function.Injective largeTypes := by decide +kernel',
 'theorem largeTypes_card : ∀ a, 3 ≤ (largeTypes a).card := by decide +kernel',
 'theorem largeTypes_complete : ∀ T : Finset (Fin 5), 3 ≤ T.card → ∃ a, largeTypes a = T := by decide +kernel',
 'def pairDegree (e : Fin 2) (i j : Fin 5) : ℕ :=',
 '  if ({i,j} : Finset (Fin 5)) = {0,1} ∨ ({i,j} : Finset (Fin 5)) = {1,2} then 2 else',
 '  if ({i,j} : Finset (Fin 5)) = {3,4} then e.val+1 else 1',
 'def lowData (e : Fin 2) (T : Finset (Fin 5)) : ℕ :=',
 '  if T = ∅ then 33 else if T.card = 1 then 7 else',
 '  if T = {0,1} ∨ T = {1,2} then 2 else if T = {3,4} then e.val+1 else 1',
 'def highValue (h : Fin 16 → Bool) (T : Finset (Fin 5)) : ℕ :=',
 '  if ∃ a : Fin 16, largeTypes a = T ∧ h a = true then 1 else 0',
 'def pairSum (h : Fin 16 → Bool) (i j : Fin 5) : ℕ :=',
 '  ∑ a : Fin 16, if i ∈ largeTypes a ∧ j ∈ largeTypes a then',
 '    if h a then 1 else 0 else 0',
 'def Admissible (e : Fin 2) (h : Fin 16 → Bool) : Prop :=',
 '  ∀ i j : Fin 5, i ≠ j → pairSum h i j ≤ pairDegree e i j','',
 'def FastAdmissible (e : Fin 2) (h : Fin 16 → Bool) : Prop :=']
for k,(i,j) in enumerate(pairs):
 vals=['(if h '+str(a)+' then 1 else 0)' for a,t in enumerate(large) if t>>i&1 and t>>j&1]
 b='2' if (i,j) in ((0,1),(1,2)) else 'e.val+1' if (i,j)==(3,4) else '1'
 lines.append('  ('+' + '.join(vals)+' : ℕ) ≤ '+b+(' ∧' if k<9 else ''))
lines+=['','set_option maxHeartbeats 1000000 in',
 'theorem admissible_fast (e : Fin 2) (h : Fin 16 → Bool) (ha : Admissible e h) : FastAdmissible e h := by',
 '  unfold FastAdmissible','  refine ⟨?_,?_,?_,?_,?_,?_,?_,?_,?_,?_⟩']
for i,j in pairs:
 lines+=['  · have hb := ha '+str(i)+' '+str(j)+' (by decide)',
         '    norm_num [pairDegree] at hb',
         '    simp only [pairSum,Fin.sum_univ_succ] at hb',
         '    simpa [largeTypes,Nat.add_assoc] using hb']
bs=','.join('b'+str(i) for i in range(16));hs=','.join('h '+str(i) for i in range(16));ba=' '.join('b'+str(i) for i in range(16))
lines+=['','set_option maxHeartbeats 0 in','set_option maxRecDepth 100000 in',
 'theorem covers_vector : ∀ e : Fin 2, ∀ '+ba+' : Bool,',
 '    FastAdmissible e !['+bs+'] → ∃ s : Fin 115, extra s = e ∧',
 '      ∀ a, !['+bs+'] a = catalog s a := by',
 '  intro e','  fin_cases e <;> intro b0 b1 b2 b3 <;>',
 '    cases b0 <;> cases b1 <;> cases b2 <;> cases b3 <;>',
 '    unfold FastAdmissible <;> decide +kernel','',
 'theorem covers (e : Fin 2) (h : Fin 16 → Bool) (admissible : Admissible e h) :',
 '    ∃ s : Fin 115, extra s = e ∧ ∀ a, h a = catalog s a := by',
 '  have hv : !['+hs+'] = h := by funext a; fin_cases a <;> rfl',
 '  have bound := covers_vector e '+' '.join('(h '+str(i)+')' for i in range(16)),
 '  rw [hv] at bound','  exact bound (admissible_fast e h admissible)','',
 'set_option maxHeartbeats 0 in','set_option maxRecDepth 100000 in',
 'theorem catalog_counts : ∀ s T, 3 ≤ T.card → highValue (catalog s) T = counts s T := by',
 '  intro s','  fin_cases s <;> decide +kernel','',
 'set_option maxHeartbeats 0 in','set_option maxRecDepth 100000 in',
 'theorem recovery_formula : ∀ s T,',
 '    MultiLockRecovery.recovered (lowData (extra s)) (counts s) T = counts s T := by',
 '  intro s','  fin_cases s <;> decide +kernel','',
 'end Aris4Math.ThirtyThree.TwentyThreeHighPathCatalog','']
(ROOT/'formal/Aris4Math/ThirtyThree/TwentyThreeHighPathCatalog.lean').write_text('\n'.join(lines))
print('Generated full local Boolean coverage and recovery formula obligations.')
