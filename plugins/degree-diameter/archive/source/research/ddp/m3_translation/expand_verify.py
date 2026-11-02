"""Independent expansion and all-source BFS, with no search mask tables."""
from pathlib import Path
from collections import deque,Counter
import argparse,json,time


def plus3(a,b):
    # Deliberately use coordinate tuples rather than the searcher's packed loops.
    av=(a%3,a//3%3,a//9);bv=(b%3,b//3%3,b//9)
    return sum(((x+y)%3)*3**i for i,(x,y) in enumerate(zip(av,bv)))


def main():
    p=argparse.ArgumentParser();p.add_argument('candidate',type=Path);args=p.parse_args()
    data=json.loads(args.candidate.read_text());n=data['control_order'];N=27*n
    control_pairs=set();edges=set()
    for u,v,d in data['edge_directions']:
        assert 0<=u<v<n and 1<=d<27 and (u,v) not in control_pairs
        control_pairs.add((u,v))
        for x in range(27):
            for delta in (0,d,plus3(d,d)):
                a=27*u+x;b=27*v+plus3(x,delta)
                assert a!=b;edges.add((a,b))
    edgefile=args.candidate.with_name(args.candidate.stem+'.expanded.edges')
    edgefile.write_text(''.join(f'{u} {v}\n' for u,v in sorted(edges)))
    # Read the written edge list afresh; BFS does not retain generation adjacency.
    adjacency=[set() for _ in range(N)];seen_edges=set()
    for line in edgefile.read_text().splitlines():
        u,v=map(int,line.split());assert 0<=u<v<N and (u,v) not in seen_edges
        seen_edges.add((u,v));adjacency[u].add(v);adjacency[v].add(u)
    degree_hist=Counter(map(len,adjacency));assert degree_hist=={12:N}
    started=time.monotonic();missing=0;missing_zero=0;diameter=0;disconnected_sources=0
    for source in range(N):
        dist=[-1]*N;dist[source]=0;queue=deque([source])
        while queue:
            u=queue.popleft()
            for v in adjacency[u]:
                if dist[v]<0:dist[v]=dist[u]+1;queue.append(v)
        bad=sum(d<0 or d>3 for d in dist);missing+=bad
        if source%27==0:missing_zero+=bad
        if min(dist)<0:disconnected_sources+=1
        diameter=max(diameter,max(dist))
    assert missing_zero==data['missing_from_control_roots_fiber_zero']
    assert missing==27*missing_zero
    result=dict(status='independent_all_source_edge_list_verification',order=N,edges=len(seen_edges),
                degree_hist=dict(degree_hist),simple=True,connected=disconnected_sources==0,
                diameter=diameter if not disconnected_sources else None,
                missing_ordered_pairs_D3=missing,missing_control_roots_zero=missing_zero,
                score_agrees=True,translation_orbit_factor_agrees=True,
                passes_degree_diameter=(missing==0),seconds=time.monotonic()-started)
    args.candidate.with_name(args.candidate.stem+'_verification.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2))


if __name__=='__main__':main()
