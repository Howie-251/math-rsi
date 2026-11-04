"""Independent forced predicate, Hall inequalities and common-index union."""
import pathlib,json,hashlib,struct,itertools,collections
R=pathlib.Path(__file__).resolve().parent
def load(n):return json.loads((R/n).read_text(encoding='utf-8-sig'))
def sha(n):return hashlib.sha256((R/n).read_bytes()).hexdigest()
def mask(xs):return sum(1<<x for x in set(xs))
def swap(x,i):return x^(3<<i) if ((x>>i)^(x>>(i+1)))&1 else x
def orbit(seed):
 seen={seed};todo=[seed]
 while todo:
  t=todo.pop()
  for i in range(4):
   u=tuple(tuple(sorted(swap(x,i) for x in a)) for a in t)
   if u not in seen:seen.add(u);todo.append(u)
 return seen
manifests=['TWELVE_NEW_FORCED_APPLICATION_MANIFEST.json','TWELVE_HALL_MANIFEST.json','TWELVE_NEW_FORCED_HALL_UNION_MANIFEST.json']
pins=['26830e8b757b40b1a226786635f2877e0de4c44733b47008cd10d188b1b2d49e',None,'b3e63e430bd2fc00c7cf4623ff980a4b262b7ce3f469ba626637025c541240c9']
allhash={}
for n,h in zip(manifests,pins):
 if h:assert sha(n)==h,n
 m=load(n)
 for p,h in m.get('hashes',m.get('files')).items():
  assert sha(p)==h,p
  if 'sizes' in m:assert (R/p).stat().st_size==m['sizes'][p],p
  if p in allhash:assert allhash[p]==h
  allhash[p]=h
local=load('TWELVE_NEW_FORCED_REVIEW.json');generic=load('HIGHER_FORCED_CHERRY_REVIEW.json')
assert local['verdict']==generic['verdict']=='PASS'
for p in ['TWELVE_NEW_FORCED_PROOF.md','TWELVE_NEW_FORCED_summary.json','TWELVE_NEW_FORCED_MANIFEST.json']:
 assert sha(p)==local['audited_input_hashes'][p].removeprefix('sha256:')
assert sha('HIGHER_FORCED_CHERRY_TRANSFER.md')==generic['audited_input_hashes']['HIGHER_FORCED_CHERRY_TRANSFER.md'].removeprefix('sha256:')
lookup=collections.defaultdict(set)
for g in local['details']['accepted_marked_statements']:
 M,J,O,h,OB=g['minority'],g['majority'],g['omitted'],g['forced_hole'],g['forced_pair']
 assert set(OB)=={h^(1<<d) for d in range(5)}-set(O)
 for anchor in M:
  seed=tuple(tuple(sorted(x^anchor for x in a)) for a in (M,J,O,OB,[h]))
  for a,b,c,r,hh in orbit(seed):lookup[(mask(a),mask(b),mask(c))].add((g['index'],mask(r)))
assert all(len(v)==1 for v in lookup.values())
def project(x,d):return sum(((x>>j)&1)<<i for i,j in enumerate(j for j in range(6) if j!=d))
def attainable(rec,v):
 Z,W=rec[:5],rec[5:];found=set();projections=0
 for d in range(6):
  A=lambda x:((x^v)&(1<<d))==0
  za=[x for x in Z if A(x)];wa=[x for x in W if A(x)];a,b=len(za),len(wa)
  if (a,b) in [(3,1),(4,1)]:pool=za;minor=[x for x in Z if not A(x)];major=[x for x in W if not A(x)];n=a
  elif (a,b) in [(0,4),(0,5)]:pool=[x for x in wa if x!=1<<d];minor=[x for x in W if not A(x)];major=[x for x in Z if not A(x)];n=b-1
  else:continue
  for sources in itertools.combinations(pool,n):
   projections+=1;mirrors=[x^(1<<d) for x in sources];assert not set(mirrors)&{0,*rec}
   mi=[project(x,d) for x in minor];jo=[project(x,d) for x in major+mirrors];om=[project(x,d) for x in mirrors];anchor=min(mi)
   key=(mask(x^anchor for x in mi),mask(x^anchor for x in jo),mask(x^anchor for x in om))
   for row,normob in lookup.get(key,()):
    actual=mask(x^anchor for x in range(32) if normob>>x&1)
    assert actual.bit_count()==2 and not actual&(mask(mi)|mask(jo))
    if v>>d&1 and actual&1:continue
    found.add((row,d,mask(sources),mask(mi),mask(jo),mask(om),actual))
 return found,projections
