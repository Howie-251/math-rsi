"""Only integer trace budgets and proved repair-gate interfaces; no P-source/H enumeration."""
import json
from pathlib import Path

HERE=Path(__file__).resolve().parent
def gate(m,t,b):
    if m<=5 and t+b<=35:return 'FIVE_TOTAL35'
    if m==6 and t<=6 and b<=35:return 'SIX_6T35B'
    if m==7 and t<=4 and b<=35:return 'SEVEN_4T35B'
    if m==8 and ((t<=3 and b<=20) or (t<=4 and b<=17)):
        return 'EIGHT_L17_3T20B_OR_4T17B'
    if m==9 and t<=3:return 'NINE_3T_ANY_B'
    if m==10 and t<=2:return 'TEN_2T_ANY_B'
    if m==11 and t==0 and b<=17:return 'ELEVEN_0T17B'
    return None

rows=[]
for I in (1,2):
    excess=21-4*I
    for n4 in range(excess//3+1):
        for n3 in range((excess-3*n4)//2+1):
            n2=excess-2*n3-3*n4
            n1=14+3*I+n3+2*n4
            bad=I+6*n3+3*n4+n2
            mmax=min(n1,16-I-n3-n4)
            interfaces=[dict(m=m,t=n2,b=n1-m,gate=gate(m,n2,n1-m)) for m in range(mmax+1)]
            complete=bad<21 and all(r['gate'] for r in interfaces)
            rows.append(dict(I=I,inventory=[n2,n3,n4],n1=n1,bad_pair_bound=bad,mmax=mmax,
                pair_guaranteed=bad<21,uniform_gate_complete=complete,
                unsupported_m=[r['m'] for r in interfaces if not r['gate']],interfaces=interfaces))
result=dict(scope=__doc__,total_inventory_count=len(rows),by_I={str(I):sum(x['I']==I for x in rows) for I in (1,2)},
            complete_by_I={str(I):[x['inventory'] for x in rows if x['I']==I and x['uniform_gate_complete']] for I in (1,2)},rows=rows)
(HERE/'SHORT_CRITERION_SCALARS.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps({k:v for k,v in result.items() if k!='rows'},indent=2))
