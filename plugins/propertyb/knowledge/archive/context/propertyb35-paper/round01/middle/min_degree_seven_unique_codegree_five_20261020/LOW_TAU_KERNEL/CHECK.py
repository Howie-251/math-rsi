"""Small positive-cost graph enumeration and saved unique-lambda5 key filter."""
from itertools import combinations
from pathlib import Path
import json
import time

HERE=Path(__file__).resolve().parent
ROUND=HERE.parents[2]
START=time.process_time()
pair=lambda x,y:tuple(sorted((x,y)))
available=[e for e in combinations(range(8),2) if e!=(0,1)]
receipts=[]
for residual in (2,3):
    records=[]
    for selected in combinations(available,residual):
        edges=set(selected)
        if not all(any(v in e for e in edges) for v in (0,1)):
            continue
        slots=[]
        for x,y in combinations(range(2,8),2):
            for A,B in [((0,x),(1,y)),((0,y),(1,x))]:
                cross=[pair(a,b) for a in A for b in B]
                positive=sum(e in edges for e in cross)
                if positive<2:
                    continue
                sidecaps=[3 if pair(*side) in edges else 2 for side in (A,B)]
                weight=min(sidecaps)
                assert weight<=2
                slots.append({'sides':[A,B],'positive_cross_edges':positive,
                              'matching_upper':weight})
        assert len(slots)<=(1 if residual==2 else 2)
        records.append({'positive_edges':selected,'bad_partitions':slots,
                        'total_matching_upper':sum(s['matching_upper'] for s in slots)})
    maximum=max(x['total_matching_upper'] for x in records)
    assert maximum==(2 if residual==2 else 4)
    receipts.append({'tau':residual+6,'complete_service_graphs':len(records),
                     'maximum_bad_outer_pairs':maximum,
                     'maximum_witness':next(x for x in records if x['total_matching_upper']==maximum),
                     'records':records})

source=json.loads((ROUND/'root/vertex_flag_capacity_20261020/LAMBDA5_RESULT.json').read_text())
jobs=[]
newly_strict=[]
for job in source['jobs']:
    rows=[]
    for k in job['cases']:
        caps=k['new_caps'][:]
        applicable=job['degrees'][-2:]==[11,11] and k['tau'] in (8,9)
        if applicable:
            caps[3]=min(caps[3],12*k['n'][3]+(2 if k['tau']==8 else 4))
        budget=k['vertex_P']
        value=6864*k['n'][1]
        allocation=[0]*5
        for i in range(4,-1,-1):
            allocation[i]=min(caps[i],budget)
            value+=(36,120,330,792,1716)[i]*allocation[i]
            budget-=allocation[i]
        assert value<=k['vertex_twice_L']
        if not applicable:
            assert value==k['vertex_twice_L']
        row={'n':k['n'],'tau':k['tau'],'low_tau_kernel_applied':applicable,
             'old_vertex_twice_L':k['vertex_twice_L'],'old_vertex_strict':k['vertex_strict'],
             'P':k['vertex_P'],'caps':caps,'allocation':allocation,
             'twice_L':value,'threshold_minus_twice_L':5445440-value,
             'strict':value<5445440}
        rows.append(row)
        if row['strict'] and not k['vertex_strict']:
            newly_strict.append({'spectrum_id':job['spectrum_id'],**row})
    jobs.append({'spectrum_id':job['spectrum_id'],'degrees':job['degrees'],
                 'old_remaining':sum(not k['vertex_strict'] for k in job['cases']),
                 'remaining_count':sum(not k['strict'] for k in rows),
                 'whole_saved_domain_strict':all(k['strict'] for k in rows),
                 'keys':rows})
out={'status':'PASS_WITH_DECLARED_IMPORTS','review_independence':'same-family',
     'acceptance_status':'provisional',
     'scope':'Actual unique lambda5 degree11/11, all other lambdas<=4, tau8/9; no whole-domain rescan.',
     'complete_graph_enumerations':receipts,
     'new_strict_key_count':len(newly_strict),'new_strict_keys':newly_strict,
     'remaining_keys':sum(j['remaining_count'] for j in jobs),
     'newly_whole_spectrum_ids':[j['spectrum_id'] for j in jobs if j['whole_saved_domain_strict'] and j['old_remaining']],
     'jobs':jobs,'cpu_seconds':time.process_time()-START}
assert out['new_strict_key_count']==13 and out['remaining_keys']==40
(HERE/'RESULT.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({k:v for k,v in out.items() if k not in ('complete_graph_enumerations','jobs','new_strict_keys')},indent=2))
