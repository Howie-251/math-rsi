from pathlib import Path
from itertools import combinations,combinations_with_replacement
import importlib.util,json,time,signal
HERE=Path(__file__).resolve().parent
spec=importlib.util.spec_from_file_location('strong',HERE/'component_trial.py');p=importlib.util.module_from_spec(spec);spec.loader.exec_module(p)
Q=p.Q;m=p.m;cal=p.cal
START=time.process_time();signal.setitimer(signal.ITIMER_PROF,40)

def main():
 data=json.loads((HERE/'COMPONENT_TRIAL.json').read_text());rows=[];branches=[]
 for old in data['failures']:
  v=old['v']
  if old['kind']!='two':continue
  d,e=old['degrees'];n=2*(v-1)-7*d;t=n-1-(7*e-(v-1));assert t>0
  excess=2128-v*d-n*(e-d);upper=e+excess//t
  for f in range(e,upper+1):
   ds=[d,e,f]
   for tri in(0,1):
    ell={0:268-sum(ds),1:d-1,2:e-1,4:f-1,7:1}if tri else{0:269-sum(ds),1:d-2,2:e-2,4:f-2,3:1,5:1,6:1}
    best=None
    for pos in((v//2-1,v//2,v//2+1),(v//2,v//2-1,v//2+1),(v//2-1,v//2+1,v//2)):
     u=cal.bound(v,pos,ell)
     if best is None or u<best[0]:best=u,pos
     if u<1:break
    rows.append(dict(v=v,kind='adaptive_three',degrees=ds,tri=tri,ell=ell,positions=best[1],U=str(best[0]),strict=best[0]<1))
  branches.append(dict(v=v,d=d,e=e,n=n,t=t,excess=excess,third_maximum=upper))
 # Tail: all17 vertices are globally unit atv120; at least32 exist.
 # Enumerate all6 K4 pair partitions independently by a tiny clique subset scan.
 pairs=list(combinations(range(4),2));blocks=[b for b in range(1,16)if b.bit_count()>=2];patterns=[]
 for subset in range(1<<len(blocks)):
  bs=[b for i,b in enumerate(blocks)if subset>>i&1]
  if all(sum(bool(b>>i&1 and b>>j&1)for b in bs)==1 for i,j in pairs):patterns.append(bs)
 assert len(patterns)==6
 for bs in patterns:
  ell={b:1 for b in bs}
  for j in range(4):ell[1<<j]=17-sum(bool(b>>j&1)for b in bs)
  ell[0]=266-sum(ell.values());pos=(58,59,60,61);u=cal.bound(120,pos,ell)
  rows.append(dict(v=120,kind='four17',degrees=[17]*4,blocks=bs,ell=ell,positions=pos,U=str(u),strict=u<1))
 out=dict(scope='All remaining72 actual minimum/unit-partner branches at103..107; full successive common-unit range; six actual four17 tail types',rows=rows,branches=branches,failures=[r for r in rows if not r['strict']],cpu_seconds=time.process_time()-START)
 (HERE/'ADAPTIVE_TRIAL.json').write_text(json.dumps(out,indent=2)+'\n');print('profiles',len(rows),'fails',len(out['failures']),'CPU',out['cpu_seconds']);print(json.dumps(out['failures'][:20],indent=2));print('TAIL',[(r['blocks'],r['U'],r['strict'])for r in rows if r['kind']=='four17'])
if __name__=='__main__':main()
