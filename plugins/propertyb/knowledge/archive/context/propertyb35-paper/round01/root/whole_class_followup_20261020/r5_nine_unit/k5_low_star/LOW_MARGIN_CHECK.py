"""Five real low points: necessary common residual-partition capacities.
Every positive G trace T has mu[T] actual edge slots, each holding at most
min(2,5-|T|) low points. Enumerate five residual partitions as a multiset;
no complete original-H or ten-lock trace catalogue is generated.
"""
from pathlib import Path
from collections import Counter
import json,time
P=Path(__file__).resolve().parent;ROOT=P.parents[6]
res=json.loads((P/'RESULT.json').read_text())
cat=json.loads((ROOT/'context/propertyb35-paper/round01/twentyfive/GROUP5_CATALOGUE.json').read_text())
mus={z['id']:{int(t):n for t,n in z['counts'].items()} for z in cat['representatives']}
start=time.process_time();out=[]
for f in res['families']:
    ident=f['id'];pp=[tuple(p) for p in f['residual_partitions']];mu=mus[ident]
    cap={t:min(5,n*min(2,5-t.bit_count())) for t,n in mu.items() if t}
    nodes=0;complete_leaves=0;witness=None;use=Counter()
    def dfs(first,left,picked):
        global nodes,complete_leaves,witness
        nodes+=1
        if not left:
            complete_leaves+=1;witness=picked;return True
        for i in range(first,len(pp)):
            part=pp[i]
            if any(use[t]+1>cap[t] for t in part):continue
            use.update(part)
            ok=dfs(i,left-1,picked+[list(part)])
            use.subtract(part)
            if ok:return True
        return False
    possible=dfs(0,5,[])
    exact={'id':ident,'residual_partition_types':len(pp),'capacity':cap,'recursion_nodes':nodes,
           'has_necessary_five_low_capacity_witness':possible,'five_low_partition_witness':witness,
           'conclusion':'not_excluded_by_this_relaxation' if possible else 'excluded_by_all_five_low_residual_partitions'}
    if witness:
        used=Counter(t for p in witness for t in p)
        assert all(used[t]<=cap[t] for t in used)
        assert all(set(p) in [set(q) for q in pp] for p in witness)
        assert all(sum(t.bit_count() for t in p)==5 for p in witness)
        exact['witness_trace_loads']=dict(used)
    out.append(exact)
summary={'scope':'Necessary capacities of the same five actual low-point G-partitions; success witnesses are relaxations, not H constructions',
         'families':18,'excluded_ids':[z['id'] for z in out if not z['has_necessary_five_low_capacity_witness']],
         'remaining_ids':[z['id'] for z in out if z['has_necessary_five_low_capacity_witness']],
         'full_G_ids_not_covered':[23,24,25,26],'CPU_seconds':time.process_time()-start}
(P/'LOW_MARGIN_RESULT.json').write_text(json.dumps({'summary':summary,'records':out},indent=2)+'\n')
print(json.dumps(summary,indent=2))
for z in out:print(z['id'],z['has_necessary_five_low_capacity_witness'],z['five_low_partition_witness'])
