import pathlib,json,hashlib,struct,itertools,collections
R=pathlib.Path(__file__).resolve().parent
def load(n):return json.loads((R/n).read_text(encoding='utf-8-sig'))
def sha(n):return hashlib.sha256((R/n).read_bytes()).hexdigest()
def mask(xs):return sum(1<<x for x in set(xs))
def swap(x,i,j):return x^((1<<i)|(1<<j)) if ((x>>i)^(x>>j))&1 else x
def orbit(seed,gens):
 seen={seed};todo=[seed]
 while todo:
  t=todo.pop()
  for i,j in gens:
   u=tuple(tuple(sorted(swap(x,i,j) for x in a)) for a in t)
   if u not in seen:seen.add(u);todo.append(u)
 return seen
p=load('TWELVE_EXTRA_FORCED_REVIEW_prepare.json');lookup={};gens5=[(i,i+1) for i in range(4)]
for g in p['local_marked_rows']:
 for M,J,O,OB in orbit(tuple(tuple(g[k]) for k in ('minority','majority','omitted','forced_pair')),gens5):
  k=(mask(M),mask(J),mask(O));val=(g['index'],mask(OB));assert k not in lookup or lookup[k]==val;lookup[k]=val
def project(x,d):return sum(((x>>j)&1)<<i for i,j in enumerate(j for j in range(6) if j!=d))
raw=(R/'TWELVE_EXTRA_FORCED_safe_witnesses.bin').read_bytes();assert len(raw)==1046*32;chosen={v:{} for v in (1,7,31)}
for v,i,row,d,S,M,J,O,OB in struct.iter_unpack('<BIHBQIIII',raw):
 assert v in chosen and i not in chosen[v];chosen[v][i]=(row,d,S,M,J,O,OB)
