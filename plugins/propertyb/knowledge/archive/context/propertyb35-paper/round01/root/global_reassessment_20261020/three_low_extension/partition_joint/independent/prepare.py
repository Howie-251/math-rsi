"""Freeze the producer's readable data as plain integer input; do not compute counts."""
import json
from pathlib import Path

here = Path(__file__).resolve().parent
data = json.loads((here.parent / 'REPRESENTATIVES.json').read_text())
assert len(data) == 264
with (here / 'INPUT.txt').open('w') as out:
    out.write(f'{len(data)}\n')
    for item in data:
        flat = [x for row in item['matrix'] for x in row]
        assert len(flat) == 25 and all(type(x) is int and 0 <= x <= 4 for x in flat)
        out.write(' '.join(map(str, [item['id'], item['key'], item['jointcount']] + flat)) + '\n')
