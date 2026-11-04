"""Independent final P6 assembly binding/DAG and finite logic checks.

Imports semantic and large finite local proofs at their explicitly audited scopes;
does not execute producers or treat mutable research ledgers as premises.
"""
from pathlib import Path
import hashlib, itertools, json, re, sys
R=Path(__file__).resolve().parent
FINAL='--final' in sys.argv
GATES=['GENERAL_NEAR_PERFECT_REVIEW.json','FOUR_HOLE_SOL_HIGH_REVIEW.json',
 'SIX_HOLE_CLOSURE_CONSEQUENCES_REVIEW.json','EIGHT_HOLE_FULL_REVIEW.json',
 'TEN_HOLE_FULL_REVIEW.json','TWELVE_HOLE_FULL_REVIEW.json','ROOTED_RANGE_REVIEW.json']
if FINAL:GATES+=['FOURTEEN_HOLE_FULL_REVIEW.json','SIXTEEN_EIGHTEEN_FULL_REVIEW.json']
cache={};checked={};nodes={};edges=[];errors=[];aux=[];legacy=[]
def read(n):return json.loads((R/n).read_text('utf-8-sig'))
def sha(n):
 p=(R/n).resolve();s=p.stat();key=(str(p),s.st_size,s.st_mtime_ns)
 if key not in cache:
  h=hashlib.sha256()
  with p.open('rb') as f:
   for b in iter(lambda:f.read(8*1024*1024),b''):h.update(b)
  cache[key]=h.hexdigest()
 return cache[key]
def bind(owner,n,v):
 if not isinstance(v,str) or not re.fullmatch(r'(sha256:)?[0-9a-fA-F]{64}',v):
  errors.append([owner,n,'invalid hash',v]);return
 try:a=sha(n)
 except OSError as e:errors.append([owner,n,'unreadable',str(e)]);return
 checked[n]=a
 if a!=v.removeprefix('sha256:').lower():errors.append([owner,n,'stale',v,a])
def path_for(d,n):
 if (R/n).is_file():return n
 t=d.get('trace_path','')
 if t and (R/t/n).is_file():return str(Path(t)/n)
 return n
def maps(owner,d):
 out={}
 for k in ('audited_input_hashes','imported_dependency_hashes','checker_artifact_hashes'):
  for n,v in d.get(k,{}).items():
   if n in out and out[n].removeprefix('sha256:')!=v.removeprefix('sha256:'):
    errors.append([owner,n,'conflicting hash'])
   out[n]=v
 for i in d.get('formal_imports',[]):out[i['file']]=i['sha256']
 return out
def evidence(owner,d):
 # Nested legacy accepted_import_source_and_evidence_hashes maps have report
 # names as containers; these keys are not themselves file-hash pairs.
 def walk(x,field):
  if not isinstance(x,dict):return
  for n,v in x.items():
   if isinstance(v,dict):walk(v,field);continue
   if isinstance(v,str) and re.fullmatch(r'(sha256:)?[0-9a-fA-F]{64}',v):
    if n in ('sha256','hash'):continue
    if n.endswith('_sha256') or n=='report_hash':
     base=n.removesuffix('_sha256').removesuffix('_hash')
     if isinstance(x.get(base),str) and (R/path_for(d,x[base])).is_file():
      bind(owner,path_for(d,x[base]),v);aux.append([owner,field,x[base]]);continue
     matches=[p for p,h in maps(owner,d).items() if h.removeprefix('sha256:')==v.removeprefix('sha256:')]
     if matches:
      for p in matches:bind(owner,p,v)
      legacy.append([owner,field,n,'digest alias resolved',matches]);continue
    p=path_for(d,n)
    # Generic producer-comparison schemas may use descriptive labels. Record
    # them explicitly, never pretend these labels are filenames.
    if '.' not in Path(n).name and not (R/p).is_file():
     legacy.append([owner,field,n,'nonpath digest metadata']);continue
    bind(owner,p,v);aux.append([owner,field,p])
 for field in ('audit_artifact_hashes','evidence_hashes','evidence',
   'accepted_import_source_bindings','accepted_import_source_and_evidence_hashes',
   'optional_certificate_hashes','producer_comparison_hashes'):
  walk(d.get(field),field)
 h=d.get('report_hash',d.get('report_sha256'))
 if h:
  p=d.get('trace_path') or owner.removesuffix('.json')+'.md'
  if (R/p).is_dir():p=str(Path(p)/(Path(owner).stem+'.md'))
  bind(owner,p,h)
