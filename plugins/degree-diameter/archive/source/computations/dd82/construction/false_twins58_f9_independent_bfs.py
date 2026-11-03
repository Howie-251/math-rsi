"""Independent all-source BFS of a saved edge list; no generator imports."""
from collections import Counter, deque
from pathlib import Path
import json
import sys
import time


def main():
    start_cpu, start_wall = time.process_time(), time.monotonic()
    source, destination = map(Path, sys.argv[1:3])
    lines = source.read_text().splitlines()
    n, stated_edges = map(int, lines[0].split())
    assert n == 58
    adjacency = [set() for _ in range(n)]
    edges = set()
    for line in lines[1:]:
        u, v = map(int, line.split())
        assert 0 <= u < n and 0 <= v < n and u != v
        edge = tuple(sorted((u, v)))
        assert edge not in edges
        edges.add(edge)
        adjacency[u].add(v)
        adjacency[v].add(u)
    assert len(edges) == stated_edges == 232
    degree = [len(row) for row in adjacency]
    assert degree == [8] * n
    bad = []
    distance_histogram = Counter()
    disconnected = False
    diameter = 0
    for start in range(n):
        distance = [-1] * n
        distance[start] = 0
        queue = deque([start])
        while queue:
            current = queue.popleft()
            for neighbor in adjacency[current]:
                if distance[neighbor] == -1:
                    distance[neighbor] = distance[current] + 1
                    queue.append(neighbor)
        for end in range(start+1, n):
            d = distance[end]
            disconnected |= d == -1
            if d >= 0:
                diameter = max(diameter, d)
            distance_histogram[str(d)] += 1
            if d == -1 or d > 2:
                bad.append(dict(pair=[start, end], distance=None if d == -1 else d,
                    common_neighbors=sorted(adjacency[start] & adjacency[end])))
    report = dict(parent_run_id='dd82-v3-f9-c7-20261013-0749',
        source=str(source), implementation='standalone adjacency sets and deque BFS',
        imports_from_search_or_matrix_code=False, all_source_bfs_count=n,
        n=n, edge_count=len(edges), simple=True, degrees=degree,
        connected=not disconnected, diameter=None if disconnected else diameter,
        bad_pair_count=len(bad), bad_pairs=bad,
        unordered_distance_histogram=dict(sorted(distance_histogram.items())),
        valid_target=not bad, cpu_seconds=time.process_time()-start_cpu,
        wall_seconds=time.monotonic()-start_wall)
    destination.write_text(json.dumps(report, indent=2)+'\n')
    print(json.dumps({key:value for key,value in report.items()
        if key not in ['degrees', 'bad_pairs']}))


if __name__ == '__main__':
    main()
