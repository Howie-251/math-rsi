"""Independent bounded multiplicity recursion; no layout/probability calculations."""
from pathlib import Path
from itertools import combinations
from collections import Counter
import json,time
H=Path(__file__).parent
st=time.time();base=json.loads((H/'DOMAIN.json').read_text());ex=json.loads((H/'EXTENDED_COVERAGE.json').read_text());pairs=list(combinations(range(7),2));missing={(0,1),(0,2),(3,4),(5,6)}
# Generate actual edge multisets by multiplicity with remaining vertex capacities.
valid=set()
def gen(k,left,caps,seq):
 if left==0:valid.add(tuple(seq));return
 if k==len(pairs):return
 i,j=pairs[k]
 for q in range(min(left,caps[i],caps[j])+1):
  cp=caps.copy();cp[i]-=q;cp[j]-=q;gen(k+1,left-q,cp,seq+[k]*q)
gen(0,5,[5]+[3]*6,[])
assert valid=={tuple(r['edge_indices']) for r in base['labelled']}
# Generate the true automorphism group by four structural generators.
gens=[(0,2,1,3,4,5,6),(0,1,2,4,3,5,6),(0,1,2,3,4,6,5),(0,1,2,5,6,3,4)]
group={tuple(range(7))};todo=list(group)
while todo:
 p=todo.pop()
 for g in gens:
  q=tuple(g[p[i]] for i in range(7))
  if q not in group:group.add(q);todo.append(q)
assert len(group)==16
assert group=={tuple(p) for p in json.loads((H/'BASELINE_COVERAGE.json').read_text())['automorphisms']}
keys=set();tally=Counter()
def predicate(edges):
 s=Counter(v for e in edges for v in e);co=Counter(edges);a=b=c=False
 for u,v in combinations(range(1,7),2):
  if (u,v) in missing:continue
  a|=s[u]==s[v]==3 and co[u,v]>0
  b|={s[u],s[v]}=={2,3} and co[u,v]==1
  c|=s[u]==s[v]==2 and co[u,v]==0
 d=s[0]==5
 e=any((u,v) not in missing and all(u in edge or v in edge for edge in edges) for u,v in pairs)
 f=any((u,v) in missing and s[u]==s[v]==3 and co[u,v]==3 for u,v in combinations(range(1,7),2))
 g=any((u,v) not in missing and {s[u],s[v]}=={2,3} and co[u,v]==2 for u,v in combinations(range(1,7),2))
 return a,b,c,d,e,f,g
for r in base['orbits']:
 edges=[tuple(e) for e in r['edges']];orbit={tuple(sorted(tuple(sorted((p[u],p[v]))) for u,v in edges)) for p in group};key=min(orbit)
 assert key not in keys;keys.add(key);assert len(orbit)==r['labelled_count']
 out=predicate(edges)
 for name,t in [('ABCD',4),('ABCDE',5),('ABCDEF',6),('ABCDEFG',7)]:
  covered=any(out[:t]);tally[name+'_covered_orbits']+=covered;tally[name+'_covered_labelled']+=covered*len(orbit)
# Verify every stored representative-to-input transport, not just orbit totals.
for r in base['labelled']:
 p=r['from_representative_permutation'];assert tuple(p) in group
 e=base['orbits'][r['orbit']]['edges'];got=sorted(tuple(sorted((p[u],p[v]))) for u,v in e)
 assert got==[pairs[k] for k in r['edge_indices']]
for k,v in ex['counts'].items():assert tally[k]==v
for name,t in [('ABCDE',5),('ABCDEF',6),('ABCDEFG',7)]:
 expected={r['id'] for r in base['orbits'] if not any(predicate([tuple(e) for e in r['edges']])[:t])}
 assert expected=={r['id'] for r in ex['survivors'][name]}
assert len(keys)==3326
out=dict(result='PASS',valid_labelled=len(valid),orbits=len(keys),automorphism_order=len(group),all_stored_transports_checked=len(base['labelled']),counts=dict(tally),elapsed_seconds=time.time()-st)
(H/'REPLAY.json').write_text(json.dumps(out,indent=2)+'\n');print(out)
