from pathlib import Path
from itertools import product
import json,time,csv

p=Path(__file__).resolve().parent
start=time.process_time()

def step(c,port,f):
    if port==0:
        f[c]+=1
        return 0 if c==0 else 3-c
    if port==1:
        f[0 if c==0 else 3-c]-=1
        return 0 if c==0 else 3-c
    if port==2:return (c+1)%3
    if port==3:return (c+2)%3
    if port==4:
        if c==2:
            f[6]+=1
            return 2
        f[3]+=1 if c==0 else -1
        return 1-c
    if port==5:
        if c==1:
            f[6]+=1
            return 1
        f[4]+=1 if c==0 else -1
        return 2-c
    if c==0:
        f[6]+=1
        return 0
    f[5]+=1 if c==1 else -1
    return 3-c

forms={}
rows=[]
for c in range(3):
    for w in product(range(7),repeat=3):
        d=c
        f=[0]*7
        for port in w:d=step(d,port,f)
        f[-1]%=2
        f=tuple(f)
        forms.setdefault((c,d),{}).setdefault(f,w)
        rows.append((c,*w,d,*f))
with (p/'ALL_WORD_FORMS.tsv').open('w') as out:
    writer=csv.writer(out,delimiter='\t')
    writer.writerow(['root','p0','p1','p2','target','alpha0','alpha1','alpha2','sigma','tau','rho','half'])
    writer.writerows(rows)
with (p/'DISTINCT_FORMS.tsv').open('w') as out:
    writer=csv.writer(out,delimiter='\t')
    writer.writerow(['root','target','alpha0','alpha1','alpha2','sigma','tau','rho','half','p0','p1','p2'])
    for (c,d),fs in sorted(forms.items()):
        for f,w in sorted(fs.items()):writer.writerow([c,d,*f,*w])
counts=[[len(forms[c,d]) for d in range(3)] for c in range(3)]
bound=min(map(min,counts))
result={'status':'SYMBOLIC_COUNT_COMPLETE','distinct_endpoint_forms':counts,'min_count':bound,'largest_even_m_possible_by_count':bound-bound%2,'controller_order_bound':3*(bound-bound%2),'prediction_min_exceeds36':bound>36,'port_words':len(rows),'CPU_seconds':time.process_time()-start,'actual_controller_searches':0,'graphs_generated':0,'BFS_Lean_solver_runs':0}
(p/'SYMBOLIC_RESULT.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result))
