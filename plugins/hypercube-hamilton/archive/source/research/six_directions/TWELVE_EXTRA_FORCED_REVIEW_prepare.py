import pathlib,json,hashlib
R=pathlib.Path(__file__).resolve().parent
def load(n):return json.loads((R/n).read_text(encoding='utf-8-sig'))
def sha(n):return hashlib.sha256((R/n).read_bytes()).hexdigest()
def mask(a):return sum(1<<x for x in a)
assert sha('TWELVE_EXTRA_FORCED_MANIFEST.json')=='0c40fc7c8d25f67aa4cc4e79698e2c7477b95b5d38ebf2f7a123a6c29c3d3534'
m=load('TWELVE_EXTRA_FORCED_MANIFEST.json')
for n,h in m['hashes'].items():
 assert sha(n)==h,n
 if 'sizes' in m:assert (R/n).stat().st_size==m['sizes'][n]
fixed={}
for line in (R/'TWELVE_EXTRA_FORCED_PROOF.md').read_text().splitlines():
 t=[x.strip() for x in line.strip('|').split('|')]
 if line.startswith('|') and t[0].isdigit():fixed[int(t[0])]=list(map(int,t[1].split(',')))
s=load('TWELVE_EXTRA_FORCED_summary.json');assert len(fixed)==len(s['reports'])==s['count']==15
old=[]
for line in (R/'Q5_T17_RANK_BATCH_PROOF.md').read_text().splitlines():
 t=[x.strip() for x in line.strip('|').split('|')]
 if line.startswith('|') and t[0].isdigit() and 'absent' in t[3]:old.append((tuple(map(int,t[1].replace('$','').split(','))),tuple(map(int,t[2].replace('$','').split(',')))))
def swap(x,i):return x^(3<<i) if ((x>>i)^(x>>(i+1)))&1 else x
def orbit(seed):
 seen={seed};todo=[seed]
 while todo:
  t=todo.pop()
  for i in range(4):
   u=tuple(tuple(sorted(swap(x,i) for x in a)) for a in t)
   if u not in seen:seen.add(u);todo.append(u)
 return seen
oldimages=set()
for seed in old:oldimages|=orbit(seed)
rows=[]
for r in s['reports']:
 g=r['geometry'];i=r['index'];J=g['majority'];O=g['omitted'];H={0,*J};K=set(range(32))-H;h=r['forced_hole'];p,q=r['forced_pair']
 assert J==fixed[i] and g['minority']==[0] and O==[1,2,4] and (h,p,q)==(0,8,16)
 assert all(x.bit_count()%2 for x in J) and len(H)==8 and set(O)<=set(J) and {p,q}<=K
 assert [{x for x in H-set(O) if len({x^(1<<d) for d in range(5)}-set(O))==2}]==[{0}]
 assert r['rank']==1024 and r['covered_endpoints']==24 and r['reduced_endpoints']==22
 assert (tuple(J),tuple(O)) not in oldimages
 assert load(r['prefix']+'.json')==r
 assert list(map(int,(R/(r['prefix']+'_config.txt')).read_text().split()))==sorted(H)+O
 rows.append(f"{i} {r['prefix']} {mask(H)} {mask(O)} {h} {p} {q}\n")
(R/'TWELVE_EXTRA_FORCED_REVIEW_rows.txt').write_text(''.join(rows))
source=load('TWELVE_EXTRA_TYPES_REVIEW.json');assert source['verdict']=='PASS' and sha('TWELVE_EXTRA_TYPES_REVIEW.json')=='d3acfe0680d227a60c7fac1f3bcef8dc22ed22d94298a0e72852428888dfad43'
for v in (1,7,31):
 n=f'TWELVE_EXTRA_TYPES_positive_remaining_v{v}.bin';assert sha(n)==source['audited_input_hashes'][n].removeprefix('sha256:')
out={'status':'PASS','manifest_sha256':sha('TWELVE_EXTRA_FORCED_MANIFEST.json'),'frozen_hashes_checked':len(m['hashes']),'local_rows':15,'new_rows_not_old_seven_images':True,'unique_forced_hole_each':True,'source_final_PASS_bound':True,'source_review_sha256':sha('TWELVE_EXTRA_TYPES_REVIEW.json'),'local_marked_rows':[{'index':r['index'],'minority':[0],'majority':r['geometry']['majority'],'omitted':[1,2,4],'forced_hole':0,'forced_pair':[8,16]} for r in s['reports']]}
(R/'TWELVE_EXTRA_FORCED_REVIEW_prepare.json').write_text(json.dumps(out,indent=2)+'\n');print({k:v for k,v in out.items() if k!='local_marked_rows'})
