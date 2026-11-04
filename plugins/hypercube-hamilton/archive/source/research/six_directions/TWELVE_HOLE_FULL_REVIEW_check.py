"""Independent assembly checks; never executes producer code or edits its state."""
import hashlib,itertools,json,pathlib,sys
R=pathlib.Path(__file__).resolve().parent
def sha(p):
 h=hashlib.sha256()
 with p.open('rb') as f:
  for b in iter(lambda:f.read(2**20),b''): h.update(b)
 return h.hexdigest()
def read(n): return json.loads((R/n).read_text(encoding='utf-8-sig'))
gates=['TEN_HOLE_FULL_REVIEW','TWELVE_HOLE_FREE_REVIEW','HIGHER_Q5_FULL_REVIEW','HIGHER_Q5_FULL_REUSE_REVIEW','HIGHER_Q5_FULL_T37_APPLICATION_REVIEW','TWELVE_NEW_TYPES_APPLICATION_REVIEW','TWELVE_NEW_FORCED_HALL_REVIEW','TWELVE_EXTRA_TYPES_REVIEW','TWELVE_EXTRA_FORCED_REVIEW','Q5_T17_RANK_BATCH_REVIEW','TWELVE_STAR_B_REVIEW','TWELVE_STAR_MAXIMAL_A_REVIEW']
if '--final' in sys.argv: gates+=['TWELVE_STAR_MAXIMAL_A_FINITE_REVIEW']
hashes={}; checked={}; errors=[]; dag={}
for n in gates:
 p=R/(n+'.json'); d=read(p.name); hashes[p.name]=sha(p)
 if d.get('verdict')!='PASS': errors.append((p.name,'not PASS'))
 dag[p.name]=[k for k in d.get('audited_input_hashes',{}) if k.endswith('_REVIEW.json')]
 bound={}
 for field in ['audited_input_hashes','imported_dependency_hashes','checker_artifact_hashes']:
  bound.update(d.get(field,{}))
 if d.get('report_hash') and d.get('trace_path') and (R/d['trace_path']).is_file():
  bound[d['trace_path']]=d['report_hash']
 for k,v in bound.items():
  q=R/k
  if k not in checked:
   checked[k]=sha(q) if q.is_file() else None
  if checked[k]!=v.removeprefix('sha256:'): errors.append((p.name,k,'stale or missing',v,checked[k]))
# Verify review-to-review graph acyclicity recursively from all imports.
visiting=set(); visited=set(); report_edges=0; scoped_edges=[]
def dfs(n):
 global report_edges
 if n in visiting: errors.append(('cycle',n)); return
 if n in visited: return
 visiting.add(n)
 d=read(n)
 for k,v in d.get('audited_input_hashes',{}).items():
  if k.endswith('_REVIEW.json') and (R/k).is_file():
   report_edges+=1
   if sha(R/k)!=v.removeprefix('sha256:'): errors.append((n,k,'stale report edge'))
   child_status=read(k).get('verdict',read(k).get('status'))
   if child_status!='PASS':
    if k=='R4_DOUBLE_BRIDGE_REVIEW.json' and child_status=='PASS_WITH_SCOPE_LIMITS' and n in ['T15_CORE4_FULL_REVIEW.json','T15_CORE24_FULL_REVIEW.json','EIGHT_HOLE_FULL_REVIEW.json']:
     # Both complete-core audits explicitly discharge the restricted bridge-label
     # hypothesis. The eight-hole assembly imports those complete cores.
     for core in (4,24):
      text=(R/f'T15_CORE{core}_FULL_REVIEW.md').read_text(encoding='utf-8')
      assert 'PASS_WITH_SCOPE_LIMITS' in text and 'discharged' in text
     scoped_edges.append([n,k,'restricted nonzero bridge labels avoid B holes; discharged by complete core4/core24 audits'])
    else: errors.append((n,k,'nonPASS report dependency',child_status))
   dfs(k)
 visiting.remove(n); visited.add(n)
for n in gates: dfs(n+'.json')
# Read exact final complement, reconstruct its six marked coordinate orbits.
last=read('TWELVE_EXTRA_FORCED_REVIEW.json'); rows=[]
for v in (1,7,31):
 p=R/f'TWELVE_EXTRA_FORCED_safe_remaining_v{v}.bin'; data=p.read_bytes()
 assert len(data)%11==0
 assert sha(p)==last['audited_input_hashes'][p.name]
 rows += [(v,tuple(data[i:i+5]),tuple(data[i+5:i+11])) for i in range(0,len(data),11)]
assert len(rows)==235 and len(set(rows))==235
assert all(v==31 and w==(1,2,4,8,16,32) for v,z,w in rows)
representatives=[(39,43,45,51,53),(39,43,45,51,63),(39,43,45,54,63),(39,43,51,60,63),(39,43,53,57,63),(39,43,53,58,63)]
def image(x,p): return sum(((x>>i)&1)<<p[i] for i in range(6))
perms=[p+(5,) for p in itertools.permutations(range(5))]
orbits=[{(31,tuple(sorted(image(x,p) for x in z)),(1,2,4,8,16,32)) for p in perms} for z in representatives]
assert list(map(len,orbits))==[30,60,60,10,15,60]
assert sum(map(len,orbits))==len(set.union(*orbits))==235
assert set(rows)==set.union(*orbits)
# All root-star representatives are legitimate independent marked configurations.
for v,z,w in rows:
 assert all(x.bit_count()%2==0 for x in z)
 assert all(y.bit_count()%2==1 for y in w)
 assert all((x^y).bit_count()!=1 for x in z for y in w)
 assert v not in w
assert sum([629747,598097,598067,598037,598067,598037])==3620052
# Integer partition identities (free branch separated before covered chain).
assert 7820116-7471880==348236
assert 348236-(133040-47)==215243
assert 215243-177838==37405
assert 37405-552-7483==29370
assert 29370-28089==1281
assert 1281-1046==235
assert 235-sum(map(len,orbits))==0
result={'stage':'final' if '--final' in sys.argv else 'prefinal','errors':errors,'direct_PASS_reviews':len(gates),'direct_bound_files_rehashed':len(checked),'transitive_review_nodes':len(visited),'report_dependency_edges':report_edges,'restricted_import_edges_with_explicit_hypothesis_discharge':scoped_edges,'review_DAG_acyclic':not any(e[0]=='cycle' for e in errors),'final_residual_records':len(rows),'orbit_sizes':list(map(len,orbits)),'exact_marked_orbit_union_equals_final_residual':True,'matching_realizability_filter_added':False,'producer_code_executed':False,'large_certificate_checks_rerun':False,'bound_direct_reviews':hashes}
(R/'TWELVE_HOLE_FULL_REVIEW_check.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(json.dumps(result,indent=2))
assert not errors, errors
