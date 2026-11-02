#!/usr/bin/env python3
"""Independent simple-graph and all-pairs BFS verifier. No generator import."""
import argparse
from collections import Counter, deque
import json
from pathlib import Path


def verify(path):
    lines = [line.split() for line in path.read_text().splitlines() if line.strip()]
    assert lines and len(lines[0]) == 2, 'Missing n m header'
    n, m = map(int, lines[0])
    assert n >= 0 and m == len(lines)-1, 'Wrong edge count'
    adj = [set() for _ in range(n)]
    edges = set()
    for row in lines[1:]:
        assert len(row)==2, 'Wrong edge arity'
        u,v = map(int,row)
        assert 0 <= u < n and 0 <= v < n and u != v, 'Invalid vertex or loop'
        edge = tuple(sorted((u,v)))
        assert edge not in edges, 'Duplicate edge'
        edges.add(edge); adj[u].add(v); adj[v].add(u)
    distances = Counter()
    missing = []
    for root in range(n):
        dist = [-1]*n; dist[root] = 0; queue = deque([root])
        while queue:
            u = queue.popleft()
            for v in adj[u]:
                if dist[v] < 0:
                    dist[v] = dist[u]+1; queue.append(v)
        for v in range(root+1,n):
            distances[dist[v]] += 1
            if dist[v] < 0 or dist[v]>2: missing.append([root,v])
    degree_hist = dict(sorted(Counter(map(len, adj)).items()))
    result = {'n':n,'m':m,'simple':True,'degree_histogram':degree_hist,
              'max_degree':max(map(len,adj), default=0),
              'distance_histogram':dict(sorted(distances.items())),
              'uncovered_pairs':missing,
              'valid_degree8_diameter2':max(map(len,adj),default=0)<=8 and not missing}
    return result


def main():
    parser = argparse.ArgumentParser(); parser.add_argument('edge_file', type=Path)
    parser.add_argument('--out',type=Path); args=parser.parse_args()
    result=verify(args.edge_file); text=json.dumps(result,indent=2)+'\n'
    if args.out: args.out.write_text(text)
    print(text,end='')
    raise SystemExit(0 if result['valid_degree8_diameter2'] else 1)

if __name__=='__main__': main()
