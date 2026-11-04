from pathlib import Path
import subprocess,hashlib,json,itertools,datetime,sys
P=Path(__file__).resolve().parent
def raw(n):return (P/n).read_bytes()
def sha(b):return hashlib.sha256(b).hexdigest()
manifest=json.loads(raw('Q5_T26_RANK_BATCH_MANIFEST.json'))
assert sha(raw('Q5_T26_RANK_BATCH_MANIFEST.json'))=='8f5980a073c646677c3ddfbf69dc8f300affccecd08d7f1cd9d34a9198fc58de'
for n,h in manifest['hashes'].items():
 assert sha(raw(n))==h,('hash',n)
 if 'sizes' in manifest:assert len(raw(n))==manifest['sizes'][n],('size',n)
registry=json.loads(raw('Q5_T26_RANK_batch_summary.json'))['reports'];assert len(registry)==55
first=json.loads(raw('Q5_T26_RANK_FIRST_REVIEW_check.json'));assert first['rank_GF2']==2048
log=[];orbits={}
for r in registry:
 i=r['orbit_index'];g=r['geometry'];prefix=r['prefix']
 expected=g['minority']+g['majority']+g['omitted']
 assert list(map(int,raw(prefix+'_config.txt').split()))==expected
 if i and '--resume-coverage' not in sys.argv:
  result=subprocess.run([str(P/'Q5_T26_RANK_BATCH_REVIEW_check.exe'),str(P/prefix)],capture_output=True,check=True)
  line=result.stdout.decode(errors='replace').strip();log.append(line);print(i,'independent rank/forest/all bits PASS',flush=True)
 for perm in itertools.permutations(range(5)):
  transformed=[sum(((x>>j)&1)<<perm[j] for j in range(5)) for x in range(32)]
  for shift in range(32):
   key=tuple(tuple(sorted(transformed[x]^shift for x in g[k])) for k in ('minority','majority','omitted'))
   assert key not in orbits or orbits[key][0]==i,('duplicate orbit',i,key)
   orbits[key]=(i,perm,shift)
if log:(P/'Q5_T26_RANK_BATCH_REVIEW_certificates.log').write_text('\n'.join(log)+'\n',encoding='utf-8')
print('all 55 rank certificates accepted; checking actual 41236 domain',flush=True)
projection=[[sum(((x>>j)&1)<<k for k,j in enumerate(z for z in range(6) if z!=d)) for x in range(64)] for d in range(6)]
def enumerate_actual(rec,v):
 Z=set(rec[:4]);W=set(rec[4:]);assert len(Z)==4 and len(W)==5 and v not in W
 assert all(x and x.bit_count()%2==0 for x in Z) and all(x.bit_count()%2==1 for x in W)
 assert all((x^y).bit_count()!=1 for x in Z for y in W)
 found={}
 for d in range(6):
  za={x for x in Z if (x>>d&1)==(v>>d&1)};wa={x for x in W if (x>>d&1)==(v>>d&1)};row=(len(za),len(wa))
  if row==(2,1):sources=[tuple(sorted(za))];minor=Z-za;major=W-wa
  elif row==(0,3):sources=itertools.combinations(sorted(wa-{1<<d}),2);minor=W-wa;major=Z-za
  else:continue
  for S in sources:
   Y={x^(1<<d) for x in S};assert len(Y)==2 and 0 not in Y and not (Y&(Z|W))
   key=tuple(tuple(sorted(projection[d][x] for x in a)) for a in (minor,major|Y,Y))
   if key not in orbits:continue
   i,perm,shift=orbits[key]
   found.setdefault(i,[]).append({'cut':d,'row':row,'sources':S,'geometry':key,'perm':perm,'shift':shift})
 return found
producer=json.loads(raw('Q5_T26_RANK_batch_projection_witnesses.json'));prd={(r['v'],r['input_index']):r for r in producer['records']}
assert len(prd)==len(producer['records'])
domainreview=json.loads(raw('TEN_COVERED_Q5_ENDPOINT_REVIEW.json'))
out=[];witnesses=[];seen=set();orbitcounts={i:0 for i in range(55)}
for v in (1,7,31):
 n=f'ten_covered_q5_and_t63_remaining_v{v}.bin';b=raw(n);assert sha(b)==domainreview['audited_input_hashes'][n]
 records=[b[i:i+9] for i in range(0,len(b),9)];assert len(set(records))==len(records)
 remain=[];covered=0
 for index,rec in enumerate(records):
  found=enumerate_actual(rec,v);p=prd.get((v,index));assert p is not None
  seen.add((v,index));assert p['record']==list(rec) and set(map(int,p['witnesses']))==set(found),('orbitsets',v,index)
  if not found:remain.append(rec);continue
  covered+=1
  for i,choices in found.items():
   orbitcounts[i]+=1;w=p['witnesses'][str(i)]
   assert any(z['cut']==w['cut'] and tuple(z['row'])==tuple(w['row']) and set(z['sources'])==set(w['sources']) and all(list(z['geometry'][k])==w[n] for k,n in enumerate(('local_minority','local_majority','local_omitted'))) for z in choices),('witness',v,index,i)
  i=min(found);witnesses.append({'v':v,'index':index,'record':list(rec),'orbit':i,**found[i][0]})
 remaining=b''.join(remain);assert remaining==raw(f'Q5_T26_RANK_batch_remaining_v{v}.bin')
 assert set(remain)==set(records)-{bytes(w['record']) for w in witnesses if w['v']==v}
 n=f'Q5_T26_RANK_BATCH_REVIEW_remaining_v{v}.bin';(P/n).write_bytes(remaining)
 out.append({'v':v,'input':len(records),'net_new':covered,'remaining':len(remain),'remaining_file':n,'remaining_sha256':sha(remaining),'exact_bytes_and_sets_equal':True})
 print(out[-1],flush=True)
assert seen==set(prd)
result={'manifest_hashes_sizes_match':True,'certificates':55,'first_reused_from_independent_check':True,'new_certificates_checked':54,'total_forests':55*2048,'total_matrix_bits':55*2048**2,'all_rank_GF2':2048,'orbit_image_lookup_size':len(orbits),'reports':out,'net_new':sum(r['net_new'] for r in out),'remaining':sum(r['remaining'] for r in out),'per_orbit_latest_domain_coverage':orbitcounts}
(P/'Q5_T26_RANK_BATCH_REVIEW_check.json').write_text(json.dumps(result,indent=2)+'\n')
(P/'Q5_T26_RANK_BATCH_REVIEW_witnesses.json').write_text(json.dumps(witnesses,separators=(',',':'))+'\n')
print(json.dumps(result),flush=True)
