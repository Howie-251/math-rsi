"""Import only the earlier independently checked matrix/J domain."""
import json
from pathlib import Path
here=Path(__file__).resolve().parent
source=here.parents[2]/'global_reassessment_20261020/three_low_extension/partition_joint/REPRESENTATIVES.json'
a=json.loads(source.read_text())
assert len(a)==264 and [x['id'] for x in a]==list(range(264))
with (here/'INPUT_LOCAL.txt').open('w') as f:
 f.write('264\n')
 for x in a:
  M=x['matrix'];assert all(sum(row)==4 for row in M)
  assert all(sum(M[i][j] for i in range(5))==4 for j in range(5))
  f.write(' '.join(map(str,[x['id'],x['jointcount']]+sum(M,[])))+'\n')
print('frozen 264 matrices imported; producer marked counts not read')
