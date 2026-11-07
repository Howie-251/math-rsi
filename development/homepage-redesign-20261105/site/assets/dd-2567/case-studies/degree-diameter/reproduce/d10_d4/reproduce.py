#!/usr/bin/env python3
"""Replay the frozen (10,4) graphs of orders 2558 through 2567."""

import argparse
import gzip
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent


def iter_graphs(stop_order=2567):
    """Yield (order, complete unordered edge set) after each saved edit."""
    recipe = json.loads((HERE / "edits.json").read_text())
    with gzip.open(HERE / recipe["source"]["file"], "rt") as source:
        n, m = map(int, source.readline().split())
        edges = {tuple(map(int, line.split())) for line in source if line.strip()}
    if (n, m, len(edges)) != (2557, 12785, 12785):
        raise ValueError("Packaged source does not have the recorded size")
    for step in recipe["steps"]:
        removed = {tuple(e) for e in step["remove_edges"]}
        added = {tuple(e) for e in step["add_edges"]}
        if not removed <= edges or added & edges:
            raise ValueError(f"Saved edits do not apply at order {step['order']}")
        edges.difference_update(removed)
        edges.update(added)
        n = step["order"]
        if len(edges) != step["edges"]:
            raise ValueError(f"Wrong edge count at order {n}")
        yield n, edges
        if n == stop_order:
            return


def write_edges(path, order, edges):
    """Write a header and one sorted u v line per undirected edge."""
    with path.open("w") as output:
        output.write(f"{order} {len(edges)}\n")
        for u, v in sorted(edges):
            output.write(f"{u} {v}\n")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    target = parser.add_mutually_exclusive_group(required=True)
    target.add_argument("--order", type=int, choices=range(2558, 2568))
    target.add_argument("--all", action="store_true", help="write all ten graphs")
    parser.add_argument("--output", type=Path, help="edge file for --order")
    parser.add_argument("--output-dir", type=Path, help="directory for --all")
    args = parser.parse_args()
    if args.all:
        if args.output_dir is None or args.output is not None:
            parser.error("--all requires --output-dir")
        args.output_dir.mkdir(parents=True, exist_ok=True)
        stop = 2567
    else:
        if args.output is None or args.output_dir is not None:
            parser.error("--order requires --output")
        stop = args.order
    for order, edges in iter_graphs(stop):
        if args.all or order == stop:
            path = (args.output_dir / f"d10_D4_n{order}.edges") if args.all else args.output
            write_edges(path, order, edges)
            print(f"Rebuilt {order} vertices / {len(edges)} edges: {path}")


if __name__ == "__main__":
    main()
