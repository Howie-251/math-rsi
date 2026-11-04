"""Construct Z2 witnesses, including a matching outside the Z1 criterion."""
import json, random
from pathlib import Path
import networkx as nx
from split_transfer import construct, criterion

ROOT=Path(__file__).resolve().parent

def degenerate():
    # In A, only the two edges incident to a,b use directions other than k.
    special=[(2,6),(60,56),(4,5),(58,59)]
    excluded={0,62,2,6,60,56,4,58}
    ma=[(q,q^2) for q in range(0,64,2) if q not in excluded and q<(q^2)]
    vertices=set(range(1,64,2))-{3,61,5,59}
    graph=nx.Graph(); graph.add_nodes_from(sorted(vertices))
    rng=random.Random(7331)
    for q in sorted(vertices):
        for j in range(1,6):
            r=q^(1<<j)
            if r in vertices and q<r: graph.add_edge(q,r,weight=rng.random())
    mb=nx.max_weight_matching(graph,maxcardinality=True)
    m=sorted(tuple(sorted(e)) for e in ma+special+list(mb))
    assert len(m)==30 and len({x for e in m for x in e})==60
    assert criterion(m,0,1) is None
    return m

def main():
    old=json.loads((ROOT/'four_hole_surgery.json').read_text(encoding='utf8'))
    templates={}
    for c in old:
        if c['kind']=='distance_five_holes':
            m=sorted(tuple(sorted(e)) for e in c['matching'])
            templates[tuple(m)]=m
    templates[tuple(degenerate())]=degenerate()
    targets=[1,2]+[v for v in range(64) if v&3==3 and v.bit_count()%2]
    out=[]
    for index,m in enumerate(templates.values()):
        mate={a:b for e in m for a,b in (e,e[::-1])}
        for v in targets:
            i=1 if v==2 else 0;bit=1<<i
            w=next(q for q in (61,62) if not q&bit);t=123-w
            a,b,y=3^bit,t^bit,w^bit
            cert=dict(cut=i,z=3,w=w,t=t,a=a,b=b,y=y,r=mate[y])
            result=construct(m,0,v,cert)
            out.append(dict(n=6,u=0,v=v,matching=m,template=index,
                            Z1_applicable=criterion(m,0,v) is not None,**cert,**result))
            (ROOT/'far_holes_results.json').write_text(json.dumps(out,indent=2),encoding='utf8')
            print(index,v,result['status'],flush=True)
    print('TOTAL',len(out),'FOUND',sum(c['status']=='FOUND' for c in out),
          'outside_Z1',sum(not c['Z1_applicable'] for c in out))

if __name__=='__main__':main()
