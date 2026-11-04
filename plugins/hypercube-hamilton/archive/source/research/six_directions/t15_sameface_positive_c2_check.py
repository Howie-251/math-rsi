"""Complete c=2, artificial-pq residual kernel. Imports audited Q4 tables.
No random inputs; no search failure is used as a negative certificate.
"""
from pathlib import Path
from itertools import combinations, permutations
from collections import Counter
import hashlib,json
R=Path(__file__).resolve().parent
V=set(range(16));D3=(7,11,13,14)
def e(a,b):return tuple(sorted((a,b)))
def edges(m):return frozenset(e(x,m[x]) for x in range(16) if x<m[x]<16)
def pairs(xs):
 xs=tuple(sorted(xs))
 if not xs:yield frozenset();return
 a=xs[0]
 for b in xs[1:]:
  for t in pairs(x for x in xs if x not in (a,b)):yield t|{e(a,b)}
def tr(x,p):return sum(((x>>i)&1)<<p[i] for i in range(4))
def check_cycle(c,t,z):
 assert len(c)==len(set(c))==14 and set(c)==V-{0,z}
 es=frozenset(e(c[i],c[(i+1)%14]) for i in range(14))
 assert t<=es and all((a^b).bit_count()==1 for a,b in es-t)
def compress(f,z,u,v):
 es=list(f)+[(0,u),(z,v)];adj={x:[] for x in V}
 for i,(a,b) in enumerate(es):adj[a].append((b,i));adj[b].append((a,i))
 if any(len(adj[x])!=(2 if x in (0,z) else 1) for x in V):return None
 used=set();out=set()
 for x in V-{0,z}:
  if adj[x][0][1] in used:continue
  a=x;prev=-1
  while True:
   choices=[(b,k) for b,k in adj[a] if k!=prev]
   if len(choices)!=1:return None
   b,k=choices[0]
   if k in used:return None
   used.add(k);a=b;prev=k
   if a not in (0,z):break
  out.add(e(x,a))
 if len(used)!=len(es):return None
 return frozenset(out)
def witness(m,z,first,port,avoid):
 p,q=port;path=[0];seen=set()
 def rec(x,left):
  if not left:return x==z
  if x==z:return False
  state=(x,left)
  if state in seen:return False
  seen.add(state)
  for bit in (1,2,4,8):
   y=x^bit
   if not left>>y&1:continue
   a=m[y]
   if y in port and y!=first:continue
   path.append(y)
   if a==255:
    if rec(y,left&~(1<<y)):return True
   else:
    path.append(a)
    if rec(a,left&~(1<<y)&~(1<<a)):return True
    path.pop()
   path.pop()
  return False
 assert rec(0,65534&~(1<<avoid[0])&~(1<<avoid[1]))
 assert len(path)==len(set(path))==14 and set(path)==V-set(avoid)
 assert path[0]==0 and path[-1]==z and path.index(first)<path.index(q if first==p else p)
 es=frozenset(e(a,b) for a,b in zip(path,path[1:]));required=edges(m)
 assert required<=es and all((a^b).bit_count()==1 for a,b in es-required)
 return path

def main():
 source=R/'q4_distance3_avoided_table.bin';data=source.read_bytes();assert len(data)==135135*30
 base={}
 for i in range(0,len(data),30):
  m=data[i:i+16];c=data[i+16:i+30];t=edges(m)
  assert len(t)==7 and sorted(x for ab in t for x in ab)==sorted(V-{0,7})
  assert t not in base;base[t]=None if c[0]==255 else tuple(c)
 assert len(base)==135135 and sum(c is None for c in base.values())==53
 tables={}
 for z in D3:
  p=next(p for p in permutations(range(4)) if tr(7,p)==z)
  tables[z]={frozenset(e(tr(a,p),tr(b,p)) for a,b in t):None if c is None else tuple(tr(x,p) for x in c) for t,c in base.items()}
 neg={z:{t for t,c in tables[z].items() if c is None} for z in D3}
 a_records=[];inputs=[]
 for v,w,p,q in ((1,2,4,8),(2,4,1,8)):
  covered=V-{0,7,11,13,v,w};count=0
  for rem in pairs(covered-{p,q}):
   full=rem|{e(p,q)};m=[255]*16
   for a,b in full:m[a]=b;m[b]=a
   ws=[{'z':z,'root_side_port':first,'path':witness(m,z,first,(p,q),(v,w))} for z in D3 for first in (p,q)]
   a_records.append({'avoid':[v,w],'artificial_pair':[p,q],'F_A':sorted(rem),'witnesses':ws});count+=1
  assert count==105
 b_records=[];hist=Counter()
 for y in combinations(range(16),2):
  z=next(z for z in D3 if z not in y);u,v=y
  if u==0:u,v=v,u
  candidates=set()
  for t in neg[z]:
   m={a:b for a,b in t}|{b:a for a,b in t}
   if v==0:
    b=m[u];f=t-{e(u,b)}|{e(z,b)}
   elif m[u]==v:f=t-{e(u,v)}|{e(0,z)}
   else:
    a,b=m[u],m[v];f=t-{e(u,a),e(v,b)}|{e(0,a),e(z,b)}
   assert len(f)==7 and sorted(x for ab in f for x in ab)==sorted(V-set(y))
   assert compress(f,z,u,v)==t;candidates.add(f)
  assert len(candidates)==53
  for f in sorted(candidates,key=lambda f:sorted(f)):
   good=[]
   for zz in D3:
    for uu,vv in (y,y[::-1]):
     t=compress(f,zz,uu,vv)
     if t is not None and tables[zz][t] is not None:
      c=tables[zz][t];check_cycle(c,t,zz);good.append((zz,uu,vv,c))
   assert good,('stalled',y,f)
   zz,uu,vv,c=good[0];hist[len(good)]+=1
   b_records.append({'ports':y,'F_B':sorted(f),'z':zz,'root_side_B_port':uu,'other_B_port':vv,'compressed_cycle':c})
 assert len(a_records)==210 and len(b_records)==6360
 result={'status':'PASS','claim':'c=2 and A ports are the two nonomitted root neighbors; conditional on audited Q4 table completeness', 'scope_excludes':'F_A contains pq; crossing counts 4,6,8; global T15 and P6','imports':{'Q4_T15_CLASSIFICATION.md':'audited theorem','q4_distance3_avoided_table.bin':hashlib.sha256(data).hexdigest()},'A_inputs':len(a_records),'A_positive_paths':sum(len(r['witnesses']) for r in a_records),'B_port_sets':120,'B_inverse_candidates':len(b_records),'B_success_count_histogram':dict(sorted(hist.items())),'A_certificates':a_records,'B_exception_certificates':b_records,'script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
 target=R/'t15_sameface_positive_c2_certificates.json';target.write_text(json.dumps(result,ensure_ascii=False,separators=(',',':'))+'\n',encoding='utf-8')
 print(json.dumps({k:v for k,v in result.items() if k not in ('A_certificates','B_exception_certificates')},ensure_ascii=False,indent=2))
if __name__=='__main__':main()

