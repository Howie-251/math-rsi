"""Read the frozen, fully checked 264 representatives; do not generate matrices."""
import json
from pathlib import Path

here = Path(__file__).parent
source = here.parent.parent / 'global_reassessment_20261020/three_low_extension/partition_joint/REPRESENTATIVES.json'
rows = json.loads(source.read_text())
assert len(rows) == 264 and [r['id'] for r in rows] == list(range(264))
with (here/'INPUT.txt').open('w') as out:
    out.write(f'{len(rows)}\n')
    for r in rows:
        m = r['matrix']
        assert all(sum(x) == 4 for x in m)
        assert all(sum(m[i][j] for i in range(5)) == 4 for j in range(5))
        out.write(' '.join(map(str,[r['id'],r['key'],r['jointcount']]+sum(m,[])))+'\n')
print('read frozen domain: 264 matrices')
