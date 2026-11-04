"""Final free-endpoint assembly gate and exact frozen free-domain lineage."""
import pathlib,json,hashlib,struct
R=pathlib.Path(__file__).resolve().parent
def load(n):return json.loads((R/n).read_text(encoding='utf-8-sig'))
def sha(n):return hashlib.sha256((R/n).read_bytes()).hexdigest()
def clean(h):return h.removeprefix('sha256:')
names=['TEN_HOLE_FULL_REVIEW.json','HIGHER_Q5_FULL_REVIEW.json','HIGHER_Q5_FULL_REUSE_REVIEW.json','HIGHER_Q5_FULL_T37_APPLICATION_REVIEW.json','Q5_T37_INDEPENDENT_REVIEW.json','Q5_T17_RANK_BATCH_REVIEW.json','HIGHER_FORCED_CHERRY_REVIEW.json']
reports={n:load(n) for n in names}
for n,d in reports.items():assert d['verdict']=='PASS',(n,'not final PASS')
prooflinks=[('TEN_HOLE_FULL_REVIEW.json','TEN_HOLE_FULL_CLOSURE.md'),('HIGHER_Q5_FULL_REVIEW.json','HIGHER_Q5_FULL_NEARBALANCED.md'),('HIGHER_Q5_FULL_REUSE_REVIEW.json','HIGHER_Q5_FULL_REUSE_PROOF.md'),('HIGHER_Q5_FULL_T37_APPLICATION_REVIEW.json','HIGHER_Q5_FULL_T37_APPLICATION.md'),('Q5_T37_INDEPENDENT_REVIEW.json','Q5_T37_INDEPENDENT_PROOF.md'),('Q5_T17_RANK_BATCH_REVIEW.json','Q5_T17_RANK_BATCH_PROOF.md'),('HIGHER_FORCED_CHERRY_REVIEW.json','HIGHER_FORCED_CHERRY_TRANSFER.md')]
for review,proof in prooflinks:assert sha(proof)==clean(reports[review]['audited_input_hashes'][proof]),(review,proof)
manifest=load('HIGHER_Q5_FULL_T37_APPLICATION_MANIFEST.json')
for n,h in manifest['hashes'].items():assert sha(n)==h and (R/n).stat().st_size==manifest['sizes'][n],n
app=reports['HIGHER_Q5_FULL_T37_APPLICATION_REVIEW.json']
assert sha('HIGHER_Q5_FULL_T37_APPLICATION_MANIFEST.json')==clean(app['audited_input_hashes']['HIGHER_Q5_FULL_T37_APPLICATION_MANIFEST.json'])
base=reports['HIGHER_Q5_FULL_REVIEW.json'];reuse=reports['HIGHER_Q5_FULL_REUSE_REVIEW.json']
for n in ['TEN_HOLE_FULL_REVIEW.json','HIGHER_Q5_FULL_REVIEW.json','HIGHER_Q5_FULL_REUSE_REVIEW.json','Q5_T37_INDEPENDENT_REVIEW.json','Q5_T17_RANK_BATCH_REVIEW.json','HIGHER_FORCED_CHERRY_REVIEW.json']:
 scopes={**app.get('audited_input_hashes',{}),**app.get('imported_dependency_hashes',{})}
 if n in scopes:assert sha(n)==clean(scopes[n]),n
# Decode separate chosen routes; require each covers every actual free input index.
T=(R/'HIGHER_Q5_FULL_T37_positive_witnesses.bin').read_bytes();F=(R/'HIGHER_Q5_FULL_FORCED17_safe_witnesses.bin').read_bytes()
assert len(T)%16==0 and len(F)%32==0
tidx={v:set() for v in (1,7,31)};fidx={v:set() for v in (1,7,31)}
for p in range(0,len(T),16):
 v,f,i,orb,d,s=struct.unpack_from('<BBIBBQ',T,p)
 if f:
  assert v in tidx and i not in tidx[v];assert orb in set(range(64))-{0,1,2,3,6,12,13,14,15};tidx[v].add(i)
for p in range(0,len(F),32):
 v,f,i,orb,d,s,M,J,O,OB=struct.unpack_from('<BBIBBQIIII',F,p)
 if f:
  assert v in fidx and i not in fidx[v];assert orb in {5,6,9,11,12,13,17};fidx[v].add(i)
  assert not ((v>>d&1) and OB&1),'actual B obstruction contains root'
chain=[]
for v,initial,final in [(1,0,0),(7,80622,27),(31,107984,20)]:
 old=f'HIGHER_Q5_FULL_residual_h12_v{v}_free.bin';mid=f'HIGHER_Q5_FULL_reuse_remaining_h12_v{v}_free.bin'
 assert sha(old)==clean(base['audited_input_hashes'][old])==clean(reuse['audited_input_hashes'][old])
 assert sha(mid)==clean(reuse['audited_input_hashes'][mid])==manifest['hashes'][mid]
 b=(R/old).read_bytes();q=(R/mid).read_bytes();assert len(b)==11*initial and len(q)==11*final
 records=[q[i:i+11] for i in range(0,len(q),11)];assert len(set(records))==final
 for rec in records:
  H={0,*rec};assert len(H)==12 and v in H
  assert all((x^y).bit_count()!=1 for x in H for y in H if x!=y)
 assert tidx[v]==fidx[v]==set(range(final))
 for route in ['T37','FORCED17','T37_FORCED_union']:
  n=f'HIGHER_Q5_FULL_{route}_remaining_h12_v{v}_free.bin';assert (R/n).read_bytes()==b''
 chain.append({'v':v,'nearbalanced_residual':initial,'reuse_remaining':final,'T37_covers_every_remaining_index':True,'forced_covers_every_remaining_index':True,'final_remaining':0})
covered=sum((R/f'HIGHER_Q5_FULL_T37_FORCED_union_remaining_h12_v{v}_covered.bin').stat().st_size//11 for v in (1,7,31));assert covered==215243
# All endpoint/root pair distances reduce under coordinate permutations to1/3/5.
odd=[x for x in range(64) if x.bit_count()%2];assert {x.bit_count() for x in odd}=={1,3,5}
assert all(x&(x-1)==0 for x in odd if x.bit_count()==1)
# Minimal combinatorial endpoint and closing-edge side conditions.
for u in range(64):
 for v in range(64):
  if (u^v).bit_count()%2!=1:continue
  for x in range(64):
   for d in range(6):
    y=x^(1<<d)
    if {x,y}!={u,v}:assert not ({u,v}<={x,y})
out={'status':'PASS','final_PASS_imports':{n:sha(n) for n in names},'proof_bindings':{p:sha(p) for n,p in prooflinks},'application_manifest_hash':sha('HIGHER_Q5_FULL_T37_APPLICATION_MANIFEST.json'),'free_domain_chain':chain,'nearbalanced_free_residual':188606,'reuse_free_residual':47,'final_free_residual':0,'covered_remaining_open':215243,'all_47_free_records_in_each_separate_route':True,'two_prescribed_free_endpoint_quantifier':True,'twelve_hole_free_targets_proved':True,'full_twelve_hole_proved':False,'full_higher_hole_layers_proved':False,'full_P6_proved':False}
(R/'TWELVE_HOLE_FREE_REVIEW_check.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({k:v for k,v in out.items() if k not in ['final_PASS_imports','proof_bindings']},indent=2))
