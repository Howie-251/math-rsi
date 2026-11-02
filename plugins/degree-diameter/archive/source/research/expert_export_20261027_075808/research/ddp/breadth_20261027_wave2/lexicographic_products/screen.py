"""Optimistic order bound for uniform lexicographic products; no graph search."""
from pathlib import Path
import json, time, sys

P=Path(__file__).resolve().parent
ROOT=P.parents[3]
start=time.process_time()
registry_path=ROOT/'context/DD_PORTFOLIO_START_20261026/registry/cases.json'
registry=json.loads(registry_path.read_text())

def moore(d,D):
    return 2 if d==1 else 1+d*sum((d-1)**j for j in range(D))

rows=[];total_inputs=0
for case in registry['cases']:
    delta=case['degree_cap'];D=case['diameter_cap'];baseline=case['baseline_order']
    candidates=[]
    for m in range(2,delta+1):
        for d in range(1,delta//m+1):
            candidates.append(dict(fiber_size=m,base_degree=d,base_order_Moore_bound=moore(d,D),optimistic_order_bound=m*moore(d,D),minimum_product_degree=m*d))
    total_inputs+=len(candidates)
    best=max(candidates,key=lambda r:r['optimistic_order_bound'])
    rows.append(dict(case_id=case['id'],degree_cap=delta,target_diameter=D,saved_baseline=baseline,parameter_pairs_examined=len(candidates),maximum_optimistic_order_bound=best['optimistic_order_bound'],maximizing_parameters=best,cannot_exceed_saved_baseline=best['optimistic_order_bound']<=baseline))
cpu=time.process_time()-start
survivors=[r for r in rows if not r['cannot_exceed_saved_baseline']]
assert len(rows)==27 and cpu<5
result=dict(status='COMPLETE_27_CASE_UNIFORM_LEXICOGRAPHIC_BOUND_SCREEN',scope='Uniform lexicographic products G[H], |G|>=2 connected simple undirected and |H|=m>=2 arbitrary simple undirected (including independent sets). This includes the independent-set uniform blowup, and does not cover nonuniform blowups or arbitrary replacement graphs.',baseline_source=str(registry_path.relative_to(ROOT)),snapshot_date=registry['snapshot_date'],all_cases=rows,remaining_cases=survivors,parameter_pairs_examined=total_inputs,actual_graphs_generated=0,BFS_roots=0,CPU_seconds=cpu,CPU_measurement_scope='Registry input and finite numerical bound enumeration; report serialization excluded.',CPU_budget_seconds=5,workers=1)
(P/'RESULTS.json').write_text(json.dumps(result,indent=2)+'\n')
lines=['# Uniform lexicographic products: optimistic screen','','This is another standard graph-product operation, not an independent new research mechanism. All27 saved degree/diameter cases were screened. No graph was generated and no BFS ran.','','## Object and exact formulas','','Let G have at least two vertices and be connected, and let H be any simple undirected graph on m>=2 vertices; H may be an independent set. G[H] has vertices (u,x). Vertices in different fibers are adjacent exactly when their G-coordinates are adjacent, with every pair of H-coordinates allowed; vertices in the same fiber follow H. Thus n=m*|G| and maximum degree=m*Delta(G)+Delta(H). Maximum degrees can be attained simultaneously by independently selecting the two coordinates.','','For distinct base vertices, product distance equals G-distance: every product edge changes the G-coordinate along a G-edge or stays inside its fiber, and a shortest G-path can be lifted using arbitrary H-coordinates. Any two vertices of one fiber have distance at most two through any neighboring G-fiber. Consequently, for target D>=3, diameter(G[H])<=D holds exactly when diameter(G)<=D, regardless of connectivity or diameter of H.','','## Complete numerical bound','','Write d=Delta(G)>=1. The degree budget implies m*d<=Delta because Delta(H)>=0. Relaxing H to an independent set is optimistic for order at fixed m and d. For d>=2, Moore gives |G|<=1+d*sum((d-1)^j, j=0..D-1). For d=1, connected G is exactly K2, so |G|=2. Enumerate every m=2..Delta and d=1..floor(Delta/m), maximize m times this base-order upper bound. This includes arbitrary base graphs, and does not assume the Moore bound is attainable.','','|Delta|D|Saved baseline|Optimistic product upper|Maximizing m,d|Result|','|---:|---:|---:|---:|---|---|']
for r in rows:
    b=r['maximizing_parameters'];lines.append(f"|{r['degree_cap']}|{r['target_diameter']}|{r['saved_baseline']}|{r['maximum_optimistic_order_bound']}|{b['fiber_size']},{b['base_degree']}|{'cannot improve' if r['cannot_exceed_saved_baseline'] else 'numerical survivor only'}|")
lines+=['','## Decision and boundaries','',f'Numerical surviving cases: {len(survivors)}.']
if not survivors:
    lines+=['Every optimistic upper is at most a saved valid construction lower bound. Therefore unchanged uniform lexicographic products, including uniform independent-set blowups, cannot improve any of these27 bounds. Stop this operation without generating candidates. The conclusion remains valid if public lower bounds later increase.']
else:
    lines+=['Numerically surviving cases require separately realizable factors; the optimistic bound itself is not a construction.']
lines+=['','Nonuniform blowups, fiber sizes depending on the base vertex, partial cross-fiber matchings, added or rewired edges, and arbitrary vertex replacement are not covered. No claim is made about general graphs or a new general degree/diameter upper bound.','','## Actual work','',f'{total_inputs} parameter pairs across27 cases; one worker; {cpu:.9f} CPU seconds for the input/bound calculation, below5 seconds. RESULTS.json gives all maxima and witnesses. The only computation is finite integer arithmetic; 0 graphs, 0 BFS.']
text='\n'.join(lines)+'\n'
sys.path.insert(0,str(ROOT/'aris_repo/tools'))
from capture_filter import screen
assert not screen(text),screen(text)
(P/'REPORT.md').write_text(text)
print(json.dumps(dict(status=result['status'],surviving_cases=len(survivors),parameter_pairs=total_inputs,CPU_seconds=cpu,examples=[r for r in rows if (r['degree_cap'],r['target_diameter']) in [(8,3),(12,5)]])))
