from pathlib import Path
import json,resource,sys,time

P=Path(__file__).resolve().parent
ROOT=P.parents[3]
start_cpu=time.process_time();start_wall=time.monotonic()
source=ROOT/'context/DD_PORTFOLIO_START_20261026/registry/cases.json'
registry=json.loads(source.read_text())

def moore(d,r):
    assert d>=1 and r>=1
    if d==1:
        assert r==1
        return 2
    return 1+d*sum((d-1)**j for j in range(r))

def factor_params(degree_cap,diameter_cap):
    return [(d,r,moore(d,r)) for d in range(1,degree_cap+1) for r in range(1,diameter_cap+1) if d!=1 or r==1]

def solve(delta,diam,method):
    # State = (exact factor count, exact accumulated degree resource,
    #          exact accumulated diameter). Each state keeps the largest
    # product of factor Moore bounds and one maximizing parameter list.
    dp={(0,0 if method=='cartesian' else 1,0):(1,[])}
    factors=factor_params(delta,diam)
    transitions=0
    max_count=diam if method=='cartesian' else (delta+1).bit_length()-1
    for k in range(max_count):
        layer=[(key,value) for key,value in dp.items() if key[0]==k]
        for (_,degree_resource,diam_resource),(value,witness) in layer:
            for d,r,m in factors:
                degree_next=degree_resource+d if method=='cartesian' else degree_resource*(d+1)
                diam_next=diam_resource+r if method=='cartesian' else max(diam_resource,r)
                cap=delta if method=='cartesian' else delta+1
                if degree_next>cap or diam_next>diam:continue
                transitions+=1
                key=(k+1,degree_next,diam_next)
                offered=(value*m,witness+[dict(degree=d,diameter=r,Moore_bound=m)])
                if key not in dp or offered[0]>dp[key][0]:dp[key]=offered
    best=max(((v,w,key) for key,(v,w) in dp.items() if key[0]>=2),key=lambda x:x[0])
    value,witness,key=best
    return dict(optimistic_order_upper_bound=value,maximizing_factor_parameters=witness,factor_count=key[0],resulting_degree=key[1] if method=='cartesian' else key[1]-1,resulting_diameter=key[2],DP_states=len(dp),legal_DP_transitions=transitions)

rows=[]
for case in registry['cases']:
    delta=case['degree_cap'];diam=case['diameter_cap'];baseline=case['baseline_order']
    row=dict(case_id=case['id'],degree_cap=delta,diameter_cap=diam,saved_baseline=baseline)
    for method in ['cartesian','strong']:
        entry=solve(delta,diam,method)
        entry.update(cannot_exceed_saved_baseline=entry['optimistic_order_upper_bound']<=baseline,optimistic_excess=entry['optimistic_order_upper_bound']-baseline)
        row[method]=entry
    rows.append(row)

