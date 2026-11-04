"""Extend the EP0 triangle rule to artificial pairs of crossing ports.

A closed branch is certified by exact Hall sets and elementary clause splits.
An avoiding matching refutes only this sufficient rule, never EP0 itself.
"""
import json,itertools
from pathlib import Path
R=Path(__file__).resolve().parent
edge=lambda a,b:tuple(sorted((a,b)))

def matching_or_hall(H,forbidden):
    ev=[a for a in range(64) if a.bit_count()%2==0 and a not in H]
    adj={a:[a^(1<<i) for i in range(6) if a^(1<<i) not in H and edge(a,a^(1<<i)) not in forbidden] for a in ev}
    mate={}
    def aug(a,seen):
        for b in adj[a]:
            if b in seen:continue
            seen.add(b)
            if b not in mate or aug(mate[b],seen):mate[b]=a;return True
        return False
    for a in ev:aug(a,set())
    if len(mate)==len(ev):return frozenset(edge(a,b) for b,a in mate.items()),None
    U=set(ev)-set(mate.values());todo=list(U)
    while todo:
        a=todo.pop()
        for b in adj[a]:
            if b in mate and mate[b] not in U:U.add(mate[b]);todo.append(mate[b])
    N={b for a in U for b in adj[a]};assert len(U)>len(N)
    return None,dict(even_set=sorted(U),neighbors=sorted(N))

def run(row):
    v=row['target'];Z=set(row['Z']);W=set(row['W']);H={0}|Z|W;clauses={}
    for i in row['cuts']:
        A={a for a in range(64) if ((a^v)>>i)&1==0};ZA=Z&A;S={w^(1<<i) for w in W}
        for q in sorted(A-H-{v}):
            if q.bit_count()%2==0 or q^(1<<i) in H:continue
            outside={q^(1<<j) for j in range(6) if j!=i}-S
            if len(outside)>2:continue
            roots={0} if 0 in A else ZA
            for root in sorted(roots):
                terminal_rule=len(outside)==2 and root in outside
                if terminal_rule and v^(1<<i) in H:continue
                required={edge(q,q^(1<<i))}
                if terminal_rule:required.add(edge(v,v^(1<<i)))
                valid=True
                if len(outside)==2:
                    for a in outside:
                        if terminal_rule and a==root:continue
                        if a in ZA-{root}:continue
                        if a in H or a^(1<<i) in H:valid=False;break
                        required.add(edge(a,a^(1<<i)))
                if not valid:continue
                clauses.setdefault(frozenset(required),dict(cut=i,q=q,root=root,outside=sorted(outside),rule="forced_endpoint_path" if terminal_rule else "triangle",required_edges=sorted(required)))
    cs=sorted(clauses,key=lambda f:(len(f),sorted(f)));nodes=[];memo={};counter=None
    def prove(forbidden):
        nonlocal counter
        if forbidden in memo:return memo[forbidden]
        idx=len(nodes);memo[forbidden]=idx;nodes.append({})
        M,hall=matching_or_hall(H,forbidden)
        if M is None:nodes[idx]=dict(hall=hall);return idx
        conflict=next((j for j,c in enumerate(cs) if c<=M),None)
        if conflict is None:counter=sorted(M);nodes[idx]=dict(counterexample=counter);return idx
        children=[]
        for e in sorted(cs[conflict]):
            children.append(prove(forbidden|{e}))
            if counter is not None:break
        nodes[idx]=dict(clause=conflict,children=children);return idx
    prove(frozenset())
    return dict(target=v,Z=sorted(Z),W=sorted(W),clauses=[clauses[c] for c in cs],
        closed_by_port_triangle=counter is None,proof_nodes=nodes,avoiding_matching=counter)

def main():
    source=json.loads((R/'eight_hole_covered_next_probe.json').read_text());reports=[]
    for row in source['joint_results']:
        r=run(row);reports.append(r)
        print(r['target'],r['Z'],'clauses',len(r['clauses']),'closed',r['closed_by_port_triangle'],'nodes',len(r['proof_nodes']),flush=True)
    (R/'eight_ep0_endpoint_path_probe.json').write_text(json.dumps(dict(scope='Candidate EP0 port triangle extension; independent check pending',reports=reports),indent=2)+'\n')
if __name__=='__main__':main()
