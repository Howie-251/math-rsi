from pathlib import Path
import subprocess,hashlib,json,itertools,datetime
P=Path(__file__).resolve().parent
def raw(n):return (P/n).read_bytes()
def sha(b):return hashlib.sha256(b).hexdigest()
manifest=json.loads(raw('Q5_T63_RANK_MANIFEST.json'));files=manifest['files']
for n,h in files.items():assert sha(raw(n))==h,('hash',n)
registry=json.loads(raw('Q5_T63_RANK_batch_summary.json'))['reports'];assert len(registry)==7
lookup={};logs=[]
for r in registry:
 i=r['orbit_index'];g=r['geometry'];prefix=r['prefix']
 assert list(map(int,raw(prefix+'_config.txt').split()))==g['holes']+g['omitted']
 assert len(set(x.bit_count()%2 for x in g['holes']))==1
 result=subprocess.run([str(P/'Q5_T63_RANK_REVIEW_check.exe'),str(P/prefix)],capture_output=True,check=True)
 line=f'{prefix} '+result.stdout.decode('ascii').strip();logs.append(line);print(line,flush=True)
 for perm in itertools.permutations(range(5)):
  transformed=[sum(((x>>j)&1)<<perm[j] for j in range(5)) for x in range(32)]
  for shift in range(32):
   key=tuple(tuple(sorted(transformed[x]^shift for x in g[k])) for k in ('holes','omitted'))
   assert key not in lookup or lookup[key][0]==i,('duplicate marked orbit',i)
   lookup[key]=(i,perm,shift)
(P/'Q5_T63_RANK_REVIEW_certificates.log').write_text('\n'.join(logs)+'\n',encoding='utf-8')
projection=[[sum(((x>>j)&1)<<k for k,j in enumerate(z for z in range(6) if z!=d)) for x in range(64)] for d in range(6)]
def enumerate_actual(rec,v):
 Z=set(rec[:4]);W=set(rec[4:]);assert len(Z)==4 and len(W)==5 and v not in W
 assert all(x and x.bit_count()%2==0 for x in Z) and all(x.bit_count()%2==1 for x in W)
 assert all((x^y).bit_count()!=1 for x in Z for y in W)
 found=[]
 for d in range(6):
  za={x for x in Z if (x>>d&1)==(v>>d&1)};wa={x for x in W if (x>>d&1)==(v>>d&1)};row=(len(za),len(wa))
  if row==(4,2):sources=itertools.combinations(sorted(za),3);base=W-wa
  elif row==(1,5):sources=itertools.combinations(sorted(wa-{1<<d}),3);base=Z-za
  else:continue
  for S in sources:
   Y={x^(1<<d) for x in S};assert len(Y)==3 and 0 not in Y and not(Y&(Z|W))
   assert all((x^(x^(1<<d))).bit_count()==1 for x in S)
   key=tuple(tuple(sorted(projection[d][x] for x in a)) for a in (base|Y,Y))
   assert len(key[0])==6 and len(key[1])==3
   if key not in lookup:continue
   i,perm,shift=lookup[key]
   found.append({'cut':d,'row':row,'sources':S,'holes':key[0],'omitted':key[1],'orbit_index':i,'cube_permutation':perm,'cube_shift':shift})
 return found
producer=json.loads(raw('Q5_T63_RANK_coverage.json'));prd={(r['v'],r['input_index']):r for r in producer['witnesses']}
assert len(prd)==len(producer['witnesses'])
domainreview=json.loads(raw('Q5_T26_RANK_BATCH_REVIEW.json'))
out=[];witnesses=[];seen=set();orbitcounts={i:0 for i in range(7)}
for v in (1,7,31):
 n=f'Q5_T26_RANK_BATCH_REVIEW_remaining_v{v}.bin';b=raw(n);assert sha(b)==domainreview['evidence'][n]
 records=[b[i:i+9] for i in range(0,len(b),9)];assert len(set(records))==len(records)
 remain=[];covered=0
 for index,rec in enumerate(records):
  found=enumerate_actual(rec,v);p=prd.get((v,index));assert bool(found)==bool(p),('coverage',v,index)
  if not found:remain.append(rec);continue
  seen.add((v,index));covered+=1
  assert any(z['cut']==p['cut'] and z['row']==tuple(p['row']) and set(z['sources'])==set(p['sources']) and list(z['holes'])==p['holes'] and list(z['omitted'])==p['omitted'] and z['orbit_index']==p['orbit_index'] for z in found),('producer witness',v,index)
  for i in {z['orbit_index'] for z in found}:orbitcounts[i]+=1
  witnesses.append({'v':v,'input_index':index,'record':list(rec),**found[0]})
 remaining=b''.join(remain);assert remaining==raw(f'Q5_T63_RANK_remaining_v{v}.bin')
 assert set(remain)==set(records)-{bytes(w['record']) for w in witnesses if w['v']==v}
 n=f'Q5_T63_RANK_REVIEW_remaining_v{v}.bin';(P/n).write_bytes(remaining)
 out.append({'v':v,'input':len(records),'net_new':covered,'remaining':len(remain),'remaining_file':n,'remaining_sha256':sha(remaining),'exact_bytes_and_sets_equal':True})
 print(out[-1],flush=True)
assert seen==set(prd)
result={'all_manifest_hashes_match':True,'certificates':7,'selected_forests':7*4096,'columns_verified':7*4096,'connectivity_bits_verified':7*4096**2,'rank_GF2_each':4096,'marked_orbit_lookup_size':len(lookup),'reports':out,'newly_covered':sum(r['net_new'] for r in out),'remaining':sum(r['remaining'] for r in out),'per_orbit_domain_coverage':orbitcounts}
(P/'Q5_T63_RANK_REVIEW_check.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
(P/'Q5_T63_RANK_REVIEW_witnesses.json').write_text(json.dumps(witnesses,separators=(',',':'))+'\n',encoding='utf-8')
print(json.dumps(result),flush=True)
