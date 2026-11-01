"""Bounded necessary P-domain: seven high points, two internal edges, four noninternal P4 traces and one P2 trace. No exterior layouts."""
from itertools import combinations,combinations_with_replacement
from collections import Counter
from pathlib import Path
import json,time
HERE=Path(__file__).resolve().parent
P=set(range(7));PAIRS=list(combinations(P,2));QUADS=list(combinations(P,4));START=time.process_time()
rows=[];stop=False
witnesses=[]
GATES=['OLD_SEVEN_4T35B','OLD_EIGHT_L17_3T20B','NEW_NINE']
for shape,F in enumerate([((0,1),(1,2)),((0,1),(2,3))]):
    internal=[P-set(f) for f in F]
    ci=[sum(v in t for t in internal) for v in P]
    tested=0;necessary=0;passed=Counter();first_bad=None;first_new=None
    for Ts in combinations_with_replacement(QUADS,4):
        h=[sum(v in T for T in Ts) for v in P]
        if any(3*h[v]>15-4*ci[v] for v in P):continue
        for edge in PAIRS:
            tested+=1;s=[int(v in edge) for v in P]
            if any(s[v]+3*h[v]>15-4*ci[v] for v in P):continue
            traces0=internal+[set(t) for t in Ts]+[set(edge)]
            if any(not any(set(pair)<=t for t in traces0) for pair in PAIRS):continue
            u=[8-ci[v]-h[v]-s[v] for v in P]
            if min(u)<0:continue
            assert sum(u)==28
            necessary+=1;accept=None
            for bluepair in PAIRS:
                B=set(bluepair)
                if any(not t&B or t<=B for t in internal):continue
                if any(not set(t)&B for t in Ts):continue
                if set(edge)<=B:continue
                m=sum(u[v] for v in B);t=int(not set(edge)&B);b=28-m
                gate=None
                if m<=7:gate='OLD_SEVEN_4T35B'
                elif m==8 and b<=20:gate='OLD_EIGHT_L17_3T20B'
                elif m==9 and t+b<=20:gate='NEW_NINE'
                if gate:accept=(gate,bluepair,m,t,b);break
            if accept:
                passed[accept[0]]+=1
                gate,blue,m,t,b=accept
                witnesses.append([shape,[sum(1<<v for v in T) for T in Ts],sum(1<<v for v in edge),u,sum(1<<v for v in blue),GATES.index(gate),[m,t,b]])
                if accept[0]=='NEW_NINE' and first_new is None:first_new=dict(higher=Ts,J=edge,private=u,witness=accept)
            elif first_bad is None:first_bad=dict(higher=Ts,J=edge,private=u)
        if time.process_time()-START>50:stop=True;break
    rows.append(dict(missing=F,passed_tested_high_families_to_J=tested,necessary=necessary,passed=dict(passed),nongated=necessary-sum(passed.values()),first_bad=first_bad,first_new=first_new,complete=not stop))
    if stop:break
result=dict(scope=__doc__,rows=rows,cpu_seconds=time.process_time()-START,complete=not stop)
assert not stop and sum(r['necessary'] for r in rows)==len(witnesses)==77840
assert all(r['nongated']==0 for r in rows)
result['witness_schema']=['missing_shape_index','four_quad_trace_masks_with_multiplicity','unique_pair_trace_mask','seven_private_trace_counts','own_blue_pair_mask','gate_index','P4_N3_N4']
result['missing_shapes']=[[[0,1],[1,2]],[[0,1],[2,3]]]
result['gate_order']=GATES
result['witness_records']=len(witnesses)
result['mathematical_status']='COMPLETE_NECESSARY_DOMAIN_ACCEPTED_BY_PROVED_GATES_PENDING_ROOT_AUDIT'
with (HERE/'FOUR_QUAD_WITNESSES.jsonl').open('w') as out:
    for record in witnesses:out.write(json.dumps(record,separators=(',',':'))+'\n')
(HERE/'FOUR_QUAD_PROFILE.json').write_text(json.dumps(result,indent=2)+'\n')
print(result)