sources={};chosen={v:{} for v in (1,7,31)};hall={v:{} for v in (1,7,31)}
for v in (1,7,31):
 raw=(R/f'TWELVE_NEW_TYPES_positive_remaining_v{v}.bin').read_bytes();assert len(raw)%11==0
 sources[v]=[raw[i:i+11] for i in range(0,len(raw),11)];assert len(set(sources[v]))==len(sources[v])
 for rec in sources[v]:
  Z,W=rec[:5],rec[5:];assert list(Z)==sorted(set(Z)) and list(W)==sorted(set(W));assert all(x and x<64 and x.bit_count()%2==0 for x in Z);assert all(x<64 and x.bit_count()%2 for x in W)
  assert v not in W and len({0,*rec})==12 and all((x^y).bit_count()!=1 for x in Z for y in W)
b=(R/'TWELVE_NEW_FORCED_safe_witnesses.bin').read_bytes();assert len(b)==552*32
for off in range(0,len(b),32):
 v,i,row,d,S,M,J,O,OB=struct.unpack_from('<BIHBQIIII',b,off)
 assert v in chosen and i<len(sources[v]) and i not in chosen[v]
 chosen[v][i]=(row,d,S,M,J,O,OB)
e=mask(x for x in range(64) if x.bit_count()%2==0);o=((1<<64)-1)^e
b=(R/'TWELVE_HALL_witnesses.bin').read_bytes();assert len(b)==7483*21;hist=collections.Counter()
for off in range(0,len(b),21):
 v,i,S,T=struct.unpack_from('<BIQQ',b,off);assert v in hall and i<len(sources[v]) and i not in hall[v]
 H=mask([0,*sources[v][i]]);L=e&~H;RR=o&~H;assert L.bit_count()==RR.bit_count()==26
 assert S and not S&~L
 actual=0
 for x in range(64):
  if S>>x&1:
   for d in range(6):actual|=1<<(x^(1<<d))
 actual&=RR
 assert actual==T and T.bit_count()<S.bit_count()
 hall[v][i]=(S,T);hist[(S.bit_count(),T.bit_count())]+=1
reports=[];totalproj=0;used=collections.Counter()
for v in (1,7,31):
 hit=set();positiveprojections=0
 for i,rec in enumerate(sources[v]):
  candidates,n=attainable(rec,v);totalproj+=n;positiveprojections+=len(candidates)
  if candidates:hit.add(i)
  if i in chosen[v]:assert chosen[v][i] in candidates;used[chosen[v][i][0]]+=1
 assert hit==set(chosen[v])
 hset=set(hall[v]);intersection=hit&hset;assert not intersection
 for prefix,remove in [('TWELVE_NEW_FORCED_safe',hit),('TWELVE_HALL',hset),('TWELVE_NEW_FORCED_HALL_union',hit|hset)]:
  actual=b''.join(rec for i,rec in enumerate(sources[v]) if i not in remove)
  assert actual==(R/f'{prefix}_remaining_v{v}.bin').read_bytes(),(prefix,v)
 reports.append({'v':v,'input':len(sources[v]),'forced_safe':len(hit),'Hall_explicitly_impossible':len(hset),'intersection':len(intersection),'removed_union':len(hit|hset),'remaining':len(sources[v])-len(hit|hset),'positive_safe_projections':positiveprojections})
assert [(r['input'],r['forced_safe'],r['Hall_explicitly_impossible'],r['remaining']) for r in reports]==[(8032,0,1717,6315),(11661,252,1581,9828),(17712,300,4185,13227)]
for p,h in allhash.items():assert sha(p)==h,p
out={'status':'PASS','source_final_acceptance_is_separate_gate':True,'frozen_unique_file_hashes_checked_before_and_after':len(allhash),'input':37405,'forced_safe':552,'forced_selected_witnesses_replayed':552,'forced_all_legal_source_projections_evaluated':totalproj,'forced_local_rows':27,'forced_lookup_entries':len(lookup),'forced_selected_local_indices':sorted(used),'Hall_witnesses_directly_checked':7483,'Hall_size_histogram':{f'{a}:{b}':n for (a,b),n in sorted(hist.items())},'intersection':0,'union_removed':8035,'remaining_covered_target_geometries':29370,'reports':reports,'all_nine_remaining_files_exact_bytes':True,'max_matching_solver_executed_or_trusted':False,'remaining_geometry_realizability_claimed':False,'full_twelve_hole_proved':False,'full_P6_proved':False,'audited_frozen_hashes':allhash}
(R/'TWELVE_NEW_FORCED_HALL_REVIEW_check.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({k:v for k,v in out.items() if k not in ('audited_frozen_hashes','Hall_size_histogram')},indent=2))
