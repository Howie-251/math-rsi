"""Independent full14 assembly checker. Reads evidence; executes no producer code.

Finite local proofs are imported only at their audited scopes. This checker
checks live bindings, review DAG, exact stream interfaces and final orbit set;
it does not claim to repeat the imported connectivity/census computations.
"""
import hashlib,itertools,json,pathlib,sys
R=pathlib.Path(__file__).resolve().parent
FINAL='--final' in sys.argv
NAMES=['HIGHER_Q5_FULL','FOURTEEN_REUSE','FOURTEEN_CACHED','FOURTEEN_HALL',
 'FOURTEEN_FORCED','FOURTEEN_MAXIMAL_A','FOURTEEN_STAR_EXPANDED',
 'FOURTEEN_STAR_B_GLOBAL35','FOURTEEN_MID_SELECTED']
if FINAL: NAMES+=['FOURTEEN_FINAL25']
GATES=['TWELVE_HOLE_FULL_REVIEW.json']+[x+'_REVIEW.json' for x in NAMES]
cache={};errors=[];checked={};nodes={};edges=[];scoped=[];extra_bindings=[]
def read(n):return json.loads((R/n).read_text('utf-8-sig'))
def sha(n):
 p=(R/n).resolve();key=str(p)
 if key not in cache:
  h=hashlib.sha256()
  with p.open('rb') as f:
   for b in iter(lambda:f.read(2**20),b''):h.update(b)
  cache[key]=h.hexdigest()
 return cache[key]
def bind(owner,n,v):
 try: actual=sha(n)
 except OSError as e: errors.append([owner,n,'missing',str(e)]);return
 checked[n]=actual
 if actual!=v.removeprefix('sha256:'):errors.append([owner,n,'stale',v,actual])
def bindings(d):
 out={}
 for field in ('audited_input_hashes','imported_dependency_hashes','checker_artifact_hashes'):
  for n,v in d.get(field,{}).items():
   if n in out and out[n].removeprefix('sha256:')!=v.removeprefix('sha256:'):
    errors.append(['conflicting declared hashes',field,n])
   out[n]=v
 for imp in d.get('formal_imports',[]):
  n,v=imp['file'],imp['sha256']
  if n in out and out[n].removeprefix('sha256:')!=v.removeprefix('sha256:'):
   errors.append(['conflicting formal import hash',n])
  out[n]=v
 if d.get('report_hash') and d.get('trace_path'):out[d['trace_path']]=d['report_hash']
 return out
def auxiliary_bindings(owner,d):
 # These fields bind audit evidence/historical source bytes, not additional
 # accepted theorem premises. In particular a historical partial review need
 # not itself be PASS to serve as source evidence of a later complete proof.
 for field in ('audit_artifact_hashes','evidence_hashes','accepted_import_source_bindings'):
  for n,v in d.get(field,{}).items():
   q=n
   if not (R/q).exists() and d.get('trace_path'):
    q=str(pathlib.Path(d['trace_path'])/n)
   bind(owner,q,v);extra_bindings.append([owner,field,q])
 if d.get('report_sha256'):
  q=d.get('trace_path') or owner.removesuffix('.json')+'.md'
  bind(owner,q,d['report_sha256']);extra_bindings.append([owner,'report_sha256',q])
visiting=set();visited=set()
def visit(n):
 if n in visiting:errors.append(['cycle',n]);return
 if n in visited:return
 visiting.add(n);d=read(n);nodes[n]=d
 auxiliary_bindings(n,d)
 status=d.get('verdict',d.get('status'))
 if status!='PASS':
  if n=='R4_DOUBLE_BRIDGE_REVIEW.json' and status=='PASS_WITH_SCOPE_LIMITS':
   scoped.append(n)
  else:errors.append([n,'nonPASS',status])
 for k,v in bindings(d).items():
  bind(n,k,v)
  if k.endswith('_REVIEW.json'):
   edges.append([n,k]);visit(k)
 visiting.remove(n);visited.add(n)
for n in GATES:visit(n)
bind('full14 frozen submission','FOURTEEN_HOLE_FULL_CLOSURE.md',
 'cb9aabaa99b1e20d9cce366f5723c9527d1e5d357af1b3efa3632f6dc079ed26')
# Restricted bridge import: only callers whose complete-core audit explicitly
# discharges the actual nonzero bridge-label exclusion may use this scope.
allowed={'T15_CORE4_FULL_REVIEW.json','T15_CORE24_FULL_REVIEW.json','EIGHT_HOLE_FULL_REVIEW.json'}
for a,b in edges:
 if b=='R4_DOUBLE_BRIDGE_REVIEW.json':
  if a not in allowed:errors.append([a,b,'restricted-scope not discharged'])
  for c in (4,24):
   text=(R/f'T15_CORE{c}_FULL_REVIEW.md').read_text('utf-8')
   assert 'PASS_WITH_SCOPE_LIMITS' in text and 'discharged' in text
