import pathlib,json,hashlib
R=pathlib.Path(__file__).resolve().parent
def load(n):return json.loads((R/n).read_text(encoding='utf-8-sig'))
def sha(n):return hashlib.sha256((R/n).read_bytes()).hexdigest()
def mask(xs):return sum(1<<x for x in set(xs))
local=load('TWELVE_EXTRA_TYPES_LOCAL_MANIFEST.json');app=load('TWELVE_EXTRA_TYPES_APPLICATION_MANIFEST.json');allhash={}
assert sha('TWELVE_EXTRA_TYPES_APPLICATION_MANIFEST.json')=='f9a28e3a7ae109e1405c3d5a337bbc2aa552d287dd1404536bc0e9a16ffa8cd0'
for m in (local,app):
 for n,h in m.get('files',m.get('hashes')).items():
  assert sha(n)==h,n
  if 'sizes' in m:assert (R/n).stat().st_size==m['sizes'][n]
  if n in allhash:assert allhash[n]==h
  allhash[n]=h
selected=[0,3,5,51,77,183,32,18,58,52,12];reg=load('TWELVE_EXTRA_TYPES_greedy_registry.json');summ=load('TWELVE_EXTRA_TYPES_summary.json');byid={r['index']:r for r in summ['reports']}
assert reg['indices']==local['claimed_indices']==selected and len(reg['rows'])==11
rows=[]
for i,r in zip(selected,reg['rows']):
 assert i==r['index'];s=byid[i];g=s['geometry'];typ=r['type'];M,J,O=[set(r[k]) for k in ('minority','majority','omitted')];H=M|J
 assert s['full_rank'] and s['rank']==r['rank']==2048
 assert all(r[k]==g[k] for k in ('type','minority','majority','omitted'))
 assert len(H)==8 and not M&J and O<=J and all(x.bit_count()%2==0 for x in M) and all(x.bit_count()%2 for x in J)
 assert (len(M),len(J),len(O))==((2,6,2) if i!=12 else (1,7,3))
 assert typ==('T26' if i!=12 else 'T17');width=36 if typ=='T26' else 34
 assert list(map(int,(R/(r['prefix']+'_config.txt')).read_text().split()))==sorted(H)+sorted(O)
 meta=load(r['prefix']+'.json')
 rows.append(f"{i} {r['prefix']} {width} {mask(H)} {mask(O)}\n")
(R/'TWELVE_EXTRA_TYPES_REVIEW_rows.txt').write_text(''.join(rows))
source=load('TWELVE_NEW_FORCED_HALL_REVIEW.json');assert source['verdict']=='PASS' and sha('TWELVE_NEW_FORCED_HALL_REVIEW.json')=='f49fe0e86ffe89109ad1d3549f1b9d46faa075ccb7354bdd1272007ed95a7216'
for v in (1,7,31):
 n=f'TWELVE_NEW_FORCED_HALL_union_remaining_v{v}.bin';assert sha(n)==source['audited_input_hashes'][n].removeprefix('sha256:')
out={'status':'PASS','selected_indices':selected,'local_manifest_sha256':sha('TWELVE_EXTRA_TYPES_LOCAL_MANIFEST.json'),'application_manifest_sha256':sha('TWELVE_EXTRA_TYPES_APPLICATION_MANIFEST.json'),'source_final_PASS_review_sha256':sha('TWELVE_NEW_FORCED_HALL_REVIEW.json'),'frozen_hashes':allhash,'local_marked_rows':reg['rows']}
(R/'TWELVE_EXTRA_TYPES_REVIEW_prepare.json').write_text(json.dumps(out,indent=2)+'\n');print({'status':'PASS','unique_frozen_hashes':len(allhash),'selected':selected})
