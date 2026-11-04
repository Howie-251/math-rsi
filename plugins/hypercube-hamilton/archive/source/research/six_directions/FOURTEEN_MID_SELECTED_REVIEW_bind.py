import hashlib,json,pathlib
R=pathlib.Path(__file__).resolve().parent
def rd(n):return json.loads((R/n).read_text(encoding='utf-8-sig'))
def sha(n):
 h=hashlib.sha256()
 with (R/n).open('rb') as f:
  for b in iter(lambda:f.read(1<<20),b''):h.update(b)
 return h.hexdigest()
assert sha('FOURTEEN_MID_SELECTED_PROOF.md')=='2fb632aa4ba65d469c1790badcb3b815cd72ee840a5e787dd4d8cd383a00d282'
assert sha('FOURTEEN_MID_SELECTED_MANIFEST.json')=='399ec9d673724ff8202e3b546a1ee9e6be97cad3ddaaa1643dc0ea42b4871c93'
m=rd('FOURTEEN_MID_SELECTED_MANIFEST.json')
for n,v in m['files'].items():assert sha(n)==v['sha256'] and (R/n).stat().st_size==v['bytes'],n
source=rd('FOURTEEN_STAR_B_GLOBAL35_REVIEW.json');assert source['verdict']=='PASS' and source['details']['remaining_covered_target_geometries']==2287 and source['details']['fourteen_hole_free_targets_proved']
for v in (1,7,31):
 n=f'FOURTEEN_STAR_B_GLOBAL35_remaining_v{v}_covered.bin';assert sha(n)==source['audited_input_hashes'][n]
gates={};checked={}
for name in ['FOURTEEN_STAR_B_GLOBAL35_REVIEW.json']+[n for n in m['files'] if n.endswith('_REVIEW.json')]:
 d=rd(name);assert d['verdict']=='PASS';gates[name]=sha(name)
 for field in ['audited_input_hashes','imported_dependency_hashes','checker_artifact_hashes']:
  for n,h in d.get(field,{}).items():
   if n not in checked:checked[n]=sha(n)
   assert checked[n]==h.removeprefix('sha256:'),(name,n)
# Mathematical crosscheck of the new alternating-cycle traversal against
# direct labelled-union DSU on every pair of perfect matchings of4/6/8 labels.
def matchings(xs):
 if not xs:yield [];return
 a=xs[0]
 for b in xs[1:]:
  for rest in matchings([x for x in xs[1:] if x!=b]):yield [(a,b)]+rest
comparisons=0
for n in [4,6,8]:
 mm=list(matchings(list(range(n))))
 for P in mm:
  p=dict(P+[(b,a) for a,b in P])
  for F in mm:
   f=dict(F+[(b,a) for a,b in F]);parents=list(range(n))
   def root(x):
    while parents[x]!=x:x=parents[x]
    return x
   for a,b in P+F:parents[root(a)]=root(b)
   connected=len({root(x) for x in range(n)})==1
   x=0;period=0
   while True:
    x=f[p[x]];period+=1
    if x==0:break
   assert connected==(period==n//2);comparisons+=1
out={'status':'PASS','manifest_files_verified':len(m['files']),'formal_gate_hashes':gates,'direct_formal_source_bindings_verified':len(checked),'source_final_PASS_and_all_three_outputs_bound':True,'alternating_cycle_traversal_independent_DSU_small_cases':comparisons,'fourteen_hole_free_targets_proved':True,'full_fourteen_hole_proved':False,'full_P6_proved':False}
(R/'FOURTEEN_MID_SELECTED_REVIEW_bind.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8');print(json.dumps(out,indent=2))
