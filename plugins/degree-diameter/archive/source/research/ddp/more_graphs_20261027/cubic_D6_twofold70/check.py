"""OnefixedAFY70 ordinary2-cover: exactshort-routecapacity andlinearnecessity."""
from pathlib import Path
from collections import Counter
from datetime import datetime,timezone
import json,re,html,time,resource

OUT=Path(__file__).resolve().parent
start=time.process_time()
resource.setrlimit(resource.RLIMIT_CPU,(5,5))
load=lambda p:json.loads(p.read_text())
save=lambda name,d:(OUT/name).write_text(json.dumps(d,indent=2)+'\n')
assert load(OUT/'PREDICTION.json')['frozen_before_route_checks']
table=(OUT/'public_table.html').read_text()
clean=lambda s:re.sub(r'\s+','',html.unescape(re.sub('<[^>]+>','',s)))
row3=None
for row in re.findall(r'<tr\b[^>]*>(.*?)</tr>',table,re.I|re.S):
    cells=re.findall(r'<t[dh]\b[^>]*>(.*?)</t[dh]>',row,re.I|re.S)
    if cells and clean(cells[0])=='3':row3=cells;break
assert row3 and len(row3)>=6
targetcell=row3[5];value=int(clean(targetcell));bold=bool(re.search(r'<(?:b|strong)\b',targetcell,re.I))
baseline=dict(checked_UTC=datetime.now(timezone.utc).isoformat(),
    table_URL='https://web.mat.upc.edu/francesc.comellas/delta-d/table_degree_diameter.html',
    target=[3,6],publicL=value,cell_html=targetcell,cell_is_bold=bold,
    page_criterion='Entriesinboldfaceareoptimal',hypothetical_n=140)
save('BASELINE.json',baseline)
assert value==132 and not bold,'Freshbaselinegatechanged;noauthorizedscan'
edges=set();vertices=set()
for line in (OUT/'source70.adjlist.txt').read_text().splitlines():
    if not line.strip() or line.startswith('#'):continue
    words=list(map(int,line.split()));u=words[0];vertices.add(u)
    for v in words[1:]:vertices.add(v);edges.add(tuple(sorted((u,v))))
edges=sorted(edges);assert vertices==set(range(70)) and len(edges)==105
adj=[[] for _ in range(70)]
for i,(u,v) in enumerate(edges):adj[u].append((v,i));adj[v].append((u,i))
assert all(len(a)==3 for a in adj) and all(u!=v for u,v in edges)
parent=[-1]*70;depth=[-1]*70;depth[0]=0;todo=[0];tree=set()
while todo:
    u=todo.pop()
    for v,e in adj[u]:
        if depth[v]<0:parent[v]=u;depth[v]=depth[u]+1;tree.add(e);todo.append(v)
assert all(d>=0 for d in depth) and len(tree)==69
cotree=[e for e in range(105) if e not in tree];assert len(cotree)==36
var={e:i for i,e in enumerate(cotree)}
edge_forms=[0 if e in tree else 1<<var[e] for e in range(105)]
nonbipartite=any(depth[u]%2==depth[v]%2 for u,v in edges)
assert nonbipartite
with (OUT/'source70.edges').open('w') as f:
    f.write('70 105\n')
    for u,v in edges:f.write(f'{u} {v}\n')
save('SOURCE.json',dict(n=70,m=105,degree=3,connected=True,nonbipartite=True,
    known_D=5,known_D_source='OfficialD5 description;noordinaryBFS',
    source_URL='https://web.mat.upc.edu/francesc.comellas/delta-d/desc_g/adjacencies/adjD5/AlFiYe70_Z_adjlist.txt',
    description_URL='https://web.mat.upc.edu/francesc.comellas/delta-d/desc_g/desc_g5.html',
    authors=['I.Alegre','M.A.Fiol','J.L.A.Yebra'],fixed_choice='officialD5link6 AFY70integerlabels',
    other70sources_investigated=False,tree_edge_ids=sorted(tree),cotree_edge_ids=cotree,
    edges_by_id=edges,free_voltage_variables=36,
    gauge='Root0spanningtreevoltageszero;all2-coversrepresenteduptovertexsheetswitches'))
