"""Independent excess-budget recursion, adjacent swaps, and alternate IE; no color enumeration."""
from pathlib import Path
from math import comb
from itertools import product
import json,time
P=Path(__file__).resolve().parent;st=time.process_time();D=comb(20,10)
def C(n,k):return comb(n,k) if 0<=k<=n else 0
# Different generation: recurse through all56 support masks with totalexcess4.
masks=[s for s in range(64) if 2<=s.bit_count()<=5]
raw=set();valid=set();bad=set()
def make(key):
 B=[set() for _ in range(6)]
 for point,s in enumerate(key):
  for i in range(6):
   if s>>i&1:B[i].add(point)
 if any(len(b)>4 for b in B):return None
 nxt=len(key)
 for b in B:
  add=4-len(b);b.update(range(nxt,nxt+add));nxt+=add
 assert nxt==20 and len(set().union(*B))==20
 return B

def finish(key):
 key=tuple(key);raw.add(key);B=make(key)
 if B is None or len({frozenset(b) for b in B})!=6:bad.add(key)
 else:valid.add(key)
def rec(i,left,key,occupied):
 if left==0:finish(key);return
 if i==len(masks):return
 s=masks[i];cost=s.bit_count()-1
 maxnum=left//cost
 for num in range(maxnum+1):
  new=[occupied[j]+num*(s>>j&1) for j in range(6)]
  # Keep all rawkeys, including actualcapacitybad ones; this small domain hasnone.
  rec(i+1,left-num*cost,key+[s]*num,new)
rec(0,4,[],[0]*6)
assert len(raw)==5901 and len(valid)==5886 and len(bad)==15

def sw(key,i):
 def image(s):
  a=s>>i&1;b=s>>(i+1)&1
  return s^((1<<i)|(1<<(i+1))) if a!=b else s
 return tuple(sorted(image(s) for s in key))
def alternate(B):
 no_red=0
 for bits in product((False,True),repeat=6):
  U=set().union(*(B[i] for i,b in enumerate(bits) if b))
  no_red+=(-1 if sum(bits)%2 else 1)*C(20-len(U),10-len(U))
 no_mono=0
 for choice in product((0,1,2),repeat=6):
  R=set().union(*(B[i] for i,c in enumerate(choice) if c==1));Z=set().union(*(B[i] for i,c in enumerate(choice) if c==2))
  if R&Z:continue
  no_mono+=(-1 if sum(c!=0 for c in choice)%2 else 1)*C(20-len(R)-len(Z),10-len(R))
 return {'no_red_mono':no_red,'no_mono_either_color':no_mono,'C':2*no_red-no_mono}
saved=json.loads((P/'RESULT.json').read_text());seenall=set();checks=[];orbit_checks=[]
for part in saved['patterns']:
 pvalid={k for k in valid if sorted(s.bit_count() for s in k)==sorted(part['repeat_multiplicities'])}
 assert len(pvalid)==part['valid_labels']
 union=set();vals=[]
 for row in part['orbits']:
  rep=tuple(row['representative_repeat_supports']);seen={rep};stack=[rep]
  while stack:
   z=stack.pop()
   for i in range(5):
    v=sw(z,i)
    if v not in seen:seen.add(v);stack.append(v)
  assert seen=={tuple(z) for z in row['orbit_members']} and seen<=pvalid and not seen&union
  union|=seen;B=make(rep)
  assert [sum(1<<v for v in b) for b in B]==row['link_masks']
  alt=alternate(B);count=alt['C'];assert count==row['C_count'];vals.append(count);orbit_checks.append({'repeat_supports':rep,'multiplicities':part['repeat_multiplicities'],**alt})
 assert union==pvalid;seenall|=union
 checks.append({'multiplicities':part['repeat_multiplicities'],'labels':len(pvalid),'orbits':len(part['orbits']),'minimum_C':min(vals)})
assert seenall==valid and len([r for part in saved['patterns'] for r in part['orbits']])==41
assert min(r['minimum_C'] for r in checks)==164896
# Closed-form exact count forone multiplicity-five point: total-starunion-good direct IE agrees.
assert checks[-1]['minimum_C']==177176 and 177176-29*6006==3002
out={'status':'PASS_COMPLETE_DOMAIN_ORBITS_AND_ALTERNATE_IE','scope':__doc__,'raw_keys':len(raw),'valid_keys':len(valid),'excluded_duplicate_links':len(bad),'S6_orbits':41,'patterns':checks,'independent_orbit_counts':orbit_checks,'C_min':164896,'denominator':D,'no_new_H_or_color_enumeration':True,'cpu_seconds':time.process_time()-st}
(P/'VERIFY.json').write_text(json.dumps(out,indent=2)+'\n');print(out)
