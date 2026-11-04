"""Positive four-port witnesses on the complete 1320-pair exception domain."""
from pathlib import Path
from itertools import combinations
from functools import lru_cache
from collections import Counter
import json,hashlib
P=Path(__file__).resolve().parent
def edge(a,b):return tuple(sorted((a,b)))
def short(a,b):return (a^b).bit_count()==1
@lru_cache(None)
def cycles(m,omit):
 units=[(a,b) for a,b in enumerate(m) if b!=255 and a<b]
 units += [(a,) for a,b in enumerate(m) if b==255 and a not in omit]
 answer=[]
 def visit(path,left):
  if not left:
   if short(path[-1],path[0]):answer.append(tuple(path))
   return
  for j,u in enumerate(left):
   for orient in ([u] if len(u)==1 else [u,u[::-1]]):
    if short(path[-1],orient[0]):visit(path+orient,left[:j]+left[j+1:])
 visit(units[0],units[1:]);return tuple(answer)
def signatures(cs,m,t):
 result={}
 for c in cs:
  optional=[i for i,a in enumerate(c) if m[a]!=c[(i+1)%len(c)]]
  for cut in combinations(optional,t):
   deleted=tuple(edge(c[i],c[(i+1)%len(c)]) for i in cut)
   ports=tuple(sorted(x for e in deleted for x in e))
   if len(set(ports))!=2*t:continue
   pairing=tuple(sorted(edge(c[(cut[j]+1)%len(c)],c[cut[(j+1)%t]]) for j in range(t)))
   result[(ports,pairing)]=(c,deleted)
 return result
def connected(a,b,ports):
 adjacency={x:set() for x in ports}
 for x,y in a+b:adjacency[x].add(y);adjacency[y].add(x)
 reached={ports[0]};front=list(reached)
 while front:
  for y in adjacency[front.pop()]-reached:reached.add(y);front.append(y)
 return len(reached)==len(ports)
def witness(A,B,omit,t):
 left=signatures(cycles(A,(0,)),A,t);right=signatures(cycles(B,omit),B,t)
 grouped={}
 for (ports,q),w in right.items():grouped.setdefault(ports,[]).append((q,w))
 for (ports,qA),wA in left.items():
  for qB,wB in grouped.get(ports,[]):
   if connected(qA,qB,ports):return ports,qA,qB,wA,wB
def expand(A,B,omit,found):
 ports,qA,qB,(cA,dA),(cB,dB)=found
 edges=set()
 for side,c,deleted in ((0,cA,dA),(16,cB,dB)):
  edges|={edge(a|side,c[(i+1)%len(c)]|side) for i,a in enumerate(c) if edge(a,c[(i+1)%len(c)]) not in deleted}
 edges|={edge(x,x|16) for x in ports}
 vertices=set(range(32))-{0,*[x|16 for x in omit]};adj={x:set() for x in vertices}
 for x,y in edges:adj[x].add(y);adj[y].add(x)
 assert len(edges)==29 and all(len(n)==2 for n in adj.values())
 sequence=[min(vertices)];previous=None
 while True:
  x=sequence[-1];y=next(y for y in adj[x] if y!=previous)
  if y==sequence[0]:break
  assert y not in sequence;sequence.append(y);previous=x
 assert set(sequence)==vertices
 original={edge(a,b) for a,b in enumerate(A) if b!=255}|{edge(a|16,b|16) for a,b in enumerate(B) if b!=255}
 assert len(original)==13 and original<=edges and all(short(a,b) for a,b in edges-original)
 return sequence
raw=(P/'Q5_T63_disjoint_pairs.bin').read_bytes();assert len(raw)==1320*34
cert=bytearray();records=[];failed=[];counts=Counter()
for i in range(1320):
 rec=raw[i*34:i*34+34];A=tuple(rec[:16]);B=tuple(rec[16:32]);omit=tuple(rec[32:])
 found=witness(A,B,omit,2);t=2
 if found is None:found=witness(A,B,omit,3);t=3
 if found is None:failed.append(i);continue
 sequence=expand(A,B,omit,found);cert.extend(rec);cert.extend(sequence);counts[2*t]+=1
 ports,qA,qB,(cA,dA),(cB,dB)=found
 records.append({'input_index':i,'bridges':2*t,'ports':ports,'pairing_A':qA,'pairing_B':qB,
  'A_cycle':cA,'B_cycle':cB,'A_deleted':dA,'B_deleted':dB})
(P/'Q5_T63_exception_positive_cycles.bin').write_bytes(cert)
out={'status':'PRODUCER_ALL_POSITIVE' if not failed else 'PRODUCER_TEMPLATE_FAILURES_REMAIN',
 'input_pairs':1320,'positive':len(records),'failed_template_indices':failed,'bridge_histogram':dict(counts),
 'witnesses':records,'input_sha256':hashlib.sha256(raw).hexdigest(),
 'positive_sha256':hashlib.sha256(cert).hexdigest(),'positive_record_bytes':63,
 'script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
 'independent_review_pending':True,'full_T63_proved':False,'full_P6_proved':False}
(P/'Q5_T63_four_port_complete.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({k:v for k,v in out.items() if k!='witnesses'},indent=2))
