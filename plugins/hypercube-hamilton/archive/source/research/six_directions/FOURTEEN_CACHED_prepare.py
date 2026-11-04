"""Unreviewed cached-positive local candidates on the frozen fourteen residual only."""
from pathlib import Path
from itertools import permutations
import json,hashlib,collections
P=Path(__file__).resolve().parent
read=lambda n:json.loads((P/n).read_text())
sha=lambda n:hashlib.sha256((P/n).read_bytes()).hexdigest()
base=read('FOURTEEN_REUSE_MANIFEST.json');rows=[]
selected_new=set(read('TWELVE_NEW_TYPES_LOCAL_REVIEW.json')['details']['claimed_indices'])
selected_extra=set(read('TWELVE_EXTRA_TYPES_REVIEW.json')['details']['selected_indices'])
for family,file,exclude in [(30,'TWELVE_NEW_TYPES_summary.json',selected_new),(31,'TWELVE_EXTRA_TYPES_summary.json',selected_extra)]:
 for r in read(file)['reports']:
  if not r['full_rank'] or r['index'] in exclude:continue
  g=r['geometry'];N=32-len(g['minority'])-len(g['majority']);assert r['rank']==1<<(N//2-1)
  rows.append({'family':family,'local_id':r['index'],'prefix':r['prefix'],'type':g['type'],
   'minority':g['minority'],'majority':g['majority'],'omitted':g['omitted'],'producer_rank':r['rank'],
   'local_independently_accepted':False,'summary_file':file})
assert collections.Counter(r['family'] for r in rows)=={30:121,31:282}
lookup={};maps=[tuple(sum(((x>>i)&1)<<perm[i] for i in range(5)) for x in range(32)) for perm in permutations(range(5))];mask=lambda xs:sum(1<<x for x in xs)
for row in rows:
 M,J,U=[row[k] for k in ('minority','majority','omitted')]
 for a in M or U:
  for tr in maps:
   key=tuple(mask(tr[x^a] for x in xs) for xs in (M,J,U));value=(row['family'],row['local_id'])
   assert key not in lookup or lookup[key]==value
   lookup[key]=value
(P/'FOURTEEN_CACHED_registry.txt').write_text(''.join(' '.join(map(str,[*key,*value]))+'\n' for key,value in sorted(lookup.items())))
sources={}
for v in (1,7,31):
 for status in ('covered','free'):
  name=f'FOURTEEN_REUSE_remaining_h14_v{v}_{status}.bin';assert sha(name)==base['output_hashes'][name];sources[name]={'sha256':sha(name),'records':(P/name).stat().st_size//13}
out={'status':'UNREVIEWED_CACHED_POSITIVE_CANDIDATES_ONLY','sources':sources,'rows':rows,'normalized_lookup_keys':len(lookup),'candidate_counts':dict(collections.Counter(r['family'] for r in rows)),
 'source_manifest_sha256':sha('FOURTEEN_REUSE_MANIFEST.json'),'input_summary_hashes':{n:sha(n) for n in ['TWELVE_NEW_TYPES_summary.json','TWELVE_EXTRA_TYPES_summary.json']},'registry_sha256':sha('FOURTEEN_CACHED_registry.txt'),
 'local_inputs_accepted':False,'full_twelve_hole_proved':False,'full_fourteen_hole_proved':False,'full_P6_proved':False}
(P/'FOURTEEN_CACHED_catalog.json').write_text(json.dumps(out,indent=2)+'\n');print('cached candidates',len(rows),'normalized keys',len(lookup))
