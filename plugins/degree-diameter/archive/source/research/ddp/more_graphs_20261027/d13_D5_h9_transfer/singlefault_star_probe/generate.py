"""Generate the fixed51418candidate from its saved51417source and literalpins."""
from pathlib import Path
import json

HERE=Path(__file__).resolve().parent
ROOT=HERE.parent.parents[3]
params=json.loads((HERE/'literal_params.json').read_text())
source=ROOT/params['source']
target=HERE/'graph_d13_D5_n51418.generated.edges'
with source.open() as old,target.open('w') as new:
    assert tuple(map(int,next(old).split()))==(51417,324451)
    new.write('51418 324461\n')
    for line in old:new.write(line)
    for p in params['full_neighbor_set']:new.write(f'{p} 51417\n')
print(target)
