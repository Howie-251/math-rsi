"""Fresh all-cut/source application audit using complete marked cube images."""
import collections,hashlib,itertools,json,pathlib,struct
R=pathlib.Path(__file__).resolve().parent
def read(n):return json.loads((R/n).read_text(encoding='utf-8-sig'))
def mask(xs):return sum(1<<x for x in set(xs))
def project(x,d):return (x&((1<<d)-1))|((x>>(d+1))<<d)
rows=read('SIXTEEN_LOCAL_candidate_classes.json')['classes'];selected_ids={r['index'] for r in read('SIXTEEN_LOCAL_CERT_summary.json')['reports']};ordinary_ids={r['index'] for r in rows if not r['forced_pairs']};lookup=collections.defaultdict(set)
allhits=read('SIXTEEN_LOCAL_all_hit_sets.json');allhit_map={(r['v'],r['index']):set(r['local_indices']) for r in allhits};assert len(allhit_map)==len(allhits)==1012
maps=[tuple(sum(((x>>p[d])&1)<<d for d in range(5)) for x in range(32)) for p in itertools.permutations(range(5))]
for row in rows:
 g=row['geometry']
 for tr in maps:
  for shift in range(32):
   key=tuple(mask(tr[x]^shift for x in g[k]) for k in ['minority','majority','omitted'])
   pairs=tuple(sorted(tuple(sorted((tr[a]^shift,tr[b]^shift))) for a,b in row['forced_pairs']))
   lookup[key].add((row['index'],pairs))
selected={};raw=(R/'SIXTEEN_LOCAL_witnesses.bin').read_bytes();assert len(raw)%40==0
for at in range(0,len(raw),40):
 r=raw[at:at+40];v,i,idx,d,S,M,J,U,n,*ends=struct.unpack('<BIHBQIIIB4B7x',r)
 assert not any(r[-7:]) and v in (1,7,31) and d<6 and n in (0,1,2) and all(x==255 for x in ends[2*n:])
 pairs=tuple(sorted(tuple(sorted(ends[j:j+2])) for j in range(0,2*n,2)))
 assert len({x for e in pairs for x in e})==2*n and (v,i) not in selected
 selected[v,i]=(idx,d,S,M,J,U,pairs)
reports=[];forcedset=set();plainset=set();hist=collections.Counter();allinput=set();projectioncount=0
for v in (1,7,31):
 src=(R/f'SIXTEEN_POST12_FORCED_remaining_v{v}_covered.bin').read_bytes();assert len(src)%15==0
 remaining=bytearray();hits=collections.Counter();positive=0;sourceprojections=0
 for i,at in enumerate(range(0,len(src),15)):
  rec=src[at:at+15];Z=set(rec[:7]);W=set(rec[7:]);assert len(Z)==7 and len(W)==8 and 0 not in Z and v not in W
  assert list(rec[:7])==sorted(Z) and list(rec[7:])==sorted(W)
  assert all(x and x<64 and x.bit_count()%2==0 for x in Z) and all(x<64 and x.bit_count()%2 for x in W)
  assert all((x^y).bit_count()!=1 for x in Z for y in W)
  allinput.add((v,i));choices=set();ids=set();candidate_ids=set()
  for d in range(6):
   side=(v>>d)&1
   za={x for x in Z if ((x>>d)&1)==side};wa={x for x in W if ((x>>d)&1)==side};a=len(za);b=len(wa)
   for branch in ['even','odd']:
    if branch=='even':
     s=a+1-b
     if s<2 or b<1:continue
     pool=za;minor=Z-za;major=W-wa
    else:
     s=b-a-1
     if s<2:continue
     pool=wa-{v,1<<d};minor=W-wa;major=Z-za
    shapes={(len(r['geometry']['minority']),len(r['geometry']['majority']),len(r['geometry']['omitted'])) for r in rows}
    if (len(minor),len(major)+s,s) not in shapes:continue
    for S in itertools.combinations(sorted(pool),s):
     sourceprojections+=1;Y={x^(1<<d) for x in S}
     assert not Y&({0}|Z|W) and all(((x>>d)&1)!=side for x in Y)
     M=mask(project(x,d) for x in minor);J=mask(project(x,d) for x in major|Y);U=mask(project(x,d) for x in Y)
     for idx,pairs in lookup.get((M,J,U),()):
      ends={x for e in pairs for x in e}
      assert not any((M|J)>>x&1 for x in ends)
      # Lift actual B endpoints; all must have the global parity of Y.
      def lift(x):return (x&((1<<d)-1))|((x>>d)<<(d+1))|((1-side)<<d)
      assert all(lift(x).bit_count()%2==next(iter(Y)).bit_count()%2 for x in ends)
      if pairs and (s<3 or (side==1 and 0 in ends)):continue
      candidate_ids.add(idx)
      if idx not in selected_ids:continue
      choice=(idx,d,mask(S),M,J,U,pairs);choices.add(choice);ids.add(idx)
  assert candidate_ids==allhit_map[v,i] and bool(ids)==bool(candidate_ids),(v,i,"selected9/all16 union or all-hit set differs")
  for idx in ids:hits[idx]+=1
  if ids-ordinary_ids:forcedset.add((v,i))
  if ids&ordinary_ids:plainset.add((v,i))
  if choices:
   assert (v,i) in selected and selected[v,i] in choices,(v,i,'missing or invalid positive witness')
   hist[str(selected[v,i][0])]+=1;positive+=1
  else:
   assert (v,i) not in selected,(v,i,'false positive');remaining.extend(rec)
 out=f'SIXTEEN_LOCAL_remaining_v{v}_covered.bin';assert bytes(remaining)==(R/out).read_bytes()
 reports.append({'v':v,'input':len(src)//15,'safe':positive,'remaining':len(remaining)//15,'legal_target_shapes_source_projections':sourceprojections,'per_local_hit_records':dict(hits),'remaining_sha256':hashlib.sha256(remaining).hexdigest()});projectioncount+=sourceprojections
assert set(selected)<=allinput and len(selected)==864
assert [x['remaining'] for x in reports]==[0,18,130]
result={'status':'PASS','all1012_actual_inputs_checked':True,'all_legal_target_shape_cut_sources_exhausted':True,'all_actual_common_marked_transports_verified':True,'root_in_R_routes_used':False,'all_R_endpoints_covered_and_same_parity_as_omissions':True,'all_selected_witnesses_verified':len(selected),'forced_safe':len(forcedset),'ordinary_safe':len(plainset),'intersection':len(forcedset&plainset),'union':len(forcedset|plainset),'remaining_covered':sum(x['remaining'] for x in reports),'remaining_free':0,'all_three_remaining_streams_byte_exact':True,'chosen_local_counts':dict(hist),'legal_source_projections':projectioncount,'reports':reports,'selected9_and_candidate16_geometric_unions_equal_on_every_input':True,'all1012_candidate_hit_sets_independently_recomputed':True,'source_reduction_conditional_on_complete14':True,'full_sixteen_hole_proved':False,'full_P6_proved':False}
(R/'SIXTEEN_LOCAL_REVIEW_application.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8');print(json.dumps(result,indent=2))
