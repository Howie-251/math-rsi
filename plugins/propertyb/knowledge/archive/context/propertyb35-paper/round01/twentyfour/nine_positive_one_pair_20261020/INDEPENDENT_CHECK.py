"""Independent stdlib: directsubset counts; star E6 domain vs orbit-image set.
Imports no discovery or previousgenerator code. Old981 is an established input
catalogue; this checker verifies the complete newmarked keys and newarithmetic.
"""
from pathlib import Path
from itertools import combinations,permutations,product
from collections import Counter
import json,time
HERE=Path(__file__).resolve().parent;start=time.process_time();EDGES=list(combinations(range(6),2));EI={e:i for i,e in enumerate(EDGES)}
old=json.loads((HERE.parent/'positive_occ_three/nine_positive_joint_negative_budget_20261020/six_label_pilot/CENSUS_PROFILE.json').read_text())['rows']
cache={}
def masks(g,marks):
 degree=[0]*6;out=[]
 for (i,j),w in zip(EDGES,g):degree[i]+=w;degree[j]+=w;out.extend([(1<<i)|(1<<j)]*w)
 for i in range(6):out.extend([1<<i]*(4-int(i in marks)-degree[i]))
 return out

def direct(g,marks):
 key=(tuple(g),tuple(marks))
 if key in cache:return cache[key]
 M=masks(g,marks);c3=sum(a|b|c==63 for a,b,c in combinations(M,3));c4=d4=0
 for a,b,c,d in combinations(M,4):
  if a|b|c|d!=63:continue
  c4+=1
  if a|b|c!=63 and a|b|d!=63 and a|c|d!=63 and b|c|d!=63:d4+=1
 cache[key]=(c3,c4,d4);return cache[key]

stats=[]
for name,marksizes,maxm,boundconstant in [('LOW_ENDPOINT_PROFILE',(1,2),4,29),('HIGH_SHARED_PROFILE',(0,1,2,3),3,23)]:
 source=json.loads((HERE/(name+'.json')).read_text());actual={(tuple(r['graph']),tuple(r['marked_three_labels'])):r for r in source['rows']}
 expected=set()
 for row in old:
  if row['M3']>maxm:continue
  for k in marksizes:
   for marked in combinations(range(6),k):
    if any(row['degrees'][v]>3 for v in marked) or 24-k-row['E']>15:continue
    expected.add((tuple(row['vector']),marked))
 assert len(actual)==len(source['rows']) and set(actual)==expected
 minimum=10**9
 for (g,marked),r in actual.items():
  c3,c4,d4=direct(g,marked)
  assert (c3,c4,d4)==(r['C3'],r['C4'],r['minimal_C4'])
  assert r['block_bound']==boundconstant-4*c3
  assert d4>r['block_bound'];minimum=min(minimum,d4-r['block_bound'])
 stats.append({'profile':name,'complete_marked_keys':len(actual),'direct_minimum_margin':minimum})

# Independently generate E6 domain via onecomplete forwardstar at a time.
CAP=[3]*3+[4]*3;g=[0]*15;remaining=CAP.copy();labels=set()
def stars(v,left):
 if v==5:
  if left:return
  m3=0
  # Direct tripleedge labels: each covers6 labels iff it is a perfectmatching.
  expanded=[]
  for (i,j),w in zip(EDGES,g):expanded.extend([(1<<i)|(1<<j)]*w)
  m3=sum(a|b|c==63 for a,b,c in combinations(expanded,3))
  if m3<=3:labels.add(tuple(g))
  return
 slots=list(range(v+1,6))
 def assign(k,used):
  if k==len(slots):stars(v+1,left-used);return
  w=slots[k];idx=EI[(v,w)]
  for mult in range(min(left-used,remaining[v],remaining[w])+1):
   g[idx]=mult;remaining[v]-=mult;remaining[w]-=mult
   assign(k+1,used+mult)
   remaining[v]+=mult;remaining[w]+=mult
  g[idx]=0
 assign(0,0)
stars(0,6)
e6=json.loads((HERE/'E6_PROFILE.json').read_text());orbit_union=set();e6bad=[];m0row=[]
PERMS=[p+q for p in permutations(range(3)) for q in permutations(range(3,6))]
def image(g,p):
 out=[0]*15
 for i,(a,b) in enumerate(EDGES):out[EI[tuple(sorted((p[a],p[b])))]]=g[i]
 return tuple(out)
for r in e6['rows']:
 g=r['graph'];orb={image(g,p) for p in PERMS}
 assert len(orb)==r['orbit_size'] and not orb&orbit_union;orbit_union|=orb
 c3,c4,d4=direct(g,(0,1,2));assert (c3,c4,d4)==(r['C3'],r['C4'],r['minimalC4'])
 if r['M2']==0:m0row.append(r);continue
 if d4<=23-4*c3:e6bad.append(r)
assert len(labels)==19916 and orbit_union==labels and len(e6['rows'])==741
assert len(m0row)==1 and len(e6bad)==3

# Verify exactly the threebad pattern candidatepair families.
shapes=[]
for r in e6bad:
 g=r['graph'];M=masks(g,(0,1,2));A=[{i for i,m in enumerate(M) if m>>v&1} for v in range(6)]
 iso=[v for v in range(6) if all(not w or v not in e for e,w in zip(EDGES,g))]
 assert iso==[0,1] and [len(A[v]) for v in iso]==[3,3]
 outside=set(range(15))-A[0]-A[1]
 H={p for p in combinations(sorted(outside),2) if all(set(p)&A[v] for v in range(2,6))}
 assert len(H)==2
 HD=Counter(v for p in H for v in p);freq=Counter(v for a in A for v in a)
 assert all(freq[v]==2 for v in HD)
 if sorted(HD.values())==[1,1,2]:
  typ='K1,2';block=max(5+t+u for t in range(4) for u in range(t+1));assert block==11<18
 else:
  assert sorted(HD.values())==[1,1,1,1];typ='2K2'
  block=max(3*x+y+z for x in range(4) for y in range(4-x) for z in range(11) if 2*x+y+2*z<=20);assert block==16<18
 shapes.append({'graph':g,'pairfamily':list(H),'shape':typ,'degree_budget_block':block,'candidates':18})

r=m0row[0];M=masks(r['graph'],(0,1,2));A=[{i for i,m in enumerate(M) if m>>v&1} for v in range(6)]
R5=[q for q in combinations(range(15),5) if all(set(q)&a for a in A)]
assert len(R5)==324
c3=Counter(t for q in R5 for t in combinations(q,3));c4=Counter(t for q in R5 for t in combinations(q,4))
assert max(c3.values())==12 and max(c4.values())==4 and 3*12+13*4==88<324
out={'status':'PASS','old981_profiles':stats,'direct_count_keys_cached':len(cache),
 'E6_independent_star_labelled_domain':len(labels),'E6_savedorbit_count':741,'E6_complete_key_sets_equal':True,
 'E6_three_degree_budget_patterns':shapes,'E6_M2zero_C5':324,'E6_M2zero_max_T3_extension':12,'E6_M2zero_max_B4_extension':4,
 'scope':__doc__,'cpu_seconds':time.process_time()-start}
(HERE/'INDEPENDENT_RESULT.json').write_text(json.dumps(out,indent=2)+'\n');print(out)
