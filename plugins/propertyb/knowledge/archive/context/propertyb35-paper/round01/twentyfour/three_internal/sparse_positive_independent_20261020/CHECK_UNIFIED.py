"""All feasible r,s sparse signatures: scalar Fraction formulas only, no set-system domain."""
from pathlib import Path
from fractions import Fraction as Q
import json

q,p,z,w=Q(1,4),Q(7,16),Q(37,64),Q(175,256)
A2=(p*p-q*q)/2;A3=(p**3-q**3)/3;A4=(p**3*q-q**4)/3
assert A2>A3>A4>0
records=[];probability_profiles=0
for R in range(5):
    for S in range(4):
        T=9-2*R-S;B=18+R+S
        if T<0:continue
        base=R*q*q+T*q**3+B*q**4
        bounds={}
        if S<=2:
            bounds['none']=base
            bounds['one2']=R*p*q+T*p*q*q+B*p*q**3
        if S<=1:
            bounds['one3']=R*z*q+T*z*q*q+B*z*q**3
            pair=(p*p+(R-1)*p*q) if R else Q()
            bounds['two2']=pair+T*p*p*q+B*p*p*q*q
        if S==0:
            bounds['one4']=min(R,3)*w*q+max(R-3,0)*q*q+T*w*q*q+B*w*q**3
            j2=min(2*R,15);j3=min(3*T,15-j2);j4=15-j2-j3
            resource=max(i*A2+j*A3+k*A4 for i in range(2*R+1)
                         for j in range(3*T+1) for k in range(16)
                         if i+j+k<=15)
            assert resource==j2*A2+j3*A3+j4*A4
            bounds['three2']=base+resource
            cross=max(i+j*q+k*q*q for i in range(min(R,1)+1)
                      for j in range(T+1) for k in range(5) if i+j+k<=4)
            expected_cross=(1+min(T,3)*q+max(3-T,0)*q*q) if R else (min(T,4)*q+max(4-T,0)*q*q)
            assert cross==expected_cross
            bounds['one3_one2']=base+4*q*(z-q)+5*q*(p-q)+(z-q)*(p-q)*cross
        if S==3:
            bounds={'two_disjoint_positive_sets':Q(R,16)}
        assert max(bounds.values())<1
        probability_profiles += len(bounds) if S<3 else 0
        records.append(dict(r=R,s=S,positive_four_count=5-S,positive_union_minimum=17-3*S,
                            negative_pairs=R,negative_triples=T,negative_fours=B,
                            exact_bounds={k:str(v) for k,v in bounds.items()}))
assert len(records)==18 and probability_profiles==63
worst=max((Q(v),r['r'],r['s'],k) for r in records for k,v in r['exact_bounds'].items())
assert worst==(Q(8181,8192),4,0,'one3_one2')
by_s={}
for S in range(4):
    subset=[r for r in records if r['s']==S]
    by_s[S]={k:str(max(Q(r['exact_bounds'][k]) for r in subset)) for k in subset[0]['exact_bounds']}
result=dict(PASS=True,feasible_r_s_cases=18,probability_profiles=63,
            two_disjoint_integer_cases=4,all_profiles=records,maxima_by_s=by_s,
            global_worst=str(worst[0]),worst_case={'r':worst[1],'s':worst[2],'profile':worst[3]},
            scope=__doc__)
(Path(__file__).resolve().parent/'UNIFIED_CHECK.json').write_text(json.dumps(result,indent=2)+'\n')
print({k:v for k,v in result.items() if k not in ('all_profiles','scope')})
