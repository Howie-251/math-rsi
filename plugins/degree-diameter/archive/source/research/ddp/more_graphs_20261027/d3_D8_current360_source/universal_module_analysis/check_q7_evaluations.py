"""Evaluate cached formal endpoints only. No word enumeration or graph code."""
from pathlib import Path
import json,time
HERE=Path(__file__).resolve().parent
start=time.process_time()
pred=json.loads((HERE/'PREDICTION.json').read_text())
raw=json.loads((HERE.parent/'quaternion_orbit_field_controls'/'UNIVERSAL_ENDPOINT_RESULT_ROOT.json').read_text())
coeffs=raw['results']['10']['universal_quaternion_endpoints']
assert len(coeffs)==53
pairs=pred['canonical_pairs']
assert len(pairs)==8 and len({tuple(x) for x in pairs})==8
rows=[]
for u,v in pairs:
    assert (u*u+v*v)%7==6
    image=sorted({((c0+u*c2+v*c3)%7,(-c1+v*c2-u*c3)%7) for c0,c1,c2,c3 in coeffs})
    missing=[[x,y] for x in range(7) for y in range(7) if (x,y) not in image]
    rows.append({'u':u,'v':v,'image_cardinality':len(image),'missing_count':49-len(image),'image':[list(x) for x in image],'missing':missing})
maximum=max(r['image_cardinality'] for r in rows)
result={'status':'COMPLETE_EIGHT_CANONICAL_EVALUATIONS','prediction_result':'SUPPORTED' if maximum<49 else 'REFUTED','formal_endpoint_count':53,'required_module_size':49,'evaluated_representations':8,'coefficient_evaluations':8*53,'max_image':maximum,'all_have_holes':maximum<49,'rows':rows,'CPU_seconds':time.process_time()-start,'new_word_enumerations':0,'new_graphs':0,'BFS':0,'solver_runs':0,'producer_control_unchanged':{'q':7,'u':2,'v':3}}
(HERE/'RESULT.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps({k:v for k,v in result.items() if k!='rows'}))
print(json.dumps([{'u':r['u'],'v':r['v'],'image':r['image_cardinality']} for r in rows]))
