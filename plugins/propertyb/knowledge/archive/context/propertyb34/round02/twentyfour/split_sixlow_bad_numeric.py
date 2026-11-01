"""Bound kernel compilation units; preserve the original 181 exact certificates."""
from pathlib import Path
ROOT=Path(__file__).resolve().parents[4];HERE=Path(__file__).resolve().parent
OUT=ROOT/'formal/Aris4Math/ThirtyFour';base='TwentyFourSixLowBad';ns='Aris4Math.ThirtyFour.'+base+'Numeric'
p=OUT/f'{base}Numeric.lean';s=p.read_text();backup=HERE/'SixLowBadNumericBeforeChunks.lean'
if 'fin_cases i <;> simp only [p_eq_computed]' in s:backup.write_text(s)
else:s=backup.read_text()
a=s.index('theorem cachedCertificates :');b=s.index('\ntheorem certificates :',a)
cert=s[a:b];typ=cert[cert.index('Numeric.validProfile'):cert.index(' := by')];prefix=s[:a]
def fixed(i):
 return typ.replace('p i',f'p {i}').replace('positions i',f'positions {i}').replace('α i',f'α {i}').replace('R i',f'R {i}').replace('quota i',f'quota {i}').replace('loss i',f'loss {i}')
for chunk in range(19):
 t=prefix
 for i in range(chunk*10,min(181,(chunk+1)*10)):
  t+=f'theorem cached_case_{i} : {fixed(i)} := by\n  simp only [p_eq_computed]\n  unfold Numeric.validProfile\n  decide +kernel\n'
 (OUT/f'{base}NumericCases{chunk}.lean').write_text(t+f'end {ns}\n')
imports='\n'.join(f'import Aris4Math.ThirtyFour.{base}NumericCases{k}' for k in range(19))+'\n'
header=prefix[prefix.index('namespace '):]
t=imports+header+cert[:cert.index(' := by')]+''' := by
  intro i
  fin_cases i
'''+''.join(f'  · exact cached_case_{i}\n' for i in range(181))+s[b:]
p.write_text(t)
# Short real certs from three different pattern families.
t=prefix
for i in [0,37,179]:
 t+=f'example : {fixed(i)} := by\n  simp only [p_eq_computed]\n  unfold Numeric.validProfile\n  decide +kernel\n'
(HERE/'BadNumericThreeProbe.lean').write_text(t+f'end {ns}\n')
print('19 independent batches (18x10+1), same original exported certificates')
