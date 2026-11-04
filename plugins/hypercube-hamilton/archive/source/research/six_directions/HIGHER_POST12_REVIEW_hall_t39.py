import collections,hashlib,itertools,json,pathlib,struct
R=pathlib.Path(__file__).resolve().parent
def rd(n):return json.loads((R/n).read_text(encoding='utf-8-sig'))
def mask(xs):return sum(1<<x for x in set(xs))
def project(x,d):return (x&((1<<d)-1))|((x>>(d+1))<<d)
even={x for x in range(64) if x.bit_count()%2==0};odd=set(range(64))-even
g=next(g for g in rd('FOURTEEN_FORCED_REVIEW.json')['accepted_marked_inputs'] if g['index']==54)
assert not g['forced_pairs'] and g['rank_GF2']==512
orbit=set()
for p in itertools.permutations(range(5)):
 tr=[sum(((x>>d)&1)<<p[d] for d in range(5)) for x in range(32)]
 for shift in range(32):orbit.add(tuple(mask(tr[x]^shift for x in g[k]) for k in ['minority','majority','omitted']))
output=[]
for k,stem in [(8,'SIXTEEN_POST12'),(9,'EIGHTEEN_POST12')]:
 width=2*k-1;NZ=k-1;inputs={};paritysets={};removed=collections.defaultdict(set);hist=collections.Counter();report=[]
 for v in (1,7,31):
  for f,status in enumerate(['covered','free']):
   raw=(R/f'{stem}_REUSE_remaining_h{2*k}_v{v}_{status}.bin').read_bytes();assert len(raw)%width==0
   records=[raw[j:j+width] for j in range(0,len(raw),width)];assert len(records)==len(set(records));inputs[v,f]=records;paritysets[v,f]=[]
   for r in records:
    z=list(r[:NZ]);w=list(r[NZ:]);assert z==sorted(set(z)) and w==sorted(set(w)) and len(z)==NZ and len(w)==k
    H={0,*z,*w};assert set(z)<=even and 0 not in z and set(w)<=odd and ((v in w)==bool(f))
    assert all((x^y).bit_count()!=1 for x in z for y in w)
    if f:assert all(y.bit_count()!=1 for y in w)
    E=even-H;O=odd-H;assert len(E)==len(O)==32-k;paritysets[v,f].append((E,O))
 raw=(R/f'{stem}_HALL_witnesses.bin').read_bytes();assert len(raw)%22==0
 for v,f,i,Sm,Tm in struct.iter_unpack('<BBIQQ',raw):
  assert (v,f) in inputs and i<len(inputs[v,f]) and i not in removed[v,f]
  E,O=paritysets[v,f][i];S={x for x in range(64) if Sm>>x&1};T={x for x in range(64) if Tm>>x&1}
  assert S and S<=E and T==({x^(1<<d) for x in S for d in range(6)}&O) and len(T)<len(S)
  removed[v,f].add(i);hist[f'{len(S)}:{len(T)}']+=1
 for (v,f),records in inputs.items():
  status='free' if f else 'covered';rem=b''.join(r for i,r in enumerate(records) if i not in removed[v,f]);out=f'{stem}_HALL_remaining_v{v}_{status}.bin'
  assert rem==(R/out).read_bytes();report.append({'v':v,'free':f,'input':len(records),'Hall_excluded':len(removed[v,f]),'remaining':len(rem)//width,'remaining_sha256':hashlib.sha256(rem).hexdigest()})
 # Check only the one formally accepted T39 input, independent of diagnostic forced rows.
 witnesses={};raw=(R/f'{stem}_FORCED_witnesses.bin').read_bytes();assert len(raw)%40==0
 for at in range(0,len(raw),40):
  r=raw[at:at+40];v,i,idx,d,S,M,J,U,n,*ends=struct.unpack('<BIHBQIIIB4B7x',r)
  assert v in (1,7,31) and idx==54 and d<6 and n==0 and ends==[255]*4 and not any(r[-7:]) and (v,i) not in witnesses
  witnesses[v,i]=(d,S,M,J,U)
 t39=[];actualinputs=set()
 for v in (1,7,31):
  raw=(R/f'{stem}_HALL_remaining_v{v}_covered.bin').read_bytes();assert len(raw)%width==0;remaining=bytearray();yes=0
  for i,at in enumerate(range(0,len(raw),width)):
   rec=raw[at:at+width];Z=set(rec[:NZ]);W=set(rec[NZ:]);assert len(Z)==NZ and len(W)==k and v not in W
   choices=set();actualinputs.add((v,i))
   for d in range(6):
    side=(v>>d)&1;za={x for x in Z if ((x>>d)&1)==side};wa={x for x in W if ((x>>d)&1)==side};a=len(za);b=len(wa)
    for branch in ['even','odd']:
     if branch=='even':
      if a+1-b!=3 or b<1:continue
      pool=za;minor=Z-za;major=W-wa
     else:
      if b-a-1!=3:continue
      pool=wa-{v,1<<d};minor=W-wa;major=Z-za
     if len(minor)!=3 or len(major)+3!=9:continue
     assert (a,b)==((k-4,k-6) if branch=='even' else (k-7,k-3))
     for S in itertools.combinations(sorted(pool),3):
      Y={x^(1<<d) for x in S};assert not Y&({0}|Z|W)
      M,J,U=tuple(mask(project(x,d) for x in xs) for xs in [minor,major|Y,Y])
      if (M,J,U) in orbit:choices.add((d,mask(S),M,J,U))
   if choices:
    assert (v,i) in witnesses and witnesses[v,i] in choices;yes+=1
   else:
    assert (v,i) not in witnesses;remaining.extend(rec)
  n=f'{stem}_FORCED_remaining_v{v}_covered.bin';assert bytes(remaining)==(R/n).read_bytes()
  t39.append({'v':v,'input':len(raw)//width,'positive54':yes,'remaining':len(remaining)//width,'remaining_sha256':hashlib.sha256(remaining).hexdigest()})
 assert set(witnesses)<=actualinputs
 expected=(16989,1211,199,1012) if k==8 else (7050,150,150,0)
 assert (sum(len(x) for x in removed.values()),sum(r['remaining'] for r in report),len(witnesses),sum(r['remaining'] for r in t39))==expected
 output.append({'k':k,'width':width,'Hall_exclusions':sum(len(x) for x in removed.values()),'Hall_size_histogram':dict(hist),'all_Hall_certificates_and_six_complements_verified':True,'Hall_reports':report,'T39_selected_witnesses':len(witnesses),'T39_all_input_cut_sources_exhausted':True,'T39_only_formal_index54_used':True,'T39_all_three_complements_verified':True,'T39_reports':t39})
result={'status':'PASS','reports':output,'complete16_implies_complete18_proved_modulo_accepted_imports':True,'full_fourteen_hole_proved':False,'full_sixteen_hole_proved':False,'full_eighteen_hole_proved':False,'full_P6_proved':False}
(R/'HIGHER_POST12_REVIEW_hall_t39.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8');print(json.dumps(result,indent=2))
