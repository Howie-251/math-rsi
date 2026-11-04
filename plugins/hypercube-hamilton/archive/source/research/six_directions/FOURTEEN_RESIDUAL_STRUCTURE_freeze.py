from pathlib import Path
import json,hashlib,itertools
P=Path(__file__).resolve().parent
sha=lambda n:hashlib.sha256((P/n).read_bytes()).hexdigest()
j=json.loads((P/'FOURTEEN_RESIDUAL_STRUCTURE.json').read_text());r=j['orbit_rows'][85];rep=r['representative'];maps=[]
for p in itertools.permutations(range(5)):
 tr=[sum(((x>>p[d])&1)<<d for d in range(5))|(x&32) for x in range(64)]
 image=tuple(sorted(tr[x] for x in rep[:6]))+tuple(sorted(tr[x] for x in rep[6:]));maps.append((image,list(p),tr))
src=(P/'FOURTEEN_FORCED_remaining_v31_covered.bin').read_bytes();positive=(P/'FOURTEEN_RESIDUAL_STRUCTURE_maxA_positive_v31_covered.bin').read_bytes();positive={tuple(positive[i:i+13]) for i in range(0,len(positive),13)};transport=[]
for i in range(0,len(src),13):
 rec=tuple(src[i:i+13])
 if rec not in positive:continue
 image,p,tr=next((im,p,tr) for im,p,tr in maps if im==rec)
 transport.append({'source_index':i//13,'actual_record':list(rec),'permutation_output_reads_input':p+[5]})
assert len(transport)==60
(P/'FOURTEEN_RESIDUAL_STRUCTURE_maxA_transport.json').write_text(json.dumps(transport,indent=2)+'\n')
j.update(status='PRODUCER_STRUCTURE_AND_NEW60_MAXIMAL_A_CANDIDATE_PENDING_INDEPENDENT_REVIEW',forced_edge_histogram_records={'0':575,'1':3036,'2':312},new_maximal_A={'orbit_index':85,'positive_actual_geometries':60,'complete_maximal_A_domain':287469,'positive_A_certificates':287469,'remaining_after_FORCED_and_candidate':2527,'remaining_by_target':{'1':240,'7':702,'31':1585},'independent_reduction_finite_and_application_review_passed':False},full_fourteen_hole_proved=False,full_P6_proved=False)
(P/'FOURTEEN_RESIDUAL_STRUCTURE.json').write_text(json.dumps(j,indent=2)+'\n')
# dependency source bytes frozen under manifest; no producer success flag acts as an import theorem
inputs=[f'FOURTEEN_HALL_remaining_v{v}_covered.bin' for v in (1,7,31)]+[f'FOURTEEN_FORCED_remaining_v{v}_covered.bin' for v in (1,7,31)]+['FOURTEEN_HALL_MANIFEST.json','FOURTEEN_FORCED_candidate_classes.json','FOURTEEN_REUSE_REVIEW_registry.txt','FOURTEEN_CACHED_REVIEW_selected_registry.txt','FOURTEEN_REUSE_REVIEW.json','FOURTEEN_CACHED_REVIEW.json','TWELVE_NEW_FORCED_REVIEW.json','TWELVE_STAR_MAXIMAL_A_FINITE_REVIEW.json','TWELVE_ROOT_STAR_NONADJACENT_OPTIONS.json']+[f'TWELVE_ROOT_STAR_OPENING_case_{c:02}_forests.bin' for c in range(5)]
for name in ('FOURTEEN_FORCED_MANIFEST.json','EIGHTEEN_POST12_HALL_remaining_v31_covered.bin'):
 if (P/name).exists():inputs.append(name)
outputs=[p.name for p in P.glob('FOURTEEN_RESIDUAL_STRUCTURE*') if p.is_file() and p.name!='FOURTEEN_RESIDUAL_STRUCTURE_MANIFEST.json' and not p.name.endswith('.exe')]
m={'status':'PRODUCER_COMPLETE_NEW60_MAXIMAL_A_CANDIDATE_PENDING_FRESH_INDEPENDENT_REVIEW','reviewer_or_producer_role':'proof-writer/computational-producer','source_HALL_records':3923,'source_FORCED_records':2587,'exact_stabilizer_orbits':88,'new_positive_geometries':60,'remaining':2527,'remaining_covered_target_geometries':2527,'remaining_free_target_geometries':0,'complete_maximal_A_domain':287469,'finite_positive_certificates':287469,'producer_sanity_passed':True,'independent_acceptance_passed':False,'source_FORCED_application_requires_separate_acceptance':True,'full_fourteen_hole_proved':False,'full_P6_proved':False,'production_or_RUN_STATE_modified':False,'input_hashes':{n:sha(n) for n in inputs},'output_hashes':{n:sha(n) for n in sorted(outputs)},'output_sizes':{n:(P/n).stat().st_size for n in sorted(outputs)}}
(P/'FOURTEEN_RESIDUAL_STRUCTURE_MANIFEST.json').write_text(json.dumps(m,indent=2)+'\n')
print('proof',sha('FOURTEEN_RESIDUAL_STRUCTURE_PROOF.md'));print('manifest',sha('FOURTEEN_RESIDUAL_STRUCTURE_MANIFEST.json'));print('outputs',len(outputs))
