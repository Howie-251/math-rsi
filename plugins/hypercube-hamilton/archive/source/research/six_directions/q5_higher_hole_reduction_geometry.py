"""Complete tiny geometry census for the Q5 A8/A10 bottlenecks.

This proves no new matching-extension assertion; output is producer evidence.
"""
import itertools as it,json,collections,hashlib
from pathlib import Path
R=Path(__file__).resolve().parent
ev=[x for x in range(32) if not x.bit_count()%2]
od=[x for x in range(32) if x.bit_count()%2]
maps=[[sum(((x>>i)&1)<<p[i] for i in range(5)) for x in range(32)] for p in it.permutations(range(5))]
neighbors={x:sum(1<<(x^(1<<d)) for d in range(5)) for x in range(32)}
hist=collections.Counter();mins=[]
for s in it.combinations(ev,5):
    mask=0
    for x in s:mask|=neighbors[x]
    hist[mask.bit_count()]+=1
    if mask.bit_count()==11:mins.append(s)
assert sum(hist.values())==4368 and min(hist)==11
levels=[]
for t in range(4,9):
    total=0;uncovered=[];delta_hist=collections.Counter()
    for w in it.combinations(od,t-1):
        allowed=[x for x in ev if x and all((x^y).bit_count()!=1 for y in w)]
        for z in it.combinations(allowed,t):
            total+=1
            ds=tuple(1+sum(not(x>>d&1) for x in z)-sum(not(y>>d&1) for y in w) for d in range(5))
            delta_hist[tuple(sorted(ds))]+=1
            if not any(d in (1,2,3) for d in ds):uncovered.append((z,w))
    orbit=collections.Counter()
    for z,w in uncovered:
        canon=min((tuple(sorted(p[x] for x in z)),tuple(sorted(p[y] for y in w))) for p in maps)
        orbit[canon]+=1
    levels.append({'holes':2*t,'independent_except_forbidden_geometries':total,
       'without_delta123':len(uncovered),'delta_histogram':[[list(k),v] for k,v in sorted(delta_hist.items())],
       'residual_orbits':[{'other_majority':z,'minority':w,'size':n} for (z,w),n in sorted(orbit.items())]})
out={'scope':'Exact Q5 geometry only; no A8/A10 extension assertion',
     'five_vertex_neighbor_histogram':dict(sorted(hist.items())),
     'five_vertex_sets_with_minimum_neighborhood':len(mins),'levels':levels,
     'producer_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
     'full_a8_proved':False,'full_a10_proved':False,'full_p6_proved':False}
(R/'q5_higher_hole_reduction_geometry.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({'neighbor_histogram':out['five_vertex_neighbor_histogram'],
                 'levels':[{k:v for k,v in l.items() if k!='delta_histogram'} for l in levels]},indent=2))
