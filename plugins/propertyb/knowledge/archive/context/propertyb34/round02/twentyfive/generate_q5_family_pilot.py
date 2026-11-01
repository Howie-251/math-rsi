from pathlib import Path
import json,sys
HERE=Path(__file__).resolve().parent;ROOT=HERE.parents[3];F=ROOT/'formal';S=ROOT/'context/propertyb34/round01/high-math'
sys.path.insert(0,str(HERE));from generate_q9_numeric import data_case,numeric_case
sys.path.insert(0,str(S));from unit_catalogue import fullblocks
from bare_layout import BareLayout
from fractions import Fraction
fs=lambda xs:'{'+','.join(map(str,xs))+'}' if xs else '∅'
tr=lambda t:fs([i for i in range(9) if t>>i&1]);li=lambda ts:'['+','.join(tr(t) for t in ts)+']'
d=json.loads((HERE/'Q5_COLORED_CERTIFICATES.json').read_text());fam=d['families'][60];row=next(r for r in d['rows'] if r['base']==60);target=row['target'];data=json.loads((S/'V25_NINE_Q5_BOUNDS.json').read_text())['results'][target];big=data['large_blocks'];full=fullblocks(big,9)
s='import Aris4Math.ThirtyFour.CachedCoefficients16\nimport Aris4Math.ThirtyFour.TwentyFiveConditionalRows\nimport Aris4Math.ThirtyFour.TwentyFiveSparseCompletion\nimport Aris4Math.ThirtyFour.TwentyFiveInventorySupport\nimport Aris4Math.ThirtyFour.CachedSparseApplication\n'
for name in ['TwentyFiveColoredActual','TwentyFiveColoredRows','TwentyFiveLowColorPruning','TwentyFiveColoredColoring','CachedChosenRows']:
 s+='\n'.join(l for l in (F/'Aris4Math/ThirtyFour'/f'{name}.lean').read_text().splitlines() if not l.startswith('import '))+'\n'
s+='''namespace Aris4Math.ThirtyFour.FiveLowFamilyPilot
open Aris4Math.ThirtyThree.MultiLockRecovery Aris4Math.K6Classification
open LocalProfiles CachedRows TwentyFiveUnitCounts TwentyFiveColoredActual
open TwentyFiveColoredColoring
open scoped BigOperators
set_option maxRecDepth 100000
set_option maxHeartbeats 0
'''
value,abc=BareLayout(25,data['positions']).bound({int(k):v for k,v in data['counts'].items()},True)
choices=[min(range(3),key=lambda i:row[i]) for row in abc]
assert value==Fraction(data['bound'])
s+=data_case(target,data,9)
template=(F/'Aris4Math/ThirtyFour/TwentyFiveCoefficientPilot.lean').read_text()
template=template[template.index('def locked'):template.index('/-- Only sparse')]
s+=f'namespace Case{target}\n'+template+f'end Case{target}\n'
s+=f'''namespace Case{target}
def choices : Fin 25 → Fin 3 := ![{','.join(map(str,choices))}]
set_option profiler true in
theorem value : CachedChosenRows.bound computed choices=({value.numerator}/{value.denominator} : ℚ) := by
  unfold CachedChosenRows.bound
  simp only [cachedA,cachedC,cachedDiagonal]
  simp_rw [aCoeff_eq,cCoeff_eq]
  decide +kernel
 theorem propertyB_of_counts (H : Simple5Hypergraph (Fin 25)) (f : Fin 9↪Fin 25)
    (counts : ∀ T,count H f T=μ T) : PropertyB H := by
  apply CachedSparseApplication.propertyB_of_sparse_counts H f positions labels labels_nodup μ support counts
  · rw [← p_eq_profile];exact valid
  · rw [← p_eq_profile,p_eq_computed]
    apply CachedChosenRows.strict computed choices
    rw [value];norm_num
end Case{target}
''' 
s+=f'''namespace Case{target}
def big : Finset (Finset (Fin 9)) := {fs([tr(t) for t in big])}
def full : List (Finset (Fin 9)) := {li(full)}
theorem completion : pairCompletion big=full.toFinset := by
  have same : big=({li(big)} : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  decide +kernel
theorem recovered (T : Finset (Fin 9)) : inventory 34 (standard 5) (pairCompletion big) T=μ T := by
  rw [completion]
  apply TwentyFiveInventorySupport.eq_of_support 34 (standard 5) full μ
  · intro U nonzero
    have member := support U nonzero
    have checked : labels.all (fun t => (TwentyFiveInventorySupport.labels full).contains t)=true := by decide +kernel
    exact List.contains_iff.mp (List.all_eq_true.mp checked U member)
  · decide +kernel
 theorem safe : Safe (standard 5) big := of_counts (standard 5) big μ recovered propertyB_of_counts
end Case{target}
'''
f='⟨'+li(fam['large_blocks'])+','+li(fam['full'])+','+fs(fam['eligible'])+',['+','.join(fs(x) for x in fam['lows'])+'],none⟩'
r='⟨Case'+str(target)+'.big,⟨'+li(fam['large_blocks'])+','+fs(row['low'])+',⟨0,!['+','.join(map(str,row['permutation']))+']⟩,none⟩⟩'
s+=f'''def family : TwentyFiveLowColorPruning.Family 9 := {f}
def rows : List (Row 9) := [{r}]
set_option profiler true in
theorem family_checked : TwentyFiveLowColorPruning.Check 5 family := by decide +kernel
set_option profiler true in
theorem rows_checked : rows.all (fun r => decide (Check 5 r))=true := by decide +kernel
theorem source_complete : rows.map source=family.lows.map (fun low => (family.listed.toFinset,low)) := by decide +kernel
 theorem rows_safe : ∀ r∈rows,Safe (standard 5) r.target := by
  intro r member
  simp only [rows,List.mem_singleton] at member
  subst r
  exact Case{target}.safe
 theorem family_safe (low : Finset (Fin 9)) (card : low.card=5)
    (feasible : Feasible 34 (colors low) (pairCompletion family.listed.toFinset)) :
    Safe (colors low) family.listed.toFinset := by
  apply from_rows 5 family.listed.toFinset family.lows rows source_complete rows_checked rows_safe low
  exact TwentyFiveLowColorPruning.low_mem 5 family family_checked low card feasible
#print axioms family_safe
end Aris4Math.ThirtyFour.FiveLowFamilyPilot
'''
(F/'FiveLowFamilyPilot.lean').write_text(s)
print('wrote complete source family',fam['base'],'using saved target',target)
