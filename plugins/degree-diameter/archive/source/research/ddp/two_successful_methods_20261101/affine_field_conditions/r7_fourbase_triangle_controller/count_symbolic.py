"""One complete symbolic word count; no numerical voltage assignments."""
import csv
import itertools
import json
from pathlib import Path
from time import process_time, perf_counter

start,wall=process_time(),perf_counter()
root=Path(__file__).resolve().parent
names=['a0','a1','a2','a3','sigma01','sigma23','tau02','tau13','rho03','rho12','third']
def unit(i,k=1):
    a=[0]*11;a[i]=k;return tuple(a)
zero=(0,)*11
def add(a,b):
    return tuple((x+y)%3 if i==10 else x+y for i,(x,y) in enumerate(zip(a,b)))
def neg(a):
    return tuple(-x%3 if i==10 else -x for i,x in enumerate(a))
matchings=[{0:(1,4),1:(0,4),2:(3,5),3:(2,5)},
           {0:(2,6),2:(0,6),1:(3,7),3:(1,7)},
           {0:(3,8),3:(0,8),1:(2,9),2:(1,9)}]
def step(base,p):
    if p==0:return (base+1)%4,unit(base)
    if p==1:return (base-1)%4,unit((base-1)%4,-1)
    if p==2:return ((base+1)%3,zero) if base<3 else (3,unit(10))
    if p==3:return ((base-1)%3,zero) if base<3 else (3,unit(10,2))
    target,v=matchings[p-4][base]
    return target,unit(v,1 if base<target else -1)
reverse=[1,0,3,2,4,5,6]
for base in range(4):
    for p in range(7):
        target,v=step(base,p);back,w=step(target,reverse[p])
        assert back==base and add(v,w)==zero
    end=base;vec=zero
    for _ in range(3):
        end,v=step(end,2);vec=add(vec,v)
    assert end==base and vec==zero

classes=[[{} for _ in range(4)]for _ in range(4)]
allrows=[]
for source in range(4):
    for word in itertools.product(range(7),repeat=3):
        target=source;vec=zero
        for p in word:
            target,v=step(target,p);vec=add(vec,v)
        allrows.append([source,*word,target,*vec])
        classes[source][target].setdefault(vec,word)
with (root/'ALL_WORD_FORMS.tsv').open('w') as f:
    writer=csv.writer(f,delimiter='\t');writer.writerow(['source','p0','p1','p2','target',*names]);writer.writerows(allrows)
with (root/'DISTINCT_FORMS.tsv').open('w') as f:
    writer=csv.writer(f,delimiter='\t');writer.writerow(['source','target',*names,'p0','p1','p2'])
    for source in range(4):
        for target in range(4):
            for vec,word in sorted(classes[source][target].items()):writer.writerow([source,target,*vec,*word])
counts=[[len(c)for c in row]for row in classes]
minimum=min(map(min,counts))
result={'status':'COMPLETE_FIXED_FOURBASE_SYMBOLIC_CAPACITY',
        'voltage_names':names,'third_coefficient_modulus':3,'word_count':len(allrows),
        'distinct_forms_by_source_target':counts,'minimum_capacity':minimum,
        'upper_modulus_from_symbolic_capacity':minimum,
        'upper_modulus_divisible_by3':minimum-minimum%3,
        'first_competitive_modulus':33,'capacity_reaches_competitive_modulus':minimum>=33,
        'symbolic_reverse_checks':28,'symbolic_B_triangle_checks':4,
        'numerical_voltage_assignments_tested':0,'controller_searches':0,'graphs_generated':0,
        'BFS_runs':0,'Lean_compilations':0,'solver_calls':0,
        'CPU_seconds':process_time()-start,'wall_seconds':perf_counter()-wall,
        'CPU_budget_seconds':5,'workers':1,'running':False,'active_processes':[]}
(root/'RESULT.json').write_text(json.dumps(result,indent=2)+'\n')
(root/'TERMINAL.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result))