assert sha('TWELVE_HOLE_FULL_REVIEW.json')=='405b019235810d8df75d58354b10c6d8ed42c1129a942940311555277a9382ce'
pred=read('TWELVE_HOLE_FULL_REVIEW.json')['details']
assert pred['full_twelve_hole_proved'] and pred['covered_targets_included']
assert pred['uniform_over_every_realizing_original_short_matching']
assert pred['remaining_covered_target_geometries']==pred['remaining_free_target_geometries']==0
# Scope checks supplement the live hashes: a numerical complement alone is
# insufficient unless each imported positive theorem quantifies over actual M.
for gate in NAMES:
 d=read(gate+'_REVIEW.json')['details']
 if gate in ('HIGHER_Q5_FULL','FOURTEEN_HALL','FOURTEEN_FINAL25'):continue
 assert d['every_realizing_original_short_matching_quantifier'] is True,gate
for gate in ('FOURTEEN_REUSE','FOURTEEN_CACHED'):
 d=read(gate+'_REVIEW.json')['details']
 assert d['source_reduction_conditional_on_full_twelve_hole'] is False
 assert d['full_twelve_hole_predecessor_sha256']==sha('TWELVE_HOLE_FULL_REVIEW.json')
hall=read('FOURTEEN_HALL_REVIEW.json')['details']
assert hall['fourteen_hole_free_targets_proved']
assert hall['free_predecessor_augmentation_including_uv_special_case_checked']
assert hall['every_realizing_original_short_matching_quantifier_checked']
assert read('FOURTEEN_FORCED_REVIEW.json')['details']['actual_compressed_L_plus_R_acyclicity_proved']
assert read('FOURTEEN_MAXIMAL_A_REVIEW.json')['details']['universal_submatching_lift_proved']
assert read('FOURTEEN_STAR_EXPANDED_REVIEW.json')['details']['finite_A_certificates_verified']==574944
assert read('FOURTEEN_MID_SELECTED_REVIEW.json')['details']['accepted_local_indices']==[1,15,44]
if FINAL:
 bind('full14 final subset','FOURTEEN_FINAL25_REVIEW.json',
  '00b922b664e81b499b3e231252fbee8393f2436e14388c6e8e2ee88432cc4ae7')
 d=read('FOURTEEN_FINAL25_REVIEW.json')['details']
 assert d['every_realizing_original_short_matching_quantifier']
 assert d['maximal_A_domain_by_orbit']==[291743,513263]
 assert d['positive_A_records']==805006
 assert d['complete_domain_by_independent_DP_and_legal_unique_equal_cardinality']
 for field in ('orbit1_mandatory_even30_internal_coverage',
  'Lprime_subset_Lstarprime_all_three_cases',
  'actual_virtual_w63_retained_in_both_crossing_cases',
  'maximal_added_mate_used_only_as_deleted_completion',
  'actual_compressed_B_forced_pair_absence_proved','all_remaining_streams_byte_exact'):
  assert d[field],field
 assert d['actual_geometry_orbit_counts']==[20,5]
 assert d['actual_witnesses_checked']==25 and d['remaining_by_target']==[0,0,0]
# Explicitly verify that all ordered opposite-parity endpoint pairs normalize
# to exactly one of the three target weights, with an invertible cube map.
normalized_pairs=0
for u in range(64):
 for v in range(64):
  if (u.bit_count()-v.bit_count())%2==0:continue
  diff=u^v;bits=[i for i in range(6) if diff>>i&1]
  order=bits+[i for i in range(6) if not diff>>i&1]
  out=lambda x:sum((((x^u)>>k)&1)<<j for j,k in enumerate(order))
  assert out(u)==0 and out(v)==(1<<len(bits))-1 in (1,7,31)
  assert len({out(x) for x in range(64)})==64
  assert all((out(x)^out(x^(1<<k))).bit_count()==1 for x in range(64) for k in range(6))
  normalized_pairs+=1
assert normalized_pairs==2048
# Expand only manifests directly bound by the assembly gates; ancillary producer
# observations in manifests are bytes, never additional theorem premises.
bound_by={}
for n in GATES:
 b=bindings(read(n));expanded=dict(b)
 for k in list(b):
  if k.endswith('_MANIFEST.json'):
   m=read(k)
   for f in ('input_hashes','output_hashes'):
    for q,v in m.get(f,{}).items():bind(k,q,v);expanded[q]=v
 bound_by[n]=expanded
stages=[('HIGHER_Q5_FULL','HIGHER_Q5_FULL_residual_h14',9252401,232042),
 ('FOURTEEN_REUSE','FOURTEEN_REUSE_remaining_h14',47893,318),
 ('FOURTEEN_CACHED','FOURTEEN_CACHED_remaining_h14',12528,18),
 ('FOURTEEN_HALL','FOURTEEN_HALL_remaining',3923,0),
 ('FOURTEEN_FORCED','FOURTEEN_FORCED_remaining',2587,0),
 ('FOURTEEN_MAXIMAL_A','FOURTEEN_RESIDUAL_STRUCTURE_maxA_remaining',2527,0),
 ('FOURTEEN_STAR_EXPANDED','FOURTEEN_STAR_EXPANDED_remaining',2407,0),
 ('FOURTEEN_STAR_B_GLOBAL35','FOURTEEN_STAR_B_GLOBAL35_remaining',2287,0),
 ('FOURTEEN_MID_SELECTED','FOURTEEN_MID_SELECTED_remaining',25,0)]
