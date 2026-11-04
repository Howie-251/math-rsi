"""Stress N6 with zero-short-edge bipartite matchings; no full-space assertion."""
import json,random
from pathlib import Path
import networkx as nx
from single_bridge_probe import solve,verify
ROOT=Path(__file__).resolve().parent

def main():
    rng=random.Random(20261105);out=[];n=5
    for s in (7,31):
        graph=nx.Graph();vertices=set(range(32))-{0,s};graph.add_nodes_from(vertices)
        graph.add_weighted_edges_from((p,q,rng.random()) for p in vertices if not p.bit_count()%2
                                     for q in vertices if q.bit_count()%2 and (p^q).bit_count()>1)
        l=sorted(tuple(sorted(e)) for e in nx.max_weight_matching(graph,maxcardinality=True))
        assert len(l)==15 and all((p^q).bit_count()>1 for p,q in l)
        p=l+[(0,s)];mate={a:b for e in p for a,b in (e,e[::-1])}
        for y in range(1,32):
            if y.bit_count()%2==0 or y==s:continue
            j=next(j for j in range(n) if not (s&y&(1<<j)) and s^(1<<j)!=mate[y])
            x=s^(1<<j);res=solve(n,p,x,y,4,seconds=8,allowed_long=p)
            c=dict(n=n,r=0,s=s,y=y,L=l,x=x,chosen_direction=j,status=res['status'])
            if res['status']=='FOUND':
                k=res['path'];pos=k.index(0);assert k[pos+1]==s
                h=k[:pos+1][::-1]+k[pos+1:];verify(n,l,0,y,h,allowed_long=l)
                c.update(intermediate_path=k,path=h)
            out.append(c);(ROOT/'nonadjacent_results.json').write_text(json.dumps(out,indent=2),encoding='utf8')
            print(s,y,c['status'],flush=True)
    print('TOTAL',len(out),'FOUND',sum(c['status']=='FOUND' for c in out))
if __name__=='__main__':main()
