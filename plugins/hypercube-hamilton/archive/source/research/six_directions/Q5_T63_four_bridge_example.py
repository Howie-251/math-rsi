"""Fresh Python cycle enumeration checks one zero-crossing four-bridge example."""
from pathlib import Path
from itertools import combinations
import json
P=Path(__file__).resolve().parent
def edge(a,b):return tuple(sorted((a,b)))
def short(a,b):return (a^b).bit_count()==1
def cycles(m,omit):
 units=[(a,b) for a,b in enumerate(m) if b!=255 and a<b]
 units += [(a,) for a,b in enumerate(m) if b==255 and a not in omit]
 first=units[0];answer=[]
 def visit(path,remaining):
  if not remaining:
   if short(path[-1],path[0]):answer.append(tuple(path))
   return
  for j,u in enumerate(remaining):
   for orientation in ([u] if len(u)==1 else [u,u[::-1]]):
    if short(path[-1],orientation[0]):visit(path+list(orientation),remaining[:j]+remaining[j+1:])
 visit(list(first),units[1:]);return answer
def signatures(cycles,m):
 result={}
 for c in cycles:
  opt=[i for i,a in enumerate(c) if m[a]!=c[(i+1)%len(c)]]
  for i,j in combinations(opt,2):
   a,b=c[i],c[(i+1)%len(c)];d,e=c[j],c[(j+1)%len(c)]
   if len({a,b,d,e})!=4:continue
   ports=tuple(sorted((a,b,d,e)))
   pairing=tuple(sorted((edge(b,d),edge(e,a))))
   result[(ports,pairing)]={'cycle':list(c),'deleted':[list(edge(a,b)),list(edge(d,e))]}
 return result
candidate=json.loads((P/'Q5_T63_zero_gluing_exact_probe.json').read_text())['disjoint_stored_union_candidates'][0]
L=candidate['N14_mate'];R=candidate['T44_mate']
CL=cycles(L,{0});CR=cycles(R,set(candidate['T44_omitted']))
UL={edge(a,c[(i+1)%len(c)]) for c in CL for i,a in enumerate(c) if L[a]!=c[(i+1)%len(c)]}
UR={edge(a,c[(i+1)%len(c)]) for c in CR for i,a in enumerate(c) if R[a]!=c[(i+1)%len(c)]}
assert not UL&UR
SL,SR=signatures(CL,L),signatures(CR,R);found=None
for (ports,pairingL),wL in SL.items():
 for (portsR,pairingR),wR in SR.items():
  if ports==portsR and pairingL!=pairingR:
   found={'ports':list(ports),'pairing_A':[list(e) for e in pairingL],
    'pairing_B':[list(e) for e in pairingR],'A':wL,'B':wR};break
 if found:break
out={'status':'PRODUCER_EXAMPLE_CHECKED','scope':'One local N14/T44 pair: one-edge gluing fails but a four-bridge certificate may work',
 'N14_mate':L,'T44_mate':R,'T44_omitted':candidate['T44_omitted'],
 'N14_cycle_count_up_to_reversal':len(CL),'T44_cycle_count_up_to_reversal':len(CR),
 'all_N14_cycles_up_to_reversal':[list(c) for c in CL],
 'all_T44_cycles_up_to_reversal':[list(c) for c in CR],
 'N14_optional_union':sorted(UL),'T44_optional_union':sorted(UR),
 'no_common_optional_edge':not bool(UL&UR),'four_bridge_witness':found}
if found:
 # Embed A at fifth bit 0 and B at fifth bit 1; delete optional edges and attach port mirrors.
 edges=set()
 for side,w in ((0,found['A']),(16,found['B'])):
  c=w['cycle'];deleted={tuple(e) for e in w['deleted']}
  edges|={edge(a|side,c[(i+1)%len(c)]|side) for i,a in enumerate(c) if edge(a,c[(i+1)%len(c)]) not in deleted}
 edges|={edge(x,x|16) for x in found['ports']}
 vertices=set(range(32))-{0,*[x|16 for x in candidate['T44_omitted']]}
 adj={x:set() for x in vertices}
 for a,b in edges:adj[a].add(b);adj[b].add(a)
 assert len(edges)==29 and all(len(n)==2 for n in adj.values())
 sequence=[min(vertices)];previous=None
 while True:
  x=sequence[-1];n=next(y for y in adj[x] if y!=previous)
  if n==sequence[0]:break
  assert n not in sequence;sequence.append(n);previous=x
 assert set(sequence)==vertices
 original={edge(a,b) for a,b in enumerate(L) if b!=255}|{edge(a|16,b|16) for a,b in enumerate(R) if b!=255}
 assert original<=edges and all(short(a,b) for a,b in edges-original)
 out['global_positive_29cycle']=sequence
(P/'Q5_T63_four_bridge_example.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({k:v for k,v in out.items() if k not in ('N14_optional_union','T44_optional_union','N14_mate','T44_mate')},indent=2))
