from pathlib import Path
from math import comb
from fractions import Fraction
import json,subprocess,time,resource
P=Path(__file__).resolve().parent
Q=P.parent/'a2_a3_joint_moment_frontier_20261020'
start=time.monotonic();cpu_start=time.process_time();child_start=resource.getrusage(resource.RUSAGE_CHILDREN)
rows=[z for z in json.loads((Q/'RESIEVE_SURVIVORS.json').read_text()) if z['n'][4]<=13];assert len(rows)==6953
remaining=json.loads((Q/'CONDITIONAL_CRITICAL_SURVIVORS.json').read_text());assert len(remaining)==5813
T=json.loads((Q/'THRESHOLD_TABLE.json').read_text())
def params(z):
 ds=sorted(map(int,z['unique_degree_key'].split(',')))
 return (sum(comb(d,2) for d in ds),sum(ds[:5]),595-z['n'][1],z['n'][4])
first=[z for z in rows if params(z)==(655,35,78,10)];assert len(first)==1
selected=[('required witness',first[0])]
selected.append(('closest surviving critical-box witness',min(remaining,key=lambda z:(z['margin'],params(z)))))
selected.append(('largest surviving objective margin',max(remaining,key=lambda z:(z['margin'],params(z)))))
selected.append(('largest E; then largest margin',max(remaining,key=lambda z:(595-z['n'][1],z['margin'],params(z)))))
selected.append(('largest margin among W=657',max((z for z in remaining if params(z)[0]==657),key=lambda z:(z['margin'],params(z)))))
assert len({params(z) for _,z in selected})==5

def f(s):
 groups=[s//5+(j<s%5) for j in range(5)]
 return sum(groups[i]*groups[j] for i in range(5) for j in range(i))
def ceil_frac(a,b):return -(-a//b)
def independent_caps(W,S,E,t):
 out=[]
 for k in range(1,14):
  N=35-k;Wp=min(W,W-k*(S-5)+4*comb(k,2));tr=Wp-comb(N,2)
  R=ceil_frac(152*N*(N-21)-273*tr,882)
  B=max(0,R-2*t,ceil_frac(152*N*(N-21)-2037*t,1428))
  out.append(E+comb(k,2)-B)
 return out
out=[]
for reason,z in selected:
 W,S,E,t=params(z)
 dp=json.loads(subprocess.check_output([str(P/'prefix_dp'),str(W),str(S),str(E),str(t)],text=True,timeout=5))
 assert dp['caps']==independent_caps(W,S,E,t)
 seq=dp['maximizer_q'];assert len(seq)==35 and seq==sorted(seq,reverse=True) and min(seq)>=3 and max(seq)<=29 and sum(seq)==2*E
 assert all(sum(seq[:k])<=dp['caps'][k-1] for k in range(1,14))
 assert sum(f(34-q) for q in seq)==dp['maxP']==dp['frequency_maxP']
 mass=2*z['n'][1];a,b=divmod(mass-175,26);box=a*f(31)+(f(5+b)+(34-a)*f(5) if a<35 else 0)
 assert dp['maxP']<=box
 threshold=T[str(z['n'][1])] if isinstance(T,dict) else T[z['n'][1]]
 assert threshold==z['old_P']
 budget=min(threshold,z['P'],box,dp['maxP']);C=[0]*5;left=budget
 for j in range(4,-1,-1):C[j]=min(left,z['C_caps'][j]);left-=C[j]
 L2=sum(c*w for c,w in zip(C,(36,120,330,792,1716)))+6864*z['n'][1]
 oldbudget=min(threshold,z['P'],box);oldC=[0]*5;left=oldbudget
 for j in range(4,-1,-1):oldC[j]=min(left,z['C_caps'][j]);left-=oldC[j]
 oldL2=sum(c*w for c,w in zip(oldC,(36,120,330,792,1716)))+6864*z['n'][1]
 out.append({'selection_reason':reason,'actual_saved_moment_row':z,'DP':dp,'threshold_T':threshold,'critical_box_cap':box,'old_critical_budget':oldbudget,'new_budget':budget,'C':C,'L':str(Fraction(L2,2)),'margin':str(Fraction(L2-5445440,2)),'old_critical_L':str(Fraction(oldL2,2)),'strictly_below_threshold':L2<5445440,'box_to_prefix_drop':box-dp['maxP']})
endchild=resource.getrusage(resource.RUSAGE_CHILDREN)
res={'scope':'Five exact degree-sequence relaxation pilots only; conditional t<=13 frontier. No original H realization, no full frontier re-sieve, no A1 extra constraints. q<=29 uses separate old <=34 low-degree local import; min q>=3 uses new theorem.', 'source_rows_t_le_13':6953,'critical_box_survivor_rows':5813,'pilot_count':len(out),'strictly_below_threshold_count':sum(z['strictly_below_threshold'] for z in out),'records':out,'budget':{'limit_cpu_seconds':20,'limit_wall_seconds':300,'pilot_script_cpu_seconds':time.process_time()-cpu_start,'child_cpu_seconds':endchild.ru_utime+endchild.ru_stime-child_start.ru_utime-child_start.ru_stime,'wall_seconds':time.monotonic()-start,'compile_wall_seconds_observed':1.501665417,'note':'CPU is measured for pilot runs; compiler execution was separate and wall under 1.51 seconds. No bulk DP was run.'}}
assert res['budget']['child_cpu_seconds']+res['budget']['pilot_script_cpu_seconds']<20
(P/'RESULT.json').write_text(json.dumps(res,indent=2)+'\n')
for z in out:print(z['selection_reason'],tuple(z['DP'][k] for k in ['W','S5','E','t']),'P',z['DP']['maxP'],'box',z['critical_box_cap'],'T',z['threshold_T'],'drop',z['box_to_prefix_drop'],'L',z['L'],'margin',z['margin'],'strict',z['strictly_below_threshold'])
print(res['budget'])
