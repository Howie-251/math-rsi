#!/usr/bin/env python3
"""Five fixed inputs, independently reconstructed; no A1 or degree-six role."""
from pathlib import Path
from fractions import Fraction as F
import sys,json,time
P=Path(__file__).resolve().parent;ROOT=P.parents[4]
sys.dont_write_bytecode=True;sys.path.insert(0,str(ROOT/'computations'))
from independent_structure_bounds import independent_rows
start=time.process_time()
source=ROOT/'context/propertyb35-paper/round01/middle/high_edge_intersection_repair_20261020/RESULT.json'
saved=json.loads(source.read_text())['extra_pair_gates']
assert len(saved)==5 and {r['codegree'] for r in saved}==set(range(5,10))
rows=[]
for c in range(5,10):
 counts={0:17+c,1:9-c,2:9-c,3:c}
 types=[frozenset(i+1 for i in range(2) if mask>>i&1) for mask,n in counts.items() for _ in range(n)]
 assert len(types)==35 and all(sum(i in T for T in types)==9 for i in (1,2))
 actual=independent_rows(21,(10,21),types)
 value=sum((min(r['A'],r['B'],r['C']) for r in actual),F())
 old=next(r for r in saved if r['codegree']==c)
 assert old['degrees']==[9,9] and old['positions']==[10,21]
 assert old['quota_losses']==['0','0']
 assert counts=={int(k):v for k,v in old['counts'].items()}
 assert value==F(old['bound'])<1
 rows.append(dict(degrees=[9,9],codegree=c,counts=counts,positions=[10,21],bound=str(value),deduction='zero; no quotas used',original_edge_stubs=35,ordered_distinct_pairs=1190,position_rows=[{k:str(v) if isinstance(v,F) else v for k,v in r.items()} for r in actual]))
out=dict(status='PASS',scope='generic fixed two degree-nine lock replay only; no A1 assumptions or free-point degree data',input_codegrees=list(range(5,10)),source=str(source.relative_to(ROOT)),cases=rows,max_bound=str(max(F(r['bound']) for r in rows)),position_rows=105,ordered_index_pairs=5950,cpu_seconds=time.process_time()-start)
P.joinpath('PAIR99_SOURCE_CHECK.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({k:v for k,v in out.items() if k!='cases'}))
