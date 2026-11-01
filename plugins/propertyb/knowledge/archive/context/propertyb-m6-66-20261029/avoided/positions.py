import itertools,json,time
from verify import *
start=time.process_time();data=json.loads((OUT/'RESULTS.json').read_text());rows=[];evals=0;complete=True
for row in data['rows']:
 if row['strict'] or len(row['degrees'])<2:continue
 v=row['v'];s=len(row['degrees']);ctr=v//2
 slots=range(ctr-3,ctr+4);best=F(row['U']);bp=row['positions'];bd=row['degrees'];before=evals
 for pos in itertools.combinations(slots,s):
  for ds in sorted(set(itertools.permutations(row['degrees']))):
   u=bound(row,pos,ds);evals+=1
   if u<best:best,bp,bd=u,pos,ds
  if time.process_time()-start>100:complete=False;break
 rows.append({k:row[k] for k in ('v','kind','degrees','tri')}|dict(previous_U=row['U'],U=str(best),approx=float(best),positions=bp,ordered_degrees=bd,strict=best<1,evaluations=evals-before))
 (OUT/'POSITIONS.json').write_text(json.dumps(dict(scope='remaining multi-lock cases; all degree orders; sorted positions within center +/-3',complete=complete,profiles=len(rows),evaluations=evals,rescued=sum(r['strict'] for r in rows),remaining=sum(not r['strict'] for r in rows),cpu_seconds=time.process_time()-start,rows=rows),indent=2))
 if not complete:break
print(json.dumps(dict(complete=complete,profiles=len(rows),evaluations=evals,rescued=sum(r['strict'] for r in rows),remaining=sum(not r['strict'] for r in rows),cpu_seconds=time.process_time()-start),indent=2))
