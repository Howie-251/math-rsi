"""One alternative low-factor rule; reuse already generated F25 coset labels."""
from pathlib import Path
import importlib.util
import json
import resource
import time

OUT=Path(__file__).resolve().parent
OLD=OUT.parent/'q25_c4_profile'
START=time.process_time()
assert json.loads((OUT/'PREDICTION.json').read_text())['frozen_before_candidate_evaluation']
assert not (OUT/'RESULT.json').exists(),'Completedfixedscope mustnot be restarted.'
resource.setrlimit(resource.RLIMIT_CPU,(15,20))
spec=importlib.util.spec_from_file_location('q25_orbital_implementation',OLD/'run.py')
m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m)
m.START=START;m.OUT=OUT
inp=json.loads((OLD/'inputs.json').read_text())
assert json.loads((OLD/'RESULT.json').read_text())['scope_exhausted']
field=m.PSL25()
reps=[tuple(x) for x in inp['right_coset_representatives']]
H=[tuple(x) for x in inp['H']]
lookup={field.mul(x,h):i for i,x in enumerate(reps) for h in H}
assert len(lookup)==7800
perms=[[lookup[field.mul(tuple(s),x)] for x in reps] for s in inp['permutation_generators']]
assert all(sorted(p)==list(range(1950)) for p in perms)
r=tuple(inp['torus_generator_order12'])
normalizer={lookup[tuple(x)] for x in inp['normalizer']}
assert len(normalizer)==6
normalmask=sum(1<<i for i in normalizer)
prep=dict(perms=perms,choices=inp['valence4_items'],cache={},bits=[1<<i for i in range(1950)])
rot=dict(id='ROTATION_C3',degree=2,representative_pair=[0,lookup[r]])
base,base_codes=m.orbital(rot,prep)
oldfirst=json.loads((OLD/'first_calibration.json').read_text())
oldseen=sum(1<<i for i,d in enumerate(oldfirst['ordinary_distances']) if 0<=d<=5)
results=[];hit=False;comparison=None
for j,item in enumerate(prep['choices']):
    if time.process_time()-START>10:break
    masks4,codes4=m.orbital(item,prep)
    masks=[a|b for a,b in zip(base,masks4)]
    assert all(row.bit_count()==6 for row in masks)
    seen=m.reachable_R5(masks)
    row=dict(case_index=j,involution=item['involution'],root_R5_missing=1950-seen.bit_count(),
             normalizer_reached=(seen&normalmask).bit_count())
    results.append(row)
    if j==0:
        comparison=dict(first_involution=item['involution'],old_C6_normalizer_reached=(oldseen&normalmask).bit_count(),
                        new_C3_normalizer_reached=(seen&normalmask).bit_count(),
                        old_missing_repaired=(seen&~oldseen).bit_count(),
                        old_reached_lost=(oldseen&~seen).bit_count(),
                        specific_repair_prediction_supported=bool(seen&~oldseen))
        m.calibrate_first(base_codes+codes4,seen,dict(profile='4+2',involution=item['involution']))
    if row['root_R5_missing']==0:
        codes=sorted(base_codes+codes4)
        assert len(codes)==len(set(codes))==5850
        (OUT/'candidate1950.edges').write_text('1950 5850\n'+''.join(f'{c//1950} {c%1950}\n' for c in codes))
        m.save('parameters.json',dict(group='PSL2F25',field=inp['field'],H=H,rotation=r,
                valence4_involution=item['involution'],profile='4+2',n=1950,m=5850,
                rightcoset_labels_source='../q25_c4_profile/inputs.json',
                root_R5_full=True,independent_acceptance_pending=True,record_claimed=False))
        hit=True;break
complete=len(results)==78
result=dict(status='FULL_HIT_PENDING_ROOT' if hit else 'COMPLETE_78_TRIANGLE_PROFILE_NO_HIT' if complete else 'BUDGET_UNKNOWN',
            n=1950,target_Delta=6,target_D=5,savedL=1518,total=78,evaluated=len(results),
            unprocessed=78-len(results),complete=complete,full_hits=int(hit),cases=results,
            first_controlled_comparison=comparison,CPU_seconds=time.process_time()-START,
            old_group_regenerated=False,old_graph_BFS=0,new_root_BFS=1,
            actual_D=None,ordinary_bad_unordered_pairs=None,
            scope='Onlysamefixedq25/C4actionwiththeuniquevalence2rotationorbitalplusoneof78selfpairedvalence4orbitals.')
m.save('RESULT.json',result);m.save('terminal.json',result)
print(json.dumps({k:v for k,v in result.items() if k!='cases'}))
