"""Finite author sanity checks; these do not replace fresh proof review."""
from pathlib import Path
from functools import lru_cache
from itertools import combinations
import json
R=Path(__file__).resolve().parent
@lru_cache(None)
def matchings(vertices):
    if not vertices:return ((),)
    a=vertices[0];out=[]
    for b in vertices[1:]:
        rest=tuple(x for x in vertices if x not in (a,b))
        out.extend((((a,b),)+m) for m in matchings(rest))
    return tuple(out)
def components(n,edges):
    p=list(range(n));cyclic=False
    def find(x):
        while x!=p[x]:p[x]=p[p[x]];x=p[x]
        return x
    for a,b in edges:
        a,b=find(a),find(b)
        if a==b:cyclic=True
        else:p[a]=b
    return len({find(x) for x in range(n)}),cyclic
def compress(n,F,Rpairs):
    deleted={x for e in Rpairs for x in e};adj={x:[] for x in range(n)}
    for a,b in F+Rpairs:adj[a].append(b);adj[b].append(a)
    out=[];seen=set()
    for a in range(n):
        if a in deleted or a in seen:continue
        prev=None;cur=a;seen.add(a)
        while True:
            nxt=next(x for x in adj[cur] if x!=prev)
            prev,cur=cur,nxt
            if cur not in deleted:break
        seen.add(cur);out.append((a,cur))
    assert seen==set(range(n))-deleted
    return tuple(out)
cases=[];allcomparisons=0
for half in range(2,6):
    n=2*half
    for r in range(1,half):
        Rpairs=tuple((2*i,2*i+1) for i in range(r));endpoints=tuple(range(2*r,n))
        good=bad=comparisons=0
        for F in matchings(tuple(range(n))):
            _,cyclic=components(n,F+Rpairs)
            if cyclic:
                bad+=1
                for Pminus in matchings(endpoints):
                    assert components(n,F+Rpairs+Pminus)[0]>1
                    comparisons+=1
            else:
                good+=1;Fminus=compress(n,F,Rpairs);found=False
                relabel={x:i for i,x in enumerate(endpoints)}
                for Pminus in matchings(endpoints):
                    full=components(n,F+Rpairs+Pminus)[0]==1
                    reduced=components(len(endpoints),tuple((relabel[a],relabel[b]) for a,b in Fminus+Pminus))[0]==1
                    assert full==reduced;found|=full;comparisons+=1
                assert found
        allcomparisons+=comparisons;cases.append(dict(terminal_count=n,cherries=r,acyclic_F=good,cyclic_F=bad,comparisons=comparisons))
gapcases=0
for c in range(1,33):
    for s in range(3,33):
        for delta in (0,1):
            size=c+s-(1-delta)
            if size%2:continue
            d=size//2
            for j in range(c//2+1):
                assert d>j;gapcases+=1
counterR=((0,1),(2,3));counterF=((1,2),(3,0),(4,5))
assert not (set(counterR)&set(counterF)) and components(6,counterR+counterF)[1]
# The abstract no-extra-gap failure restores an entire tagged cycle.
D=((0,1),(2,3),(4,5),(6,7));T=((1,2),(3,4),(5,6),(7,0))
assert not set(D)&set(T) and components(8,D+T)==(1,True)
out=dict(status='AUTHOR_SANITY_PASS_PENDING_FRESH_REVIEW',local_contraction_cases=cases,local_pairing_comparisons=allcomparisons,automatic_gap_parameter_cases=gapcases,multi_cycle_counterexample_checked=True,no_extra_gap_abstract_counterexample_checked=True,full_higher_layer_proved=False)
(R/'HIGHER_FORCED_CHERRY_author_check.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
