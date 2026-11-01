#!/usr/bin/env python3
from itertools import combinations,product
from collections import Counter
from math import comb
from functools import lru_cache
from pathlib import Path
from time import process_time
import json,sys
P=Path(__file__).resolve().parent
U=int(sys.argv[1]) if len(sys.argv)>1 and sys.argv[1].isdigit() else 7
TAG='_U'+str(U)+('_R13' if '--r13' in sys.argv else '')
DIRECT=json.loads((P.parent/'twentythree_internal_map/independent/RESULT.json').read_text())['direct_counts']
FAIL={}
for q in (8,9):
 FAIL[q]={'w0':max(v[str(q)] for n,v in DIRECT.items() if n.startswith('w0'))}
 for c in 'RB':FAIL[q]['w1_'+c]=max(DIRECT['w1_'+s+'_'+c][str(q)] for s in ('34','44'))
 for kind in ('double','two'):
  for sig in ('RR','BB','RB'):FAIL[q]['w2_'+kind+'_'+sig]=DIRECT['w2_'+kind+'_'+sig][str(q)]
@lru_cache(None)
def price(q,r,c):
 k=q-r if c=='B' else q
 return comb(18-r,k) if 0<=k<=18-r else 0
@lru_cache(None)
def ded(q,c,m):
 if m<2:return 0
 j=[price(q,8-i,c) for i in range(4)];t=[price(q,9,c),price(q,8,c)];n=min(m,6)
 vals=[j[3]+(n-2)*j[0]]
 if n>=3:vals.append(2*j[2]+(n-3)*j[0])
 for h in (0,1):
  u=max(0,4*n-18-2*h)
  vals.append(comb(n,2)*j[0]+(j[1]-j[0])*u+(j[2]-j[0])*h-comb(n,3)*t[0]-h*(n-2)*(t[1]-t[0]))
 return min(vals)+max(0,m-6)*j[0]
def options(tr):
 c=Counter(z for e in tr for z in e);K=21-U+sum(len(e)-1 for e in tr);ans=[]
 for nf in (1,2,3):
  for free in combinations(range(3),nf):
   if any(len(set(e)&set(free))>1 for e in tr):continue
   fixed=[z for z in range(5) if z not in free]
   for cc in product('RB',repeat=len(fixed)):
    if len(set(cc))<2:continue
    colors=dict(zip(fixed,cc));types=[]
    for z in free:
     groups=[tuple(colors[v] for v in e if v!=z) for e in tr if z in e]
     sig=''.join(sorted((v for g in groups for v in g),reverse=True));w=len(sig)
     types.append('w0' if w==0 else 'w1_'+sig if w==1 else 'w2_'+('double_' if len(groups)==1 else 'two_')+sig)
    for q in (8,9):
     pure=price(q,5,'R')+price(q,5,'B')
     base=K*pure-(1+c[4])*price(q,4,colors[4]);slope=price(q,4,colors[4])-pure
     groups=Counter()
     for z in fixed:
      if z==4:continue
      n=(5 if z<3 else U-1)-c[z];groups[colors[z]]+=n;base+=n*price(q,4,colors[z])
     for e in tr:
      if set(e)&set(free):continue
      ce={colors[z] for z in e}
      if len(ce)==1:base+=price(q,5-len(e),next(iter(ce)))
     base+=sum(FAIL[q][t] for t in types)
     ans.append((base,slope,q,dict(groups),colors[4],1+c[4],free,colors,types))
 return ans

def run():
 start=process_time();domain=json.loads((P/('DOMAIN'+TAG+'.json')).read_text());pilot='--profile' in sys.argv
 if pilot:domain=domain[:5]
 rows=[];rc=Counter();nc=0;strict=0;r13strict=0
 for tr,lo,hi,r13 in domain:
  assert process_time()-start<30,'30CPU budget reached'
  opts=options(tr)
  for d in range(lo,hi+1):
   best=None
   for o in opts:
    base,slope,q,groups,hcolor,hsub,free,colors,types=o
    red=groups.get('R',0)+(d-hsub if hcolor=='R' else 0)
    blue=groups.get('B',0)+(d-hsub if hcolor=='B' else 0)
    total=base+slope*d-ded(q,'R',red)-ded(q,'B',blue);space=comb(18,q)
    if best is None or total*best[1]<best[0]*space:best=(total,space,q,free,colors,types,red,blue)
    nc+=1
   total,space,q,free,colors,types,red,blue=best
   row={'traces':tr,'d':d,'r13':r13,'total':total,'space':space,'quota':q,'free':free,'fixed':colors,'types':types,'red_singletons':red,'blue_singletons':blue}
   rows.append(row);strict+=total<space;r13strict+=r13 and total<space
   if total>=space:rc['r13' if r13 else 'other']+=1
 out={'status':'PILOT_COMPLETE' if pilot else 'COMPLETE','inventories':len(domain),'keys':len(rows),'options':nc,'strict':strict,'r13_strict':r13strict,'uncovered':dict(rc),'cpu_seconds':process_time()-start,'residual':[r for r in rows if r['total']>=r['space']],'rows':rows}
 (P/('PILOT'+TAG+'.json' if pilot else 'RESULT'+TAG+'.json')).write_text(json.dumps(out,indent=2)+'\n')
 print(json.dumps({k:v for k,v in out.items() if k not in ('rows','residual')}))
if __name__=='__main__':run()
