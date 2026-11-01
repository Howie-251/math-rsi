"""Export all q5 witnesses using direct target theorem names, no global lookup.
All placements are the existing paper certificates. This is source generation;
every produced theorem still requires ordinary Lean kernel verification.
"""
from pathlib import Path
from fractions import Fraction
import sys,json
HERE=Path(__file__).resolve().parent;ROOT=HERE.parents[3];F=ROOT/'formal/Aris4Math/ThirtyFour';S=ROOT/'context/propertyb34/round01/high-math'
sys.path.insert(0,str(HERE));from generate_q9_numeric import data_case
sys.path.insert(0,str(S));from bare_layout import BareLayout
from unit_catalogue import fullblocks
q5=json.loads((S/'V25_NINE_Q5_BOUNDS.json').read_text())['results'];cert=json.loads((HERE/'Q5_COLORED_CERTIFICATES.json').read_text())
assert len(q5)==11692
fs=lambda xs:'{'+','.join(map(str,xs))+'}' if xs else '∅'
tr=lambda t:fs([i for i in range(9) if t>>i&1]);li=lambda ts:'['+','.join(tr(t) for t in ts)+']'
ns='Aris4Math.ThirtyFour.TwentyFiveFiveLow'
header=f'''namespace {ns}
open Aris4Math.ThirtyThree.MultiLockRecovery Aris4Math.K6Classification
open LocalProfiles CachedRows TwentyFiveUnitCounts TwentyFiveColoredActual
open TwentyFiveColoredColoring
open scoped BigOperators
set_option maxRecDepth 100000
set_option maxHeartbeats 0
'''
tail=f'end {ns}\n'
size=24;numeric=[];inventory=[];datas=[];record=[]
for start in range(0,len(q5),size):
 j=start//size;batch=q5[start:start+size]
 dn=f'TwentyFiveFiveLowData{j}';iv=f'TwentyFiveFiveLowInventory{j}';nu=f'TwentyFiveFiveLowNumeric{j}'
 datas.append(dn);inventory.append(iv);numeric.append(nu)
 ds='import Aris4Math.ThirtyFour.CachedSparseApplication\nimport Aris4Math.ThirtyFour.TwentyFiveColoredColoring\n'+header
 ins=f'import Aris4Math.ThirtyFour.{dn}\n'+header
 nus=f'import Aris4Math.ThirtyFour.{iv}\nimport Aris4Math.ThirtyFour.CachedChosenRows\n'+header
 for row in batch:
  c=row['id'];big=row['large_blocks'];full=fullblocks(big,9)
  ds+=data_case(c,row,9)
  ds+=f'namespace Case{c}\ndef big : Finset (Finset (Fin 9)) := {fs([tr(t) for t in big])}\ndef full : List (Finset (Fin 9)) := {li(full)}\nend Case{c}\n'
  ins+=f'''namespace Case{c}
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
end Case{c}
'''
  value,abc=BareLayout(25,row['positions']).bound({int(k):v for k,v in row['counts'].items()},True)
  assert value==Fraction(row['bound']) and value<1,(c,value,row['bound'])
  choice=[min(range(3),key=lambda i:r[i]) for r in abc]
  record.append(dict(id=c,choices=choice,value=str(value)))
  nus+=f'''namespace Case{c}
def choices : Fin 25 → Fin 3 := ![{','.join(map(str,choice))}]
theorem value : CachedChosenRows.bound computed choices=({value.numerator}/{value.denominator} : ℚ) := by decide +kernel
 theorem propertyB_of_counts (H : Simple5Hypergraph (Fin 25)) (f : Fin 9↪Fin 25)
    (counts : ∀ T,count H f T=μ T) : PropertyB H := by
  apply CachedSparseApplication.propertyB_of_sparse_counts H f positions labels labels_nodup μ support counts
  · rw [← p_eq_profile];exact valid
  · rw [← p_eq_profile,p_eq_computed]
    apply CachedChosenRows.strict computed choices
    rw [value];norm_num
 theorem safe : Safe (standard 5) big := of_counts (standard 5) big μ recovered propertyB_of_counts
end Case{c}
'''
 (F/f'{dn}.lean').write_text(ds+tail);(F/f'{iv}.lean').write_text(ins+tail);(F/f'{nu}.lean').write_text(nus+tail)
