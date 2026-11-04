"""Producer format and synchronous-map checks, then freeze all ten B local cases."""
from pathlib import Path
from itertools import permutations,combinations
import json,hashlib
P=Path(__file__).resolve().parent
profile=json.loads((P/'TWELVE_STAR_B_profile.json').read_text())
summary=json.loads((P/'TWELVE_STAR_B_summary.json').read_text())
assert summary['completed']==summary['total']==summary['reduced_fullrank_cases']==10
rows={r['index']:r for r in profile['rows']};runs={r['index']:r for r in summary['reports']}
perms=list(permutations(range(5)))
units={1,2,4,8,16};Z={7,11,13,19,21};actual=[]
assert len(profile['choices'])==50
seen=set()
for c in profile['choices']:
 t=c['consumed_t'];pair=set(c['pair']);U=units-pair;J=(Z-{t})|U
 assert len(pair)==2 and pair<=units and t in Z and c['omitted']==sorted(U) and c['majority']==sorted(J)
 assert (t,tuple(sorted(pair))) not in seen;seen.add((t,tuple(sorted(pair))))
 q=perms[c['permutation_index_to_canonical']]
 mapping=[sum(((x>>q[d])&1)<<d for d in range(5)) for x in range(32)]
 r=rows[c['orbit_index']]
 assert mapping[0]==0
 assert sorted(mapping[x] for x in J)==r['majority']
 assert sorted(mapping[x] for x in U)==r['omitted']
 assert sorted(mapping[x] for x in pair)==r['forced_pair']
 assert mapping[t] not in {0,*r['majority']}, 'Consumed t must be a covered terminal'
 actual.append({**c,'coordinate_permutation_output_reads_input':q,
  'vertex_map':mapping,'mapped_consumed_t':mapping[t],
  'canonical_minority':[0],'canonical_majority':r['majority'],
  'canonical_omitted':r['omitted'],'canonical_forced_pair':r['forced_pair']})
assert seen=={(t,pair) for t in Z for pair in combinations(sorted(units),2)}
mapping_out={'status':'PRODUCER_EXACT_SYNCHRONOUS_MAP','choices':50,'canonical_classes':10,
 'minority_fixed':0,'pair_unordered_B_data_only':True,'maps':actual,
 'star_Q6_closed':False,'A_mixed_opening_interface_proved':False}
(P/'TWELVE_STAR_B_actual_choices_map.json').write_text(json.dumps(mapping_out,indent=2)+'\n')
sizes={'_forests.bin':1024*34,'_full_pairs.bin':1024*24,'_pairs.bin':1024*22,
 '_columns.bin':1024*22,'_matrix.bin':1024*128,'_pivots.bin':1024*128,'_combos.bin':1024*128}
names=['TWELVE_STAR_B_PROOF.md','TWELVE_STAR_B_profile.py','TWELVE_STAR_B_profile.json',
 'TWELVE_STAR_B_run.py','TWELVE_STAR_B_rank.cpp','TWELVE_STAR_B_summary.json',
 'TWELVE_STAR_B_actual_choices_map.json','TWELVE_STAR_B_OPTIONS.md',
 'TWELVE_STAR_B_fixed_pair_options.json','TWELVE_STAR_B_freeze.py',
 'A10_ORBIT3_UNIVERSAL_PRIMARY_SOURCE.md','FORCED_CHERRY_RANK_REDUCTION.md',
 'HIGHER_FORCED_CHERRY_TRANSFER.md','HIGHER_FORCED_CHERRY_REVIEW.json']
for i in range(10):
 r=runs[i];assert r['geometry']==rows[i] and r['rank_GF2']==1024 and r['full_rank']
 assert len(r['selected_indices'])==1024 and len(set(r['selected_indices']))==1024
 pre=r['prefix'];names += [pre+'.json',pre+'_config.txt']
 for suffix,nbytes in sizes.items():
  name=pre+suffix;assert (P/name).stat().st_size==nbytes,(name,nbytes);names.append(name)
check={'status':'PASS_PRODUCER_FORMAT_AND_MAP_ONLY_NOT_INDEPENDENT_PROOF_CHECK',
 'canonical_classes':10,'actual_choices':50,'forests_each':1024,'total_forests':10240,
 'matrix_rows_each':1024,'columns_each':1024,'matrix_bits_to_independently_check':10485760,
 'fullpairs_record_bytes':24,'reducedpairs_record_bytes':22,'column_record_bytes':22,
 'forest_record_bytes':34,'all_synchronous_actual_maps_verified':True,
 'checker_triggered':False,'star_Q6_closed':False}
(P/'TWELVE_STAR_B_producer_format_map_check.json').write_text(json.dumps(check,indent=2)+'\n')
names.append('TWELVE_STAR_B_producer_format_map_check.json')
manifest={'status':'FROZEN_PRODUCER_TEN_LOCAL_CLASSIFICATIONS_PENDING_FRESH_REVIEW',
 'exact_scope':'ten explicit minority0/majority7/omit3 local Q5 classifications iff required F lacks the actual forced pair, plus their50 actual B choices',
 'claimed_indices':list(range(10)),'forests_each':1024,'forests_total':10240,
 'reduced_endpoints':22,'reduced_rank_each':1024,'matrix_bits_total':10485760,
 'actual_choices_map':'TWELVE_STAR_B_actual_choices_map.json',
 'hashes':{n:hashlib.sha256((P/n).read_bytes()).hexdigest() for n in names},
 'sizes':{n:(P/n).stat().st_size for n in names},
 'independent_local_review_pending':True,'checker_triggered_by_producer':False,
 'A_mixed_opening_interface_proved':False,'star_Q6_closed':False,
 'full_twelve_hole_proved':False,'full_P6_proved':False}
(P/'TWELVE_STAR_B_MANIFEST.json').write_text(json.dumps(manifest,indent=2)+'\n')
print('proof '+manifest['hashes']['TWELVE_STAR_B_PROOF.md'])
print('manifest '+hashlib.sha256((P/'TWELVE_STAR_B_MANIFEST.json').read_bytes()).hexdigest())
print('all50 actual M/J/U/pair and consumed-t maps verified; formats1024 records each; no checker triggered')
