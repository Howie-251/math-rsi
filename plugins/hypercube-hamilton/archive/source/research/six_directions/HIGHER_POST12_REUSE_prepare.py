"""Conditional producer exploration for h16/h18; never an acceptance gate."""
from pathlib import Path
from itertools import permutations
import json,hashlib
R=Path(__file__).resolve().parent
lookup={}
for line in (R/'FOURTEEN_REUSE_registry.txt').read_text().splitlines():
 vals=list(map(int,line.split()));lookup[tuple(vals[:3])]=tuple(vals[3:])
review=json.loads((R/'FOURTEEN_CACHED_REVIEW.json').read_text());assert review['verdict']=='PASS'
maps=[tuple(sum(((x>>i)&1)<<p[i] for i in range(5)) for x in range(32)) for p in permutations(range(5))]
for g in review['accepted_marked_inputs']:
 M,J,U=[g[k] for k in ('minority','majority','omitted')]
 for anchor in M or U:
  for tr in maps:
   key=tuple(sum(1<<tr[x^anchor] for x in xs) for xs in (M,J,U))
   value=(0,g['family'],g['index'])
   if key in lookup:assert lookup[key][0]==0
   else:lookup[key]=value
(R/'HIGHER_POST12_REUSE_registry.txt').write_text(''.join(' '.join(map(str,[*k,*v]))+'\n' for k,v in sorted(lookup.items())))
base=(R/'FOURTEEN_REUSE_scan.cpp').read_text()
for k,stem in ((8,'SIXTEEN_POST12_REUSE'),(9,'EIGHTEEN_POST12_REUSE')):
 s=base.replace('FOURTEEN_REUSE',stem)
 s=s.replace(stem+'_registry.txt','HIGHER_POST12_REUSE_registry.txt')
 changes={
 'registry.size()==44085':f'registry.size()=={len(lookup)}',
 '\\"holes\\":14':f'\\"holes\\":{2*k}',
 '"h14_v"':f'"h{2*k}_v"',
 'unsigned char rec[13]':f'unsigned char rec[{2*k-1}]',
 'in.read((char*)rec,13)':f'in.read((char*)rec,{2*k-1})',
 'i<13;++i':f'i<{2*k-1};++i',
 'i<6?0:1':f'i<{k-1}?0:1',
 'if(i>=6)':f'if(i>={k-1})',
 'for(int i=0;i<6;++i)':f'for(int i=0;i<{k-1};++i)',
 'for(int i=6;i<13;++i)':f'for(int i={k-1};i<{2*k-1};++i)',
 'out.write((char*)rec,13)':f'out.write((char*)rec,{2*k-1})',
 'source_reduction_conditional_on_full_twelve_hole':f'source_reduction_conditional_on_full_{"fourteen" if k==8 else "sixteen"}_hole',
 'full_fourteen_hole_proved':f'full_{"sixteen" if k==8 else "eighteen"}_hole_proved'
 }
 # Specific second-part record loop before the general bound replacement.
 key='for(int i=6;i<13;++i)';assert key in s;s=s.replace(key,changes.pop(key))
 for a,b in changes.items():
  assert a in s,(stem,a)
  s=s.replace(a,b)
 (R/(stem+'_scan.cpp')).write_text(s)
print(json.dumps({'registry_keys':len(lookup),'status':'CONDITIONAL_PRODUCER_ONLY','full_P6_proved':False}))
