"""Equivalent sparse storage and bounded proofs for the saved 181 certificates."""
from pathlib import Path
import json,sys
ROOT=Path(__file__).resolve().parents[4];HERE=Path(__file__).resolve().parent
OUT=ROOT/'formal/Aris4Math/ThirtyFour';base='TwentyFourSixLowBad';ns='Aris4Math.ThirtyFour.'+base+'Data'
D=json.loads((HERE/(base+'_REPLAY.json')).read_text());assert len(D)==181
vec=lambda a:'!['+','.join(a)+']';fs=lambda m:'{'+','.join(str(j) for j in range(6) if m>>j&1)+'}' if m else '∅'
if '--recovery-only' not in sys.argv:
 p=OUT/(base+'Data.lean');s=p.read_text()
 if 'def μRows :' not in s:
  a=s.index('def μ :');b=s.index('def positionFn :')
  raw='def μRows : Array (List (ℕ×ℕ)) := #['+','.join('['+','.join(f'({t},{n})' for t,n in sorted(d['counts'].items(),key=lambda x:int(x[0])))+']' for d in D)+']\n'
  raw+='def typeCode (T : Finset (Fin 6)) : ℕ := ∑j∈T,2^j.val\ndef μ (i : Case) (T : Finset (Fin 6)) : ℕ := ((μRows.getD i.val []).lookup (typeCode T)).getD 0\n'
  s=s[:a]+raw+s[b:]
 s=s.replace('theorem positionFn_injective : ∀ i, Function.Injective (positionFn i) := by decide +kernel','set_option maxHeartbeats 0 in\ntheorem positionFn_injective : ∀ i, Function.Injective (positionFn i) := by\n  intro i\n  fin_cases i <;> decide +kernel')
 rv=tuple(tuple(z[0] for z in row) for row in D[0]['dual']);qv=tuple(tuple(z[2] for z in row) for row in D[0]['dual'])
 assert all(tuple(tuple(z[0] for z in row) for row in d['dual'])==rv for d in D)
 assert all(tuple(tuple(z[2] for z in row) for row in d['dual'])==qv for d in D)
 s='\n'.join('def R (_i : Case) : Fin 6 → Quota → Finset (Fin 6) := '+vec(vec(fs(t) for t in row) for row in rv) if l.startswith('def R :') else
  'def quota (_i : Case) : Fin 6 → Quota → ℕ := '+vec(vec(str(t) for t in row) for row in qv) if l.startswith('def quota :') else l for l in s.splitlines())+'\n'
 if 'theorem μ_eq_recovered' in s:
  a=s.index('set_option maxHeartbeats 0 in\ntheorem μ_eq_recovered');b=s.index('end Aris4Math.',a);s=s[:a]+s[b:]
 p.write_text(s)
 p=OUT/(base+'.lean');s=p.read_text();imp='import Aris4Math.ThirtyFour.'+base+'Recovery\n'
 if imp not in s:s=imp+s
 p.write_text(s)
end=f'end {ns}\n'
for b in range(6):
 s=f'import Aris4Math.ThirtyFour.{base}Data\nnamespace {ns}\nset_option maxRecDepth 100000\nset_option maxHeartbeats 0\n'
 for i in range(30*b,181 if b==5 else 30*(b+1)):
  s+=f'theorem recover_{i} : ∀ T, μ {i} T=Aris4Math.ThirtyThree.MultiLockRecovery.recovered (upper {i}) (μ {i}) T := by decide +kernel\n'
 (OUT/f'{base}Recovery{b}.lean').write_text(s+end)
s='\n'.join(f'import Aris4Math.ThirtyFour.{base}Recovery{b}' for b in range(6))+f'\nnamespace {ns}\nset_option maxRecDepth 100000\nset_option maxHeartbeats 0\n'
s+='theorem μ_eq_recovered : ∀ i T, μ i T=Aris4Math.ThirtyThree.MultiLockRecovery.recovered (upper i) (μ i) T := by\n  intro i\n  fin_cases i\n'+''.join(f'  · exact recover_{i}\n' for i in range(181))
(OUT/f'{base}Recovery.lean').write_text(s+end+f'#print axioms {ns}.μ_eq_recovered\n')
print('Saved data preserved; six recovery blocks and exact aggregate generated.')
