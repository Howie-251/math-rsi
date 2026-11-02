"""Current3645 literal binding and localdegree/block diagnostics only; noBFS."""
from pathlib import Path
from collections import Counter
from datetime import datetime,timezone
import json,re,html,time

OUT=Path(__file__).resolve().parent
start=time.process_time()
save=lambda name,d:(OUT/name).write_text(json.dumps(d,indent=2)+'\n')
assert json.loads((OUT/'PREDICTION.json').read_text())['frozen_before_literal_profile']
clean=lambda s:re.sub(r'\s+','',html.unescape(re.sub('<[^>]+>','',s)))
table=(OUT/'public_table.html').read_text()
target=None
for row in re.findall(r'<tr\b[^>]*>(.*?)</tr>',table,re.I|re.S):
    cells=re.findall(r'<t[dh]\b[^>]*>(.*?)</t[dh]>',row,re.I|re.S)
    if cells and clean(cells[0])=='11':target=cells[3];break
assert target
value=int(clean(target));bold=bool(re.search(r'<(?:b|strong)\b',target,re.I))
assert value==3645 and not bold
desc=(OUT/'public_desc_g4.html').read_text(encoding='latin1')
save('BASELINE.json',dict(checked_UTC=datetime.now(timezone.utc).isoformat(),target=[11,4],
    publicL=value,cell_is_bold=bold,cell_html=target,
    main_URL='https://web.mat.upc.edu/francesc.comellas/delta-d/table_degree_diameter.html',
    description_URL='https://web.mat.upc.edu/francesc.comellas/delta-d/desc_g/desc_g4.html',
    description_mentions3645='3645' in desc,description_old_order3444='3444' in desc))
edges=[];adj=[[] for _ in range(3645)]
for line in (OUT/'source3645.edges').read_text().splitlines():
    if not line.strip() or line.startswith('#'):continue
    u,v=map(int,line.split());assert 0<=u<v<3645
    edges.append((u,v));adj[u].append(v);adj[v].append(u)
degrees=list(map(len,adj));assert len(edges)==20044 and max(degrees)==11
free=[v for v,d in enumerate(degrees) if d<11]
sat=[sum(degrees[w]==11 for w in ns) for ns in adj]
def kind(v):return 'pointcopy' if v<1640 else 'linecopy' if v<3280 else 'spreadtwin' if v<3444 else 'insertedlayer'
bytype={}
for k in ['pointcopy','linecopy','spreadtwin','insertedlayer']:
    vertices=[v for v in range(3645) if kind(v)==k]
    bytype[k]=dict(n=len(vertices),degree_histogram=dict(Counter(degrees[v] for v in vertices)))
edge_types=Counter(','.join(sorted((kind(u),kind(v)))) for u,v in edges)
blocks=[];counterexample=None
for b in range(45):
    variants={}
    for v in range(81*b,81*(b+1)):
        sig=tuple(sorted(Counter(w//81 for w in adj[v]).items()))
        variants.setdefault(sig,v)
    blocks.append(dict(block=b,distinct_neighborblock_signatures=len(variants)))
    if len(variants)>1 and counterexample is None:
        a=list(variants.items())[:2]
        counterexample=dict(block=b,vertices=[x[1] for x in a],neighborblock_count_signatures=[list(x[0]) for x in a])
minimum=min(sat)
result=dict(status='CURRENT3645_LITERAL_PROFILE_COMPLETE',source_n=3645,source_m=20044,
    degree_cap=11,target_D=4,savedL=3645,actual_candidate_n=None,actual_candidate_D=None,
    source_degree_histogram=dict(Counter(degrees)),free_vertices=free,free_vertex_count=len(free),
    free_vertex_degrees=[degrees[v] for v in free],free_slots=sum(11-d for d in degrees),
    saturated_neighbor_count_histogram=dict(sorted(Counter(sat).items())),
    min_saturated_neighbors=minimum,min_attaining_vertices=[v for v,c in enumerate(sat) if c==minimum],
    full_spare_star_prototypes=[v for v,c in enumerate(sat) if c==0],
    natural_vertex_types=bytype,edge_type_counts=dict(edge_types),
    naive81_partition=dict(block_count=45,fiber_size=81,non_equitable_blocks=sum(b['distinct_neighborblock_signatures']>1 for b in blocks),
        block_diagnostics=blocks,first_counterexample=counterexample,
        interpretation='Onlycontiguous81labelpartitiontested;authoractualmechanismisW9doubleplus201insertions,notboundasF3^4chart'),
    author_source='https://github.com/f4t4nt/degree-diameter-graphs/tree/main/graphs/deg11/dia4',
    author_literal='https://raw.githubusercontent.com/f4t4nt/degree-diameter-graphs/main/graphs/deg11/dia4/deg11-dia4-n3645.edges.txt',
    author_recipe='DoubleofW9+164spreadtwins gives3444regularbase;201absorbed-deletioninsertionsgive3645',
    current_old3444_induced_edges=sum(u<3444 and v<3444 for u,v in edges),
    author_source_D4_reused=True,source_BFS=0,coverage_algorithm_run=False,hash_computations=0,
    CPU_seconds=time.process_time()-start,pending=['Freezeaconcreteactualfree-setcoveragepredictionbeforenextalgorithm'])
save('SOURCE_PROFILE.json',result);save('RESULT.json',result);save('terminal.json',result)
print(json.dumps({k:v for k,v in result.items() if k not in ['naive81_partition','min_attaining_vertices']}))
print('MIN_VERTICES',result['min_attaining_vertices'])
print('81COUNTEREXAMPLE',counterexample)
