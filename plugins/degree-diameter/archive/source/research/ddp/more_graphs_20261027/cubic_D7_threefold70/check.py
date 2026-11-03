"""FixedAFY70 C3cover D7: route capacity and tight linear necessities only."""
from pathlib import Path
from collections import Counter
from datetime import datetime,timezone
import json,re,html,time,resource

OUT=Path(__file__).resolve().parent
OLD=OUT.parent/'cubic_D6_twofold70'
start=time.process_time()
resource.setrlimit(resource.RLIMIT_CPU,(5,5))
load=lambda p:json.loads(p.read_text())
save=lambda name,d:(OUT/name).write_text(json.dumps(d,indent=2)+'\n')
assert load(OUT/'PREDICTION.json')['frozen_before_route_checks']
table=(OLD/'public_table.html').read_text()
clean=lambda s:re.sub(r'\s+','',html.unescape(re.sub('<[^>]+>','',s)))
row3=None
for row in re.findall(r'<tr\b[^>]*>(.*?)</tr>',table,re.I|re.S):
    cells=re.findall(r'<t[dh]\b[^>]*>(.*?)</t[dh]>',row,re.I|re.S)
    if cells and clean(cells[0])=='3':row3=cells;break
assert row3 and len(row3)>6
cell=row3[6];value=int(clean(cell));bold=bool(re.search(r'<(?:b|strong)\b',cell,re.I))
save('BASELINE.json',dict(target=[3,7],publicL=value,cell_is_bold=bold,cell_html=cell,
    cached_fresh_table='../cubic_D6_twofold70/public_table.html',
    prior_table_check_UTC=load(OLD/'BASELINE.json')['checked_UTC'],
    extraction_UTC=datetime.now(timezone.utc).isoformat(),
    official_URL='https://web.mat.upc.edu/francesc.comellas/delta-d/table_degree_diameter.html'))
assert value==200 and not bold
source=load(OLD/'SOURCE.json');edges=source['edges_by_id'];cotree=source['cotree_edge_ids']
assert len(edges)==105 and len(cotree)==36
variables={e:i for i,e in enumerate(cotree)}
adj=[[] for _ in range(70)]
for e,(u,v) in enumerate(edges):
    assert u<v
    adj[u].append((v,variables.get(e),1))
    adj[v].append((u,variables.get(e),2))
assert all(len(a)==3 for a in adj)

def decode(mask):return [(mask>>(2*j))&3 for j in range(36)]
def step(mask,index,sign):
    if index is None:return mask
    shift=2*index;old=(mask>>shift)&3;new=(old+sign)%3
    return mask^((old^new)<<shift)
def normalize(row):
    p=next((i for i,v in enumerate(row) if v),None)
    return tuple(row) if p is None or row[p]==1 else tuple(2*v%3 for v in row)

forms=[[{} for _ in range(70)] for _ in range(70)]
rawcounts=[[0]*70 for _ in range(70)]
bylength=[0]*8
for root in range(70):
    def visit(u,last,mask,path):
        length=len(path)-1;bylength[length]+=1;rawcounts[root][u]+=1
        forms[root][u].setdefault(mask,path)
        if length==7:return
        for v,index,sign in adj[u]:
            if v!=last:visit(v,u,step(mask,index,sign),path+(v,))
    visit(root,-1,0,(root,))
assert bylength==[70,210,420,840,1680,3360,6720,13440]
hist=Counter(len(forms[u][v]) for u in range(70) for v in range(70))
rawhist=Counter(rawcounts[u][v] for u in range(70) for v in range(70))
bad=[(u,v) for u in range(70) for v in range(70) if len(forms[u][v])<3]
rawbad=[(u,v) for u in range(70) for v in range(70) if rawcounts[u][v]<3]
save('route_forms.json',dict(source_n=70,D=7,field=3,variables=36,
    coefficient_encoding='2bitspercoordinate;digits0/1/2;additioncoordinatewiseF3notxor',
    cotree_edge_ids=cotree,raw_walk_count_by_length=bylength,
    distinct_form_count_histogram=dict(sorted(hist.items())),raw_route_count_histogram=dict(sorted(rawhist.items())),
    raw_counts_by_ordered_slot=rawcounts,
    forms_by_ordered_slot=[[sorted(forms[u][v]) for v in range(70)] for u in range(70)]))
result=dict(source_n=70,source_m=105,source_file='../cubic_D6_twofold70/source70.edges',
    Delta=3,target_D=7,savedL=200,hypothetical_n=210,actual_n=None,actual_D=None,
    field=3,tree_gauge_variables=36,base_roots_enumerated=70,ordered_slots=4900,
    raw_walk_count_by_length=bylength,distinct_form_count_histogram=dict(sorted(hist.items())),
    raw_route_count_histogram=dict(sorted(rawhist.items())),
    capacity_bad_C3_form_slots=len(bad),raw_route_count_below3_slots=len(rawbad),
    capacity_bad_diagonal_slots=sum(u==v for u,v in bad),
    capacity_bad_distinct_ordered_slots=sum(u!=v for u,v in bad),
    raw_diagonal_route_count_histogram=dict(Counter(rawcounts[u][u] for u in range(70))),
    voltage_assignments_tested=0,graph_generated=False,source_BFS=0,hash_computations=0,pending=[])
