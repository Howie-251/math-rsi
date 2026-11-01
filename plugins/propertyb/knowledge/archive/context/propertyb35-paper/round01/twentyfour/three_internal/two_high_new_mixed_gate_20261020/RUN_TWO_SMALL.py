"""Fresh complete necessary P-inventory pass with the seven-positive/two-small/one-triple gate; no H enumeration."""
from collections import Counter
from itertools import combinations, combinations_with_replacement, permutations
from pathlib import Path
import json
import time

HERE=Path(__file__).resolve().parent
PAIRS=tuple(combinations(range(7),2))
IX={e:i for i,e in enumerate(PAIRS)}
ST=time.perf_counter()

def gate(m4,m3,t,b):
    if m4+m3<=7 and m3<=2 and t<=1:return 'new_seven_mixed_two_small_one_T'
    if m4+m3==0:return 'empty'
    if m4+m3<=4 and t<=3:return 'four_small_3T'
    if m4+m3<=5 and t<=2:return 'five_small_2T'
    if m3==0:
        if m4<=5 and t<=10 and b<=32:return 'five_four_10T'
        if m4<=6 and t<=6 and b<=35:return 'six_four_6T'
        if m4<=7 and t<=4 and b<=22:return 'seven_four_4T'
        if m4==8 and ((t<=4 and b<=17) or (t<=3 and b<=20)):
            return 'eight_four'
    if m3<=1 and m4+m3<=7 and ((t==0 and b<=21) or (t<=1 and b<=20)):
        return 'seven_mixed'
    if m4==7 and m3==1 and t==0 and b<=20:return 'eight_mixed_18'
    return None

def graphs(n):
    out=[]
    for inds in combinations_with_replacement(range(21),n):
        g=[0]*21;d=[0]*7;mask=0
        for k in inds:
            g[k]+=1;mask|=1<<k
            u,v=PAIRS[k];d[u]+=1;d[v]+=1
        out.append((tuple(g),tuple(d),mask))
    return out

J={n:graphs(n) for n in (3,4,5)}
shapes=[('P3+K2',((0,1),(1,2),(3,4))),
        ('3K2',((0,1),(2,3),(4,5)))]
rows=[]
stop=None
for name,F in shapes:
    F=frozenset(F);D=sorted(set().union(*map(set,F)));C=sorted(set(range(7))-set(D))
    c=[3-sum(v in e for e in F) for v in range(7)]
    autos=[]
    for per in permutations(D):
        p=dict(zip(D,per))
        if frozenset(tuple(sorted((p[u],p[v]))) for u,v in F)==F:autos.append(p)
    traces=[tuple(t) for n in (3,4) for t in combinations(D,n)]
    allhigh=list(combinations_with_replacement(traces,2))
    def image(T,p):return tuple(sorted(tuple(sorted(p[v] for v in t)) for t in T))
    representatives=sorted({min(image(T,p) for p in autos) for T in allhigh})
    for T in representatives:
        n2=11-sum(map(len,T));n1=30-n2
        h=[sum(v in t for t in T) for v in range(7)]
        weight=[sum(len(t)-1 for t in T if v in t) for v in range(7)]
        cap=[min(8-c[v]-h[v],15-4*c[v]-weight[v]) for v in range(7)]
        required=0
        for k,(u,v) in enumerate(PAIRS):
            covered=any(u not in e and v not in e for e in F) or any(u in t and v in t for t in T)
            if not covered:required|=1<<k
        eligible=[(i,j,k) for k,(i,j) in enumerate(PAIRS)
                  if (i,j) not in F and all(i in t or j in t for t in T)]
        count=Counter();legal=0
        for g,d,mask in J[n2]:
            if required&mask != required or any(x>y for x,y in zip(d,cap)):continue
            legal+=1
            witness=None
            for i,j,k in eligible:
                s=d[i]+d[j];m4=16-c[i]-c[j]-h[i]-h[j]-s
                m3=g[k];t=n2-s+m3;b=n1-m4
                assert min(m4,m3,t,b)>=0
                which=gate(m4,m3,t,b)
                if which:
                    witness=(which,(i,j),m4,m3,t,b)
                    break
            if witness:count[witness[0]]+=1
            else:
                stop={'missing_shape':name,'missing_pairs':sorted(F),'C':C,'D':D,
                      'high_traces':T,'internal_degrees':c,'high_trace_degrees':h,
                      'J':[{ 'pair':PAIRS[k], 'multiplicity':v} for k,v in enumerate(g) if v],
                      'J_degrees':d,'single_trace_counts':[8-c[v]-h[v]-d[v] for v in range(7)],
                      'n2':n2,'n1':n1,'required_J_pairs':[PAIRS[k] for k in range(21) if required>>k&1],
                      'all_proper_high_hitting_blue_pairs':[]}
                for i,j,k in eligible:
                    s=d[i]+d[j];m4=16-c[i]-c[j]-h[i]-h[j]-s
                    m3=g[k];t=n2-s+m3;b=n1-m4
                    stop['all_proper_high_hitting_blue_pairs'].append({
                        'blue':(i,j),'m4':m4,'m3':m3,'T':t,'B':b})
                break
        rows.append({'missing_shape':name,'high_traces':T,'n2':n2,
                     'necessary_inventories_checked':legal,'successful_gate_counts':dict(count),
                     'high_orbit_finished':stop is None,
                     'number_high_orbit_representatives_for_this_shape':len(representatives)})
        if stop:break
    if stop:break
    if time.perf_counter()-ST>180:break

complete = stop is None and all(
    len([r for r in rows if r['missing_shape']==name]) == expected
    and all(r['high_orbit_finished'] for r in rows if r['missing_shape']==name)
    for name,expected in [('P3+K2',49),('3K2',34)])
if complete:
    assert sum(r['necessary_inventories_checked'] for r in rows)==1249695
    assert all(sum(r['successful_gate_counts'].values())==r['necessary_inventories_checked'] for r in rows)
result={'scope':__doc__,'read_original_pilot':True,
        'original_pilot_scope':'Read source logic and prior first failure; no old numerical output is used as a result of this run.',
        'new_gate_source':'proofs/propertyb35/SEVEN_MIXED_TWO_SMALL_ONE_TRIPLE_REPAIR.md',
        'used_four_small_zero_triple_extension':False,'status':'FIRST_NONGATED_NECESSARY_INVENTORY' if stop else 'BOUNDED_PROFILE',
        'complete_for_both_missing_shapes':complete,
        'graph_label_counts':{str(n):len(v) for n,v in J.items()},
        'completed_rows':rows,'first_nongated':stop,'seconds':time.perf_counter()-ST}
if complete:result['status']='COMPLETE_NECESSARY_P_DOMAIN_PASS'
(HERE/'RUN_TWO_SMALL.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps({k:v for k,v in result.items() if k!='completed_rows'},indent=2))
