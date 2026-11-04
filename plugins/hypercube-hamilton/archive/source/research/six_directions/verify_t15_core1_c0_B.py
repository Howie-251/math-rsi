import json,itertools
from pathlib import Path
R=Path('.')
from r4_boundary_blocking_probe import negative_table
pairs=lambda a,b:tuple(sorted((a,b)))
us=(3,5,9);neg=[set(negative_table(*[v for v in us if v!=u],1)) for u in us]
def pm(v):
 if not v:yield frozenset();return
 a=min(v)
 for b in sorted(v-{a}):
  for q in pm(v-{a,b}):yield q|{(a,b)}
exception=set();count=0
for F in pm(set(range(2,16))):
 count+=1;mate={a:b for e in F for a,b in (e,e[::-1])};okay=False
 for f,u in enumerate(us):
  s,t=[z for z in us if z!=u]
  if mate[s]==t:continue
  k,l=mate[s],mate[t];L=(F-{pairs(s,k),pairs(t,l)})|{pairs(k,l)}
  if L not in neg[f]:okay=True;break
 if not okay:exception.add(F)
assert count==135135 and len(exception)==105
saved=set();raw=R/'t15_core1_route_c0_residual_inputs.bin'
with raw.open('rb') as f:
 for k in range(105):
  f.seek(k*10395*26);r=f.read(26)
  saved.add(frozenset(pairs(r[j]//2,r[j+1]//2) for j in range(12,26,2)))
assert saved==exception and raw.stat().st_size==105*10395*26
# Rebuild every A pairing, in matching-generation order, for every B input.
A=[]
for F in pm(set(range(1,16))-{3,5,9}):
 A.append(bytes(z for a,b in sorted(F) for z in (2*a+1,2*b+1)))
assert len(A)==len(set(A))==10395
with raw.open('rb') as stream:
 for F in sorted(exception,key=lambda f:sorted(f)):
  B=bytes(2*z for e in sorted(F) for z in e)
  want=b''.join(a+B for a in A)
  assert stream.read(len(want))==want
 assert stream.read()==b''
out={'status':'PASS','B_matchings':count,'B_exceptions':len(exception),'residual_full_input_list_rebuilt':105*10395,'scope':'Independent c0 suppression, exact B list, every A pairing and every original matching regenerated. A path exists uniformly by N14.'}
(R/'t15_core1_c0_B_verification.json').write_text(json.dumps(out,indent=2));print(out)
