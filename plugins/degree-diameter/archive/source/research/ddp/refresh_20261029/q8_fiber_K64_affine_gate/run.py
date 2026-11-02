#!/usr/bin/env python3
import itertools,json,os,time
from pathlib import Path
HERE=Path(__file__).resolve().parent
assert not (HERE/'TERMINAL.json').exists(), 'Do not rerun closed gate'
start=time.process_time();wall=time.monotonic();ALL=(1<<64)-1
sigma=[v^((v&30)>>1)^16 for v in range(64)]
assert sorted(sigma)==list(range(64));inverse=[0]*64
for v,w in enumerate(sigma):inverse[w]=v
cycles=[];unseen=set(range(64))
while unseen:
 v=min(unseen);cyc=[];w=v
 while w not in cyc:cyc.append(w);unseen.remove(w);w=sigma[w]
 assert w==v and len(cyc)==8;cycles.append(cyc)

def rank(vectors):
 p={}
 for v in vectors:
  for bit in range(5,-1,-1):
   if v>>bit&1:
    if bit in p:v^=p[bit]
    else:p[bit]=v;break
 return len(p)
# Actual columns of A-I are N(e_i).
assert rank([((v&30)>>1) for v in [1,2,4,8,16,32]])==4
(HERE/'INPUT.json').write_text(json.dumps(dict(sigma=sigma,inverse=inverse,cycles=cycles,A_minus_I_rank=4,cokernel_bits=[4,5],coarse_quotient='K4 with repeated generator',coset0=list(range(32,48)),coset1=list(range(48,64)),raw_scope=3840),indent=2)+'\n')
handle=dict(status='RUNNING',pid=os.getpid(),worker_count=1,CPU_budget_seconds=30,raw_scope=3840)
(HERE/'HANDLE.json').write_text(json.dumps(handle,indent=2)+'\n');print(json.dumps(handle),flush=True)
rows=[];counts=[0,0];checks=0;found=None;timedout=False;fail_hist={}
with (HERE/'CASES.jsonl').open('w') as log:
 for branch in range(2):
  pair=range(32,48) if branch==0 else range(48,64)
  single=range(48,64) if branch==0 else range(32,48)
  for a,b in itertools.combinations(pair,2):
   for c in single:
    if time.process_time()-start>=29.5:timedout=True;break
    S=sorted([a,b,c]);assert rank(S)==3
    adj=[]
    for v in range(64):
     ns=[v^s for s in S]+[sigma[v],inverse[v]]
     assert len(set(ns))==5 and v not in ns
     adj.append(ns)
    assert all(v in adj[w] for v in range(64) for w in adj[v])
    masks=[sum(1<<w for w in ns) for ns in adj]
    spectra=[];failure=None
    for root in range(64):
     checks+=1;seen=front=1<<root;hist=[1]
     for distance in range(1,4):
      neighbors=0
      while front:
       bit=front&-front;front^=bit;neighbors|=masks[bit.bit_length()-1]
      front=neighbors&~seen;seen|=front;hist.append(front.bit_count())
     spectra.append(hist)
     if seen!=ALL:
      failure=dict(root=root,reached=seen.bit_count(),first_missing=((~seen&ALL)&-(~seen&ALL)).bit_length()-1)
      fail_hist[root]=fail_hist.get(root,0)+1;break
    counts[branch]+=1
    rec=dict(cursor=sum(counts)-1,branch=branch,S=S,roots_checked=len(spectra),PASS=failure is None,failure=failure)
    log.write(json.dumps(rec)+'\n')
    if failure is None:
     complement=[];basis=S[:]
     for e in [1,2,4,8,16,32]:
      if rank(basis+[e])>len(basis):basis.append(e);complement.append(e)
      if len(basis)==6:break
     assert len(complement)==3
     map_a_l=[]
     for aa in range(8):
      for ll in range(8):
       v=0
       for i in range(3):
        if aa>>i&1:v^=complement[i]
        if ll>>i&1:v^=S[i]
       map_a_l.append(v)
     assert sorted(map_a_l)==list(range(64))
     inverse_map=[None]*64
     for code,v in enumerate(map_a_l):inverse_map[v]=[code//8,code%8]
     assert all(map_a_l[8*aa+(ll^(1<<i))]==(map_a_l[8*aa+ll]^S[i]) for aa in range(8) for ll in range(8) for i in range(3))
     edges=[(v,w) for v in range(64) for w in adj[v] if v<w];assert len(edges)==160
     (HERE/'K64.edges').write_text('64 160\n'+''.join(f'{u} {v}\n' for u,v in edges))
     found=dict(S=S,sigma=sigma,inverse=inverse,n=64,m=160,degree=5,diameter=3,roots_checked=64,root_distance_spectra=spectra,complement_basis=complement,field_basis_Xprime=[1,2,4],coordinate_to_vertex=map_a_l,vertex_to_coordinate=inverse_map,pencil_cubes_verified=True,candidate=rec)
     (HERE/'K64_PARAMETERS.json').write_text(json.dumps(found,indent=2)+'\n')
     print('FOUND_K64 '+json.dumps(rec),flush=True);break
   if found or timedout:break
  if found or timedout:break
status='FOUND_K64_D3' if found else 'CPU_LIMIT_PREFIX_SAVED' if timedout else 'COMPLETE_3840_NO_K64_D3'
result=dict(status=status,running=False,raw_scope=3840,candidates_evaluated=sum(counts),branch_counts=counts,full_scope_completed=sum(counts)==3840,root_checks=checks,first_failed_root_histogram=fail_hist,found=found is not None,positive_parameters='K64_PARAMETERS.json' if found else None,large_graphs_generated=0,large_graph_BFS=0,worker_count=1,CPU_seconds=time.process_time()-start,wall_seconds=time.monotonic()-wall,next_cursor=sum(counts) if timedout else None,scope='Only fixedJ5+I1 affine permutation and specified two-coset triples',pending=['Parent1088 construction and independent validation'] if found else [])
(HERE/'TERMINAL.json').write_text(json.dumps(result,indent=2)+'\n');handle.update(status=status,running=False);(HERE/'HANDLE.json').write_text(json.dumps(handle,indent=2)+'\n');print(json.dumps(result,indent=2),flush=True)
