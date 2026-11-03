from pathlib import Path
from collections import deque,Counter
import json,random,resource,subprocess,time

P=Path(__file__).resolve().parent
t0=time.monotonic()
def usage():
 a=resource.getrusage(resource.RUSAGE_SELF);b=resource.getrusage(resource.RUSAGE_CHILDREN)
 return a.ru_utime+a.ru_stime+b.ru_utime+b.ru_stime
c0=usage()
def dump(name,x):(P/name).write_text(json.dumps(x,indent=2)+'\n')
def code(x):return sum(v*13**i for i,v in enumerate(x))
def canonical(x):return min(tuple(x),tuple(-v%13 for v in x),key=code)
def mult(x,y):
 a,b,c,d=x;e,f,g,h=y
 return canonical(((a*e+b*g)%13,(a*f+b*h)%13,(c*e+d*g)%13,(c*f+d*h)%13))
identity=canonical((1,0,0,1))
sl=[(a,b,c,d) for a in range(13) for b in range(13) for c in range(13) for d in range(13) if (a*d-b*c)%13==1]
assert len(sl)==2184
group=sorted({canonical(m) for m in sl},key=code)
group.remove(identity);group.insert(0,identity)
index={m:i for i,m in enumerate(group)}
assert len(group)==1092
inverse=[index[canonical((d,-b%13,-c%13,a))] for a,b,c,d in group]
pairs=[(i,inverse[i]) for i in range(1,1092) if i<inverse[i]]
invol=[i for i in range(1,1092) if inverse[i]==i]
assert len(pairs)==500 and len(invol)==91
rng=random.Random(20261027130)
starts=[]
for p,i in [(6,0),(5,2),(4,4)]:
 for _ in range(4):
  pa=rng.sample(range(500),p);iv=rng.sample(range(91),i)
  S=[g for q in pa for g in pairs[q]]+[invol[q] for q in iv]
  assert len(set(S))==12 and all(inverse[g] in S for g in S)
  starts.append(dict(pair_pool_ids=pa,involution_pool_ids=iv,S=S))
first=starts[0]['S']
# Independent direct matrix expansion for the first production candidate.
adj=[[index[mult(g,group[s])] for s in first] for g in group]
assert all(len(set(row))==12 and u not in row for u,row in enumerate(adj))
assert all(u in adj[v] for u,row in enumerate(adj) for v in row)
dist=[-1]*1092;dist[0]=0;q=deque([0])
while q:
 u=q.popleft()
 if dist[u]==3:continue
 for v in adj[u]:
  if dist[v]<0:dist[v]=dist[u]+1;q.append(v)
dump('first_python_check.json',dict(n=1092,degree=12,simple=True,undirected=True,matrix_direct_adjacencies=1092*12,radius3_distance_histogram=dict(Counter(dist)),radius3_missing=dist.count(-1),first_S=first))
dump('group_definition.json',dict(name='PSL(2,13)',vertices=1092,SL2_order=2184,canonical_rule='min(code(M),code(-M)) with code=a+13*b+169*c+2197*d; identity reindexed zero',matrix_codes=[code(m) for m in group],matrices=group,inverse_ids=inverse,pair_pool=pairs,involution_pool=invol,edges='u--u*s for twelve distinct inverse-closed nonidentity generators',symmetry='left multiplication acts transitively; exact identity-root radius-three coverage determines diameter-at-most-three'))
dump('starts.json',dict(seed=20261027130,profile='4 starts each: 6 pairs; 5 pairs+2 involutions; 4 pairs+4 involutions',starts=starts,segments_per_start=3,maximum_strict_moves_per_segment=12,kick_seed=20261027131))
lines=['1092',' '.join(map(str,[code(m) for m in group])),'12']
for s in starts:
 pa=s['pair_pool_ids'];iv=s['involution_pool_ids'];lines.append(' '.join(map(str,[len(pa),len(iv)]+pa+iv)))
lines.append(' '.join(map(str,dist)))
(P/'input.txt').write_text('\n'.join(lines)+'\n')
subprocess.run(['g++','-std=c++17','-O3',str(P/'search.cpp'),'-o',str(P/'search')],check=True)
prep=usage()-c0
remaining=max(0,90-prep-1)
dump('run.json',dict(status='RUNNING',preparation_CPU_seconds=prep,total_CPU_budget=90,production_budget=remaining,worker_count=1,restarts=0))
with (P/'search.log').open('w') as log:
 run=subprocess.run([str(P/'search'),str(P),str(remaining)],stdout=log,stderr=subprocess.STDOUT)
assert run.returncode==0,(run.returncode,(P/'search.log').read_text()[-2000:])
terminal=json.loads((P/'terminal.json').read_text());terminal.update(preparation_CPU_seconds=prep,total_measured_CPU_seconds=usage()-c0,wall_seconds=time.monotonic()-t0,total_CPU_budget=90,worker_count=1,restarts=0)
dump('terminal.json',terminal);dump('run.json',dict(status=terminal['status'],running=False,total_measured_CPU_seconds=terminal['total_measured_CPU_seconds'],pending=terminal['pending']))
print(json.dumps(terminal))
