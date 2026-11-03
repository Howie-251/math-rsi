#!/usr/bin/env python3
"""Rebuild a frozen D5 graph from one compressed source and literal additions."""
import argparse
import gzip
import importlib.util
import json
from pathlib import Path
import shutil
import tempfile

HERE = Path(__file__).resolve().parent


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--degree', type=int, choices=[11, 12, 13], required=True)
    parser.add_argument('--order', type=int, required=True)
    parser.add_argument('--output', type=Path)
    parser.add_argument('--compare', type=Path)
    args = parser.parse_args()
    if args.output is None and args.compare is None:
        parser.error('Supply --output or --compare.')
    spec = importlib.util.spec_from_file_location('saved_d5_generator', HERE / 'family_generator.py')
    generator = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(generator)
    family = json.loads((HERE / 'families.json').read_text())['families'][str(args.degree)]
    with tempfile.TemporaryDirectory(prefix='dd-d5-source-') as tmp:
        source = Path(tmp) / 'base.adjlist.txt'
        with gzip.open(HERE / 'bases' / f'degree{args.degree}.adjlist.txt.gz', 'rb') as src:
            with source.open('wb') as dst:
                shutil.copyfileobj(src, dst)
        edges, report = generator.construct(family, args.order, source)
    if args.compare:
        n, m, rows, saved = generator.read_edge_set(args.compare)
        matches = n == args.order and m == len(edges) and len(rows) == len(saved) and saved == edges
        if not matches:
            raise ValueError('Rebuilt graph differs from the supplied literal edge list.')
        report['literal_edge_comparison'] = 'PASS'
    if args.output:
        opener = gzip.open if args.output.suffix == '.gz' else open
        with opener(args.output, 'wt') as stream:
            stream.write(f'{args.order} {len(edges)}\n')
            for u, v in sorted(edges):
                stream.write(f'{u} {v}\n')
        report['output'] = str(args.output)
    report['distance_checks_executed'] = False
    print(json.dumps(report, ensure_ascii=False, indent=2))


if __name__ == '__main__':
    main()