if FINAL:stages += [('FOURTEEN_FINAL25','FOURTEEN_FINAL25_remaining',0,0)]
interfaces=[];counts=[]
for i,(gate,prefix,nc,nf) in enumerate(stages):
 totals={'covered':0,'free':0}
 for status in ('covered','free'):
  if i>=4 and status=='free':continue # zero free branch proved at Hall
  for v in (1,7,31):
   f=f'{prefix}_v{v}_{status}.bin';data=(R/f).read_bytes()
   assert len(data)%13==0
   totals[status]+=len(data)//13
   own=bound_by[gate+'_REVIEW.json'];assert own[f]==sha(f)
   if i+1<len(stages):
    nxt=bound_by[stages[i+1][0]+'_REVIEW.json']
    if status=='free' and i>=3:continue
    assert nxt[f]==own[f],(gate,stages[i+1][0],f)
    interfaces.append([gate,stages[i+1][0],f,sha(f),len(data)//13])
 assert (totals['covered'],totals['free'])==(nc,nf)
 counts.append({'gate':gate,'covered':nc,'free':nf})
# Reconstruct both complete marked target-stabilizer orbits independently.
z=(39,43,45,51,53,57);ws=[(1,2,4,8,14,16,32),(1,2,4,8,16,32,62)]
def image(x,p):return sum(((x>>i)&1)<<p[i] for i in range(6))
orbits=[]
for w in ws:
 o=set()
 for p5 in itertools.permutations(range(5)):
  p=p5+(5,);assert image(0,p)==0 and image(31,p)==31
  o.add(tuple(sorted(image(x,p) for x in z))+tuple(sorted(image(x,p) for x in w)))
 orbits.append(o)
assert list(map(len,orbits))==[20,5] and not orbits[0]&orbits[1]
data=(R/'FOURTEEN_MID_SELECTED_remaining_v31_covered.bin').read_bytes()
records=[tuple(data[i:i+13]) for i in range(0,len(data),13)]
assert len(records)==len(set(records))==25
assert set(records)==orbits[0]|orbits[1]
T={x^32 for x in z};assert 31 not in T and 30^32 in ws[1]
assert all(x.bit_count()%2==0 for x in z)
assert all(all(y.bit_count()%2==1 for y in w) for w in ws)
assert all(all((x^y).bit_count()!=1 for x in z for y in w) for w in ws)
# No backward theorem-dependency from the accepted full12 or local Q5 inputs
# to a full14/full16/full18/P6 theorem; all report edges are fully traversed.
for n in visited:
 if any(x in n for x in ('SIXTEEN_HOLE_FULL','EIGHTEEN_HOLE_FULL','FOURTEEN_HOLE_FULL')):
  errors.append([n,'unexpected full-higher premise'])
result={'stage':'final' if FINAL else 'prefinal','errors':errors,
 'direct_gates':{n:sha(n) for n in GATES},'all_live_bound_files_rehashed':len(checked),
 'transitive_review_nodes':len(visited),'report_dependency_edges':len(edges),
 'dependency_DAG_acyclic':not any(e[0]=='cycle' for e in errors),
 'theorem_dependency_fields':['audited_input_hashes','imported_dependency_hashes','checker_artifact_hashes','formal_imports'],
 'additional_evidence_binding_fields':['audit_artifact_hashes','evidence_hashes','accepted_import_source_bindings','report_sha256'],
 'additional_evidence_bindings_checked':len(extra_bindings),
 'binding_scope':'Declared bindings in named supported fields of traversed reviews, plus input/output hashes of directly bound gate manifests. Historical source/evidence bindings are byte checks, not extra theorem premises. This is not a claim to parse arbitrary nested schemas or repeat upstream finite proofs.',
 'restricted_bridge_scope_callers_checked':sorted(allowed),
 'exact_stream_interfaces':interfaces,'residual_chain':counts,
 'final_orbit_sizes':[20,5],'final_orbit_union_equals_exact25':True,
 'all_ordered_opposite_parity_endpoint_normalizations_checked':normalized_pairs,
 'full12_includes_covered_targets':True,'producer_code_executed':False,
 'large_imported_census_or_connectivity_checks_rerun':False,
 'full_fourteen_hole_proved':FINAL and not errors,'full_P6_proved':False}
(R/'FOURTEEN_HOLE_FULL_REVIEW_check.json').write_text(json.dumps(result,indent=2)+'\n','utf-8')
print(json.dumps({k:v for k,v in result.items() if k not in ('exact_stream_interfaces','direct_gates')},indent=2))
assert not errors,errors
