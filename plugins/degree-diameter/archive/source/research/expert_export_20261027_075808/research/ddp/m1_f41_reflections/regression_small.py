"""Independent implementation regression only: four prescribed 40-vertex families.

This does not extend the research parameter scope. Every legal tiny assignment
is expanded as an undirected graph and checked by BFS from all forty vertices.
"""
from collections import Counter,deque
from itertools import product
from pathlib import Path
import json,time

HERE=Path(__file__).resolve().parent
P=5;M=4;R=2;Q=P*M
power=[pow(R,i,P) for i in range(M)]

def multiply(g,h):
    x,i=divmod(g,M);y,j=divmod(h,M)
    return ((x+power[i]*y)%P)*M+(i+j)%M

def inverse(g):
    x,i=divmod(g,M)
    return (-power[-i%M]*x%P)*M+(-i)%M

def graph(kind,beta,sigma,tau,values):
    if kind=='mixed':
        b,s,t=values;b=b*M+beta
        if b==inverse(b):return None
        B=[b,inverse(b)]
    else:
        b,d,s,t=values
        if b==d:return None
        B=[b*M+2,d*M+2]
    S=[0,s*M+sigma,t*M+tau]
    if len(set(S))<3:return None
    A=[2,M+2];edges=set()
    for side,internal in [(0,A),(1,B)]:
        for g in range(Q):
            for a in internal:edges.add(tuple(sorted((side*Q+g,side*Q+multiply(g,a)))))
    for g in range(Q):
        for s in S:edges.add((g,Q+multiply(g,s)))
    assert len(edges)==100 and all(u!=v for u,v in edges)
    adj=[set() for _ in range(2*Q)]
    for u,v in edges:adj[u].add(v);adj[v].add(u)
    assert all(len(ns)==5 for ns in adj)
    return adj

def check(adj):
    misses=[];diameter=0
    for root in range(2*Q):
        distances=[-1]*(2*Q);distances[root]=0;queue=deque([root])
        while queue:
            u=queue.popleft()
            for v in adj[u]:
                if distances[v]<0:distances[v]=distances[u]+1;queue.append(v)
        assert -1 not in distances
        misses.append(sum(d>5 for d in distances));diameter=max(diameter,max(distances))
    assert len(set(misses[:Q]))==len(set(misses[Q:]))==1
    score=misses[0]+misses[Q]
    assert sum(misses)==Q*score
    return score,diameter

def main():
    start=time.process_time();rows=[]
    specs=[('mixed',0,0,1),('mixed',1,0,1),('both',2,0,1),('both',2,1,1)]
    for kind,beta,sigma,tau in specs:
        count=0;illegal=0;hist=Counter();dhist=Counter();examples={}
        dimension=3 if kind=='mixed' else 4
        for values in product(range(P),repeat=dimension):
            count+=1;adj=graph(kind,beta,sigma,tau,values)
            if adj is None:illegal+=1;continue
            score,diameter=check(adj);hist[score]+=1;dhist[diameter]+=1
            key='diameter_at_most5' if score==0 else 'diameter_over5'
            examples.setdefault(key,dict(parameters=list(values),two_root_missing=score,diameter=diameter))
        rows.append(dict(kind=kind,beta=beta,sigma=sigma,tau=tau,raw_assignments=count,
                         legal_assignments=count-illegal,illegal_assignments=illegal,
                         two_root_missing_histogram=dict(sorted(hist.items())),
                         diameter_histogram=dict(sorted(dhist.items())),examples=examples))
    result=dict(scope='Four prescribed tiny implementation regression families only; no production search',
                group=dict(p=P,m=M,r=R),vertices=2*Q,edges_per_legal_graph=100,
                root_vertex_ids=[0,Q],vertex_id='layer*20+translation*4+quotient',
                A=[[0,2],[1,2]],method='independent explicit undirected edge set, every-source BFS for every legal assignment',
                counts=rows,total_raw=sum(r['raw_assignments'] for r in rows),
                total_legal=sum(r['legal_assignments'] for r in rows),cpu_seconds=time.process_time()-start)
    (HERE/'regression_expected.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2))

if __name__=='__main__':main()
