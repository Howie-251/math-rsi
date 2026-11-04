"""Exact current core-cover planning after the proved a1b4 row."""
import collections,hashlib,json
from pathlib import Path
ROOT=Path(__file__).resolve().parent
def main():
 source=ROOT/'eight_t15_core_map.json';data=json.loads(source.read_text())
 remaining=[]
 for row in data['targets']:
  v=row['target'];Z=row['Z'];W=row['W']
  solved=any(sum((z>>i&1)==(v>>i&1) for z in Z)==1 and all((w>>i&1)==(v>>i&1) for w in W) for i in range(6))
  if not solved:remaining.append(row)
 assert len(remaining)==41408
 patterns={tuple(r['core_choices']) for r in remaining}
 forced={p[0] for p in patterns if len(p)==1}
 assert forced=={0,1,2,4,5,8,10,13,14,15,19,23,24,27}
 residual={p for p in patterns if not set(p)&forced}
 groups=[{6,7,9},{18,21,25,26},{30,34,41,44,46},{31,43},{32,42},{35,45}]
 assert all(not a&b for i,a in enumerate(groups) for b in groups[i+1:])
 assert all(not g&forced for g in groups)
 assert all(sum(set(p)<=g for g in groups)==1 for p in residual)
 assert all(any(set(p)<=g for p in residual) for g in groups)
 selected=forced|{7,26,44,31,32,35}
 assert len(selected)==20 and all(set(p)&selected for p in patterns)
 result={'status':'PASS','scope':'Minimum whole-orbit core cover within current a2b1 scheme, not P6 proof necessity',
 'source_sha256':hashlib.sha256(source.read_bytes()).hexdigest(),'remaining_with_a2b1':41408,'remaining_without_a2b1':50,
 'used_orbits':len(set().union(*(set(p) for p in patterns))),'choice_patterns':len(patterns),
 'forced_cores':sorted(forced),'disjoint_groups':[sorted(g) for g in groups],'remaining_constraints':[list(p) for p in sorted(residual)],
 'minimum_core_cover_size':20,'selected':sorted(selected),'by_target':dict(collections.Counter(r['target'] for r in remaining)),
 'new_T15_cores_proved':0,'full_eight_hole_proved':False,'full_p6_proved':False}
 (ROOT/'after_a1b4_core_cover.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
 print(json.dumps(result))
if __name__=='__main__':main()
