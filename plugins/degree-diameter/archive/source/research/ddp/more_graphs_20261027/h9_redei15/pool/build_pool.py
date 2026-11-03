"""New Redei15 shape only: PGL3(F3)702 masks in cached1120planes.
Degree and pin-count filters only; noR4,anchors,BFS or graphgeneration.
"""
from array import array
from collections import Counter
from pathlib import Path
import json,resource,time
P=Path(__file__).resolve().parent;ROOT=P.parents[4];start=time.process_time()
resource.setrlimit(resource.RLIMIT_CPU,(89,90))

def cpu():return time.process_time()-start

def save(name,data):
 (P/name).write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n')

orbit=json.load(open(P/'orbit.json'));count=orbit['orbit_size'];ids15=orbit['point_indices15']
masks=[int(a)+(int(b)<<64)for a,b in orbit['mask_words_u64_decimal']]
assert len(masks)==len(ids15)==702
flatdir=ROOT/'research/ddp/more_graphs_20261027/h9_baer_plane_pool'
nonflatdir=ROOT/'research/ddp/more_graphs_20261027/h9_baer_nonflat_F3_pool'
sources=json.load(open(nonflatdir/'sources.json'))
coeff=orbit['coefficient_points_PG2F9']
words=list(map(int,(nonflatdir/'coefficient_points91.txt').read_text().split()))
assert words[0]==91 and [words[1+3*j:4+3*j]for j in range(91)]==coeff
flats=json.load(open(flatdir/'planes.json'))['records']
nonflats=json.load(open(nonflatdir/'nonflat_planes.json'))['records']
assert len(flats)==364 and len(nonflats)==756
planes=[]
for x in flats:
 planes.append({'global_index':len(planes),'kind':'flat','local_index':x['plane_index'],'basis':x['basis_y_x_z'],'point_ids91':x['point_ids91'],'center_original_label':x['center_original_label']})
for x in nonflats:
 planes.append({'global_index':len(planes),'kind':'nonflat','local_index':x['nonflat_plane_index'],'basis':x['RREF_basis'],'point_ids91':x['Q9_point_ids91']})
assert len(planes)==1120
coords=(ROOT/sources['coords']).read_bytes();assert len(coords)==66430*7
fold={};degree={};bindings={}
for cap in [11,12]:
 f=array('H');f.frombytes((ROOT/sources['fold'+str(cap)]).read_bytes());assert len(f)==66430
 fold[cap]=f
 degree[cap]=(nonflatdir/('degree'+str(cap)+'.u8.bin')).read_bytes()
 info=sources['sourceinfo'][str(cap)]
 expected_n=37631 if cap==11 else 42398;expected_m=205329 if cap==11 else 245889
 assert info['source_n']==expected_n and info['source_m']==expected_m
 assert len(degree[cap])==expected_n
 with(ROOT/info['source_file']).open()as h:header=list(map(int,h.readline().split()))
 assert header==[expected_n,expected_m]
 bindings[cap]={'source_file':info['source_file'],'source_n':expected_n,'source_m':expected_m,'degree_cache':str((nonflatdir/('degree'+str(cap)+'.u8.bin')).relative_to(ROOT)),
 'point_to_actual_pin_cache':sources['fold'+str(cap)],'degree_cache_reused_without_recomputation':True}
save('sources.json',{'bases':bindings,'raw_point_coordinates':sources['coords'],'flat_plane_cache':str((flatdir/'planes.json').relative_to(ROOT)),'nonflat_plane_cache':str((nonflatdir/'nonflat_planes.json').relative_to(ROOT)),'coefficient_index_binding_matches':True,
 'source_graph_checks':'Header/sourcecache binding only;no edge revalidation or sourceBFS.'})
classes={11:{},12:{}}
stats={cap:{'degree_allowed_occurrences':0,'pin_count_feasible_occurrences':0,'degree_allowed_pin_count_histogram':Counter(),'by_plane_kind':{'flat':Counter(),'nonflat':Counter()},'planes_with_under15_allowed_raw_points':0}for cap in [11,12]}
processed=0;limited=False;profile_stopped=False;prep_CPU=cpu();loop_start=cpu()
for plane in planes:
 if orbit['CPU_seconds']+cpu()>88:
  limited=True;break
 raw91=plane['point_ids91'];assert len(raw91)==91
 actual={cap:[fold[cap][raw]for raw in raw91]for cap in [11,12]}
 allowed={cap:sum(1<<j for j,v in enumerate(actual[cap])if degree[cap][v]<cap)for cap in [11,12]}
 for cap in [11,12]:
  kind=plane['kind'];st=stats[cap];st['by_plane_kind'][kind]['planes_processed']+=1
  st['by_plane_kind'][kind]['raw_occurrences']+=count
  if allowed[cap].bit_count()<15:
   st['planes_with_under15_allowed_raw_points']+=1;continue
  for oi,mask in enumerate(masks):
   if mask&~allowed[cap]:continue
   st['degree_allowed_occurrences']+=1;st['by_plane_kind'][kind]['degree_allowed_occurrences']+=1
   pins=tuple(sorted({actual[cap][j]for j in ids15[oi]}))
   assert 10<=len(pins)<=15
   st['degree_allowed_pin_count_histogram'][len(pins)]+=1
   if len(pins)>cap:continue
   st['pin_count_feasible_occurrences']+=1;st['by_plane_kind'][kind]['pin_count_feasible_occurrences']+=1
   ref=[plane['global_index'],oi]
   if pins in classes[cap]:
    rec=classes[cap][pins];rec['witness_multiplicity']+=1;rec['all_witness_plane_orbit_refs'].append(ref);continue
   rawids=[raw91[j]for j in ids15[oi]]
   witness={'plane_kind':kind,'plane_global_index':plane['global_index'],'plane_local_index':plane['local_index'],'plane_basis':plane['basis'],
    'orbit_index':oi,'Redei_orbit_index':oi,'coefficient_point_indices15':ids15[oi],'original_point_ids15':rawids,'original_point_coordinates15':[list(coords[7*j:7*j+7])for j in rawids],
    'mask_words_u64_decimal':orbit['mask_words_u64_decimal'][oi]}
   if 'center_original_label'in plane:witness['center_original_label']=plane['center_original_label']
   deg=[degree[cap][v]for v in pins]
   classes[cap][pins]={'pins':list(pins),'anchor_cap':cap-len(pins),'mandatory_pin_count':len(pins),'pin_current_degrees':deg,'pin_free_slots':[cap-d for d in deg],
    'raw_point_count':15,'witness_multiplicity':1,'all_witness_plane_orbit_refs':[ref],'witness':witness}
 processed+=1
 if processed==10:
  elapsed=cpu()-loop_start;projected=orbit['CPU_seconds']+prep_CPU+elapsed*1120/10
  profile={'planes_processed_once':10,'shape_occurrences_covered':10*count,'loop_CPU_seconds':elapsed,'preparation_CPU_seconds':prep_CPU,'orbit_CPU_seconds':orbit['CPU_seconds'],'projected_full1120_CPU_seconds':projected,
   'distinct_pool11_sofar':len(classes[11]),'distinct_pool12_sofar':len(classes[12]),'continue_complete_scope':projected<=90,'profile_not_replayed':True}
  save('profile10planes.json',profile);print('PROFILE10',json.dumps(profile),flush=True)
  if projected>90:profile_stopped=True;break
