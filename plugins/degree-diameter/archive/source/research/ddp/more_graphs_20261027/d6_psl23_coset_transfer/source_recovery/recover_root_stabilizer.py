"""Recover source stabilizer permutations by deterministic colour matching.

Only individualizes root0 and each member of its known four-suborbit, then
checks resulting maps against literal adjacency. No BFS/new graph search.
"""
from pathlib import Path
from collections import Counter
from math import lcm
import json
import time

OUT=Path(__file__).resolve().parent


def colours(adj,pin,root=0):
    c=[0]*len(adj);c[root]=1;c[pin]=2;rounds=0
    while True:
        keys=[(c[v],tuple(sorted(c[w] for w in adj[v]))) for v in range(len(adj))]
        ids={k:i for i,k in enumerate(sorted(set(keys)))}
        new=[ids[k] for k in keys];rounds+=1
        if len(set(new))==len(set(c)):return new,rounds
        c=new


def main():
    t=time.process_time()
    adj=[set(map(int,l.split())) for l in (OUT/'graph_d6_k5_n1518.adj').read_text().splitlines()]
    base,rounds=colours(adj,329)
    result=dict(status='ROOT_STABILIZER_SOURCE_RECOVERY',n=len(adj),root=0,
                base_individualized=329,base_rounds=rounds,base_colour_count=len(set(base)),
                rows=[],source_BFS=0,new_parameter_graphs=0)
    if len(set(base))==len(adj):
        for target in [329,435,533,776]:
            c,steps=colours(adj,target)
            row=dict(target=target,rounds=steps,colour_count=len(set(c)))
            if len(set(c))==len(adj):
                lookup={v:i for i,v in enumerate(c)}
                perm=[lookup[v] for v in base]
                exact=all({perm[w] for w in adj[v]}==adj[perm[v]] for v in range(len(adj)))
                order=1;seen=set()
                for v in range(len(adj)):
                    if v in seen:continue
                    w=v;length=0
                    while w not in seen:seen.add(w);length+=1;w=perm[w]
                    order=lcm(order,length)
                row.update(exact_source_automorphism=exact,root_fixed=perm[0]==0,
                           base_pin_image=perm[329],order=order,permutation=perm)
            result['rows'].append(row)
    # Actual source connection transporters, retained as literal permutations.
    # The four-valent orbital has a unique edge flip because its arc stabilizer
    # is trivial. Degree-one orbitals are tried at their actual source labels.
    result['connection_transporters']=[]
    for target in [329,967,981]:
        for pin in ([0] if target==329 else sorted(adj[target])):
            c,steps=colours(adj,pin,root=target)
            if len(set(c))!=len(adj):continue
            lookup={v:i for i,v in enumerate(c)}
            perm=[lookup[v] for v in base]
            exact=all({perm[w] for w in adj[v]}==adj[perm[v]] for v in range(len(adj)))
            if not exact or perm[0]!=target:continue
            order=1;seen=set()
            for v in range(len(adj)):
                if v in seen:continue
                w=v;length=0
                while w not in seen:seen.add(w);length+=1;w=perm[w]
                order=lcm(order,length)
            result['connection_transporters'].append(dict(root_image=target,base329_image=pin,
                exact_source_automorphism=True,order=order,permutation=perm))
            break
    result['CPU_seconds']=time.process_time()-t
    (OUT/'root_stabilizer.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({k:v for k,v in result.items() if k not in ['rows','connection_transporters']},indent=2))
    for row in result['rows']:print({k:v for k,v in row.items() if k!='permutation'})
    for row in result['connection_transporters']:print({k:v for k,v in row.items() if k!='permutation'})


if __name__=='__main__':main()