forms=[[{} for _ in range(70)] for _ in range(70)]
raw=[[[] for _ in range(70)] for _ in range(70)]
bylength=[0]*7
for root in range(70):
    def visit(u,last,mask,path):
        length=len(path)-1;bylength[length]+=1
        forms[root][u].setdefault(mask,path);raw[root][u].append((mask,path))
        if length==6:return
        for v,e in adj[u]:
            if v!=last:visit(v,u,mask^edge_forms[e],path+(v,))
    visit(root,-1,0,(root,))
assert bylength==[70,210,420,840,1680,3360,6720]
hist=Counter(len(forms[u][v]) for u in range(70) for v in range(70))
rawhist=Counter(len(raw[u][v]) for u in range(70) for v in range(70))
bad=[(u,v) for u in range(70) for v in range(70) if len(forms[u][v])<2]
save('route_forms.json',dict(source_n=70,ordered_slots=4900,tree_gauge_variables=36,
    raw_walk_count_by_length=bylength,distinct_form_count_histogram=dict(sorted(hist.items())),
    raw_walk_count_histogram=dict(sorted(rawhist.items())),
    forms_by_ordered_slot=[[sorted(forms[u][v]) for v in range(70)] for u in range(70)]))
result=dict(source_n=70,source_m=105,degree=3,target_D=6,savedL=132,hypothetical_n=140,
    actual_n=None,actual_D=None,voltage_assignments_tested=0,graph_generated=False,
    base_roots_enumerated=70,ordered_slots=4900,raw_walk_count_by_length=bylength,
    distinct_form_count_histogram=dict(sorted(hist.items())),capacity_bad_ordered_slots=len(bad),
    tree_gauge_variables=36,ordinary_source_BFS=0,hash_computations=0,pending=[])
if bad:
    u,v=bad[0]
    witness=dict(u=u,v=v,distinct_form_count=len(forms[u][v]),raw_reduced_walk_count=len(raw[u][v]),
        all_reduced_walks=[dict(vertices=list(path),form=mask) for mask,path in raw[u][v]],
        diagonal_nonzero_closed_forms=[m for m in forms[u][u] if m],
        implication='ForanyF2voltageassignmentthisslotreachesatmostonesheetwithin6;backtrackscancel',
        tree_gauge_free_edge_ids=cotree)
    save('capacity_witness.json',witness)
    result.update(status='ALL_TWO_COVERS_FIXED_SOURCE_EXCLUDED_BY_ROUTE_CAPACITY',
        prediction_supported=False,first_bad_slot=[u,v],linear_stage_run=False,
        capacity_bad_diagonal_slots=sum(u==v for u,v in bad),
        capacity_bad_distinct_ordered_slots=sum(u!=v for u,v in bad),
        witness_file='capacity_witness.json')
else:
    equations={}
    for u in range(70):
        for v in range(70):
            values=sorted(forms[u][v])
            if len(values)==2:
                mask=values[0]^values[1]
                equations.setdefault(mask,dict(mask=mask,rhs=1,slot=[u,v],forms=values,
                    paths=[list(forms[u][v][z]) for z in values]))
    eq=list(equations.values());basis={};contradiction=None
    for i,row in enumerate(eq):
        mask=row['mask'];rhs=1;combo=1<<i
        while mask:
            pivot=mask.bit_length()-1
            if pivot not in basis:basis[pivot]=(mask,rhs,combo);break
            a,b,c=basis[pivot];mask^=a;rhs^=b;combo^=c
        if not mask and rhs:
            contradiction=[j for j in range(len(eq)) if combo>>j&1];break
    save('LINEAR.json',dict(equations=eq,equation_count=len(eq),rank=len(basis),
        free_variables=36-len(basis),consistent=contradiction is None,
        contradiction_equation_indices=contradiction))
    result.update(status='NECESSARY_LINEAR_SYSTEM_CONSISTENT_NO_SEARCH' if contradiction is None else 'ALL_TWO_COVERS_FIXED_SOURCE_EXCLUDED_BY_LINEAR_CONTRADICTION',
        prediction_supported=True,linear_stage_run=True,linear_equations=len(eq),linear_rank=len(basis),
        remaining_free_variables=36-len(basis),linear_consistent=contradiction is None)
    if contradiction is None:result['pending']=['Rootdecisiononstrongercoverconditions;noassignmentsearchauthorized']
result['CPU_seconds']=time.process_time()-start
save('RESULT.json',result);save('terminal.json',result)
print(json.dumps(result))
