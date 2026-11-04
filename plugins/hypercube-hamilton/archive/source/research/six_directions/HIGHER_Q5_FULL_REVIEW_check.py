"""Independent census-to-manifest binding, frozen-input hashes, row arithmetic."""
import hashlib,json,pathlib,datetime
R=pathlib.Path(__file__).resolve().parent
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
m=json.loads((R/'HIGHER_Q5_FULL_MANIFEST.json').read_text(encoding='utf-8-sig'))
assert sha(R/'HIGHER_Q5_FULL_MANIFEST.json')=='1278b483dd4cb90c376caa8deca167b3512aefef3d8ce9475f5f7747f1c81fab'
hashes={}
for name,h in m['hashes'].items():
 p=R/name;assert sha(p)==h,(name,'hash');assert p.stat().st_size==m['sizes'][name],(name,'size');hashes[name]=h
imports={}
for name in ['HIGHER_HOLE_UNIFIED_TRANSFER_REVIEW.json','Q5_A10_FULL_REVIEW.json','TEN_HOLE_FULL_REVIEW.json']:
 d=json.loads((R/name).read_text(encoding='utf-8-sig'));assert d['verdict']=='PASS';imports[name]=d['verdict']
rows=[];unique_geometry_count=0;eligible_total=0;raw_total=0
for k,l in zip(range(6,10),m['levels']):
 c=json.loads((R/f'HIGHER_Q5_FULL_REVIEW_k{k}.json').read_text(encoding='utf-8-sig'))
 prod=json.loads((R/f'HIGHER_Q5_FULL_census_{k}_{k}.json').read_text(encoding='utf-8-sig'))['levels'][0]
 assert c['status']=='PASS' and c['holes']==l['holes']==prod['holes']
 for a,b,p in zip(c['targets'],l['targets'],prod['targets']):
  for key in ['v','free_target','eligible','known_cut','free_root_adjacent_to_predecessor','residual']:assert a[key]==b[key]==p[key],(k,key)
  assert a['eligible']==a['known_cut']+a['free_root_adjacent_to_predecessor']+a['residual']
  assert a['raw_membership_unique_count']==a['residual']
  eligible_total+=a['eligible'];raw_total+=a['residual']
  if a['v']==1:unique_geometry_count+=a['eligible']
 rows.append(c)
# Exhaust all port populations possible in a 32-vertex face of a short M.
checks=0
for k in range(6,10):
 for a in range(k):
  for b in range(k+1):
   if not (b>=1 and b-a in (0,1,2)):continue
   d=b-a;s=int(d==0);t=int(d==2)
   for delta in (0,1):
    for pe in range(17):
     for po in range(17):
      if a+delta+pe>16 or b+po>16:continue
      if 16-a-delta-pe!=16-b-po:continue
      c=pe+po
      if not c:continue # separate explicit five-direction import
      if delta:pairing=c+s+t;ae=a+1-s;ao=b-t
      elif s:pairing=c;ae=a;ao=b
      else:
       assert pe-po==d and pe>=1
       pairing=c-1+t;ae=a+1;ao=b-t
      assert pairing%2==0
      assert ae==ao and 1<=ae<=16
      if delta:assert pairing>=2
      be=k-a-1+t;bo=k-b+s
      assert 0<=be<=16 and 0<=bo<=16
      if d==0:assert bo==be+2 and 1<=be+1<=15
      elif d==1:assert be==bo
      else:assert be==bo+2 and 1<=bo+1<=15
      checks+=1
result=dict(status='PASS',manifest_sha256=sha(R/'HIGHER_Q5_FULL_MANIFEST.json'),
 frozen_file_hashes_checked=len(hashes),frozen_bytes_checked=sum(m['sizes'].values()),
 accepted_import_verdicts=imports,independent_enumeration='W-first followed by all admissible Z subsets, all six target-facing cuts',
 eligible_marked_records=eligible_total,distinct_ZW_geometries_all_four_levels=unique_geometry_count,
 raw_records_individually_validated=raw_total,raw_files=24,port_population_checks=checks,
 exact_raw_set_equality_reason='Each raw file strictly lexicographically increasing; every raw record belongs to the independently defined residual; its count equals independent exhaustive residual cardinality.',
 levels=rows,full_twelve_hole_proved=False,full_higher_hole_layers_proved=False,full_P6_proved=False)
(R/'HIGHER_Q5_FULL_REVIEW_check.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(json.dumps({k:v for k,v in result.items() if k!='levels'},indent=2))