source_groups={c:[] for c in range(374)}
for row in cert['rows']:source_groups[row['base']].append(row)
families=[]
for fam in cert['families']:
 c=fam['base'];name=f'TwentyFiveFiveLowFamily{c}';families.append(name);group=source_groups[c]
 targetids=sorted({row.get('target',0) for row in group})
 dependencies=sorted({i//size for i in targetids})
 s='import Aris4Math.ThirtyFour.TwentyFiveColoredColoring\n'+''.join(f'import Aris4Math.ThirtyFour.TwentyFiveFiveLowNumeric{j}\n' for j in dependencies)
 s+=header+f'namespace Family{c}\n'
 if 'rejection' in fam:
  no=fam['rejection'];rejection='some ⟨'+li(fam['large_blocks'])+','+li(no['incident'])+','+str(no['vertex'])+'⟩'
  family='⟨'+li(fam['large_blocks'])+',[],∅,[],'+rejection+'⟩'
 else:family='⟨'+li(fam['large_blocks'])+','+li(fam['full'])+','+fs(fam['eligible'])+',['+','.join(fs(low) for low in fam['lows'])+'],none⟩'
 s+=f'def family : TwentyFiveLowColorPruning.Family 9 := {family}\n'
 s+='theorem checked : decide (TwentyFiveLowColorPruning.Check 5 family)=true := by decide +kernel\n'
 if group:
  data=[]
  for row in group:
   target=row.get('target',0)
   if 'target' in row:witness='⟨0,!['+','.join(map(str,row['permutation']))+']⟩';rejection='none'
   else:witness='⟨0,![0,1,2,3,4,5,6,7,8]⟩';rejection='some (.inr '+li(row['rejection']['full'])+')'
   data.append('⟨Case'+str(target)+'.big,⟨'+li(fam['large_blocks'])+','+fs(row['low'])+','+witness+','+rejection+'⟩⟩')
  s+='def rows : List (Row 9) := ['+',\n'.join(data)+']\n'
  s+='theorem rows_checked : rows.all (fun r => decide (Check 5 r))=true := by decide +kernel\n'
  s+='theorem source_complete : rows.map source=family.lows.map (fun low => (family.listed.toFinset,low)) := by decide +kernel\n'
  s+='theorem rows_safe : ∀ r∈rows,Safe (standard 5) r.target := by\n  simp only [rows,List.forall_mem_cons]\n'
  if len(group)==1:s+=f"  exact ⟨Case{group[0].get('target',0)}.safe,List.forall_mem_nil _⟩\n"
  else:s+='  exact ⟨'+','.join(f"Case{row.get('target',0)}.safe" for row in group)+',List.forall_mem_nil _⟩\n'
  s+='''theorem safe : ∀ low∈family.lows,Safe (colors low) family.listed.toFinset :=
  from_rows 5 family.listed.toFinset family.lows rows source_complete rows_checked rows_safe
'''
 else:s+='''theorem safe : ∀ low∈family.lows,Safe (colors low) family.listed.toFinset := by
  simp only [family,List.not_mem_nil,IsEmpty.forall_iff,implies_true]
'''
 s+=f'end Family{c}\n'+tail;(F/f'{name}.lean').write_text(s)
name='TwentyFiveFiveLowComplete'
s=''.join(f'import Aris4Math.ThirtyFour.{f}\n' for f in families)
s+='import Aris4Math.ThirtyFour.TwentyFiveUnit9Actual\nimport Aris4Math.ThirtyFour.TwentyFiveSelection\n'+header
s+='def families : List (TwentyFiveLowColorPruning.Family 9) := ['+','.join(f'Family{c}.family' for c in range(374))+']\n'
s+='''theorem sources : families.map (fun r => r.listed.toFinset)=List.ofFn TwentyFiveUnit9Data.catalogue := by decide +kernel
theorem checked : families.all (fun r => decide (TwentyFiveLowColorPruning.Check 5 r))=true := by
  simp only [families,List.all_cons,List.all_nil,'''+','.join(f'Family{c}.checked' for c in range(374))+''',Bool.true_and]
theorem safe : ∀ r∈families,∀ low∈r.lows,Safe (colors low) r.listed.toFinset := by
  simp only [families,List.forall_mem_cons]
  exact ⟨'''+','.join(f'Family{c}.safe' for c in range(374))+''',List.forall_mem_nil _⟩
theorem propertyB (H : Simple5Hypergraph (Fin 25)) (edges : H.edges.card=34)
    (selection : TwentyFiveSelection.MixedLocks H 5 4) : PropertyB H := by
  obtain ⟨f,degrees,unit⟩ := selection
  exact TwentyFiveColoredColoring.actual H edges f unit 5 degrees (by decide +kernel)
    TwentyFiveUnit9Data.catalogue TwentyFiveUnit9Actual.actual
    (pruned_table TwentyFiveUnit9Data.catalogue families sources 5 checked safe)
'''+tail+f'#print axioms {ns}.propertyB\n';(F/f'{name}.lean').write_text(s)
manifest=dict(cases=len(q5),numeric_group_size=size,data=datas,inventory=inventory,numeric=numeric,families=families,aggregate=name,
 source_colorings=23759,feasible=23507,rejected_budget=252,rejected_whole_families=65)
(HERE/'Q5_DIRECT_BUILD_MANIFEST.json').write_text(json.dumps(manifest,indent=2)+'\n')
(HERE/'Q5_SELECTED_ROW_CERTIFICATES.json').write_text(json.dumps(record,indent=2)+'\n')
print(json.dumps({k:v for k,v in manifest.items() if not isinstance(v,list)}))
