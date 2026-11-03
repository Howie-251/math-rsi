"""One read-only labelled edge inclusion comparison; no BFS or isomorphism search."""
from pathlib import Path
from collections import Counter
import json
import lzma
import time

OUT=Path(__file__).resolve().parent
ROOT=OUT.parents[3]
old_path=ROOT/'research/ddp/breadth_20261027_wave3/hexagon_partial_fold_scout/partial_fold_source/graph_d12k5_n41699.edges.xz'
new_path=ROOT/'research/ddp/breadth_20261027_wave4/pencil_source/deg12_diam5_n42342.txt'
started=time.process_time();stride=42342
with lzma.open(old_path,'rt') as f:
    oldn,oldm=map(int,f.readline().split());oldedges=set();olddeg=[0]*oldn
    for line in f:
        if not line.strip():continue
        u,v=map(int,line.split());assert 0<=u<v<oldn
        oldedges.add(stride*u+v);olddeg[u]+=1;olddeg[v]+=1
assert oldn==41699 and len(oldedges)==oldm==237699
rows=[]
for line in new_path.read_text().splitlines():
    if not line.strip() or line.startswith('#'):continue
    values=list(map(int,line.split()));u=values[0];ns=values[1:]
    assert u==len(rows) and u not in ns and len(ns)==len(set(ns))
    rows.append(ns)
assert len(rows)==stride
newedges={stride*u+v for u,row in enumerate(rows) for v in row if u<v}
assert len(newedges)==245217 and sum(map(len,rows))==2*len(newedges)
def edge(code):return divmod(code,stride)
def prefix(es,k):return {a for a in es if a%stride<k}
def sample(es,n=12):return [list(edge(a)) for a in sorted(es)[:n]]
comparisons=[]
for k in [41356,41636,41699]:
    oe=prefix(oldedges,k);ne=prefix(newedges,k)
    comparisons.append(dict(prefix_vertices=k,old_induced_edges=len(oe),new_induced_edges=len(ne),
        common_edges=len(oe&ne),old_edges_missing=len(oe-ne),new_edges_added=len(ne-oe),
        induced_edge_sets_equal=oe==ne,old_edge_set_contained=oe<=ne,
        first_old_edges_missing=sample(oe-ne),first_new_edges_added=sample(ne-oe)))
missing=oldedges-newedges;added=newedges-oldedges
bounds=[0,41356,41636,41699,42177,42342]
names=['old_partial_fold_41356','old_H3copy280_label_range','old_padding63_label_range',
       'additional478_untyped_label_range','final165_untyped_label_range']
def seg(u):return next(i for i in range(5) if bounds[i]<=u<bounds[i+1])
def blockcounts(es):
    c=Counter()
    for a in es:
        u,v=edge(a);c[f'{names[seg(u)]} -- {names[seg(v)]}']+=1
    return dict(sorted(c.items()))
suffix=[]
for k in [41356,41636,41699,42177]:
    cross={a for a in newedges if a//stride<k<=a%stride}
    inner={a for a in newedges if a//stride>=k}
    suffix.append(dict(prefix=k,suffix_vertices=stride-k,
        prefix_induced_edges=len(prefix(newedges,k)),cross_edges=len(cross),suffix_internal_edges=len(inner),
        suffix_degree_histogram=dict(Counter(len(rows[u]) for u in range(k,stride))),
        first_internal_edges=sample(inner)))
result=dict(status='COMPLETE_LABELLED_EDGE_COMPARISON',
    old_source=str(old_path.relative_to(ROOT)),new_source=str(new_path.relative_to(ROOT)),
    old=dict(n=oldn,m=oldm,degree_histogram=dict(Counter(olddeg))),
    current=dict(n=stride,m=len(newedges),degree_histogram=dict(Counter(map(len,rows)))),
    comparison_map='Explicit identity injection of old labels0..41698 into current labels; tested, not assumed geometrically',
    old_all_edges_present=len(missing)==0,old_edges_missing=len(missing),first_old_edges_missing=sample(missing),
    current_edges_not_in_old=len(added),prefix_comparisons=comparisons,
    missing_old_edges_by_numeric_segment=blockcounts(missing),
    added_current_edges_by_numeric_segment=blockcounts(added),suffix_splits=suffix,
    ID_geometry_correspondence_proved=False,graph_isomorphism_or_embedding_search=False,
    BFS_performed=False,source_generators_or_verifiers_executed=False,
    CPU_seconds=time.process_time()-started)
(OUT/'adjacency_comparison.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