if bad:
    u,v=bad[0]
    witness=dict(slot=[u,v],distinct_forms=len(forms[u][v]),raw_reduced_route_count=rawcounts[u][v],
        forms=[dict(encoded=z,coefficients=decode(z),path=list(forms[u][v][z])) for z in sorted(forms[u][v])],
        cyclic_C3_excluded=True,arbitrary_threecover_excluded=rawcounts[u][v]<3)
    if rawbad:witness['first_raw_count_obstruction']=dict(slot=list(rawbad[0]),raw_routes=rawcounts[rawbad[0][0]][rawbad[0][1]])
    save('capacity_witness.json',witness)
    result.update(status='ALL_C3_COVERS_FIXED_SOURCE_EXCLUDED_BY_ROUTE_CAPACITY',
        capacity_prediction_supported=False,linear_stage_run=False,first_bad_slot=[u,v],
        arbitrary_threecover_also_excluded=bool(rawbad))
else:
    equations={};inequalities={};tight_slots=0
    for u in range(70):
        for v in range(70):
            zs=sorted(forms[u][v])
            if len(zs)!=3:continue
            tight_slots+=1;a,b,c=map(decode,zs)
            eq=normalize([(a[j]+b[j]+c[j])%3 for j in range(36)])
            ne=normalize([(a[j]-b[j])%3 for j in range(36)])
            context=dict(slot=[u,v],forms=zs,paths=[list(forms[u][v][z]) for z in zs])
            if any(eq):equations.setdefault(eq,context)
            inequalities.setdefault(ne,context)
    eqs=list(equations);basis={};combinations={}
    def addcombo(a,b,mult):
        a=a.copy()
        for j,c in b.items():
            a[j]=(a.get(j,0)+mult*c)%3
            if not a[j]:del a[j]
        return a
    for i,e in enumerate(eqs):
        row=list(e);combo={i:1}
        for p in sorted(basis):
            if row[p]:
                factor=row[p];row=[(x-factor*y)%3 for x,y in zip(row,basis[p])]
                combo=addcombo(combo,combinations[p],-factor)
        pivot=next((j for j,x in enumerate(row) if x),None)
        if pivot is not None:
            scale=1 if row[pivot]==1 else 2
            row=[scale*x%3 for x in row];combo={j:scale*x%3 for j,x in combo.items()}
            basis[pivot]=row;combinations[pivot]=combo
    obstruction=None;nonzero=0
    for row,context in inequalities.items():
        residual=list(row);representation={}
        for p in sorted(basis):
            if residual[p]:
                factor=residual[p];residual=[(x-factor*y)%3 for x,y in zip(residual,basis[p])]
                representation=addcombo(representation,combinations[p],factor)
        if not any(residual):
            obstruction=dict(required_nonzero_row=list(row),context=context,
                equality_row_combination=[dict(equation_index=j,coefficient=c) for j,c in sorted(representation.items())])
            break
        nonzero+=1
    save('LINEAR.json',dict(field=3,variables=36,tight_ordered_slots=tight_slots,
        homogeneous_equations=[dict(row=list(e),context=equations[e]) for e in eqs],
        equation_count=len(eqs),rank=len(basis),nullity=36-len(basis),
        unique_nonzero_requirements=len(inequalities),
        inequalities=[dict(row=list(e),context=c) for e,c in inequalities.items()],
        required_functionals_nonzero_on_kernel_before_obstruction=nonzero,
        obstruction=obstruction,
        all_inequalities_individually_nonzero_on_kernel=obstruction is None))
    result.update(status='ALL_C3_COVERS_FIXED_SOURCE_EXCLUDED_BY_TIGHT_LINEAR_KERNEL' if obstruction else 'TIGHT_NECESSITIES_NOT_EXCLUDED_NO_ASSIGNMENT_SEARCH',
        capacity_prediction_supported=True,linear_stage_run=True,tight_ordered_slots=tight_slots,
        homogeneous_equation_count=len(eqs),equality_rank=len(basis),equality_nullity=36-len(basis),
        unique_nonzero_requirements=len(inequalities),kernel_obstruction=obstruction is not None,
        cyclic_C3_scope_excluded=obstruction is not None,arbitrary_threecover_also_excluded=False)
    if not obstruction:result['pending']=['Rootdecision;necessaryconstraintsalonearenotacompletecoverwitness']
result['CPU_seconds']=time.process_time()-start
save('RESULT.json',result);save('terminal.json',result)
print(json.dumps(result))
