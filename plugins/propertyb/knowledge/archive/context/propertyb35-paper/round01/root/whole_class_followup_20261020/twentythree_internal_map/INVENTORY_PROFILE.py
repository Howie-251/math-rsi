#!/usr/bin/env python3
from itertools import combinations
from pathlib import Path
from time import process_time
import json
P=Path(__file__).resolve().parent
# Labels0..3 low,4=h. Record actual non-singleton G traces, not just pairgraph.
types=[tuple(t) for k in (2,3) for t in combinations(range(5),k)]
def inventories(k=0,remaining=(2,2,2,2),chosen=()):
    if k==len(types):yield chosen;return
    t=types[k];cost=len(t)-1;low=[i for i in t if i<4]
    cap=min(remaining[i]//cost for i in low)
    for n in range(cap+1):
        rest=tuple(remaining[i]-n*cost if i in low else remaining[i] for i in range(4))
        yield from inventories(k+1,rest,chosen+(t,)*n)
if __name__=='__main__':
    start=process_time();items=list(inventories());elapsed=process_time()-start
    out={'actual_trace_inventory_count':len(items),'trace_type_count':len(types),'cpu_seconds':elapsed,
         'maximum_internal_edges':max(map(len,items)),
         'definition':'all nongroup G traces size2/3 with four low row repeat budgets <=2; no H enumeration',
         'histogram':{str(n):sum(len(x)==n for x in items) for n in range(9)}}
    (P/'INVENTORY_PROFILE.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out))
