"""Independent search formulation: binary degrees plus disconnected-component cuts."""
import json,time
from pathlib import Path
import numpy as np
from scipy.optimize import milp, Bounds, LinearConstraint
from scipy.sparse import csc_matrix
ROOT=Path(__file__).resolve().parent
data=json.loads((ROOT/'pilot_results.json').read_text(encoding='utf8'))
start=time.monotonic()
for index,c in enumerate(data['cases']):
    if c['status']!='UNKNOWN':continue
    n=c['n'];N=1<<n;es=[(x,x^(1<<i)) for x in range(N) for i in range(n) if not x&(1<<i)]
    lookup={e:i for i,e in enumerate(es)};E=len(es)
    lo=np.zeros(E);hi=np.ones(E)
    for e in c['matching']:lo[lookup[tuple(sorted(e))]]=1
    rows=np.zeros((N,E))
    for i,(a,b) in enumerate(es):rows[a,i]=rows[b,i]=1
    deg=np.full(N,2.);deg[c['u']]=deg[c['v']]=1
    lbs=list(deg);ubs=list(deg);cuts=[];rounds=0;t0=time.monotonic()
    while time.monotonic()-t0<5:
        rounds+=1
        mat=np.vstack([rows,*cuts]) if cuts else rows
        res=milp(np.zeros(E),integrality=np.ones(E),bounds=Bounds(lo,hi),
                 constraints=LinearConstraint(csc_matrix(mat),lbs,ubs),
                 options={'time_limit':max(.05,5-(time.monotonic()-t0)),'mip_rel_gap':0})
        if res.status not in (0,1) or res.x is None:break
        if np.max(np.abs(res.x-np.round(res.x)))>1e-6:break
        chosen=np.round(res.x).astype(int)
        if not np.array_equal(rows@chosen,deg) or np.any(chosen<lo) or np.any(chosen>hi):break
        adj=[[] for _ in range(N)]
        for i,(a,b) in enumerate(es):
            if chosen[i]:adj[a].append(b);adj[b].append(a)
        seen=set();components=[]
        for v in range(N):
            if v in seen:continue
            comp={v};todo=[v];seen.add(v)
            while todo:
                for z in adj[todo.pop()]:
                    if z not in seen:seen.add(z);comp.add(z);todo.append(z)
            components.append(comp)
        if len(components)==1:
            p=[c['u']];previous=-1
            while p[-1]!=c['v']:
                choices=[z for z in adj[p[-1]] if z!=previous]
                assert len(choices)==1
                previous=p[-1];p.append(choices[0])
            c['path']=p;c['status']='FOUND';break
        for comp in components:
            if c['u'] in comp:continue
            row=np.array([float(a in comp and b in comp) for a,b in es])
            cuts.append(row);lbs.append(-np.inf);ubs.append(len(comp)-1)
    c['milp_retry']={'seconds':time.monotonic()-t0,'rounds':rounds,'last_status':int(res.status)}
data['summary']={s:sum(c['status']==s for c in data['cases']) for s in ('FOUND','UNKNOWN','EXHAUSTED')}
data['milp_retry_elapsed_seconds']=time.monotonic()-start
(ROOT/'pilot_results_retry.json').write_text(json.dumps(data,indent=2),encoding='utf8')
print(json.dumps({'summary':data['summary'],'retry_seconds':data['milp_retry_elapsed_seconds']}))
