#!/usr/bin/env python3
"""Exact binary matrix check: integer rows, coordinate j = bit j."""
import argparse
from collections import Counter
import json
from pathlib import Path

ap = argparse.ArgumentParser()
ap.add_argument('--matrix', type=Path, required=True, help='JSON list of integer rows, or object with rows')
ap.add_argument('--n', type=int, required=True)
ap.add_argument('--k', type=int, required=True)
ap.add_argument('--distance', type=int, required=True)
ap.add_argument('--output', type=Path, required=True)
a = ap.parse_args()
if not (0 < a.k <= a.n and 0 < a.distance <= a.n):
    raise ValueError('Expected positive feasible n/k/d')
data = json.loads(a.matrix.read_text())
rows = data['rows'] if isinstance(data, dict) else data
if not (isinstance(rows, list) and len(rows) == a.k and
        all(type(r) is int and 0 <= r < 1 << a.n for r in rows)):
    raise ValueError('Wrong row count or nonbinary/out-of-range integer row')
# Exhaustive by contract. Caller checks 2^k cost before requesting large k.
pivots = {}
for row in rows:
    x = row
    while x:
        j = x.bit_length()-1
        if j in pivots:
            x ^= pivots[j]
        else:
            pivots[j] = x
            break
spectrum = Counter()
best = a.n+1
word = previous_gray = 0
witness = None
for index in range(1, 1 << a.k):
    gray = index ^ (index >> 1)
    bit = (gray ^ previous_gray).bit_length()-1
    word ^= rows[bit]
    previous_gray = gray
    weight = word.bit_count()
    spectrum[weight] += 1
    if weight < best:
        best = weight
        witness = dict(message=gray, codeword=word, weight=weight)
passed = len(pivots) == a.k and best >= a.distance
report = dict(status='PASS' if passed else 'FAIL', n=a.n, k=a.k,
              target_distance=a.distance, rank=len(pivots), minimum_distance=best,
              nonzero_messages=(1 << a.k)-1, minimum_witness=witness,
              spectrum=dict(sorted(spectrum.items())), input_rows=rows)
a.output.write_text(json.dumps(report, indent=2)+'\n')
print(json.dumps({k: report[k] for k in ('status', 'rank', 'minimum_distance', 'nonzero_messages')}))
raise SystemExit(0 if passed else 1)
