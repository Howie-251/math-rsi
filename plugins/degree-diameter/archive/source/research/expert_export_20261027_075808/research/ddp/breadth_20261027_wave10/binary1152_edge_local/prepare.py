"""Complete controller walk-capacity filter and signed-GF2 initial data."""
from pathlib import Path
from collections import Counter
import json
import time

OUT=Path(__file__).resolve().parent
ROOT=OUT.parents[3]
started=time.process_time()
SOURCE=ROOT/'research/ddp/breadth_20261027_wave5/mizuno_d4_source'
lab=json.loads((SOURCE/'controller72.labels.json').read_text())
construction=json.loads((SOURCE/'construction.json').read_text())
nb=lab['out'];inverse=lab['inverse'];assert lab['n']==72 and inverse==[3,2,1,0]
for u in range(72):
    assert len(set(nb[u]))==4 and u not in nb[u]
    for t,v in enumerate(nb[u]):assert nb[v][inverse[t]]==u
counts=[[[0]*5 for _ in range(72)] for _ in range(72)]
def walks(root,u,k):
    counts[root][u][k]+=1
    if k<4:
        for v in nb[u]:walks(root,v,k+1)
for u in range(72):walks(u,u,0)
capacities=[[sum((1<<k)*counts[u][v][k] for k in range(5)) for v in range(72)] for u in range(72)]
missing=[dict(u=u,v=v,walks_by_length=counts[u][v],endpoint_upper_bound=capacities[u][v])
         for u in range(72) for v in range(72) if capacities[u][v]<16]
unique3=[dict(u=u,v=v,counts=counts[u][v]) for u in range(72) for v in range(72)
         if counts[u][v]==[0,0,0,1,0]]
capacity=dict(status='FAIL' if missing else 'PASS_NECESSARY_ONLY',controller_n=72,
              complete_walks_per_root=341,complete_walks_all_roots=72*341,
              weighted_endpoint_bound='sum_k(2^k*number_of_lengthk_walks),0<=k<=4',
              minimum_endpoint_bound=min(map(min,capacities)),
              capacity_histogram=dict(Counter(x for row in capacities for x in row)),
              missing_slots=missing,unique3_without_other_le4_walks=unique3,
              counts_all_ordered_pairs=counts,CPU_seconds=time.process_time()-started,
              ordinary_BFS_performed=False)
(OUT/'capacity_screen.json').write_text(json.dumps(capacity,indent=2)+'\n')
if missing:
    (OUT/'terminal.json').write_text(json.dumps(dict(status='FIXED_CONTROLLER_WALK_CAPACITY_BLOCKED',
        witness=missing[0],profiles_started=0,graphs_generated=0,BFS_performed=False),indent=2)+'\n')
else:
    def columns(M):return [sum((M[i][j]!=0)<<i for i in range(4)) for j in range(4)]
    def action(cols,x):
        y=0
        for i in range(4):
            if (x>>i)&1:y^=cols[i]
        return y
    cols=[columns(construction['matrices'][t]) for t in (0,1)]
    bs=[sum((x!=0)<<i for i,x in enumerate(construction['control_vectors'][t])) for t in (0,1)]
    for a in cols:assert len({action(a,x) for x in range(16)})==16
    assert all(bs)
    edges=[]
    for u in range(72):
        for t in (0,1):edges.append(dict(u=u,v=nb[u][t],label=t,columns=cols[t],b=bs[t],c=0))
    assert len({tuple(sorted((e['u'],e['v']))) for e in edges})==144
    (OUT/'input.txt').write_text('72 144\n'+''.join(' '.join(map(str,[e['u'],e['v'],e['label'],*e['columns'],e['b'],0]))+'\n' for e in edges))
    plan=dict(status='FROZEN_FINITE_PROFILE',n=1152,degree=8,m=4608,target_D=4,savedL=1100,
              controller_source=str((SOURCE/'controller72.labels.json').relative_to(ROOT)),
              inverse_labels=inverse,controller_out=nb,oriented_edges=edges,
              encoding='vertex=16*controller+x0+2*x1+4*x2+8*x3',
              relation='y=T*x XOR c XOR lambda*b, lambda inF2; reverse freshly recomputed inGF2',
              matrix_encoding='four binary column integers, bit i is row i',
              init0='signed source forward labels0/1:zero->0,nonzero1or2->1; c0; freshGF2 inverse',
              init1='each144edge independent uniformGL4(2),uniform nonzerob,uniformc',
              seeds=[20261027115201,20261027115202],proposals_per_start=1000,
              moves=['replace nonzero b','c XOR one bit','T left multiply one elementary transvection'],
              temperature='800 geometrically to5 over1000',native_CPU_soft_seconds=18,
              native_CPU_hard_seconds=20,workers=1,preparation_CPU_seconds=time.process_time()-started,
              graph_connected_not_assumed=True)
    (OUT/'encoding_and_plan.json').write_text(json.dumps(plan,indent=2)+'\n')
print(json.dumps({k:capacity[k] for k in ['status','minimum_endpoint_bound','complete_walks_all_roots','CPU_seconds']}) )
