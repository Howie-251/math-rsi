import json,itertools,time
from pathlib import Path
P=Path(__file__).resolve().parent
D=json.load(open(P/'EIGHT_QUAD_DATA.json'));trip=json.load(open(P/'REMAINING_TRIPLE_DATA.json'))
pairs=[(0,1),(0,2),(0,3),(1,2),(1,3),(2,3)];highs=[(0,1,2),(0,1,3),(0,2,3),(1,2,3),(0,1,2,3)]
perms=list(itertools.permutations(range(4)))
ci=[[pairs.index(tuple(sorted(p[x] for x in q))) for q in pairs] for p in perms]
hi=[[highs.index(tuple(sorted(p[x] for x in q))) for q in highs] for p in perms]
strict=set()
for d in D:
 for c,h in zip(ci,hi):
  co=[0]*6;high=[0]*5
  for j,k in enumerate(c):co[k]=d['co'][j]
  for j,k in enumerate(h):high[k]=d['high'][j]
  strict.add((tuple(co),tuple(high)))
small=set()
for sh,q in zip([[2,2,2,2,2,2],[1,2,2,2,2,2],[1,2,2,1,2,1],[1,1,1,2,2,2],[1,2,1,1,2,1]],[0,0,0,0,1]):
 for c in ci:
  co=[0]*6
  for j,k in enumerate(c):co[k]=sh[j]
  small.add((tuple(co),q))
# Inspect data schema once rather than treating arbitrary fields as trusted.
T=set((d['a'],d['b'],d['c'],d['t']) for d in trip if not d['high'])
stats=dict(valid=0,residue=0,triple=0,quad=0);bad=[];start=time.monotonic()
for co in itertools.product(range(1,4),repeat=6):
 for h in itertools.product(range(4),repeat=5):
  a,b,c,d,q=h;inventory=(a+b+q,a+c+q,b+c+q,a+d+q,b+d+q,c+d+q)
  if any(x>y for x,y in zip(inventory,co)):continue
  stats['valid']+=1
  if (3 in co and not any(h)) or (co,q) in small:stats['residue']+=1;continue
  if any(t in T for t in ((co[0],co[1],co[3],a+q),(co[0],co[2],co[4],b+q),(co[1],co[2],co[5],c+q),(co[3],co[4],co[5],d+q))):stats['triple']+=1;continue
  if (co,h) in strict:stats['quad']+=1;continue
  bad.append((co,h))
print(stats,'bad',len(bad),bad[:10],time.monotonic()-start)
assert not bad
(P/'EIGHT_COVERAGE_CHECK.json').write_text(json.dumps({'scope':'Full bounded local pair inventories; weak residue or stored strict triple/quad, not probability replay','counts':stats,'bad':bad,'seconds':time.monotonic()-start},indent=2)+'\n')
