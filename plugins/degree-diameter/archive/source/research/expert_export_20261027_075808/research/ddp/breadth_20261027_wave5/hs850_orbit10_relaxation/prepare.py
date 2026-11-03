from pathlib import Path
from collections import defaultdict,Counter
import json,time

P=Path(__file__).resolve().parent
t=time.process_time()
screen=json.loads((P/'SCREEN.json').read_text())
assert screen['status']=='SYMBOLIC_CAPACITY_PASSES_NOT_EXISTENCE'
slots=[]
for r,record in enumerate(screen['roots']):
    for target in record['slots']:
        if target['kind']!='nonadjacent':continue
        families=defaultdict(int)
        for form in target['forms']:families[tuple(form['coeff'])]|=1<<form['constant']
        assert len(families)==7
        slots.append((r,target['target'],families))
assert len(slots)==420
with (P/'families.txt').open('w') as f:
    print(26,len(slots),file=f)
    for root,target,families in slots:
        print(root,25*target[0]+5*target[1]+target[2],len(families),file=f)
        for coeff,mask in sorted(families.items()):
            terms=[(i,c if c<=8 else c-17) for i,c in enumerate(coeff) if c]
            print(mask,len(terms),*(v for term in terms for v in term),file=f)

def gi(i,k):return 10+(i-1)*4+k-1 if i and k else None
def vertex(l,i,j,z):return (25*l+5*i+j%5)*17+z%17
def graph(params):
    X=screen['X_sets'];adj=[set() for _ in range(850)]
    def edge(u,v):
        assert u!=v
        adj[u].add(v);adj[v].add(u)
    for i in range(5):
        for j in range(5):
            for z in range(17):
                edge(vertex(0,i,j,z),vertex(0,i,j+1,z+params[i]))
                edge(vertex(1,i,j,z),vertex(1,i,j+2,z+params[5+i]))
                for k in range(5):
                    gamma=params[gi(i,k)] if gi(i,k) is not None else 0
                    for c in X[(k-i)%5]:edge(vertex(0,i,j,z),vertex(1,k,j+i*k,z+gamma+c))
    assert all(len(row)==12 for row in adj)
    return adj
zero=[0]*26
adj=graph(zero);roots=[85*i for i in range(10)]
direct=[]
for root in roots:
    seen={root}
    for _ in range(3):seen|={v for u in seen for v in adj[u]}
    direct.append(850-len(seen))
symbolic=[0]*10
for root,target,families in slots:
    covered=0
    for mask in families.values():covered|=mask
    symbolic[root]+=17-covered.bit_count()
assert direct==symbolic
preflight=dict(status='MATCH',parameters=zero,root_vertex_ids=roots,direct_depth3_misses=direct,
               sparse_symbolic_misses=symbolic,total_representative_misses=sum(direct),
               generated_vertices=850,generated_edges=sum(map(len,adj))//2,all_degrees=12,
               scope='one all-zero parameter graph, exact depth-three expansion from ten proved translation-orbit roots; not all-850-source final BFS',
               CPU_seconds=time.process_time()-t)
(P/'preflight.json').write_text(json.dumps(preflight,indent=2)+'\n')
fixed=dict(starts=4,proposals_per_start=25000,worker_count=1,search_CPU_cutoff_seconds=85,
           all_task_CPU_limit_seconds=90,seeds=[202610270700,202610270701,202610270702,202610270703],
           start0='all 26 parameters zero',other_starts='uniform fixed-seed xorshift64 values mod17',
           moves='choose one of 26 parameters uniformly, replace by one of the other 16 residues',
           energy='sum of exact missing z residues over all 420 nonadjacent slots of ten proved orbit representatives',
           temperature='12*(0.05/12)^(proposal/24999)',new_variants_after_this_batch=False)
(P/'preset.json').write_text(json.dumps(fixed,indent=2)+'\n')
print(json.dumps(preflight,indent=2))