reports=[];used=collections.Counter();projections=0;before=[];after=[]
for v in (1,7,31):
 raw=(R/f'TWELVE_EXTRA_TYPES_positive_remaining_v{v}.bin').read_bytes();assert len(raw)%11==0;recs=[raw[i:i+11] for i in range(0,len(raw),11)];assert len(set(recs))==len(recs)
 rem=bytearray();hit=0
 for index,rec in enumerate(recs):
  Z,W=rec[:5],rec[5:];H={0,*rec};assert len(H)==12 and list(Z)==sorted(set(Z)) and list(W)==sorted(set(W)) and all(x and x<64 and x.bit_count()%2==0 for x in Z) and all(x<64 and x.bit_count()%2 for x in W) and v not in W
  assert all((x^y).bit_count()!=1 for x in Z for y in W)
  candidates=set()
  for d in range(6):
   A=lambda x:((x^v)&(1<<d))==0
   za=[x for x in Z if A(x)];wa=[x for x in W if A(x)];shape=(len(za),len(wa))
   if shape==(4,2):pool=za;minor=[x for x in Z if not A(x)];major=[x for x in W if not A(x)]
   elif shape==(1,5):pool=[x for x in wa if x!=1<<d];minor=[x for x in W if not A(x)];major=[x for x in Z if not A(x)]
   else:continue
   for S in itertools.combinations(pool,3):
    projections+=1;Y=[x^(1<<d) for x in S];assert not set(Y)&H
    mi=[project(x,d) for x in minor];jo=[project(x,d) for x in major+Y];om=[project(x,d) for x in Y];anchor=mi[0]
    key=(mask(x^anchor for x in mi),mask(x^anchor for x in jo),mask(x^anchor for x in om));found=lookup.get(key)
    if found is None:continue
    row,normOB=found;actualOB=mask(x^anchor for x in range(32) if normOB>>x&1)
    assert actualOB.bit_count()==2 and not actualOB&(mask(mi)|mask(jo))
    if v>>d&1 and actualOB&1:continue
    candidates.add((row,d,mask(S),mask(mi),mask(jo),mask(om),actualOB))
  before.append((v,rec,bool(candidates)))
  if candidates:
   assert index in chosen[v] and chosen[v][index] in candidates;used[chosen[v][index][0]]+=1;hit+=1
  else:assert index not in chosen[v];rem.extend(rec);after.append((v,rec,False))
 assert set(chosen[v])<=set(range(len(recs)))
 assert bytes(rem)==(R/f'TWELVE_EXTRA_FORCED_safe_remaining_v{v}.bin').read_bytes()
 reports.append({'v':v,'input':len(recs),'safe':hit,'remaining':len(rem)//11,'remaining_sha256':hashlib.sha256(rem).hexdigest()})
assert [(r['input'],r['safe'],r['remaining']) for r in reports]==[(0,0,0),(504,504,0),(777,542,235)]
assert sha('TWELVE_EXTRA_FORCED_safe_remaining_v31.bin')=='a84bde6025aac56f976bcf1a1c3367251b4ce9723c152e509102132cadd73124'
def profile(records):
 cache={};groups=collections.Counter();degree=collections.Counter();wn0=collections.Counter();single=0
 for v,rec,covered in records:
  Z,W=tuple(rec[:5]),tuple(rec[5:]);H={0,*rec};available={v^(1<<d) for d in range(6)}-H;degree[len(available)]+=1
  if len(available)==1:single+=1;assert covered # every one-candidate source record is safe
  if set(W)=={1<<d for d in range(6)}:wn0[v]+=1
  seed=(Z,W);key=(v,seed)
  if key not in cache:
   gens=[]
   for bit in (0,1):
    positions=[i for i in range(6) if v>>i&1==bit];gens.extend(zip(positions,positions[1:]))
   images=orbit(seed,gens);canonical=min(images)
   for image in images:cache[(v,image)]=(v,*canonical)
  groups[cache[key]]+=1
 return {'records':len(records),'coordinate_orbits':len(groups),'target_available_original_neighbor_histogram':dict(sorted(degree.items())),'W_equals_N0_by_target':dict(sorted(wn0.items())),'one_neighbor_records':single,'orbits':[{'v':v,'Z':Z,'W':W,'records':n} for (v,Z,W),n in sorted(groups.items())]}
bp=profile(before);ap=profile(after);assert bp['coordinate_orbits']==41 and ap['coordinate_orbits']==6
assert bp['target_available_original_neighbor_histogram']=={1:984,4:50,5:208,6:39};assert ap['target_available_original_neighbor_histogram']=={5:205,6:30};assert ap['W_equals_N0_by_target']=={31:235}
prod=load('TWELVE_EXTRA_FORCED_geometry_profile.json')
for ours,key in [(bp,'before_safe_forced'),(ap,'after_safe_forced')]:
 claimed=prod[key];assert ours['records']==claimed['input_count'] and ours['coordinate_orbits']==claimed['marked_coordinate_orbits']
 assert {str(k):v for k,v in ours['target_available_original_neighbor_histogram'].items()}==claimed['target_M_degree_histogram']
 assert {(r['v'],tuple(r['Z']),tuple(r['W']),r['records']) for r in ours['orbits']}=={(r['v'],tuple(r['canonical_Z']),tuple(r['canonical_W']),r['records']) for r in claimed['orbits']}
m=load('TWELVE_EXTRA_FORCED_MANIFEST.json')
for n,h in m['hashes'].items():assert sha(n)==h,n
out={'status':'PASS','input':1281,'safe':1046,'remaining_covered_target_geometries':235,'source_projections_evaluated':projections,'marked_lookup_entries':len(lookup),'all_1046_selected_witnesses_replayed':True,'full_six_cut_all_legal_source_predicate_equals_selected_membership':True,'all_three_remaining_files_exact_bytes':True,'selected_local_indices':sorted(used),'unused_local_index113':113 not in used,'reports':reports,'supplementary_before_geometry':bp,'supplementary_remaining_geometry':ap,'remaining_matching_realizability_claimed':False,'full_twelve_hole_proved':False,'full_P6_proved':False}
(R/'TWELVE_EXTRA_FORCED_REVIEW_application.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({k:v for k,v in out.items() if not k.startswith('supplementary')},indent=2))
