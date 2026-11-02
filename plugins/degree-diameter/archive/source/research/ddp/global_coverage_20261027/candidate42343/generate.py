#!/usr/bin/env python3
"""Reproduce the42343-vertex extension of Dharunish's published42342 graph.

No searches or distance computations. --dry-run --compare only reads files.
"""
import argparse
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
PROJECT = HERE.parents[3]


def read_base(path, expected_n, expected_m):
    adjacency = []
    with path.open() as stream:
        for line in stream:
            if not line.strip() or line.startswith('#'):
                continue
            row = list(map(int, line.split()))
            if row[0] != len(adjacency):
                raise ValueError('source rows must be numbered0..n-1 in order')
            adjacency.append(row[1:])
    if len(adjacency) != expected_n:
        raise ValueError('source order differs from the fixed construction')
    edges = set()
    for u, neighbors in enumerate(adjacency):
        if len(neighbors) != len(set(neighbors)):
            raise ValueError('source has a repeated neighbor')
        for v in neighbors:
            if not 0 <= v < expected_n or v == u:
                raise ValueError('source contains an invalid neighbor')
            if u < v:
                edges.add((u, v))
    if len(edges) != expected_m or sum(map(len, adjacency)) != 2*expected_m:
        raise ValueError('source edge count differs from the fixed construction')
    if any(u not in adjacency[v] for u, neighbors in enumerate(adjacency) for v in neighbors):
        raise ValueError('source adjacency is not symmetric')
    return adjacency, edges


def compare_edge_file(path, expected_n, expected_edges):
    with path.open() as stream:
        n, m = map(int, stream.readline().split())
        listed = [tuple(sorted(map(int, line.split()))) for line in stream if line.strip()]
    actual = set(listed)
    return dict(file=str(path), header_matches=n == expected_n and m == len(expected_edges),
                edge_set_matches=actual == expected_edges,
                repeated_edges=len(listed)-len(actual),
                missing_edges=len(expected_edges-actual), extra_edges=len(actual-expected_edges))


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--parameters', type=Path, default=HERE/'parameters.json')
    parser.add_argument('--source', type=Path, help='Dhar42342 adjacency file; defaults to project-saved source')
    parser.add_argument('--output', type=Path, help='Write rebuilt edge list here; no default output')
    parser.add_argument('--dry-run', action='store_true', help='Only construct in memory; never write a graph')
    parser.add_argument('--compare', type=Path, help='Read and compare an existing edge list, without BFS')
    args = parser.parse_args()
    if not args.dry_run and args.output is None:
        parser.error('--output is required unless --dry-run is selected')
    parameters = json.loads(args.parameters.read_text())
    source = args.source or PROJECT/parameters['base_graph']['project_file']
    base_n, base_m = parameters['base_graph']['n'], parameters['base_graph']['m']
    adjacency, old_edges = read_base(source, base_n, base_m)
    new_vertex = parameters['extension']['new_vertex_label']
    neighbors = parameters['extension']['full_neighbor_set']
    assert new_vertex == base_n and neighbors == sorted(set(neighbors))
    assert len(neighbors) == 12 and all(len(adjacency[v]) < 12 for v in neighbors)
    edges = old_edges | {(v, new_vertex) for v in neighbors}
    degrees = list(map(len, adjacency)) + [len(neighbors)]
    for v in neighbors:
        degrees[v] += 1
    result = dict(n=base_n+1, m=len(edges), min_degree=min(degrees), max_degree=max(degrees),
                  source_n=base_n, source_m=len(old_edges), new_vertex=new_vertex,
                  new_neighbor_set=neighbors, all_old_edges_preserved=old_edges <= edges,
                  dry_run=args.dry_run, graph_written=False, BFS_performed=False)
    assert result['n'] == 42343 and result['m'] == 245229 and result['max_degree'] == 12
    if args.compare:
        comparison = compare_edge_file(args.compare, result['n'], edges)
        result['comparison'] = comparison
        assert comparison['header_matches'] and comparison['edge_set_matches']
        assert comparison['repeated_edges'] == 0
    if not args.dry_run:
        with args.output.open('w') as stream:
            stream.write(f"{result['n']} {result['m']}\n")
            for u, v in sorted(edges):
                stream.write(f'{u} {v}\n')
        result['graph_written'] = True
        result['output'] = str(args.output)
    print(json.dumps(result, indent=2))


if __name__ == '__main__':
    main()
