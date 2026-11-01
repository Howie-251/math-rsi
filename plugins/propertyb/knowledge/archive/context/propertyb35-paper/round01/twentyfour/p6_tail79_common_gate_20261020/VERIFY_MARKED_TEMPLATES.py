"""Independent conditional-IE replay of unchanged oldtemplates with3label mark."""
from pathlib import Path
from itertools import combinations
from math import comb
import json,time
HERE=Path(__file__).resolve().parent;BASE=HERE.parent/'positive_occ_three';start=time.process_time()
found=json.loads((HERE/'CHECK_MIXED_EIGHT.json').read_text());rows={r['name']:r for r in found['rows']}
expected={}
def fromvector(vector,mark):
 sets=[set() for _ in range(5)];degree=[0]*5;p=0
 for (i,j),w in zip(combinations(range(5),2),vector):
  degree[i]+=w;degree[j]+=w
  for _ in range(w):sets[i].add(p);sets[j].add(p);p+=1
 if degree[mark]>3:return None
 for i in range(5):
  for _ in range(4-int(i==mark)-degree[i]):sets[i].add(p);p+=1
 return sets
for i,r in enumerate(json.loads((BASE/'eighteen_one_triple/THREE_EDGE_CHECK.json').read_text())['results']):
 for mark in range(5):
  A=fromvector(r['vector'],mark)
  if A:expected['old7_%d_mark%d'%(i,mark)]=A
for i,r in enumerate(json.loads((BASE/'five_graph_catalogue.json').read_text())['graphs']):
 for mark in range(5):
  A=fromvector(r['edge_vector'],mark)
  if A:expected['old86_%d_mark%d'%(i,mark)]=A
for i,r in enumerate(json.loads((BASE/'eight_mixed_eighteen/SMALL_GRAPH_CHECK.json').read_text())['rows']):
 if r['E']==2:expected['old59_%d_E2'%i]=list(map(set,r['sets']))
assert set(rows)==set(expected) and len(rows)==384
bad=[];comparisons=0
for key,A in expected.items():
 r=rows[key];assert [sorted(a) for a in A]==r['sets']
 U=set.union(*A);N=len(U);unions={m:set.union(set(),*[A[i] for i in range(5) if m>>i&1]) for m in range(32)}
 def choose(n,k):return comb(n,k) if n>=k else 0
 c={k:sum((-1)**m.bit_count()*choose(N-len(unions[m]),k) for m in range(32)) for k in (3,4)}
 assert (c[3],c[4])==(r['C3'],r['C4'])
 prefix={3:[],4:[]}
 for pair in combinations(sorted(U),2):
  F=set(pair);missing=sum(1<<i for i,a in enumerate(A) if not a&F)
  for k in (3,4):
   z=0;s=missing
   while True:
    z+=(-1)**s.bit_count()*choose(N-2-len(unions[s]),k-2)
    if not s:break
    s=(s-1)&missing
   prefix[k].append(z)
 for k in (3,4):
  prefix[k]=[sum(sorted(prefix[k],reverse=True)[:u]) for u in range(3)]
  assert prefix[k]==r['C%d_pair_prefix'%k]
 h3=0
 for tri in combinations(sorted(U),3):
  F=set(tri);miss=[a for a in A if not a&F]
  possible=set.intersection(*miss) if miss else U
  h3=max(h3,len(possible-F))
 assert h3==r['h3']
 failures=[]
 for t in range(3):
  for u in range(t+1):
   for v in range(5-u):
    B3=prefix[3][u]+t-u+v;B4=prefix[4][u]+(t-u+v)*h3+19-v
    if c[3]<=B3 and c[4]<=B4:failures.append((u,t,v,19,B3,B4))
    comparisons+=1
 stored=[(p['r'],p['t'],p['v'],p['b'],p['block3'],p['block4']) for p in r['nongated_parameters']]
 assert failures==stored
 if failures:bad.append(key)
assert set(bad)=={'old59_0_E2','old59_15_E2'}
out={'status':'PASS','old_template_keys_complete':384,'E3_marked_rows':sum(k.startswith('old7_') for k in rows),'E4plus_marked_rows':sum(k.startswith('old86_') for k in rows),'old59_E2_rows':2,'parameter_checks':comparisons,'only_raw_bound_failures':bad,'conditional_IE_pair_and_intersection_triple_counts_independent':True,'cpu_seconds':time.process_time()-start}
(HERE/'VERIFY_MARKED_TEMPLATES.json').write_text(json.dumps(out,indent=2)+'\n');print(out)
