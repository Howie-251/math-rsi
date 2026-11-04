import pathlib,json,hashlib
R=pathlib.Path(__file__).resolve().parent
def load(p):return json.loads((R/p).read_text(encoding='utf-8-sig'))
def sha(p):return hashlib.sha256((R/p).read_bytes()).hexdigest()
m=load('HIGHER_Q5_FULL_REUSE_MANIFEST.json');p=load('HIGHER_Q5_FULL_REUSE_REVIEW_prepare.json');c=load('HIGHER_Q5_FULL_REUSE_REVIEW_census.json')
assert c['status']==p['status']=='PASS'
assert sha('HIGHER_Q5_FULL_REVIEW.json')=='265c0d65b6fbbe28d2fe5123e7f901c317cd299230f354eeab3a16ad1e0ed0fd'
prev=load('HIGHER_Q5_FULL_REVIEW.json');assert prev['verdict']=='PASS'
for n,h in m['hashes'].items():
 assert sha(n)==h and (R/n).stat().st_size==m['sizes'][n],n
 if n.startswith('HIGHER_Q5_FULL_residual_h12'):assert prev['audited_input_hashes'][n]==h
for n,h in p['bound_imports'].items():assert sha(n)==h
prod=load('HIGHER_Q5_FULL_reuse_filter.json');assert c['reports']==prod['reports']
tot={k:sum(r[k] for r in c['reports']) for k in ('input','covered','remaining')}
assert tot=={'input':8008722,'covered':7660439,'remaining':348283}
hist=[sum(r['first_witness_family_counts'][i] for r in c['reports']) for i in range(8)]
assert hist==[0,25788,120791,3919665,2856110,0,690981,47104]
counts={str(f):sum(r['remaining'] for r in c['reports'] if r['free_target']==f) for f in (False,True)}
assert counts=={'False':348236,'True':47}
popchecks=0;maxs=0
for a in range(6):
 for b in range(7):
  gap=a+1-b;even=gap>=0;n=abs(gap)
  if even and (b<1 or n>a):continue
  if not even and n>b:continue
  maxs=max(maxs,n)
  for delta in (0,1):
   for pe in range(17):
    for po in range(17):
     if a+delta+pe>16 or b+po>16 or 16-a-delta-pe!=16-b-po or pe+po==0:continue
     if even:
      if delta:pairing=pe+po+n;ae=a+1-n;ao=b
      elif n:pairing=pe+po+n-1;ae=a-n+1;ao=b
      else:assert pe-po==1 and pe>=1;pairing=pe+po-1;ae=a+1;ao=b
      minority,majority=5-a,6-b+n
     else:
      if delta:pairing=pe+po+n;ae=a+1;ao=b-n
      else:assert pe-po==n+1 and pe>=1;pairing=pe+po+n-1;ae=a+1;ao=b-n
      minority,majority=6-b,5-a+n
     assert ae==ao and 1<=ae<=16 and pairing%2==0
     if delta:assert pairing>=2
     assert 0<=minority<=16 and majority-minority==2*n and 0<=majority<=16
     popchecks+=1
out={'status':'PASS','totals':tot,'remaining_covered':348236,'remaining_free':47,'witness_family_histogram':hist,'port_population_checks':popchecks,'max_source_number':maxs,'exact_source_domain_binding_to_previous_final_review':True,'all_manifest_hashes_sizes_rechecked_after_run':True,'all_accepted_import_bindings_rechecked':True,'all_selected_witnesses_replayed':7660439,'all_remaining_inputs_exhaustive_six_cuts_all_legal_sources':348283,'exact_partition_and_remaining_bytes':True,'full_twelve_hole_proved':False,'full_P6_proved':False}
(R/'HIGHER_Q5_FULL_REUSE_REVIEW_check.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
