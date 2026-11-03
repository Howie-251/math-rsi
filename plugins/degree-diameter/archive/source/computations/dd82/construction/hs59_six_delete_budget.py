"""Tiny exact budgets used by the analytic six-deletion obstruction; no graph search."""
from pathlib import Path
import json,math,time

def partitions(n,minimum=1):
    if n==0:
        yield []
    for first in range(minimum,n+1):
        for tail in partitions(n-first,first):
            yield [first]+tail

start=time.process_time()
parts=[]
for sizes in partitions(9):
    if len(sizes)<4:continue
    cross=36-sum(math.comb(s,2) for s in sizes)
    if cross<=27:
        parts.append(dict(component_sizes=sizes,cross_component_pairs=cross,isolated_vertices=sizes.count(1),required_deleted_wedges=cross-12))
f=[]
for r in range(7):
    values={a:a*(1+r-a) for a in range(min(3,1+r)+1)}
    maximum=max(values.values())
    assert 5*maximum<=5*r+2*math.comb(r,2)
    f.append(dict(deleted_degree=r,maximum_cross_slots=maximum,maximizing_isolate_counts=[a for a,v in values.items() if v==maximum],five_times_maximum=5*maximum,bound=5*r+2*math.comb(r,2)))
result=dict(status='FINITE_ARITHMETIC_CHECK',component_partitions=parts,three_isolate_cross_slot_table=f,cpu_seconds=time.process_time()-start,scope='Partitions and seven small integer maxima only; analytic graph and port arguments are in HS59_SIX_DELETE_DESIGN.md.',solver_run=False,graph_search_run=False)
assert [x['component_sizes'] for x in parts]==[[1,1,1,1,5],[1,1,1,6],[1,1,2,5],[1,1,3,4]]
p=Path(__file__).with_suffix('.json');p.write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps({'component_partitions':parts,'max_cross_slots':[x['maximum_cross_slots'] for x in f],'cpu_seconds':result['cpu_seconds']}))
