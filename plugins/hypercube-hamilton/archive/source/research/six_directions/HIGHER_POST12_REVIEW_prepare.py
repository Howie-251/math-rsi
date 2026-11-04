import pathlib,json,hashlib,itertools
R=pathlib.Path(__file__).resolve().parent
def read(n):return json.loads((R/n).read_text(encoding='utf-8-sig'))
def sha(n):
 h=hashlib.sha256()
 with (R/n).open('rb') as f:
  for b in iter(lambda:f.read(1<<20),b''):h.update(b)
 return h.hexdigest()
manifests=['HIGHER_POST12_REUSE_MANIFEST.json','HIGHER_POST12_T39_MANIFEST.json'];bound={}
for name in manifests:
 m=read(name)
 for n,v in m['files'].items():assert sha(n)==v['sha256'] and (R/n).stat().st_size==v['bytes'];bound[n]=v['sha256']
gates=['HIGHER_Q5_FULL_REVIEW.json','FOURTEEN_REUSE_REVIEW.json','FOURTEEN_CACHED_REVIEW.json','HIGHER_FORCED_CHERRY_REVIEW.json','Q5_HIGHER_HOLE_REDUCTION_REVIEW.json','FOURTEEN_FORCED_REVIEW.json']
checked={}
for name in gates:
 d=read(name);assert d['verdict']=='PASS'
 for field in ['audited_input_hashes','imported_dependency_hashes','checker_artifact_hashes']:
  for n,h in d.get(field,{}).items():
   if n not in checked:checked[n]=sha(n)
   assert checked[n]==h.removeprefix('sha256:'),(name,n)
# Reconstruct explicit local input union from final accepted theorem statements.
rows=[]
for fam,name,path in [(10,'Q5_T37_INDEPENDENT_REVIEW.json',('accepted_marked_inputs',)),(11,'TWELVE_NEW_TYPES_LOCAL_REVIEW.json',('accepted_marked_inputs',)),(12,'TWELVE_EXTRA_TYPES_REVIEW.json',('details','accepted_marked_local_rows')),(21,'TWELVE_NEW_FORCED_REVIEW.json',('details','accepted_marked_statements')),(22,'TWELVE_EXTRA_FORCED_REVIEW.json',('details','accepted_marked_local_rows')),(23,'TWELVE_STAR_B_REVIEW.json',('accepted_marked_inputs',))]:
 d=read(name);assert d['verdict']=='PASS'
 for key in path:d=d[key]
 for g in d:rows.append(dict(family=fam,local_id=g['index'],minority=g['minority'],majority=g['majority'],omitted=g['omitted'],forced_pair=g.get('forced_pair',[]) if fam>=20 else []))
old=read('Q5_T17_RANK_BATCH_REVIEW.json');assert sha('Q5_T17_RANK_BATCH_PROOF.md')==old['audited_input_hashes']['Q5_T17_RANK_BATCH_PROOF.md']
for line in (R/'Q5_T17_RANK_BATCH_PROOF.md').read_text().splitlines():
 t=[x.strip() for x in line.strip('|').split('|')]
 if line.startswith('|') and t[0].isdigit() and 'absent' in t[3]:rows.append(dict(family=20,local_id=int(t[0]),minority=[0],majority=list(map(int,t[1].replace('$','').split(','))),omitted=list(map(int,t[2].replace('$','').split(','))),forced_pair=[8,16]))
assert len(rows)==236
for g in read('FOURTEEN_CACHED_REVIEW.json')['accepted_marked_inputs']:rows.append(dict(family=g['family'],local_id=g['index'],minority=g['minority'],majority=g['majority'],omitted=g['omitted'],forced_pair=[]))
assert len(rows)==256
maps=[tuple(sum(((x>>d)&1)<<p[d] for d in range(5)) for x in range(32)) for p in itertools.permutations(range(5))]
def mask(xs):return sum(1<<x for x in set(xs))
expanded=set()
for g in rows:
 for a in g['minority'] or g['omitted']:
  for tr in maps:expanded.add((*[mask(tr[x^a] for x in g[k]) for k in ['minority','majority','omitted','forced_pair']],g['family'],g['local_id']))
producer={tuple(map(int,line.split())) for line in (R/'HIGHER_POST12_REUSE_registry.txt').read_text().splitlines()}
assert producer<=expanded and {r[:3] for r in producer}=={r[:3] for r in expanded}
assert len({r[:3] for r in expanded})==47015
(R/'HIGHER_POST12_REVIEW_registry.txt').write_text(''.join(' '.join(map(str,r))+'\n' for r in sorted(expanded)),encoding='utf-8')
# The legacy ordinary rows are source-bound accepted tables, not a new cache.
legacy=read('HIGHER_Q5_FULL_REUSE_REVIEW.json')['checker_artifact_hashes']
for t in ['T26','T15','T17','T63']:
 n=f'HIGHER_Q5_FULL_REUSE_REVIEW_{t}.txt';assert sha(n)==legacy[n]
out={'status':'PASS','frozen_files_verified':len(bound),'formal_gate_sources_rehashed':len(checked),'formal_gate_hashes':{n:sha(n) for n in gates},'canonical_explicit_local_rows':len(rows),'normalized_marked_keys':47015,'producer_lookup_keys_equal_and_all_values_accepted':True,'legacy_ordinary_tables_source_bound':True,'local54_formal_PASS_bound':True,'full_fourteen_hole_proved':False,'full_sixteen_hole_proved':False,'full_eighteen_hole_proved':False,'full_P6_proved':False}
(R/'HIGHER_POST12_REVIEW_prepare.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8');print(json.dumps(out,indent=2))
