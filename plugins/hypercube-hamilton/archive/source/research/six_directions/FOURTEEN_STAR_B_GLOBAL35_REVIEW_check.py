"""Fresh all-cut/source application audit using complete marked cube images."""
import collections,hashlib,itertools,json,pathlib,struct
R=pathlib.Path(__file__).resolve().parent
def read(n):return json.loads((R/n).read_text(encoding='utf-8-sig'))
def mask(xs):return sum(1<<x for x in set(xs))
def project(x,d):return (x&((1<<d)-1))|((x>>(d+1))<<d)
formal=read('FOURTEEN_STAR_EXPANDED_REVIEW.json');assert formal['verdict']=='PASS'
g=next(g for g in formal['accepted_marked_inputs'] if g['index']==35);rows=[{'index':35,'geometry':g,'forced_pairs':[g['forced_pair']]}];lookup=collections.defaultdict(set)
maps=[tuple(sum(((x>>p[d])&1)<<d for d in range(5)) for x in range(32)) for p in itertools.permutations(range(5))]
for row in rows:
 g=row['geometry']
 for tr in maps:
  for shift in range(32):
   key=tuple(mask(tr[x]^shift for x in g[k]) for k in ['minority','majority','omitted'])
   pairs=tuple(sorted(tuple(sorted((tr[a]^shift,tr[b]^shift))) for a,b in row['forced_pairs']))
   lookup[key].add((row['index'],pairs))
selected={};raw=(R/'FOURTEEN_STAR_B_GLOBAL35_witnesses.bin').read_bytes();assert len(raw)%40==0
for at in range(0,len(raw),40):
 r=raw[at:at+40];v,i,idx,d,S,M,J,U,n,*ends=struct.unpack('<BIHBQIIIB4B7x',r)
 assert not any(r[-7:]) and v in (1,7,31) and d<6 and n in (0,1,2) and all(x==255 for x in ends[2*n:])
 pairs=tuple(sorted(tuple(sorted(ends[j:j+2])) for j in range(0,2*n,2)))
 assert len({x for e in pairs for x in e})==2*n and (v,i) not in selected
 selected[v,i]=(idx,d,S,M,J,U,pairs)
reports=[];forcedset=set();plainset=set();hist=collections.Counter();allinput=set();projectioncount=0
for v in (1,7,31):
 src=(R/f'FOURTEEN_STAR_EXPANDED_remaining_v{v}_covered.bin').read_bytes();assert len(src)%13==0
 remaining=bytearray();hits=collections.Counter();positive=0;sourceprojections=0
 for i,at in enumerate(range(0,len(src),13)):
  rec=src[at:at+13];Z=set(rec[:6]);W=set(rec[6:]);assert len(Z)==6 and len(W)==7 and 0 not in Z and v not in W
  assert all(x and x<64 and x.bit_count()%2==0 for x in Z) and all(x<64 and x.bit_count()%2 for x in W)
  assert all((x^y).bit_count()!=1 for x in Z for y in W)
  allinput.add((v,i));choices=set();ids=set()
  for d in range(6):
   side=(v>>d)&1
   za={x for x in Z if ((x>>d)&1)==side};wa={x for x in W if ((x>>d)&1)==side};a=len(za);b=len(wa)
   for branch in ['even','odd']:
    if branch=='even':
     s=a+1-b
     if s<3 or b<1:continue
     pool=za;minor=Z-za;major=W-wa
    else:
     s=b-a-1
     if s<3:continue
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
      if side==1 and 0 in ends:continue
      choice=(idx,d,mask(S),M,J,U,pairs);choices.add(choice);ids.add(idx)
  for idx in ids:hits[idx]+=1
  if ids-{54}:forcedset.add((v,i))
  if 54 in ids:plainset.add((v,i))
  if choices:
   assert (v,i) in selected and selected[v,i] in choices,(v,i,'missing or invalid positive witness')
   hist[str(selected[v,i][0])]+=1;positive+=1
  else:
   assert (v,i) not in selected,(v,i,'false positive');remaining.extend(rec)
 out=f'FOURTEEN_STAR_B_GLOBAL35_remaining_v{v}_covered.bin';assert bytes(remaining)==(R/out).read_bytes()
 reports.append({'v':v,'input':len(src)//13,'safe':positive,'remaining':len(remaining)//13,'legal_target_shapes_source_projections':sourceprojections,'per_local_hit_records':dict(hits),'remaining_sha256':hashlib.sha256(remaining).hexdigest()});projectioncount+=sourceprojections
assert set(selected)<=allinput and len(selected)==120 and len(forcedset)==120 and len(plainset)==0 and not forcedset&plainset
assert [x['remaining'] for x in reports]==[240,702,1345]
manifest=read('FOURTEEN_STAR_B_GLOBAL35_MANIFEST.json')
for name,val in manifest['files'].items():assert hashlib.sha256((R/name).read_bytes()).hexdigest()==val['sha256'] and (R/name).stat().st_size==val['bytes']
assert hashlib.sha256((R/'FOURTEEN_STAR_EXPANDED_REVIEW.json').read_bytes()).hexdigest()=='0ee6de8602e4e364adce1e98893228db3077c3dd5bfc08fc3748ac98c4727ee8'
checked={}
for name in ['FOURTEEN_STAR_EXPANDED_REVIEW.json','HIGHER_FORCED_CHERRY_REVIEW.json']:
 d=read(name);assert d['verdict']=='PASS'
 for field in ['audited_input_hashes','imported_dependency_hashes','checker_artifact_hashes']:
  for path,h in d.get(field,{}).items():
   if path not in checked:checked[path]=hashlib.sha256((R/path).read_bytes()).hexdigest()
   assert checked[path]==h.removeprefix('sha256:')
for v in (1,7,31):
 name=f'FOURTEEN_STAR_EXPANDED_remaining_v{v}_covered.bin';assert hashlib.sha256((R/name).read_bytes()).hexdigest()==formal['audited_input_hashes'][name]
result={'status':'PASS','all2407_actual_inputs_checked':True,'all_legal_target_shape_cut_sources_exhausted':True,'all_actual_common_marked_transports_verified':True,'root_in_R_routes_used':False,'all_R_endpoints_covered_and_same_parity_as_omissions':True,'all_selected_witnesses_verified':len(selected),'forced_safe':len(forcedset),'unconditional_routes':len(plainset),'intersection':len(forcedset&plainset),'union':len(forcedset|plainset),'remaining_covered':sum(x['remaining'] for x in reports),'remaining_free':0,'all_three_remaining_streams_byte_exact':True,'chosen_local_counts':dict(hist),'legal_source_projections':projectioncount,'reports':reports,'only_finally_accepted_class35_used':True,'manifest_files_verified':len(manifest['files']),'formal_direct_bindings_verified':len(checked),'fourteen_hole_free_targets_proved':True,'full_fourteen_hole_proved':False,'full_P6_proved':False}
(R/'FOURTEEN_STAR_B_GLOBAL35_REVIEW_check.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8');print(json.dumps(result,indent=2))
