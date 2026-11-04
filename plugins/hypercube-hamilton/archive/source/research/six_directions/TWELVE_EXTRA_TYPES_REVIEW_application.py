"""Independent complete marked predicates, all-hit witnesses and exact complement."""
import pathlib,json,hashlib,collections,itertools,struct
R=pathlib.Path(__file__).resolve().parent
def load(n):return json.loads((R/n).read_text(encoding='utf-8-sig'))
def sha(n):return hashlib.sha256((R/n).read_bytes()).hexdigest()
def mask(xs):return sum(1<<x for x in set(xs))
def swap(x,i):return x^(3<<i) if ((x>>i)^(x>>(i+1)))&1 else x
def orbit(seed):
 seen={seed};todo=[seed]
 while todo:
  t=todo.pop()
  for d in range(4):
   u=tuple(tuple(sorted(swap(x,d) for x in a)) for a in t)
   if u not in seen:seen.add(u);todo.append(u)
 return seen
p=load('TWELVE_EXTRA_TYPES_REVIEW_prepare.json');sel=set(p['selected_indices']);s=load('TWELVE_EXTRA_TYPES_summary.json');profile=load('TWELVE_EXTRA_TYPES_profile.json');producer=load('TWELVE_EXTRA_TYPES_coverage.json')
byid={r['index']:r for r in s['reports']};prof={r['index']:r for r in profile['rows']};positive={i for i,r in byid.items() if r['full_rank']}
assert len(positive)==293 and positive==set(producer['producer_full_rank_indices']) and sel<=positive
lookup={}
for i in positive:
 g=byid[i]['geometry'];assert all(g[k]==prof[i][k] for k in ['type','minority','majority','omitted','actual_records'])
 n=32-len(g['minority'])-len(g['majority']);assert byid[i]['rank']==1<<(n//2-1)
 for anchor in g['minority']:
  seed=tuple(tuple(sorted(x^anchor for x in g[k])) for k in ['minority','majority','omitted'])
  for a,b,c in orbit(seed):
   key=(mask(a),mask(b),mask(c));assert key not in lookup or lookup[key]==i;lookup[key]=i
def project(x,d):return sum(((x>>j)&1)<<i for i,j in enumerate(j for j in range(6) if j!=d))
def witnesses(name,count):
 raw=(R/name).read_bytes();assert len(raw)==count*28
 yield from struct.iter_unpack('<BIHBQIII',raw)
alliter=iter(witnesses('TWELVE_EXTRA_TYPES_positive_hits.bin',448830));siter=iter(witnesses('TWELVE_EXTRA_TYPES_selected_witnesses.bin',28089));allw=next(alliter,None);sw=next(siter,None)
rows={ (3,2):('T26',True,2),(1,4):('T26',False,2),(4,3):('T15',True,2),(2,5):('T15',False,2),(4,2):('T17',True,3),(1,5):('T17',False,3)}
counts=collections.Counter();projections=collections.Counter();chosen=collections.Counter();reports=[];totalallw=0;totalsw=0
for v in (1,7,31):
 name=f'TWELVE_NEW_FORCED_HALL_union_remaining_v{v}.bin';raw=(R/name).read_bytes();assert len(raw)%11==0
 recs=[raw[j:j+11] for j in range(0,len(raw),11)];assert len(set(recs))==len(recs)
 rem=bytearray();hitn=0
 for index,rec in enumerate(recs):
  Z,W=rec[:5],rec[5:];H={0,*rec};assert len(H)==12 and all(x and x<64 and x.bit_count()%2==0 for x in Z) and all(x<64 and x.bit_count()%2 for x in W);assert list(Z)==sorted(Z) and list(W)==sorted(W) and v not in W
  assert all((x^y).bit_count()!=1 for x in Z for y in W)
  candidates=collections.defaultdict(set)
  for d in range(6):
   A=lambda x:((x^v)&(1<<d))==0
   za=[x for x in Z if A(x)];wa=[x for x in W if A(x)];shape=(len(za),len(wa))
   if shape not in rows:continue
   typ,even,n=rows[shape]
   if even:pool=za;minor=[x for x in Z if not A(x)];major=[x for x in W if not A(x)]
   else:pool=[x for x in wa if x!=1<<d];minor=[x for x in W if not A(x)];major=[x for x in Z if not A(x)]
   for sources in itertools.combinations(pool,n):
    projections[typ]+=1;Y=[x^(1<<d) for x in sources];assert not set(Y)&H
    M,J,O=[project(x,d) for x in minor],[project(x,d) for x in major+Y],[project(x,d) for x in Y];anchor=min(M)
    key=(mask(x^anchor for x in M),mask(x^anchor for x in J),mask(x^anchor for x in O));orb=lookup.get(key)
    if orb is not None:candidates[orb].add((d,mask(sources),mask(M),mask(J),mask(O)))
  observed=set()
  while allw is not None and allw[:2]==(v,index):
   vv,ii,orb,d,S,M,J,O=allw;assert orb in positive and orb not in observed and (d,S,M,J,O) in candidates.get(orb,())
   observed.add(orb);totalallw+=1;allw=next(alliter,None)
  assert observed==set(candidates),(v,index,'full record/orbit equality')
  counts.update(observed)
  selectedhits=set(candidates)&sel;assert bool(selectedhits)==bool(candidates),(v,index,'selected11/full293 union mismatch')
  if selectedhits:
   assert sw is not None and sw[:2]==(v,index);vv,ii,orb,d,S,M,J,O=sw
   assert orb in selectedhits and (d,S,M,J,O) in candidates[orb];chosen[orb]+=1;totalsw+=1;sw=next(siter,None);hitn+=1
  else:rem.extend(rec)
 assert bytes(rem)==(R/f'TWELVE_EXTRA_TYPES_positive_remaining_v{v}.bin').read_bytes()
 reports.append({'v':v,'input':len(recs),'covered':hitn,'remaining':len(rem)//11,'independent_remaining_sha256':hashlib.sha256(rem).hexdigest()})
assert allw is None and sw is None and totalallw==448830 and totalsw==28089
for i in positive:assert counts[i]==prof[i]['actual_records']
assert [r['remaining'] for r in reports]==[0,504,777]
for n,h in p['frozen_hashes'].items():assert sha(n)==h,n
out={'status':'PASS','source_final_PASS_bound':True,'input':29370,'independent_lookup_keys_full293':len(lookup),'selected11_and_full293_geometric_unions_exactly_equal':True,'all_positive_record_orbit_sets_exactly_equal':True,'all_positive_hit_witnesses_replayed':448830,'selected_witnesses_replayed':28089,'legal_source_projections':dict(projections),'selected_witness_counts':dict(chosen),'per_orbit_record_counts':dict(sorted(counts.items())),'reports':reports,'covered':28089,'remaining_covered_target_geometries':1281,'all_three_remaining_files_exact_bytes':True,'unselected282_rank_certificates_audited':False,'nonfull_searches_used_as_negative_certificates':False,'full_twelve_hole_proved':False,'full_P6_proved':False}
(R/'TWELVE_EXTRA_TYPES_REVIEW_application.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({k:v for k,v in out.items() if k not in ['per_orbit_record_counts','selected_witness_counts']},indent=2))
