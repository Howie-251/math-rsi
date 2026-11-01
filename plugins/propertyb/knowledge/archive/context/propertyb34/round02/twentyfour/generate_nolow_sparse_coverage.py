from pathlib import Path
import json
HERE=Path(__file__).resolve().parent
old=HERE/'generate_nolow_coverage.py';env={'__file__':str(old)}
exec(compile(old.read_text().split("s='''import")[0],str(old),'exec'),env)
ROOT=env['ROOT'];OUT=ROOT/'formal/Aris4Math/ThirtyFour';profiles=env['rows'];fs=env['fs'];vec=env['vec'];hi=env['hi'];pairs=env['pairs'];lookup=env['lookup']

def enumerate_values(b):
 def rec(i,cap):
  if i==len(hi):return [()]
  out=[]
  cost=[int(p&hi[i]==p) for p in pairs]
  for k in (0,1):
   if all(k*c<=v for c,v in zip(cost,cap)):
    out.extend((k,)+tail for tail in rec(i+1,tuple(v-k*c for c,v in zip(cost,cap))))
  return out
 return rec(0,tuple(2 if b and j==0 else 1 for j in range(15)))
rows=[]
for b in (False,True):
 values=enumerate_values(b);assert len(values)==[352,467][b]
 rs=[]
 for v in values:
  code=sum(k*(2**j) for j,k in enumerate(v));assert code in lookup[b]
  i,pi=lookup[b][code];rs.append((v,i,pi))
 assert len(rs)==len(lookup[b]);rows.append(rs)

s='''import Aris4Math.ThirtyFour.TwentyFourNoLowCoverageData
import Aris4Math.ThirtyFour.TwentyFourSparseDecode
namespace Aris4Math.ThirtyFour.TwentyFourNoLowCoverage
open TwentyFourNoLowSixData
open TwentyFourSparseDecode
set_option maxRecDepth 100000
set_option maxHeartbeats 0
'''
s+='def profileHigh : Case→Finset (Finset (Fin 6)) := '+vec('{'+','.join(fs(int(t)) for t,v in r['counts'].items() if int(t).bit_count()>=3 and v)+'}' if any(int(t).bit_count()>=3 and v for t,v in r['counts'].items()) else '∅' for r in profiles)+'\n'
s+='''/-- One actual local vector and its concrete matching witness. The order
agrees with the complete capacity-pruned catalogue, not a hash lookup. -/
abbrev Row := ℕ×(Case×Perm)
def rowValues (r : Row) : List ℕ := (List.range 41).map (fun i=>if r.1.testBit i then 1 else 0)
def rows : Bool→List Row
'''
for b,name in [(False,'false'),(True,'true')]:
 s+='  | '+name+' => ['+','.join(f'({sum(k*(2**j) for j,k in enumerate(v))},({i},{pi}))' for v,i,pi in rows[b])+']\n'
s+='''def CheapMatch (b : Bool) (values : List ℕ) (selected : Case×Perm) : Prop :=
  (∀k∈values,k≤1) ∧ extraPair selected.1=b ∧
  (b=true→({0,1} : Finset (Fin 6)).map (perm selected.2).toEmbedding={0,1}) ∧
  support entries values=(profileHigh selected.1).image (fun T=>T.map (perm selected.2).toEmbedding)
instance (b : Bool) (values : List ℕ) (selected : Case×Perm) : Decidable (CheapMatch b values selected) := by unfold CheapMatch;infer_instance
end Aris4Math.ThirtyFour.TwentyFourNoLowCoverage
'''
(OUT/'TwentyFourNoLowSparseData.lean').write_text(s)
fragment=(HERE/'sparse_bridge_fragment.txt').read_text()
s='''import Aris4Math.ThirtyFour.TwentyFourNoLowSparseData
namespace Aris4Math.ThirtyFour.TwentyFourNoLowCoverage
open TwentyFourNoLowSixData
open TwentyFourSparseDecode
set_option maxHeartbeats 0
set_option maxRecDepth 100000
'''+fragment+'\nend Aris4Math.ThirtyFour.TwentyFourNoLowCoverage\n'
(OUT/'TwentyFourNoLowSparseBridge.lean').write_text(s)
s='''import Aris4Math.ThirtyFour.TwentyFourNoLowSparseBridge
namespace Aris4Math.ThirtyFour.TwentyFourNoLowCoverage
open TwentyFourNoLowSixData
set_option maxHeartbeats 0
set_option maxRecDepth 100000

/-- Exact equality with the complete bounded domain, checked once. -/
theorem rows_cover_false : (rows false).map rowValues=catalogue false := by decide +kernel
theorem rows_cover_true : (rows true).map rowValues=catalogue true := by decide +kernel
theorem rows_cover (b : Bool) : (rows b).map rowValues=catalogue b := by
  cases b
  · exact rows_cover_false
  · exact rows_cover_true

theorem rows_correct_false : ∀r∈rows false,CheapMatch false (rowValues r) r.2 := by decide +kernel
theorem rows_correct_true : ∀r∈rows true,CheapMatch true (rowValues r) r.2 := by decide +kernel
theorem rows_correct (b : Bool) : ∀r∈rows b,CheapMatch b (rowValues r) r.2 := by
  cases b
  · exact rows_correct_false
  · exact rows_correct_true

/-- Every complete-domain input has a genuine matching witness. Sparse
support equality is lifted to all high traces by the generic decoder proof. -/
theorem coverage (b : Bool) (values : List ℕ) (member : values∈catalogue b) :
    ∃selected : Case×Perm,
      (∀T,T.card≤2→low b (T.map (perm selected.2).toEmbedding)=upper selected.1 T) ∧
      (∀T,3≤T.card→vector values (T.map (perm selected.2).toEmbedding)=μ selected.1 T) := by
  have inrows : values∈(rows b).map rowValues := by rw [rows_cover];exact member
  obtain ⟨r,hr,eq⟩ := List.mem_map.mp inrows
  rw [← eq]
  exact ⟨r.2,cheap_correct b (rowValues r) r.2 (rows_correct b _ hr)⟩
end Aris4Math.ThirtyFour.TwentyFourNoLowCoverage
#print axioms Aris4Math.ThirtyFour.TwentyFourNoLowCoverage.coverage
'''
(OUT/'TwentyFourNoLowCoverageKernel.lean').write_text(s)
print('Complete sparse witness domains',list(map(len,rows)))
(HERE/'SPARSE_COVERAGE_GENERATION.json').write_text(json.dumps({'domain_sizes':list(map(len,rows)),'source':'V24_NO_SIX_CERTIFICATES.json','method':'ordered rows, exact full-domain equality, sparse support matching'},indent=2)+'\n')
