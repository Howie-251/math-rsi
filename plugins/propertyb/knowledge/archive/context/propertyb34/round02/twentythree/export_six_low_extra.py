"""Adapt the existing exact layout exporter to the saved 5/6-low domains.
It reuses the same actual-count applications; this script performs no search.
"""
from pathlib import Path
from fractions import Fraction as F
import importlib.util,inspect,json
ROOT=Path(__file__).resolve().parents[4]
HERE=Path(__file__).resolve().parent
spec=importlib.util.spec_from_file_location('base', ROOT/'context/propertyb34/round01/middle-lean/generate_few_low_four.py')
base=importlib.util.module_from_spec(spec);spec.loader.exec_module(base)
summary=[]
for n in [7]:
 env=dict(base.__dict__)
 env['K']=n
 env['fs']=lambda m,n=n: '{'+','.join(str(i) for i in range(n) if m>>i&1)+'}' if m else '∅'
 # The exporter treats every actual lock identically. Replace its lock arity;
 # discard the 4-lock-only recovery wrapper, retaining the general counts caller.
 def write(name,text,n=n):
  text=text.replace('Fin 4',f'Fin {n}')
  if name == 'TwentyThreeSixLowExtra7Joint16':
   text=text.replace('TwentyThreeSixLowExtra7Joint16Numeric','TwentyThreeSixLowExtra7Joint16CachedNumeric')
  text='\n'.join(line for line in text.splitlines() if not line.startswith(('def co :', 'def high :')))+'\n'
  if 'theorem μ_eq_recovered' in text:
   before,after=text.split('set_option maxHeartbeats 0 in\ntheorem μ_eq_recovered',1)
   text=before+'end Aris4Math.'+after.split('end Aris4Math.',1)[1]
  if 'theorem propertyB_of_data' in text:
   before,after=text.split('theorem propertyB_of_data',1)
   text=before+'end Aris4Math.'+after.split('end Aris4Math.',1)[1]
   text='\n'.join(line for line in text.splitlines() if '.propertyB_of_data' not in line)+'\n'
  (ROOT/'formal/Aris4Math/ThirtyFour'/f'{name}.lean').write_text(text)
 env['write']=write
 for name in ['mu','computed','labels','pure_record','export_pure','export_joint']:
  src=inspect.getsource(getattr(base,name)).replace('range(4)','range(K)').replace('range(16)','range(1<<K)').replace('15 ^ bit','((1<<K)-1) ^ bit')
  exec(compile(src,str(HERE/'export_five_six_low.py'), 'exec'),env)
 raw=json.loads((ROOT/'context/propertyb34/round01/middle-math/MIXED_LOW_23.json').read_text())
 for degree in [7,8]:
  source=[r for r in raw['results'] if r['degrees'][-1]==degree]
  pure=[r for r in source if F(r['bound'])<1]
  joint=[r for r in source if F(r['bound'])>=1 and F(r['joint']['bound'])<1]
  name=f'TwentyThreeSixLowExtra{degree}'
  data=env['export_pure'](name,pure,[6]*6+[degree])
  (HERE/f'SIX_LOW_EXTRA{degree}_REPLAY.json').write_text(json.dumps(base.json_value(data),indent=2)+'\n')
  out=dict(degree=degree,pure=[r['group'] for r in pure],joint=[],numeric_status='exported, not Lean checked')
  for row in joint:
   out['joint'].append(env['export_joint'](name+f'Joint{row["group"]}',row,[6]*6+[degree]))
  summary.append(out)
(HERE/'SIX_LOW_EXTRA_CERTIFICATE_EXPORT.json').write_text(json.dumps(summary,indent=2)+'\n')
print(json.dumps(summary,indent=2))
