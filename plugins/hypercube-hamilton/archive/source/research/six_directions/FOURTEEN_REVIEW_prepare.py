import json,hashlib,pathlib,itertools
P=pathlib.Path(__file__).resolve().parent
read=lambda n:json.loads((P/n).read_text(encoding='utf-8'))
sha=lambda n:hashlib.sha256((P/n).read_bytes()).hexdigest()
for stage in ('REUSE','CACHED'):
 m=read('FOURTEEN_'+stage+'_MANIFEST.json')
 for k in ('input_hashes','output_hashes'):
  for n,h in m[k].items():assert sha(n)==h,(n,sha(n),h)
 print(stage,'all manifest hashes match')
cat=read('FOURTEEN_REUSE_catalog.json')
for n,h in cat['gate_hashes'].items():assert sha(n)==h and read(n)['verdict']=='PASS'
rows=[]
for fam,name,path in [(10,'Q5_T37_INDEPENDENT_REVIEW.json',('accepted_marked_inputs',)),(11,'TWELVE_NEW_TYPES_LOCAL_REVIEW.json',('accepted_marked_inputs',)),(12,'TWELVE_EXTRA_TYPES_REVIEW.json',('details','accepted_marked_local_rows')),(21,'TWELVE_NEW_FORCED_REVIEW.json',('details','accepted_marked_statements')),(22,'TWELVE_EXTRA_FORCED_REVIEW.json',('details','accepted_marked_local_rows')),(23,'TWELVE_STAR_B_REVIEW.json',('accepted_marked_inputs',))]:
 j=read(name)
 for key in path:j=j[key]
 for g in j:rows.append(dict(family=fam,source_gate=name,local_id=g['index'],minority=g['minority'],majority=g['majority'],omitted=g['omitted'],forced_pair=g.get('forced_pair',[]) if fam>=20 else []))
forced={5:[1,2,4,7,11,28,31],6:[1,2,4,11,13,22,31],9:[1,2,4,7,11,21,31],11:[1,2,4,11,19,25,26],12:[1,2,4,7,11,13,31],13:[1,2,4,11,13,14,31],17:[1,2,4,7,11,13,14]}
for i,J in forced.items():rows.append(dict(family=20,source_gate='Q5_T17_RANK_BATCH_REVIEW.json',local_id=i,minority=[0],majority=J,omitted=[1,2,4],forced_pair=[8,16]))
assert sorted(rows,key=lambda g:(g['family'],g['local_id']))==sorted(cat['explicit_local_rows'],key=lambda g:(g['family'],g['local_id']))
maps=[[sum(((x>>d)&1)<<p[d] for d in range(5)) for x in range(32)] for p in itertools.permutations(range(5))]
mask=lambda xs:sum(1<<x for x in xs)
# Do not depend on producer collision priority: retain every permitted (family,id,R).
expanded=set()
for g in rows:
 for a in (g['minority'] or g['omitted']):
  for tr in maps:
   masks=[mask(tr[x^a] for x in g[k]) for k in ('minority','majority','omitted','forced_pair')]
   expanded.add((*masks,g['family'],g['local_id']))
actual={tuple(map(int,line.split())) for line in (P/'FOURTEEN_REUSE_registry.txt').read_text().splitlines()}
assert actual<=expanded
assert {r[:3] for r in expanded}=={r[:3] for r in actual}
(P/'FOURTEEN_REUSE_REVIEW_registry.txt').write_text(''.join(' '.join(map(str,r))+'\n' for r in sorted(expanded)))
sel=read('FOURTEEN_CACHED_greedy_registry.json')['rows']; cand=read('FOURTEEN_CACHED_catalog.json')['rows']
print('selected/candidate',len(sel),len(cand));print('candidate sample',cand[0])
with (P/'FOURTEEN_CACHED_REVIEW_geometries.txt').open('w') as f:
 for g in sel:
  H=g['minority']+g['majority'];U=g['omitted'];N=32-len(H);R=2**(N//2-1);E=(N+2*(len(H)-len(U)))//2
  f.write(' '.join(map(str,[g['prefix'],N,R,E,len(H),len(U),*H,*U]))+'\n')
# candidate registry expanded independently from exact explicit marked rows.
for label,rr in [('all',cand),('selected',sel)]:
 exp=set()
 for g in rr:
  for a in g['minority'] or g['omitted']:
   for tr in maps:exp.add((*[mask(tr[x^a] for x in g[k]) for k in ('minority','majority','omitted')],g['family'],g['local_id']))
 (P/f'FOURTEEN_CACHED_REVIEW_{label}_registry.txt').write_text(''.join(' '.join(map(str,r))+'\n' for r in sorted(exp)))
print('all registry rebuild pass')
