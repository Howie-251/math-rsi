"""One symbolic set comparison; no parameter or finite-field enumeration."""
import csv
import json
from pathlib import Path
from time import process_time

start = process_time()
root = Path(__file__).resolve().parent
rows = list(csv.DictReader((root.parent / 'DISTINCT_FORMS.tsv').open(), delimiter='\t'))
names = ['alpha0', 'alpha1', 'alpha2', 'sigma', 'tau', 'rho', 'half']
actual = {tuple(int(r[n]) for n in names) for r in rows if r['root'] == r['target'] == '0'}
def form(**kw):
    return tuple(kw.get(n, 0) % 2 if n == 'half' else kw.get(n, 0) for n in names)
def add(u, v):
    return tuple((a+b) % 2 if i == 6 else a+b for i, (a,b) in enumerate(zip(u,v)))
def neg(u):
    return tuple(-a % 2 if i == 6 else -a for i,a in enumerate(u))
F7 = {form(alpha0=k) for k in [-3,-1,1,3]} | {form(half=1, alpha0=k) for k in [-2,0,2]}
base = set(F7)
for v in ['sigma', 'tau']:
    for a in [-1,1]:
        for b in [-1,1]:
            base.add(form(alpha0=a, **{v:b}))
    for b in [-1,1]:
        base.add(form(half=1, **{v:b}))
base |= {form(), form(sigma=1), form(sigma=-1), form(tau=1), form(tau=-1),
         form(sigma=1,tau=-1), form(sigma=-1,tau=1)}
blocks = []
for d in [form(alpha1=1),form(alpha2=-1),form(rho=1)]:
    positive = {add(d,z) for z in [form(),form(sigma=1),form(tau=-1),form(sigma=1,tau=-1)]}
    blocks.append(positive | {neg(z) for z in positive})
predicted = base.union(*blocks)
assert len(F7)==7 and len(base)==26 and all(len(b)==8 for b in blocks)
assert len(predicted)==50 and actual==predicted
result = {'status':'PASS_SYMBOLIC_ROOT00_26_PLUS_THREE8_IDENTITY',
          'actual_forms':len(actual),'base_forms':len(base),'block_sizes':[len(b) for b in blocks],
          'missing_forms':[],'extra_forms':[],'finite_parameter_assignments_tested':0,
          'CPU_seconds':process_time()-start}
(root/'SYMBOLIC_IDENTITY_RESULT.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result))