visiting=set();visited=set()
def visit(n):
 if n in visiting:errors.append(['cycle',n]);return
 if n in visited:return
 visiting.add(n);d=read(n);nodes[n]=d
 status=d.get('verdict',d.get('status'))
 if status!='PASS' and not (n=='R4_DOUBLE_BRIDGE_REVIEW.json' and status=='PASS_WITH_SCOPE_LIMITS'):
  errors.append([n,'not accepted',status])
 evidence(n,d)
 for p,h in maps(n,d).items():
  bind(n,p,h)
  if p.endswith('_MANIFEST.json'):
   manifest=read(p)
   for field in ('input_hashes','output_hashes'):
    for q,z in manifest.get(field,{}).items():bind(p,q,z)
  if Path(p).name.endswith('_REVIEW.json') and p!=n:
   edges.append([n,p]);visit(p)
 visiting.remove(n);visited.add(n)
for n in GATES:visit(n)
assert sha('P6_FULL_CLOSURE.md')=='657bdbfc07f14210cde5a8afe1090fc49deb240a88738bc7e0e0f811a81474df'
for a,b in edges:
 if b=='R4_DOUBLE_BRIDGE_REVIEW.json':
  assert a in ('T15_CORE4_FULL_REVIEW.json','T15_CORE24_FULL_REVIEW.json','EIGHT_HOLE_FULL_REVIEW.json')
  for c in (4,24):
   t=(R/f'T15_CORE{c}_FULL_REVIEW.md').read_text('utf-8')
   assert 'PASS_WITH_SCOPE_LIMITS' in t and 'discharged' in t
assert 'A6_CONSEQUENCES_STATE_REVIEW.json' not in visited
assert not any(Path(k).name in ('RUN_STATE.json','PROOF_CHECK_STATE.json') for k in checked)
# Entire opposite-parity ordered endpoint domain admits one common invertible
# translation/permutation; check every endpoint pair and all cube adjacencies.
npairs=0
for u in range(64):
 for v in range(64):
  if (u^v).bit_count()%2==0:continue
  one=[i for i in range(6) if (u^v)>>i&1]
  order=one+[i for i in range(6) if i not in one]
  def f(x):return sum((((x^u)>>i)&1)<<j for j,i in enumerate(order))
  assert f(u)==0 and f(v) in (1,7,31)
  assert len({f(x) for x in range(64)})==64
  assert all((f(x)^f(x^(1<<i))).bit_count()==1 for x in range(64) for i in range(6))
  npairs+=1
assert npairs==2048
# Independent sanity check of the rooted range's extremal witness (not an
# empirical substitute for the universal imported >=24 theorem).
w=read('rooted_23_matching.json')
root=w.get('root',0);m=w.get('matching',w.get('edges'))
assert len(m)==23
covered=[x for e in m for x in e]
assert len(set(covered))==46 and root not in covered
assert all((a^b).bit_count()==1 for a,b in m)
free=set(range(64))-set(covered)
addable=[(a,a^(1<<i)) for a in free for i in range(6) if a<(a^(1<<i)) and (a^(1<<i)) in free]
assert len(free)==18 and len(addable)==6 and all(root in e for e in addable)
for a,b in addable:
 remainder=free-{a,b}
 assert not any((x^(1<<i)) in remainder for x in remainder for i in range(6))
