from pathlib import Path
from itertools import permutations,combinations
import json,hashlib
R=Path(__file__).resolve().parent
def read(n):return json.loads((R/n).read_text(encoding='utf-8-sig'))
def dump(n,x):(R/n).write_text(json.dumps(x,indent=2)+'\n',encoding='utf-8')
def sha(n):return 'sha256:'+hashlib.sha256((R/n).read_bytes()).hexdigest()
reg=read('Q5_TWO_TARGET_REGISTRY.json');proof=read('Q6_T15_GOOD_ROOT_COMPONENTS.json');profile=read('Q6_T15_ACTUAL_PROFILE.json')
accepted={r['index'] for r in read('Q6_T15_TWO_TARGET_REVIEW_checks.json')['reports'] if r['returncode']==0}
assert accepted==set(range(78))-{37,67}
maps=[[sum(((v>>i)&1)<<q[i] for i in range(5)) for v in range(32)] for q in permutations(range(5))]
lookup=set()
for row in reg['rows']:
 if row['index'] not in accepted:continue
 for m in maps:lookup.add((m[row['holes'][1]],m[row['holes'][2]],*sorted(m[t] for t in row['targets']),m[row['root']]))
stored={r['core_index']:r for r in proof['closed_cores']+proof['open_cores_with_candidates']}
closed=set();summary=[];total_transports=0
for c in profile['orbits']:
 I,U=c['included'],c['omitted'];H={0,*I,*U};V=set(range(64))-H;cuts={}
 for j in range(6):
  A={v for v in H if not v&(1<<j)};ua=A.intersection(U);ia=A.intersection(I)
  if len(A)!=3 or len(ua)!=1 or len(ia)!=1:continue
  f=next(iter(ua));b=next(iter(ia));ub=next(iter(set(U)-ua));T={v^(1<<j) for v in I if v&(1<<j)}
  assert len(T)==2 and 0 not in T and all(t.bit_count()%2==0 for t in T)
  def project(v):return sum(((v>>k)&1)<<(k-(k>j)) for k in range(6) if k!=j)
  roots=set()
  for d in V:
   if d&(1<<j):continue
   key=(project(b^f),project(f),*sorted(project(t^f) for t in T),project(d^f))
   if key in lookup:roots.add(d)
  if roots:cuts[j]=(f,b,ub,T,roots)
 if not cuts:
  assert c['index'] not in stored;continue
 s=stored[c['index']];assert {v['coordinate'] for v in s['cuts']}==set(cuts)
 for cut in s['cuts']:
  j=cut['coordinate'];f,b,ub,T,roots=cuts[j]
  assert (f,b,ub,T)==(cut['omitted_A'],cut['included_A'],cut['omitted_B'],set(cut['targets_global']))
  assert len(cut['good_roots'])==len(roots) and {r['root_global'] for r in cut['good_roots']}==roots
  def project(v):return sum(((v>>k)&1)<<(k-(k>j)) for k in range(6) if k!=j)
  for r in cut['good_roots']:
   assert r['registry_index'] in accepted
   row=reg['rows'][r['registry_index']];q=r['certificate_to_projected_permutation'];assert sorted(q)==list(range(5))
   def pm(v):return sum(((v>>i)&1)<<q[i] for i in range(5))
   assert (pm(row['holes'][1]),pm(row['holes'][2]),*sorted(pm(t) for t in row['targets']),pm(row['root']))==(project(b^f),project(f),*sorted(project(t^f) for t in T),project(r['root_global']^f))
   total_transports+=1
 # Independently build the remaining COMPLETE graph by removing incident
 # cross-side edges for each certified A root; no shortness/parity restriction.
 adj={v:set(V)-{v} for v in V}
 for j,(_,_,_,_,roots) in cuts.items():
  B={v for v in V if v&(1<<j)}
  for d in roots:
   for w in B:adj[d].discard(w);adj[w].discard(d)
 rem=set(V);components=[]
 while rem:
  todo={min(rem)};comp=set()
  while todo:
   v=todo.pop();comp.add(v);todo.update(adj[v]-comp)
  rem-=comp;components.append(sorted(comp))
 assert [len(S) for S in components]==s['component_sizes']
 odd=[S for S in components if len(S)%2]
 assert bool(odd)==('odd_component' in s)
 if odd:
  assert s['odd_component'] in odd;closed.add(c['index'])
 summary.append(dict(core_index=c['index'],components=components))
assert closed=={x['core_index'] for x in proof['closed_cores']} and len(closed)==24
base=read('Q6_T15_S2_COMBINED_EXTENSION_REVIEW.json');old=set(base['union_closed_core_indices']);assert len(old)==1009
new=closed-old;assert len(new)==8
remaining=[x for x in profile['choice_sets'] if not old.intersection(x['choices'])]
gain=sum(x['count'] for x in remaining if closed.intersection(x['choices']))
assert gain==proof['additional_parent_configurations']==183576
assert sum(x['count'] for x in remaining)-gain==proof['remaining_with21']==98366
for cid,bad in [(114,6),(117,30)]:
 c=profile['orbits'][cid];swap=lambda v:(v&~3)|((v&1)<<1)|((v&2)>>1)
 assert {swap(v) for v in c['included']}==set(c['included']) and {swap(v) for v in c['omitted']}==set(c['omitted'])
 assert bad&3 and swap(bad)&3
 assert {v for v in {0,*c['included'],*c['omitted']} if v&3==0}=={0}
# Generator-group BFS builds independent orbit-domain keys for the binary filter.
def norm(t):return tuple(sorted(t[:3]))+tuple(sorted(t[3:]))
allkeys={}
with (R/'Q6_T15_GOOD_ROOT_COMPONENTS_REVIEW_keys.txt').open('w') as f:
 for c in profile['orbits']:
  start=norm(c['included']+c['omitted']);seen={start};queue=[start]
  for cfg in queue:
   for j in range(5):
    z=norm(tuple(v if (v>>j&1)==(v>>(j+1)&1) else v^(3<<j) for v in cfg))
    if z not in seen:seen.add(z);queue.append(z)
  assert len(seen)==c['size']
  for cfg in seen:
   key=sum(v<<(6*k) for k,v in enumerate(cfg));assert key not in allkeys;allkeys[key]=c['index']
   f.write(f'{key} {c["index"]} {int(c["index"] in closed)} {int(c["index"] in old)}\n')
assert len(allkeys)==1055600
dump('Q6_T15_GOOD_ROOT_COMPONENTS_REVIEW_geometry.json',dict(verdict='PASS',all_preprocessed_cores=2229,cores_with_candidates=len(stored),all_transports=total_transports,closed_core_indices=sorted(closed),new_core_indices=sorted(new),union_closed_core_indices=sorted(old|closed),additional_parent_configurations=gain,remaining_with21=98366,all_complete_graph_components=summary,orbit_keys=len(allkeys)))
print('PASS',len(closed),len(new),gain,total_transports,flush=True)
