import importlib.util,json,time,itertools
from fractions import Fraction as F
from pathlib import Path
P=Path(__file__).resolve().parent;ROOT=P.parents[2]
spec=importlib.util.spec_from_file_location('av',ROOT/'context/propertyb-m6-66-20261029/avoided/verify.py');av=importlib.util.module_from_spec(spec);spec.loader.exec_module(av);c=av.c;c.M=66
start=time.process_time();rows=[]
def ell_for(ds,blocks):
 ell={b:1 for b in blocks}
 for j,d in enumerate(ds):ell[1<<j]=d-sum(bool(b&(1<<j)) for b in blocks)
 ell[0]=66-sum(ell.values());return {t:n for t,n in ell.items() if n}
def bound(v,pos,ell,avoid=False):
 if not avoid:return c.profile_bound(v,pos,ell)
 dels={pos[j]:av.deletion(v,pos,ell,j) for j in range(len(pos))};total=F(0)
 for h in range(1,v+1):
  A=sum(n*c.endpoint(v,pos,h,T,True) for T,n in ell.items());B=sum(n*c.endpoint(v,pos,h,T,False) for T,n in ell.items());Q=sum(n*(m-(T==U))*c.weight(v,pos,h,T,U) for T,n in ell.items() for U,m in ell.items());total+=min(A,B,Q-dels.get(h,F(0)))
 return total
# v37 new structural selection: all 112 sorted triples, all positional degree assignments.
for ds in itertools.combinations_with_replacement(range(8,14),3):
 for blocks in ([3,5,6],[7]):
  best=None;done=False;attempts=0
  for pos in [(17,18,19),(15,16,17),(16,17,18),(18,19,20)]:
   for perm in sorted(set(itertools.permutations(ds))):
    ell=ell_for(perm,blocks);u=bound(37,pos,ell,True);attempts+=1
    if best is None or u<best['U']:best=dict(U=u,positions=pos,assigned=perm)
    if u<1:done=True;break
   if done:break
  rows.append(dict(v=37,degrees=ds,blocks=blocks,U=str(best['U']),strict=done,positions=best['positions'],assigned=best['assigned'],attempts=attempts))
  if time.process_time()-start>45:break
 if time.process_time()-start>45:break
(P/'V37_REPAIR.json').write_text(json.dumps(dict(rows=rows,complete=len(rows)==112,failures=[r for r in rows if not r['strict']],stats=av.stats,cpu_seconds=time.process_time()-start),indent=2))
print('v37 profiles',len(rows),'failures',sum(not r['strict'] for r in rows),'CPU',time.process_time()-start,flush=True)
# Remaining known 4-lock tails: try shifts only, no selection changes.
a=json.loads((P/'RESULTS.json').read_text());tails=[]
for r in a['rows']:
 if r['kind']!='uniform4':continue
 ds=r['degrees'];v=r['v'];best=None
 for shift in range(-4,4):
  pos=tuple(range(v//2-1+shift,v//2+3+shift));u=bound(v,pos,ell_for(ds,r['blocks']))
  if best is None or u<best[0]:best=(u,pos)
  if u<1:break
 tails.append(dict(v=v,degrees=ds,blocks=r['blocks'],U=str(best[0]),positions=best[1],strict=best[0]<1))
(P/'TAIL_LAYOUT_REPAIR.json').write_text(json.dumps(dict(rows=tails,failures=[r for r in tails if not r['strict']],cpu_seconds=time.process_time()-start),indent=2))
print('tails failures',[(v,sum(r['v']==v and not r['strict'] for r in tails)) for v in range(40,45)],'CPU',time.process_time()-start)
