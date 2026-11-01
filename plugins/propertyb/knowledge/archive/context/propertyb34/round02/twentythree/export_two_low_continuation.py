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
for n in [5,6,7]:
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
 raw=json.loads((ROOT/f'context/propertyb34/round01/middle-math/FEW_LOW23_2_{n-2}.json').read_text())
 pure=[r for r in raw['results'] if F(r['bound'])<1]
 joint=[r for r in raw['results'] if F(r['bound'])>=1 and F(r['final_bound'])<1]
 residue=[r['group'] for r in raw['results'] if F(r['final_bound'])>=1]
 prefix=f'TwentyThreeTwoLow{["Zero","One","Two","Three","Four","Five","Six","Seven"][n]}Strict'
 out=dict(locks=n,pure=[],joint=[],residue=residue,status='exported, not Lean checked')
 for b in range(0,len(pure),16):
  name=prefix+f'Block{b//16}'
  rows=pure[b:b+16]
  data=env['export_pure'](name,rows,[6,6]+[7]*(n-2))
  (HERE/f'{name}_REPLAY.json').write_text(json.dumps(base.json_value(data),indent=2)+'\n')
  out['pure'].append(dict(module=name,groups=[r['group']for r in rows]))
 for row in joint:
  out['joint'].append(env['export_joint'](prefix+f'Joint{row["group"]}',row,[6,6]+[7]*(n-2)))
 summary.append(out)
 print(n,len(pure),len(joint),len(residue),flush=True)
(HERE/'TWO_LOW_CONTINUATION_EXPORT.json').write_text(json.dumps(summary,indent=2)+'\n')
