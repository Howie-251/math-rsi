#!/usr/bin/env python3
"""Generate Brown's PG(2,7) orthogonality graph, using integer arithmetic only."""
import argparse
import json
from itertools import combinations
from pathlib import Path


def generate():
    # Canonical projective representatives: first nonzero coordinate is 1.
    points = [(1, a, b) for a in range(7) for b in range(7)]
    points += [(0, 1, a) for a in range(7)] + [(0, 0, 1)]
    edges = [(i, j) for i, j in combinations(range(len(points)), 2)
             if sum(x*y for x, y in zip(points[i], points[j])) % 7 == 0]
    return points, edges


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--out', type=Path, default=Path(__file__).parent)
    args = parser.parse_args()
    args.out.mkdir(parents=True, exist_ok=True)
    points, edges = generate()
    # A fully explicit independent format: n m header; then one undirected edge per line.
    (args.out/'brown57.edges').write_text(f'{len(points)} {len(edges)}\n' + ''.join(f'{i} {j}\n' for i,j in edges))
    (args.out/'brown57.vertices.json').write_text(json.dumps(points, indent=2)+'\n')
    print(json.dumps({'n':len(points),'m':len(edges),'edge_file':str(args.out/'brown57.edges')}))

if __name__ == '__main__':
    main()
