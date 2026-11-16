"""Independent edge parser/count/retention and finite-array structural checks.
No imports from supplied reproduction or verification code; no all-root BFS.
"""
from pathlib import Path
from array import array
from collections import Counter
import argparse, json, time
start=time.process_time()
parser=argparse.ArgumentParser(description=__doc__)
parser.add_argument('--archive',type=Path,required=True,help='Read-only source archive root')
parser.add_argument('--reconstructed',type=Path,required=True,help='Previously reconstructed graphs directory')
parser.add_argument('--output',type=Path,required=True,help='Explicit external output JSON path; existing original receipts should be preserved')
args=parser.parse_args()
source=args.archive
reconstructed=args.reconstructed
def graph(path):
    with path.open() as f:
        n,m=map(int,next(f).split()); edges=set(); degree=[0]*n; rows=0
        for line in f:
            u,v=map(int,line.split()); assert 0<=u<v<n
            assert (u,v) not in edges
            rows+=1;edges.add((u,v));degree[u]+=1;degree[v]+=1
    assert rows==m and sum(degree)==2*m
    return n,edges,degree
result={'graphs':[]}
for name,cap in [('graph_d11_D5_n37632.edges',11),('graph_d12_D5_n42433.edges',12)]:
    n,e,d=graph(source/'graphs'/name)
    nn,ee,dd=graph(reconstructed/name);assert (n,e,d)==(nn,ee,dd)
    assert max(d)==cap
    result['graphs'].append(dict(file=name,n=n,m=len(e),simple=True,maximum_degree=max(d),minimum_degree=min(d),degree_histogram=dict(Counter(sorted(d))),reconstructed_exact=True))
    if cap==12:
        sn,se,sd=graph(source/'inputs/d12_source42402.edges')
        assert se=={(u,v) for u,v in e if v<sn}
        added=[]
        for v in range(sn,n):
            ns=sorted(u if w==v else w for u,w in e if u==v or w==v)
            row=json.loads((source/'inputs/d12_additions.json').read_text())[v-sn]
            # Later insertions may also use v; compare its neighbors at insertion.
            assert [u for u in ns if u<v]==sorted(row['pins'])
            added.append({'vertex':v,'earlier_neighbors':len([u for u in ns if u<v]),'final_degree':len(ns)})
        result['d12_retention']={'all_source_edges_retained':True,'old_induced_subgraph_exact':True,'source_n':sn,'source_m':len(se),'new_edges':len(e-se),'added':added}
    else:
        sn,se,sd=graph(source/'inputs/h9_source37631.edges')
        result['d11_edits']={'removed_old_edges':len(se-e),'added_edges':len(e-se),'old_exterior_exact':{(u,v)for u,v in se if v>=37471}=={(u,v)for u,v in e if 37471<=v<37631}}
        assert result['d11_edits']=={'removed_old_edges':186,'added_edges':223,'old_exterior_exact':True}
def data(name,kind):
    x=array(kind);x.frombytes((source/'inputs'/name).read_bytes())
    import sys
    if sys.byteorder!='little':x.byteswap()
    return x
N=66430;tau=data('h9_tau.i32.bin','i');pi=data('h9_pi.u16.bin','H');flat=data('h9_line_points.i32.bin','i')
assert len(tau)==2*N and sorted(tau)==list(range(2*N))
assert all((p<N)!=(tau[p]<N) and tau[tau[tau[tau[p]]]]==p for p in range(2*N))
assert set(pi)==set(range(37471))
assert len(flat)==N*10
pointdegrees=[0]*N
lines=[]
for i in range(N):
    row=flat[10*i:10*i+10];assert len(set(row))==10 and all(0<=p<N for p in row)
    lines.append(set(row))
    for p in row:pointdegrees[p]+=1
assert set(pointdegrees)=={10}
# Incidence duality: p incident L iff tau(L) incident tau(p).
for L,row in enumerate(lines):
    assert all(tau[N+L] in lines[tau[p]-N] for p in row)
choice=json.loads((source/'inputs/h9_parameters.json').read_text());cl=json.loads((source/'inputs/fold11_classes.json').read_text())
eps=[0]*N
for fold in cl['split_fold_ids']:
    p=cl['point_representatives'][fold];eps[p]=eps[tau[tau[p]]]=choice['colors'][str(fold)]
assert all(eps[p]==eps[tau[tau[p]]] for p in range(N))
result['h9_array_checks']={'tau_permutation_part_swapping_order_divides4':True,'tau2_fixed_both_parts':sum(tau[tau[p]]==p for p in range(2*N)),'pi_surjective':True,'line_sizes':10,'point_incidence_degrees':10,'tau_incidence_duality_all_flags':True,'eps_phi_constant':True,'geometry_distance6_proof_reexecuted':False}
result['CPU_seconds']=time.process_time()-start
args.output.write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps({k:v for k,v in result.items() if k!='d12_retention'},indent=2))
