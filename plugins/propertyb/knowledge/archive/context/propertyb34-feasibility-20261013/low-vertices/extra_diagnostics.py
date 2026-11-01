"""Additional specified profiles, not structural selection proofs."""
import runpy, json
from pathlib import Path
ns=runpy.run_path(str(Path(__file__).with_name('diagnose.py')))
Profile,rows,total_bound,certificate,json_value=[ns[k] for k in ('Profile','rows','total_bound','certificate','json_value')]
check=ns['check_independent']
cases=[]

def run(v,counts,positions,degrees,label):
 options=[]
 for pos in positions:
  p=Profile(v,5,pos,counts);cs=[certificate(p,i) for i in range(len(pos))]
  rs=rows(p,deductions={pos[i]:cs[i]['loss'] for i in range(len(pos))})
  options.append(dict(v=v,m=34,degrees=degrees,positions=pos,counts=counts,
   certificates=cs,rows=rs,bound=total_bound(rs)))
 best=min(options,key=lambda c:c['bound']);check(best)
 best['tested_positions']=positions;best['label']=label
 cases.append(best);print(label,best['positions'],best['bound'],flush=True)

for t in (0,1):
 counts={0:13-t,1:6+t,2:6+t,4:6+t,3:1-t,5:1-t,6:1-t,7:t}
 assert sum(counts.values())==34
 run(19,counts,[(k,k+1,k+2) for k in range(7,12)],(8,8,8),'v19_unit_triple_t'+str(t))

for a,b,c in [(1,1,2),(1,2,2),(2,2,2)]:
 for t in range(min(a,b,c)+1):
  counts={0:10+a+b+c-t,1:8-a-b+t,2:8-a-c+t,4:8-b-c+t,
          3:a-t,5:b-t,6:c-t,7:t}
  run(19,counts,[(k,k+1,k+2) for k in range(7,12)],(8,8,8),
      'v19_triple_'+str((a,b,c))+'_t'+str(t))

for lam in range(3,9):
 counts={0:18+lam,1:8-lam,2:8-lam,3:lam}
 run(19,counts,[(1,11)],(8,8),'v19_8_8_lambda'+str(lam))

for lam in range(5,10):
 counts={0:16+lam,1:9-lam,2:9-lam,3:lam}
 run(21,counts,[(k,k+1) for k in range(8,13)]+[(k,k+2) for k in range(8,12)],(9,9),'v21_9_9_lambda'+str(lam))

for lam in (8,9):
 counts={0:15+lam,1:9-lam,2:10-lam,3:lam}
 run(21,counts,[(k,k+1) for k in range(8,13)]+[(k,k+2) for k in range(8,12)],(9,10),'v21_9_10_lambda'+str(lam))

run(21,{0:16,1:3,2:6,4:6,3:1,5:1,6:1},
    [p for k in range(7,13) for p in ((k,k+1,k+2),(k+1,k,k+2),(k+2,k,k+1))],
    (5,8,8),'v21_5_8_8_unit_t0')
for dx,dy in ((6,8),(7,8),(8,8)):
 counts={0:35-dx-dy,1:dx-1,2:dy-1,3:1}
 run(21,counts,[(k,k+1) for k in range(8,13)]+[(k,k+2) for k in range(8,12)],(dx,dy),
     'v21_'+str(dx)+'_'+str(dy)+'_unit')

Path(__file__).with_name('EXTRA_RESULTS.json').write_text(json.dumps(json_value(dict(
 scope='Specified local profiles; no assertion they cover all actual inputs.',cases=cases)),indent=2)+'\n')
