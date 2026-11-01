import importlib.util,json,time,itertools
from pathlib import Path
P=Path(__file__).resolve().parent
sp=importlib.util.spec_from_file_location('p',P/'pilot.py');p=importlib.util.module_from_spec(sp);sp.loader.exec_module(p);c=p.c
start=time.process_time();rows=[];ranges={}
for v in range(54,71):
 for d in range(c.ceil(v-1,6),910//v+1):
  s=2*(v-1)-6*d
  if s<=0:
   rows.append(dict(v=v,d=d,gap='no unit-neighbor guarantee'));continue
  B=next(b for b in range(d,911) if v*d+s*(b+1-d)>910)
  ranges.setdefault(v,[]).append([d,B])
  for dy in range(d,B+1):
   ell={0:131-d-dy,1:d-1,2:dy-1,3:1};trials=[]
   for pos in ((v//2,v//2+1),(v//2,v//2-1)):
    u=p.bound(v,pos,ell,True);trials.append((u,pos))
   u,pos=min(trials);rows.append(dict(v=v,degrees=[d,dy],B=B,U=str(u),positions=pos,strict=u<1))
fail=[r for r in rows if not r.get('strict',False)]
out=dict(scope='all min-degree/unit-neighbor profiles at v54..70; both adjacent central orientations; avoided quotas',ranges=ranges,profiles=len(rows),failures=fail,rows=rows,cpu=time.process_time()-start)
(P/'TWO_EXPANDED.json').write_text(json.dumps(out,indent=2))
print('two',len(rows),'fail',len(fail),'cpu',out['cpu']);print(json.dumps(fail,indent=2))
# Short tri probe on genuinely selectable low-degree unit-codegree triples.
trs=[];sels=[]
for v in range(62,71):
 d0=c.ceil(v-1,6)
 Ds=[D for D in range(d0,25) if (D+1)*v>910 and 24*((D+1)*v-910)>2*(6*(D+1)-v+2)**2]
 if not Ds:continue
 D=min(Ds);Z=(D+1)*v-910;T=6*(D+1)-v+2
 sels.append(dict(v=v,d0=d0,D=D,Z=Z,T=T,lhs=24*Z,rhs=2*T*T))
 for ds in itertools.combinations_with_replacement(range(d0,D+1),3):
  for tri in (0,1):
   ell={0:132-sum(ds),1:ds[0]-1,2:ds[1]-1,4:ds[2]-1,7:1} if tri else {0:133-sum(ds),1:ds[0]-2,2:ds[1]-2,4:ds[2]-2,3:1,5:1,6:1}
   pos=(v//2-1,v//2,v//2+1);u=p.bound(v,pos,ell,True)
   trs.append(dict(v=v,degrees=ds,tri=tri,U=str(u),strict=u<1,positions=pos))
  if time.process_time()-start>110:raise RuntimeError('CPU budget')
tfail=[r for r in trs if not r['strict']]
out2=dict(scope='smallest D from valid generalized low-degree unit triple lemma; ascending degrees at three central positions; avoided quotas',selection=sels,profiles=len(trs),failures=tfail,rows=trs,cpu=time.process_time()-start)
(P/'THREE_SHORT.json').write_text(json.dumps(out2,indent=2))
print('three',len(trs),'fail',len(tfail),'total cpu',out2['cpu']);print(json.dumps(sels,indent=2));print(json.dumps(tfail[:12],indent=2))
