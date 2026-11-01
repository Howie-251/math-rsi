"""Bounded transfer audit: integer inventories and THREE already saved explicit P sources.
No new P-domain, original H, exterior-layout or negative-layout generation.
"""
from pathlib import Path
from itertools import combinations
from collections import Counter
import json,time
HERE=Path(__file__).resolve().parent
BASE=HERE.parent/'p7_one_two_new_gate_transfer_20261020'
t0=time.process_time()
P=127
mask=lambda a:sum(1<<i for i in a)
def menu(name,internal,higher,u):
    traces=internal+higher+[1<<i for i in range(7) for _ in range(u[i])]
    assert len(traces)==35
    assert all(sum(bool(T&(1<<i)) for T in traces)==8 for i in range(7))
    rows=[]
    for a in (2,3):
        for Qpoints in combinations(range(7),a):
            Q=mask(Qpoints); roles=[]
            for j,T in enumerate(traces):
                if T&Q and T&(P^Q): role='proper'
                elif T&Q: role='P'+str(5-T.bit_count())
                else: role='N'+str(5-T.bit_count())
                roles.append(role)
            count=Counter(roles)
            accepted=(count['P4']==9 and count['N2']<=1 and count['N4']<=17
                      and all(k in ('proper','P4','N2','N4') for k in count))
            # Every proper edge has at least one blue P incidence.
            assert 8*a>=count['P4']+count['proper']
            assert not(a==2 and accepted)
            rows.append(dict(blue=Q,blue_points=list(Qpoints),risk_counts=dict(sorted(count.items())),
                             nine_N2_accept=accepted,roles_by_original_index=roles))
    return dict(name=name,internal=internal,higher=higher,u=u,
                traces=traces,menus=rows,new_gate_acceptances=sum(r['nine_N2_accept'] for r in rows),
                source_is_H=False)

saved=[]
f=json.loads((BASE/'FANO_PAIR_OBSTRUCTION.json').read_text())
saved.append(menu('saved Fano-five P3 obstruction (already closed I2 stock)',
    [P^mask(x) for x in f['missing']],[mask(x) for x in f['higher']],f['u']))
for fn in ('FAILURE.json','FALLBACK_FAILURE.json'):
    f=json.loads((BASE/'zero_pair_n1_28'/fn).read_text())
    saved.append(menu('saved I2 n1=28 '+fn,f['internal_masks'],f['quad_masks']+f['triple_masks'],f['u']))

closed={1:{(17,0,0),(0,4,3),(1,2,4),(2,0,5),(0,1,5)},
        2:{(13,0,0),(0,5,1),(1,3,2),(2,1,3),(1,0,4)}}
inv=[]
for I in (1,2):
  for n2 in range(22):
   for n3 in range(11):
    for n4 in range(8):
     if n2+2*n3+3*n4!=21-4*I:continue
     n1=14+3*I+n3+2*n4
     inv.append(dict(I=I,inventory=[n2,n3,n4],n1=n1,
       fully_closed_by_imported_stock_theorem=(n2,n3,n4) in closed[I],
       possible_new_N2_caller_by_scalar_budget=n3>=1 and 21<=n1<=26,
       two_blue_N2_caller_possible=False))
assert len(inv)==54
out=dict(scope=__doc__,gate_status='candidate under root audit; no promotion in this diagnosis',
         complete_integer_inventory_count=54,closed_imported_stock_count=10,
         remaining_by_I={str(I):[r['inventory'] for r in inv if r['I']==I and not r['fully_closed_by_imported_stock_theorem']] for I in (1,2)},
         possible_new_N2_remaining_by_I={str(I):[r['inventory'] for r in inv if r['I']==I and not r['fully_closed_by_imported_stock_theorem'] and r['possible_new_N2_caller_by_scalar_budget']] for I in (1,2)},
         inventories=inv,explicit_saved_sources=saved,
         original_trace_classifications=3*56*35,new_gate_explicit_acceptances=sum(s['new_gate_acceptances'] for s in saved),
         cpu_seconds=time.process_time()-t0)
(HERE/'TRANSFER_CHECK.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({k:v for k,v in out.items() if k not in ('inventories','explicit_saved_sources')},indent=2))