# Counts forced by root preservation and the literature lower bound.
assert [64-2*k for k in range(31,22,-1)]==list(range(2,19,2))
if FINAL:
 p=nodes['FOURTEEN_HOLE_FULL_REVIEW.json']['details']
 assert p['full_fourteen_hole_proved'] is True
 p=nodes['SIXTEEN_EIGHTEEN_FULL_REVIEW.json']['details']
 assert p['full_sixteen_hole_proved'] is True and p['full_eighteen_hole_proved'] is True
 # A complete predecessor discharges the exact conditional implication; old
 # immutable local reports saying 'not established' describe their own date.
 for n in ('FOURTEEN_HOLE_FULL_REVIEW.json','SIXTEEN_EIGHTEEN_FULL_REVIEW.json'):
  t=(R/n.replace('.json','.md')).read_text('utf-8')
  assert 'covered' in t and ('predecessor' in t or 'conditional' in t)
 b=maps('full16',nodes['SIXTEEN_EIGHTEEN_FULL_REVIEW.json'])
 assert b['FOURTEEN_HOLE_FULL_REVIEW.json'].removeprefix('sha256:')==sha('FOURTEEN_HOLE_FULL_REVIEW.json')
 # Independently compare exact final14 orbit set and final16 complementary
 # certificates' retained sets; cardinality addition is insufficient.
 z=(39,43,45,51,53,57)
 def image(x,p):return sum(((x>>i)&1)<<p[i] for i in range(6))
 orbits=[]
 for w in ((1,2,4,8,14,16,32),(1,2,4,8,16,32,62)):
  orbits.append({tuple(sorted(image(x,p+(5,)) for x in z))+tuple(sorted(image(x,p+(5,)) for x in w)) for p in itertools.permutations(range(5))})
 def records(n,width):
  data=(R/n).read_bytes();assert len(data)%width==0
  ans=[data[i:i+width] for i in range(0,len(data),width)]
  assert len(ans)==len(set(ans));return set(ans)
 assert list(map(len,orbits))==[20,5] and not orbits[0]&orbits[1]
 assert records('FOURTEEN_MID_SELECTED_remaining_v31_covered.bin',13)=={bytes(x) for x in orbits[0]|orbits[1]}
 for v in (1,7,31):
  source=records(f'SIXTEEN_LOCAL_remaining_v{v}_covered.bin',15)
  star=records(f'SIXTEEN_STAR_remaining_v{v}_covered.bin',15)
  small=records(f'SIXTEEN_SMALLCUT_remaining_v{v}_covered.bin',15)
  assert star|small==source and not star&small
 assert 80805==73605+7050+150
for n in ('TEN_HOLE_FULL_REVIEW.json','TWELVE_HOLE_FULL_REVIEW.json'):
 p=nodes[n]['details'];assert p['covered_targets_included']
 assert p['remaining_covered_target_geometries']==p['remaining_free_target_geometries']==0
result={'stage':'final' if FINAL else 'prefinal','errors':errors,'gates':{n:sha(n) for n in GATES},
 'frozen_P6_proof_hash':sha('P6_FULL_CLOSURE.md'), 'bound_files_rehashed':len(checked),
 'transitive_review_nodes':len(visited),'report_dependency_edges':len(edges),
 'dependency_DAG_acyclic':not any(x[0]=='cycle' for x in errors),
 'review_nodes':sorted(visited),'review_edges':edges,'evidence_bindings':len(aux),
 'legacy_nonpath_digest_metadata':legacy,'live_mutable_ledgers_used':False,
 'ordered_opposite_parity_pairs_checked':npairs,'rooted_witness_independently_checked':True,
 'large_local_certificate_computations_rerun':False,'producer_code_executed':False}
(R/'P6_FULL_REVIEW_check.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(json.dumps({k:v for k,v in result.items() if k not in ('review_nodes','review_edges')},indent=2))
assert not errors,errors
