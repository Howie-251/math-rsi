"""Seven unit six-degree locks, large traces at most three: complete local packing catalogue."""
from pathlib import Path
from itertools import permutations
import sys,json,time
sys.dont_write_bytecode=True
ROOT=Path(__file__).resolve().parents[3];sys.path[:0]=[str(ROOT/'computations'),str(Path(__file__).parent)]
from enumerate_pair_partitions import enumerate_partitions,exact_types
from average_actual_low import average,rawrows
from multilock import json_value
start=time.perf_counter();ps=enumerate_partitions(7,3);orbit={};gs=[];perms=list(permutations(range(1,8)))
for part in ps:
 tri=tuple(sorted(b for b in part if len(b)==3))
 if tri in orbit:continue
 gid=len(gs);ns=exact_types(part,7,degree=6,edges=34)['counts_by_mask'];gs.append(dict(group=gid,triples=tri,counts=ns))
 for p in perms:orbit[tuple(sorted(tuple(sorted(p[i-1] for i in b)) for b in tri))]=gid
print('raw',len(ps),'orbits',len(gs),'sec',time.perf_counter()-start,flush=True)
Path(__file__).with_name('SEVEN_LOW_CATALOGUE.json').write_text(json.dumps(json_value(dict(raw=len(ps),groups=gs)),indent=2)+'\n')
for pos in (tuple(range(9,16)),tuple(range(10,17)),(10,11,12,13,14,23,24)):
 rs=rawrows(24,7,pos)
 for g in gs:
  if g.get('best') and g['best']['bound']<1:continue
  z=average(g['counts'],24,7,pos,rs)
  if 'best' not in g or z['bound']<g['best']['bound']:g['best']=z
  print(g['group'],len(g['triples']),pos,z['bound'],'sec',time.perf_counter()-start,flush=True)
  Path(__file__).with_name('SEVEN_LOW_AVERAGE.json').write_text(json.dumps(json_value(dict(scope=__doc__,elapsed=time.perf_counter()-start,raw=len(ps),groups=gs)),indent=2)+'\n')
