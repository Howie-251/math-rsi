"""Substitute one voltage relation into saved forms, without word enumeration."""
import csv
import json
from pathlib import Path
from time import process_time,perf_counter

start,wall=process_time(),perf_counter()
root=Path(__file__).resolve().parent
assert not (root/'RESULT.json').exists(),'This symbolic substitution already completed.'
names=['a0','a1','a2','a3','sigma01','sigma23','tau02','tau13','rho03','rho12','third']
rows=list(csv.DictReader((root.parent/'DISTINCT_FORMS.tsv').open(),delimiter='\t'))
groups=[[{}for _ in range(4)]for _ in range(4)]
input_counts=[[0]*4 for _ in range(4)]
for line,row in enumerate(rows,start=2):
    c=[int(row[n])for n in names];old=list(c)
    c[3]=0;c[5]+=c[7];c[9]+=c[7];c[7]=0;c[10]%=3
    s,t=int(row['source']),int(row['target']);input_counts[s][t]+=1
    record={'source_line':line,'old_coefficients':old,'word':[int(row['p'+str(i)])for i in range(3)]}
    groups[s][t].setdefault(tuple(c),[]).append(record)
with (root/'SUBSTITUTED_FORMS.tsv').open('w')as f:
    w=csv.writer(f,delimiter='\t');w.writerow(['source','target',*names,'merged_old_forms','p0','p1','p2','first_source_line'])
    for s in range(4):
        for t in range(4):
            for coeff,origins in sorted(groups[s][t].items()):
                w.writerow([s,t,*coeff,len(origins),*origins[0]['word'],origins[0]['source_line']])
merges=[];hist={}
for s in range(4):
    for t in range(4):
        for coeff,origins in sorted(groups[s][t].items()):
            hist[len(origins)]=hist.get(len(origins),0)+1
            if len(origins)>1:merges.append({'source':s,'target':t,'substituted_coefficients':list(coeff),'old_forms':origins})
counts=[[len(c)for c in row]for row in groups];minimum=min(map(min,counts))
result={'status':'COMPLETE_TRIANGLE123_CLOSURE_SYMBOLIC_GATE','substitution':'a3=0;tau13=rho12+sigma23',
        'voltage_names':names,'source_forms_read':len(rows),'source_word_enumerations':0,
        'old_capacities':input_counts,'new_capacities':counts,'minimum_capacity':minimum,
        'minimum_classes':[[s,t]for s in range(4)for t in range(4)if counts[s][t]==minimum],
        'upper_modulus':minimum-minimum%3,'m33_capacity_survives':minimum>=33,
        'distinct_new_forms':sum(map(sum,counts)),'merged_groups':len(merges),
        'old_form_multiplicity_histogram':hist,'maximum_old_forms_per_new_form':max(hist),
        'parameter_assignments_tested':0,'controller_searches':0,'graphs_generated':0,'BFS_runs':0,
        'Lean_compilations':0,'solver_calls':0,'CPU_seconds':process_time()-start,
        'wall_seconds':perf_counter()-wall,'CPU_budget_seconds':5,'workers':1,
        'running':False,'active_processes':[]}
(root/'MERGED_FORM_GROUPS.json').write_text(json.dumps(merges,indent=2)+'\n')
(root/'RESULT.json').write_text(json.dumps(result,indent=2)+'\n')
(root/'TERMINAL.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result))
