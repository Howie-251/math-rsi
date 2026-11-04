import pathlib,json,hashlib,collections
R=pathlib.Path(__file__).resolve().parent
def sha(n):return hashlib.sha256((R/n).read_bytes()).hexdigest()
def load(n):return json.loads((R/n).read_text(encoding='utf-8-sig'))
def mask(a):return sum(1<<x for x in a)
m=load('TWELVE_NEW_FORCED_MANIFEST.json');s=load('TWELVE_NEW_FORCED_summary.json')
for n,h in m['files'].items():assert sha(n)==h,n
assert len(m['files'])==249 and len(s['reports'])==s['count']==27
assert set(m['claimed_indices'])=={r['index'] for r in s['reports']} and len(m['claimed_indices'])==27
rows=[];types=collections.Counter()
for r in s['reports']:
 g=r['geometry'];M,J,O=map(set,(g['minority'],g['majority'],g['omitted']));H=M|J;K=set(range(32))-H;h=r['forced_hole'];p,q=r['forced_pair'];types[g['type']]+=1
 assert len(H)==10 and len(K)==22 and not M&J and O<=J and h in H-O and p in K and q in K
 assert all(x.bit_count()%2==0 for x in M) and all(x.bit_count()%2 for x in J)
 assert ({h^(1<<d) for d in range(5)}-O)=={p,q}
 assert (len(M),len(J),len(O))=={'T28':(2,8,3),'T19':(1,9,4)}[g['type']]
 assert r['rank']==512 and r['covered_endpoints']==22 and r['reduced_endpoints']==20
 assert r['forest_record_bytes']=={'T28':36,'T19':34}[g['type']]
 assert load(r['prefix']+'.json')==r
 config=list(map(int,(R/(r['prefix']+'_config.txt')).read_text().split()))
 assert config==sorted(H)+sorted(O)
 rows.append(f"{r['index']} {r['prefix']} {r['forest_record_bytes']} {mask(H)} {mask(O)} {h} {p} {q}\n")
(R/'TWELVE_NEW_FORCED_REVIEW_rows.txt').write_text(''.join(rows))
out={'status':'PASS','manifest_sha256':sha('TWELVE_NEW_FORCED_MANIFEST.json'),'frozen_hashes_checked':249,'types':dict(types),'claimed_indices':m['claimed_indices'],'exact_summary_config_and_metadata_rows_match':True,'all_available_cherry_neighbors_checked':True}
(R/'TWELVE_NEW_FORCED_REVIEW_prepare.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
