from pathlib import Path
import json
HERE=Path(__file__).resolve().parent
old=HERE/'generate_sixlow_bad_coverage.py';env={'__file__':str(old)}
exec(compile(old.read_text().split("s='''import")[0],str(old),'exec'),env)
ROOT=env['ROOT'];OUT=ROOT/'formal/Aris4Math/ThirtyFour';profiles=env['rows'];fs=env['fs'];vec=env['vec'];hi=env['hi'];pairs=env['pairs'];lookup=env['lookup']

def enumerate_values(b):
 def rec(i,cap):
  if i==len(hi):return [()]
  out=[];cost=[int(p&hi[i]==p) for p in pairs]
  for k in (0,1):
   if all(k*c<=v for c,v in zip(cost,cap)):
    out.extend((k,)+tail for tail in rec(i+1,tuple(v-k*c for c,v in zip(cost,cap))))
  return out
 return rec(0,tuple(2 if mask in [3,12,48][:b+1] else 1 for mask in pairs))
rows=[]
for b in range(3):
 values=enumerate_values(b);assert len(values)==[467,611,787][b]
 rs=[]
 for v in values:
  code=sum(k*(2**j) for j,k in enumerate(v));assert code in lookup[b]
  i,pi=lookup[b][code];rs.append((code,i,pi))
 assert len(rs)==len(lookup[b]);rows.append(rs)
s='''import Aris4Math.ThirtyFour.TwentyFourSixLowBadCoverageData
import Aris4Math.ThirtyFour.TwentyFourSparseDecode
namespace Aris4Math.ThirtyFour.TwentyFourSixLowBadCoverage
open TwentyFourSixLowBadData
open TwentyFourSparseDecode
set_option maxRecDepth 100000
set_option maxHeartbeats 0
'''
s+='def profileHigh : Case→Finset (Finset (Fin 6)) := '+vec('{'+','.join(fs(int(t)) for t,v in r['counts'].items() if int(t).bit_count()>=3 and v)+'}' if any(int(t).bit_count()>=3 and v for t,v in r['counts'].items()) else '∅' for r in profiles)+'\n'
s+='''def inputBad (b : Pattern) : Finset (Finset (Fin 6)) :=
  {{0,1}} ∪ (if 1≤b.val then {{2,3}} else ∅) ∪ (if 2≤b.val then {{4,5}} else ∅)
def profileBad (i : Case) : Finset (Finset (Fin 6)) :=
  {{0,1}} ∪ (if 2≤badCount i then {{2,3}} else ∅) ∪ (if 3≤badCount i then {{4,5}} else ∅)
abbrev Row := ℕ×(Case×Perm)
def rowValues (r : Row) : List ℕ := (List.range 41).map (fun i=>if r.1.testBit i then 1 else 0)
def rows : Pattern→List Row
'''
for b in range(3):s+='  | '+str(b)+' => ['+','.join(f'({code},({i},{pi}))' for code,i,pi in rows[b])+']\n'
s+='''def CheapMatch (b : Pattern) (values : List ℕ) (selected : Case×Perm) : Prop :=
  (∀k∈values,k≤1) ∧
  inputBad b=(profileBad selected.1).image (fun T=>T.map (perm selected.2).toEmbedding) ∧
  support entries values=(profileHigh selected.1).image (fun T=>T.map (perm selected.2).toEmbedding)
instance (b : Pattern) (values : List ℕ) (selected : Case×Perm) : Decidable (CheapMatch b values selected) := by unfold CheapMatch;infer_instance
end Aris4Math.ThirtyFour.TwentyFourSixLowBadCoverage
'''
(OUT/'TwentyFourSixLowBadSparseData.lean').write_text(s)
s='''import Aris4Math.ThirtyFour.TwentyFourSixLowBadSparseBridge
namespace Aris4Math.ThirtyFour.TwentyFourSixLowBadCoverage
open TwentyFourSixLowBadData
set_option maxHeartbeats 0
set_option maxRecDepth 100000
'''
for b in range(3):s+=f'theorem rows_cover_{b} : (rows {b}).map rowValues=catalogue {b} := by decide +kernel\n'
s+='theorem rows_cover (b : Pattern) : (rows b).map rowValues=catalogue b := by\n  fin_cases b\n'+''.join(f'  · exact rows_cover_{b}\n' for b in range(3))
for b in range(3):s+=f'theorem rows_correct_{b} : ∀r∈rows {b},CheapMatch {b} (rowValues r) r.2 := by decide +kernel\n'
s+='theorem rows_correct (b : Pattern) : ∀r∈rows b,CheapMatch b (rowValues r) r.2 := by\n  fin_cases b\n'+''.join(f'  · exact rows_correct_{b}\n' for b in range(3))
s+='''theorem coverage (b : Pattern) (values : List ℕ) (member : values∈catalogue b) :
    ∃selected : Case×Perm,
      (∀T,T.card≤2→low b (T.map (perm selected.2).toEmbedding)=upper selected.1 T) ∧
      (∀T,3≤T.card→vector values (T.map (perm selected.2).toEmbedding)=μ selected.1 T) := by
  have inrows : values∈(rows b).map rowValues := by rw [rows_cover];exact member
  obtain ⟨r,hr,eq⟩ := List.mem_map.mp inrows
  rw [← eq]
  exact ⟨r.2,cheap_correct b (rowValues r) r.2 (rows_correct b _ hr)⟩
end Aris4Math.ThirtyFour.TwentyFourSixLowBadCoverage
#print axioms Aris4Math.ThirtyFour.TwentyFourSixLowBadCoverage.coverage
'''
(OUT/'TwentyFourSixLowBadCoverageKernel.lean').write_text(s)
(HERE/'SIX_LOW_BAD_SPARSE_GENERATION.json').write_text(json.dumps({'domain_sizes':list(map(len,rows)),'profiles':181,'method':'ordered binary allocation rows; exact domain equality; bad-pair and high-trace support matching'},indent=2)+'\n')
print('Complete sparse witness domains',list(map(len,rows)))