complete=processed==1120
summaries=[]
for cap in [11,12]:
 records=[classes[cap][pins]for pins in sorted(classes[cap])]
 for i,rec in enumerate(records):rec['pool_index']=i
 hist=Counter(len(rec['pins'])for rec in records)
 pool={'status':'COMPLETE_DEGREE_ONLY_POOL'if complete else'PARTIAL_DEGREE_ONLY_POOL','delta':cap,**bindings[cap],
  'shape':'Redei15 x^5 graphplus6 directions; fixedPGL3F3 orbit','raw_point_count':15,'orbit_size':count,'planes_expected':1120,'planes_processed':processed,'complete1120plane_scope':complete,
  'source_binding':'Frozen base;producer mustrecheckdegreesifbasechanges. No R4completionperformedhere.',
  'pin_count_histogram':dict(sorted(hist.items())),'records':records}
 save('pool'+str(cap)+'.json',pool)
 st=stats[cap]
 summaries.append({'delta':cap,**bindings[cap],'raw_degree_allowed_occurrences':st['degree_allowed_occurrences'],'degree_and_pincount_feasible_occurrences':st['pin_count_feasible_occurrences'],
  'distinct_folded_pinsets':len(records),'duplicate_feasible_occurrences':st['pin_count_feasible_occurrences']-len(records),'distinct_pin_count_histogram':dict(sorted(hist.items())),
  'degree_allowed_fold_size_histogram':dict(sorted(st['degree_allowed_pin_count_histogram'].items())),
  'minimum_mandatory_pin_count':min(hist)if hist else None,'maximum_mandatory_pin_count':max(hist)if hist else None,'maximum_anchor_cap':max((r['anchor_cap']for r in records),default=None),
  'planes_with_under15_allowed_raw_points':st['planes_with_under15_allowed_raw_points'],'by_plane_kind':st['by_plane_kind'],'pool_file':'pool'+str(cap)+'.json'})
result={'status':'COMPLETE_702_F3_ORBIT_X1120_PLANES_DEGREE_POOL'if complete else'PARTIAL_PROFILE_OVER_BUDGET'if profile_stopped else'PARTIAL_CPU_WINDOW',
 'prediction_id':'P_REDEI15_F3_PLANE_DEGREE_POOL','prediction_verdict':'SUPPORTED' if len(classes[12]) else 'REFUTED' if complete else 'UNRESOLVED',
 'PGL_scope':'OnlyPGL3F3 orbit ofone15shape;otherGaloisforms and fullPGL3F9notenumerated.','orbit_size':count,'raw_points_per_set':15,'Frobenius_fixed_points_per_set':5,'fully_unsplit_pin_count':10,
 'flat_planes_reused':364,'nonflat_planes_reused':756,'planes_expected':1120,'planes_processed':processed,'complete1120plane_scope':complete,'raw_shape_occurrences_covered':processed*count,
 'deltas':summaries,'orbit_CPU_seconds':orbit['CPU_seconds'],'pool_process_CPU_seconds':cpu(),'total_CPU_seconds':orbit['CPU_seconds']+cpu(),'CPU_budget_seconds':90,'workers':1,
 'profile10_replayed':False,'old_Baer_masks_enumerated_or_read':False,'old_Baer_candidate_pool_retested':False,'planes_regenerated':False,'source_BFS':0,'R4_evaluations':0,'anchor_tests':0,'graphs_generated':0,'new_lower_bounds':0,
 'pending':[],'handoff':'Poolonly;exactfullbase R4 andanchorcompletion belong to separateproducer.'}
# Keep the prediction verdict explicit and independent of output formatting.
result['prediction_verdict']='SUPPORTED'if len(classes[12])>0 else'REFUTED'if complete else'UNRESOLVED'
save('RESULT.json',result);save('terminal.json',result)
print('FINAL',json.dumps({k:v for k,v in result.items()if k!='deltas'}),flush=True)
print('POOLS',[(d['delta'],d['distinct_folded_pinsets'],d['distinct_pin_count_histogram'],d['maximum_anchor_cap'])for d in summaries],flush=True)
