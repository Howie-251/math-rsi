from pathlib import Path
from fractions import Fraction as F
import json,subprocess,time,resource
P=Path(__file__).resolve().parent;st=time.process_time();cs=resource.getrusage(resource.RUSAGE_CHILDREN)
old=json.loads((P.parent/'a1_independent_set_degree_prefix_20261020/SIMPLE_CHAIN_RESULT.json').read_text());rows=old['profiles'];assert len(rows)==25
keys=sorted({(r['e'],r['n'][4]) for r in rows});assert len(keys)==19
out=[];bounds={}
for e,t in keys:
 a=json.loads(subprocess.check_output(['/tmp/middle_min3_dp',str(e),str(t)],text=True));b=json.loads(subprocess.check_output(['/tmp/middle_min3_frequency',str(e),str(t)],text=True));assert a['bound']==b['bound']
 q=a['q'];assert len(q)==35 and min(q)>=3 and q==sorted(q,reverse=True) and sum(q)==2*e
 def f(s):x,y=divmod(s,5);return (s*s-(5-y)*x*x-y*(x+1)**2)//2
 assert sum(f(34-x) for x in q)==a['bound']
 bounds[e,t]=a['bound'];out.append({'primary':a,'frequency':b})
alloc=[]
for row in rows:
 n=row['n'];D=bounds[row['e'],n[4]];B=F(min(D,F(row['modes'][0]['P_bound'])));caps=[33*n[0],26*n[1]+339,24*n[2],13*n[3],4*n[4]];C=[F(0)]*5
 for k in range(4,-1,-1):C[k]=min(B,caps[k]);B-=C[k]
 L=sum(x*w for x,w in zip(C,(36,120,330,792,1716)))/2+3432*n[1]
 alloc.append({'n':n,'tau':row['tau'],'min3_DP_bound':D,'C':list(map(str,C)),'L':str(L),'survives':L>=2722720})
ce=resource.getrusage(resource.RUSAGE_CHILDREN);cpu=time.process_time()-st+ce.ru_utime+ce.ru_stime-cs.ru_utime-cs.ru_stime
j={'status':'PASS_LOCAL_DIAGNOSTIC','scope':'copies of existing twoDPs changedonlyqmin3; conditional on newdirectgate proof acceptance;not replacement of reviewedSIMPLE_CHAIN','keys':19,'profiles':25,'records':out,'allocations':alloc,'survivors':sum(x['survives'] for x in alloc),'max_L':max(alloc,key=lambda x:F(x['L'])),'cpu_seconds':cpu};(P/'MIN3_RESULT.json').write_text(json.dumps(j,indent=2)+'\n');print({k:v for k,v in j.items() if k not in ('records','allocations')})