survivors=[dict(case_id=r['case_id'],method=m,entry=r[m]) for r in rows for m in ['cartesian','strong'] if not r[m]['cannot_exceed_saved_baseline']]
assert len(rows)==27
cpu=time.process_time()-start_cpu
result=dict(status='COMPLETE_27_CASE_OPTIMISTIC_PRODUCT_BOUND_SCREEN',scope='All Cartesian products, and separately all strong products, with at least two nontrivial finite connected simple undirected factors, degree cap4..12 and diameter cap3,4,5. Arbitrary factors are bounded by their Moore bounds; degree-one connected factors are K2 only.',baseline_source=str(source.relative_to(ROOT)),snapshot_date=registry['snapshot_date'],all_cases=rows,remaining_cases=survivors,actual_graphs_generated=0,graph_BFS_runs=0,CPU_seconds=cpu,CPU_measurement_scope='DP and baseline input; report serialization not included',wall_seconds=time.monotonic()-start_wall,worker_count=1,CPU_budget=10)
(P/'RESULTS.json').write_text(json.dumps(result,indent=2)+'\n')
lines=['# Cartesian and strong graph products: complete optimistic screen','','A small integer dynamic program checked all27 degree/diameter cells against the saved2026-10-26 baseline. Each factor is allowed the ordinary Moore upper bound, even when that bound is unattainable. Thus rejection is valid without constructing factors; a surviving numerical bound would not prove existence. This task generated no graph and ran no BFS.','','## Scope and formulas','','Every factor is nontrivial, finite, connected, simple and undirected. With actual maximum degree d and diameter r, its order is at most M(d,r)=1+d*sum((d-1)^j,j=0..r-1). A connected graph of degree one is exactly K2 and has diameter one, so this exceptional factor contributes(d,r,M)=(1,1,2). Factors of degree at least two have r>=1.','','For a Cartesian product, vertex counts multiply, maximum degrees add, and diameters add. A product path must change coordinates separately; shortest paths in each coordinate concatenate, proving the exact sum distance formula. Therefore enumerate all factor parameters with sum d_i<=Delta and sum r_i<=D, and maximize product M(d_i,r_i). At least two factors are required.','','For a strong product, vertex counts multiply and maxdegree+1=product(d_i+1); its diameter is max r_i. At a product vertex, its closed neighborhood is the Cartesian product of the factor closed neighborhoods. Maximum-degree factor vertices can be chosen independently, proving the degree formula even for nonregular factors. Each coordinate advances at most one edge per step, and shortest coordinate paths can be followed simultaneously, proving the maximum distance formula. Therefore enumerate product(d_i+1)<=Delta+1 and max r_i<=D, maximizing the same factor-bound product.','','The DP keeps the maximum bound at each exact factor count and exact degree/diameter resource state, appending every allowed(d,r) factor. Cartesian factor count is at most D because every r>=1. Strong factor count is at most floor(log2(Delta+1)) because every d_i+1>=2. These bounds make the enumeration finite and complete for the stated formulas. Keeping only the largest bound in a state is safe because future transitions depend only on those resources and multiply by positive factor bounds.','','## All27 results','','|Delta|D|Saved baseline|Cartesian optimistic upper|Strong optimistic upper|Result|','|---:|---:|---:|---:|---:|---|']
for r in rows:
    lines.append('|%s|%s|%s|%s|%s|%s|'%(r['degree_cap'],r['diameter_cap'],r['saved_baseline'],r['cartesian']['optimistic_order_upper_bound'],r['strong']['optimistic_order_upper_bound'],'both excluded' if all(r[m]['cannot_exceed_saved_baseline'] for m in ['cartesian','strong']) else 'numerical survivor; not existence'))
lines+=['','## Consequence and boundaries','',f'Numerical surviving cases: {len(survivors)}.']
if not survivors:
    lines+=['Every optimistic upper bound is already no larger than its saved public construction baseline. Consequently neither plain Cartesian nor plain strong products of two or more nontrivial connected factors can improve any of these27 saved bounds. No factor generation or product graph search is warranted for this unchanged method. Since a lower bound remains valid if a public table later increases, the exclusion against the saved constructions remains valid.']
else:
    lines+=['A numerical survivor requires separately supplied realizable factor graphs; the DP maximizing Moore bounds are not constructions. See remaining_cases in RESULTS.json.']
lines+=['','This does not exclude arbitrary graphs, modified products with deleted/added/rewired edges, tensor/direct or lexicographic products, or lifts with coordinate-dependent connections. Arbitrary factors inside the two specified outer product operations are covered, whether or not those factors themselves have further structure. No claim of a new general degree/diameter bound or original theorem is made.','','## Cost and files','',f'One worker; measured DP/input CPU {cpu:.9f} seconds, below10 seconds; report serialization is outside that core measurement. RESULTS.json records all27 cells, complete maximizing factor parameter lists and DP counts. screen.py is the reproduction command source. No actual graph was generated.']
text='\n'.join(lines)+'\n'
sys.path.insert(0,str(ROOT/'aris_repo/tools'))
from capture_filter import screen
assert not screen(text),screen(text)
(P/'REPORT.md').write_text(text)
print(json.dumps(dict(CPU_seconds=cpu,survivor_count=len(survivors),rows=[dict(d=r['degree_cap'],D=r['diameter_cap'],L=r['saved_baseline'],cart=r['cartesian']['optimistic_order_upper_bound'],strong=r['strong']['optimistic_order_upper_bound']) for r in rows])))
