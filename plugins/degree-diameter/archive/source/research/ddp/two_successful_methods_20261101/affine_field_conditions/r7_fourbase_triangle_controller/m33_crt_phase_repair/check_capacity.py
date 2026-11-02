"""Exact per-quotient affine-function capacity; no phase-cube sampling."""
import csv
import json
from pathlib import Path
from time import process_time,perf_counter

start,wall=process_time(),perf_counter()
root=Path(__file__).resolve().parent
assert not (root/'CAPACITY_RESULT.json').exists(),'One capacity batch already completed.'
diagnostic=json.loads((root.parent/'m33_global_batch/DIAGNOSTIC_RESULT.json').read_text())
names=['a0','a1','a2','a3','sigma01','sigma23','tau02','tau13','rho03','rho12','third']
free=[0,1,2,4,5,6,7,8,9]
rows=list(csv.DictReader((root.parent/'DISTINCT_FORMS.tsv').open(),delimiter='\t'))
parsed=[]
for line,row in enumerate(rows,start=2):
    coeff=[int(row[n])for n in names]
    parsed.append({'source':int(row['source']),'target':int(row['target']),
                   'coefficient_vector':coeff,'word':[int(row['p'+str(i)])for i in range(3)],
                   'distinct_forms_tsv_line':line})
summaries=[]
for pi,old in enumerate(diagnostic['three_candidates'],start=1):
    values=old['parameters'];quotient=[v%11 for v in values]
    buckets=[[[]for _ in range(11)]for _ in range(16)]
    for row in parsed:
        c=row['coefficient_vector'];r=sum(c[i]*quotient[i]for i in range(10))%11
        affine=tuple(c[i]%3 for i in free)+(2*c[10]%3,)
        record=dict(row,quotient_residue=r,affine_phase_coefficients_and_constant=list(affine))
        buckets[4*row['source']+row['target']][r].append(record)
    counts=[[len({tuple(x['affine_phase_coefficients_and_constant'])for x in b})for b in row]for row in buckets]
    bad=[]
    for pair,row in enumerate(buckets):
        for residue,b in enumerate(row):
            if counts[pair][residue]<3:
                bad.append({'source':pair//4,'target':pair%4,'quotient_residue':residue,
                            'symbolic_forms':len(b),'distinct_affine_functions':counts[pair][residue],
                            'reason':'fewer_than_three_symbolic_routes' if len(b)<3 else 'unavoidable_affine_function_aliasing',
                            'word_line_witnesses':b})
    result={'profile':pi,'source_attempt_1based':old['attempt_1based'],'source_parameters':values,
            'fixed_parameters_mod11':quotient,'free_phase_variable_indices':free,
            'free_phase_variable_names':[names[i]for i in free],
            'affine_function_encoding':'nine variable coefficients mod3, then affine constant mod3',
            'phase_e':2,'capacity_by_source_times4_plus_target_then_quotient_residue':counts,
            'minimum_distinct_affine_functions':min(map(min,counts)),
            'bad_bucket_count':len(bad),'capacity_pass':not bad,'bad_buckets':bad}
    sub=root/('profile'+str(pi));sub.mkdir(exist_ok=True)
    (sub/'CAPACITY.json').write_text(json.dumps(result,indent=2)+'\n')
    summaries.append({k:result[k]for k in ['profile','source_attempt_1based','fixed_parameters_mod11',
                                        'minimum_distinct_affine_functions','bad_bucket_count','capacity_pass']})
result={'status':'COMPLETE_THREE_FIXED_QUOTIENT_CAPACITY_CHECK',
        'profiles':summaries,'source_symbolic_forms_read_once':len(parsed),
        'quotient_buckets_per_profile':176,'phase_assignments_tested':0,
        'CPU_seconds':process_time()-start,'wall_seconds':perf_counter()-wall,
        'CPU_budget_seconds':20,'workers':1,'running':False,'active_processes':[]}
(root/'CAPACITY_RESULT.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result))
