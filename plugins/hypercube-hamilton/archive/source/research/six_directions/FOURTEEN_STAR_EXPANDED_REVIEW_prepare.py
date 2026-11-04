import hashlib,itertools,json,pathlib
R=pathlib.Path(__file__).resolve().parent
def rd(n):return json.loads((R/n).read_text(encoding='utf-8-sig'))
def sha(n):
 h=hashlib.sha256()
 with (R/n).open('rb') as f:
  for b in iter(lambda:f.read(1<<20),b''):h.update(b)
 return h.hexdigest()
expected={'FOURTEEN_STAR_EXPANDED_PROOF.md':'2c510152040c17bf84217228703e76be0c85d47f4284256527f632bd13ba36b4','FOURTEEN_STAR_EXPANDED_MANIFEST.json':'24eedd54aa1e9b07b83bd9dcf7642474b2de81ed85a8546083f0ed18acd55085'}
for n,h in expected.items():assert sha(n)==h
m=rd('FOURTEEN_STAR_EXPANDED_MANIFEST.json')
for n,v in m['files'].items():assert sha(n)==v['sha256'] and (R/n).stat().st_size==v['bytes'],n
gates={};checked={}
for name in m['files']:
 if not name.endswith('_REVIEW.json'):continue
 d=rd(name);assert d['verdict']=='PASS';gates[name]=sha(name)
 for field in ['audited_input_hashes','imported_dependency_hashes','checker_artifact_hashes']:
  for n,h in d.get(field,{}).items():
   if n not in checked:checked[n]=sha(n)
   assert checked[n]==h.removeprefix('sha256:'),(name,n)
prior=rd('FOURTEEN_MAXIMAL_A_REVIEW.json');assert prior['details']['remaining_covered_target_geometries']==2527 and prior['details']['fourteen_hole_free_targets_proved']
old=rd('FOURTEEN_RESIDUAL_STRUCTURE_MANIFEST.json')
for group in ['input_hashes','output_hashes']:
 for n,h in old[group].items():assert sha(n)==h.removeprefix('sha256:')
local=rd('FOURTEEN_STAR_EXPANDED_REVIEW_local.json');assert local['status']=='PASS' and local['local_inputs']==10
rows=rd('FOURTEEN_STAR_B_REDUCED_summary.json')['reports'];assert {r['index'] for r in rows}=={0,1,7,8,17,24,25,26,30,35}
perms=list(itertools.permutations(range(5)));maps=[tuple(sum(((x>>p[d])&1)<<d for d in range(5)) for x in range(32)) for p in perms]
def mask(xs):return sum(1<<x for x in set(xs))
keys=set()
for row in rows:
 g=row['geometry'];assert g['minority']==[0] and len(g['majority'])==9 and len(g['omitted'])==4 and len(g['forced_pair'])==2
 for tr in maps:keys.add((mask(tr[x] for x in g['majority']),mask(tr[x] for x in g['omitted']),mask(tr[x] for x in g['forced_pair']),row['index']))
(R/'FOURTEEN_STAR_EXPANDED_REVIEW_B_registry.txt').write_text(''.join(' '.join(map(str,r))+'\n' for r in sorted(keys)),encoding='utf-8')
J={1,2,4,8,14,16};W=J|{32};Ts={79:{7,11,13,19,21,31},87:{7,11,13,22,26,31}}
def full(x,tr):return tr[x&31]|(x&32)
orbits={}
for idx,T in Ts.items():
 assert set(map(int,(R/f'FOURTEEN_STAR_B_EXPAND_A_T_{idx}.txt').read_text().split()))==T
 Z={x^32 for x in T};assert 31 in T and len(T)==6 and 14 not in T
 orbits[idx]={tuple(sorted(full(x,tr) for x in Z))+tuple(sorted(full(x,tr) for x in W)) for tr in maps};assert len(orbits[idx])==60
oldZ={39,43,45,51,60,63};oldorbit={tuple(sorted(full(x,tr) for x in oldZ))+tuple(sorted(full(x,tr) for x in W)) for tr in maps}
assert not orbits[79]&orbits[87] and not (orbits[79]|orbits[87])&oldorbit
transport=rd('FOURTEEN_STAR_EXPANDED_transport.json')['transports'];byindex={};seen=set();reports=[];orbitcounts={79:0,87:0}
for item in transport:
 v,i,idx,pi=[item[k] for k in ['v','source_index','orbit','permutation']];assert v==31 and idx in Ts and pi in range(120) and (v,i) not in byindex
 tr=maps[pi];Z={x^32 for x in Ts[idx]};rec=tuple(sorted(full(x,tr) for x in Z))+tuple(sorted(full(x,tr) for x in W));assert rec not in seen
 seen.add(rec);byindex[v,i]=rec;orbitcounts[idx]+=1
assert seen==orbits[79]|orbits[87] and orbitcounts=={79:60,87:60}
for v in (1,7,31):
 name=f'FOURTEEN_RESIDUAL_STRUCTURE_maxA_remaining_v{v}_covered.bin';assert sha(name)==old['output_hashes'][name]
 raw=(R/name).read_bytes();assert len(raw)%13==0;records=[tuple(raw[j:j+13]) for j in range(0,len(raw),13)];assert len(records)==len(set(records));positive=0;remain=bytearray()
 for i,rec in enumerate(records):
  z,w=rec[:6],rec[6:];assert list(z)==sorted(set(z)) and list(w)==sorted(set(w)) and len(z)==6 and len(w)==7 and v not in w
  assert all(x and x<64 and x.bit_count()%2==0 for x in z) and all(x<64 and x.bit_count()%2 for x in w)
  assert all((x^y).bit_count()!=1 for x in z for y in w)
  hit=v==31 and rec in seen
  assert hit==((v,i) in byindex)
  if hit:assert byindex[v,i]==rec;positive+=1
  else:remain.extend(bytes(rec))
 n=f'FOURTEEN_STAR_EXPANDED_remaining_v{v}_covered.bin';assert bytes(remain)==(R/n).read_bytes()
 reports.append({'v':v,'input':len(records),'new_positive':positive,'remaining':len(remain)//13,'remaining_sha256':sha(n)})
assert [r['remaining'] for r in reports]==[240,702,1465] and sum(r['new_positive'] for r in reports)==120
out={'status':'PASS','manifest_files_verified':len(m['files']),'formal_gate_hashes':gates,'direct_formal_source_bindings_verified':len(checked),'B_common_map_keys':len(keys),'new_orbit_sizes':orbitcounts,'new_orbits_disjoint_from_each_other_and_old85':True,'exact120_transport_and_source_index_checks':True,'all_three_complements_byte_exact':True,'reports':reports,'fourteen_hole_free_targets_proved':True,'remaining_free_target_geometries':0,'full_fourteen_hole_proved':False,'full_P6_proved':False}
(R/'FOURTEEN_STAR_EXPANDED_REVIEW_prepare.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8');print(json.dumps(out,indent=2))
