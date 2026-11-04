import hashlib,itertools,json,pathlib,struct
R=pathlib.Path(__file__).resolve().parent
def rd(n):return json.loads((R/n).read_text(encoding='utf-8-sig'))
def sha(n):return hashlib.sha256((R/n).read_bytes()).hexdigest()
expected={'SIXTEEN_STAR_PROOF.md':'18ec2b46bf4a7206abe9dae12e20eba0ba742dd46f38f1c1485e4c55cc7ecbd6','SIXTEEN_STAR_APPLICATION.md':'b4643bec2fd51ff109c447c1944fe59d28d91f67eb6ecd79f42ed4ae39eb6e23','SIXTEEN_STAR_MANIFEST.json':'88935189ca9ed9c75c144a1c5df194e72c540c82495a7aadc8ac5e934aba8826'}
for n,h in expected.items():assert sha(n)==h
m=rd('SIXTEEN_STAR_MANIFEST.json')
for n,h in m['input_hashes'].items():assert sha(n)==h,n
gates={};checked={}
for name in ['SIXTEEN_LOCAL_REVIEW.json','HIGHER_FORCED_CHERRY_REVIEW.json']:
 d=rd(name);assert d['verdict']=='PASS';gates[name]=sha(name)
 for field in ['audited_input_hashes','imported_dependency_hashes','checker_artifact_hashes']:
  for n,h in d.get(field,{}).items():
   if n not in checked:checked[n]=sha(n)
   assert checked[n]==h.removeprefix('sha256:'),(name,n)
source=rd('SIXTEEN_LOCAL_REVIEW.json');assert source['details']['remaining_covered_target_geometries']==148 and not source['details']['predecessor_requirement_discharged']
assert rd('SIXTEEN_STAR_REVIEW_local.json')['status']=='PASS'
rows=rd('SIXTEEN_STAR_B_candidate_classes.json')['classes'];assert {r['index'] for r in rows}=={5,6,7}
perms=list(itertools.permutations(range(5)));maps=[tuple(sum(((x>>p[d])&1)<<d for d in range(5)) for x in range(32)) for p in perms]
def mask(xs):return sum(1<<x for x in set(xs))
keys=set()
for row in rows:
 g=row['geometry'];assert g['minority']==[0]
 for tr in maps:keys.add((mask(tr[x] for x in g['majority']),mask(tr[x] for x in g['omitted']),mask(tr[x] for x in row['forced_pairs'][0]),row['index']))
(R/'SIXTEEN_STAR_REVIEW_B_registry.txt').write_text(''.join(' '.join(map(str,r))+'\n' for r in sorted(keys)),encoding='utf-8')
T={7,11,13,19,21,25,31};J={1,2,4,8,14,16,22};units={1,2,4,8,16};canonical={r['index']:r for r in rows};options=[]
for op in rd('SIXTEEN_STAR_checked_options.json')['options']:
 q,t,w,b,c,pi,idx,bpi=[op[k] for k in ['q','t','w','b','case','permutation_index','Bclass','B_permutation_index']]
 assert q and q<32 and q.bit_count()%2==0 and t in T-{31} and (q^t).bit_count()==1 and w in units and b in units-{w}
 assert c in (0,3) and pi in range(120) and bpi in range(120) and idx in canonical
 seed={0:(3,4,7),3:(15,1,7)}[c];assert tuple(maps[pi][x] for x in seed)==(q,b,t)
 S=J-{w,b};M={0};major=(T-{t})|S;pair={w,b};g=canonical[idx]['geometry'];tr=maps[bpi]
 # The supplied B permutation is actual-to-canonical, as stated in the
 # proof; the independent full-image registry is orientation independent.
 assert {tr[x] for x in M}==set(g['minority']) and {tr[x] for x in major}==set(g['majority']) and {tr[x] for x in S}==set(g['omitted']) and {tr[x] for x in pair}==set(canonical[idx]['forced_pairs'][0])
 assert not pair&({0}|major) and {14,22}<=S
 options.append((q,t,w,b,c,pi,idx))
assert len(set(options))==len(options)==160
(R/'SIXTEEN_STAR_REVIEW_options.txt').write_text(''.join(' '.join(map(str,r))+'\n' for r in sorted(options)),encoding='utf-8')
Z={x^32 for x in T};W=J|{32};rep=tuple(sorted(Z))+tuple(sorted(W))
def full(x,tr):return tr[x&31]|(x&32)
orbit={tuple(sorted(full(x,tr) for x in Z))+tuple(sorted(full(x,tr) for x in W)) for tr in maps};assert len(orbit)==30
raw=(R/'SIXTEEN_STAR_actual_witnesses.bin').read_bytes();assert len(raw)==30*6;witnesses={}
for v,i,pi in struct.iter_unpack('<BIB',raw):assert v==31 and pi in range(120) and (v,i) not in witnesses;witnesses[v,i]=pi
reports=[];seen=set()
for v in (1,7,31):
 n=f'SIXTEEN_LOCAL_remaining_v{v}_covered.bin';assert sha(n)==source['audited_input_hashes'][n]
 raw=(R/n).read_bytes();assert len(raw)%15==0;records=[tuple(raw[j:j+15]) for j in range(0,len(raw),15)];assert len(records)==len(set(records));remain=bytearray();yes=0
 for i,rec in enumerate(records):
  z,w=rec[:7],rec[7:];assert list(z)==sorted(set(z)) and list(w)==sorted(set(w)) and len(z)==7 and len(w)==8 and v not in w
  assert all(x and x<64 and x.bit_count()%2==0 for x in z) and all(x<64 and x.bit_count()%2 for x in w) and all((x^y).bit_count()!=1 for x in z for y in w)
  hit=v==31 and rec in orbit;assert hit==((v,i) in witnesses)
  if hit:
   tr=maps[witnesses[v,i]];assert tuple(sorted(full(x,tr) for x in z))+tuple(sorted(full(x,tr) for x in w))==rep
   seen.add(rec);yes+=1
  else:remain.extend(bytes(rec))
 out=f'SIXTEEN_STAR_remaining_v{v}_covered.bin';assert bytes(remain)==(R/out).read_bytes()
 reports.append({'v':v,'input':len(records),'positive':yes,'remaining':len(remain)//15,'remaining_sha256':sha(out)})
assert seen==orbit and [r['remaining'] for r in reports]==[0,18,100]
out={'status':'PASS','manifest_hashes_verified':len(m['input_hashes']),'formal_gate_hashes':gates,'direct_formal_source_bindings_verified':len(checked),'B_common_map_registry_keys':len(keys),'all160_formal_options_and_paired_B_maps_verified':True,'actual_orbit_size':30,'all30_actual_to_representative_transports_verified':True,'all_three_remaining_streams_byte_exact':True,'reports':reports,'remaining_covered_target_geometries':118,'remaining_free_target_geometries':0,'complete14_predecessor_condition_retained':True,'full_sixteen_hole_proved':False,'full_P6_proved':False}
(R/'SIXTEEN_STAR_REVIEW_prepare.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8');print(json.dumps(out,indent=2))
