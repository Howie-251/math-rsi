from pathlib import Path
from collections import deque, Counter
import json, time

P=Path(__file__).resolve().parent
out=P/'root_monotone_closure.json'
assert not out.exists(), 'Reuse the existing closure check.'
started=time.process_time()
q=json.loads((P.parent/'hexagon_partial_fold_scout/Q_data.json').read_text())
s=json.loads((P/'best_state.json').read_text())
st=s['states']; cp=s['h3_extra_copies']; Q=q['Q']; hn=q['H3_neighbors']
loads=[sum(st[v]!=0 and (st[u]==0 or st[u]==st[v]) for v in Q[u])+(cp[hn[u]] if hn[u]>=0 else 0) for u in range(len(Q))]
hd=[7-int(q['H3_absolute'][h])+sum(st[v]!=0 for v in q['H3_generic_neighbors'][h])+sum(cp[g] for g in q['H3_graph'][h]) for h in range(364)]
saved=json.loads((P/'best_loads.json').read_text())
assert loads==saved['generic_loads'] and hd==saved['H3_copy_degrees']
assert max(loads)<=2 and max(hd)<=12
merged={u for u,v in enumerate(st) if v==0}
critical={u for u in merged if loads[u]==2}
blocked={u for u in merged if hn[u]>=0 and hd[hn[u]]==12}
initial=sorted(blocked)
queue=deque(sorted(blocked&critical)); seen=set(queue); reason={u:['H3_FULL',hn[u]] for u in blocked}
while queue:
    v=queue.popleft()
    for u in Q[v]:
        if u in merged and u not in blocked:
            blocked.add(u); reason[u]=['FORCED_CRITICAL_MERGED_NEIGHBOR',v]
            if u in critical and u not in seen: seen.add(u); queue.append(u)
seen_comp=set(); sizes=[]
for root in sorted(critical):
    if root in seen_comp: continue
    seen_comp.add(root); queue=deque([root]); size=0
    while queue:
        u=queue.popleft(); size+=1
        for v in Q[u]:
            if v in critical and v not in seen_comp: seen_comp.add(v); queue.append(v)
    sizes.append(size)
result=dict(status='COMPLETE',source_split_fibers=sum(v!=0 for v in st),merged_fibers=len(merged),critical_merged_fibers=len(critical),initial_H3_full_blocked=len(initial),propagated_forbidden_merged=len(blocked),remaining_not_excluded=len(merged-blocked),critical_component_sizes=sorted(sizes,reverse=True),entire_monotone_extension_excluded=(blocked==merged),scope='Any S superset of the fixed7959 splits with the same280 H3 copy counts; existing/new split colors may vary. This is only a necessary implication closure, not a general partial-fold exclusion.',implication='If old merged v has full load2 and a neighbor u is newly split, v must also be newly split. A vertex at an already full H3 neighbor cannot be newly split.',CPU_seconds=time.process_time()-started,full_BFS_performed=False,new_lower_bounds=0)
out.write_text(json.dumps(result,indent=2)+'\n')
(P/'monotone_closure_witness.json').write_text(json.dumps({'initial_H3_full_blocked':initial,'forbidden_reasons':reason,'not_excluded_merged':sorted(merged-blocked)})+'\n')
print(json.dumps(result))
