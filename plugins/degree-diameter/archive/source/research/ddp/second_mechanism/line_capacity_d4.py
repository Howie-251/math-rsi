"""All-control-pair necessary capacity for dimension-four F2 line lifts.

This overcounts unions, so a capacity below 16 is an obstruction; passing is
not an existence claim. Rank bounds through length four use only immediate
edge reversals and the nested return e,f,f,e, and permit arbitrary charts.
"""
from pathlib import Path
from collections import deque,Counter
import argparse,json,time


def main():
    parser=argparse.ArgumentParser();parser.add_argument('edges',type=Path)
    parser.add_argument('--baseline',type=int,required=True);args=parser.parse_args()
    edges=[tuple(map(int,line.split())) for line in args.edges.read_text().splitlines()
           if line and not line.startswith('#')]
    n=max(max(e) for e in edges)+1;adj=[[] for _ in range(n)]
    assert len(set(tuple(sorted(e)) for e in edges))==len(edges)
    for e,(u,v) in enumerate(edges):
        assert u!=v;adj[u].append((v,e));adj[v].append((u,e))
    degrees={len(a) for a in adj};assert len(degrees)==1
    start=time.monotonic();hist=Counter();worst=0;bad=[];mincap=10**9
    for source in range(n):
        distance=[-1]*n;distance[source]=0;queue=deque([source])
        while queue:
            u=queue.popleft()
            for v,_ in adj[u]:
                if distance[v]<0:distance[v]=distance[u]+1;queue.append(v)
        assert min(distance)>=0;worst=max(worst,max(distance));hist.update(distance)
        cap=[0]*n;cap[source]=1;paths=[(source,())]
        for length in range(1,5):
            nxt=[]
            for u,h in paths:
                for v,e in adj[u]:
                    hh=h+(e,)
                    rank=length-sum(hh[i]==hh[i+1] for i in range(length-1))
                    if length==4 and hh[0]==hh[3] and hh[1]==hh[2]:rank=min(rank,2)
                    cap[v]+=2**rank;nxt.append((v,hh))
            paths=nxt
        for v,c in enumerate(cap):
            mincap=min(mincap,c)
            if c<16:bad.append([source,v,c,distance[v]])
    rho=next(iter(degrees))
    result=dict(status='known_control_verified_necessary_capacity_only',control_order=n,
                control_degree=rho,control_diameter=worst,q=2,s=4,lift_degree=2*rho,
                lift_order=16*n,target_D=4,snapshot_lower_bound=args.baseline,
                ordered_distance_hist=dict(hist),bad_capacity_pairs=len(bad),
                first_bad_pairs=bad[:20],min_capacity=mincap,seconds=time.monotonic()-start)
    out=args.edges.with_name(args.edges.stem+'_f2s4_capacity.json')
    out.write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2))


if __name__=='__main__':main()
