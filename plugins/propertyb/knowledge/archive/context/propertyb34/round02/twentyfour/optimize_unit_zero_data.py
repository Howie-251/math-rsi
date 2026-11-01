"""Keep all 120 prescribed layouts and original rational values; split only elaboration."""
from pathlib import Path
ROOT=Path(__file__).resolve().parents[4];OUT=ROOT/'formal/Aris4Math/ThirtyFour';NAME='TwentyFourSixLowUnitAverage0'
p=OUT/(NAME+'Data.lean');s=p.read_text()
# Reorder the profile: computed literal is immediately usable; raw count binding
# is proved in separate chunks, so arithmetic probes need not rebuild all bindings.
a=s.index('def p (l : Layout)');b=s.index('def computed',a);old=s[a:b]
raw=old[:old.index('theorem p_eq')].replace('def p (l : Layout)','def rawExecutable (l : Layout)')
s=s[:a]+s[b:]
a=s.index('theorem p_eq_computed');b=s.index('\n',a)
s=s[:a]+'''def p := computed
theorem p_eq_computed (l : Layout) : p l=computed l := rfl
'''+raw+s[b+1:]
# Dense outer indexing is a direct array read; numerical contents remain exact.
inner={'positionFn':('Fin 6→Fin 24','fun _=>0'),'computed':('Numeric.Profile','⟨0,[],[],none,[]⟩'),'gamma':('ℚ','0'),'freeValue':('ℚ','0'),'aValue':('Fin 6→ℚ','fun _=>0'),'cValue':('Fin 6→ℚ','fun _=>0'),'valueValue':('SlotIndex→ℚ','fun _=>0')}
for name,(typ,default) in inner.items():
 a=s.index('def '+name+' :');b=s.index('\n',a);line=s[a:b];body=line.split(' := ',1)[1]
 assert body.startswith('![')
 replacement=f'def {name}Rows : Array ({typ}) := #'+body[1:]+f'\ndef {name} (l : Layout) : {typ} := {name}Rows.getD l.val ({default})'
 s=s[:a]+replacement+s[b:]
p.write_text(s)
header=f'import Aris4Math.ThirtyFour.{NAME}Data\nnamespace Aris4Math.ThirtyFour.{NAME}\nopen Aris4Math.ThirtyThree.MultiLockRecovery LocalProfiles\nset_option maxRecDepth 100000\nset_option maxHeartbeats 0\n'
end=f'end Aris4Math.ThirtyFour.{NAME}\n'
for b in range(24):
 body=header
 for i in range(5*b,5*b+5):
  body+=f'''theorem profile_{i} : p {i}=profile labels (positions {i}) μ (List.ofFn fun j=>(positions {i} j).val+1) := by
  have eq : p {i}=rawExecutable {i} := by rfl
  rw [eq]
  simp only [rawExecutable,executableType_eq,profile,rawProfile]
'''
 (OUT/f'{NAME}Profile{b}.lean').write_text(body+end)
body='\n'.join(f'import Aris4Math.ThirtyFour.{NAME}Profile{b}' for b in range(24))+f'\nnamespace Aris4Math.ThirtyFour.{NAME}\nopen Aris4Math.ThirtyThree.MultiLockRecovery\ntheorem p_eq (l : Layout) : p l=profile labels (positions l) μ (List.ofFn fun j=>(positions l j).val+1) := by\n  fin_cases l\n'+''.join(f'  · exact profile_{i}\n' for i in range(120))+end
(OUT/f'{NAME}Profile.lean').write_text(body)
p=OUT/(NAME+'.lean');s=p.read_text();s=f'import Aris4Math.ThirtyFour.{NAME}Profile\n'+s;p.write_text(s)
# All proposed slot values have common denominator 2210: store just integers.
import json
from fractions import Fraction as F
r=json.loads((Path(__file__).parent/(NAME+'_REPLAY.json')).read_text())
p=OUT/(NAME+'Data.lean');s=p.read_text()
for key,denom,typ in [('value',2210,'SlotIndex'),('a',340,'Fin 6'),('c',2210,'Fin 6')]:
 name=key+'Value';a=s.index('def '+name+'Rows :');b=s.index('\n',s.index('def '+name+' (l : Layout)',a))
 integers=[]
 for row in r['layouts']:
  nums=[F(z)*denom for z in row[key]];assert all(q.denominator==1 for q in nums)
  integers.append('#['+','.join(str(q.numerator) for q in nums)+']')
 replacement=f'def {name}Numer : Array (Array ℤ) := #['+','.join(integers)+f']\ndef {name} (l : Layout) (j : {typ}) : ℚ := (({name}Numer.getD l.val #[]).getD j.val 0 : ℚ)/{denom}'
 s=s[:a]+replacement+s[b:]
for name,value in [('gamma','(1/120:ℚ)'),('freeValue','(13/34:ℚ)')]:
 a=s.index('def '+name+'Rows :');b=s.index('\n',s.index('def '+name+' (l : Layout)',a))
 s=s[:a]+f'def {name} (_l : Layout) : ℚ := {value}'+s[b:]
p.write_text(s)
